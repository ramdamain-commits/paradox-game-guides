# CK3 汎用システムガイド + ローカライズ対照表 1.19 拡充 実装計画

> 状態: 2026-04-10 時点で `ck3/ck3-systems-guide.md` と `index.html` への反映は完了済み。本文の checkbox は実装履歴として残し、成果物側を正本とする。

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** CK3 1.19 Scribe のローカライズ対照表拡充と汎用システムガイドを作成する

**Architecture:** ローカライズ対照表を先に更新（システムガイドが参照するため）、次にシステムガイドを執筆。スクリプトからの数値抽出はガイド執筆と並行。

**Tech Stack:** Markdown、CK3ゲームスクリプト（`C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game\`）

**設計書:** `docs/superpowers/specs/2026-04-09-ck3-systems-guide-design.md`

---

## Task 1: ローカライズ対照表 — パッチ番号更新 + 正統性・封臣スタンス追加

**Files:**
- Modify: `ck3/localization-reference.md`

**スクリプト参照先:**
- `localization/japanese/game_concepts_l_japanese.yml` — 正統性、封臣スタンス、権力の秤
- `localization/japanese/vassal_stances_l_japanese.yml` — 封臣スタンス名
- `localization/japanese/activities/coronation_activity_l_japanese.yml` — 戴冠式・誓約

- [ ] **Step 1: パッチ番号を更新**

`ck3/localization-reference.md` の冒頭:
```
確認パッチ: **1.18.4**（2026-03-31 確認）
```
↓
```
確認パッチ: **1.19.0.1**（2026-04-09 確認）
```

- [ ] **Step 2: 正統性カテゴリを追加**

「## その他」セクションの直前に新セクションを挿入:

```markdown
## 正統性

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Legitimacy | 正統性 | 統治者の支配権の正当性（1.19新設） |
| Legitimacy Level | 正統性レベル | 5段階 + 非正統の計6段階 |
| Legitimacy Expectations | 正統性への期待 | 封臣が主君に要求する正統性の水準 |
| Initial Legitimacy | 初期正統性 | 統治者就任時に計算される初期値 |
| Coronation | 戴冠式 | 正統性を大幅に獲得する活動 |
| Oath | 誓約 | 戴冠式で宣言する統治方針 |
| Scales of Power | 権力の秤 | 統治者と摂政の権力バランス |
| Diarch | 共同統治者 | 権力を共有する相手 |
| Diarchy | 権力の共有 | 統治者が封臣/廷臣と権限を共有する状態 |

## 封臣スタンス

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Vassal Stance | 封臣のスタンス | 封臣の態度・傾向 |
| Courtly | 礼節 | 宮廷の華やかさを重視 |
| Parochial | 地方主義 | 地域の自治を重視 |
| Glory Hound | 名誉追求者 | 戦争の勝利を重視 |
| Zealot | 狂信 | 宗教的純粋さを重視 |
| Minority | 少数派 | 文化的少数派の権利を重視 |
| Barons and Minor Landholders | 弱小地主 | 低い税と自由を重視 |
| Belligerent | 好戦的 | 積極的な拡張を重視 |
```

- [ ] **Step 3: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides
git add ck3/localization-reference.md
git commit -m "$(cat <<'EOF'
更新: CK3ローカライズ対照表 — 1.19正統性・封臣スタンス追加

パッチ番号を1.19.0.1に更新。正統性（Legitimacy）セクション、
封臣スタンス（Vassal Stance）セクションを新設。

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 2: ローカライズ対照表 — 叙勲・徴税スロット・教育特性追加

**Files:**
- Modify: `ck3/localization-reference.md`

**スクリプト参照先:**
- `localization/japanese/accolades/accolades_l_japanese.yml` — 叙勲用語
- `localization/japanese/traits_l_japanese.yml` — 教育特性Lv5名
- `common/tax_slots/types/00_tax_slot_types.txt` — 徴税スロット
- `localization/japanese/culture/cultural_innovations_l_japanese.yml` — 台帳イノベーション

- [ ] **Step 1: 叙勲カテゴリを追加**

「## 封臣スタンス」セクションの直後に挿入:

```markdown
## 叙勲

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Accolade | 叙勲 | 騎士への栄誉。1.19で刷新 |
| Accolade Type | 叙勲の種別 | 騎士のスキル・特性で決定 |
| Accolade Rank | 叙勲ランク | Glory蓄積で上昇 |
| Glory | 栄光 | 叙勲の成長リソース |
| Acclaimed Knight | 叙勲された騎士 | 叙勲対象の騎士 |
```

- [ ] **Step 2: 氏族政体・遊牧関連の用語を追加**

「## 政体」セクション末尾に追加:

```markdown
| Administrative | 官僚制 | ビザンツ系の政体（DLC: Roads to Power） |
| Nomadic | 遊牧政体 | 遊牧民の政体（DLC: Roads to Power） |
| Mandala | マンダラ政体 | 東南アジアの政体（DLC: Roads to Power） |
```

「## 叙勲」セクションの直後に挿入:

```markdown
## 徴税（氏族政体）

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Tax Slot | 徴税スロット | 氏族政体の徴税管理（1.19新設） |
| Tax Collector | 徴税官 | 徴税スロットの管理者 |
| Obligation | 義務 | 徴税スロットの税制種別 |
| Tax Jurisdiction | 徴税管轄 | 宰相が提供する追加スロット |
```

- [ ] **Step 3: 教育特性の表を拡充**

「## ライフスタイル」の「### 能力（スキル）」の直後に新サブセクションを追加:

```markdown
### 教育特性（Lv5のみ — 全レベルはシステムガイド参照）

