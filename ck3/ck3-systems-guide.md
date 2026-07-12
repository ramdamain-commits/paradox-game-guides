# CK3 汎用システムガイド（Patch 1.19.0.6 時点）

> CK3 の主要システムを横断的に解説するリファレンス。
> 2026-07-12 確認時点。インストール版 **1.19.0.6（Scribe）** に合わせて作成。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。
> **DLC前提**: 基本ゲームのシステムを中心に解説。DLC固有機能は注記で明示する。

---

## 1.19 主要変更サマリー

| 変更 | 内容 | 影響度 |
|------|------|--------|
| 正統性（Legitimacy） | Patch 1.12（Scythe）で導入済みの既存システム。1.19での変更なし | — |
| 直轄領上限の計算式変更 | 管理（Stewardship）スキル依存 → 教育特性レベル依存 | 大 |
| 叙勲（Accolade）刷新 | primary/secondary attribute構造を撤廃し、個別named attribute・ランク1-3・Glory閾値6段階へ再設計 | 中 |
| 封臣スタンス（Vassal Stance） | Patch 1.9（Tours & Tournaments）で導入済みの既存システム。1.19での変更なし | — |
| 戴冠式（Coronation）と誓約（Oath） | Patch 1.17（Coronations）で導入済み。1.19では戴冠式終了フェーズ短縮・一部誓約要件緩和のみ | 小 |
| 遊牧連合（Confederation） | Patch 1.16（Chamfron）で無料機能として導入済み。1.19でコサック王国建国ディシジョン等が追加 | 小 |
| 課税区域（Tax Jurisdiction） | Patch 1.11（Peacock）で導入済みの既存システム。1.19での変更なし | — |
| 台帳（Ledger）ウィンドウ新設 | 戦争/アーティファクト/キャラクター/家門・王朝/所領/伯爵領/称号/信仰/文化の9ページからなる統計閲覧UI（文化イノベーションの「台帳」とは別物） | 小 |

---

## 正統性（Legitimacy）

Patch 1.12（Scythe、2024-03-04）で導入されたシステム。統治者（Ruler）が支配権を持つに相応しいかどうかを数値で表す。1.19 では仕様変更なし。（コミュニティ知見：wiki由来、スクリプト未確認）統治者になった瞬間に初期正統性（Initial Legitimacy）が計算され、前統治者の正統性の一部も後継者に引き継がれる。[src: game_concepts_l_japanese.yml, game_concept_legitimacy]

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
| Lv1 | -1 | 稚拙な陰謀家 | 気弱な仲介者 | 世間知らずの浪費家 | 将才なき戦士 | 愚直な書記官 |
| Lv2 | 0 | 悪目立ちする山師 | 平凡な交渉人 | ケチな出納係 | 不屈の軍人 | 洞察力のある思想家 |
| Lv3 | +1 | 緻密な策略家 | 魅力的な交渉人 | 金儲けの達人 | 熟練の戦術家 | 鋭敏な知識人 |
| Lv4 | +2 | 稀代の黒幕 | 影の実力者 | 経済の錬金術師 | 不世出の戦略家 | 並ぶ者なき哲学者 |
| Lv5 | +3 | 神算鬼謀の人形師 | 超絶技巧の調停者 | 黄金の君主 | 無双の軍神 | 博覧強記の託宣者 |

> **実用上の意味**: 王（base 3）+ 教育Lv5（+3）= 直轄領6。旧仕様では管理18で同等の+3だったが、1.19では教育結果で固定される。後継者の教育が以前より格段に重要。

#### その他の補正源

- 法律（Crown Authority 等）
- 建造物（特定の建物）
- 特性やイベント付与の modifier
- 文化イノベーション

---

## 叙勲（Accolade）

<!-- 1.20更新候補: 叙勲の種別・効果が調整される可能性 -->

