"""check_checklist.py のテスト。壊したデータを1種類ずつ流し、検出できることを確かめる。"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_checklist as cc  # noqa: E402

SAMPLE = ROOT / "tests" / "fixtures" / "checklist_sample.md"
GAME_FILES = {"00_default.txt", "cabinet_actions.txt"}
# 3行: L1 タイトル / L2 対象パッチ / L3 空行。本文は L4 から始まる
HEADER = "# T\n> 対象パッチ: 1.0 ／ 最終確認日: 2026-10-13\n\n"


def doc(body: str) -> str:
    return HEADER + body


def errors(text: str, game_files=GAME_FILES) -> list[str]:
    return cc.check(text, game_files).errors


class CheckTests(unittest.TestCase):
    def test_sample_passes(self):
        res = cc.check(SAMPLE.read_text(encoding="utf-8-sig"), GAME_FILES)
        self.assertEqual(res.errors, [])
        self.assertEqual(res.items, 7)

    def test_missing_id(self):
        self.assertEqual(errors(doc("## 1. A\n- [ ] 行動\n")), ["L5: 末尾に {#id} がない"])

    def test_duplicate_id(self):
        self.assertEqual(
            errors(doc("## 1. A\n- [ ] a {#x}\n- [ ] b {#x}\n")),
            ["L6: id「x」が L5 と重複"],
        )

    def test_invalid_id(self):
        self.assertEqual(
            errors(doc("## 1. A\n- [ ] a {#Bad_Id}\n")),
            ["L5: id「Bad_Id」は英小文字・数字・ハイフンのみ"],
        )

    def test_prechecked_item(self):
        self.assertEqual(
            errors(doc("## 1. A\n- [x] a {#a}\n")),
            ["L5: Markdown 側でチェック済みにしない（- [ ] にする）"],
        )

    def test_item_in_section_6(self):
        self.assertEqual(
            errors(doc("## 6. 困ったとき\n- [ ] a {#a}\n")),
            ["L5: チェック項目は1〜5章にだけ置ける"],
        )

    def test_item_before_any_section(self):
        self.assertEqual(errors(doc("- [ ] a {#a}\n")), ["L4: チェック項目は1〜5章にだけ置ける"])

    def test_routine_group_items_ok(self):
        self.assertEqual(errors(doc("## 5. 定期ルーチン {.routine}\n### 毎年\n- [ ] a {#a}\n")), [])

    def test_src_missing_file(self):
        self.assertEqual(
            errors(doc("## 1. A\n- [ ] a {#a}\n  - なぜ: b [src: nothere.txt, key]\n")),
            ["L6: [src:] のファイル「nothere.txt」がインストール版に無い"],
        )

    def test_src_with_line_number_and_path(self):
        text = doc("## 1. A\n- [ ] a {#a}\n  - なぜ: b [src: in_game/common/age/00_default.txt:54]\n")
        self.assertEqual(errors(text), [])

    def test_src_non_file_marker_skipped(self):
        self.assertEqual(errors(doc("## 1. A\n- [ ] a [src: Patch_1.4 wiki] {#a}\n")), [])

    def test_src_checked_outside_checklist_sections(self):
        self.assertEqual(
            errors(doc("## 7. 判断の目安\n| a | [src: nothere.txt] |\n")),
            ["L5: [src:] のファイル「nothere.txt」がインストール版に無い"],
        )

    def test_src_skipped_when_game_files_none(self):
        self.assertEqual(errors(doc("## 7. B\n[src: nothere.txt]\n"), game_files=None), [])

    def test_missing_header(self):
        self.assertEqual(
            errors("# T\n\n## 1. A\n- [ ] a {#a}\n"),
            ["L1: 冒頭10行に「対象パッチ:」がない", "L1: 冒頭10行に「最終確認日:」がない"],
        )

    def test_item_limit(self):
        body = "## 1. A\n" + "".join(f"- [ ] a {{#i-{n}}}\n" for n in range(100))
        self.assertEqual(errors(doc(body)), [])
        body101 = body + "- [ ] a {#i-100}\n"
        self.assertEqual(errors(doc(body101)), ["項目数 101 が上限 100 を超えている"])

    def test_char_limit(self):
        base = doc("")
        exact = base + "あ" * (cc.MAX_CHARS - len(base))
        self.assertEqual(errors(exact), [])
        self.assertEqual(errors(exact + "あ"), ["文字数 20001 が上限 20000 を超えている"])

    def test_crlf_same_as_lf(self):
        lf = doc("## 1. A\n- [ ] a {#x}\n- [ ] b {#x}\n")
        self.assertEqual(errors(lf.replace("\n", "\r\n")), errors(lf))


class NormalizeTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(cc.normalize_src_name(" a/b/c.txt:12 "), "c.txt")
        self.assertEqual(cc.normalize_src_name("x_l_japanese.yml"), "x_l_japanese.yml")
        self.assertIsNone(cc.normalize_src_name("Patch_1.4 wiki"))


class MainTests(unittest.TestCase):
    def test_game_file_names(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "in_game" / "common"
            p.mkdir(parents=True)
            (p / "foo.txt").write_text("x", encoding="utf-8")
            self.assertEqual(cc.game_file_names(Path(d)), {"foo.txt"})

    def test_main_reads_bom(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "c.md"
            f.write_bytes(SAMPLE.read_text(encoding="utf-8").encode("utf-8-sig"))
            self.assertEqual(cc.main([str(f), "--skip-src"]), 0)

    def test_main_returns_1_on_error(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "c.md"
            f.write_text(doc("## 1. A\n- [ ] a\n"), encoding="utf-8")
            self.assertEqual(cc.main([str(f), "--skip-src"]), 1)

    def test_main_returns_2_without_game_dir(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "c.md"
            f.write_text(doc(""), encoding="utf-8")
            self.assertEqual(cc.main([str(f), "--game-dir", str(Path(d) / "none")]), 2)


if __name__ == "__main__":
    unittest.main()
