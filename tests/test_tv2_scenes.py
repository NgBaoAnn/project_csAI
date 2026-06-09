"""Static tests for TV2 Manim scene implementations."""

from pathlib import Path
import ast
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCENES = ROOT / "src" / "scenes"


TV2_SCENES = {
    "scene_11_hidden_subpopulations.py": {
        "class": "HiddenSubpopulationsScene",
        "target": 80,
        "tokens": [
            "Subpopulations ẩn",
            r"P_A(Y\mid X)",
            "đường trung bình",
            "Nhóm A",
            "Nhóm B",
            "Một model trung bình có thể che giấu nhiều cơ chế.",
        ],
        "animations": ["Transform(", "ShowPassingFlash(", "residuals"],
    },
    "scene_12_pipeline_view.py": {
        "class": "PipelineViewScene",
        "target": 70,
        "tokens": [
            "Thu thập",
            "Training",
            "Đánh giá",
            "Deployment",
            "OOD generalization là cả một quy trình, không chỉ là một thuật toán.",
        ],
        "animations": ["MoveAlongPath(", "ShowPassingFlash(", "Circumscribe("],
    },
    "scene_13_erm_formula.py": {
        "class": "ERMFormulaScene",
        "target": 80,
        "tokens": [
            r"\arg\min_{\theta}",
            r"\frac{1}{n} \sum_{i=1}^{n}",
            r"\mathcal{L}(f_\theta(x_i),\, y_i)",
            "ERM tối ưu loss trung bình trên dữ liệu train.",
        ],
        "animations": ["Transform(", "ShowPassingFlash(", "ApplyWave("],
    },
    "scene_14_average_risk.py": {
        "class": "AverageRiskScene",
        "target": 70,
        "tokens": [
            "Nhóm lớn (85%)",
            "99%",
            "Nhóm nhỏ B (5%)",
            "43%",
            "Hiệu năng trung bình có thể che giấu lỗi cục bộ.",
        ],
        "animations": ["ChangeDecimalToValue(", "Flash(", "Indicate("],
    },
    "scene_15_spurious_cow_camel.py": {
        "class": "SpuriousCowCamelScene",
        "target": 80,
        "tokens": [
            "Bò",
            "Lạc đà",
            "ERM học background",
            "Shape là tín hiệu thật",
            "Spurious correlation: đúng trong train, sai khi môi trường đổi.",
        ],
        "animations": ["Indicate(", "Flash(", "MoveAlongPath("],
    },
    "scene_16_dro_intuition.py": {
        "class": "DROIntuitionScene",
        "target": 70,
        "tokens": [
            r"\min_{\theta}",
            r"\sup_{Q \in \mathcal{U}}",
            "adversary: chọn Q",
            "DRO chuẩn bị cho một họ shift xấu đã chọn.",
        ],
        "animations": ["TransformMatchingShapes(", "ShowPassingFlash(", "there_and_back"],
    },
    "scene_17_uncertainty_set.py": {
        "class": "UncertaintySetScene",
        "target": 75,
        "tokens": [
            r"P_{\mathrm{train}}",
            r"\rho",
            r"\mathcal{U}(P_{\mathrm{train}},\, \rho)",
            "Uncertainty set là giả định cốt lõi của DRO.",
        ],
        "animations": ["ValueTracker(", "Flash(", "Q_{\\mathrm{real}}"],
    },
    "scene_18_f_divergence.py": {
        "class": "FDivergenceScene",
        "target": 75,
        "tokens": [
            r"D_f(Q \| P)",
            r"\frac{dQ}{dP}",
            "70%",
            "40%",
            "60%",
            "f-divergence mô phỏng shift bằng cách reweight",
        ],
        "animations": ["Indicate(", "ShowPassingFlash(", "TransformFromCopy("],
    },
    "scene_19_wasserstein.py": {
        "class": "WassersteinScene",
        "target": 80,
        "tokens": [
            "Wasserstein",
            "Chi phí vận chuyển khối lượng",
            r"W_p(P, Q)",
            "Wasserstein nhìn geometry qua chi phí vận chuyển.",
        ],
        "animations": ["GrowArrow(", "ChangeDecimalToValue(", "MoveAlongPath("],
    },
    "scene_20_dro_limits.py": {
        "class": "DROLimitsScene",
        "target": 70,
        "tokens": [
            r"P_{\mathrm{train}}",
            r"Q^*",
            r"Q_{\mathrm{real}}",
            "Quá bi quan",
            "DRO tốt cần giả định shift sát thực tế.",
        ],
        "animations": ["Indicate(", "ShowPassingFlash(", "Circumscribe("],
    },
}


class TV2ScenesTest(unittest.TestCase):
    def scene_specs(self):
        selected = os.environ.get("TV2_SCENE")
        if selected:
            self.assertIn(selected, TV2_SCENES, f"Unknown TV2_SCENE={selected}")
            return {selected: TV2_SCENES[selected]}
        return TV2_SCENES

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
        for filename, spec in self.scene_specs().items():
            with self.subTest(filename=filename):
                source = self.source(filename)
                self.assertIn(f"TARGET_DURATION_SECONDS = {spec['target']}", source)

    def test_each_scene_uses_shared_style_and_motion(self):
        for filename, spec in self.scene_specs().items():
            with self.subTest(filename=filename):
                source = self.source(filename)
                self.assertIn("setup_dark_scene(self)", source)
                self.assertIn("animate_title_card", source)
                self.assertGreaterEqual(source.count("self.play"), 3)
                for token in spec["animations"]:
                    self.assertIn(token, source)


if __name__ == "__main__":
    unittest.main()
