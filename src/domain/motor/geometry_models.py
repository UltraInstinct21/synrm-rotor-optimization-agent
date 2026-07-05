"""Motor geometry Pydantic models — stator, rotor, winding, and rating specs."""

from __future__ import annotations

from pydantic import BaseModel, Field


class StatorGeometry(BaseModel):
    """Stator geometric parameters."""

    outer_diameter_mm: float = Field(default=250.0, ge=50, le=1000)
    inner_diameter_mm: float = Field(default=160.0, ge=30, le=900)
    core_length_mm: float = Field(default=200.0, ge=10, le=1000)
    number_of_slots: int = Field(default=48, ge=12, le=144)
    slot_type: str = Field(default="rectangular", description="Slot geometry type")


class RotorGeometry(BaseModel):
    """Rotor geometric parameters — barrier layout for SynRM/PMaSynRM."""

    outer_diameter_mm: float = Field(default=159.0, ge=20, le=900)
    inner_diameter_mm: float = Field(default=50.0, ge=10, le=500)
    shaft_diameter_mm: float = Field(default=40.0, ge=10, le=300)
    airgap_mm: float = Field(default=0.5, ge=0.2, le=5.0)
    barrier_layers: int = Field(default=4, ge=2, le=8)
    barrier_angles_deg: list[float] | None = Field(
        default=None,
        description="Angular positions of flux barriers in degrees",
    )


class WindingConfig(BaseModel):
    """Winding parameters."""

    turns_per_coil: int = Field(default=8, ge=1, le=100)
    parallel_paths: int = Field(default=2, ge=1, le=8)
    number_of_layers: int = Field(default=2, ge=1, le=4)
    coil_pitch: int = Field(default=8, ge=1, le=48)
    fill_factor: float = Field(default=0.45, ge=0.2, le=0.8)
    wire_diameter_mm: float = Field(default=1.0, ge=0.1, le=5.0)


class RatingConfig(BaseModel):
    """Motor rating / operating point."""

    power_kw: float = Field(default=45.0, ge=0.1, le=10000)
    speed_rpm: float = Field(default=3000.0, ge=1, le=50000)
    voltage_v: float = Field(default=400.0, ge=10, le=10000)
    current_a: float | None = Field(default=None, ge=0)
    frequency_hz: float | None = Field(default=None, ge=0)
    dc_bus_voltage_v: float = Field(default=560.0, ge=10, le=10000)

    @property
    def torque_nm(self) -> float:
        """Rated torque: T = P / ω."""
        import math

        omega = self.speed_rpm * (2 * math.pi / 60)
        return (self.power_kw * 1000) / omega if omega > 0 else 0.0


class MotorDesign(BaseModel):
    """Complete motor design — geometry + winding + rating."""

    name: str = Field(default="SynRM_Design")
    machine_type: str = Field(default="SynRM", pattern="^(SynRM|PMaSynRM|IM|PMSM)$")
    stator: StatorGeometry = Field(default_factory=StatorGeometry)
    rotor: RotorGeometry = Field(default_factory=RotorGeometry)
    winding: WindingConfig = Field(default_factory=WindingConfig)
    rating: RatingConfig = Field(default_factory=RatingConfig)
