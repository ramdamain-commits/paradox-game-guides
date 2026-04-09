# EU5 宗教グループ別攻略ガイド（Patch 1.1 時点）

> 各宗教グループの固有メカニクス・修正値・法学派（School）の選択指針をまとめた参照ガイド。
> 国家固有の宗教戦略は各国家別ガイドも参照すること。
> 2026-04-08 確認。スクリプト照合対象: `in_game/common/religions/`・`religious_aspects/`・`religious_schools/`・`building_types/religion_buildings.txt`
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳箇所は英語を併記する。

> 基本メカニクスは [汎用攻略ガイド](eu5-universal-guide.md) を参照。
---

## 概要：宗教グループ一覧

| グループ | 主要宗教 | 固有パラメータ | 奴隷取引 | 備考 |
|---------|---------|------------|--------|------|
| キリスト教（christian） | カトリック・正教・プロテスタント系 | Religious Influence / Rite Power | 不可 | `[src: religion_groups/00_default.txt:1-6]` |
| イスラム教（muslim） | スンニ・シーア・イバード | Piety スライダー（神秘主義 vs 律法主義） | 可 | `[src: religion_groups/00_default.txt:13-19]` |
| 仏教（buddhist） | 大乗・上座部・神道・三教 | カルマ（Karma） / 神道のみ純粋（Purity）＋名誉（Honor） | 不可 | `[src: religion_groups/00_default.txt:8-11]` |
| ダルマ（dharmic） | ヒンドゥー・ジャイナ・シク | アヴァタール / カルマ | 不可 | `[src: religion_groups/00_default.txt:22-25]` |
| ゾロアスター教（zoroastrian_group） | ゾロアスター教 | ― | 不可 | `[src: religion_groups/00_default.txt:27-31]` |
| トナル（tonal_group） | ナワトル・マヤ・メソアメリカ | Doom / 信仰フォーカス（Religious Focus） | 可 | `[src: religion_groups/00_default.txt:123-129]` |
| ペルー民族（folk_peruvian_group） | インティ（Inti）系 | ヤナンティン（Yanantin）バランス | 可 | `[src: religion_groups/00_default.txt:179-185]` |
| アフリカ・その他民族 | アフリカ各宗教 | 信仰アスペクト | 可 | `[src: religion_groups/00_default.txt:57-64]` |

> **グループ共通**: イスラム教グループのみ国家レベルで奴隷需要（`allow_rgo_slave_demand`）を持ち、ワイン・ビール・蒸留酒の輸入が禁止される `[src: religions/muslim.txt:36-40]`

---

## キリスト教グループ

### キリスト教共通メカニクス：Religious Influence（宗教的影響力）

ほぼすべてのキリスト教宗教は `has_religious_influence = yes` を持つ。

| パラメータ | 値 | 出典 |
|-----------|---|------|
| 月間 Religious Influence 増加 | +0.1（多くの宗教の基本値） | `[src: religions/christian.txt]` |
| 最大 Religious Influence（プロテスタント系） | 400 | `[src: religions/christian.txt:各定義]` |
| 最大 Religious Influence（カトリック・正教・ボスニア教会） | 900 | `[src: religions/christian.txt:210,95]` |

---

### カトリック（Catholic）

| 項目 | 内容 | 出典 |
|------|------|------|
| 聖職者エステート最大税率ペナルティ | clergy_estate_max_tax −1.0 | `[src: religions/christian.txt:205]` |
| 月間聖職者識字率上昇 | global_clergy_max_literacy +25 | `[src: religions/christian.txt:207]` |
| 修道院建設可否 | 可（`can_have_monasteries = yes`） | `[src: religions/christian.txt:208]` |
| 帝国位への昇格制限 | 帝国昇格不可（`block_from_change_to_empire_rank_catholic`） | `[src: religions/christian.txt:210]` |
| 最大 Religious Influence | 900 | `[src: religions/christian.txt:212]` |
| 教会十分の一税（Tithe） | 2%（`tithe = 0.02`） | `[src: religions/christian.txt:203]` |
| 対異教・異端宣戦禁止 | 宗教長（教皇）への宣戦不可（`cannot_declare_no_cb_wars_on_religion_head`） | `[src: religions/christian.txt:214]` |
| 固有機能 | 教皇庁（Papacy）・枢機卿（Cardinal）・列聖（Canonization）あり | `[src: religions/christian.txt:196-201]` |

**外交傾向**
- 正教：友好（kindred）
- ユダヤ教：否定的（negative）
- スンニ・シーア・イバード：敵対（enemy）
- ボゴミル・カタリ・ワルドー・フス派：敵対（enemy）

`[src: religions/christian.txt:217-228]`

> ⚠ **1.2 更新候補**: カトリック改革（`needs_reform = yes`）周辺のメカニクスが 1.2 で調整予定

---

### 正教会（Orthodox）

| 項目 | 内容 | 出典 |
|------|------|------|
| 安定度コスト削減 | stability_cost −0.1 | `[src: religions/christian.txt:427]` |
| 最大識字率上昇 | global_max_literacy +5 | `[src: religions/christian.txt:428]` |
| 最大 Religious Influence | 400 | `[src: religions/christian.txt:429]` |
| 聖職者アイコン（Icons） | 使用可（`use_icons = yes`） | `[src: religions/christian.txt:423]` |
| 総主教座（Patriarchates） | 自立的総主教座あり（`has_autocephalous_patriarchates`） | `[src: religions/christian.txt:420]` |
| 列聖（Canonization） | あり | `[src: religions/christian.txt:419]` |

**外交傾向**
- カトリック：好意的（positive）
- ユダヤ教：好意的（positive）
- ボゴミル：敵対（enemy）
- スンニ・シーア：敵対（enemy）

`[src: religions/christian.txt:432-442]`

**建物：正教会修道院（Orthodox Monastery）**

| 修正値 | 値 |
|--------|---|
| local_clergy_max_literacy | +10 |
| local_clergy_food_consumption | +0.2 |
| local_pop_conversion_speed_modifier | +0.1 |

`[src: building_types/religion_buildings.txt:203-241]`

