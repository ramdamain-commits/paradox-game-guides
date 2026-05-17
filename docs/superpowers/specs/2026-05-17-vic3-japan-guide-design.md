# VIC3 日本攻略ガイド 設計書

- 作成日: 2026-05-17
- 対象: VIC3 Patch 1.13 + DLC（日本フィーチャー、海軍改修）
- 想定読者: VIC3 既プレイヤー、日本フルスペック攻略を求める層
- 進め方: 2セッション分割（今セッション=spec+plan+research、次セッション=執筆+検証+コミット）

## ガイドの軸

1. DLC 目玉国家としての日本固有メカニクス
2. 1.13 海軍改修の反映（日本は島国のため独立セクション扱い）

## スコープ

プロイセン版（`vic3/vic3-prussia-guide.md` 361行）と同構成のフルスペック攻略を新規作成。想定 550-700 行。

## 目次

```
# VIC3 日本攻略ガイド（Patch 1.13 + DLC 時点）

## パッチ 1.13 / DLC での日本関連変更点
## 開始状況（1836年）
  ### 周辺国との関係
  ### 初期の強み・弱み
  ### IG構造の特殊性（幕府/藩/学者）           ← 日本固有サブセクション
## 開国の肋（Unrecognized脱却・不平等条約・関税） ← 日本固有、Day 1 前に挿入
## Day 1（ポーズ解除直後）
## 時系列戦略
  ### 序盤（1836〜1860）: 開国対応と国力蓄積
  ### 中盤（1860〜1880）: 明治維新と内戦処理
  ### 終盤（1880〜1936）: 列強入りと帝国運営
## 内政・経済
  ### 建設の優先順位
  ### 利益団体（IG）管理（維新前後の変化）
    #### プロミネンスの活用（1.13）
  ### 法律改正ロードマップ（維新前/維新後で分岐）
## 外交・同盟
  ### 必須外交
  ### Unrecognized → Recognized 昇格ルート
  ### 1.13 で増えた外交手段
## 軍事ドクトリン（陸軍）
  ### 将軍の選び方（1.13 単一指揮官制）
## 海軍ドクトリン（1.13 海軍改修）             ← 日本固有、独立セクション 200-300行
  ### 艦隊編成・製造拠点・進出ルート
## 固有イベント時系列
  ### 明治維新JE 攻略チャート                  ← 期限・前提条件・報酬を表形式
## 技術・法律
## よくあるミス
## 用語対照表
## 出典
```

## 日本固有要素の扱い（プロイセン版にない4点）

1. **海軍ドクトリン**: 独立セクション。1.13 海軍改修の構造変更点を反映。艦隊編成・製造拠点・進出ルート。200-300行
2. **開国の肋**: 序盤に統合セクションとして挿入。Unrecognized脱却判定・不平等条約・関税自主権の喪失と回復
3. **明治維新JE 攻略チャート**: 固有イベント時系列内に独立掲載。前提条件・達成期限・分岐・報酬を表形式
4. **IG構造の特殊性**: 開始状況のサブセクション。Shogunate/Daimyo関連IGと一般的なIGの違い、明治維新前後の変化

## 検証方針

CLAUDE.md 学び「wiki を信じ切らずスクリプト検証を最低 1 つ挟む」を全面適用。DLC 関連スクリプトを網羅的に読んでから執筆。

### researcher 調査範囲

対象パス（`C:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game/`）:

- `events/` 配下の日本関連（japan, meiji, shogunate, restoration を glob 確認）
- `common/journal_entries/` 内 `*japan*`, `*meiji*`, `*shogunate*`, `*restoration*`
- `common/decisions/` 同上
- `common/character_templates/JAP_*` および日本人物テンプレ
- `common/country_definitions/` → JAP 定義、tag swap (JAP→EOJ 等)
- `common/scripted_modifiers/`, `common/static_modifiers/` → 日本固有 modifier
- `common/laws/` → unrecognized 関連、isolationism 関連
- `common/diplomatic_plays/`, `common/diplomatic_actions/` → 開国圧力・不平等条約系
- `common/buildings/` → 日本専用建造物（あれば）
- 海軍改修関連: `common/military_formations/`, `common/combat_unit_*/`, `common/flotilla_*`, `common/coastal_*`
- `localization/japanese/`, `localization/english/` → 用語の正式表記取得