| 英語 | ゲーム内日本語 | 系統 | domain_limit |
|------|---------------|------|-------------|
| education_intrigue_5 | 神算鬼謀の人形師 | 策略 | +3 |
| education_diplomacy_5 | 超絶技巧の調停者 | 外交 | +3 |
| education_stewardship_5 | 黄金の君主 | 管理 | +3 |
| education_martial_5 | 無双の軍神 | 軍事 | +3 |
| education_learning_5 | 博覧強記の託宣者 | 学識 | +3 |

> **1.19変更**: 直轄領上限（Domain Limit）が管理スキル依存から教育特性レベル依存に変更された。詳細は `ck3-systems-guide.md` を参照。
```

- [ ] **Step 4: 文化イノベーションに台帳を追加**

「### 主要な文化イノベーション」テーブルに追加:

```markdown
| Ledger | 台帳 | 部族 |
```

「Motte（防塁）」の直後に挿入。

- [ ] **Step 5: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides
git add ck3/localization-reference.md
git commit -m "$(cat <<'EOF'
更新: CK3ローカライズ対照表 — 叙勲・徴税・教育特性追加

叙勲（Accolade）、徴税スロット（Tax Slot）、教育特性Lv5名、
台帳（Ledger）イノベーション、追加政体を追記。

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 3: CK3 汎用システムガイド — セクション 1〜4（メタ・変更サマリー・正統性・直轄領上限）

**Files:**
- Create: `ck3/ck3-systems-guide.md`

**スクリプト参照先:**
- `common/legitimacy/00_legitimacy.txt` — 正統性レベル定義・閾値・効果
- `common/defines/00_defines.txt:NDomain` — STEWARDSHIP_SKILL_FOR_DOMAIN_LIMIT_INCREASE
- `common/traits/00_traits.txt` — 教育特性の domain_limit 値
- `common/modifiers/00_basic_modifiers.txt` — 称号ティア別 domain_limit

**注意:**
- 数値は必ず `[src: ファイル名:識別子]` マーカー付き
- 1.20で変わりそうな箇所に `<!-- 1.20更新候補 -->` マーカー
- DLC固有機能は「（DLC: ○○ 必要）」注記

- [ ] **Step 1: ファイル作成 — セクション 1〜2**

`ck3/ck3-systems-guide.md` を新規作成。以下の内容:

```markdown
# CK3 汎用システムガイド（Patch 1.19.0.1 時点）

> CK3 の主要システムを横断的に解説するリファレンス。
> 2026-04-09 確認時点の最新パッチ 1.19.0.1 (Scribe) に合わせて作成。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。
> **DLC前提**: 基本ゲームのシステムを中心に解説。DLC固有機能は注記で明示する。

---

## 1.19 主要変更サマリー

| 変更 | 内容 | 影響度 |
|------|------|--------|
| 正統性（Legitimacy）新設 | 統治者の支配権の正当性を数値化。6段階のレベル制 | 大 |
| 直轄領上限の計算式変更 | 管理（Stewardship）スキル依存 → 教育特性レベル依存 | 大 |
| 叙勲（Accolade）刷新 | 種別選択、ランクシステム、Glory蓄積の再設計 | 中 |
| 封臣スタンス（Vassal Stance）導入 | 封臣の態度を7種に分類。正統性への期待値と連動 | 中 |
| 戴冠式（Coronation）と誓約（Oath） | 正統性を大幅獲得する活動。誓約で統治方針を宣言 | 中 |
| 遊牧連合（Confederation）新設 | 遊牧政体の新しい政治単位（DLC: Roads to Power 必要） | 小 |
| 徴税スロット（Tax Slot）新設 | 氏族政体の徴税管理の再設計 | 小 |
| 台帳（Ledger）イノベーション追加 | 部族時代の文化イノベーション | 小 |