叙勲は騎士（Knight）に栄誉を与えるシステム。元々は Patch 1.9（Tours & Tournaments、2023-05-11）で導入されたが、1.19 でメカニクスが大規模に再設計された。旧仕様（ティア×セットによる種別選択）は廃止され、個別の named attribute とランク制へ刷新されている。[src: accolades_l_japanese.yml]

### 基本メカニクス（1.19版）

1. **対象条件の確認** — 叙勲を与えられるのは**公爵（Duke）ランク以上の統治者**のみ。対象となる騎士は**武勇（Prowess）8以上**かつ**主君への好感度+15以上**が必要（コミュニティ知見：wiki由来、スクリプト未確認）
2. **騎士を叙勲** — 条件を満たす騎士（Acclaimed Knight）を1人指定
3. **Glory蓄積** — 騎士の活躍でGlory（栄光）が溜まる
4. **ランク上昇** — Gloryが6段階の閾値（100 / 300 / 600 / 1000 / 1500 / 2100）に達するたびにランクが上がる（ランクは1〜3）（コミュニティ知見：wiki由来、スクリプト未確認）
5. **属性ポイントの獲得** — ランクアップのたびに属性ポイントを1個獲得。既存の属性を強化するか、新規属性を追加するかを選べる（属性は最大3つまで保有可能）（コミュニティ知見：wiki由来、スクリプト未確認）

### 叙勲属性（Accolade Attributes）

1.19 以降は「ティア（common/skilled/exceptional/eminent）」「セット（personality/skill/culture/men_at_arms）」による分類は廃止され、Blademaster・Besieger・Charmer・Mentor 等の**個別の named attribute**を直接選択する方式に変わっている。各属性はランク（強化段階）ごとに効果が段階的に強くなる。（コミュニティ知見：wiki由来、スクリプト未確認）

> `[src: 00_accolade_categories.txt]`（未検証） — 旧仕様（ティア×セット構造）時点での出典。1.19でファイル自体が再構成された可能性があり、現行データと一致するか未確認。

> **DLC注記**: 叙勲システム自体は Tours & Tournaments DLC（EP2）が必要。

### 叙勲の戦略的意義

- 優秀な騎士を叙勲してGloryを蓄積させると、常備軍や外交に持続的なボーナスを得られる
- 叙勲ランクが高いと封臣への影響力も増す（正統性と連動）
- 騎士が死亡・離脱しても叙勲は継承者に引き継がれる

---

## 封臣スタンス（Vassal Stance）

<!-- 1.20更新候補: 封臣スタンスの種類・効果が調整される可能性 -->

Patch 1.9（Tours & Tournaments、2023-05-11）で導入された既存システム。1.19での変更なし。封臣のスタンスは、封臣が主君に対してどのような態度を取るかを分類するシステム。正統性への期待値（Legitimacy Expectations）と連動し、各スタンスは特定の後継者をひいきする。[src: game_concepts_l_japanese.yml, game_concept_vassal_stance]

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

## 相続の基本

相続法の一覧は [ローカライズ対照表](localization-reference.md) を参照。ここでは 1.19 での変更に焦点を当てる。

### 1.19 での相続関連変更

1. **正統性の継承**: 前統治者の正統性の一部が後継者に引き継がれる。高い正統性を持つ統治者の後継者は有利なスタートを切れる [src: game_concepts_l_japanese.yml, game_concept_legitimacy]

2. **教育依存 Domain Limit の影響**: 直轄領上限が教育特性で決まるため、教育Lv1の後継者が即位すると直轄領上限が -1（称号ベースから1減）。管理スキルでは挽回できない。後継者の教育は相続戦略の最重要要素に

3. **封臣スタンスとの連動**: 後継者が封臣のスタンスにひいきされているかどうかが、継承直後の正統性に影響

### 相続対策チェックリスト（1.19版）（コミュニティ知見）

