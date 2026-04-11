# HRE メカニクス調査データ

> ゲームスクリプト一次ソース方式。数値・効果には `[ファイル名:行番号]` の出典を付ける。

## 調査ファイル

| ファイル | 内容 |
|---|---|
| `common/international_organizations/hre.txt` | HRE 組織定義（911行） |
| `common/laws/20_hre.txt` | 帝国法・ポリシー定義 |
| `events/hre.txt` | HRE イベント（1,084行） |
| `main_menu/localization/japanese/international_organizations_l_japanese.yml` | 日本語ローカライズ（組織系） |
| `main_menu/localization/japanese/laws_and_policies_l_japanese.yml` | 日本語ローカライズ（法律系） |
| `main_menu/localization/japanese/country_interactions_l_japanese.yml` | 日本語ローカライズ（外交アクション） |

---

## 1. HRE 組織定義 — 基本設定

| 属性 | 値 | src |
|---|---|---|
| 議会タイプ（初期） | `hre_court_assembly`（宮廷議会） | hre.txt:15 |
| 王朝パワー連動 | `has_dynastic_power = yes` | hre.txt:17 |
| リーダー選出方法 | 投票（`vote`）、決議 `hre_election` | hre.txt:46-47 |
| リーダー変更トリガー | `rulerchange`（君主交代時） | hre.txt:45 |
| リーダー不在で解散 | しない（`disband_if_no_leader = no`） | hre.txt:48 |
| 防衛戦争加入（メンバー攻撃時） | 皇帝国のみ参戦（`only_leader_country_joins_defensive_wars = yes`） | hre.txt:51 |
| 防衛戦争への共同参戦 | 可（`joins_defensive_wars_as_co_belligerent = yes`） | hre.txt:52 |
| 軍事アクセス共有 | 戦時中は全メンバーに自動付与 | hre.txt:112 |
| アンタゴニズム倍率（メンバー間） | ×1.25 | hre.txt:119 |
| アンタゴニズム倍率（非メンバーがメンバー領取得） | ×2.0 | hre.txt:120 |
| 反乱支援許可（皇帝） | 可（`allowed_support_rebels = yes`） | hre.txt:155 |
| 帝国の権威（IA）変数 | 0〜100、毎月変動 | hre.txt:362-656 |

---

## 2. 皇帝ボーナス（leader_modifier）

皇帝国（`leader_country`）が自動取得するボーナス一覧。

| 効果 | 値 | src |
|---|---|---|
| 外交容量 | +1 | hre.txt:139 |
| 最大外交官数 | +2 | hre.txt:140 |
| 外交射程 | +500 | hre.txt:141 |
| 要塞上限 | +1 | hre.txt:143 |
| 芸術家スロット | +1 | hre.txt:145 |
| 文化容量 | +1 | hre.txt:146 |
| 政府規模 | +1 | hre.txt:147 |
| 毎月威信 | +0.1 | hre.txt:148 |
| 毎月外交官（外交アクション頻度） | +0.5 | hre.txt:157 |
| 同盟許可 | 可 | hre.txt:150 |
| 保証許可 | 可 | hre.txt:151 |
| 介入戦争許可 | 可 | hre.txt:153 |
| 平和強制許可 | 可 | hre.txt:154 |
| 戦争威嚇許可 | 可 | hre.txt:155 |
| 大国スコア免除（喪失閾値） | 50 | hre.txt:137 |

---

## 3. 帝国の権威（IA）— 月次変動要因

帝国の権威（0〜100）が変動する要因。

### 上昇要因

