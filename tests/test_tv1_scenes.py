"""Static tests for TV1 Manim scene implementations.

These tests avoid importing Manim so they can run in a lightweight CI/dev
environment. They assert that each scene has moved beyond placeholders and
contains the specific visual/content cues required by the script.
"""

from pathlib import Path
import ast
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCENES = ROOT / "src" / "scenes"


TV1_SCENES = {
    "scene_01_accuracy_fail.py": {
        "class": "AccuracyFailScene",
        "tokens": ["DecimalNumber", "99.1", "High test accuracy", "deployment reliability"],
    },
    "scene_02_failure_montage.py": {
        "class": "FailureMontageScene",
        "tokens": ["robot", "camera", "hospital", "car", "What changed?"],
    },
    "scene_03_model_or_data.py": {
        "class": "ModelOrDataScene",
        "tokens": ["Model problem?", "Data problem?", "sources", "subpopulations", "mechanisms", "shifts"],
    },
    "scene_04_iid_box.py": {
        "class": "IIDBoxScene",
        "tokens": ["P(X,Y)", "P_{train}", "P_{test}", "i.i.d.", "same data-generating distribution"],
    },
    "scene_05_train_test_split.py": {
        "class": "TrainTestSplitScene",
        "tokens": ["P_{train}", "P_{target}", "96.4", "69.2", "Distribution shift begins"],
    },
    "scene_06_shift_taxonomy.py": {
        "class": "ShiftTaxonomyScene",
        "tokens": ["X-shift", "Label shift", "Y|X-shift", "Distribution Shift", "Robust to what shift?"],
    },
    "scene_07_x_shift.py": {
        "class": "XShiftScene",
        "tokens": ["P(X)", "Q(X)", "decision rule", "X-shift changes where data appears"],
    },
    "scene_08_yx_shift.py": {
        "class": "YXShiftScene",
        "tokens": ["P(Y|X)", "mechanism", "decision boundary", "Y|X-shift changes what the data means"],
    },
    "scene_09_data_sources.py": {
        "class": "DataSourcesScene",
        "tokens": ["Source A", "Source B", "Source C", "Source D", "mixture"],
    },
    "scene_10_pooled_illusion.py": {
        "class": "PooledIllusionScene",
        "tokens": ["pooled dataset", "colored clusters", "Hospital A", "Hospital B", "Hospital C"],
    },
}


class TV1ScenesTest(unittest.TestCase):
    def scene_specs(self):
        selected = os.environ.get("TV1_SCENE")
        if selected:
            self.assertIn(selected, TV1_SCENES, f"Unknown TV1_SCENE={selected}")
            return {selected: TV1_SCENES[selected]}
        return TV1_SCENES

    def source(self, filename: str) -> str:
        path = SCENES / filename
        self.assertTrue(path.exists(), f"Missing scene file: {path}")
        return path.read_text(encoding="utf-8")

    def test_each_scene_has_expected_class_and_no_placeholder(self):
        for filename, spec in self.scene_specs().items():
            with self.subTest(filename=filename):
                source = self.source(filename)
                tree = ast.parse(source)
                class_names = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
                self.assertIn(spec["class"], class_names)
                self.assertNotIn("placeholder", source.lower())
                self.assertNotIn("TODO", source)

    def test_each_scene_contains_required_content_cues(self):
        for filename, spec in self.scene_specs().items():
            with self.subTest(filename=filename):
                source = self.source(filename)
                for token in spec["tokens"]:
                    self.assertIn(token, source)

    def test_each_scene_uses_manim_animation_primitives(self):
        required_any = ("FadeIn", "Write", "Create", "Transform", "LaggedStart")
        for filename in self.scene_specs():
            with self.subTest(filename=filename):
                source = self.source(filename)
                self.assertIn("setup_dark_scene(self)", source)
                self.assertIn("animate_title_card", source)
                self.assertGreaterEqual(source.count("self.play"), 3)
                self.assertTrue(any(name in source for name in required_any))


if __name__ == "__main__":
    unittest.main()
