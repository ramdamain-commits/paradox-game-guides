# EU5 オーストリア攻略ガイド 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** EU5 オーストリア（HAB）の攻略ガイドを、既存4国ガイドと同等品質でゲームスクリプト一次ソース方式により作成する

**Architecture:** スクリプト調査（Task 1-4）→ ガイド本文執筆（Task 5-8）→ 付随更新+レビュー（Task 9-10）の3フェーズ。flavor_HAB.txt が 10,388行/172イベントと大規模なため、調査フェーズはサブエージェント並列分割する

**Tech Stack:** Markdown、ゲームスクリプト（Paradox Script）、Git

**Spec:** `docs/superpowers/specs/2026-04-11-eu5-austria-guide-design.md`

---

## スクリプトパス一覧

以後のタスクで使うファイルパスをここで一括定義する。

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
| 固有イベント | `${DHE}/flavor_HAB.txt` | 10,388 |
| チロル固有イベント | `${DHE}/flavor_hab_tir.txt` | 626 |
| 固有進歩 | `${COMMON}/advances/country_HAB.txt` | 177 |
| HRE 定義 | `${COMMON}/international_organizations/hre.txt` | 911 |
| 婚姻連合 | `${COMMON}/international_organizations/marriage_union.txt` | 79 |
| 連合 | `${COMMON}/international_organizations/union.txt` | 334 |
| HRE イベント | `${EVENTS}/hre.txt` | 1,084 |
| 政府改革イベント | `${EVENTS}/government_reforms.txt` | 352 |
| HAB ローカライズ | `${LOC_DHE}/flavor_hab_l_japanese.yml` | — |
| チロルローカライズ | `${LOC_DHE}/flavor_hab_tir_l_japanese.yml` | — |
| 国際組織ローカライズ | `${LOC}/international_organizations_l_japanese.yml` | — |

---

## フェーズ 1: スクリプト調査（Task 1-4）

### Task 1: 固有進歩（Advance）ツリー調査

**目的:** オーストリア固有進歩の全件リスト+効果+条件を抽出

**Files:**
- Read: `${COMMON}/advances/country_HAB.txt`（177行）
- Read: `${LOC}/` 内の HAB advance 関連ローカライズ
- Create: `${GUIDE}/eu5/data/hab-advances.md`（中間データ）

- [ ] **Step 1: country_HAB.txt を全文読み、進歩名・効果・条件を表形式で抽出**

出力形式:
```markdown
| 進歩名（英語） | 日本語名 | 時代 | 条件 | 効果 | src |
|---------------|---------|------|------|------|-----|
```

- [ ] **Step 2: ローカライズファイルで日本語名を確認**

`${LOC}/` 内を `country_HAB` で grep し、各進歩の正式日本語名を取得。

- [ ] **Step 3: 中間データファイルに書き出し**

`eu5/data/hab-advances.md` に表を保存。このファイルは最終ガイドに統合後に削除してよい。

- [ ] **Step 4: コミット**

```bash
cd ${GUIDE} && git add eu5/data/hab-advances.md && git commit -m "data: オーストリア固有進歩の調査データ"
```

---

### Task 2: 固有イベント調査（flavor_HAB.txt — 並列分割）

**目的:** 172個のイベントを全件抽出し、イベント一覧表を作成

**Files:**
- Read: `${DHE}/flavor_HAB.txt`（10,388行）
- Read: `${DHE}/flavor_hab_tir.txt`（626行）
- Read: `${LOC_DHE}/flavor_hab_l_japanese.yml`
- Read: `${LOC_DHE}/flavor_hab_tir_l_japanese.yml`
- Create: `${GUIDE}/eu5/data/hab-events.md`（中間データ）

**並列分割方針:** flavor_HAB.txt を行番号で3分割し、サブエージェント3体に委任。各エージェントは担当範囲のイベントID・条件・選択肢・効果を表形式で抽出する。

