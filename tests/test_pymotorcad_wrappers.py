import unittest

from agent.tools import pymotorcad


class OfficialMotorCADFake:
    def __init__(self):
        self.values = {"ShaftTorque": 143.0, "L1_Diameter": 100.0}
        self.set_calls = []
        self.context_shown = False
        self.calculated = False
        self.saved_path = None

    def get_variable_names(self):
        return list(self.values)

    def get_variable(self, name):
        if name not in self.values:
            raise KeyError(name)
        return self.values[name]

    def set_variable(self, name, value):
        if name not in self.values:
            raise KeyError(name)
        self.set_calls.append((name, value))
        self.values[name] = value

    def show_magnetic_context(self):
        self.context_shown = True

    def do_magnetic_calculation(self):
        self.calculated = True

    def save_to_file(self, path):
        self.saved_path = path


class PyMotorCADWrapperTests(unittest.TestCase):
    def test_discover_variables_uses_official_api(self):
        mc = OfficialMotorCADFake()

        self.assertEqual(
            pymotorcad.discover_variables(mc, keyword="torque"),
            ["ShaftTorque"],
        )

    def test_safe_get_raises_clear_error_for_missing_variable(self):
        mc = OfficialMotorCADFake()

        with self.assertRaisesRegex(RuntimeError, "get_variable\\('Missing'\\) failed"):
            pymotorcad.safe_get(mc, "Missing")

    def test_safe_set_raises_clear_error_for_missing_variable(self):
        mc = OfficialMotorCADFake()

        with self.assertRaisesRegex(RuntimeError, "set_variable\\('Missing'"):
            pymotorcad.safe_set(mc, "Missing", 1)

    def test_safe_set_writes_official_api_value(self):
        mc = OfficialMotorCADFake()

        pymotorcad.safe_set(mc, "L1_Diameter", 101.5)

        self.assertEqual(mc.values["L1_Diameter"], 101.5)
        self.assertEqual(mc.set_calls, [("L1_Diameter", 101.5)])

    def test_run_emag_shows_context_before_calculation(self):
        mc = OfficialMotorCADFake()

        pymotorcad.run_emag(mc)

        self.assertTrue(mc.context_shown)
        self.assertTrue(mc.calculated)


if __name__ == "__main__":
    unittest.main()