| 要因 | 効果 | src |
|---|---|---|
| 帝国内平和 | +0.05/月 | hre.txt:391-402 |
| 帝国自由都市 1都市につき | +0.003/月 | hre.txt:407-419 |
| 諸侯数（75超の場合） | +0.001×(諸侯数−75)/月 | hre.txt:421-436 |
| 皇帝の統治能力（adm+dip+mil 各50超分） | +(各能力値−50)×0.001/月 | hre.txt:618-635 |
| 王朝パワー | dynastic_power × 0.005/月 | hre.txt:611-615 |
| `monthly_imperial_authority` modifier | modifier 値による | hre.txt:638-640 |
| 防衛戦争勝利（hre.904） | 敵戦力/自戦力 × 5（上限10） | events/hre.txt:706-721 |
| 皇帝が諸侯を臣下に解放（hre.901） | 人口比 ×10（上限20、下限2） | events/hre.txt:477-518 |
| 諸侯が皇帝宗教に改宗（hre.903） | 人口比 ×100（上限20、下限1） | events/hre.txt:588-658 |
| 非 HRE 諸侯の解放（hre.907） | 人口比 ×100（上限20、下限1） | events/hre.txt:778-847 |
| HRE 領土奪還（hre.950） | 人口比（上限1） | events/hre.txt:994-1003 |
| 皇帝が防衛戦争参戦（hre.908） | 自軍人口/攻撃国人口 × 5（上限10） | events/hre.txt:866-894 |

### 低下要因

| 要因 | 効果 | src |
|---|---|---|
| 皇帝がメンバーへの攻撃戦争主導 | −0.5/月 | hre.txt:369-387 |
| 選帝侯不足（1名欠につき） | −0.1/月 | hre.txt:442-455 |
| 属国選帝侯（1名につき） | −0.05/月 | hre.txt:456-471 |
| 大司教選帝侯不足（1名欠につき） | −0.1/月 | hre.txt:472-489 |
| 属国大司教選帝侯（1名につき） | −0.05/月 | hre.txt:490-505 |
| 異教諸侯（宗教差異に応じて変動） | 各諸侯の宗教乖離度 × −0.01（または −0.005）/月 | hre.txt:507-531 |
| ドイツ地域の非メンバー領土（1地域ごと） | −0.003/月 | hre.txt:533-551 |
| その他 HRE 地域の非メンバー領土 | −0.001/月 | hre.txt:552-571 |
| 外国に従属する HRE メンバー（1国ごと） | −0.003/月 | hre.txt:572-583 |
| 空位期間（皇帝不在） | 月次ゲインをゼロに | hre.txt:584-608 |
| 長期空位期間（`LONG_IMPERIAL_REGENCY_YEARS` 超過） | 超過年数 × −0.25/月 | hre.txt:596-607 |
| 諸侯が皇帝宗教外に改宗（hre.902） | 人口比 × −100（上限−20、下限−1） | events/hre.txt:540-585 |
| 防衛戦争不参加（hre.909） | `imperial_authority_strong_penalty`（定数） | events/hre.txt:911 |
| 非 HRE 国によるメンバー併合（hre.905） | 攻撃国人口/200 × −10（上限−20、下限−1） | events/hre.txt:744-756 |

---

## 4. メンバーシップ条件

| 条件 | 内容 | src |
|---|---|---|
| 加入条件（宗教） | 皇帝国と同一宗教 | hre.txt:239 |
| 加入条件（地理） | HRE 隣接国、または HRE 領土内に拠点を持つ | hre.txt:241-242 |
| 加入条件（皇帝不在時） | 不可（皇帝が存在すること） | hre.txt:236-238 |
| 自動加入 | HRE 内に首都がある国は月次チェックで自動加入 | hre.txt:310-323 |
| 離脱条件 | `golden_bull_policy` 有効中は原則不可（戦争で強制のみ） | hre.txt:257-275 |
| 離脱方法（平和時） | `hre_enable_leave_hre_peace_treaty` modifier が必要 | hre.txt:264-270 |
| 皇帝資格（政体） | 君主制（`monarchy`）、革命国ではない、独立国 | hre.txt:169-172 |
| 皇帝資格（宗教） | 帝国宗教要件を満たすこと（選挙タイプ） | hre.txt:174 |
| 皇帝資格（君主） | 摂政ではない（または相続人あり）、女性不可（別法律で解放可） | hre.txt:176-203 |
| 議会投票資格 | `country_highest_rated_special_status_power > 0` | hre.txt:295 |

### メンバーの特別地位（special_statuses）

