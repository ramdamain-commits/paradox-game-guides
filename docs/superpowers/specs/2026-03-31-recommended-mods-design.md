# おすすめMOD記事 設計書

## 概要

EU5 / VIC3 / CK3 の3タイトルについて、キュレーション型のおすすめMOD記事を作成する。
各タイトル1ファイル、カテゴリ別テーブル形式。

## ファイル

| ファイルパス | 対象 | パッチ |
|-------------|------|--------|
| `eu5/eu5-recommended-mods.md` | Europa Universalis V | 1.1.10 |
| `vic3/vic3-recommended-mods.md` | Victoria 3 | 1.12.4 |
| `ck3/ck3-recommended-mods.md` | Crusader Kings III | 1.18.4 |

## テンプレート構造

各記事は以下のセクション順で構成する。

### 1. タイトル + メタデータ

```markdown
# {タイトル} おすすめMODガイド（Patch X.X.X 時点）

> 信頼性マーカー: MOD情報はコミュニティ知見ベース（コミュニティ知見）。
> YYYY-MM-DD 確認時点。パッチ更新でMOD互換性が変わる場合あり。
> 日本語は原則としてゲーム内ローカライズ準拠。
```

### 2. MOD導入の基本（全タイトル共通内容、各ファイルにインライン記載）

- Steam Workshop のサブスクライブ方法（1-2行）
- ランチャーでのロード順の考え方（1-2行）
- 実績互換の注意（実績非互換MODを使うと実績が解除されない）
- 「incompatible」表示の意味（特にEU5: バージョンチェック機構で表示されるが動作する場合が多い）

### 3. カテゴリ別MODテーブル

各カテゴリは以下のフォーマット:

```markdown
## {カテゴリ名}

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| ... | ... | ... | ... | ... | ... |
```

テーブルの下に必要に応じて1-2行の補足を付ける（互換性の詳細、ロード順の推奨など）。

### 4. 出典

```markdown
## 出典

- **コミュニティ:** GameRant, Reddit, Steam Workshop 等（各URLを記載）
```

## タイトル別カテゴリ構成

### EU5（8 MOD / 4カテゴリ）

| カテゴリ | MOD | 最終更新 | 備考 |
|---------|-----|---------|------|
| ビジュアル変更 | Imperial Papermap | 2026-03-16 | Lite版は実績互換 |
| ビジュアル変更 | Community Flavor Pack | 2025-11-06 | 更新停滞警告付き。作者Paradox入社 |
| UI・便利系 | Nice Wide Mapmode UI | 2025-11-14 | 更新停滞警告付き |
| ゲームプレイ変更 | Formable Nations: Reworked | 2026-03-30 | 140+建国、超アクティブ |
| ゲームプレイ変更 | New World Improvement Project | 2026-03-07 | バニラ上書き多、互換性注意 |
| ゲームプレイ変更 | Way of the Dodo | 2025-12-31 | 追加型イベント、壊れにくい |
| ゲームプレイ変更 | Beyond the Cape | 2026-03-28 | 探検・海軍オーバーホール |
| AI強化 | Xorme AI | 2026-02-03 | EU4同名MOD後継 |

チートカテゴリ: 信頼できる候補なし → 省略

### VIC3（7 MOD / 4カテゴリ）

| カテゴリ | MOD | 最終更新 | 備考 |
|---------|-----|---------|------|
| AI強化 | Kuromi's AI | 2025-12-13 | 65K購読、定番 |
| ゲームプレイ変更 | Victorian Flavor Mod (VFM) | 2026-03-26 | 総合オーバーホール |
| ゲームプレイ変更 | Better Politics Mod (BPM) | 3.0 Beta | 政治システム拡張 |
| ゲームプレイ変更 | Morgenrote - Dawn of Flavor | 2026-03-25 | 文化・ライフスタイル |
| ゲームプレイ変更 | Kikko's Formable Nations | 2025-12-11 | 100+建国 |
| チート・デバッグ | Advanced Cheat Menu ++ | 2025-12-11 | 1.12確認済み |
| フレームワーク | Community Mod Framework | 1.12確認 | 複数MODの前提依存 |

ビジュアルカテゴリ: 信頼できるアクティブ候補なし → 省略

### CK3（10 MOD / 6カテゴリ）

| カテゴリ | MOD | 最終更新 | 備考 |
|---------|-----|---------|------|
| ビジュアル変更 | Community Flavor Pack | 2025-01-27 | 587K購読、更新停滞警告付き |
| ビジュアル変更 | Ethnicities & Portraits Expanded | 2025-03-18 | 331K購読、更新停滞警告付き |
| UI・便利系 | Nameplates | 2025-11-12 | 425K購読 |
| ゲームプレイ変更 | RICE | 2026-02-11 | 43フレーバーパック |
| パフォーマンス | A Culling of the Weak | 2025-11-13 | 約30%改善 |
| チート・デバッグ | Divine Intervention Cheat Menu | 2026-03-14 | 106K購読 |
| 大型変換 | A Game of Thrones | 2026-03 | 566K購読 |
| 大型変換 | Princes of Darkness | 2026-03-12 | World of Darkness |
| 大型変換 | Elder Kings 2 | 1.18.3対応 | Elder Scrolls |

## 更新停滞MODの警告フォーマット

テーブルの注意点列に以下を記載:

```
更新停滞の可能性あり（最終更新: YYYY-MM-DD）。ビジュアル系のため動作継続の可能性は高い
```

## 用語ルール

- 各タイトルの `localization-reference.md` に従う
- MOD名は Steam Workshop 表記をそのまま使用（英語）
- ゲーム内概念の日本語訳は localization-reference.md 準拠
- 信頼性マーカー: 全MODに「（コミュニティ知見）」を冒頭で一括宣言

## 実装順序

1. EU5（最優先、最もアクティブなタイトル）
2. VIC3
3. CK3

## 出典一覧（調査で使用）

### EU5
- GameRant: Best Mods for EU5
- Deltia's Gaming: EU5 5 Best Mods
- Steam Workshop Essential Mods コレクション (ID: 3606622874)
- Taj's EU5 Vanilla++ コレクション (ID: 3617720785)

### VIC3
- GameRant: 18 Best Victoria 3 Mods
- GameWatcher: Best Victoria 3 Mods
- Steam Workshop Must Have コレクション (ID: 3258909663)

### CK3
- Seven Swords: Best CK3 Mods 2026
- TheGamer: 16 Best Mods for CK3
- PC Gamer: Best CK3 Mods
- Sensible CK3 2026 コレクション (ID: 3596996385)
