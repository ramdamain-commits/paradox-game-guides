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

| レベル | domain_limit | 策略系 | 外交系 | 管理系 | 軍事系 | 学識系 |
|--------|-------------|--------|--------|--------|--------|--------|
| Lv1 | -1 | 稚拙な陰謀家 | 気弱な仲介者 | （Task 6で補完） | （Task 6で補完） | （Task 6で補完） |
| Lv2 | 0 | 悪目立ちする山師 | 平凡な交渉人 | （Task 6で補完） | （Task 6で補完） | （Task 6で補完） |
| Lv3 | +1 | 緻密な策略家 | 魅力的な交渉人 | （Task 6で補完） | （Task 6で補完） | （Task 6で補完） |
| Lv4 | +2 | 稀代の黒幕 | 影の実力者 | （Task 6で補完） | （Task 6で補完） | （Task 6で補完） |
| Lv5 | +3 | 神算鬼謀の人形師 | 超絶技巧の調停者 | 黄金の君主 | 無双の軍神 | 博覧強記の託宣者 |

> **実用上の意味**: 王（base 3）+ 教育Lv5（+3）= 直轄領6。旧仕様では管理18で同等の+3だったが、1.19では教育結果で固定される。後継者の教育が以前より格段に重要。

#### その他の補正源

- 法律（Crown Authority 等）
- 建造物（特定の建物）
- 特性やイベント付与の modifier
- 文化イノベーション