> ⚠ **1.2 更新候補**: 正教会は 1.2「エキナデス」で Rite Power（儀式力）を含む大幅なメカニクス追加が予定されている（`has_rite_power = yes` はミアフィジット派に現時点で実装済み。正教会への追加は開発日記で示唆）

---

### ミアフィジット派（Miaphysite）— コプト・エチオピア正教系

| 項目 | 内容 | 出典 |
|------|------|------|
| 聖職者最大税率ペナルティ | clergy_estate_max_tax −0.5 | `[src: religions/christian.txt:369]` |
| 自信仰への寛容 | tolerance_own +1 | `[src: religions/christian.txt:370]` |
| 異端への寛容 | tolerance_heretic −1 | `[src: religions/christian.txt:371]` |
| Rite Power | あり（`has_rite_power = yes`） | `[src: religions/christian.txt:365]` |
| 最大 Religious Influence | 400 | `[src: religions/christian.txt:374]` |

**建物：ミアフィジット修道院（Miaphysite Monastery）**

| 修正値 | 値 | 備考 |
|--------|---|------|
| local_clergy_max_literacy | +10 | — |
| local_pop_conversion_speed_modifier | +0.1 | — |
| monthly_rite_power（首都のみ） | +0.05 | `[src: building_types/religion_buildings.txt:280-282]` |

---

### ネストリウス派（Nestorianism）

| 項目 | 内容 | 出典 |
|------|------|------|
| 聖職者最大税率ペナルティ | clergy_estate_max_tax −0.5 | `[src: religions/christian.txt:398]` |
| 自信仰への寛容 | tolerance_own +1 | `[src: religions/christian.txt:399]` |
| 安定度コスト削減 | stability_cost −0.1 | `[src: religions/christian.txt:400]` |
| 最大 Religious Influence | 400 | `[src: religions/christian.txt:403]` |

---

### プロテスタント系共通（Church Aspects）

ルター派（Lutheran）・カルヴァン派（Calvinist）・英国国教会（Anglican）・フス派（Hussite）・ロラード派（Lollardy）・ワルドー派（Waldensian）などは `custom_tags = { church_aspects }` を持ち、Church Aspect（教会方針）を選択できる。

各宗教は Aspect スロット数が異なる（`religious_aspects = 3` が標準）。

**主要 Aspect と修正値**

| アスペクト名 | 適用宗教 | 主な修正値 | 出典 |
|------------|---------|---------|------|
| 翻訳聖書（Translated Bibles） | プロテスタント系全般 | global_max_literacy +10、社会価値→革新的 | `[src: religious_aspects/common.txt:454-478]` |
| 世俗君主が信仰の長（Crown as Head of Faith） | 英国国教会・カルヴァン・ルター他 | global_crown_estate_power +0.1、monthly_control +0.001 | `[src: religious_aspects/common.txt:147-174]` |
| 聖職者の清貧（Clerical Poverty） | プロテスタント系全般 | clergy_estate_max_tax +0.1 | `[src: religious_aspects/common.txt:117-145]` |
| 成人洗礼（Adult Baptism） | 英国国教会・カルヴァン他 | global_pop_conversion_speed_modifier +0.20 | `[src: religious_aspects/common.txt:27-45]` |
| 高利貸し容認（Usury Allowed） | 英国国教会・カルヴァン・ルター他 | bank_interest −0.01、minting_income +0.05 | `[src: religious_aspects/common.txt:480-496]` |
| 修道院制（Monasticism） | 英国国教会・カルヴァン他 | can_have_monasteries、clergy_max_literacy +5 | `[src: religious_aspects/common.txt:247-271]` |
| 信仰のみによる義（Sola Fide） | カルヴァン・フス・ルター | pop_join_rebel_threshold −0.03 | `[src: religious_aspects/common.txt:394-411]` |
| 聖書のみによる権威（Sola Scriptura） | カルヴァン・フス・ルター | global_max_literacy +5 | `[src: religious_aspects/common.txt:413-432]` |
| 神のみに栄光を（Soli Deo Gloria） | カルヴァン・フス・ルター | monthly_art_start_chance +0.1、宗教的影響 +0.1 | `[src: religious_aspects/common.txt:434-452]` |
| 戦争説教（War Sermons） | 英国国教会・カルヴァン他 | land_morale_recovery +0.02 | `[src: religious_aspects/common.txt:498-515]` |
| 布教の自由（Freedom to Preach） | プロテスタント系全般 | tolerance_heretic +1 | `[src: religious_aspects/common.txt:176-202]` |
| 小教区登録（Parish Registers） | 英国国教会・カルヴァン他 | monthly_religious_influence +0.1、税収効率ボーナス | `[src: religious_aspects/common.txt:341-358]` |

#### ルター派（Lutheran）固有修正値

| 項目 | 内容 | 出典 |
|------|------|------|
| 聖職者エステート満足度目標 | medium_permanent（中程度の恒常目標） | `[src: religions/christian.txt:323]` |
| 税収効率 | tax_income_efficiency bonus | `[src: religions/christian.txt:324]` |
| 月間 Religious Influence | +0.1 | `[src: religions/christian.txt:326]` |
| 最大 Religious Influence | 400 | `[src: religions/christian.txt:328]` |

**ルター派固有アスペクト**

| アスペクト | 修正値 | 出典 |
|-----------|--------|------|
| 敬虔主義（Pietism） | global_max_literacy +5、monthly_religious_influence +0.1 | `[src: religious_aspects/protestant.txt:17-29]` |
| 正戦論（Justified Conflicts） | antagonism_received_modifier −0.1、global_war_score_cost −0.05 | `[src: religious_aspects/protestant.txt:1-15]` |

#### カルヴァン派（Calvinist）固有修正値

| 項目 | 内容 | 出典 |
|------|------|------|
| 聖職者エステート満足度目標 | large_permanent（大きな恒常目標） | `[src: religions/christian.txt:117]` |
| 戦闘予定説（is_battles_preordained） | 有効（退却遅延 +20） | `[src: religions/christian.txt:119-120]` |
| 月間芸術開始チャンス | −0.1 | `[src: religions/christian.txt:122]` |
| 軍規（Discipline） | +0.05 | `[src: religions/christian.txt:123]` |

