# EU5 ${COUNTRY_JA}攻略ガイド 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** EU5 ${COUNTRY_JA}（${TAG}）の攻略ガイドを、既存ガイドと同等品質でゲームスクリプト一次ソース方式により作成する

**Architecture:** スクリプト調査→ガイド本文執筆→付随更新+レビューの3フェーズ。イベントファイルが3000行超の場合は調査を並列分割する

**Tech Stack:** Markdown、ゲームスクリプト（Paradox Script）、Git

---

## 変数（Plan 生成時に埋める）

```
TAG            = ${TAG}           # 例: FRA, ENG, POL
COUNTRY_JA     = ${COUNTRY_JA}    # 例: フランス, イングランド
COUNTRY_EN     = ${COUNTRY_EN}    # 例: France, England
EVENT_FILES    = ${EVENT_FILES}   # 例: flavor_FRA.txt (5200行), flavor_fra_hun.txt (300行)
ADVANCE_FILES  = ${ADVANCE_FILES} # 例: country_FRA.txt (200行)
EXTRA_SECTIONS = ${EXTRA_SECTIONS} # 例: 10.5a 百年戦争メカニクス, 10.5b ユグノー戦争
EXTRA_SCRIPTS  = ${EXTRA_SCRIPTS}  # 例: events/hundred_years_war.txt, events/religion/calvinist.txt
```

## スクリプトパス

```
EU5_ROOT = C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis V\game
EVENTS   = ${EU5_ROOT}\in_game\events
DHE      = ${EVENTS}\DHE
COMMON   = ${EU5_ROOT}\in_game\common
LOC      = ${EU5_ROOT}\main_menu\localization\japanese
LOC_DHE  = ${LOC}\events\DHE
GUIDE    = C:\Users\ramda\projects\paradox-game-guides
```

| ファイル | パス | 行数 |
|---------|------|------|
| 固有イベント | `${DHE}/${EVENT_FILES}` | ${EVENT_LINES} |
| 固有進歩 | `${COMMON}/advances/${ADVANCE_FILES}` | ${ADVANCE_LINES} |
| ローカライズ | `${LOC_DHE}/flavor_${TAG_LOWER}_l_japanese.yml` | — |
| （追加調査） | ${EXTRA_SCRIPTS} | — |

---

## フェーズ 1: スクリプト調査

### Task 1: 固有進歩（Advance）ツリー調査

**Files:**
- Read: `${COMMON}/advances/${ADVANCE_FILES}`
- Read: ローカライズ内の advance 関連
- Create: `${GUIDE}/eu5/data/${TAG_LOWER}-advances.md`

- [ ] **Step 1:** 進歩ファイルを全文読み、進歩名・効果・条件を表形式で抽出
- [ ] **Step 2:** ローカライズで日本語名を確認
- [ ] **Step 3:** 中間データファイルに書き出し
- [ ] **Step 4:** コミット

---

### Task 2: 固有イベント調査

**Files:**
- Read: `${DHE}/${EVENT_FILES}`
- Read: ローカライズ
- Create: `${GUIDE}/eu5/data/${TAG_LOWER}-events.md`（+ 分割時は part1/2/3）

**分割判断:**
- 3000行未満 → 単体処理
- 3000行以上 → 3000行ごとに分割、サブエージェント並列起動

各エージェントへの指示:
```
flavor_${TAG}.txt の ${START}〜${END} 行を読み、以下の表形式で全イベントを抽出。
| イベントID | 日本語名 | 発生条件（要約） | 選択肢（日本語） | 主要効果 | src行 |
- 推奨選択の判断は不要。データ抽出のみ
- 効果は主要なものに絞る（modifier, 戦争, 領土変更, 関係変動）
```

- [ ] **Step 1:** イベント分布を確認し、分割境界を決定（必要な場合）
- [ ] **Step 2:** サブエージェントを起動（単体 or 並列）
- [ ] **Step 3:** 結果を統合（分割時）、コミット

---

### Task 3: 追加メカニクス調査（国による — 不要なら省略）

**対象:** ${EXTRA_SCRIPTS}
**出力:** `${GUIDE}/eu5/data/${TAG_LOWER}-extra-mechanics.md`

- [ ] **Step 1:** 追加スクリプトを読み、データ抽出
- [ ] **Step 2:** ローカライズで日本語名確認
- [ ] **Step 3:** コミット

---

## フェーズ 2: ガイド本文執筆

### Task 4: ガイド骨格 + セクション 1-4

- [ ] **Step 1:** セクション 1（タイトル+メタ）
- [ ] **Step 2:** セクション 2（パッチ差分）
- [ ] **Step 3:** セクション 3（開始状況）
- [ ] **Step 4:** セクション 4（Day 1）
- [ ] **Step 5:** コミット

### Task 5: セクション 5-8（時系列・軍事・外交・内政）

- [ ] **Step 1:** セクション 5（時系列戦略）— 序盤/中盤/終盤
- [ ] **Step 2:** セクション 6（軍事ドクトリン）
- [ ] **Step 3:** セクション 7（外交・同盟）
- [ ] **Step 4:** セクション 8（内政・経済）
- [ ] **Step 5:** コミット

### Task 6: セクション 9-10 + 10.5（イベント・進歩・追加セクション）

- [ ] **Step 1:** セクション 9（固有イベント時系列）
- [ ] **Step 2:** セクション 10（固有進歩）
- [ ] **Step 3:** セクション 10.5（${EXTRA_SECTIONS}）— 追加セクションがない場合スキップ
- [ ] **Step 4:** コミット

### Task 7: セクション 11-13（ミス・用語・出典）

- [ ] **Step 1:** セクション 11（よくあるミス）
- [ ] **Step 2:** セクション 12（用語対照表）
- [ ] **Step 3:** セクション 13（出典）
- [ ] **Step 4:** コミット

---

## フェーズ 3: 付随更新+レビュー

### Task 8: 付随ファイル更新

- [ ] **Step 1:** index.html にカード追加
- [ ] **Step 2:** localization-reference.md に新規用語追加
- [ ] **Step 3:** 既存ガイドとの相互リンク追加（双方向）
- [ ] **Step 4:** コミット

### Task 9: レビュー + 中間データ削除

- [ ] **Step 1:** 3名レビュー（熟練者/中級者/テクニカルライター）
- [ ] **Step 2:** レビュー指摘を反映
- [ ] **Step 3:** 中間データ削除（`eu5/data/${TAG_LOWER}-*`）
- [ ] **Step 4:** 最終コミット
