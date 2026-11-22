#!/usr/bin/env python3
"""チェックリストの [src:] が指す中身を、インストール版のゲームファイルから引いて一覧にする。

パッチ更新のときに、行番号つきの出典（file:行）がまだ同じ記述を指しているか、
ローカライズキー（file, key）がまだあって文言が変わっていないかを目で確かめるための補助。
check_checklist.py はファイル名の実在しか見ないので、こちらで中身を見る。

使い方: python scripts/dump_src.py vic3/vic3-play-checklist.md [--game-dir DIR] [--out FILE]
出力: 項目ID ごとに、各 [src:] の解決先パスと中身（行参照はその行、キー参照はキーの行）。
      見つからない参照・空行や括弧だけの行を指す参照には先頭に "!!" を付ける。
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_checklist import GAME_DIRS, REPO_ROOT  # noqa: E402

SRC_RE = re.compile(r"\[src:\s*([^\]]+)\]")
ID_RE = re.compile(r"\{#([^}]*)\}\s*$")
LINE_REF_RE = re.compile(r"^(?P<file>[^,:]+):(?P<a>\d+)(?:-(?P<b>\d+))?$")
KEY_REF_RE = re.compile(r"^(?P<file>[^,]+),\s*(?P<key>.+)$")
TRIVIAL_LINE_RE = re.compile(r"^\s*([{}]\s*)*(#.*)?$")


def index_files(game_dir: Path) -> dict[str, list[Path]]:
    idx: dict[str, list[Path]] = defaultdict(list)
    for p in game_dir.rglob("*"):
        if p.is_file():
            idx[p.name].append(p)
    return idx


def pick(paths: list[Path]) -> Path:
    """同名ファイルが複数あるときは日本語ローカライズを優先し、次に dlc 以外を選ぶ。"""
    def rank(p: Path) -> tuple[int, int, str]:
        s = p.as_posix()
        return ("/japanese/" not in s, "/dlc/" in s, s)
    return sorted(paths, key=rank)[0]


def read_lines(path: Path, cache: dict[Path, list[str]]) -> list[str]:
    if path not in cache:
        cache[path] = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    return cache[path]


def resolve(ref: str, idx, game_dir: Path, cache) -> list[str]:
    ref = ref.strip()
    m = LINE_REF_RE.match(ref)
    if m:
        name = m["file"].strip().rsplit("/", 1)[-1]
        if name not in idx:
            return [f"!! {ref}: ファイルが無い"]
        path = pick(idx[name])
        lines = read_lines(path, cache)
        a = int(m["a"])
        b = int(m["b"] or a)
        rel = path.relative_to(game_dir).as_posix()
        out = []
        for n in range(a, b + 1):
            if n > len(lines):
                out.append(f"!! {rel}:{n}: 行が無い（全{len(lines)}行）")
                continue
            text = lines[n - 1].strip()
            flag = "!! " if TRIVIAL_LINE_RE.match(text) else "   "
            out.append(f"{flag}{rel}:{n}: {text[:200]}")
        return out
    m = KEY_REF_RE.match(ref)
    if m:
        name = m["file"].strip().rsplit("/", 1)[-1]
        key = m["key"].strip()
        if name not in idx:
            return [f"!! {ref}: ファイルが無い"]
        path = pick(idx[name])
        lines = read_lines(path, cache)
        rel = path.relative_to(game_dir).as_posix()
        pat = re.compile(r"^\s*" + re.escape(key) + r"\s*[:=]")
        for n, line in enumerate(lines, 1):
            if pat.match(line):
                return [f"   {rel}:{n}: {line.strip()[:400]}"]
        # キーが識別子でない（"Contestion Type" 等）ときは部分一致で探す
        for n, line in enumerate(lines, 1):
            if key in line:
                return [f"~~ {rel}:{n}: {line.strip()[:400]}"]
        return [f"!! {ref}: キーが見つからない（{rel}）"]
    return [f"?? {ref}: 書式を解釈できない"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("--game-dir")
    ap.add_argument("--out")
    args = ap.parse_args()
    md = Path(args.md)
    if not md.is_absolute():
        md = (Path.cwd() / md).resolve()
    game = md.relative_to(REPO_ROOT).parts[0]
    game_dir = Path(args.game_dir) if args.game_dir else GAME_DIRS[game]
    idx = index_files(game_dir)
    cache: dict[Path, list[str]] = {}
    out: list[str] = []
    current = "(冒頭)"
    bad = 0
    for ln, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
        m = ID_RE.search(line)
        if m:
            current = m.group(1)
            out.append(f"\n## {current} (md:{ln})")
        refs = SRC_RE.findall(line)
        if not refs:
            continue
        if not m:
            out.append(f"-- md:{ln}")
        for ref in refs:
            for r in resolve(ref, idx, game_dir, cache):
                out.append(r)
                if r.startswith(("!!", "??")):
                    bad += 1
    text = "\n".join(out) + f"\n\n要確認（!! / ??）: {bad} 件\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"書き出し: {args.out}（要確認 {bad} 件）")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