**カルヴァン派固有アスペクト**

| アスペクト | 修正値 | 出典 |
|-----------|--------|------|
| アルミニウス主義（Arminianism） | tolerance_own −1、tolerance_heretic +1、stability_cost −0.1 | `[src: religious_aspects/calvinist.txt:1-24]` |
| ゴマール主義（Gomarism） | tolerance_own +1、tolerance_heretic −1、stability_cost −0.1 | `[src: religious_aspects/calvinist.txt:26-49]` |
| 制度化アルミニウス主義 | 上記に加え research_speed +0.1 | `[src: religious_aspects/calvinist.txt:51-74]` |
| 制度化ゴマール主義 | 上記に加え global_pop_conversion_speed +0.15 | `[src: religious_aspects/calvinist.txt:76-99]` |

#### 英国国教会（Anglican）固有修正値

| 項目 | 内容 | 出典 |
|------|------|------|
| 最大識字率 | global_max_literacy +5 | `[src: religions/christian.txt:16]` |
| 建設コスト | global_build_buildings_cost −0.05 | `[src: religions/christian.txt:17]` |
| 月間 Religious Influence | +0.1 | `[src: religions/christian.txt:19]` |

**英国国教会固有アスペクト**

| アスペクト | 修正値 | 出典 |
|-----------|--------|------|
| 第一聖書（Prima Scriptura） | tolerance_heathen +0.5（Sola Scripturaとは共存不可） | `[src: religious_aspects/anglican.txt:1-13]` |

#### フス派（Hussite）固有修正値

| 項目 | 内容 | 出典 |
|------|------|------|
| 傭兵維持費 | army_auxiliary_maintenance_cost_modifier −0.25 | `[src: religions/christian.txt:245]` |
| 人口昇格速度 | global_pop_promotion_speed_modifier +0.10 | `[src: religions/christian.txt:246]` |
| 人口改宗速度 | global_pop_conversion_speed_modifier +0.10 | `[src: religions/christian.txt:247]` |

---

### ボスニア教会（Bosnian Church）

| 項目 | 内容 | 出典 |
|------|------|------|
| 異端への寛容 | tolerance_heretic +1.5 | `[src: religions/christian.txt:88]` |
| 聖職者・貴族満足度目標 | medium_permanent | `[src: religions/christian.txt:89-90]` |
| 修道院建設可否 | 可 | `[src: religions/christian.txt:92]` |
| 最大 Religious Influence | 900 | `[src: religions/christian.txt:93]` |
| 列聖 | あり | `[src: religions/christian.txt:83]` |

---

## イスラム教グループ

### イスラム教共通メカニクス

**Piety スライダー（敬虔度：神秘主義 vs 律法主義）**

| 方向 | 解放条件 | 代表的法学派 |
|------|---------|-----------|
| 律法主義（Jurisprudence、≥50） | 法学派（Fiqh Schools）が選択可能 | ハナフィー・ハンバリー・マーリキー・シャーフィイー・ザーヒリー派 |
| 神秘主義（Mysticism、≤−50） | スーフィー教団が選択可能 | ベクタシー・チシュティー・メヴレヴィー・ナクシュバンディー他 |

`[src: religious_schools/sunni.txt（enabled_for_country 条件）]`

**共通禁止事項**

- ワイン・ビール・蒸留酒の輸入禁止（`ban_imports_of_wine/beer/liquor = yes`）
- 奴隷労働需要は許可（`allow_rgo_slave_demand = yes`）
- 認可される宗教的人物数（Religious Figure）の基本値: 1 `[src: religions/muslim.txt:34-40, 64-67, 91-96]`

**max_religious_figures_for_religion（宗教的人物の最大数計算）**

| 条件 | 追加量 |
|------|--------|
| 宗教を信奉する国家ごと | +1.5 |
| 宗教の聖地（Holy Site）ごと | +1.0 |

`[src: religions/muslim.txt（各宗教の max_religious_figures_for_religion ブロック）]`

---

### スンニ派（Sunni）

| 項目 | 内容 | 出典 |
|------|------|------|
| 貿易効率ボーナス | trade_efficiency（tiny bonus） | `[src: religions/muslim.txt:153-155]` |
| 利用可能法学派 | ハナフィー・ハンバリー・マーリキー・シャーフィイー・ザーヒリー（律法主義） | `[src: religions/muslim.txt:129-133]` |
| 神学校 | アシュアリー・マートゥリーディー・アタリー・ムウタズィラ・ワッハービー | `[src: religions/muslim.txt:135-139]` |
| スーフィー教団 | ベクタシー・チシュティー・ハルワティー・メヴレヴィー・ナクシュバンディー・カーディリー・サファヴィー・シャーズィリー・スフラワルディー・イサーウィーヤ・ディーン・イ・イラーヒー | `[src: religions/muslim.txt:141-150]` |

**スンニ派法学派（律法主義 ≥50 で選択可能）**

| 法学派 | 修正値 | 出典 |
|--------|--------|------|
| ハナフィー（Hanafi） | global_clergy_max_literacy +10 | `[src: religious_schools/sunni.txt:3-24]` |
| ハンバリー（Hanbali） | antagonism_received_modifier −0.05 | `[src: religious_schools/sunni.txt:26-47]` |
| マーリキー（Maliki） | global_monthly_development +0.001 | `[src: religious_schools/sunni.txt:49-70]` |
| シャーフィイー（Shafii） | global_merchant_capacity_modifier +0.1 | `[src: religious_schools/sunni.txt:72-94]` |
| ザーヒリー（Zahiri） | global_pop_conversion_speed_modifier +0.1 | `[src: religious_schools/sunni.txt:96-116]` |

**スンニ派神学校（常時選択可能）**