---
```

- [ ] **Step 2: セクション 3 — 正統性（Legitimacy）**

ファイル末尾に追加。スクリプト `common/legitimacy/00_legitimacy.txt` から抽出した数値を使用:

```markdown
## 正統性（Legitimacy）

1.19 で新設されたシステム。統治者（Ruler）が支配権を持つに相応しいかどうかを数値で表す。統治者になった瞬間に初期正統性（Initial Legitimacy）が計算され、前統治者の正統性の一部も後継者に引き継がれる。[src: game_concepts_l_japanese.yml, game_concept_legitimacy]

### 正統性レベル

<!-- 1.20更新候補: 正統性のレベル閾値・効果が調整される可能性 -->

正統性には6段階のレベルがある。レベルの閾値は称号ティアと文化時代で変動する（部族時代の伯爵は中世後期の皇帝の4倍少ない値で到達可能）。[src: 00_legitimacy.txt, count_legitimacy]

| レベル | 効果 |
|--------|------|
| 非正統（Lv1未満） | 短期治世ペナルティ +25%、王朝威信 -0.1/月、伯爵領好感度 -10。婚姻受諾低下、請求権CBコスト増、同盟受諾低下、臣従受諾低下、朝貢受諾低下、派閥活発化 [src: 00_legitimacy.txt, legitimacy_level_1] |
| 低（Lv2） | 短期治世ペナルティ -10% [src: 00_legitimacy.txt, legitimacy_level_2] |
| 中（Lv3） | 短期治世ペナルティ -25%。請求権CBコスト減、婚姻受諾上昇 [src: 00_legitimacy.txt, legitimacy_level_3] |
| 高（Lv4） | 短期治世ペナルティ -50%、伯爵領好感度 +10。婚姻受諾上昇、同盟受諾上昇、請求権CBコスト大幅減、派閥沈静化、権力の秤コスト減 [src: 00_legitimacy.txt, legitimacy_level_4] |
| 最高（Lv5） | 上記に加え、さらなるボーナス（スクリプトの legitimacy_level_5 で定義） |

> **注意**: 閾値の具体的な数値はスクリプト変数（`legitimacy_level_1`〜`legitimacy_level_5`）で定義され、称号ティア × 文化時代で変動するため固定値ではない。

### 正統性の獲得手段

- 戦争（War）に勝利する
- 貴重な囚人（Valuable Prisoner）を解放する
- 伝説（Legend）を誕生させる（DLC: Legends of the Dead 必要）
- 宮廷（Court）を開く（DLC: Royal Court 必要）
- 活動（Activity）に参加する
- 戴冠式（Coronation）を開催する — 最も効率的
- 誓約（Oath）を達成する

[src: game_concepts_l_japanese.yml, game_concept_legitimacy_level_desc]

### 正統性の喪失

- 首都が疫病（Epidemic）に見舞われる
- 戦争に敗北する（特に派閥戦争）
- 称号（Title）を喪失する
- 敵対工作（Hostile Scheme）が発覚する

[src: game_concepts_l_japanese.yml, game_concept_legitimacy_level_desc]

### 戴冠式と誓約

戴冠式（Coronation）は正統性を大幅に獲得できる活動。戴冠式中に誓約（Oath）を宣言し、統治の方針を定める。誓約を達成すると追加の正統性・威信点等を獲得できる。[src: coronation_activity_l_japanese.yml]

主な誓約の種類:

| 系統 | 誓約 | 達成条件の概要 |
|------|------|-------------|
| 外交 | 同盟を確立する | 好感度50以上の同格以上の統治者と同盟3個以上（20年以内） |
| 外交 | 一族の力を強める | 嫡子7人以上（30年以内） |
| 軍事 | 領国を統一する | 主要称号のde jure領を完全支配（20年以内） |
| 軍事 | 領国を拡大する | 領国規模を指定値以上に（20年以内） |
| 管理 | 平和を確立する | 5年以上の平和維持（50年以内） |
| 管理 | 領国を形作る | 建造物8棟以上を建設/アップグレード（20年以内） |
| 学識 | 啓蒙を促進する | 大学建設 or 評議員全員能力20以上（50年以内） |
| — | 僭称者を追放する | 自分の子供以外の請求者を排除（50年以内） |

