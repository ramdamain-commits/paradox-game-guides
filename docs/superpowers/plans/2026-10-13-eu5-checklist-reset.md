# EU5 プレイ中チェックリスト 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 既存の EU5 攻略を廃止し、どの国でも使える「プレイ中に横に置くチェックリスト」（Markdown 正本＋チェック可能な HTML）を 1.4 オープンベータ基準でゼロから作る。

**Architecture:** 中身は `eu5/eu5-play-checklist.md` に決まった書式で書き、ルート直下の `checklist.html` が CDN の marked で読み込んで、チェックボックス付きで描画する。チェック状態は localStorage に保存する。書式と `[src:]` の実在は `scripts/check_checklist.py` で機械的に検証する。

**Tech Stack:** 素の HTML/CSS/JS、marked 15.0.12（jsDelivr）、Python 3.13 標準ライブラリ（argparse / re / unittest）、GitHub Pages（main への push で公開）

**Spec:** `docs/superpowers/specs/2026-10-13-eu5-checklist-reset-design.md`（実装前に必ず通読する）

## Global Constraints

- 作業はすべて repo `C:\Users\ramda\projects\paradox-game-guides` の作業ブランチ `eu5-checklist-reset` で行う。main へのマージと push は Task 9 の最後に、ユーザーの了承を得てから行う（main への push で即公開されるため）
- 対象パッチ: 1.4 オープンベータ（Steam ベータブランチ `1.4-open-beta`、ビルド 25606497）。冒頭の表記は「1.4 オープンベータ（ビルド 25606497）・変動注意」
- ゲームスクリプトの場所: `C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis V/game`
- チェック項目は1〜5章の合計で100以内。`eu5/eu5-play-checklist.md` は全体で20,000字以内
- 1項目は「行動1行（`- [ ] … {#id}`）＋任意の『なぜ』1行（`  - なぜ: …`）」まで
- id は `^[a-z0-9]+(-[a-z0-9]+)*$`、ファイル内で一意。一度付けた id は変えない
- 数値・条件には `[src: ファイル名, 識別子]` を付け、ファイル名は実在確認する。信頼性マーカーと用語のルールは repo の `CLAUDE.md` に従う（例外: 本文は日本語名のみとし、英語の併記は8章の用語表に集める）
- 国別・政体別・宗教別の行動は書かない。過去パッチとの差分も書かない
- 旧 EU5 ガイドの記述は根拠にしない（ゼロベース）。一次情報はゲームスクリプトとゲーム内ローカライズ
- ドキュメント・コミットメッセージは日本語。コミット末尾に `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
- `git add` と `git commit` は別コマンドにし、間に `git diff --cached --stat` を見る

## Review Focus

1. 保存できない環境（localStorage が例外を投げる）でもチェック操作と件数表示が動き、コンソールに未処理例外が出ないこと → Task 2 Step 5 の (g)
2. Markdown から消えた・改名された id の保存値が残っていても、件数と進捗に混ざらないこと → Task 2 Step 5 の (f)
3. Windows の作業ツリーは CRLF、BOM 付きのことがある。検証スクリプトも HTML も LF・BOM なしと同じ結果になること → Task 1 のテスト `test_crlf_same_as_lf` と `test_main_reads_bom`、Task 2 はローカル（CRLF）で確認
4. `[src:]` に行番号付き（`file.txt:54`）・パス付き（`in_game/.../file.txt`）・ファイルでないマーカー（`Patch_1.4 wiki`）が混ざっても、誤検出・見逃しがないこと → Task 1 のテスト `test_src_*`
5. Markdown 側で `- [x]` と書いても初期状態でチェックが付かず、検証スクリプトがエラーにすること → Task 1 の `test_prechecked_item`、Task 2 Step 5 の (l)

---

### Task 1: 検証スクリプト `check_checklist.py`

**Files:**
- Create: `scripts/check_checklist.py`
- Create: `tests/test_check_checklist.py`
- Create: `tests/fixtures/checklist_sample.md`
- Modify: `.gitignore`（末尾に `__pycache__/` を追加）

**Interfaces:**
- Produces:
  - `check(text: str, game_files: set[str] | None) -> Result`。`Result` は `NamedTuple(errors: list[str], items: int)`。`game_files=None` のときは `[src:]` の実在確認を省く
  - `game_file_names(game_dir: Path) -> set[str]`（`game_dir` 配下の全ファイル名の集合）
  - `normalize_src_name(raw: str) -> str | None`
  - `main(argv: list[str] | None = None) -> int`（0=合格、1=違反あり、2=ゲームディレクトリが無い）
  - CLI: `python scripts/check_checklist.py <md> [--game-dir DIR] [--skip-src]`
  - `tests/fixtures/checklist_sample.md`（Task 2 の動作確認でも使う）

- [ ] **Step 0: 作業ブランチを作る**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && git branch --show-current && git status --short
```
main・変更なし（仕様書と計画はコミット済み）を確かめてから:
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git switch -c eu5-checklist-reset
```

- [ ] **Step 1: サンプル（正しいデータ）を作る** — `tests/fixtures/checklist_sample.md`

```markdown
# サンプル チェックリスト
> 対象パッチ: 0.0.0（テスト用） ／ 最終確認日: 2026-10-13

テスト用のサンプル。内容はゲームと無関係。