- [ ] **Step 1: イベントIDの分布を確認し、3分割の境界を決定**

```bash
grep -n "flavor_hab\." "${DHE}/flavor_HAB.txt" | head -1
grep -n "flavor_hab\." "${DHE}/flavor_HAB.txt" | awk -F: 'NR==1{first=$1} END{print first, $1, NR}'
```

おおよそ 1-3500行、3501-7000行、7001-10388行 で3分割する（イベント境界で調整）。

- [ ] **Step 2: サブエージェント3体を並列起動**

各エージェントへの指示テンプレート:

```
flavor_HAB.txt の ${START}〜${END} 行を読み、以下の表形式で全イベントを抽出してください。

| イベントID | 日本語名 | 発生条件（トリガー） | 選択肢（日本語） | 選択肢の主要効果 | src行番号 |

- 日本語名は ${LOC_DHE}/flavor_hab_l_japanese.yml で確認
- 選択肢は全選択肢を列挙（推奨選択の判断は不要、データのみ）
- 効果は modifier, add_xxx, remove_xxx 等の主要なものだけ
- 出力は Markdown テーブルで
- 変更は一切行わない（読み取り専用）
```

- [ ] **Step 3: flavor_hab_tir.txt を別途調査**

626行なので単体で処理可能。同じ表形式で抽出。

- [ ] **Step 4: 3体の結果を統合し hab-events.md に書き出し**

イベントIDの番号順にソート。重複チェック。

- [ ] **Step 5: コミット**

```bash
cd ${GUIDE} && git add eu5/data/hab-events.md && git commit -m "data: オーストリア固有イベント172件の調査データ"
```

---

### Task 3: HRE メカニクス調査

**目的:** HRE の皇帝権限・帝国改革・選帝侯メカニクスをデータ化

**Files:**
- Read: `${COMMON}/international_organizations/hre.txt`（911行）
- Read: `${EVENTS}/hre.txt`（1,084行）
- Read: `${EVENTS}/government_reforms.txt`（352行）
- Read: `${LOC}/international_organizations_l_japanese.yml`
- Create: `${GUIDE}/eu5/data/hab-hre-mechanics.md`（中間データ）

- [ ] **Step 1: hre.txt（組織定義）を読み、以下を抽出**

```markdown
## 皇帝権限
| 権限名（英語） | 日本語名 | 効果 | src |

## 帝国改革
| 改革名（英語） | 日本語名 | 条件 | 効果 | src |

## 選帝侯
| メカニクス | 内容 | src |
```

- [ ] **Step 2: hre.txt（イベント）を読み、HRE 運営に関わるイベントを抽出**

皇帝選挙、帝国防衛、諸侯反乱等のイベントを表形式で。

- [ ] **Step 3: government_reforms.txt から HRE 関連改革を抽出**

- [ ] **Step 4: ローカライズで日本語名を確認**

- [ ] **Step 5: 中間データファイルに書き出し+コミット**

```bash
cd ${GUIDE} && git add eu5/data/hab-hre-mechanics.md && git commit -m "data: HRE メカニクス調査データ"
```

---

### Task 4: 婚姻・連合メカニクス調査

**目的:** 婚姻→同君連合の成立条件を確認

**Files:**
- Read: `${COMMON}/international_organizations/marriage_union.txt`（79行）
- Read: `${COMMON}/international_organizations/union.txt`（334行）
- Create: `${GUIDE}/eu5/data/hab-union-mechanics.md`（中間データ）

- [ ] **Step 1: marriage_union.txt を全文読み、婚姻連合の条件・効果を抽出**

- [ ] **Step 2: union.txt を全文読み、同君連合（Personal Union）の成立・維持・解消条件を抽出**

確率式か確定かを明記。

- [ ] **Step 3: 中間データファイルに書き出し+コミット**

```bash
cd ${GUIDE} && git add eu5/data/hab-union-mechanics.md && git commit -m "data: 婚姻・連合メカニクス調査データ"
```