[src: coronation_activity_l_japanese.yml, oath tooltips]

### 政体別の正統性

- **遊牧政体（Nomadic）**: 称号ランクに関係なく特別な正統性タイプを使用（DLC: Roads to Power 必要） [src: game_concepts_l_japanese.yml, game_concept_legitimacy_desc_nomadic]
- **マンダラ政体（Mandala）**: 追加のレベルが存在する特別な正統性タイプ（DLC: Roads to Power 必要） [src: game_concepts_l_japanese.yml, game_concept_legitimacy_desc_mandala]

---
```

- [ ] **Step 3: セクション 4 — 直轄領上限（Domain Limit）**

ファイル末尾に追加:

```markdown
## 直轄領上限（Domain Limit）

<!-- 1.20更新候補: 教育特性の domain_limit 値が調整される可能性 -->

1.19 で計算式が大幅に変更された。管理（Stewardship）スキルによるボーナスが事実上無効化され、教育特性のレベルが直轄領上限の主要因となった。

### 旧仕様（1.18以前）との比較

| 項目 | 旧（1.18） | 新（1.19） |
|------|-----------|-----------|
| 管理スキルの影響 | 6ごとに +1 | 200ごとに +1（事実上無効） |
| 教育特性の影響 | なし | Lv1: -1 / Lv2: 0 / Lv3: +1 / Lv4: +2 / Lv5: +3 |

[src: 00_defines.txt, STEWARDSHIP_SKILL_FOR_DOMAIN_LIMIT_INCREASE = 200]

### 計算式

```
直轄領上限 = 称号ティアベース + 教育特性ボーナス + その他補正
```

#### 称号ティアベース

| 称号ティア | domain_limit |
|-----------|-------------|
| 伯爵（Count） | 2 [src: 00_basic_modifiers.txt, count_modifier] |
| 公爵（Duke） | 2 [src: 00_basic_modifiers.txt, duke_modifier] |
| 王（King） | 3 [src: 00_basic_modifiers.txt, king_modifier] |
| 皇帝（Emperor） | 4 [src: 00_basic_modifiers.txt, emperor_modifier] |

#### 教育特性による補正

全5系統（策略・外交・管理・軍事・学識）共通のパターン: [src: 00_traits.txt]

| レベル | domain_limit | 例（策略系） | 例（管理系） |
|--------|-------------|-------------|-------------|
| Lv1 | -1 | 稚拙な陰謀家 | （要ローカライズ確認） |
| Lv2 | 0 | 悪目立ちする山師 | （要ローカライズ確認） |
| Lv3 | +1 | 緻密な策略家 | （要ローカライズ確認） |
| Lv4 | +2 | 稀代の黒幕 | （要ローカライズ確認） |
| Lv5 | +3 | 神算鬼謀の人形師 | 黄金の君主 |

> **実用上の意味**: 王（base 3）+ 教育Lv5（+3）= 直轄領6。旧仕様では管理18で同等の+3だったが、1.19では教育結果で固定される。後継者の教育が以前より格段に重要。

#### その他の補正源

- 法律（Crown Authority 等）
- 建造物（特定の建物）
- 特性やイベント付与の modifier
- 文化イノベーション

---
```

- [ ] **Step 4: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides
git add ck3/ck3-systems-guide.md
git commit -m "$(cat <<'EOF'
追加: CK3汎用システムガイド — 正統性・直轄領上限セクション

1.19 Scribeの正統性（Legitimacy）システム全体像と
直轄領上限（Domain Limit）の教育特性依存化を解説。

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 4: CK3 汎用システムガイド — セクション 5〜8（叙勲・封臣スタンス・相続・教育）

**Files:**
- Modify: `ck3/ck3-systems-guide.md`

**スクリプト参照先:**
- `common/accolade_types/` — 叙勲種別定義
- `localization/japanese/vassal_stances_l_japanese.yml` — 封臣スタンス詳細
- `common/laws/00_succession_laws.txt` — 相続法
- `common/traits/00_traits.txt` — 教育特性全レベル

- [ ] **Step 1: セクション 5 — 叙勲（Accolade）**

ファイル末尾に追加:

```markdown
## 叙勲（Accolade）

<!-- 1.20更新候補: 叙勲の種別・効果が調整される可能性 -->