| 神学校 | 修正値 | 出典 |
|--------|--------|------|
| アシュアリー（Ashari） | research_speed_modifier +0.05 | `[src: religious_schools/sunni.txt:120-139]` |
| マートゥリーディー（Maturidi） | tolerance_own +1 | `[src: religious_schools/sunni.txt:141-160]` |
| アタリー（Athari） | stability_investment（standard） | `[src: religious_schools/sunni.txt:162-181]` |
| ムウタズィラ（Mutazili） | pop_join_rebel_threshold −0.05 | `[src: religious_schools/sunni.txt:183-202]` |
| ワッハービー（Wahhabi）※条件付き | stability_investment（small）、pop_conversion_speed +0.1、tolerance_heretic −2 | `[src: religious_schools/sunni.txt:204-224]` |

---

### シーア派（Shia）

| 項目 | 内容 | 出典 |
|------|------|------|
| 陸軍士気ボーナス | land_morale_modifier +0.05 | `[src: religions/muslim.txt:91]` |
| 利用可能法学派 | ジャアファリー・イスマーイーリー・ザイドィー（律法主義） | `[src: religions/muslim.txt:71-77]` |
| 神学校 | イマーミーヤ・ニザーリー・ムスターリー・アレウィー・アラウィー | `[src: religions/muslim.txt:76-80]` |
| スーフィー教団 | ベクタシー・ハルワティー・メヴレヴィー・サファヴィー・シャーズィリー・スフラワルディー・イサーウィーヤ・ディーン・イ・イラーヒー | `[src: religions/muslim.txt:82-88]` |

**シーア派固有法学派**

| 法学派 | 修正値 | 出典 |
|--------|--------|------|
| ジャアファリー（Jafari） | global_population_growth +0.00025 | `[src: religious_schools/shia.txt:3-23]` |
| イスマーイーリー（Ismaili） | monthly_legitimacy/republican_tradition/devotion/horde_unity/tribal_cohesion +0.1 | `[src: religious_schools/shia.txt:27-50]` |
| ザイドィー（Zaidi） | tolerance_heretic +1 | `[src: religious_schools/shia.txt:52-71]` |
| イマーミーヤ（Imamiya） | army_infantry_power +0.05 | `[src: religious_schools/shia.txt:75-94]` |
| ニザーリー（Nizari） | tolerance_heathen +1 | `[src: religious_schools/shia.txt:96-115]` |
| ムスターリー（Mustali） | global_pop_conversion_speed_modifier +0.1 | `[src: religious_schools/shia.txt:117-136]` |
| アレウィー（Alevism）※テュルク・クルド文化限定 | pop_join_rebel_threshold −0.05 | `[src: religious_schools/shia.txt:138-165]` |
| アラウィー（Alawi）※アラウィー文化限定 | tolerance_heathen +1 | `[src: religious_schools/shia.txt:167-188]` |

---

### イバード派（Ibadi）

| 項目 | 内容 | 出典 |
|------|------|------|
| 商人力（Merchant Power）ボーナス | global_merchant_power +0.05 | `[src: religions/muslim.txt:31]` |
| 造船速度 | ship_build_speed +0.05 | `[src: religions/muslim.txt:32]` |
| 利用可能法学派 | イバード固有 + シーア系 + スンニ系の全派が選択可能 | `[src: religions/muslim.txt:7-28]` |

> イバード派は最も多くの法学派にアクセスできる。神秘主義・律法主義を問わず全イスラム法学派が利用可能。

---

### スーフィー教団（Sufi Schools）— 神秘主義側（≤−50）で選択可能

| 教団名 | 修正値 | 適用宗教 | 出典 |
|--------|--------|---------|------|
| ベクタシー（Bektashi）※テュルク文化限定 | army_infantry_power +0.1 | スンニ・シーア | `[src: religious_schools/sufi.txt:1-23]` |
| チシュティー（Chishti） | pop_join_rebel_threshold −0.1 | スンニ | `[src: religious_schools/sufi.txt:25-39]` |
| ハルワティー（Khalwati） | stability_investment（standard） | スンニ・シーア | `[src: religious_schools/sufi.txt:41-61]` |
| メヴレヴィー（Mevlevi） | cultural_influence_modifier +0.1 | スンニ・シーア | `[src: religious_schools/sufi.txt:63-83]` |
| ナクシュバンディー（Naqshbandi） | monthly_legitimacy +0.1 | スンニ | `[src: religious_schools/sufi.txt:85-99]` |
| カーディリー（Qadiri） | monthly_prestige +0.1 | スンニ | `[src: religious_schools/sufi.txt:101-115]` |
| サファヴィー（Safavid） | monthly_army_tradition +0.05 | スンニ・シーア | `[src: religious_schools/sufi.txt:117-137]` |
| シャーズィリー（Shadhili） | cultural_tradition_modifier +0.1 | スンニ・シーア | `[src: religious_schools/sufi.txt:139-159]` |
| スフラワルディー（Suhrawardi） | global_pop_conversion_speed_modifier +0.1 | スンニ・シーア | `[src: religious_schools/sufi.txt:161-181]` |
| イサーウィーヤ（Isawiyya）※条件付き | global_monthly_prosperity +0.001 | スンニ・シーア | `[src: religious_schools/sufi.txt:183-205]` |
| ディーン・イ・イラーヒー（Din-i Ilahi）※条件付き | cultures_capacity +2、tolerance_own −1、tolerance_heathen +1 | スンニ・シーア | `[src: religious_schools/sufi.txt:207-231]` |

**建物：マドラサ（Madrasa）**— イスラム教グループ専用

| 修正値 | 値 |
|--------|---|
| local_clergy_max_literacy | +5 |
| local_pop_conversion_speed_modifier | +0.1 |
| local_tribal_promotion | +0.1 |

`[src: building_types/religion_buildings.txt:111-162]`

**建物：スーフィー道場（Sufi Lodge）**— スーフィズム採用国専用

| 修正値 | 値 |
|--------|---|
| local_clergy_max_literacy | +10 |
| local_pop_conversion_speed_modifier | +0.1 |

`[src: building_types/religion_buildings.txt:164-201]`

---

## 仏教グループ

### 仏教共通メカニクス：カルマ（Karma）

テーラワーダ・大乗・チベット仏教・ジャイナ教・ボン教などが `has_karma = yes` を持つ。月間カルマ値（`monthly_karma`）が蓄積する。

