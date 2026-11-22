"""置換リスト(JSON)をチェックリストへ適用する。old が指定行で一意に1回だけ出ることを確かめてから置換する。

使い方: python scripts/apply_fixes.py <md> <fix1.json> [<fix2.json> ...] [--dry]
手順は docs/procedures/patch-update.md
"""
import json
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if a != "--dry"]
dry = "--dry" in sys.argv
md = Path(args[0])
lines = md.read_text(encoding="utf-8").split("\n")
fixes = []
for f in args[1:]:
    for fx in json.loads(Path(f).read_text(encoding="utf-8")):
        fx["_src"] = Path(f).name
        fixes.append(fx)

errors = []
seen = {}
for fx in fixes:
    i = fx["md_line"] - 1
    key = (i, fx["old"])
    if key in seen:
        errors.append(f"重複: md:{fx['md_line']} {fx['old']!r}（{seen[key]} と {fx['_src']}）")
        continue
    seen[key] = fx["_src"]
    n = lines[i].count(fx["old"])
    if n != 1:
        errors.append(f"md:{fx['md_line']} に old が {n} 回: {fx['old']!r}（{fx['_src']}）")
        continue
    lines[i] = lines[i].replace(fx["old"], fx["new"], 1)

sys.stdout.reconfigure(encoding="utf-8")
print(f"置換 {len(fixes) - len(errors)} / {len(fixes)} 件")
for e in errors:
    print("NG", e)
if not dry and not errors:
    md.write_text("\n".join(lines), encoding="utf-8")
    print("書き込み済み")
elif errors:
    print("エラーがあるため書き込まない")
    sys.exit(1)
