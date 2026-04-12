# Paradox Game Guides

Paradox Interactive のグランドストラテジーゲーム攻略メモ集。

## 収録タイトル

### Europa Universalis V

| 勢力 | ファイル | 難易度 | 対応パッチ |
|------|----------|--------|-----------|
| ブランデンブルク | [eu5/eu5-brandenburg-guide.md](eu5/eu5-brandenburg-guide.md) | 中級〜上級 | 1.1.10 |
| ハンガリー | [eu5/eu5-hungary-guide.md](eu5/eu5-hungary-guide.md) | 初級〜中級 | 1.1.10 |
| オスマン帝国 | [eu5/eu5-ottoman-guide.md](eu5/eu5-ottoman-guide.md) | 初級〜中級 | 1.1.10 |
| カスティーリャ | [eu5/eu5-castile-guide.md](eu5/eu5-castile-guide.md) | 初級〜中級 | 1.1.10 |

#### 共通システム

| テーマ | ファイル | 概要 | 対応パッチ |
|--------|----------|------|-----------|
| 汎用攻略 | [eu5/eu5-universal-guide.md](eu5/eu5-universal-guide.md) | 国家共通の序盤運営・拡張指針 | 1.1.10 |
| 政体 | [eu5/eu5-government-guide.md](eu5/eu5-government-guide.md) | 君主制・共和国・神権制などの違い | 1.1.10 |
| 宗教 | [eu5/eu5-religion-guide.md](eu5/eu5-religion-guide.md) | 宗教グループ別の固有メカニクス | 1.1.10 |
| 地域 | [eu5/eu5-regional-guide.md](eu5/eu5-regional-guide.md) | 地域別の難易度とおすすめ国家 | 1.1.10 |

**おすすめMOD**: [eu5/eu5-recommended-mods.md](eu5/eu5-recommended-mods.md)（1.1.10 時点）

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
- 公開先: `https://ramdamain-commits.github.io/paradox-game-guides/`

## 構成

```
eu5/          … Europa Universalis V 攻略（勢力ガイド + おすすめMOD）
vic3/         … Victoria 3 攻略（勢力ガイド + おすすめMOD）
ck3/          … Crusader Kings III 攻略（勢力ガイド + おすすめMOD）
index.html    … GitHub Pages トップ
viewer.html   … Markdown ビューア
docs/         … 内部計画・設計メモ
CLAUDE.md     … 攻略ガイド作成ルール・テンプレート
```

## ファイル命名規則

```
{タイトル略称}/{タイトル略称}-{勢力名}-guide.md
```

例: `eu5/eu5-brandenburg-guide.md`, `ck3/ck3-england-1066-guide.md`

## ガイドの方針

- パッチバージョンを明記し、仕様変更があれば更新する
- 日本語はゲーム内ローカライズ準拠。各ゲームの `localization-reference.md` が用語の正本
- ゲームスクリプトを一次ソースとし、コミュニティ知見と区別する
- 詳細な作成ルールとテンプレートは [CLAUDE.md](CLAUDE.md) を参照
