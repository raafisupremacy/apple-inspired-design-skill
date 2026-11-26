"""Tests for scripts/palette.py (standard library only)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import palette  # noqa: E402

SEEDS = ["#F2643A", "#FFD60A", "#0A1F44", "#888888", "#FFFFFF", "#000000", "#34C759", "#7B61FF"]


class ParseTests(unittest.TestCase):
    def test_accepts_six_and_three_digit_hex(self):
        self.assertEqual(palette.parse_hex("#F2643A"), "#f2643a")
        self.assertEqual(palette.parse_hex("f60"), "#ff6600")

    def test_rejects_malformed_input(self):
        for bad in ("orange", "#12", "#GGGGGG", "", "#1234567"):
            with self.assertRaises(ValueError):
                palette.parse_hex(bad)


class ColorMathTests(unittest.TestCase):
    def test_oklch_roundtrip(self):
        for seed in SEEDS + ["#123456", "#abcdef", "#ff0000", "#00ff00", "#0000ff"]:
            back = palette.oklch_to_hex(*palette.hex_to_oklch(seed))
            for i in (1, 3, 5):
                self.assertLessEqual(abs(int(back[i:i + 2], 16) - int(seed[i:i + 2], 16)), 1, (seed, back))

    def test_out_of_gamut_is_clamped(self):
        value = palette.oklch_to_hex(0.7, 0.4, 145)
        self.assertRegex(value, r"^#[0-9a-f]{6}$")

    def test_contrast_extremes(self):
        self.assertAlmostEqual(palette.contrast("#000000", "#ffffff"), 21.0, places=1)
        self.assertAlmostEqual(palette.contrast("#777777", "#777777"), 1.0, places=3)


class PaletteTests(unittest.TestCase):
    def test_all_seeds_and_strategies_pass_floors(self):
        for seed in SEEDS:
            for strategy in palette.STRATEGIES:
                with self.subTest(seed=seed, strategy=strategy):
                    result = palette.build_palette(seed, strategy)
                    self.assertEqual(palette.check_palette(result), [])

    def test_brand_preserves_seed_exactly(self):
        result = palette.build_palette("#F2643A")
        self.assertEqual(result["light"]["brand"], "#f2643a")
        self.assertEqual(result["dark"]["brand"], "#f2643a")

    def test_roles_complete_in_both_themes(self):
        result = palette.build_palette("#7B61FF", "vivid")
        for theme in ("light", "dark"):
            self.assertEqual(set(result[theme]), set(palette.ROLES))

    def test_light_seed_gets_dark_on_accent(self):
        result = palette.build_palette("#FFD60A")
        self.assertLess(palette.hex_to_oklch(result["light"]["onAccent"])[0], 0.5)

    def test_chromatic_seed_keeps_its_color_as_light_accent(self):
        for strategy in palette.STRATEGIES:
            self.assertEqual(palette.build_palette("#FFD60A", strategy)["light"]["accent"], "#ffd60a")

    def test_near_white_seed_accent_is_visible(self):
        light = palette.build_palette("#FFFFFF")["light"]
        self.assertGreaterEqual(palette.contrast(light["accent"], light["bg"]), 3.0)

    def test_pressed_state_dims_in_light_theme_when_contrast_allows(self):
        light = palette.build_palette("#F2643A")["light"]
        self.assertLess(palette.hex_to_oklch(light["accentPressed"])[0],
                        palette.hex_to_oklch(light["accent"])[0])

    def test_dark_seed_is_lightened_for_dark_theme(self):
        result = palette.build_palette("#0A1F44")
        self.assertGreater(palette.hex_to_oklch(result["dark"]["accent"])[0],
                           palette.hex_to_oklch("#0A1F44")[0])

    def test_default_theme(self):
        self.assertEqual(palette.build_palette("#F2643A")["defaultTheme"], "light")
        self.assertEqual(palette.build_palette("#F2643A", "immersive")["defaultTheme"], "dark")

    def test_dark_background_is_not_pure_black(self):
        for strategy in palette.STRATEGIES:
            self.assertNotEqual(palette.build_palette("#F2643A", strategy)["dark"]["bg"], "#000000")

    def test_tinted_background_carries_seed_hue(self):
        bg = palette.build_palette("#F2643A", "tinted")["light"]["bg"]
        self.assertGreater(palette.hex_to_oklch(bg)[1], 0.004)

    def test_unknown_strategy_rejected(self):
        with self.assertRaises(ValueError):
            palette.build_palette("#F2643A", "rainbow")

    def test_ramp_has_eleven_steps_light_to_dark(self):
        ramp = palette.build_palette("#34C759")["ramp"]
        self.assertEqual(list(ramp), ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"])
        lightness = [palette.hex_to_oklch(v)[0] for v in ramp.values()]
        self.assertEqual(lightness, sorted(lightness, reverse=True))


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.p = palette.build_palette("#F2643A")

    def test_css_has_light_dark_and_override(self):
        css = palette.render_css(self.p)
        self.assertIn("--color-bg:", css)
        self.assertIn("prefers-color-scheme: dark", css)
        self.assertIn('[data-theme="dark"]', css)
        self.assertIn('[data-theme="light"]', css)

    def test_every_renderer_produces_text(self):
        for render in (palette.render_css, palette.render_json, palette.render_tailwind,
                       palette.render_swiftui, palette.render_compose, palette.render_flutter):
            out = render(self.p)
            self.assertIsInstance(out, str)
            self.assertIn("f2643a", out.lower())


if __name__ == "__main__":
    unittest.main()
