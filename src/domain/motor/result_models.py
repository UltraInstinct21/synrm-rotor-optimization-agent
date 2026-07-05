"""Motor-CAD result models — typed representations of FEA output metrics."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ElectromagneticResult(BaseModel):
    """Results from Motor-CAD electromagnetic analysis."""

    torque_nm: float | None = Field(default=None, description="Average electromagnetic torque")
    efficiency_pct: float | None = Field(default=None, ge=0, le=100)
    power_factor: float | None = Field(default=None, ge=0, le=1)
    speed_rpm: float | None = Field(default=None)
    output_power_kw: float | None = Field(default=None)

    # Inductances
    ld_mh: float | None = Field(default=None, description="d-axis inductance in mH")
    lq_mh: float | None = Field(default=None, description="q-axis inductance in mH")
    saliency: float | None = Field(default=None, description="Lq/Ld ratio")

    # Losses
    iron_loss_w: float | None = Field(default=None)
    copper_loss_w: float | None = Field(default=None)
    magnet_loss_w: float | None = Field(default=None)
    mechanical_loss_w: float | None = Field(default=None)

    @property
    def total_loss_w(self) -> float | None:
        if all(v is not None for v in [self.iron_loss_w, self.copper_loss_w, self.mechanical_loss_w]):
            total = self.iron_loss_w + self.copper_loss_w + self.mechanical_loss_w
            if self.magnet_loss_w is not None:
                total += self.magnet_loss_w
            return total
        return None


class ComparisonResult(BaseModel):
    """Comparison across multiple candidate designs."""

    designs: dict[str, ElectromagneticResult] = Field(
        default_factory=dict,
        description="Design name → result mapping",
    )

    def best_by_metric(self, metric: str = "torque_nm") -> tuple[str, ElectromagneticResult]:
        """Return the (name, result) with the highest value for *metric*."""
        best_name = ""
        best_val = -float("inf")
        best_result = ElectromagneticResult()
        for name, res in self.designs.items():
            val = getattr(res, metric, None)
            if val is not None and val > best_val:
                best_val = val
                best_name = name
                best_result = res
        return best_name, best_result
