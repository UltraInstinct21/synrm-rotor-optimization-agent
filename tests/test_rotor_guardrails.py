import csv
import os
import tempfile
import unittest

from agent.tools import rotor


class RotorGuardrailTests(unittest.TestCase):
    def test_default_barrier_params_are_allowed_and_valid(self):
        params = rotor.default_barrier_params()

        self.assertEqual(set(params), set(rotor.ALLOWED_BARRIER_VARIABLES))
        self.assertTrue(rotor.check_geometry_constraints(params))

    def test_rejects_unknown_rotor_parameter(self):
        params = rotor.default_barrier_params()
        params["Airgap"] = 0.6

        with self.assertRaisesRegex(ValueError, "not allowed"):
            rotor.check_geometry_constraints(params)

    def test_rejects_invalid_diameter_order(self):
        params = rotor.default_barrier_params()
        params["L2_Diameter"] = params["L1_Diameter"] - 1

        with self.assertRaisesRegex(ValueError, "L1_Diameter < L2_Diameter"):
            rotor.check_geometry_constraints(params)

    def test_rejects_low_bridge_thickness(self):
        params = rotor.default_barrier_params()
        params["L3_Bridge_Thickness"] = 0.5

        with self.assertRaisesRegex(ValueError, "L3_Bridge_Thickness"):
            rotor.check_geometry_constraints(params)

    def test_objective_prefers_target_torque_and_efficiency(self):
        good = rotor.objective({"ShaftTorque": 143.0, "Efficiency": 96.5})
        bad = rotor.objective({"ShaftTorque": 120.0, "Efficiency": 94.0})

        self.assertLess(good, bad)

    def test_log_result_writes_csv_row_immediately(self):
        params = rotor.default_barrier_params()
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "results.csv")
            rotor.log_result(
                path,
                iteration=1,
                params=params,
                torque=143.0,
                input_power=46875.0,
                shaft_power=44924.8,
                efficiency=95.8,
                extra={"PowerFactor": 0.86},
            )

            with open(path, newline="", encoding="utf-8") as f:
                rows = list(csv.DictReader(f))

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["iteration"], "1")
        self.assertEqual(rows[0]["L1_Diameter"], "100")
        self.assertEqual(rows[0]["PowerFactor"], "0.86")


if __name__ == "__main__":
    unittest.main()