| 宗教 | monthly_karma | 出典 |
|------|-------------|------|
| ボン教（Bon） | +0.1 | `[src: religions/buddhist.txt:10]` |
| 大乗仏教（Mahayana） | +0.1 | `[src: religions/buddhist.txt:30]` |
| テーラワーダ（Theravada） | +0.1 | `[src: religions/buddhist.txt:82]` |
| サンミティヤ派（Sammitiya） | +0.1 | `[src: religions/buddhist.txt:98]` |
| チベット仏教（Tibetan Buddhism） | +0.1 | `[src: religions/buddhist.txt:117]` |

---

### テーラワーダ（Theravada）— 上座部仏教

| 項目 | 内容 | 出典 |
|------|------|------|
| 異端への寛容 | tolerance_heretic +1 | `[src: religions/buddhist.txt:81]` |
| 月間カルマ | +0.1 | `[src: religions/buddhist.txt:82]` |
| 内閣効率 | country_cabinet_efficiency +0.05 | `[src: religions/buddhist.txt:83]` |
| 修道院建設可否 | 可 | `[src: religions/buddhist.txt:84]` |
| 最大宗派数 | 1 | `[src: religions/buddhist.txt:79]` |

---

### 大乗仏教（Mahayana）

| 項目 | 内容 | 出典 |
|------|------|------|
| 異端への寛容 | tolerance_heretic +1 | `[src: religions/buddhist.txt:29]` |
| 月間カルマ | +0.1 | `[src: religions/buddhist.txt:30]` |
| 最大識字率 | global_max_literacy +5 | `[src: religions/buddhist.txt:31]` |
| 修道院建設可否 | 可 | `[src: religions/buddhist.txt:32]` |
| 最大宗派数 | 3 | `[src: religions/buddhist.txt:27]` |

---

### チベット仏教（Tibetan Buddhism）

| 項目 | 内容 | 出典 |
|------|------|------|
| 月間戦争疲弊度 | monthly_war_exhaustion −0.05 | `[src: religions/buddhist.txt:116]` |
| 月間カルマ | +0.1 | `[src: religions/buddhist.txt:117]` |
| 最大識字率 | global_max_literacy +5 | `[src: religions/buddhist.txt:118]` |
| 修道院建設可否 | 可 | `[src: religions/buddhist.txt:119]` |
| 最大宗派数 | 1 | `[src: religions/buddhist.txt:113]` |

---

### 神道（Shinto）

神道は仏教グループに属するが固有パラメータを持つ。

| 項目 | 内容 | 出典 |
|------|------|------|
| 純粋さ（Purity） | あり（`has_purity = yes`） | `[src: religions/buddhist.txt:50]` |
| 名誉（Honor） | あり（`has_honor = yes`） | `[src: religions/buddhist.txt:51]` |
| 最大宗派数 | 1 | `[src: religions/buddhist.txt:52]` |
| 最大識字率 | global_max_literacy +10 | `[src: religions/buddhist.txt:55]` |
| 異端への寛容 | tolerance_heretic +1 | `[src: religions/buddhist.txt:56]` |
| 異教への寛容 | tolerance_heathen +1 | `[src: religions/buddhist.txt:57]` |
| 修道院建設可否 | 可 | `[src: religions/buddhist.txt:58]` |

**神道固有勢力（Factions）**

| 勢力名 | 内容 |
|--------|------|
| imperial_court（朝廷） | 天皇系勢力 |
| shogunate_court（幕府） | 武家系勢力 |
| ikko_ikki（一向一揆） | 民衆反乱勢力 |
| religious_sects（宗教宗派） | 仏教各派 |
| kirishitan_monks（キリシタン修道士） | キリスト教宣教師 |

`[src: religions/buddhist.txt:61-68]`

---

### 三教（Sanjiao）— 三教合一

| 項目 | 内容 | 出典 |
|------|------|------|
| 正義感（Righteousness） | あり（`allow_righteousness = yes`） | `[src: religions/buddhist.txt:138]` |
| 調和（Harmony） | あり（`allow_harmony = yes`） | `[src: religions/buddhist.txt:139]` |
| 月間正統性 | monthly_legitimacy +0.05 | `[src: religions/buddhist.txt:140]` |
| 最大識字率 | global_max_literacy +10 | `[src: religions/buddhist.txt:141]` |
| 修道院建設可否 | 可 | `[src: religions/buddhist.txt:142]` |
| 最大宗派数 | 3（儒教・道教で 2 枠すでに占有） | `[src: religions/buddhist.txt:136]` |
| 大乗仏教との関係 | 親族（kindred） | `[src: religions/buddhist.txt:148]` |

---

### ボン教（Bon）

| 項目 | 内容 | 出典 |
|------|------|------|
| 最大識字率 | global_max_literacy +5 | `[src: religions/buddhist.txt:9]` |
| 全エステート満足度目標 | small_permanent（小さな恒常目標） | `[src: religions/buddhist.txt:10]` |
| 月間カルマ | +0.1 | `[src: religions/buddhist.txt:11]` |
| 修道院建設可否 | 可 | `[src: religions/buddhist.txt:12]` |
| チベット仏教との関係 | 親族（kindred） | `[src: religions/buddhist.txt:17]` |

---

## ダルマグループ（Dharmic）

### ヒンドゥー教（Hindu）

| 項目 | 内容 | 出典 |
|------|------|------|
| 異教への寛容 | tolerance_heathen +1 | `[src: religions/dharmic.txt:9]` |
| 自信仰への寛容 | tolerance_own +1 | `[src: religions/dharmic.txt:10]` |
| 宗教的人物の基本数 | 1 | `[src: religions/dharmic.txt:11]` |
| アヴァタール（Avatars） | あり（`has_avatars = yes`） | `[src: religions/dharmic.txt:7]` |

**ヒンドゥー法学派（Hindu Schools）**