| 地位 | 日本語名 | 条件 | src |
|---|---|---|---|
| `emperor` | 皇帝 | 選挙で選出 | hre.txt:659, loc |
| `elector` | 公・選帝侯 | 君主制 HRE メンバー、最大数制限あり | hre.txt:660, loc |
| `archbishop_elector` | 大司教・選帝侯 | 神権政治 HRE メンバー、最大数制限あり | hre.txt:661, loc |
| `free_city` | 帝国自由都市 | 小規模都市国家、皇帝の保護下 | hre.txt:662, loc |
| `primas_germaniae` | （ドイツ首席大司教） | 専用 | hre.txt:663 |
| `legatus_natus` | （教皇特使） | 専用 | hre.txt:664 |
| `imperial_prelate` | 帝国司教国 | 神権政治で archbishop_elector でないメンバー | hre.txt:665, loc |
| `imperial_prince` | 帝国諸侯 | 上記以外の HRE メンバー | hre.txt:666, loc |
| `imperial_peasant_republic` | 帝国農民共和国 | 農民共和国政府改革を持つメンバー | hre.txt:667, loc |

### 選帝侯数の上限（初期値）

| 種別 | 最大数 | src |
|---|---|---|
| 公・選帝侯（elector） | 4 | hre.txt:133 |
| 大司教・選帝侯（archbishop_elector） | 3 | hre.txt:134 |

---

## 5. 皇帝アクション（外交インタラクション）

帝国の権威UIに表示される皇帝固有アクション（`HRE_EMPEROR_ACTIONS_LIST` より）。

| アクション（英語） | 日本語名 | 概要 | src |
|---|---|---|---|
| `enforce_landfriede` | ラント平和令を強制 | 諸侯間戦争を中止させる | country_interactions_l_japanese.yml:245 |
| `enforce_religious_unity` | 宗教統一の強制 | 諸侯に帝国宗教への改宗を求める | country_interactions_l_japanese.yml:292 |
| `demand_unlawful_territory` | 不法領土を要求 | 非メンバーが保有する HRE 領土の返還要求 | country_interactions_l_japanese.yml:303 |
| `ask_to_vote_for_me_as_emperor` | 選挙での支持を要求する | 選帝侯に自国への投票を求める | country_interactions_l_japanese.yml:108 |
| `bolster_imperial_army` | 帝国軍を強化 | 諸侯に皇帝の戦争への参戦を要請 | country_interactions_l_japanese.yml:314 |
| `cb_imperial_ban`（CB） | 帝国の禁令 | 法律侵犯者に対する宣戦布告 CB | casus_belli_l_japanese.yml |

---

## 6. 帝国法（Laws）一覧

帝国法は「金印勅書」成立後に解放される。各法は左（諸侯有利）〜右（皇帝有利）の5段階ポリシーを持つ。

### 6.1 金印勅書（golden_bull）

| 項目 | 内容 | src |
|---|---|---|
| 日本語名 | 金印勅書 | laws_and_policies_l_japanese.yml |
| カテゴリ | - | 20_hre.txt:22 |
| 概要 | HRE 憲法の根幹。これを制定することで他の帝国法が解放される | 20_hre.txt:22-119 |
| 制定コスト | `imperial_authority_golden_bull`（定数） | 20_hre.txt:26 |
| 効果（制定時） | 全帝国法を有効化、`monthly_imperial_authority` 軽微ボーナス | 20_hre.txt:57, 67 |
| 追記 | 一度制定すると取消不可（locked） | 20_hre.txt:28-34 |

### 6.2 帝国税法（monetary_contribution）

| ポリシー（英語） | 日本語名 | レベル | 主な効果 | src |
|---|---|---|---|---|
| `no_monetary_contribution` | 無課税 | 1（諸侯有利） | 皇帝に cabinet_efficiency +5% | 20_hre.txt:134 |
| `only_treasury_payment` | — | 2 | 帝国国庫貢献を解放、非皇帝に毎月威信↑ | 20_hre.txt:175 |
| `only_emperor_payment` | — | 2（別ルート） | 皇帝への直接貢物を解放 | 20_hre.txt:234 |
| `complete_imperial_contribution` | — | 3（皇帝有利） | 国庫・皇帝貢物の両方を解放、`hre_emperor_comfort_policies_counter +1` | 20_hre.txt:286 |

### 6.3 帝国登録簿（military_contribution）