---

## フェーズ 2: ガイド本文執筆（Task 5-8）

### Task 5: ガイド骨格 + セクション 1-4 執筆

**目的:** ガイドファイルを作成し、メタ情報〜Day 1 までを執筆

**Files:**
- Create: `${GUIDE}/eu5/eu5-austria-guide.md`
- Read: `${GUIDE}/eu5/eu5-ottoman-guide.md`（模範例として構成参照）
- Read: `${GUIDE}/eu5/data/hab-advances.md`
- Read: `${GUIDE}/eu5/data/hab-events.md`

- [ ] **Step 1: セクション 1（タイトル+メタ）を執筆**

```markdown
# EU5 オーストリア攻略ガイド（Patch 1.1.10 時点）

> オーストリア → ハプスブルク外交と神聖ローマ帝国運営を両立する序盤から帝国改革完遂までの整理。
> 2026-04-11 確認時点の最新公開ホットフィックス 1.1.10 に合わせて更新。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。
```

- [ ] **Step 2: セクション 2（パッチ差分）を執筆**

Task 1-3 の調査データ + 既存ガイドのパッチ差分セクションを参照し、HAB に影響する変更を表形式で記載。1.2 ベータ情報はオスマンガイドの形式に合わせる。

- [ ] **Step 3: セクション 3（開始状況）を執筆**

スクリプトデータから HAB の開始状態（皇帝ステータス、周辺国テーブル、強み・弱み）を記載。

- [ ] **Step 4: セクション 4（Day 1）を執筆**

皇帝としての初動を番号付きリストで。

- [ ] **Step 5: コミット**

```bash
cd ${GUIDE} && git add eu5/eu5-austria-guide.md && git commit -m "feat: オーストリアガイド骨格+セクション1-4"
```

---

### Task 6: セクション 5-8 執筆（時系列戦略・軍事・外交・内政）

**Files:**
- Modify: `${GUIDE}/eu5/eu5-austria-guide.md`
- Read: 全中間データファイル

- [ ] **Step 1: セクション 5（時系列戦略）を執筆**

序盤（1337-1400）、中盤（1400-1500）、終盤（1500-）の3段構成。各段で「目標→手順→注意点」を記載。イベントは概要のみ触れ、詳細はセクション 9 へ誘導。

- [ ] **Step 2: セクション 6（軍事ドクトリン）を執筆**

固有ユニット、帝国防衛軍の活用、兵科比率テーブル。

- [ ] **Step 3: セクション 7（外交・同盟）を執筆**

必須同盟・推奨関係テーブル。ハプスブルク婚姻外交の概要（詳細は 10.5b へ誘導）。既存ガイドへの相互リンクを含む。

- [ ] **Step 4: セクション 8（内政・経済）を執筆**

建造物優先順位、階級管理、帝国領の収入構造。

- [ ] **Step 5: コミット**

```bash
cd ${GUIDE} && git add eu5/eu5-austria-guide.md && git commit -m "feat: オーストリアガイド セクション5-8（時系列・軍事・外交・内政）"
```

---

### Task 7: セクション 9-10 + 10.5 執筆（イベント・進歩・追加セクション）

**Files:**
- Modify: `${GUIDE}/eu5/eu5-austria-guide.md`
- Read: 全中間データファイル

- [ ] **Step 1: セクション 9（固有イベント時系列）を執筆**

hab-events.md のデータを元に、テンプレートの表形式（イベント名・ID・発生条件・推奨選択・効果）で全件記載。172件を時系列 or テーマ別にグルーピング。

- [ ] **Step 2: セクション 10（固有進歩）を執筆**

hab-advances.md のデータを元に、時代別に整理。

- [ ] **Step 3: セクション 10.5a（神聖ローマ帝国運営）を執筆**

hab-hre-mechanics.md のデータを元に、皇帝権限・帝国改革・選帝侯管理・帝国防衛を記載。eu5-government-guide との重複を避け、オーストリア固有の運用視点で書く。