| 学派 | 修正値 | 出典 |
|------|--------|------|
| サーンキヤ（Samkhya） | tolerance_heathen +0.5、tolerance_heretic +0.5 | `[src: religious_schools/hinduism.txt:1-15]` |
| ヨーガ（Yoga） | global_population_growth +0.00025 | `[src: religious_schools/hinduism.txt:17-30]` |
| ニヤーヤ（Nyaya） | global_monthly_literacy +0.01 | `[src: religious_schools/hinduism.txt:32-45]` |
| ヴァイシェーシカ（Vaisheshika） | global_max_literacy +5 | `[src: religious_schools/hinduism.txt:47-60]` |
| ミーマーンサー（Mimamsa） | cultural_tradition_modifier +0.1 | `[src: religious_schools/hinduism.txt:62-75]` |
| ヴェーダーンタ（Vedanta） | tolerance_own +1 | `[src: religious_schools/hinduism.txt:77-90]` |

---

### ジャイナ教（Jain）

| 項目 | 内容 | 出典 |
|------|------|------|
| 無条件宣戦禁止 | cannot_declare_no_cb_wars = yes | `[src: religions/dharmic.txt:43]` |
| 月間識字率 | global_monthly_literacy +0.03 | `[src: religions/dharmic.txt:44]` |
| 自制（Self Control） | あり（`allow_self_control = yes`） | `[src: religions/dharmic.txt:45]` |
| 修道院建設可否 | 可 | `[src: religions/dharmic.txt:46]` |
| 宗教的人物の基本数 | 1 | `[src: religions/dharmic.txt:47]` |
| カルマ | あり（`has_karma = yes`） | `[src: religions/dharmic.txt:32]` |

> ジャイナ教は無条件宣戦が不可なため、拡張には同盟・宣戦布告理由（CB）の取得が必須。貿易・経済特化国向き。

**ジャイナ法学派（現在スクリプト内でコメントアウト済み）**

下記の学派はスクリプト上では `# religious_school = ...` でコメントアウトされており、Patch 1.1 時点では未実装。

`[src: religions/dharmic.txt:34-41]`（未検証）

| 学派名 | 状態 |
|--------|------|
| ムーラ・サンガ | 未実装（コメントアウト） |
| バラタカラ・ガナ | 未実装（コメントアウト） |
| カシュタ・サンガ | 未実装（コメントアウト） |

ただし `religious_schools/jain.txt` には同名学派が実装されており、何らかの条件で解放される可能性あり。

**ジャイナ法学派（jain.txt に定義済み）**

| 学派 | 修正値 | 出典 |
|------|--------|------|
| ムーラ・サンガ（Mula Sangh） | global_max_literacy +5 | `[src: religious_schools/jain.txt:1-14]` |
| バラタカラ・ガナ（Balatkara Gana） | cultural_tradition_modifier +0.1 | `[src: religious_schools/jain.txt:16-29]` |
| カシュタ・サンガ（Kashtha Sangha） | global_pop_conversion_speed_modifier +0.05 | `[src: religious_schools/jain.txt:31-44]` |
| ウパケーシャ・ガッチャ（Upkesa Gaccha） | monthly_legitimacy +0.1 | `[src: religious_schools/jain.txt:46-59]` |
| クハラタラ・ガッチャ（Kharatara Gaccha） | stability_investment（tiny） | `[src: religious_schools/jain.txt:61-74]` |
| タパ・ガッチャ（Tapa Gaccha） | monthly_self_control +0.05 | `[src: religious_schools/jain.txt:76-89]` |
| トリシュティカ・ガッチャ（Tristutik Gaccha） | clergy_estate_satisfaction_recovery +0.0025 | `[src: religious_schools/jain.txt:91-104]` |

---

### シク教（Sikhism）

| 項目 | 内容 | 出典 |
|------|------|------|
| 解放日 | 1526年1月1日（enable = 1526.01.01） | `[src: religions/dharmic.txt:66]` |
| 研究速度 | research_speed_modifier +0.1 | `[src: religions/dharmic.txt:69]` |
| 全エステート満足度 | global_estate_target_satisfaction（small_permanent） | `[src: religions/dharmic.txt:70]` |

---

## ゾロアスター教グループ

### ゾロアスター教（Zoroastrian）

| 項目 | 内容 | 出典 |
|------|------|------|
| 自信仰への寛容 | tolerance_own +1 | `[src: religions/zoroastrian.txt:10]` |
| 貿易効率 | trade_efficiency（medium bonus） | `[src: religions/zoroastrian.txt:11]` |

---

## トナルグループ（Tonal）— メソアメリカ

### ナワトル（Nahuatl）— アステカ系

| 項目 | 内容 | 出典 |
|------|------|------|
| 陸軍士気 | land_morale_modifier +0.1 | `[src: religions/tonal.txt:9]` |
| 固有ユニット建設可 | global_may_build_nahuatl_units = yes（ジャガー戦士・鷹戦士） | `[src: religions/tonal.txt:10]` |
| 奴隷制 | any_pop_can_be_slave = yes | `[src: religions/tonal.txt:11]` |
| Doom（破滅）メカニクス | あり（`enable_doom = yes`） | `[src: religions/tonal.txt:12]` |
| Religious Aspects スロット | 1 | `[src: religions/tonal.txt:6]` |

**Doom（破滅度）管理の重要性**

Doom が蓄積するほど国家にペナルティが加わる。これを抑制するため「宗教フォーカス（Religious Focus）」を完遂する必要がある。

**ナワトル宗教フォーカス（Religious Focuses）— 全8項目**

| フォーカス | 完遂ボーナス | 出典 |
|-----------|-----------|------|
| オメテオトル採択（Adopt Ometeotl） | country_child_education +0.1、monthly_doom −0.1 | `[src: religious_focuses/nahuatl.txt:1-63]` |
| 守護神高揚（Elevate Patron God） | global_pop_conversion_speed_modifier +0.2 | `[src: religious_focuses/nahuatl.txt:65-117]` |
| シワコアトル設立（Establish Cihuacoatl） | country_cabinet_efficiency +0.1 | `[src: religious_focuses/nahuatl.txt:119-182]` |
| クアウピルティン拡大（Expand Cuahpipiltin） | global_manpower_modifier +0.1 | `[src: religious_focuses/nahuatl.txt:184-227]` |
| 軍国主義強化（Increase Militarism） | army_tradition_decay −0.001 | `[src: religious_focuses/nahuatl.txt:229-283]` |
| 花の戦争制度化（Institute Flower Wars） | slave_raid_efficiency +0.25 | `[src: religious_focuses/nahuatl.txt:285-343]` |
| 法制度改革（Legal Reforms） | government_size +1 | `[src: religious_focuses/nahuatl.txt:345-418]` |
| 生贄率引き上げ（Raise Sacrifice Rate） | monthly_doom −0.05 | `[src: religious_focuses/nahuatl.txt:420-478]` |

