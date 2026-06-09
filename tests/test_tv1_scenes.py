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
        "tokens": [
            "TARGET_DURATION_SECONDS = 80",
            "MathTex(",
            "Text(",
            "99.1",
            "Dashboard đẹp",
            "Nếu 99.1% là đúng",
            r"P_{\mathrm{train}}",
            r"P_{\mathrm{deploy}}",
            "Test accuracy cao",
            "đáng tin ngoài đời",
        ],
    },
    "scene_02_failure_montage.py": {
        "class": "FailureMontageScene",
        "tokens": ["robot", "camera", "hospital", "car", "Điều gì đã đổi?"],
    },
    "scene_03_model_or_data.py": {
        "class": "ModelOrDataScene",
        "tokens": ["Lỗi model?", "Lỗi dữ liệu?", "nguồn dữ liệu", "nhóm ẩn", "cơ chế", "shifts"],
    },
    "scene_04_iid_box.py": {
        "class": "IIDBoxScene",
        "tokens": ["MathTex(", "P(X,Y)", r"P_{\mathrm{train}}", r"P_{\mathrm{test}}", "i.i.d.", "cùng một phân phối sinh dữ liệu"],
    },
    "scene_05_train_test_split.py": {
        "class": "TrainTestSplitScene",
        "tokens": ["MathTex(", r"P_{\mathrm{train}}", r"P_{\mathrm{target}}", "96.4", "69.2", "Distribution shift bắt đầu"],
    },
    "scene_06_shift_taxonomy.py": {
        "class": "ShiftTaxonomyScene",
        "tokens": ["X-shift", "Label shift", "Y|X-shift", "Distribution Shift", "Cần robust với shift nào?"],
    },
    "scene_07_x_shift.py": {
        "class": "XShiftScene",
        "tokens": ["MathTex(", "P(X)", "Q(X)", "rule dự đoán", "X-shift đổi nơi dữ liệu xuất hiện"],
    },
    "scene_08_yx_shift.py": {
        "class": "YXShiftScene",
        "tokens": ["MathTex(", "P(Y|X)", "Cơ chế source", "ranh giới dự đoán", "Y|X-shift đổi ý nghĩa"],
    },
    "scene_09_data_sources.py": {
        "class": "DataSourcesScene",
        "tokens": ["Nguồn A", "Nguồn B", "Nguồn C", "Nguồn D", "hỗn hợp"],
    },
    "scene_10_pooled_illusion.py": {
        "class": "PooledIllusionScene",
        "tokens": ["dataset gộp", "Các cụm màu", "Bệnh viện A", "Bệnh viện B", "Bệnh viện C"],
    },
}


TV1_TARGET_DURATIONS = {
    "scene_01_accuracy_fail.py": 80,
    "scene_02_failure_montage.py": 70,
    "scene_03_model_or_data.py": 70,
    "scene_04_iid_box.py": 80,
    "scene_05_train_test_split.py": 75,
    "scene_06_shift_taxonomy.py": 70,
    "scene_07_x_shift.py": 75,
    "scene_08_yx_shift.py": 80,
    "scene_09_data_sources.py": 70,
    "scene_10_pooled_illusion.py": 75,
}


TV1_ANIMATION_SIGNATURES = {
    "scene_02_failure_montage.py": ["Flash(", "Indicate("],
    "scene_03_model_or_data.py": ["Circumscribe(", "ApplyWave("],
    "scene_04_iid_box.py": ["MoveAlongPath(", "TracedPath("],
    "scene_05_train_test_split.py": ["MoveAlongPath(", "Flash("],
    "scene_06_shift_taxonomy.py": ["Circumscribe(", "Indicate("],
    "scene_07_x_shift.py": ["TransformFromCopy(", "Indicate("],
    "scene_08_yx_shift.py": ["Rotate(", "Circumscribe("],
    "scene_09_data_sources.py": ["MoveAlongPath(", "TransformFromCopy("],
    "scene_10_pooled_illusion.py": ["MoveAlongPath(", "Transform("],
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

    def test_each_scene_declares_script_duration_target(self):
        for filename in self.scene_specs():
            with self.subTest(filename=filename):
                source = self.source(filename)
                target = TV1_TARGET_DURATIONS[filename]
                self.assertIn(f"TARGET_DURATION_SECONDS = {target}", source)

    def test_each_scene_after_intro_has_animation_signature(self):
        for filename in self.scene_specs():
            if filename == "scene_01_accuracy_fail.py":
                continue
            with self.subTest(filename=filename):
                source = self.source(filename)
                for token in TV1_ANIMATION_SIGNATURES[filename]:
                    self.assertIn(token, source)

    def test_each_scene_uses_manim_animation_primitives(self):
        required_any = ("FadeIn", "Write", "Create", "Transform", "LaggedStart")
        for filename in self.scene_specs():
            with self.subTest(filename=filename):
                source = self.source(filename)
                self.assertIn("setup_dark_scene(self)", source)
                if filename != "scene_01_accuracy_fail.py":
                    self.assertIn("animate_title_card", source)
                self.assertGreaterEqual(source.count("self.play"), 3)
                self.assertTrue(any(name in source for name in required_any))


if __name__ == "__main__":
    unittest.main()
