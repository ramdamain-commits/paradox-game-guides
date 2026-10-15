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
# 文字数上限の対象外にする範囲（checklist.html の wrapSrc と同じ。マーカーは既定で非表示のため）
STRIP_SRC_RE = re.compile(r"\[src:[^\]]*\]")
FILE_EXT_RE =re.compile(r"\.(txt|yml|csv|gui|json)$")


class Result(NamedTuple):
    errors: list[str]
    items: int
    chars: int  # [src:] マーカーを除いた文字数


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
    chars = len(STRIP_SRC_RE.sub("", text))
    if chars > MAX_CHARS:
        errors.append(f"文字数 {chars}（[src:] を除く）が上限 {MAX_CHARS} を超えている")
    return Result(errors, items, chars)


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
    print(f"OK: 項目数 {result.items} / 文字数 {result.chars}（[src:] を除く。全体 {len(text)}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