「オメテオトル採択」はすべての他フォーカスを完遂した後に解放される最終フォーカス。`[src: religious_focuses/nahuatl.txt:43-50]`

**ナワトル固有アスペクト（宗教的アスペクト = 神々への崇拝）**

| アスペクト（神） | 修正値 | 出典 |
|---------------|--------|------|
| トラロック（Tlaloc）— 雨神 | global_monthly_prosperity +0.001 | `[src: religious_aspects/tonal.txt:4-11]` |
| フィツィロポチトリ（Huitzilopochtli）— 戦争神 | land_morale_modifier +0.05、monthly_war_exhaustion −0.03 | `[src: religious_aspects/tonal.txt:13-21]` |
| ケツァルコアトル（Quetzalcoatl）— 知恵神 | research_speed_modifier +0.1 | `[src: religious_aspects/tonal.txt:23-30]` |
| テスカトリポカ（Tezcatlipoca）— 暗黒神 | monthly_diplomats +0.2、colonial_maintenance_cost −0.1 | `[src: religious_aspects/tonal.txt:32-40]` |
| シウテクトリ（Xiuhtecuhtli）— 火神 | army_maintenance_cost −0.15 | `[src: religious_aspects/tonal.txt:42-49]` |
| コアトリクエ（Coatlicue）— 豊穣神 | global_life_expectancy +2、global_population_growth +0.00025 | `[src: religious_aspects/tonal.txt:51-59]` |

---

### マヤ（Mayan）

| 項目 | 内容 | 出典 |
|------|------|------|
| 土地戦闘威信 | prestige_from_land_battle +0.1 | `[src: religions/tonal.txt:56]` |
| 徴兵回復修正 | levy_recovery_modifier +0.1 | `[src: religions/tonal.txt:57]` |
| Religious Aspects スロット | 1 | `[src: religions/tonal.txt:50]` |
| Religious Influence | あり | `[src: religions/tonal.txt:53]` |

**マヤ固有アスペクト**

| 神 | 修正値 | 出典 |
|----|--------|------|
| チャアク（Chaac）— 雨神 | global_monthly_prosperity +0.001 | `[src: religious_aspects/tonal.txt:98-106]` |
| ククルカン（Kukulkan） | army_movement_speed +0.1 | `[src: religious_aspects/tonal.txt:109-118]` |
| カウィール（Kawiil） | army_maintenance_cost −0.10 | `[src: religious_aspects/tonal.txt:120-129]` |
| テペウ（Tepeu）— 創造神 | stability_cost −0.1 | `[src: religious_aspects/tonal.txt:131-138]` |
| フラカン（Huracan）— 嵐神 | global_hostile_attrition +1、global_raw_material_output +0.05 | `[src: religious_aspects/tonal.txt:140-148]` |
| フンフナフプー（Hunhunahpu） | global_life_expectancy +3、global_population_growth +0.00025 | `[src: religious_aspects/tonal.txt:150-157]` |
| イシュチェル（Ixchel）— 医療神 | global_disease_resistance +0.1 | `[src: religious_aspects/tonal.txt:159-167]` |

---

## ペルー民族宗教グループ

### インティ（Inti）— インカ系

| 項目 | 内容 | 出典 |
|------|------|------|
| 軍隊移動速度 | army_movement_speed +0.1 | `[src: religions/folk_peruvian.txt:11]` |
| 軍隊補充コスト | army_reinforce_cost −0.1 | `[src: religions/folk_peruvian.txt:12]` |
| 文化伝統修正 | cultural_tradition_modifier +0.05 | `[src: religions/folk_peruvian.txt:13]` |
| ヤナンティン（Yanantin）バランス | あり（`has_yanantin = yes`） | `[src: religions/folk_peruvian.txt:6]` |
| Religious Aspects スロット | 1 | `[src: religions/folk_peruvian.txt:7]` |

**Yanantin（ヤナンティン）— 二元均衡メカニクス**

各神へのアスペクトは `monthly_yanantin` を −0.5 または +0.5 で変化させる。バランスの維持が重要。

| アスペクト（神） | 修正値 | Yanantin 移動 | 出典 |
|---------------|--------|-------------|------|
| ビラコチャ（Viracocha） | stability_cost −0.1 | −0.5 | `[src: religious_aspects/inti.txt:3-9]` |
| インティ神（Inti） | global_life_expectancy +2、population_growth +0.0002 | −0.5 | `[src: religious_aspects/inti.txt:12-19]` |
| イジャパ（Illapa）— 雷神 | land_morale_modifier +0.1 | −0.5 | `[src: religious_aspects/inti.txt:22-27]` |
| スパイ（Supay） | global_hostile_attrition +0.25、expand_rgo_mining_cost −0.025 | −0.5 | `[src: religious_aspects/inti.txt:30-37]` |
| ママ・キジャ（Mamaquilla）— 月神 | global_separatism −0.05 | +0.5 | `[src: religious_aspects/inti.txt:41-47]` |
| パチャママ（Pachamama）— 大地母 | global_monthly_prosperity +0.001 | +0.5 | `[src: religious_aspects/inti.txt:50-55]` |
| ママ・コチャ（Mama Cocha）— 海神 | naval_morale_modifier +0.1 | +0.5 | `[src: religious_aspects/inti.txt:58-63]` |
| ウルピワチャク（Urpihuachac） | diplomatic_capacity_modifier +0.05 | +0.5 | `[src: religious_aspects/inti.txt:65-71]` |

---

## 宗教改宗の仕組み（共通）

