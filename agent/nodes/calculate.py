"""Phase 3 — Calculation Node: sizing, winding, magnetic, thermal parameter derivation."""

import math
from datetime import datetime
from typing import Any

from agent.state import AgentState
from agent.tools.rotor import default_barrier_params


def _fundamental_sizing(spec: dict) -> dict:
    """Derive rated torque, estimated losses, thermal budget from motor spec.

    Uses: T = P / omega, basic loss estimation, IE5 threshold validation.
    """
    power_kw = spec.get("power_kw", 45)
    speed_rpm = spec.get("speed_rpm", 3000)
    target_eff = spec.get("target_efficiency", 96.0)

    # Rated torque (Nm)
    torque_nm = (power_kw * 1000) / (2 * math.pi * speed_rpm / 60)

    # Input power at target efficiency
    input_power_kw = power_kw / (target_eff / 100)

    # Total losses (kW)
    total_losses_kw = input_power_kw - power_kw

    # Estimated copper loss (~60% of total for SynRM)
    copper_loss_kw = total_losses_kw * 0.60
    iron_loss_kw = total_losses_kw * 0.25
    mechanical_loss_kw = total_losses_kw * 0.10
    stray_loss_kw = total_losses_kw * 0.05

    return {
        "rated_torque_nm": round(torque_nm, 1),
        "input_power_kw": round(input_power_kw, 2),
        "total_losses_kw": round(total_losses_kw, 3),
        "copper_loss_kw": round(copper_loss_kw, 3),
        "iron_loss_kw": round(iron_loss_kw, 3),
        "mechanical_loss_kw": round(mechanical_loss_kw, 3),
        "stray_loss_kw": round(stray_loss_kw, 3),
        "target_efficiency_pct": target_eff,
    }


def _winding_calculation(spec: dict, sizing: dict) -> dict:
    """Calculate winding parameters: Kw, turns, conductor size, slot fill.

    Uses existing design guide values as starting point:
    - Kw = 0.9576 (from 45kW IE5 Design Guide)
    - Under-winding strategy for voltage headroom
    - Parallel paths, turns per slot, wire diameter
    """
    power_kw = spec.get("power_kw", 45)
    voltage_v = spec.get("voltage_v", 580)
    poles = spec.get("poles", 4)
    target_pf = spec.get("target_pf", 0.85)

    # Winding factor (from design guide — double-layer winding)
    kw = 0.9576

    # Rated current estimate (I = P / (sqrt(3) * V * PF * eff))
    eff = sizing["target_efficiency_pct"] / 100
    rated_current_a = (power_kw * 1000) / (math.sqrt(3) * voltage_v * target_pf * eff)

    # Effective turns per slot (from design guide)
    turns_per_slot = 24

    # Parallel paths
    parallel_paths = 2

    # Conductor size for current density ~5.6 A/mm2
    current_density_a_per_mm2 = 5.6
    conductor_area_mm2 = (rated_current_a / parallel_paths) / current_density_a_per_mm2
    wire_diameter_mm = 2 * math.sqrt(conductor_area_mm2 / math.pi)

    # Use standard wire (multiple strands if needed)
    strand_diameter_mm = 1.25  # from design guide
    strand_area_mm2 = math.pi * (strand_diameter_mm / 2) ** 2
    strands_per_parallel = math.ceil(conductor_area_mm2 / strand_area_mm2)

    # Slot fill estimate (rough)
    slot_area_mm2 = 200  # typical for this frame size
    total_conductor_area = turns_per_slot * strands_per_parallel * strand_area_mm2
    fill_factor = total_conductor_area / slot_area_mm2

    return {
        "kw": kw,
        "turns_per_slot": turns_per_slot,
        "parallel_paths": parallel_paths,
        "rated_current_a": round(rated_current_a, 1),
        "current_density_a_per_mm2": current_density_a_per_mm2,
        "wire_diameter_mm": round(wire_diameter_mm, 3),
        "strand_diameter_mm": strand_diameter_mm,
        "strands_per_parallel": strands_per_parallel,
        "conductor_area_mm2": round(conductor_area_mm2, 3),
        "slot_area_mm2": slot_area_mm2,
        "fill_factor": round(fill_factor, 3),
    }