### EU4 派生キーワード除外 grep（最初に流す）

`fabricate_claim`, `forge_claim`, `spy_network`, 領有権主張捏造, 理念グループ, 交易ノード, `Tariff`, `Liberty Desire`, 関税。VIC3 に実在しないものは記述から除外。

### researcher プロンプト規約

- 行番号付きで該当ファイルパスを明示
- 推測禁止、不在は「不在」と明記
- 出力は `paradox-game-guides/vic3/_staging/japan-research.md`（5000-8000 字想定）に Write
- 完了報告は要約 200 字のみ

### レポート章立て指定

1. 1.13/DLC 日本関連 changelog 要約
2. 明治維新 JE（前提条件・期限・報酬・分岐）
3. 開国・不平等条約フロー（イベント連鎖・modifier）
4. 日本固有 IG とプロミネンス挙動
5. 海軍改修の構造変更点（旧→新の差分）
6. 主要人物テンプレ（徳川慶喜・明治天皇・西郷ほか）
7. 開始 modifier・建造物・法律で日本固有のもの一覧
8. EU4 派生メカニクス除外 grep の結果（不在キーワード列挙）

## ファイル配置

### 新規

- `paradox-game-guides/vic3/vic3-japan-guide.md` — ガイド本体（次セッションで執筆）
- `paradox-game-guides/vic3/_staging/japan-research.md` — researcher 出力（gitignore 済、ローカルのみ）

### 更新

- `paradox-game-guides/vic3/localization-reference.md` — 日本関連用語追記
- `paradox-game-guides/CLAUDE.md` — 学びが出たら追記
- `paradox-game-guides/CHANGELOG.md`, `README.md` — リリース時

## 進行プラン

### 今セッション（B方式）

1. spec を `docs/superpowers/specs/2026-05-17-vic3-japan-guide-design.md` に書き出し（本ファイル）
2. 実装計画を `docs/superpowers/plans/2026-05-17-vic3-japan-guide-plan.md` に書き出し（writing-plans スキルで作成）
3. researcher 1回投入 → `_staging/japan-research.md` を確定
4. spec + plan の2点を子 repo にコミット & push、root の submodule 参照を更新

### 次セッション

1. spec + plan + research レポートを読み込み
2. implementer 2-3並列でセクション分担執筆（_staging 経由）
3. reviewer 並列（行番号+一行要約のみ報告）で網羅性チェック
4. 修正 → コミット境界ごとに分割コミット
5. localization-reference.md / CHANGELOG.md / README.md 更新

### 次セッションのコミット境界

1. 海軍ドクトリン以外の本体執筆 → 1コミット
2. 海軍ドクトリン執筆 → 1コミット
3. localization-reference.md 更新 → 1コミット
4. CHANGELOG.md・README.md（必要なら）→ 1コミット

## トークン安全策

- サブエージェント並列は最大3
- レビュアー指示には「行番号+一行要約のみ報告、ファイル全文転記禁止」を必ず含める
- staging ファイルはサブエージェントに直書きさせ、メイン側で中間整形しない
- 1セッションでのバッチ上限は2（CLAUDE.md ルール）

## 成功基準

- スクリプト由来の記述すべてに行番号付き出典が紐づく
- EU4 派生メカニクスが本文に紛れ込んでいない（除外 grep 通過）
- 海軍ドクトリンが 1.13 改修後の構造で書かれている（旧構造の流用が無い）
- 明治維新JE の期限・前提・報酬が表で参照可能
- プロイセン版と同じセクション順で読める（読者が両ガイドを横断しやすい）