- [ ] **Step 4: セクション 10.5b（ハプスブルク婚姻外交）を執筆**

hab-union-mechanics.md のデータを元に、婚姻→同君連合の条件・戦略を記載。

- [ ] **Step 5: セクション 10.5c の判断**

宗教改革がオーストリア固有の分量を持つか、調査データから判断。
- 固有分量がある → 独立セクションとして執筆
- 薄い → 10.5a の「帝国運営」に統合（1サブセクションとして）

- [ ] **Step 6: コミット**

```bash
cd ${GUIDE} && git add eu5/eu5-austria-guide.md && git commit -m "feat: オーストリアガイド セクション9-10.5（イベント・進歩・HRE・婚姻外交）"
```

---

### Task 8: セクション 11-13 執筆（よくあるミス・用語・出典）

**Files:**
- Modify: `${GUIDE}/eu5/eu5-austria-guide.md`

- [ ] **Step 1: セクション 11（よくあるミス）を執筆**

オーストリア固有 + HRE 全般の2部構成。

- [ ] **Step 2: セクション 12（用語対照表）を執筆**

HRE 関連用語を重点的に。localization-reference.md へのリンクを含める。

- [ ] **Step 3: セクション 13（出典）を執筆**

一次情報（スクリプトファイル名一覧）とコミュニティ情報を分離。

- [ ] **Step 4: コミット**

```bash
cd ${GUIDE} && git add eu5/eu5-austria-guide.md && git commit -m "feat: オーストリアガイド セクション11-13（ミス・用語・出典）"
```

---

## フェーズ 3: 付随更新+レビュー（Task 9-10）

### Task 9: 付随ファイル更新

**Files:**
- Modify: `${GUIDE}/index.html`
- Modify: `${GUIDE}/eu5/localization-reference.md`
- Modify: 既存ガイド（相互リンク追加）

- [ ] **Step 1: index.html にオーストリアガイドのカードを追加**

EU5 セクションの `card-list` に `<li>` を追加。リンクは `viewer.html?file=eu5/eu5-austria-guide.md` 形式。

- [ ] **Step 2: localization-reference.md に HRE 用語を追加**

Task 3 で確認した HRE 用語のうち、未登録のものを追加。

- [ ] **Step 3: 既存ガイドに相互リンクを追加**

spec の「相互参照（双方向）」テーブルに従い、ブランデンブルク・ハンガリー・eu5-government-guide からオーストリアガイドへのリンクを追加。

- [ ] **Step 4: コミット**

```bash
cd ${GUIDE} && git add index.html eu5/localization-reference.md eu5/eu5-brandenburg-guide.md eu5/eu5-hungary-guide.md eu5/eu5-government-guide.md && git commit -m "feat: オーストリアガイド付随更新（index・用語・相互リンク）"
```

---

### Task 10: レビュー + 中間データ削除

**Files:**
- Read: `${GUIDE}/eu5/eu5-austria-guide.md`（完成版）
- Delete: `${GUIDE}/eu5/data/` ディレクトリ（中間データ）

- [ ] **Step 1: 3名レビュー（サブエージェント）**

CLAUDE.md のレビュー仕様に従い、以下3名でレビュー:
- **熟練者**: 戦略の正確性、パッチ対応、抜け漏れ
- **中級者**: 用語の正確性、ゲーム内表記との一致
- **テクニカルライター**: 構成統一、表記揺れ、保守性

レビュー指摘は「問題箇所の行番号+周辺コードのみ報告」形式。

- [ ] **Step 2: レビュー指摘をガイド本体に反映**

- [ ] **Step 3: 中間データを削除**

```bash
cd ${GUIDE} && rm -rf eu5/data/ && git add -A eu5/data/ && git commit -m "chore: オーストリアガイド中間データを削除"
```

- [ ] **Step 4: 最終確認+完了コミット**

`git diff --stat` で想定外の変更がないか確認。