叙勲は騎士（Knight）に栄誉を与えるシステム。1.19 で種別選択・ランクシステム・Glory蓄積が刷新された。[src: accolades_l_japanese.yml]

### 基本メカニクス

1. **騎士を選択** — 叙勲された騎士（Acclaimed Knight）を1人指定
2. **種別を選択** — 騎士のスキル・特性で利用可能な種別が決まる
3. **Glory蓄積** — 騎士の活躍でGlory（栄光）が溜まる
4. **ランク上昇** — Gloryが閾値に達するとランクが上がり、効果が強化
5. **種別追加** — ランク上昇でポイントを獲得し、新たな種別を追加選択可能

### 叙勲の種別カテゴリ

叙勲の種別はカテゴリとティアで分類される: [src: 00_accolade_categories.txt]

**ティア**: common（一般）、skilled（熟練）、exceptional（卓越）、eminent（著名）

**セット**: personality（性格）、skill（スキル）、culture（文化）、men_at_arms（常備軍）

> **DLC注記**: 一部の叙勲種別は Tours & Tournaments DLC（EP2）が必要。

### 叙勲の戦略的意義

- 優秀な騎士を叙勲してGloryを蓄積させると、常備軍や外交に持続的なボーナスを得られる
- 叙勲ランクが高いと封臣への影響力も増す（正統性と連動）
- 騎士が死亡・離脱しても叙勲は継承者に引き継がれる

---
```

- [ ] **Step 2: セクション 6 — 封臣スタンス（Vassal Stance）**

```markdown
## 封臣スタンス（Vassal Stance）

<!-- 1.20更新候補: 封臣スタンスの種類・効果が調整される可能性 -->

封臣のスタンスは、封臣が主君に対してどのような態度を取るかを分類するシステム。正統性への期待値（Legitimacy Expectations）と連動し、各スタンスは特定の後継者をひいきする。[src: game_concepts_l_japanese.yml, game_concept_vassal_stance]

### 7種のスタンス

| スタンス | 英語 | 好む行動 | 嫌う行動 | ひいきする後継者 |
|---------|------|---------|---------|--------------|
| 礼節 | Courtly | 宮廷の華やかさ | 粗野な振る舞い | 外交的な後継者 |
| 地方主義 | Parochial | 地域の自治 | 中央集権 | 地方出身の後継者 |
| 名誉追求者 | Glory Hound | 戦争の勝利 | 戦争の敗北 | 軍事的な後継者 |
| 狂信 | Zealot | 宗教的純粋さ | 異教徒への寛容 | 信心深い後継者 |
| 少数派 | Minority | 文化的少数派の権利 | 文化的抑圧 | 少数派出身の後継者 |
| 弱小地主 | Barons and Minor Landholders | 低い税、自由 | 男爵領の剥奪、高い王権 | 寛大な後継者 |
| 好戦的 | Belligerent | 積極的な拡張 | 消極的な外交 | 好戦的な後継者 |

[src: vassal_stances_l_japanese.yml]

### 正統性との関係

- 各スタンスの封臣は主君に対して正統性への期待（Legitimacy Expectations）を持つ
- 継承時、特定のスタンスがひいきする後継者が即位すると、そのスタンスの封臣からの期待値が下がる（円滑な統治開始）
- 逆に、どのスタンスもひいきしない後継者が即位すると全方面から高い期待を課される

---
```

- [ ] **Step 3: セクション 7 — 相続の基本**

```markdown
## 相続の基本

相続法の一覧は [ローカライズ対照表](localization-reference.md) を参照。ここでは 1.19 での変更に焦点を当てる。

### 1.19 での相続関連変更

1. **正統性の継承**: 前統治者の正統性の一部が後継者に引き継がれる。高い正統性を持つ統治者の後継者は有利なスタートを切れる [src: game_concepts_l_japanese.yml, game_concept_legitimacy]

2. **教育依存 Domain Limit の影響**: 直轄領上限が教育特性で決まるため、教育Lv1の後継者が即位すると直轄領上限が -1（称号ベースから1減）。管理スキルでは挽回できない。後継者の教育は相続戦略の最重要要素に

3. **封臣スタンスとの連動**: 後継者が封臣のスタンスにひいきされているかどうかが、継承直後の正統性に影響

### 相続対策チェックリスト（1.19版）（コミュニティ知見）