| ポリシー（英語） | 日本語名 | レベル | src |
|---|---|---|---|
| `no_military_contribution` | 軍役免除 | 1 | 20_hre.txt:348 |
| `manpower_from_cities` | — | 2 | 20_hre.txt:386 |
| `manpower_from_electors` | — | 3 | 20_hre.txt:465 |
| `manpower_from_princes` | — | 4 | 20_hre.txt:525 |
| `great_imperial_army` | — | 5（皇帝有利） | 帝国軍に大規模マンパワー供出 | 20_hre.txt:573 |

### 6.4 帝国の宗教（imperial_religion）

帝国宗教を変更するポリシー。

| ポリシー（英語） | 日本語名 | 効果 | src |
|---|---|---|---|
| `hre_religion_catholic` | 帝国の宗教：カトリック | 帝国宗教をカトリックに設定 | 20_hre.txt:637 |
| `hre_religion_lutheran` | 帝国の宗教：ルター派 | 帝国宗教をルター派に設定 | 20_hre.txt:651 |
| `hre_religion_hussite` | 帝国の宗教：フス派 | 帝国宗教をフス派に設定 | 20_hre.txt:665 |
| `hre_religion_calvinist` | 帝国の宗教：カルヴァン派 | 帝国宗教をカルヴァン派に設定 | 20_hre.txt:679 |
| `hre_religion_christian` | 帝国の宗教：キリスト教 | 帝国宗教をキリスト教グループ全体に設定 | 20_hre.txt:699 |

### 6.5 選帝侯の宗教に関する法律（electorate_religion_law）

| ポリシー（英語） | 日本語名 | src |
|---|---|---|
| `only_imperial_religion_policy` | 帝国の宗教のみ | 20_hre.txt |
| `only_imperial_religion_group_policy` | 帝国の宗教グループのみ | 20_hre.txt |

### 6.6 皇位継承（imperial_succession_law）

金印勅書後に解放。

| ポリシー（英語） | 日本語名 | 主な効果 | src |
|---|---|---|---|
| `hre_agnatic_succession_policy` | 男系子孫による継承 | 男性君主のみ帝位継承可 | 20_hre.txt:768 |
| `hre_pragmatic_sanction_policy` | 国事詔書 | `hre_allow_female_emperors = yes`（女性皇帝を許可） | 20_hre.txt:805 |

### 6.7 皇帝の選挙（imperial_voting_law）

皇帝選出プロセスを規定する最重要法のひとつ。

| ポリシー（英語） | 日本語名 | レベル | 主な効果 | src |
|---|---|---|---|---|
| `rotating_emperorship_policy` | 輪番制皇帝 | 1 | 現職再選を抑制、`allow_self_vote = no`、IA −0.025/月（皇帝） | 20_hre.txt:880 |
| `free_electorate_policy` | 選帝侯の自由投票 | 2 | `allow_self_vote = yes` | 20_hre.txt:936 |
| `emperor_dynastic_preference_policy` | 皇帝王朝優先 | 3 | 同一王朝に `reasons_to_elect +50`、皇帝 IA +mild | 20_hre.txt:983 |
| `emperor_successor_preference_policy` | 皇帝の後継者優先 | 4 | 皇帝に `reasons_to_elect +50`、IA +mild、`hre_emperor_comfort_policies_counter +1` | 20_hre.txt:1045 |
| `erbkaisertum_policy` | 帝位の世襲 | 5（皇帝有利） | 選挙廃止（`leader_change_method = none`）、世襲制へ移行、`hre_emperor_comfort_policies_counter +1`。選帝侯法・宗教法をロック | 20_hre.txt:1104 |

### 6.8 選挙組織（electorate_organization_law）

選帝侯数と皇帝の選挙権を規定。

