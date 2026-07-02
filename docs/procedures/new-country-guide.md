# 新規国別ガイド追加の手順（定型パターン）

> 2026-07-03 に CLAUDE.md から分離。章構成の正本は `guide-section-template.md`、Plan 変数は `country-guide-plan-template.md`。

新しい国の攻略ガイドを追加するとき、ブレスト→Spec→Plan の儀式は不要。以下の手順で即実行する。

### 1. ファイル探索（5分）

```bash
EU5_ROOT="C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis V\game"
TAG=XXX  # 国タグ（HAB, TUR, BRA 等）

# 固有イベント
ls "${EU5_ROOT}/in_game/events/DHE/" | grep -i "flavor_${TAG}"
wc -l "${EU5_ROOT}/in_game/events/DHE/flavor_${TAG}"*.txt

# 固有進歩
ls "${EU5_ROOT}/in_game/common/advances/" | grep -i "country_${TAG}"
wc -l "${EU5_ROOT}/in_game/common/advances/country_${TAG}"*.txt

# ローカライズ
ls "${EU5_ROOT}/main_menu/localization/japanese/events/DHE/" | grep -i "flavor_${TAG}"

# 汎用メカニクス（国による：HRE, 宗教, 地域等）
# → 必要なものだけ追加調査
```

### 2. Plan 生成

`docs/templates/country-guide-plan-template.md` の変数を埋める:
- `${TAG}`, `${COUNTRY_JA}`, `${COUNTRY_EN}`
- `${EVENT_FILES}`, `${EVENT_LINES}`, `${ADVANCE_FILES}`
- `${EXTRA_SECTIONS}` — 10.5 の追加セクション（HRE, 宗教改革等。なければ空）
- `${EXTRA_SCRIPTS}` — 汎用メカニクスの追加調査対象

Plan をコミットしたら即 subagent-driven-development で実行。

### 3. 調査フェーズ（サブエージェント並列）

- flavor_XXX.txt が **3000行以上** → 3000行ごとに分割して並列起動
- flavor_XXX.txt が **3000行未満** → 単体で処理
- 固有進歩・汎用メカニクスは独立タスクとして並列起動
- 中間データは `eu5/data/` に Markdown テーブルで出力

### 4. 執筆フェーズ

- テンプレート（本ファイルのセクション構成）に従い、中間データを元に執筆
- 模範例: `eu5/eu5-ottoman-guide.md`, `eu5/eu5-hungary-guide.md`

### 5. 付随更新（必ず4点セットで todo に入れる）

メインのガイドファイル作成と**同一コミット内で**完了させる:

1. **`index.html`** にカード追加（既存カード群と同じ HTML 構造を踏襲）
2. **`localization-reference.md`** に新規用語追加（ゲーム内ローカライズで日本語名確認）
3. **`CHANGELOG.md`** に新規ガイド追加エントリ（行数・主要章・スクリプト検証範囲を明記）
4. **地域ガイド（`{ゲーム}-regional-guide.md`）** の難易度評価・推奨度を再評価し、新ガイドへの相互リンクを追加（双方向）

**運用ルール**:
- implementer 委任時は「本体作成のみ。付随4点はメインで実施」と責任範囲を明示する。implementer が付随更新まで担うとファイル間整合のミスが起きやすい（実例: 2026-05-16 ビザンツガイド追加時、当初 implementer プロンプトに付随更新を含めず後から system-reminder で気付いた）
- ブレスト段階の todo 作成時に**最初から付随更新4点を含める**。「実装→付随更新を後から追加」の流れだと CLAUDE.md 再読込で気付くまでロスする
- 地域ガイドの評価更新は「⚠ 非推奨」「上級者向け」等の難易度ラベルだけでなく、新ガイドへの行内リンク（`[eu5-byzantium-guide.md](eu5-byzantium-guide.md)`）まで含める

### ブレスト・Spec が必要になるケース

- 国固有の大規模メカニクスがあり、追加セクション（10.5）の設計判断が必要な場合
- 既存テンプレートに収まらない特殊な国（遊牧民、植民地国家等）
- ユーザーが特定の切り口（軍事特化、外交特化等）を求めた場合

上記に該当しなければ、ブレスト・Spec をスキップして Plan テンプレートから即実行する。