- [ ] 後継者の教育を Lv3 以上（できれば Lv4-5）に育てる → 直轄領に直結
- [ ] 戴冠式で正統性を高めておく → 後継者への引き継ぎ量が増える
- [ ] 主要な封臣スタンスがひいきする後継者を把握する → 継承直後の期待値低下
- [ ] 継承法の確認（長子相続制への移行を検討）
- [ ] 後継者に称号を事前付与して直轄領超過を防ぐ

---
```

- [ ] **Step 4: セクション 8 — 教育と後継者育成**

```markdown
## 教育と後継者育成

<!-- 1.20更新候補: 教育特性の効果値が調整される可能性 -->

1.19 で教育特性が直轄領上限に直結するようになったため、後継者の教育は以前よりも遥かに重要。

### 教育特性 全レベル効果表

全5系統（策略・外交・管理・軍事・学識）で domain_limit パターンは共通: [src: 00_traits.txt]

| Lv | domain_limit | スキル | XP倍率 | 策略系の名前 | 外交系の名前 | 管理系の名前 | 軍事系の名前 | 学識系の名前 |
|----|-------------|--------|--------|------------|------------|------------|------------|------------|
| 1 | -1 | +2 | +10% | 稚拙な陰謀家 | 気弱な仲介者 | （要確認） | （要確認） | （要確認） |
| 2 | 0 | +4 | +20% | 悪目立ちする山師 | 平凡な交渉人 | （要確認） | （要確認） | （要確認） |
| 3 | +1 | +6 | +30% | 緻密な策略家 | 魅力的な交渉人 | （要確認） | （要確認） | （要確認） |
| 4 | +2 | +8 | +40% | 稀代の黒幕 | 影の実力者 | （要確認） | （要確認） | （要確認） |
| 5 | +3 | +10 | +50% | 神算鬼謀の人形師 | 超絶技巧の調停者 | 黄金の君主 | 無双の軍神 | 博覧強記の託宣者 |

> **Lv5 特殊効果**: 策略Lv5は敵対工作成功率 +10%・エージェント受諾 +25。各Lv5は主系統に加えて副系統のスキル +3・副系統XP +25% を持つ。[src: 00_traits.txt, education_intrigue_5]

### 教育結果を高めるコツ（コミュニティ知見）

- **Guardian（後見人）の選択**: 対応するスキルが高いキャラクターを後見人に指定する
- **学識ライフスタイルの Scholar パーク**: 後見人のスキルに追加ボーナス
- **天才（Genius）・利発（Quick）特性**: 教育の最終結果にボーナス
- **目標レベル**: Lv3（domain_limit +1）が最低ライン、Lv4-5 を目指す

### 教育系統の選択指針（コミュニティ知見）

| 状況 | 推奨系統 | 理由 |
|------|---------|------|
| 序盤・戦争が多い | 軍事 | 戦争遂行能力 + domain_limit |
| 内政安定期 | 管理 | 収入増 + domain_limit（1.19では管理スキル自体のdomain効果はないが、収入系パークは健在） |
| 外交拡張期 | 外交 | 同盟・婚姻 + domain_limit |
| 諜報重視 | 策略 | 暗殺・工作 + domain_limit |
| 文化発展 | 学識 | イノベーション加速 + domain_limit |

---
```

- [ ] **Step 5: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides
git add ck3/ck3-systems-guide.md
git commit -m "$(cat <<'EOF'
追加: CK3システムガイド — 叙勲・封臣スタンス・相続・教育セクション

叙勲刷新、封臣スタンス7種、相続の1.19変更点、
教育特性の全レベル効果表を追加。

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 5: CK3 汎用システムガイド — セクション 9〜12（その他変更・誤解・用語・出典）+ index.html

**Files:**
- Modify: `ck3/ck3-systems-guide.md`
- Modify: `index.html`

- [ ] **Step 1: セクション 9〜10**

ファイル末尾に追加:

```markdown
## その他 1.19 変更点

### 遊牧連合（Confederation）

遊牧政体の新しい政治単位。遊牧連合に加入・脱退するとメンバー全員に通知される。加入直後の3年間は「新規連合員」フラグが付き、5年間は連合メンバー補正が適用される。[src: 00_confederation_types.txt, nomadic_confederation]

（DLC: Roads to Power 必要）

### 徴税スロット（Tax Slot）

氏族政体の徴税管理を再設計したシステム。1スロットあたり封臣12名を管理できる。徴税官（Tax Collector）を任命し、異なる税制（義務）を適用する。[src: 00_tax_slot_types.txt, clan_tax_slot]