| ポリシー（英語） | 日本語名 | レベル | 主な効果 | src |
|---|---|---|---|---|
| `elector_council_policy` | 選帝侯評議会 | 1（諸侯有利） | 選帝侯+3/大司教選帝侯+3、皇帝を選帝侯から除外、議会で帝位剥奪が可能に、IA −very_strong/月 | 20_hre.txt:1180 |
| `expanded_electors_policy` | 選帝侯の拡大 | 2 | 選帝侯+1/大司教選帝侯+1、皇帝を選帝侯から除外 | 20_hre.txt:1238 |
| `electorate_policy` | 有権者 | 3（中立） | デフォルト、変更なし | 20_hre.txt:1292 |
| `limited_electors_policy` | 限定的な選帝侯 | 4 | 選帝侯−1/大司教選帝侯−1、皇帝が選帝侯剥奪権を取得 | 20_hre.txt:1329 |
| `integrated_electors_policy` | 選帝侯を統合 | 5（皇帝有利） | 選帝侯−2/大司教選帝侯−2、皇帝が選帝侯になる（`is_hre_elector = yes`）、`hre_emperor_comfort_policies_counter +1` | 20_hre.txt:1393 |

### 6.9 自由都市（free_city_law）

| ポリシー（英語） | 主な効果 | src |
|---|---|---|
| `no_free_cities_policy` | 自由都市制度を廃止 | 20_hre.txt:1502 |
| （保護なし） | 自由都市保護を無効化 | 20_hre.txt:1562 |
| `free_cities_policy` | 自由都市を標準保護 | 20_hre.txt:1612 |
| （臣下化） | 自由都市を帝国直轄臣下に | 20_hre.txt:1694 |
| （直接臣下化） | 自由都市を直接臣下に（hre.104-107） | 20_hre.txt:1803 |

### 6.10 自由都市の特権（free_city_rights_law）

| src |
|---|
| 20_hre.txt:1904 |

### 6.11 ラント平和令（landfriede_law）

| ポリシー（英語） | 日本語名 | レベル | 主な効果 | src |
|---|---|---|---|---|
| `no_landfriede_policy` | ラント平和令を不採用 | 1 | 全メンバーに安定度コスト +0.025 | 20_hre.txt:2035 |
| `landfriede_policy` | ラント平和令を制定 | 2 | 皇帝に `allow_landfriede = yes`、全メンバーに安定度コスト −0.025 | 20_hre.txt:2087 |
| `landfriede_rank_2_policy` | ラント平和令を拡大 | 3 | 平和令コスト −2、クールダウン −1、安定度コスト −0.05、「内部平和要求」議会案件を解放 | 20_hre.txt:2156 |
| `landfriede_rank_3_policy` | ラント平和令を強化 | 4 | さらに強化 | 20_hre.txt:2157 |
| `landfriede_rank_4_policy` | 永久平和令 | 5（皇帝有利） | メンバー間戦争を恒久禁止 | 20_hre.txt（上位） |

### 6.12 帝国議会（imperial_diet_law）

| ポリシー（英語） | 日本語名 | 議会タイプ | 主な効果 | src |
|---|---|---|---|---|
| `no_imperial_diet_policy` | （なし） | — | 議会なし | 20_hre.txt:2484 |
| `hre_early_imperial_diet_policy` | — | `hre_early_imperial_diet`（初期帝国議会） | IA +weak/月（皇帝）、公・大司教・諸侯のみ投票 | 20_hre.txt:2531 |
| `hre_bi_camerial_imperial_diet_policy` | — | `hre_bi_camerial_imperial_diet`（二院制帝国議会） | IA +mild/月（皇帝）、聖職者も投票権 | 20_hre.txt:2585 |
| `hre_tri_camerial_imperial_diet_policy` | — | `hre_tri_camerial_imperial_diet`（三院制帝国議会） | IA +medium/月（皇帝）、自由都市にも投票権 | 20_hre.txt:2652 |

### 6.13 常設帝国議会（perpetual_diet_law）

| ポリシー（英語） | 日本語名 | 条件 | 主な効果 | src |
|---|---|---|---|---|
| `perpetual_diet_policy` | 常設帝国議会 | 二院制または三院制帝国議会が必要 | 議会本拠地に `local_monthly_development_modifier +0.1`、`local_monthly_prosperity +0.01`、「常設議会の設立」議会案件を解放 | 20_hre.txt:2759 |

### 6.14 皇帝の権力（power_of_the_emperor_law）— 集権化の核心

**注意:** このポリシーはデフォルトで `improved_imperial_authority_policy`（レベル3）から開始する（他の法律と異なる）。