- 後継者の教育を Lv3 以上（できれば Lv4-5）に育てる → 直轄領に直結
- 戴冠式で正統性を高めておく → 後継者への引き継ぎ量が増える
- 主要な封臣スタンスがひいきする後継者を把握する → 継承直後の期待値低下
- 継承法の確認（長子相続制への移行を検討）
- 後継者に称号を事前付与して直轄領超過を防ぐ

---

## 教育と後継者育成

<!-- 1.20更新候補: 教育特性の効果値が調整される可能性 -->

1.19 で教育特性が直轄領上限に直結するようになったため、後継者の教育は以前よりも遥かに重要。

### 教育特性 全レベル効果表

全5系統（策略・外交・管理・軍事・学識）で domain_limit パターンは共通: [src: 00_traits.txt]

| Lv | domain_limit | スキル | XP倍率 | 策略系 | 外交系 | 管理系 | 軍事系 | 学識系 |
|----|-------------|--------|--------|--------|--------|--------|--------|--------|
| 1 | -1 | +2 | +10% | 稚拙な陰謀家 | 気弱な仲介者 | 世間知らずの浪費家 | 将才なき戦士 | 愚直な書記官 |
| 2 | 0 | +4 | +20% | 悪目立ちする山師 | 平凡な交渉人 | ケチな出納係 | 不屈の軍人 | 洞察力のある思想家 |
| 3 | +1 | +6 | +30% | 緻密な策略家 | 魅力的な交渉人 | 金儲けの達人 | 熟練の戦術家 | 鋭敏な知識人 |
| 4 | +2 | +8 | +40% | 稀代の黒幕 | 影の実力者 | 経済の錬金術師 | 不世出の戦略家 | 並ぶ者なき哲学者 |
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

## その他 1.19 変更点

### 遊牧連合（Confederation）

Patch 1.16（Chamfron、2025-04-28）で無料機能として導入、1.19でコサック王国建国ディシジョン等が追加された。遊牧政体の政治単位。遊牧連合に加入・脱退するとメンバー全員に通知される。加入直後の3年間は「新規連合員」フラグが付き、5年間は連合メンバー補正が適用される。[src: 00_confederation_types.txt, nomadic_confederation]

### 課税区域（Tax Jurisdiction）

Patch 1.11（Peacock、2023-11-09）で導入された既存システム。1.19での変更なし。氏族政体の徴税管理システム。1区域あたり封臣12名を管理できる。徴税官（Tax Collector）を任命し、異なる税制（義務）を適用する。[src: 00_tax_slot_types.txt, clan_tax_slot]

> **正式名称について**: 日本語ローカライズを確認したところ、正式名称は「課税区域」（`game_concepts_l_japanese.yml: game_concept_tax_jurisdiction`, `government_l_japanese.yml: clan_tax_slot = "課税区域"`）。「徴税スロット」「徴税管轄」はいずれも旧称・非公式表記のため本ガイドでは「課税区域」に統一する。[src: government_l_japanese.yml, clan_tax_slot]

- 徴税官の条件: 成人、投獄されていない、無能力でない
- 性別制限: 宗派の教義（男性優位等）に従う
- 宰相（Vizier）を任命すると追加の課税区域を獲得（DLC: Roads to Power 必要）

### 台帳（Ledger）ウィンドウ

1.19 で新設されたUI機能。**戦争・アーティファクト・キャラクター・家門/王朝・所領・伯爵領・称号・信仰・文化の9ページ**からなる統計閲覧画面で、王国全体の情報をまとめて確認できる。（コミュニティ知見：wiki由来、スクリプト未確認）

> **文化イノベーション「台帳」との混同に注意**: 部族時代の文化イノベーションにも同名の「台帳（Ledger）」が存在するが、これは上記の1.19新設UIとは全くの別物。効果は建造物スロット+1・畜群からの月間収入+5%。[src: cultural_innovations_l_japanese.yml, innovation_ledger]

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
| 課税区域 | Tax Jurisdiction | 氏族政体の徴税管理単位（旧称: 徴税スロット/徴税管轄） |
| 徴税官 | Tax Collector | 課税区域の管理者 |
| 遊牧連合 | Confederation | 遊牧政体の政治単位 |
| 台帳イノベーション | Ledger（文化イノベーション） | 部族時代の文化イノベーション。1.19新設の台帳ウィンドウとは別物 |
| 台帳ウィンドウ | Ledger window | 1.19新設のUI機能（統計閲覧画面、9ページ構成） |
| 教育 | Education | 子供時代の育成結果 |