- 徴税官の条件: 成人、投獄されていない、無能力でない
- 性別制限: 宗派の教義（男性優位等）に従う
- 宰相（Vizier）を任命すると追加の徴税管轄を獲得（DLC: Roads to Power 必要）

### 台帳（Ledger）イノベーション

部族時代の文化イノベーション。所有物の記録管理を可能にする。[src: cultural_innovations_l_japanese.yml, innovation_ledger]

---

## よくある誤解（1.19版）

| 誤解 | 実際 |
|------|------|
| 「管理（Stewardship）を上げれば直轄領が増える」 | 1.19 では管理スキル200ごとに +1（事実上無効）。教育特性レベルで決まる [src: 00_defines.txt, STEWARDSHIP_SKILL_FOR_DOMAIN_LIMIT_INCREASE = 200] |
| 「教育の系統は好みで選んでいい」 | 1.19 では全系統が同じ domain_limit パターン（Lv1: -1, Lv5: +3）のため、系統自体よりレベルが重要 [src: 00_traits.txt] |
| 「正統性は威信点（Prestige）と同じようなもの」 | 正統性は独立したリソース。威信点とは別に管理が必要。低い正統性は婚姻・同盟・臣従の受諾率を直接下げる [src: 00_legitimacy.txt] |
| 「戴冠式は1回やれば十分」 | 新しい統治者になるたびに戴冠式が必要。代替わりごとの必須イベント |
| 「叙勲は騎士が強いときだけ意味がある」 | 叙勲ランクは封臣管理やスキルボーナスにも影響。軍事以外の価値も大きい |

---
```

- [ ] **Step 2: セクション 11〜12（用語対照表・出典）**

```markdown
## 用語対照表

> 完全版は [localization-reference.md](localization-reference.md) を参照。以下はこのガイドで使う用語の抜粋。

| 日本語 | 英語 | 補足 |
|--------|------|------|
| 正統性 | Legitimacy | 統治者の支配権の正当性 |
| 正統性レベル | Legitimacy Level | 6段階 |
| 正統性への期待 | Legitimacy Expectations | 封臣が主君に要求する水準 |
| 戴冠式 | Coronation | 正統性を獲得する活動 |
| 誓約 | Oath | 戴冠式での方針宣言 |
| 直轄領上限 | Domain Limit | 保持できる直轄領の数 |
| 叙勲 | Accolade | 騎士への栄誉 |
| 栄光 | Glory | 叙勲の成長リソース |
| 封臣のスタンス | Vassal Stance | 封臣の態度分類 |
| 礼節 | Courtly | 封臣スタンスの一種 |
| 地方主義 | Parochial | 封臣スタンスの一種 |
| 名誉追求者 | Glory Hound | 封臣スタンスの一種 |
| 狂信 | Zealot | 封臣スタンスの一種 |
| 少数派 | Minority | 封臣スタンスの一種 |
| 弱小地主 | Barons and Minor Landholders | 封臣スタンスの一種 |
| 好戦的 | Belligerent | 封臣スタンスの一種 |
| 権力の秤 | Scales of Power | 統治者と摂政の権力バランス |
| 徴税スロット | Tax Slot | 氏族政体の徴税管理 |
| 徴税官 | Tax Collector | 徴税スロットの管理者 |
| 遊牧連合 | Confederation | 遊牧政体の政治単位 |
| 台帳 | Ledger | 文化イノベーション |
| 教育 | Education | 子供時代の育成結果 |

---

## 出典

### 一次情報（ゲームスクリプト・公式）

- ローカルのゲームスクリプトと日本語ローカライズを照合
  - `common/legitimacy/00_legitimacy.txt` — 正統性レベル定義・閾値・効果
  - `common/defines/00_defines.txt:NDomain` — STEWARDSHIP_SKILL_FOR_DOMAIN_LIMIT_INCREASE = 200
  - `common/traits/00_traits.txt` — 教育特性の domain_limit 値（全5系統×5レベル）
  - `common/modifiers/00_basic_modifiers.txt` — 称号ティア別 domain_limit ボーナス
  - `common/accolade_types/00_accolade_categories.txt` — 叙勲種別カテゴリ定義
  - `common/confederation_types/00_confederation_types.txt` — 遊牧連合定義
  - `common/tax_slots/types/00_tax_slot_types.txt` — 徴税スロット定義
  - `localization/japanese/game_concepts_l_japanese.yml` — 正統性、封臣スタンス、権力の秤
  - `localization/japanese/vassal_stances_l_japanese.yml` — 封臣スタンス名
  - `localization/japanese/traits_l_japanese.yml` — 教育特性名
  - `localization/japanese/accolades/accolades_l_japanese.yml` — 叙勲用語
  - `localization/japanese/activities/coronation_activity_l_japanese.yml` — 戴冠式・誓約
  - `localization/japanese/culture/cultural_innovations_l_japanese.yml` — 台帳イノベーション
