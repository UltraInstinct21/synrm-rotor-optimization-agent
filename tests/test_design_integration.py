import tempfile
import unittest
from unittest.mock import patch

from agent.graph import initial_state
from agent.nodes.design import design_node
from agent.tools.rotor import default_barrier_params


class DesignIntegrationTests(unittest.TestCase):
    def test_design_invokes_optimization_with_valid_barrier_params(self):
        state = initial_state()
        state["phase_status"] = {}
        state["barrier_params"] = default_barrier_params()

        with tempfile.NamedTemporaryFile("w", suffix=".mot", delete=False) as f:
            f.write("[Header]\nFoo=Bar\n")
            state["mot_file_path"] = f.name

        fake_result = {
            "optimization_results": [{"iteration": 0, "score": 0.1}],
            "best_model_path": "best.mot",
        }
        with patch("agent.nodes.design.launch_motorcad", return_value=None), patch(
            "agent.nodes.design.optimization_sub_node", return_value=fake_result
        ) as optimization:
            result = design_node(state)

        optimization.assert_called_once()
        called_state = optimization.call_args.args[0]
        self.assertEqual(called_state["barrier_params"], default_barrier_params())
        self.assertEqual(result["optimization_results"], fake_result["optimization_results"])
        self.assertEqual(result["best_model_path"], "best.mot")
        self.assertEqual(result["phase_status"]["design"]["status"], "done")


if __name__ == "__main__":
    unittest.main()