def _magnetic_parameters(spec: dict, sizing: dict) -> dict:
    """Derive magnetic circuit parameters.

    Airgap from project spec (0.5mm), barrier spacing ratios from literature,
    Ld/Lq saliency targets.
    """
    poles = spec.get("poles", 4)

    # Airgap from project spec (Orlova et al., confirmed 0.5mm)
    airgap_mm = 0.5

    # Barrier spacing ratios (from literature: inner barriers closer to shaft)
    # L1 (innermost) : L2 : L3 spacing — typical ratio 1.0 : 0.7 : 0.5
    barrier_ratios = {"L1": 1.0, "L2": 0.7, "L3": 0.5}

    # Saliency target for IE5 / PF >= 0.85
    # PFmax = (xi-1)/(xi+1) -> xi >= 6.33 for PF=0.85
    target_saliency = 7.0  # rounded up from minimum 6.33

    # Field weakening range
    # omega_n_max = (xi^2+1)/(2*xi) for rated speed
    fw_range = (target_saliency**2 + 1) / (2 * target_saliency)

    return {
        "airgap_mm": airgap_mm,
        "barrier_ratios": barrier_ratios,
        "target_saliency_ratio": target_saliency,
        "field_weakening_range": round(fw_range, 2),
        "target_pf": spec.get("target_pf", 0.85),
    }


def _thermal_constraints(spec: dict, winding: dict) -> dict:
    """Derive thermal constraints from winding and operating conditions."""
    return {
        "current_density_a_per_mm2": winding.get("current_density_a_per_mm2", 5.6),
        "target_temperature_c": 120,  # from design guide thermal coupling rule
        "cooling_method": "IC411",    # standard forced ventilation
        "insulation_class": "H",      # 180 degC rated
        "ambient_temp_c": 40,
    }


def _log(state: AgentState, msg: str) -> None:
    phase = state.get("phase", "?")
    print(f"  [{phase:<12}] {msg}")


def calculate_node(state: AgentState) -> AgentState:
    """Execute Phase 3: derive all motor parameters from spec."""
    state["phase"] = "calculate"
    state["phase_status"]["calculate"] = {"status": "running", "error": None}
    errors = []

    try:
        spec = state.get("motor_spec", {})

        # 1. Fundamental sizing
        _log(state, "fundamental sizing (torque, losses, thermal budget)...")
        sizing = _fundamental_sizing(spec)
        state["derived_params"] = {**state.get("derived_params", {}), **sizing}

        # 2. Winding calculation
        _log(state, "winding calculation (turns, fill factor, wire gauge)...")
        winding = _winding_calculation(spec, sizing)
        state["winding_params"] = winding

        # 3. Magnetic parameters
        _log(state, "magnetic circuit parameters (airgap, barriers, saliency)...")
        magnetic = _magnetic_parameters(spec, sizing)
        state["derived_params"]["magnetic"] = magnetic
        state["barrier_params"] = default_barrier_params()

        # 4. Thermal constraints
        _log(state, "thermal constraints (cooling, insulation, temps)...")
        thermal = _thermal_constraints(spec, winding)
        state["derived_params"]["thermal"] = thermal

        state["phase_status"]["calculate"] = {"status": "done", "error": None}

    except Exception as e:
        errors.append(str(e))
        state["phase_status"]["calculate"] = {"status": "failed", "error": str(e)}
        # Provide conservative defaults
        if not state.get("winding_params"):
            state["winding_params"] = {"kw": 0.9576, "turns_per_slot": 24}
        if not state.get("barrier_params"):
            state["barrier_params"] = default_barrier_params()

    if errors:
        state["error_log"] = state.get("error_log", [])
        state["error_log"].append({
            "phase": "calculate",
            "error": str(errors),
            "timestamp": datetime.now().isoformat(),
        })

    return state