- [Patch 1.19 Scribe - CK3 Wiki](https://ck3.paradoxwikis.com/Patches)

### コミュニティ情報（補足知見）

プレイ報告・体感ベースの情報。条件の裏取りには一次情報を参照のこと。

- 教育系統の選択指針は経験則ベース
- 相続対策チェックリストはコミュニティで広く共有される知見
- 叙勲の戦略的意義はプレイ報告ベース
```

- [ ] **Step 3: index.html にカード追加**

`index.html` の CK3 セクション（L294-315 付近）、既存カード2枚の直前（`<li>` 群の先頭）に挿入:

```html
        <li>
          <a class="card" href="viewer.html?file=ck3/ck3-systems-guide.md" target="_blank" rel="noopener">
            <div class="card__info">
              <div class="card__title">汎用システムガイド</div>
              <div class="card__meta">1.19 Scribe — 正統性・直轄領・叙勲</div>
            </div>
            <span class="card__tag tag--guide">攻略</span>
            <svg class="card__arrow" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </li>
```

- [ ] **Step 4: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides
git add ck3/ck3-systems-guide.md index.html
git commit -m "$(cat <<'EOF'
完成: CK3汎用システムガイド + index.htmlカード追加

その他1.19変更点、よくある誤解、用語対照表、出典を追加。
index.htmlにCK3汎用システムガイドのカードを追加。

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## Task 6: QAレビュー — 表記揺れ・リンク・マーカー確認

**Files:**
- Read: `ck3/ck3-systems-guide.md`
- Read: `ck3/localization-reference.md`
- Read: `index.html`

- [ ] **Step 1: 表記揺れチェック**

```bash
cd /c/Users/ramda/projects/paradox-game-guides
# localization-reference.md の用語と systems-guide の用語が一致しているか
grep -oP '(?<=\| )[^\|]+(?= \|)' ck3/localization-reference.md | sort -u > /tmp/loc_terms.txt
grep -oP '(?<=\| )[^\|]+(?= \|)' ck3/ck3-systems-guide.md | sort -u > /tmp/guide_terms.txt
# 目視確認: ガイド内の日本語用語がすべてlocalization-referenceに存在するか
```

- [ ] **Step 2: リンク確認**

```bash
# ガイド内の内部リンクが正しいか
grep -n '\[.*\](.*\.md)' ck3/ck3-systems-guide.md
# index.html のリンクが正しいか
grep -n 'ck3-systems-guide' index.html
```

- [ ] **Step 3: パッチ追従マーカー確認**

```bash
grep -c '1.20更新候補' ck3/ck3-systems-guide.md
# 期待: 4件以上（正統性レベル、教育特性domain_limit、叙勲、封臣スタンス）
```

- [ ] **Step 4: 教育特性テーブルの「（要確認）」を埋める**

ローカライズファイルから残りの教育特性名を確認して置換:

```bash
grep -n "education_stewardship_\|education_martial_\|education_learning_" \
  "C:/Program Files (x86)/Steam/steamapps/common/Crusader Kings III/game/localization/japanese/traits_l_japanese.yml" | head -15
```

確認後、`ck3-systems-guide.md` の教育特性テーブル内の「（要確認）」をすべて正式名称に置換する。

- [ ] **Step 5: コミット（修正があれば）**

```bash
cd /c/Users/ramda/projects/paradox-game-guides
git add ck3/ck3-systems-guide.md ck3/localization-reference.md
git commit -m "$(cat <<'EOF'
修正: CK3ガイドQA — 表記揺れ修正・教育特性名補完

QAレビューで発見した表記揺れを修正。
教育特性テーブルの「（要確認）」をローカライズ正式名称に置換。

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

## 実装メモ

### エージェント委任時の注意

- ローカライズ対照表のカテゴリは3つ以下に分割（CLAUDE.md準拠）
- スクリプト参照時はファイル名:識別子でマーカーを付ける
- 「（要確認）」はQAタスクで必ず埋める — 残さない
- `sed` 全置換前に `grep -c` で件数確認（CLAUDE.md学び）
- 共通CSS/JSの変更はなし（index.htmlのHTML追加のみ）