### 安定度コスト（宗教変更）

EU4 の宣教師システムは廃止され、EU5 では異なるメカニクスで宗教改宗が進む。安定度変更コストの基本値として `stability 50` が確認されている。

`[src: common/diplomatic_costs/00_hardcoded.txt]`（※宗教変更固有コストは同ファイルに記載なし。安定度コストは別経路で処理）（未検証）

### 改宗に影響するスクリプト確認済み修正値

| 修正値 | 効果 | 代表的な発生源 |
|--------|------|-------------|
| global_pop_conversion_speed_modifier | 住民改宗速度 | 法学派・建物・アスペクト多数 |
| local_pop_conversion_speed_modifier | 地域住民改宗速度 | 修道院（+0.1）・マドラサ（+0.1） |
| can_have_monasteries | 修道院建設可否 | カトリック・正教・仏教系等 |

### 宗教建物一覧（Patch 1.1 スクリプト確認済み）

| 建物名 | 適用宗教 | 主要修正値 | 出典 |
|--------|---------|---------|------|
| 修道院（Monastery） | can_have_monasteries 宗教全般 | 改宗速度 +0.1、聖職者識字率 +10 | `[src: building_types/religion_buildings.txt:1-59]` |
| 要塞教会（Fortress Church） | 同上（修道院が前提） | 改宗速度 +0.1、識字率 +10、守備兵規模 +0.05 | `[src: building_types/religion_buildings.txt:61-109]` |
| マドラサ（Madrasa） | イスラム教グループ | 改宗速度 +0.1、聖職者識字率 +5、部族昇進 +0.1 | `[src: building_types/religion_buildings.txt:111-162]` |
| スーフィー道場（Sufi Lodge） | イスラム教（スーフィズム採用時） | 改宗速度 +0.1、聖職者識字率 +10 | `[src: building_types/religion_buildings.txt:164-201]` |
| 正教会修道院（Orthodox Monastery） | 正教会のみ | 改宗速度 +0.1、聖職者識字率 +10 | `[src: building_types/religion_buildings.txt:203-241]` |
| ミアフィジット修道院（Miaphysite Monastery） | ミアフィジット派のみ | 改宗速度 +0.1、識字率 +10、首都で Rite Power +0.05 | `[src: building_types/religion_buildings.txt:243-282]` |

---

## 用語対照表

| 日本語 | 英語（ゲーム内） | 備考 |
|--------|--------------|------|
| 宗教的影響力 | Religious Influence | プロテスタント系・正教系で使用 |
| カルマ | Karma | 仏教・ジャイナ教 |
| 純粋さ | Purity | 神道固有 |
| 名誉 | Honor | 神道固有 |
| 破滅度 | Doom | ナワトル固有。蓄積するとペナルティ |
| ヤナンティン | Yanantin | インティ（インカ）固有の均衡メカニクス |
| 正義感 | Righteousness | 三教固有 |
| 調和 | Harmony | 三教固有 |
| 教会方針 | Church Aspect | プロテスタント系が選択するアスペクト |
| 法学派 | Religious School / School | イスラム・ヒンドゥー・ジャイナで使用 |
| スーフィー教団 | Sufi School / Order | イスラム神秘主義側で選択 |
| 宗教フォーカス | Religious Focus | ナワトル固有の改革システム |
| 列聖 | Canonization | カトリック・正教・ボスニア教会・ミアフィジット等 |
| 総主教座 | (Autocephalous) Patriarchate | 正教・ミアフィジット・ネストリウス派 |
| アヴァタール | Avatar | ヒンドゥー教固有キャラクターシステム |
| 宗派 | Sect | 仏教系の宗派（max_sects で上限設定） |
| Rite Power（儀式力） | Rite Power | ミアフィジット現行実装、正教は 1.2 予定 |
| Piety スライダー | Mysticism vs Jurisprudence | イスラム教グループ全体 |

---

## 出典

| ファイルパス | 内容 |
|------------|------|
| `in_game/common/religion_groups/00_default.txt` | 宗教グループ定義・奴隷取引フラグ |
| `in_game/common/religions/christian.txt` | キリスト教各宗教の定義・修正値 |
| `in_game/common/religions/muslim.txt` | イスラム教三派の定義・修正値 |
| `in_game/common/religions/buddhist.txt` | 仏教系宗教の定義・修正値 |
| `in_game/common/religions/dharmic.txt` | ダルマ系宗教の定義・修正値 |
| `in_game/common/religions/zoroastrian.txt` | ゾロアスター教の定義 |
| `in_game/common/religions/tonal.txt` | ナワトル・マヤ・メソアメリカの定義 |
| `in_game/common/religions/folk_peruvian.txt` | インティ系宗教の定義 |
| `in_game/common/religious_aspects/common.txt` | プロテスタント系共通アスペクト |
| `in_game/common/religious_aspects/protestant.txt` | ルター派固有アスペクト |
| `in_game/common/religious_aspects/calvinist.txt` | カルヴァン派固有アスペクト |
| `in_game/common/religious_aspects/anglican.txt` | 英国国教会固有アスペクト |
| `in_game/common/religious_aspects/hussite.txt` | フス派固有アスペクト |
| `in_game/common/religious_aspects/tonal.txt` | ナワトル・マヤ各神アスペクト |
| `in_game/common/religious_aspects/inti.txt` | インティ神群アスペクト |
| `in_game/common/religious_schools/sunni.txt` | スンニ派法学派・神学校 |
| `in_game/common/religious_schools/shia.txt` | シーア派法学派・神学校 |
| `in_game/common/religious_schools/sufi.txt` | スーフィー教団一覧 |
| `in_game/common/religious_schools/hinduism.txt` | ヒンドゥー六哲学学派 |
| `in_game/common/religious_schools/jain.txt` | ジャイナ法学派 |
| `in_game/common/religious_focuses/nahuatl.txt` | ナワトル宗教フォーカス8種 |
| `in_game/common/building_types/religion_buildings.txt` | 宗教建物定義・修正値 |

> スクリプト確認日: 2026-04-08 / EU5 Patch 1.1.10 時点
