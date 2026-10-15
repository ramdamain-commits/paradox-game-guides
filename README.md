# Paradox Game Guides

Paradox Interactive のグランドストラテジーゲーム攻略メモ集。

## 収録タイトル

### Europa Universalis V

| 資料 | ファイル | 概要 | 対応パッチ |
|------|----------|------|-----------|
| プレイ中チェックリスト | [eu5/eu5-play-checklist.md](eu5/eu5-play-checklist.md)（[`checklist.html`](https://ramdamain-commits.github.io/paradox-game-guides/checklist.html?file=eu5/eu5-play-checklist.md) で表示） | どの国でも共通の「いつ・何をするか」。チェック状態はブラウザに保存 | 1.4 オープンベータ |
| 用語対照表 | [eu5/localization-reference.md](https://ramdamain-commits.github.io/paradox-game-guides/viewer.html?file=eu5/localization-reference.md) | ゲーム内日本語訳と英語名の対照 | — |

### Victoria 3

| 勢力 | ファイル | 難易度 | 対応パッチ |
|------|----------|--------|-----------|
| プロイセン | [vic3/vic3-prussia-guide.md](vic3/vic3-prussia-guide.md) | 中級 | 1.12.4 |

**おすすめMOD**: [vic3/vic3-recommended-mods.md](vic3/vic3-recommended-mods.md)（1.12.4 時点）

### Crusader Kings III

| 勢力 | ファイル | 難易度 | 対応パッチ |
|------|----------|--------|-----------|
| 汎用システム | [ck3/ck3-systems-guide.md](ck3/ck3-systems-guide.md) | 初級〜上級 | 1.19.0.1 |
| イングランド 1066 | [ck3/ck3-england-1066-guide.md](ck3/ck3-england-1066-guide.md) | 中級 | 1.19.0.1 |

**おすすめMOD**: [ck3/ck3-recommended-mods.md](ck3/ck3-recommended-mods.md)（1.19.0.1 時点）

## GitHub Pages

- `index.html` — ゲーム別のガイド一覧トップ
- `viewer.html` — Markdown をブラウザで読むためのビューア
- `checklist.html` — Markdown をチェックリストとして表示するビューア
- 公開先: `https://ramdamain-commits.github.io/paradox-game-guides/`

## 構成

```
eu5/          … Europa Universalis V 攻略（プレイ中チェックリスト＋用語対照表）
vic3/         … Victoria 3 攻略（勢力ガイド + おすすめMOD）
ck3/          … Crusader Kings III 攻略（勢力ガイド + おすすめMOD）
index.html    … GitHub Pages トップ
viewer.html   … Markdown ビューア
checklist.html … Markdown をチェックリストとして表示
scripts/      … 検証スクリプト（check_checklist.py）
tests/        … 検証スクリプトのテスト
docs/         … 内部計画・設計メモ
CLAUDE.md     … 攻略ガイド作成ルール（章テンプレは docs/templates/guide-section-template.md）
```

## ファイル命名規則

```
{タイトル略称}/{タイトル略称}-{勢力名}-guide.md
```

例: `vic3/vic3-prussia-guide.md`, `ck3/ck3-england-1066-guide.md`

EU5 は国別ガイドを置かず、`eu5/eu5-play-checklist.md` を正本とする。

## ガイドの方針

- パッチバージョンを明記し、仕様変更があれば更新する
- 日本語はゲーム内ローカライズ準拠。各ゲームの `localization-reference.md` が用語の正本
- ゲームスクリプトを一次ソースとし、コミュニティ知見と区別する
- 詳細な作成ルールは [CLAUDE.md](CLAUDE.md)、章構成テンプレートは [docs/templates/guide-section-template.md](docs/templates/guide-section-template.md)、新規ガイド追加手順は [docs/procedures/new-country-guide.md](docs/procedures/new-country-guide.md) を参照
