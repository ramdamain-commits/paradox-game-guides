# EU5 カスティーリャ プレイ中チェックリスト
> 対象パッチ: 1.4「Río Salado」正式版（ビルド 26211608）＋ DLC「Across the Pillars」 ／ 最終確認日: 2026-10-30

1.4 の主要国カスティーリャで、1337年から局面「海峡をめぐる戦い」と「黄金世紀」を勝ち抜くための固有の手順。財政・研究・内閣など、どの国でも同じことは [共通チェックリスト](checklist.html?file=eu5/eu5-play-checklist.md) で行う。2つの局面・宝船の遠征・グラナダとサンタ・エルマンダーの決断は DLC が必要。「（公式の説明）」の意味は共通チェックリストと同じ。

## 1. 開始直後（ポーズ中にやること）

- [ ] 局面「海峡をめぐる戦い」を開き、「グラナダへの影響力」の値と毎月の増減の内訳を確認する {#cas-start-situation}
  - なぜ: 影響力は−100〜100で、マイナスがカスティーリャ寄り、開始値は−33。発見の時代に入ると、勝者なしで終わる [src: battle_for_the_strait.txt, influence_over_granada] [src: battle_for_the_strait.txt, battle_for_the_strait_neutral_outcome] [src: d009_situations_l_japanese.yml, castilian_influence_over_granada]
- [ ] 影響力を貯める間は、グラナダとの朝貢関係を保つ（グラナダ側からも解消できるので、関係が残っているか時々確かめる） {#cas-start-tributary}
  - なぜ: グラナダは開始時からカスティーリャの朝貢国。従属国である間は影響力が毎月0.30寄り、従属の年数に応じてさらに寄る [src: 12_diplomacy.txt:244] [src: battle_for_the_strait.txt, BFTS_INFLUENCE_GRA_SUBJECT_OF_CAS] [src: battle_for_the_strait.txt, BFTS_YEARS_SUBJECT_UNDER_CAS] [src: default_values.txt, bfts_influence_gain_mid] [src: tributary.txt, subject_can_cancel]
- [ ] グラナダの自国への評価が50以上なら、独立保障を結ぶ {#cas-start-ally}
  - なぜ: 保障で影響力が毎月0.05寄る。自国のランクが相手以上で、税基盤と陸軍の規模が相手より大きいことも条件。同盟は従属国とは結べない [src: battle_for_the_strait.txt, BFTS_INFLUENCE_GRA_GUARANTEED_BY_CAS] [src: guarantee.txt:25-48] [src: country_triggers.txt, alliance_can_exist]
- [ ] 伝統の時代の進歩では、「封建制」の次に固有の「城塞の地」を研究する {#cas-start-adv}
  - なぜ: 陸軍士気+15%と要塞の維持効率+20%。モロッコ・グラナダとの戦争の前に取る [src: country_cas.txt, cas_a_land_of_castles]

## 2. 序盤：海峡をめぐる戦い（1337〜1437）

### モロッコをイベリアから追い出す

到達目標: モロッコのイベリア側の領土をなくす。

- [ ] 共通チェックリストの戦争準備を済ませ、モロッコのイベリア側（アルヘシラス・ジブラルタル・マルベーリャ・ロンダ）を取る戦争をする {#cas-war-morocco}
  - なぜ: 勝利条件の1つが、モロッコがイベリア地方に領土も従属国も持たないこと。モロッコは開始時にこの4ロケーションを持つ [src: situation_triggers.txt, battle_for_the_strait_castile_holds_the_strait] [src: 10_countries.txt, MOR]
- [ ] モロッコが別の戦争で劣勢な時期を狙う {#cas-war-timing}
  - なぜ: モロッコがグラナダと交戦しておらず、戦勝点−10未満の戦争を抱えている間は、影響力が毎月0.15寄る [src: battle_for_the_strait.txt, BFTS_INFLUENCE_MOR_LOSING_WAR]
- [ ] 戦後、マラガ・カディス・アルメリア・グラナダの州と、アンダルシア・グラナダ・ムルシアの3地域のうち、全域を持てていないものを埋める {#cas-war-provinces}
  - なぜ: 州を全域持つごとに毎月0.02、地域なら0.05、影響力が寄る。北アフリカ側の州も数える [src: battle_for_the_strait.txt, BFTS_INFLUENCE_CAS_PROV_MALAGA] [src: battle_for_the_strait.txt, BFTS_INFLUENCE_CAS_AREA_ANDALUSIA] [src: battle_for_the_strait.txt, BFTS_INFLUENCE_CAS_AREA_MURCIA] [src: battle_for_the_strait.txt, BFTS_INFLUENCE_CAS_PROV_HABAT]

### グラナダへの影響力を貯めて決着させる

到達目標: 発見の時代の前に、グラナダの問題を片づける。

- [ ] 陸軍を増強し、グラナダとの軍事力の差を広げる {#cas-granada-army}
  - なぜ: グラナダが軍事力で劣るほど影響力が寄る（最大で毎月0.2） [src: battle_for_the_strait.txt, BFTS_INFLUENCE_GRA_MILITARY_WEAKNESS_VS_CAS]
- [ ] 影響力が−100に達したら、決断「グラナダの信仰をめぐる決断」で「改宗させる」を選ぶか決める {#cas-granada-convert}
  - なぜ: グラナダの宗教が自国と違い、両国とも平時なら実行できる。改宗させると同じ宗教として毎月0.05寄り、自国の「グラナダのヒネーテ」が「イベリア軽騎兵」に変わる。グラナダが従属国なら独立欲求が大きく上がる。勝利に必須ではない [src: cas_decisions.txt, demand_conversion_of_granada] [src: battle_for_the_strait.txt, BFTS_INFLUENCE_GRA_SHARED_RELIGION_WITH_CAS]
- [ ] モロッコをイベリアから追い出したら、「従属国の管理」パネルで朝貢関係を解消し、グラナダ地域を征服してグラナダを滅ぼす {#cas-granada-finish}
  - なぜ: 勝利には、グラナダ地域を自国か従属国で持つことに加え、「影響力−99未満かつグラナダが属国」か「グラナダが存在しない」のどちらかが要る。朝貢国は併合できない。属国にする道は7章 [src: situation_triggers.txt, battle_for_the_strait_castile_requirements_met] [src: tributary.txt, can_be_annexed] [src: tributary.txt, overlord_can_cancel]
- [ ] 制度「律法主義」を受容したら、政府改革「カスティーリャ王国」を選ぶ {#cas-reform-crown}
  - なぜ: ポリシーの変更コスト−25%、人的資源+10%、毎月の正統性+0.05。海峡で勝つと、聖職者の目標満足度と交易収入+5%も付く [src: country_specific.txt, crown_castile_reform] [src: d009_country_specific.txt, crown_castile_reform]

## 3. 中盤：発見〜宗教改革（1437〜1637）

### 統治の固め

- [ ] 発見の時代に入ったら、平時に決断「カスティーリャ王立評議会の創設」を実行し、政府改革「カスティーリャ王立評議会」を選ぶ {#cas-council}
  - なぜ: 税収効率が上がり、貴族の権力が−20%、中央集権へ寄る。DLC では官僚機構のスロットも+1 [src: spanish_councils_decisions.txt, spa_establish_the_council_of_castile_decision] [src: country_specific.txt, royal_council_of_castile] [src: d009_country_specific.txt, royal_council_of_castile]
- [ ] ルネサンスの時代に「ルネサンスの宮廷」の次の「市議会同盟」を研究しておき、発見の時代に決断「サンタ・エルマンダーの設立」で政府改革「サンタ・エルマンダー」を解禁して選ぶ {#cas-hermandad}
  - なぜ: 反乱の増加を抑え、安定度のコスト効率+10%、安定度の減衰を抑える [src: country_cas.txt, cas_santa_hermandad] [src: cas_decisions.txt, cas_found_the_santa_hermandad_decision] [src: d009_country_specific.txt, cas_santa_hermandad_reform]

### 黄金世紀の準備

到達目標: 決断「黄金世紀の幕開け」の条件をそろえる（海峡で勝っていることが前提）。

- [ ] アラゴン・ポルトガルなど、イベリア文化でキリスト教の国と王室婚姻を結び、同君連合をつくる {#cas-union}
  - なぜ: 同君連合の加盟国にイベリア文化でキリスト教の国が2か国以上いると、自動でイベリア連合になる。DLC では「イベリア婚姻協定」で結ばれた2国の王位継承が連動し、同君連合ができうる（公式の説明） [src: international_organization_triggers.txt, union_flavor_is_spain] [src: union.txt, on_creation] [src: game_concepts_l_japanese.yml, game_concept_union_desc] [src: iberian_wedding_pact.txt, iberian_wedding_pact]
- [ ] イベリア連合の同君上位国の地位を保ち、統合レベルを3以上にする {#cas-union-level}
  - なぜ: カスティーリャのまま黄金世紀を始めるには、統合レベル3以上のイベリア連合の同君上位国であることが必要（スペインになっていれば不要） [src: d009_golden_century_decisions.txt, gc_decision] [src: d009_golden_century_l_japanese.yml, gc_decision_iberian_union_leader_tt]
- [ ] スペインになるなら、統合レベル5以上・イベリア地方の半分以上を加盟国が保有した状態で「スペイン王国の宣言」を行う {#cas-spain}
  - なぜ: 同君上位国だけが実行でき、局面「海峡をめぐる戦い」の進行中はできない [src: iberian_union.txt, proclaim_spanish_monarchy]
- [ ] グラナダ・アンダルシア・ムルシアの3地域を、自国か従属国ですべて持つ {#cas-gc-areas}
  - なぜ: 黄金世紀を始める条件 [src: d009_golden_century_decisions.txt, gc_decision]
- [ ] 条件がそろったら、平時・破産していない状態で決断「黄金世紀の幕開け」を実行する {#cas-gc-start}
  - なぜ: 局面「黄金世紀」はこの決断でしか始まらない [src: d009_golden_century_decisions.txt, gc_decision] [src: d009_golden_century_l_japanese.yml, can_only_be_activated_via_decision_tt]

### 新大陸

- [ ] 進歩「植民地憲章」を研究し、キューバ島と、メソアメリカかコロンビアの大西洋岸に港を持つ {#cas-colonies}
  - なぜ: 宝船の遠征の前提。メソアメリカは「フロタ・デ・ヌエバ・エスパーニャ」、コロンビアは「ガレオネス・デ・ティエラ・フィルメ」 [src: d009_gold_fleet_nueva_espana.txt, gold_fleet_nueva_espana_expedition] [src: d009_gold_fleet_tierra_firme.txt, gold_fleet_tierra_firme_expedition]
- [ ] 「遠征が可能」のアラートが出たら、宝船の遠征を出す {#cas-treasure-fleet}
  - なぜ: 出発には費用と、農村でない港、ヨーロッパにある中核の港などが要る。黄金世紀の間は宝船が植民地支配度を上げる（公式の説明） [src: d009_gold_fleet_nueva_espana.txt, can_start] [src: gold_fleet.txt, gold_fleet_departure_cost] [src: alerts_l_japanese.yml, ALERT_POSSIBLE_EXPEDITION_TITLE] [src: d009_golden_century_l_japanese.yml, gc_colonial_dominance_desc]

## 4. 終盤：黄金世紀の100年

到達目標: 100年間、領土を大きく減らさずに乗り切る。

- [ ] 領土（ロケーション数）を、黄金世紀が始まったときの75%より多く保つ {#cas-gc-keep}
  - なぜ: 平時に75%以下になると「縮小する巨像」で終わり、安定度に深刻な打撃を受ける [src: golden_century.txt, golden_century_colossus_diminished] [src: golden_century.txt, golden_century_min_locations] [src: d009_golden_century_l_japanese.yml, golden_century_colossus_diminished_desc]
- [ ] 大同盟が結成されたら、同盟国と陸軍を整え、大同盟の加盟国の動きを見張る {#cas-gc-alliance}
  - なぜ: 大同盟は自国を標的とする列強の同盟。ヨーロッパ支配度か植民地支配度が75以上だと、加盟国が自国に宣戦できる。数値は7章 [src: d009_grand_alliance.txt, can_declare_war] [src: d009_golden_century_l_japanese.yml, grand_alliance_desc]
- [ ] 「発火点の進行度」が100に近づいたら、インフレと借入を抑え、大きな戦争を始めない {#cas-gc-flashpoint}
  - なぜ: 進行度は毎月、基礎値に王室の権力・安定度・列強スコア・借入の数・インフレが加わって上がり、係数はインフレが最も大きい。100に達すると発火点が起き、大きな飛躍にも激震にもなりうる（公式の説明） [src: golden_century.txt, gc_flashpoint_meter] [src: golden_century_values.txt, gc_flashpoint_inflation_factor] [src: d009_golden_century_l_japanese.yml, gc_flashpoint_meter_desc]
- [ ] 100年経ったら、結果「巨像は耐え抜く」で得た補正を確認する {#cas-gc-end}
  - なぜ: 開始から100年で勝ちになり、どこまで支配を広げたかに応じて補正が付く（公式の説明） [src: golden_century.txt, golden_century_colossus_endures] [src: d009_golden_century_l_japanese.yml, golden_century_colossus_endures_desc]

## 5. 定期ルーチン {.routine}

### 毎年（海峡をめぐる戦いの間）

- [ ] 局面「海峡をめぐる戦い」で、影響力の毎月の変化がマイナス（カスティーリャ寄り）か確認する {#cas-yearly-influence}
  - なぜ: 影響力は毎月、今の値の0.65%ずつ0へ戻るほか、グラナダが独立していることや自国より大きくなることでも戻される。−100を保つには毎月0.65より多く寄せ続ける必要がある [src: battle_for_the_strait.txt, BFTS_INFLUENCE_AXIS_DECAY] [src: battle_for_the_strait.txt, influence_over_granada]
- [ ] モロッコがイベリア地方に領土や従属国を持っていないか確認する {#cas-yearly-morocco}
  - なぜ: 取り返されると海峡の確保の条件を失う [src: situation_triggers.txt, battle_for_the_strait_castile_holds_the_strait]

### 毎年（黄金世紀の間）

- [ ] 局面「黄金世紀」で、ヨーロッパ支配度・植民地支配度・発火点の進行度と、ロケーション数を確認する {#cas-yearly-gc}
  - なぜ: 支配度が大同盟の宣戦の条件を、ロケーション数が「縮小する巨像」の線を決める [src: d009_grand_alliance.txt, can_declare_war] [src: golden_century.txt, golden_century_min_locations]

## 6. 困ったとき

**影響力が−100まで届かない**
- 見る場所: 局面「海峡をめぐる戦い」の、影響力の毎月の増減の内訳 [src: battle_for_the_strait.txt, influence_over_granada]
- 打ち手: 保障、州と地域の全域保有、陸軍の増強を重ねる。グラナダの自国への評価も少し効く（評価100で毎月0.025） [src: battle_for_the_strait.txt, BFTS_INFLUENCE_GRA_OPINION_OF_CAS]

**発見の時代が近いのに決着がつかない**
- 見る場所: 局面の勝利条件の一覧 [src: situation_triggers.txt, battle_for_the_strait_castile_requirements_met]
- 打ち手: 影響力を待たず、朝貢関係を解消してグラナダを征服する。発見の時代に入ると勝者なしで終わり、黄金世紀に進めない [src: battle_for_the_strait.txt, battle_for_the_strait_neutral_outcome]

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|
| 影響力が寄る量（毎月） | 従属国0.30／モロッコの劣勢0.15／保障0.05／同じ宗教0.05／軍事力の差 最大0.2／州0.02・地域0.05（全域保有ごと）。同盟の0.15は従属国の間は使えない | [src: default_values.txt, bfts_influence_gain_mid] [src: battle_for_the_strait.txt, influence_over_granada] |
| 影響力が0へ戻る量（毎月） | 今の値の0.65%（−100なら0.65）。ほかにグラナダの独立や領土・国力でも戻る | [src: battle_for_the_strait.txt, BFTS_INFLUENCE_AXIS_DECAY] |
| 海峡の決着の期限 | 発見の時代の開始（1437年） | [src: battle_for_the_strait.txt, battle_for_the_strait_neutral_outcome] [src: age/00_default.txt, age_3_discovery] |
| グラナダを属国にして勝つ道 | 勝利条件に「影響力−99未満かつグラナダが属国」がある。朝貢国を属国に変える手段は、スクリプトでは確かめられなかった | [src: situation_triggers.txt, battle_for_the_strait_castile_requirements_met] |
| 黄金世紀の開始条件 | 海峡で勝った国・発見の時代以降・従属国でない・平時・破産していない・スペインか統合レベル3以上のイベリア連合の同君上位国・グラナダ／アンダルシア／ムルシアの3地域を自国か従属国で保有 | [src: d009_golden_century_decisions.txt, gc_decision] |
| 縮小する巨像 | 平時にロケーション数が開始時の75%以下 | [src: golden_century.txt, golden_century_min_locations] |
| 発火点の進行度の上がり方（毎月） | 基礎0.35＋王室の権力×0.2＋安定度×0.0025＋列強スコア×0.001＋借入の数×0.025＋インフレ×1.0 | [src: golden_century_values.txt, gc_flashpoint_base] [src: golden_century.txt, gc_flashpoint_meter] |
| 大同盟が宣戦できる条件 | ヨーロッパ支配度か植民地支配度が75以上（ツールチップの表記は25だが、スクリプトの値は75）。ヨーロッパ支配度25以上で大同盟に防衛力+10%などの補正 | [src: d009_grand_alliance.txt, can_declare_war] [src: d009_golden_century_l_japanese.yml, ga_dominance_threshold_tt] |
| スペイン王国の宣言 | イベリア連合の統合レベル5以上・イベリア地方の半分以上を加盟国が保有・海峡の局面が終わっている | [src: iberian_union.txt, proclaim_spanish_monarchy] |

## 8. 用語

完全版は [用語対照表](viewer.html?file=eu5/localization-reference.md)。

- 局面（Situation）／海峡をめぐる戦い（Battle for the Strait）／グラナダへの影響力（Influence over Granada）／黄金世紀（Golden Century）／黄金世紀の幕開け（Usher in the Golden Century）／発火点（Flashpoint）／発火点の進行度（Flashpoint Progress）／大同盟（The Grand Alliance）／ヨーロッパ支配度（European Dominance）／植民地支配度（Colonial Dominance）／巨像は耐え抜く（The Colossus Endures）／縮小する巨像（The Colossus Diminished）
- 朝貢国（Tributary）／属国（Vassal）／独立保障（Guarantee）／同君連合（Union）／イベリア連合（Iberian Union）／イベリア婚姻協定（Iberian Wedding Pact）／同君上位国（Senior Partner）／統合レベル（Integration Level）／スペイン王国の宣言（Proclaim the Spanish Monarchy）
- カスティーリャ王国（Crown of Castile）／カスティーリャ王立評議会（Royal Council of Castile）／サンタ・エルマンダー（Santa Hermandad）／城塞の地（A Land of Castles）／市議会同盟（Hermandades Concejiles。進歩名）／封建制（Feudalism）／ルネサンスの宮廷（Renaissance Court）／律法主義（Legalism）／植民地憲章（Colonial Charters）
- 遠征（Expedition）／フロタ・デ・ヌエバ・エスパーニャ（Flota de Nueva España）／ガレオネス・デ・ティエラ・フィルメ（Galeones de Tierra Firme）／グラナダのヒネーテ（Granadan Jinetes）／イベリア軽騎兵（Iberian Jinetes）

## 9. 出典

### 一次情報（ゲームスクリプト）

- `dlc/D009_across_the_pillars/in_game/common/situations/battle_for_the_strait.txt`、`golden_century.txt`、`script_values/golden_century_values.txt`（2つの局面の条件、影響力と発火点の増減）
- `in_game/common/scripted_triggers/situation_triggers.txt`（海峡をめぐる戦いの勝利条件）
- `main_menu/common/script_values/default_values.txt`（影響力の増分値）
- `main_menu/setup/1337/10_countries.txt`、`12_diplomacy.txt`（開始時の領土と、グラナダの朝貢関係）
- `in_game/common/advances/country_cas.txt`（固有の進歩）
- `dlc/D009_across_the_pillars/in_game/common/decisions/cas_decisions.txt`、`d009_golden_century_decisions.txt`、`in_game/common/decisions/spanish_councils_decisions.txt`（決断）
- `in_game/common/government_reforms/country_specific.txt`、`dlc/D009_across_the_pillars/in_game/common/government_reforms/d009_country_specific.txt`（政府改革）
- `in_game/common/subject_types/tributary.txt`、`in_game/common/scripted_relations/guarantee.txt`、`in_game/common/scripted_triggers/country_triggers.txt`（朝貢国の性質、独立保障と同盟の条件）
- `in_game/common/international_organizations/union.txt`、`in_game/common/scripted_triggers/international_organization_triggers.txt`、`dlc/D009_across_the_pillars/in_game/common/generic_actions/iberian_union.txt`、`scripted_relations/iberian_wedding_pact.txt`（イベリア連合とスペイン王国の宣言）
- `dlc/D009_across_the_pillars/in_game/common/international_organizations/d009_grand_alliance.txt`（大同盟）
- `dlc/D009_across_the_pillars/in_game/common/expedition_types/d009_gold_fleet_nueva_espana.txt`、`d009_gold_fleet_tierra_firme.txt`、`in_game/common/script_values/gold_fleet.txt`（宝船の遠征）
- `main_menu/localization/japanese/` と `dlc/D009_across_the_pillars/main_menu/localization/japanese/` の各 yml（用語と説明文）

### コミュニティ情報

- eu5.paradoxwikis.com/Patch_1.4（1.4 の主要国がカスティーリャ・モロッコ・グラナダであること）