| ポリシー（英語） | 日本語名 | レベル | 主な効果 | src |
|---|---|---|---|---|
| `holy_roman_figurehead_policy` | 神聖ローマの傀儡 | 1（諸侯有利） | IA −very_strong/月、議会で帝位剥奪が可能に | 20_hre.txt:2830 |
| `kaisertum_policy` | 帝政 | 2 | 帝国禁令（`imperial_ban_allowed = yes`）を解放 | 20_hre.txt:2885 |
| `improved_imperial_authority_policy` | 帝国の権威の改善 | 3（初期） | 帝国禁令+議会拒否権（`allow_overrule_imperial_diet`）を解放、外交評判 +weak、IA +mild/月。要件: emperor_comfort 2個以上 | 20_hre.txt:2931 |
| `revoke_privilegia_policy` | 特権を剥奪 | 4 | 帝国禁令+議会拒否権、外交評判 +weak、IA +very_strong/月、威信 +0.1/月、全 HRE 領土に制度成長 +10%。要件: emperor_comfort 5個以上、hre.100 イベント発火 | 20_hre.txt:2988 |
| `renovatio_policy` | 帝国の復活 | 5（最終） | 全メンバーに安定度コスト −0.2、皇帝に威信 +0.2/月・外交評判 +mild、強制内部平和（`enforced_internal_peace`）。hre.102 イベント（帝国統一オプション）発火。要件: emperor_comfort 5個以上 | 20_hre.txt:3068 |

---

## 7. 集権化の進め方（皇帝路線ロードマップ）

`hre_emperor_comfort_policies_counter` を積み上げることで `improved_imperial_authority_policy` と `renovatio_policy` の解放条件を満たす。

| ステップ | 法律 / ポリシー | +comfort_counter | 累積 |
|---|---|---|---|
| 1 | `complete_imperial_contribution` | +1 | 1 |
| 2 | `emperor_successor_preference_policy` または `erbkaisertum_policy` | +1 | 2 |
| → | **improved_imperial_authority_policy が解放**（要件2） | — | — |
| 3 | `integrated_electors_policy` | +1 | 3 |
| 4 | さらに他の comfort 改革 | +1〜+2 | 4〜5 |
| → | **revoke_privilegia / renovatio が解放**（要件5） | — | — |

---

## 8. HRE イベント一覧

### 皇帝権力強化系

| イベント ID | 名称（概要） | トリガー | 主な効果 | src |
|---|---|---|---|---|
| hre.100 | 特権剥奪の宣言（皇帝側） | `revoke_privilegia_policy` 制定時 | 威信 +ultimate、全メンバーに hre.101 送信 | events/hre.txt:4 |
| hre.101 | 特権剥奪の通知（諸侯側） | hre.100 から送信 | 選択肢A: 帝国宗教に忠誠（`united_empire` opinion +）/ 選択肢B: HRE 離脱 | events/hre.txt:42 |
| hre.102 | 帝国の復活（皇帝側） | `renovatio_policy` 制定時 | 帝国統一（HRE 消滅・全メンバーを外交併合） | events/hre.txt:108 |
| hre.103 | 帝国の復活（諸侯側） | hre.102 から送信 | 帝国に外交的に併合される | events/hre.txt:172 |

### 帝国自由都市系

| イベント ID | 名称（概要） | src |
|---|---|---|
| hre.104 | 自由都市を臣下化（皇帝宣言） | events/hre.txt:195 |
| hre.105 | 自由都市が臣下化される | events/hre.txt:243 |
| hre.106 | 自由都市を直接臣下化（皇帝宣言） | events/hre.txt:269 |
| hre.107 | 自由都市が直接臣下化される | events/hre.txt:320 |

### 定期・通知系

| イベント ID | 名称（概要） | src |
|---|---|---|
| hre.6 | 常設帝国議会の設置（開催地） | events/hre.txt:1009 |
| hre.7 | 常設帝国議会の通知（諸侯） | events/hre.txt:1039 |
| hre.15 | 神聖ローマ帝国の解体 | events/hre.txt:1059 |

### 帝国の権威変動通知（On Action）