---

## 出典

### 一次情報（ゲームスクリプト・公式）

- ローカルのゲームスクリプトと日本語ローカライズを照合
  - `common/legitimacy/00_legitimacy.txt` — 正統性レベル定義・閾値・効果
  - `common/defines/00_defines.txt:NDomain` — STEWARDSHIP_SKILL_FOR_DOMAIN_LIMIT_INCREASE = 200
  - `common/traits/00_traits.txt` — 教育特性の domain_limit 値（全5系統×5レベル）
  - `common/modifiers/00_basic_modifiers.txt` — 称号ティア別 domain_limit ボーナス
  - `common/accolade_types/00_accolade_categories.txt` — 叙勲種別カテゴリ定義（未検証: 1.19で再構成された可能性あり）
  - `common/confederation_types/00_confederation_types.txt` — 遊牧連合定義
  - `common/tax_slots/types/00_tax_slot_types.txt` — 課税区域（Tax Jurisdiction）定義
  - `localization/japanese/game_concepts_l_japanese.yml` — 正統性、封臣スタンス、権力の秤、課税区域（tax_jurisdiction）
  - `localization/japanese/government_l_japanese.yml` — 課税区域（clan_tax_slot = "課税区域"）
  - `localization/japanese/vassal_stances_l_japanese.yml` — 封臣スタンス名
  - `localization/japanese/traits_l_japanese.yml` — 教育特性名
  - `localization/japanese/accolades/accolades_l_japanese.yml` — 叙勲用語
  - `localization/japanese/activities/coronation_activity_l_japanese.yml` — 戴冠式・誓約
  - `localization/japanese/culture/cultural_innovations_l_japanese.yml` — 台帳イノベーション（文化イノベーション、Ledgerウィンドウとは別物）
- [Patch 1.19 Scribe - CK3 Wiki](https://ck3.paradoxwikis.com/Patches)
- [Patch 1.9 - CK3 Wiki](https://ck3.paradoxwikis.com/Patch_1.9) — 封臣スタンス・叙勲の導入元
- [Patch 1.11 Peacock - CK3 Wiki](https://ck3.paradoxwikis.com/Patch_1.11) — 課税区域（Tax Jurisdiction）の導入元
- [Patch 1.12 Scythe - CK3 Wiki](https://ck3.paradoxwikis.com/Patch_1.12) — 正統性（Legitimacy）の導入元
- [Patch 1.16 Chamfron - CK3 Wiki](https://ck3.paradoxwikis.com/Patch_1.16) — 遊牧連合（Confederation）の導入元
- [Patch 1.17 - CK3 Wiki](https://ck3.paradoxwikis.com/Patch_1.17) — 戴冠式（Coronation）・誓約（Oath）の導入元
- [Accolade - CK3 Wiki](https://ck3.paradoxwikis.com/Accolade) — 1.19刷新後の叙勲メカニクス（現行仕様）

### コミュニティ情報（補足知見）

プレイ報告・体感ベースの情報。条件の裏取りには一次情報を参照のこと。

- 教育系統の選択指針は経験則ベース
- 相続対策チェックリストはコミュニティで広く共有される知見
- 叙勲の戦略的意義はプレイ報告ベース
- 叙勲の対象条件（公爵ランク以上・武勇8以上・好感度+15以上）、Glory閾値6段階、ランクアップごとの属性ポイント獲得はいずれも wiki 由来でスクリプト未確認
- 台帳（Ledger）ウィンドウの9ページ構成は wiki 由来でスクリプト未確認