## 1. 開始直後（ポーズ中にやること）
- [ ] **太字**を含む行動 {#start-a}
  - なぜ: 理由の説明 [src: 00_default.txt, age_2_renaissance]
- [ ] 理由なしの行動 {#start-b}

## 2. 序盤：伝統〜ルネサンス（1337〜1437）
### 安全確保
- [ ] 序盤の行動その1 {#early-a}
  - なぜ: 理由（コミュニティ知見）
### 安定化
- [ ] 序盤の行動その2 {#early-b}

## 5. 定期ルーチン {.routine}
### 毎年
- [ ] 毎年の確認 {#yearly-a}
- [ ] 毎年の確認その2 {#yearly-b}
### 10年ごと
- [ ] 10年ごとの見直し {#decade-a}

## 6. 困ったとき
**赤字になった** → 見る場所 → 打ち手

## 7. 判断の目安
| 指標 | 目安 | 出典 |
|---|---|---|
| ルネサンス開始年 | 1342 | [src: 00_default.txt, age_2_renaissance] |

## 8. 用語
- 用語A（Term A）

## 9. 出典
- 00_default.txt
```

- [ ] **Step 2: 失敗するテストを書く** — `tests/test_check_checklist.py`

```python
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
```

- [ ] **Step 3: テストが失敗することを確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest tests.test_check_checklist -v`
Expected: `ModuleNotFoundError: No module named 'check_checklist'` で ERROR

- [ ] **Step 4: 実装する** — `scripts/check_checklist.py`

```python
#!/usr/bin/env python3
"""プレイ中チェックリスト（Markdown）の書式と出典を検証する。

使い方: python scripts/check_checklist.py eu5/eu5-play-checklist.md [--game-dir DIR] [--skip-src]
違反があれば行番号つきで表示して終了コード 1、ゲームディレクトリが無ければ 2 を返す。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple

DEFAULT_GAME_DIR = Path("C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis V/game")
MAX_ITEMS = 100
MAX_CHARS = 20000
LAST_CHECK_SECTION = 5  # チェック項目を置けるのは 1〜5 章
HEADER_LINES = 10
HEADER_LABELS = ("対象パッチ:", "最終確認日:")

H2_RE = re.compile(r"^## (\d+)\.")
ITEM_RE = re.compile(r"^\s*- \[( |x|X)\] ")
ID_RE = re.compile(r"\{#([^}]*)\}\s*$")
VALID_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SRC_RE = re.compile(r"\[src:\s*([^,\]]+)")
FILE_EXT_RE = re.compile(r"\.(txt|yml|csv|gui|json)$")


class Result(NamedTuple):
    errors: list[str]
    items: int


def normalize_src_name(raw: str) -> str | None:
    """[src:] の先頭要素からファイル名を取り出す。ファイルでないマーカー（Patch_1.4 wiki 等）は None。"""
    name = raw.strip()
    name = re.sub(r":\d+(?:-\d+)?$", "", name)  # 行番号を外す
    name = name.replace("\\", "/").rsplit("/", 1)[-1]
    return name if FILE_EXT_RE.search(name) else None


def game_file_names(game_dir: Path) -> set[str]:
    return {p.name for p in game_dir.rglob("*") if p.is_file()}


def check(text: str, game_files: set[str] | None) -> Result:
    errors: list[str] = []
    lines = text.splitlines()

    head = "\n".join(lines[:HEADER_LINES])
    for label in HEADER_LABELS:
        if label not in head:
            errors.append(f"L1: 冒頭{HEADER_LINES}行に「{label}」がない")

    section = 0
    seen: dict[str, int] = {}
    items = 0
    for no, line in enumerate(lines, 1):
        h2 = H2_RE.match(line)
        if h2:
            section = int(h2.group(1))
            continue

        if game_files is not None:
            for raw in SRC_RE.findall(line):
                name = normalize_src_name(raw)
                if name and name not in game_files:
                    errors.append(f"L{no}: [src:] のファイル「{name}」がインストール版に無い")

        item = ITEM_RE.match(line)
        if not item:
            continue
        if not 1 <= section <= LAST_CHECK_SECTION:
            errors.append(f"L{no}: チェック項目は1〜{LAST_CHECK_SECTION}章にだけ置ける")
            continue
        items += 1
        if item.group(1) != " ":
            errors.append(f"L{no}: Markdown 側でチェック済みにしない（- [ ] にする）")
        id_match = ID_RE.search(line)
        if not id_match:
            errors.append(f"L{no}: 末尾に {{#id}} がない")
            continue
        item_id = id_match.group(1)
        if not VALID_ID_RE.match(item_id):
            errors.append(f"L{no}: id「{item_id}」は英小文字・数字・ハイフンのみ")
            continue
        if item_id in seen:
            errors.append(f"L{no}: id「{item_id}」が L{seen[item_id]} と重複")
            continue
        seen[item_id] = no

    if items > MAX_ITEMS:
        errors.append(f"項目数 {items} が上限 {MAX_ITEMS} を超えている")
    if len(text) > MAX_CHARS:
        errors.append(f"文字数 {len(text)} が上限 {MAX_CHARS} を超えている")
    return Result(errors, items)


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="チェックリスト Markdown の書式と出典を検証する")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--game-dir", type=Path, default=DEFAULT_GAME_DIR)
    parser.add_argument("--skip-src", action="store_true", help="[src:] の実在確認をしない")
    args = parser.parse_args(argv)

    text = args.markdown.read_text(encoding="utf-8-sig")
    game_files = None
    if not args.skip_src:
        if not args.game_dir.is_dir():
            print(f"ゲームディレクトリが見つからない: {args.game_dir}（--skip-src で省略可）", file=sys.stderr)
            return 2
        game_files = game_file_names(args.game_dir)

    result = check(text, game_files)
    for e in result.errors:
        print(e)
    if result.errors:
        print(f"NG: {len(result.errors)} 件", file=sys.stderr)
        return 1
    print(f"OK: 項目数 {result.items} / 文字数 {len(text)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

`.gitignore` の末尾に追加:
```
__pycache__/
```

- [ ] **Step 5: テストが通ることを確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest tests.test_check_checklist -v`
Expected: 全件 OK

- [ ] **Step 6: 変異テスト（ガードを外すと落ちることの確認）**

scratchpad に `scripts/check_checklist.py` を複製し、次のガードを1つずつ外して（その行をコメントアウトするか条件を常に偽にして）、テストのインポート先を複製に向けて実行する。どれでも最低1件のテストが FAIL になることを確かめ、結果（外したガード → 落ちたテスト名）を報告に書く。repo の本体は変更しない。

1. ヘッダ確認 2. 章範囲の判定 3. `[x]` 判定 4. id の有無 5. id の形式 6. id の重複 7. `[src:]` の実在 8. 行番号の除去 9. 項目数の上限 10. 文字数の上限

- [ ] **Step 7: 実際のゲームディレクトリで動くことを確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python scripts/check_checklist.py tests/fixtures/checklist_sample.md`
Expected: `OK: 項目数 7 / 文字数 …`（`00_default.txt` は実在するため）。所要秒数も報告に書く

- [ ] **Step 8: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && git add scripts/check_checklist.py tests/test_check_checklist.py tests/fixtures/checklist_sample.md .gitignore
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git diff --cached --stat
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git commit -F - <<'EOF'
feat: チェックリスト Markdown の検証スクリプトを追加

id の有無・形式・重複、チェック項目を置ける章、項目数・文字数の上限、
[src:] のファイルがインストール版に実在するかを検証する。

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
```

---

### Task 2: チェックリストビューア `checklist.html`

**Files:**
- Create: `checklist.html`

**Interfaces:**
- Consumes: Task 1 の `tests/fixtures/checklist_sample.md`（動作確認用）。Markdown 書式は仕様書3章
- Produces: `checklist.html?file=<repo相対パス>.md`。localStorage キー `checklist:<file>`、値 `{"checked":{id:true},"open":{key:bool},"showSrc":bool}`

- [ ] **Step 1: 実装する** — `checklist.html`

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>プレイ中チェックリスト</title>
<style>
  :root {
    --bg: #f8fafc; --surface: #ffffff; --border: #e2e8f0;
    --text: #0f172a; --muted: #64748b;
    --accent: #c2410c; --accent-dim: rgba(194, 65, 12, 0.12);
    --radius: 8px;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #0f172a; --surface: #1e293b; --border: #334155;
      --text: #f1f5f9; --muted: #94a3b8;
      --accent: #fb923c; --accent-dim: rgba(251, 146, 60, 0.15);
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--bg); color: var(--text); line-height: 1.6;
    font-family: system-ui, -apple-system, "Segoe UI", "Hiragino Sans", "Yu Gothic UI", sans-serif;
  }
  a { color: var(--accent); }
  .wrap { max-width: 860px; margin: 0 auto; padding: 0 16px 48px; }
  .toolbar {
    position: sticky; top: 0; z-index: 1; background: var(--bg);
    padding: 10px 0; border-bottom: 1px solid var(--border);
    display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
  }
  .progress { flex: 1 1 160px; height: 8px; background: var(--border); border-radius: 4px; overflow: hidden; }
  .progress > span { display: block; height: 100%; width: 0; background: var(--accent); }
  #progress-text { font-size: .85rem; color: var(--muted); }
  button {
    font: inherit; font-size: .85rem; padding: 4px 10px; cursor: pointer;
    border: 1px solid var(--border); border-radius: var(--radius);
    background: var(--surface); color: var(--text);
  }
  button[aria-pressed="true"] { background: var(--accent-dim); border-color: var(--accent); }
  details { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); margin: 12px 0; padding: 0 12px; }
  details details { margin: 8px 0; }
  summary {
    list-style: none; cursor: pointer; font-weight: 700; padding: 10px 0;
    display: flex; flex-wrap: wrap; gap: 8px; align-items: baseline;
  }
  summary::-webkit-details-marker { display: none; }
  summary::before { content: "▸"; color: var(--muted); }
  details[open] > summary::before { content: "▾"; }
  summary button { margin-left: auto; font-weight: 400; }
  .count { color: var(--muted); font-weight: 400; font-size: .85rem; }
  ul.items { list-style: none; padding: 0; margin: 0 0 12px; }
  ul.items li { padding: 6px 0; border-top: 1px solid var(--border); }
  ul.items label { display: flex; gap: 8px; align-items: flex-start; cursor: pointer; }
  ul.items input { flex: none; margin-top: .3em; width: 1.1em; height: 1.1em; accent-color: var(--accent); }
  li.done .text { color: var(--muted); text-decoration: line-through; }
  .why { display: block; margin-left: 1.9em; font-size: .85rem; color: var(--muted); }
  .src { font-size: .75rem; color: var(--muted); }
  body:not(.show-src) .src { display: none; }
  .doc, .note, ul.items { overflow-wrap: anywhere; }
  table { border-collapse: collapse; display: block; overflow-x: auto; max-width: 100%; }
  th, td { border: 1px solid var(--border); padding: 4px 8px; text-align: left; }
  blockquote { margin: 8px 0; padding: 4px 12px; border-left: 3px solid var(--accent); color: var(--muted); }
  .error { border: 1px solid var(--accent); border-radius: var(--radius); padding: 12px; }
</style>
</head>
<body>
<div class="wrap">
  <div class="toolbar">
    <div class="progress"><span id="bar"></span></div>
    <span id="progress-text"></span>
    <button type="button" id="toggle-src" aria-pressed="false">出典を表示</button>
    <button type="button" id="reset-all">新しいプレイを始める</button>
    <a id="md-link" href="viewer.html">Markdown で読む</a>
  </div>
  <main id="content"><p>読み込み中…</p></main>
</div>
<script src="https://cdn.jsdelivr.net/npm/marked@15.0.12/marked.min.js"></script>
<script>
(function () {
  'use strict';
  const FILE_RE = /^[A-Za-z0-9_-]+(\/[A-Za-z0-9_-]+)*\.md$/;
  const ITEM_RE = /^\s*- \[ \] (.*?)\s*\{#([a-z0-9]+(?:-[a-z0-9]+)*)\}\s*$/;
  const WHY_RE = /^\s+- なぜ:\s*(.*)$/;
  const H2_RE = /^## (.*)$/;
  const H3_RE = /^### (.*)$/;
  const ROUTINE_MARK = '{.routine}';
  const LAST_CHECK_SECTION = 5;     // チェック項目を描画するのは 1〜5 章
  const LAST_PROGRESS_SECTION = 4;  // 進捗バーに数えるのは 1〜4 章（ルーチンは除く）

  const main = document.getElementById('content');
  const file = new URLSearchParams(location.search).get('file') || '';

  function showError(msg) {
    main.textContent = '';
    const p = document.createElement('p');
    p.className = 'error';
    p.textContent = msg;
    main.appendChild(p);
  }

  if (!FILE_RE.test(file)) {
    showError('file パラメータが不正です（例: checklist.html?file=eu5/eu5-play-checklist.md）');
    return;
  }
  if (typeof marked === 'undefined') {
    showError('Markdown ライブラリを読み込めませんでした。通信状況を確認して再読み込みしてください。');
    return;
  }

  const storageKey = 'checklist:' + file;
  const state = loadState();

  function loadState() {
    try {
      const raw = localStorage.getItem(storageKey);
      const s = raw ? JSON.parse(raw) : null;
      if (s && typeof s === 'object') {
        return { checked: s.checked || {}, open: s.open || {}, showSrc: !!s.showSrc };
      }
    } catch (e) { /* 保存できない環境では初期状態で動かす */ }
    return { checked: {}, open: {}, showSrc: false };
  }

  function save() {
    try { localStorage.setItem(storageKey, JSON.stringify(state)); } catch (e) { /* 保存だけ諦める */ }
  }

  function wrapSrc(html) {
    return html.replace(/\[src:[^\]]*\]/g, m => '<span class="src">' + m + '</span>');
  }

  function inline(s) { return wrapSrc(marked.parseInline(s)); }

  function parse(md) {
    const lines = md.replace(/\r\n?/g, '\n').split('\n');
    const head = [];
    const sections = [];
    let cur = null;
    for (const line of lines) {
      const h = line.match(H2_RE);
      if (h) {
        const routine = h[1].includes(ROUTINE_MARK);
        const title = h[1].replace(ROUTINE_MARK, '').trim();
        const num = Number((title.match(/^(\d+)\./) || [])[1] || 0);
        cur = { title, num, routine, lines: [] };
        sections.push(cur);
        continue;
      }
      (cur ? cur.lines : head).push(line);
    }
    return { head: head.join('\n'), sections };
  }

  function groupBlocks(lines) {
    const groups = [{ title: null, blocks: [] }];
    let lastItem = null;
    for (const line of lines) {
      const h3 = line.match(H3_RE);
      if (h3) { groups.push({ title: h3[1].trim(), blocks: [] }); lastItem = null; continue; }
      const g = groups[groups.length - 1];
      const it = line.match(ITEM_RE);
      if (it) { lastItem = { type: 'item', text: it[1], id: it[2], why: null }; g.blocks.push(lastItem); continue; }
      const why = line.match(WHY_RE);
      if (why && lastItem) { lastItem.why = why[1]; continue; }
      lastItem = null;
      if (line.trim() === '') continue;
      const prev = g.blocks[g.blocks.length - 1];
      if (prev && prev.type === 'md') prev.text += '\n' + line;
      else g.blocks.push({ type: 'md', text: line });
    }
    return groups.filter(g => g.title !== null || g.blocks.length);
  }

  function makeDetails(key, titleHtml, className) {
    const d = document.createElement('details');
    d.className = className + ' counted';
    d.open = key in state.open ? !!state.open[key] : true;
    const s = document.createElement('summary');
    const t = document.createElement('span');
    t.innerHTML = titleHtml;
    const c = document.createElement('span');
    c.className = 'count';
    s.append(t, c);
    d.appendChild(s);
    d.addEventListener('toggle', () => { state.open[key] = d.open; save(); });
    return { d, s };
  }

  function renderItem(block, progress) {
    const li = document.createElement('li');
    const label = document.createElement('label');
    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.dataset.id = block.id;
    if (progress) cb.dataset.progress = '1';
    cb.checked = !!state.checked[block.id];
    const text = document.createElement('span');
    text.className = 'text';
    text.innerHTML = inline(block.text);
    label.append(cb, text);
    li.appendChild(label);
    if (block.why) {
      const w = document.createElement('span');
      w.className = 'why';
      w.innerHTML = 'なぜ: ' + inline(block.why);
      li.appendChild(w);
    }
    li.classList.toggle('done', cb.checked);
    cb.addEventListener('change', () => {
      if (cb.checked) state.checked[block.id] = true;
      else delete state.checked[block.id];
      li.classList.toggle('done', cb.checked);
      save();
      updateCounts();
    });
    return li;
  }

  function uncheck(container) {
    container.querySelectorAll('input[data-id]').forEach(cb => {
      cb.checked = false;
      delete state.checked[cb.dataset.id];
      cb.closest('li').classList.remove('done');
    });
    save();
    updateCounts();
  }

  function renderChecklistSection(sec) {
    const progress = sec.num <= LAST_PROGRESS_SECTION;
    const { d } = makeDetails('s' + sec.num, marked.parseInline(sec.title), 'sec');
    for (const g of groupBlocks(sec.lines)) {
      let target = d;
      if (g.title !== null) {
        const sub = makeDetails('s' + sec.num + ':' + g.title, marked.parseInline(g.title), 'group');
        if (sec.routine) {
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.textContent = 'リセット';
          btn.addEventListener('click', e => {
            e.preventDefault();
            e.stopPropagation();
            if (confirm('「' + g.title + '」のチェックを外しますか？')) uncheck(sub.d);
          });
          sub.s.appendChild(btn);
        }
        d.appendChild(sub.d);
        target = sub.d;
      }
      let ul = null;
      for (const b of g.blocks) {
        if (b.type === 'item') {
          if (!ul) { ul = document.createElement('ul'); ul.className = 'items'; target.appendChild(ul); }
          ul.appendChild(renderItem(b, progress));
        } else {
          ul = null;
          const div = document.createElement('div');
          div.className = 'note';
          div.innerHTML = wrapSrc(marked.parse(b.text));
          target.appendChild(div);
        }
      }
    }
    return d;
  }

  function updateCounts() {
    main.querySelectorAll('details.counted').forEach(d => {
      const boxes = [...d.querySelectorAll('input[data-id]')];
      const done = boxes.filter(b => b.checked).length;
      d.querySelector(':scope > summary > .count').textContent = '[' + done + '/' + boxes.length + ']';
    });
    const p = [...main.querySelectorAll('input[data-progress]')];
    const done = p.filter(b => b.checked).length;
    document.getElementById('bar').style.width = (p.length ? done / p.length * 100 : 0) + '%';
    document.getElementById('progress-text').textContent = '進捗 ' + done + '/' + p.length;
  }

  const srcBtn = document.getElementById('toggle-src');
  function applySrc() {
    document.body.classList.toggle('show-src', state.showSrc);
    srcBtn.setAttribute('aria-pressed', String(state.showSrc));
    srcBtn.textContent = state.showSrc ? '出典を隠す' : '出典を表示';
  }
  srcBtn.addEventListener('click', () => { state.showSrc = !state.showSrc; save(); applySrc(); });

  document.getElementById('reset-all').addEventListener('click', () => {
    if (!confirm('すべてのチェックを外して、新しいプレイを始めますか？')) return;
    state.checked = {};
    uncheck(main);
  });

  document.getElementById('md-link').href = 'viewer.html?file=' + encodeURIComponent(file);

  function render(md) {
    const { head, sections } = parse(md);
    main.textContent = '';
    const h = document.createElement('div');
    h.className = 'doc';
    h.innerHTML = marked.parse(head);
    main.appendChild(h);
    const h1 = h.querySelector('h1');
    if (h1) document.title = h1.textContent;
    for (const sec of sections) {
      if (sec.num >= 1 && sec.num <= LAST_CHECK_SECTION) {
        main.appendChild(renderChecklistSection(sec));
      } else {
        const s = document.createElement('section');
        s.className = 'doc';
        s.innerHTML = marked.parse('## ' + sec.title + '\n' + sec.lines.join('\n'));
        main.appendChild(s);
      }
    }
    applySrc();
    updateCounts();
  }

  fetch(file, { cache: 'no-cache' })
    .then(r => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.text(); })
    .then(render)
    .catch(e => showError('チェックリストを読み込めませんでした（' + file + '）: ' + e.message));
})();
</script>
</body>
</html>
```

- [ ] **Step 2: ローカルサーバを起動する**

`run_in_background` で起動する（フォアグラウンドで待たない）:
```bash
cd /c/Users/ramda/projects/paradox-game-guides && python -m http.server 8765
```

- [ ] **Step 3: ブラウザで開く**

Playwright MCP（`mcp__playwright__browser_navigate`）で `http://localhost:8765/checklist.html?file=tests/fixtures/checklist_sample.md&nocache=<時刻>` を開く。キャッシュ回避のため、再読込のたびに `nocache` の値を変える。`confirm()` は `mcp__playwright__browser_handle_dialog` で受諾する。

- [ ] **Step 4: 初期表示を確かめる**

`browser_evaluate` で次を評価し、期待値と完全一致することを確かめる:
```js
() => ({
  boxes: document.querySelectorAll('input[data-id]').length,          // 7
  progress: document.getElementById('progress-text').textContent,           // "進捗 0/4"
  s1: document.querySelector('details.sec > summary .count').textContent,   // "[0/2]"
  srcHidden: getComputedStyle(document.querySelector('.why .src')).display, // "none"
  tableSrc: document.querySelector('table').textContent.includes('[src:'),  // true（7章は常に表示）
  title: document.title                                                      // "サンプル チェックリスト"
})
```

- [ ] **Step 5: 操作を確かめる**（各項目の結果を報告に書く）

a. `start-a` をクリック → 再読込 → チェックが残り、`進捗 1/4`、1章 `[1/2]`
b. `yearly-a` と `decade-a` をチェック → 「毎年」のリセットを押して受諾 → `yearly-a` だけ外れ、`decade-a` と `start-a` は残る。ルーチンは進捗に数えない（`進捗 1/4` のまま）
c. 「出典を表示」 → `.why .src` が表示される → 再読込しても表示のまま（`showSrc` が保存されている）
d. 1章を折りたたむ → 再読込しても閉じたまま
e. 「新しいプレイを始める」を受諾 → 全チェックが外れ `進捗 0/4`。「キャンセル」を選んだときは何も変わらないことも確かめる
f. 消えた id: `localStorage.setItem('checklist:tests/fixtures/checklist_sample.md', JSON.stringify({checked:{'gone-id':true,'start-a':true}}))` → 再読込 → `進捗 1/4`、チェックボックスは7個のまま
g. 保存できない環境: `Storage.prototype.setItem = () => { throw new Error('quota'); }` を評価 → `start-b` をクリック → チェックが付き、`進捗` が増え、`browser_console_messages` にエラーが無い
h. 不正な file: `checklist.html?file=../x.md` と `checklist.html?file=/x.md` → 「file パラメータが不正です」が出る。`checklist.html?file=nope.md` → 「読み込めませんでした（nope.md）: HTTP 404」が出る
i. 幅375px（`browser_resize` 375×812）で `document.documentElement.scrollWidth <= 375` が true。スクリーンショットを撮る
j. ダークモード（`browser_emulate_media` で `colorScheme: 'dark'`）で `getComputedStyle(document.body).backgroundColor === 'rgb(15, 23, 42)'`。スクリーンショットを撮る
k. 「Markdown で読む」の href が `viewer.html?file=tests%2Ffixtures%2Fchecklist_sample.md`
l. Markdown 側の `- [x]`: gitignore 対象の `_staging/prechecked.md` に次を書き、`checklist.html?file=_staging/prechecked.md` を開く → `document.querySelectorAll('input[data-id]').length === 1`、`進捗 0/1`、1章の件数が `[0/1]`。確認後にファイルを消す

```markdown
# P
> 対象パッチ: 0 ／ 最終確認日: 2026-10-13
## 1. A
- [x] a {#a}
- [ ] b {#b}
```

不具合があれば `checklist.html` を直し、Step 4 からやり直す。終わったら http.server を止める。

- [ ] **Step 6: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && git add checklist.html
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git diff --cached --stat
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git commit -F - <<'EOF'
feat: Markdown を読み込みチェックリスト化する checklist.html を追加

チェック状態・折りたたみ・出典表示をブラウザに保存し、全体リセットと
定期ルーチンのグループ単位リセットに対応する。

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
```

---

### Task 3: 対象パッチの確定とチェックリストの骨組み

**Files:**
- Create: `eu5/eu5-play-checklist.md`

**Interfaces:**
- Consumes: Task 1 の CLI
- Produces: 見出しと冒頭だけの `eu5/eu5-play-checklist.md`。章見出しの文言は以下で固定（後続タスクはこの見出しの下に書く）

- [ ] **Step 1: ビルド番号を確かめる**

```bash
grep -E '"buildid"|BetaKey' "/c/Program Files (x86)/Steam/steamapps/appmanifest_3450310.acf"
```
Expected: `buildid` が `25606497`、`BetaKey` が `1.4-open-beta`。違っていたら作業を止めてユーザーに報告する（仕様書の前提が変わるため）

- [ ] **Step 2: 1.4 ベータの版番号を確かめる**

`https://eu5.paradoxwikis.com/Patches` を Playwright で開き、1.4 ベータの版番号（例: 1.4.0）と公開日を控える。2026-10-12 前後の更新と対応づけられないときは、ユーザーに「ランチャー右下の版表示」を1問で確認する。

- [ ] **Step 3: 骨組みを書く** — `eu5/eu5-play-checklist.md`（`<版番号>` は Step 2 の値、`<日付>` は作業日）

```markdown
# EU5 プレイ中チェックリスト
> 対象パッチ: <版番号> オープンベータ（ビルド 25606497）・変動注意 ／ 最終確認日: <日付>

どの国でも共通の「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。国ごとの事情は扱わない。

## 1. 開始直後（ポーズ中にやること）

## 2. 序盤：伝統〜ルネサンス（1337〜1437）

## 3. 中盤：発見〜宗教改革（1437〜1637）

## 4. 終盤：絶対主義〜革命（1637〜）

## 5. 定期ルーチン {.routine}

## 6. 困ったとき

## 7. 判断の目安

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

## 9. 出典
```

- [ ] **Step 4: 時代の開始年を 1.4 ベータで確かめる**

```bash
G="/c/Program Files (x86)/Steam/steamapps/common/Europa Universalis V/game"; sed 's/^\xEF\xBB\xBF//' "$G/in_game/common/age/00_default.txt" | grep -nE '^age_[0-9a-z_]+ = \{|^\s*year ='
```
Expected: 伝統 1 / ルネサンス 1342 / 発見 1437 / 宗教改革 1537 / 絶対主義 1637 / 革命 1737。違っていれば見出しの年を直し、ユーザーに報告する。この確認結果を7章の最初の行に入れる:

```markdown
| 時代の開始年 | ルネサンス1342／発見1437／宗教改革1537／絶対主義1637／革命1737 | [src: 00_default.txt, age_2_renaissance 〜 age_6_revolutions] |
```
（表のヘッダ `| 指標 | 目安 | 出典 |` と区切り行も付ける。`00_default.txt` は複数フォルダにあるので、9章の出典には `in_game/common/age/00_default.txt` とフルパスで書く）

- [ ] **Step 5: 検証してコミット**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python scripts/check_checklist.py eu5/eu5-play-checklist.md`
Expected: `OK: 項目数 0 / …`

```bash
cd /c/Users/ramda/projects/paradox-game-guides && git add eu5/eu5-play-checklist.md
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git diff --cached --stat
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git commit -F - <<'EOF'
eu5: プレイ中チェックリストの骨組みを追加（1.4 オープンベータ基準）

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
```

---

## 中身の執筆タスク（Task 4〜7）に共通する手順

Task 4〜7 は、各章の中身を一次情報から書き起こす。手順と合格基準は共通で、以下のとおり。

**一次情報の当たり先**（`G` = ゲームディレクトリ）

| 何を知りたいか | 見る場所 |
|---|---|
| 公式が教える手順・順序 | `G/in_game/common/tutorial_lessons/`（admin / basics / diplomacy / military）、`tutorial_lesson_chains/` |
| 「困った状態」の判定条件 | `G/in_game/common/alert_descriptions/00_default.txt`、`scriptable_hints/` |
| 内政の操作 | `estates/`、`estate_privileges/`、`laws/`、`policies/`、`cabinet_actions/`、`building_types/` |
| 時代・進歩・ランク | `age/`、`advances/`、`country_ranks/` |
| 戦争と講和 | `casus_belli/`、`wargoals/`、`peace_treaties/`、`levies/`、`unit_types/` |
| 自動で効く補正 | `auto_modifiers/`、`static_modifiers/`（無ければ `grep -rl` で探す） |
| 数値の定数 | `G/loading_screen/common/defines/00_defines.txt` |
| 正式な日本語名 | `G/main_menu/localization/japanese/`（`game_concepts_l_japanese.yml` 等）と `eu5/localization-reference.md` |
| コミュニティの定石 | `eu5.paradoxwikis.com`（数値は必ずスクリプトで1件以上照合） |

**書き方**

1. 候補の行動を一次情報から洗い出し、「どの国でも当てはまるか」「その時期にやることか」で絞る。国・宗教・政体に依存するものは載せない
2. 行動文は「〈画面や対象〉で〈操作〉する」「〈状態〉を確認する」の形で、動詞で終える。1行に1つの行動
3. 「なぜ」は判断の根拠を1行で。根拠がスクリプトなら `[src: ファイル名, 識別子]`、プレイ報告なら `（コミュニティ知見）`
4. 数値を書いたら、その数値を7章の表にも同じ値で載せる（判断の目安になる数値のみ）
5. 用語は書く前にローカライズで正式な訳を確かめる。英語名は8章に「日本語名（English）」で追加する
6. EU4 由来の語を混ぜない。書いたあと `grep -nE 'fabricate|forge_claim|spy_network|捏造|交易ノード|Trade Node|Coalition|AE' eu5/eu5-play-checklist.md` で0件を確かめる
7. 新しく使ったスクリプトファイルは9章「一次情報」に `in_game/...` のフルパスで追記し、wiki の URL は9章「コミュニティ情報」に書く（本文の `[src:]` に URL を入れない）
8. スクリプトは BOM 付きが多い。件数を数えるときは `sed 's/^\xEF\xBB\xBF//'` で剥がしてから数える

**合格基準**（各タスクの最終ステップで確かめ、報告に書く）

- `python scripts/check_checklist.py eu5/eu5-play-checklist.md` が `OK`
- そのタスクの章の項目数が予算以内
- タスクで書いた数値ごとに「数値 → 確かめたファイルと識別子 → 実際の値」の対応表を報告に書く（`[src:]` が名称の yml しか指していないものは、効果値の裏取りになっていないので不合格）
- 上の EU4 語 grep が0件
- 国・宗教・政体に依存する行動が入っていない（入れかけて外したものがあれば、その一覧を報告に書く）

---

### Task 4: 1章「開始直後」と2章「序盤」

**Files:**
- Modify: `eu5/eu5-play-checklist.md`（1・2章、必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: Task 3 の見出し
- Produces: 1章（10項目以内）、2章（25項目以内。`### 安全確保` `### 安定化` `### 拡大の開始` の3グループ）。id の接頭辞は1章 `start-`、2章 `early-`

- [ ] **Step 1: 一次情報を集める**（共通手順の表。特に `tutorial_lessons/` 全4ファイルと `alert_descriptions/`）。候補一覧を scratchpad に書く
- [ ] **Step 2: 1章を書く**（ポーズ中に済む設定・確認のみ。時間を進めないとできないことは2章へ）
- [ ] **Step 3: 2章を書く**（3グループの順。各グループの冒頭に、そのグループの到達目標を1行の通常文で書いてよい）
- [ ] **Step 4: 7〜9章への追記**（共通手順の書き方 4・5・7）
- [ ] **Step 5: 合格基準を確かめる**
- [ ] **Step 6: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && git add eu5/eu5-play-checklist.md
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git diff --cached --stat
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git commit -F - <<'EOF'
eu5: チェックリストの開始直後・序盤の章を執筆

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
```

---

### Task 5: 3章「中盤」と4章「終盤」

**Files:**
- Modify: `eu5/eu5-play-checklist.md`（3・4章、必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: Task 4 で使った id（重複させない）と8章の用語
- Produces: 3章（20項目以内）、4章（15項目以内）。id の接頭辞は3章 `mid-`、4章 `late-`

- [ ] **Step 1: 一次情報を集める**（特に `age/`、`advances/`、`country_ranks/`。時代の切り替わりで何が変わるかを `age/00_default.txt` の各時代ブロックから読む）
- [ ] **Step 2: 3章を書く**（本格拡大・国家ランクの昇格・進歩の取り方）
- [ ] **Step 3: 4章を書く**（維持と仕上げ、終盤に崩れやすい点の予防）
- [ ] **Step 4: 7〜9章への追記**
- [ ] **Step 5: 合格基準を確かめる**（1〜4章の合計が70項目以内であることも確かめる。5章の枠を残すため）
- [ ] **Step 6: コミット**（メッセージ: `eu5: チェックリストの中盤・終盤の章を執筆`。手順は Task 4 Step 6 と同じ3コマンド）

---

### Task 6: 5章「定期ルーチン」と6章「困ったとき」

**Files:**
- Modify: `eu5/eu5-play-checklist.md`（5・6章、必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: 1〜4章の内容（ルーチンと重複させない。1〜4章で一度だけやることは5章に書かない）
- Produces: 5章（`### 毎年` `### 10年ごと` `### 時代が変わったとき` `### 戦争の前と後` の4グループ、合計25項目以内。かつ1〜5章の合計が100以内）。id の接頭辞は `yearly-` `decade-` `age-` `war-`。6章は8症状以内

- [ ] **Step 1: 一次情報を集める**（6章は `alert_descriptions/00_default.txt` の警告条件を主な根拠にする）
- [ ] **Step 2: 5章を書く**
- [ ] **Step 3: 6章を書く**。1症状は次の3行の形にする（チェックボックスは使わない）:

```markdown
**〈症状〉**
- 見る場所: 〈画面・指標〉
- 打ち手: 〈行動〉（根拠 `[src: …]` または（コミュニティ知見））
```

- [ ] **Step 4: 7〜9章への追記**
- [ ] **Step 5: 合格基準を確かめる**
- [ ] **Step 6: コミット**（メッセージ: `eu5: チェックリストの定期ルーチン・困ったときの章を執筆`）

---

### Task 7: 7〜9章の仕上げと全体の整合

**Files:**
- Modify: `eu5/eu5-play-checklist.md`

- [ ] **Step 1: 数値の突き合わせ**。1〜6章に出てくる数値をすべて grep で抜き出す（`grep -nE '[0-9]' eu5/eu5-play-checklist.md`）。判断に使う数値が7章に同じ値であること、7章の全行に `[src:]` か（コミュニティ知見）があることを確かめる
- [ ] **Step 2: 用語の突き合わせ**。本文に出る用語がすべて8章にあり、8章の語がすべて本文で使われていることを確かめる。8章の訳語は `localization-reference.md` かローカライズ yml と一致させる。対照表に無い汎用語（複数の国で使う語）は、`localization-reference.md` にも追記する
- [ ] **Step 3: 出典の突き合わせ**。本文の `[src:]` に出るファイルが、すべて9章「一次情報」にあることを確かめる
- [ ] **Step 4: 通読**。`checklist.html?file=eu5/eu5-play-checklist.md` をローカルで開き（Task 2 Step 2〜3 の方法）、1〜5章の流れに矛盾や重複がないか、1項目が2行を超えていないかを確かめる。スクリーンショットを1枚撮る
- [ ] **Step 5: 合格基準と上限を確かめる**（`OK: 項目数 ≤100 / 文字数 ≤20000`）
- [ ] **Step 6: コミット**（メッセージ: `eu5: チェックリストの数値表・用語・出典を整備`）

---

### Task 8: 3名レビュー

**Files:**
- Modify: `eu5/eu5-play-checklist.md`（指摘の反映）

- [ ] **Step 1: レビュー依頼**。`reviewer` エージェントを3並列で起動する（読み取り専用）。各レビュワーの観点は repo の `CLAUDE.md`「レビュー」節のとおり:
  - 熟練者: 行動の正しさ・時期の妥当性・抜け漏れ・1.4 ベータでの仕様
  - プレイヤー（一通り遊んだが忘れる人）: 項目だけ見て操作できるか、用語がゲーム内表記と一致するか
  - テクニカルライター: 書式・表記揺れ・1項目2行以内・数値の再掲の一致

  3名共通の依頼事項:
  - `[src:]` を最低10件、実際にファイルを開いて値と識別子を照合する
  - 国・宗教・政体に依存する行動が混入していないかを見る
  - 指摘には重大度（critical / important / suggestion）と行番号を付ける
  - 結果は `_staging/2026-10-xx-eu5-checklist-review-<観点>.md` に書かせる

- [ ] **Step 2: 反映**。critical と important はすべて反映する。suggestion は採否と理由を一覧にする。訂正した語句・数値ごとに `grep -n` でファイル全体を確かめ、旧値が残っていないことを確認する
- [ ] **Step 3: 合格基準を確かめてコミット**（メッセージ: `eu5: チェックリストに3名レビューの指摘を反映`）

---

### Task 9: 旧ファイルの削除・付随更新・マージ

**Files:**
- Delete: `eu5/eu5-austria-guide.md` `eu5/eu5-austria-hre-guide.md` `eu5/eu5-brandenburg-guide.md` `eu5/eu5-byzantium-guide.md` `eu5/eu5-castile-guide.md` `eu5/eu5-government-guide.md` `eu5/eu5-hungary-guide.md` `eu5/eu5-ottoman-guide.md` `eu5/eu5-recommended-mods.md` `eu5/eu5-regional-guide.md` `eu5/eu5-religion-guide.md` `eu5/eu5-universal-guide.md`
- Delete: `docs/superpowers/specs/2026-04-01-eu5-ottoman-guide-design.md` `docs/superpowers/specs/2026-04-06-eu5-castile-guide-design.md` `docs/superpowers/specs/2026-04-06-eu5-patch12-update-design.md` `docs/superpowers/specs/2026-04-08-eu5-universal-guide-design.md` `docs/superpowers/specs/2026-04-11-eu5-austria-guide-design.md` `docs/superpowers/specs/2026-06-16-eu5-patch13-update-design.md`
- Delete: `docs/superpowers/plans/2026-04-01-eu5-ottoman-guide.md` `docs/superpowers/plans/2026-04-11-eu5-austria-guide.md` `docs/superpowers/plans/2026-06-18-eu5-patch13-stable-promotion.md`
- Delete（git 管理外・復元不可）: `_staging/2026-07-10-eu5-13-stable-reverify.md` `_staging/2026-07-11-eu5-mods-13-compat.md` `_staging/2026-07-11-ottoman-enrich-research.md` `_staging/2026-07-11-brandenburg-enrich-research.md` `_staging/2026-07-11-castile-enrich-research.md` `_staging/eu5-6countries-review-player.md` `_staging/eu5-6countries-review-writer.md` `_staging/eu5-6countries-review-veteran.md` `eu5/_staging/`（3本） ※ Task 8 のレビュー結果 `_staging/2026-10-xx-eu5-checklist-review-*.md` もここで消す
- Modify: `index.html`、`README.md`、`CHANGELOG.md`、`CLAUDE.md`、`docs/templates/guide-section-template.md`、`docs/procedures/new-country-guide.md`

- [ ] **Step 1: ビルド番号を再確認する**（Task 3 Step 1 と同じコマンド）。25606497 から変わっていたら、`python scripts/check_checklist.py eu5/eu5-play-checklist.md` を再実行し、変わった旨と結果をユーザーに報告してから進む
- [ ] **Step 2: git 管理下のファイルを削除する**（上の Delete 1〜3段目を `git rm` で）
- [ ] **Step 3: git 管理外のファイルを削除する**（上の Delete 4段目を `rm` で。消す前に `ls` で対象を表示する）
- [ ] **Step 4: `index.html` を直す**。EU5 セクション（`<section class="game-section" data-game="eu5">` の `card-list`）の `<li>` 12枚を、次の2枚に置き換える:

```html
        <li>
          <a class="card" href="checklist.html?file=eu5/eu5-play-checklist.md" target="_blank" rel="noopener">
            <div class="card__info">
              <div class="card__title">プレイ中チェックリスト</div>
              <div class="card__meta">1.4 オープンベータ — どの国でも共通の「いつ・何をするか」</div>
            </div>
            <span class="card__tag tag--guide">攻略</span>
            <svg class="card__arrow" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </li>
        <li>
          <a class="card" href="viewer.html?file=eu5/localization-reference.md" target="_blank" rel="noopener">
            <div class="card__info">
              <div class="card__title">用語対照表</div>
              <div class="card__meta">ゲーム内日本語訳と英語名の対照</div>
            </div>
            <span class="card__tag tag--guide">用語</span>
            <svg class="card__arrow" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </li>
```

- [ ] **Step 5: `README.md` を直す**。「### Europa Universalis V」節の国別表・共通システム表・おすすめMOD行を、チェックリストと用語対照表の2行の表に置き換える。「構成」のツリーに `checklist.html … Markdown をチェックリストとして表示` と `scripts/ … 検証スクリプト（check_checklist.py）`、`tests/ … 検証スクリプトのテスト` を追加し、`eu5/` の説明を「プレイ中チェックリスト＋用語対照表」にする
- [ ] **Step 6: `CLAUDE.md`（repo）を直す**
  - 4行目の模範例を `vic3/vic3-japan-guide.md` にする
  - 24行目の命名例から `eu5/eu5-brandenburg-guide.md` を外す
  - 「ファイル構成」節に、EU5 は国別ガイドを置かずに `eu5/eu5-play-checklist.md`（`checklist.html` で表示）を正本とし、書式は仕様書 `docs/superpowers/specs/2026-10-13-eu5-checklist-reset-design.md` の3章に従うこと、コミット前に `python scripts/check_checklist.py eu5/eu5-play-checklist.md` を通すことを追記する
  - 「スクリプト参照時のルール」の公開ベータの行の直後に、EU5 チェックリストはユーザーの指示で 1.4 オープンベータを本文の基準にしており、差分セクション方式の例外であること、安定版が出たら再検証することを追記する
- [ ] **Step 7: テンプレート・手順書を直す**。`docs/templates/guide-section-template.md` 4行目と `docs/procedures/new-country-guide.md` 48行目の模範例を `vic3/vic3-japan-guide.md` にする。`new-country-guide.md` 43行目の `eu5/data/` は `{タイトル略称}/data/` に、62行目の `eu5-byzantium-guide.md` の例は「新ガイドへの行内リンク」の一般表現にする
- [ ] **Step 8: 参照切れが無いことを確かめる**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && grep -rnE 'eu5-(hungary|ottoman|universal|brandenburg|castile|austria|byzantium|government|religion|regional|recommended)' --include=*.md --include=*.html . | grep -vE '^\./CHANGELOG\.md:|^\./docs/superpowers/(specs|plans)/2026-03-31-recommended-mods|^\./docs/superpowers/(specs|plans)/2026-10-13-eu5-checklist-reset'
```
Expected: 出力なし（CHANGELOG の過去エントリ、3タイトル共通のMOD仕様書、今回の仕様書・計画は除外）

- [ ] **Step 9: `CHANGELOG.md` に追記する**（先頭に追加）

```markdown
## 2026-10-xx EU5 攻略をプレイ中チェックリストへ作り直し

### Changed
- EU5 の攻略を、どの国でも共通の「いつ・何をするか」をまとめたプレイ中チェックリスト（[eu5-play-checklist.md](eu5/eu5-play-checklist.md)）に一本化した。対象は 1.4 オープンベータ（ビルド 25606497）
- Markdown を読み込み、チェック状態をブラウザに保存して表示する `checklist.html` を追加した
- チェックリストの書式と `[src:]` の実在を検証する `scripts/check_checklist.py` とテストを追加した

### Removed
- EU5 の国別ガイド6本（ブランデンブルク・ハンガリー・オスマン・カスティーリャ・オーストリア（本編＋詳細編）・ビザンツ）、共通ガイド4本（汎用・政体・宗教・地域）、おすすめMOD。git 履歴から復元できる
- 上記に対応する EU5 の設計書6本・実装計画3本
```

- [ ] **Step 10: 最終確認**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest tests.test_check_checklist && python scripts/check_checklist.py eu5/eu5-play-checklist.md
```
ローカルで `index.html` を開き、EU5 のカード2枚から、チェックリストと用語対照表がそれぞれ開けることを確かめる。

- [ ] **Step 11: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && git add -A
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git diff --cached --stat
```
削除・変更されたのが上の Files の範囲だけであることを確かめてから:
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git commit -F - <<'EOF'
eu5: 旧ガイドを削除し、チェックリスト中心の構成へ切り替え

国別6本・共通4本・おすすめMODと関連する設計書・計画を削除し、
index/README/CLAUDE.md/テンプレートの参照を新構成に合わせた。

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
```

- [ ] **Step 12: マージと push の了承を得る**。ユーザーに差分の概要（`git diff --stat main...eu5-checklist-reset`）を示し、main へのマージと push（＝ GitHub Pages への即公開）の了承を得る。了承後:

```bash
cd /c/Users/ramda/projects/paradox-game-guides && git switch main && git merge --no-ff eu5-checklist-reset
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git push origin main
```
push 後、親 workspace repo（`C:\Users\ramda\projects`）でサブモジュール参照を更新してコミットする（`git add paradox-game-guides` → `git diff --cached --stat` → commit）。公開ページ `https://ramdamain-commits.github.io/paradox-game-guides/checklist.html?file=eu5/eu5-play-checklist.md` が開けることを確かめる。