| イベント ID | 名称（概要） | IA 変動 | src |
|---|---|---|---|
| hre.800 | 皇帝が帝国宝物を新首都へ移送 | — | events/hre.txt:347 |
| hre.801 | 皇帝崩御の通知（諸侯） | — | events/hre.txt:395 |
| hre.900 | 同一王朝から新皇帝（連続性） | +weak | events/hre.txt:421 |
| hre.901 | 諸侯を解放（皇帝が臣下国を独立させた） | +（人口比で変動、上限+20） | events/hre.txt:464 |
| hre.902 | 諸侯が帝国宗教外に改宗 | −（人口比で変動、上限−20） | events/hre.txt:524 |
| hre.903 | 諸侯が帝国宗教に改宗 | +（人口比で変動、上限+20） | events/hre.txt:588 |
| hre.904 | 皇帝が帝国防衛戦争に勝利 | +(敵/自比率) × 5（上限+10） | events/hre.txt:664 |
| hre.905 | HRE メンバーが非HRE国に併合される | −（敵人口/200）× 10（上限−20） | events/hre.txt:726 |
| hre.907 | HRE メンバーが非HRE従属から解放される | +（人口比で変動、上限+20） | events/hre.txt:778 |
| hre.908 | 皇帝が HRE メンバーの防衛に参戦 | +（自人口/攻撃国人口）× 5（上限+10） | events/hre.txt:850 |
| hre.909 | 皇帝が HRE メンバー防衛に不参加 | `imperial_authority_strong_penalty` | events/hre.txt:897 |
| hre.950 | HRE メンバーが HRE 領土を奪還 | +（人口比、上限+1）、威信ボーナス、領土統合 | events/hre.txt:922 |

---

## 9. 帝国宝物（Imperial Works of Art）

皇帝の首都に保管される帝国宝物。首都移転時に hre.800 で自動移動。

| 宝物（英語） | src |
|---|---|
| `imperial_crown_hre` | events/hre.txt:369 |
| `imperial_orb_hre` | events/hre.txt:373 |
| `saint_stephans_purse` | events/hre.txt:377 |
| `coronation_gospel_hre` | events/hre.txt:381 |

---

## 10. 選帝侯メカニクス詳細

### 選出プロセス

- 皇帝は選帝侯（elector / archbishop_elector）の投票で選出（決議: `hre_election`）
- `leader_change_trigger_type = rulerchange`：君主交代時に選挙が発生
- デッドロック時（全票がロックされ過半数未達で2年以上）：最強の HRE メンバーを自動的に皇帝に任命
- `erbkaisertum_policy` 制定後は `leader_change_method = none`（選挙廃止・世襲制）

### 選帝侯の得票傾向（AI bias）

| 要因 | 影響 | src |
|---|---|---|
| 皇帝への opinion | 高いと皇帝を支持しやすい | hre.txt:56-67（hre.101の判定） |
| 同一王朝（emperor_dynastic_preference_policy） | `reasons_to_elect +50` | 20_hre.txt:1007 |
| 皇帝後継者優先（emperor_successor_preference_policy） | 皇帝に `reasons_to_elect +50` | 20_hre.txt:1065 |
| ドイツ宮廷言語（HRE_ELECTION_GERMAN_COURT_LANGUAGE） | ボーナス | loc |
| 大国（dominant nation、人口100万超） | penalties | loc |

### 選帝侯の独立性条件

`elector` 地位は `government_type = monarchy` かつ非臣下の HRE メンバーのみ保持可（臣下選帝侯は IA にペナルティ）。

---

## 11. 議会タイプ（Parliament Types）

| タイプ（英語） | 日本語名 | 主な特徴 | src |
|---|---|---|---|
| `hre_court_assembly` | 宮廷議会 | 初期設定。皇帝・選帝侯の議決権が大幅増大、自由都市等の影響力が著しく低下 | hre.txt:15, loc |
| `hre_early_imperial_diet` | 初期帝国議会 | 公・大司教・諸侯のみ参加、自由都市は排除 | 20_hre.txt:2542, loc |
| `hre_bi_camerial_imperial_diet` | 二院制帝国議会 | 聖職者にも投票権、自由都市はまだ排除 | 20_hre.txt:2595, loc |
| `hre_tri_camerial_imperial_diet` | 三院制帝国議会 | 自由都市にも投票権（最も包括的） | 20_hre.txt:2662, loc |
