# EU5 プレイ中チェックリスト
> 対象パッチ: 1.4 オープンベータ（ビルド 25606497）・変動注意 ／ 最終確認日: 2026-10-13

どの国でも共通の「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。国ごとの事情は扱わない。

## 1. 開始直後（ポーズ中にやること）

- [ ] 「アジェンダ」を開き、自国の歴史的背景と状況別のヒントを読む {#start-agenda}
  - なぜ: 公式チュートリアルが、ゲームを始めるたびに一読するよう勧めている [src: tutorial_l_japanese.yml, lesson_basics_wrap_up_6_desc]
- [ ] 「自動化」パネルを開き、ゲームに任せる項目と自分で管理する項目を決める {#start-automation}
  - なぜ: 自動化した項目はアラートに出なくなるため、何を見るかを先に決めておく [src: tutorial_l_japanese.yml, lesson_basics_wrap_up_3b_desc]
- [ ] 「実施可能な改革」のアラートが出ていれば、「政府」パネルの「国家」タブにある「階級」タブで、王室カード下の＋ボタンから政府改革を選ぶ {#start-reform}
  - なぜ: 政府改革は国の姿を大きく変えるので、新規ゲームでは最初に設定する [src: tutorial_l_japanese.yml, lesson_admin_6b_desc] [src: hints_l_japanese.yml, hint_has_possible_reform_hint_text_2]
- [ ] 「成文化されていない法律」のアラートが出ていれば、「政府」パネルの「国家」タブにある「法律」タブでポリシーを設定する {#start-laws}
  - なぜ: ポリシーが空のままだと得られる恩恵を逃す。設定にはゴールドと安定度がかかる [src: hints_l_japanese.yml, hint_has_possible_law_hint_text_1] [src: hints_l_japanese.yml, hint_has_possible_law_hint_text_3]
- [ ] 「経済」パネルの「収支」タブで、課税スライダー横の歯車を押して全階級への課税を自動化する {#start-tax-auto}
  - なぜ: 自動化すると、各階級の満足度が50%以上になるよう課税される [src: tutorial_l_japanese.yml, lesson_core_loop_4_desc] [src: 00_tutorial_lesson_basics.txt, lesson_core_loop_4]
- [ ] 「収支」タブで月間収支がプラスか確認し、赤字ならスライダーを調整して黒字にする {#start-balance}
  - なぜ: 月間収支がマイナスのままだと、負債や破産につながる [src: scripted_hints.txt, hint_in_deficit] [src: hints_l_japanese.yml, hint_in_deficit_hint_text_1]
- [ ] 「進歩」パネルを開き、研究する進歩を選ぶ {#start-research}
  - なぜ: 研究は常に1つ進めておく。使わなかった研究ポイントは上限まで蓄積され、それを超えると無駄になる [src: hints_l_japanese.yml, hint_can_do_more_research_hint_text_1] [src: hints_l_japanese.yml, hint_can_do_more_research_hint_text_3]
- [ ] 「政府」パネルの「内閣」タブで、空いている席にキャラクターを割り当てる {#start-cabinet}
  - なぜ: 内閣アクションは国を動かす最も強力な道具で、利用できる席はすべて使うべきとされている [src: hints_l_japanese.yml, hint_has_possible_cabinet_action_hint_text_1]
- [ ] 首都のパネルから街道ビルダーを開き、首都に隣接するロケーションへ街道の敷設を始める {#start-road}
  - なぜ: 街道は首都からの近接性の低下を減らして支配度を保つ。国の大小を問わず重要な施策とされている [src: tutorial_l_japanese.yml, lesson_road_3_desc]
- [ ] ミッションが有効なら、「コンテンツ」パネルの「ミッション」タブでミッションツリーを1つ選んで開始する {#start-mission}
  - なぜ: ミッションは序盤を導く目標と報酬を出し、各パネルの使い方の練習にもなる [src: tutorial_l_japanese.yml, lesson_basics_final_desc] [src: tutorial_l_japanese.yml, lesson_admin_28_desc]

## 2. 序盤：伝統〜ルネサンス（1337〜1437）

### 安全確保

到達目標: 赤字・不安定・階級の不満・飢えのどれも放置していない状態にする。

- [ ] 「破産リスク」のアラートが出たら、「経済」パネルのスライダーで税を上げるか支出を下げて黒字に戻す {#early-deficit}
  - なぜ: 月間収支がマイナスのままだと、負債や破産につながる [src: scripted_hints.txt, hint_in_deficit]
- [ ] インフレのアラートが出たら、「経済」パネルの貨幣鋳造スライダーを最小にする {#early-inflation}
  - なぜ: 鋳造はインフレを加速させ、いったん進んだインフレは減速させにくい [src: hints_l_japanese.yml, hint_inflation_hint_text_1] [src: hints_l_japanese.yml, hint_inflation_hint_text_2]
- [ ] 安定度が0以下になったら、「経済」パネルで安定度投資を増やす {#early-stability}
  - なぜ: 安定度が低いと、POPの反乱参加や階級の内戦の危険が高まる [src: scripted_hints.txt, hint_low_stability] [src: hints_l_japanese.yml, hint_low_stability_hint_text_1] [src: economy_lateralview.gui, MODIFIER_TYPE_NAME_stability_investment]
- [ ] 投資しても安定度が戻らないときは、内閣アクション「国家の安定化」を実行する {#early-stability-cabinet}
  - なぜ: 安定度を上げる手段として、公式ヒントが投資の次に挙げている [src: hints_l_japanese.yml, stability_raise_actions] [src: stabilize_country.txt, stabilize_country]
- [ ] 政府力（正統性など）が50未満なら、内閣アクション「政府の強化」を実行する {#early-govpower}
  - なぜ: 正統性が低いと君主力の恩恵が損なわれ、反乱や階級満足度の低下を招く。共和的伝統・献身・遊牧民の結束・部族の団結も同じ50未満で警告される [src: scripted_hints.txt, hint_low_legitimacy] [src: strengthen_government.txt, strengthen_government]
- [ ] 満足度が50%未満の階級があれば、「政府」パネルの「国家」タブにある「階級」タブで特権を見直すか、課税を下げる {#early-estates}
  - なぜ: 不満な階級は国にペナルティを与え、その階級のPOPが反乱に加わりやすくなる [src: scripted_hints.txt, hint_unhappy_estates] [src: 00_defines.txt, LOW_SATISFACTION_THRESHOLD]
- [ ] 「食糧市場在庫の少ない市場」のアラートが出たら、食糧を作るRGOを拡大するか、食糧を輸入する {#early-food}
  - なぜ: 市場の食糧備蓄が足りないと、その州のロケーションが飢饉に陥る [src: hints_l_japanese.yml, hint_low_food_in_market_hint_text_1] [src: hints_l_japanese.yml, hint_low_food_in_market_hint_text_2]
- [ ] 「指揮官の不在」のアラートが出たら、アラートから軍に指揮官を任命する {#early-leader}
  - なぜ: 指揮官がいないと、軍は戦闘で力を発揮できない [src: hints_l_japanese.yml, hint_has_army_without_leader_hint_text_1]
- [ ] 同盟国がいなければ、「外交アクション」パネルの友好アクションで「同盟を提案する」の候補を探し、あまりに弱い国を避けて結ぶ {#early-alliance}
  - なぜ: 同盟は攻撃されたときに味方を呼べるが、弱すぎる国と結ぶと無関係の戦争で敗戦国になることがある [src: scripted_hints.txt, hint_no_allies] [src: hints_l_japanese.yml, hint_no_allies_hint_text_3]

### 安定化

到達目標: 研究・制度・支配度・建造物・交易が止まったり遊んだりしていない状態にする。

- [ ] 「進行中の研究なし」「研究上限が間近」のアラートが出たら、「進歩」パネルで次の進歩を選ぶ {#early-research}
  - なぜ: 研究ポイントは上限までしか蓄積されず、超えた分は無駄になる [src: 00_default.txt, has_nearly_maxed_out_stored_research_progress] [src: hints_l_japanese.yml, hint_can_do_more_research_hint_text_3]
- [ ] 「受容可能な制度」のアラートが出たら、その制度を受容する {#early-institution}
  - なぜ: 制度を受容すると、その時代の新しい進歩を研究できる。受容にはゴールドと安定度がかかる [src: game_concepts_l_japanese.yml, game_concept_institution_desc] [src: 00_hardcoded.txt, embrace_institution]
- [ ] 制度が自国に広がるのが遅いときは、内閣アクション「制度の推進」を実行する（部族政体では不可） {#early-institution-push}
  - なぜ: 公式の説明が、伝播が足りない場合の手段として挙げている。部族政体は実行できない [src: game_concepts_l_japanese.yml, game_concept_institution_desc] [src: study_institutions.txt, study_institutions]
- [ ] 支配度が95%未満で税基盤の大きい州に、内閣アクション「州支配を強化」を実行する {#early-control}
  - なぜ: 支配が及ばない富には課税できず、そのまま階級の取り分になる [src: tutorial_l_japanese.yml, lesson_location_4_desc] [src: increase_control.txt, increase_control_province]
- [ ] 街道ビルダーで、首都から外へ向けて街道を延ばし続ける {#early-roads}
  - なぜ: 支配度は首都からの近接性で決まり、街道がその低下を減らす [src: tutorial_l_japanese.yml, lesson_road_3_desc]
- [ ] 「赤字の建造物」のアラートが出たら、投入物資の輸入で供給を確保するか、不要な建造物を閉鎖する {#early-buildings}
  - なぜ: 投入物資の合計コストが生産物の利益を上回る建造物は赤字になる [src: hints_l_japanese.yml, hint_unprofitable_buildings_hint_text_1] [src: hints_l_japanese.yml, hint_unprofitable_buildings_hint_text_2]
- [ ] 「文化許容量超過」のアラートが出たら、「社会」パネルの「文化」タブで重要度の低い文化の地位を下げる {#early-culture-cap}
  - なぜ: 文化許容量が足りない国はペナルティを受ける [src: scripted_hints.txt, hint_cultural_capacity] [src: hints_l_japanese.yml, hint_cultural_capacity_hint_text_2]
- [ ] 「未使用の交易許容量」のアラートが出たら、市場カードの歯車ボタンで交易を自動化する {#early-trade-auto}
  - なぜ: 交易許容量は使い切るのが基本で、慣れるまでは自動化したままにするよう勧められている [src: hints_l_japanese.yml, hint_unused_trade_capacity_hint_text_1] [src: tutorial_l_japanese.yml, lesson_economy_4_desc]
- [ ] 「関係過多」のアラートが出たら、関係改善を止めるか、一部の同盟や条約を破棄する {#early-diplo-cap}
  - なぜ: 外交許容量を超えて関係を結ぶと、外交的評判と威信にペナルティを受ける [src: scripted_hints.txt, hint_over_diplo_capacity] [src: hints_l_japanese.yml, hint_over_diplo_capacity_hint_text_2]
- [ ] 選択中のミッションを完了したら、「新しいミッションツリーを開始しよう！」の表示から次のツリーを選ぶ {#early-mission}
  - なぜ: ミッションは序盤を導く目標と報酬を出す [src: 00_default.txt, start_new_mission] [src: tutorial_l_japanese.yml, lesson_basics_final_desc]

### 拡大の開始

到達目標: 統合できる速さで、備えの整った戦争だけを始める。

- [ ] 正規兵で戦う予定なら、人的資源が20%以下の間は宣戦布告を控える {#early-manpower}
  - なぜ: 人的資源が少ないと、軍の補充能力が著しく制限される [src: scripted_hints.txt, hint_manpower] [src: hints_l_japanese.yml, hint_manpower_hint_text_2]
- [ ] 宣戦布告の前に、自国の中核地を領有している国に対して使える開戦事由を確認する {#early-cb}
  - なぜ: 開戦事由なしだと安定度と近隣国の評価が下がる。「州の請求」の開戦事由は、相手が自国の中核地を領有していることが条件 [src: tutorial_l_japanese.yml, lesson_military_war_0_desc] [src: conquest.txt, cb_conquer_province]
- [ ] 征服した土地は、内閣アクション「州の統合」で統合する {#early-integrate}
  - なぜ: 統合するまで、征服した土地は国に貢献せず厳しいペナルティを受ける [src: hints_l_japanese.yml, hint_has_conquered_provinces_hint_text_1] [src: integrate_province.txt, integrate_province]
- [ ] 戦争疲弊のアラートが出ている間は、新しい宣戦布告を控えて平和状態にし、下がるのを待つ {#early-war-exhaustion}
  - なぜ: 戦争疲弊が高いと軍の戦闘力が落ち、POPの増加が鈍り、経済が破綻する [src: 00_default.txt, has_high_war_exhaustion] [src: hints_l_japanese.yml, hint_war_exhaustion_hint_text_1] [src: hints_l_japanese.yml, hint_war_exhaustion_hint_text_2] [src: hints_l_japanese.yml, hint_war_exhaustion_hint_text_3]

## 3. 中盤：発見〜宗教改革（1437〜1637）

### 国家の格と外交

- [ ] 「国家ランクをアップグレード可能」のアラートが出たら、クリックして「新しい国家に変容」パネルでランクを上げる {#mid-rank}
  - なぜ: ランクが上がるほど外交許容量・毎月の威信・ライバル枠が増え、一度上げたランクは失われない。条件は7章 [src: 00_default.txt, rank_kingdom] [src: game_concepts_l_japanese.yml, game_concept_country_rank_upper_desc]
- [ ] 帝国ランクの国は、マップモード「支配度」で首都のある地域に支配度の低いロケーションがないか確認し、あれば内閣アクション「州支配を強化」を実行する {#mid-empire-guard}
  - なぜ: 帝国は安定度0未満かつ首都地域の平均支配度が基準未満（または非寛容な文化の人口が総人口の3分の1超）だと、国難「慢心による衰退」で研究速度が半減する。基準は7章 [src: decline_of_empire.txt, can_start] [src: decline_of_empire.txt, research_speed_modifier]
- [ ] 「ライバル候補たち」「不十分なライバル」のアラートが出たら、クリックしてライバル選択画面を開き、自国を脅かす強い国を「ライバルに指定」する {#mid-rival}
  - なぜ: ライバル枠はランクが上がるほど増える。脅威とならないライバルは威信を毎月失わせ、脅威となるライバルは威信をもたらす（公式ヒントの説明・スクリプト未確認） [src: 00_default.txt, num_possible_rivals] [src: hints_l_japanese.yml, hint_has_inadequate_rivals_hint_text_1]
- [ ] 「不忠の従属国」のアラートが出たら、クリックして「従属国の管理」パネルを開き、対象国に外交アクション「評価改善」を実行する {#mid-subjects}
  - なぜ: 忠誠度が基準を下回ると、従属国は戦争を支援せず併合もできない（公式の説明・スクリプト未確認）。公式ヒントは評価の改善を最優先に勧める。基準は7章 [src: game_concepts_l_japanese.yml, game_concept_disloyal_subjects_desc] [src: hints_l_japanese.yml, hint_has_disloyal_subjects_hint_text_2]

### 進歩と内政

- [ ] 「進歩」パネルで、君主力を増やす進歩と、続く内閣の席を増やす進歩を優先して研究する（発見は「国政術」→「初期行政能力」、宗教改革は「信仰属地主義」→「近世の統治」） {#mid-adv-crown}
  - なぜ: 君主力が高いほど内閣の効率が上がり、法律を制定しやすくなる（公式ヒントの説明・スクリプト未確認）。続く進歩で内閣の席も1つ増える [src: hints_l_japanese.yml, hint_crown_power_hint_text_1] [src: 0_age_of_discovery.txt, government_size_discovery] [src: 0_age_of_reformation.txt, early_modern_administation]
- [ ] 「進歩」パネルで、政府改革保有数が増える進歩（発見は「初期行政改革」、宗教改革は「君主」）を研究する {#mid-adv-reform}
  - なぜ: 公式ヒントは可能なかぎりの政府改革を実施すべきとしている。保有数は各時代に1つ増える [src: hints_l_japanese.yml, hint_has_possible_reform_hint_text_1] [src: 0_age_of_discovery.txt, gov_reform_discovery_a] [src: 0_age_of_reformation.txt, gov_reform_reformation_a]
- [ ] 進歩「舗装路」を研究したら、街道ビルダーで主要な街道を舗装路にアップグレードする {#mid-road-upgrade}
  - なぜ: 舗装路は砂利道より近接性の補正が大きく、首都からの距離による支配度の低下を和らげる [src: 00_generic.txt, paved_road] [src: interfaces_l_japanese.yml, ROAD_BUILDER_UPGRADE_ROADS]
- [ ] 「官僚機構の空きスロット」のアラートが出たら、クリックして「官僚機構」パネルで「官僚機構を追加」する {#mid-bureau}
  - なぜ: 官僚機構は維持費を払いきれればマイナス補正が出ず、払えないとマイナス補正だけが出る（公式の説明・スクリプト未確認）。スロットは進歩「執行官僚制度」などで増える [src: game_concepts_l_japanese.yml, game_concept_bureaucracy_maintenance_desc] [src: 0_age_of_reformation.txt, generic_bureaucracy_4_advance]
- [ ] 進歩「自治区特権」を研究したら、「都市特権」パネルで生産に向く都市に専門化の都市特権を付与する {#mid-town-rights}
  - なぜ: 指定した品の生産量が増える代わりに、その都市の生産効率が下がる。数値は7章 [src: 01_discovery.txt, royal_textile_rights] [src: default_values.txt, town_right_efficiency_penalty] [src: hints_l_japanese.yml, hint_town_rights_hint_text_3]

### 戦争と反乱の後始末

- [ ] 戦争が始まったら、「未動員の召集軍」のアラートから「軍事」パネルの「召集軍を動員」で召集軍を動員する {#mid-levy}
  - なぜ: 序盤の数世紀は軍の大部分が召集軍で、戦争中は常に動員するのが推奨される（公式ヒントの説明・スクリプト未確認） [src: hints_l_japanese.yml, hint_has_unraised_levies_in_war_hint_text_1]
- [ ] 平和になっても戦争疲弊が残るときは、内閣アクション「戦争疲弊を軽減」を実行する {#mid-war-exh}
  - なぜ: 自然減に上乗せして毎月の戦争疲弊を減らせる。戦争疲弊が0を超えていれば実行できる [src: country.txt, country_base_values] [src: reduce_war_exhaustion.txt, reduce_war_exhaustion]
- [ ] 「荒廃したロケーション」のアラートが出たら、荒廃したロケーションのある州に内閣アクション「復興への取り組み」を実行する {#mid-recovery}
  - なぜ: 繁栄度がマイナスのロケーションは人口に壊滅的な影響を受ける（公式の説明・スクリプト未確認）。このアクションは繁栄度がマイナスの州にだけ実行できる [src: game_concepts_l_japanese.yml, game_concept_prosperity_desc] [src: recovery_effort.txt, recovery_effort]
- [ ] 「反乱運動」のアラートが出たら、クリックして「混乱」パネルで反乱軍を確認し、内閣アクション「反乱軍の弾圧」を実行する {#mid-rebels}
  - なぜ: 反乱の支持が最大に達すると反乱または内戦が起きる。弾圧は反乱の進行を抑える（公式ヒントの説明） [src: hints_l_japanese.yml, hint_rebels_growing_hint_text_1] [src: rebel_crackdown.txt, rebel_crackdown]

## 4. 終盤：絶対主義〜革命（1637〜）

### 進歩の取り方

- [ ] 「進歩」パネルで、君主力を大きく増やす進歩（絶対主義は「絶対的支配者」、革命は「国家」）と、内閣の席を増やす進歩（「忠実な従属者」「現代的代表制度」）を優先して研究する {#late-adv-crown}
  - なぜ: 君主力は、絶対主義に進むと進歩によって顕著に増える（公式の説明） [src: game_concepts_l_japanese.yml, game_concept_crown_power_desc] [src: 0_age_of_absolutism.txt, absolute_rulership] [src: 0_age_of_revolutions.txt, crown_power_advance_revolutions]
- [ ] 「進歩」パネルで、政府改革保有数や官僚機構のスロットが増える進歩（絶対主義は「立憲主義」、革命は「権力の分離」「現代的官僚制度」）を研究する {#late-adv-reform}
  - なぜ: 公式ヒントは可能なかぎりの政府改革を実施すべきとしている [src: hints_l_japanese.yml, hint_has_possible_reform_hint_text_1] [src: 0_age_of_absolutism.txt, the_constitution] [src: 0_age_of_revolutions.txt, modern_bureaucracy]
- [ ] 進歩「近代的街道」「鉄道」を研究したら、街道ビルダーで主要な街道をアップグレードする {#late-road-upgrade}
  - なぜ: 近接性の補正は街道の種別が上がるほど大きい [src: 00_generic.txt, railroad] [src: 3_road_unlocks.txt, modern_road_advance]

### 崩れの予防

- [ ] 絶対主義の時代に入ったら、「従属国の管理」パネルで忠誠度が基準に近い従属国がないか確認し、あれば外交アクション「評価改善」を実行する {#late-subjects-age}
  - なぜ: 従属国の忠誠度は絶対主義で下がり、革命でさらに下がる。数値は7章 [src: 00_default.txt, age_5_absolutism] [src: 00_default.txt, age_6_revolutions]
- [ ] 革命の時代に制度「啓蒙」を受容したら、「政府」パネルの「国家」タブにある「階級」タブで庶民と市民の満足度を確認し、下回りそうなら課税を下げるか特権を見直す {#late-revolution}
  - なぜ: 啓蒙を受容した国は、庶民と市民の満足度がともに基準を下回ると国難「革命！」の対象になりうる（ほかに識字率や列強などの条件あり）。始まると安定度投資に大きなペナルティがつく。基準は7章 [src: revolution_disaster.txt, can_start] [src: revolution_disaster.txt, stability_investment]

## 5. 定期ルーチン {.routine}

## 6. 困ったとき

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|
| 時代の開始年 | ルネサンス1342／発見1437／宗教改革1537／絶対主義1637／革命1737 | [src: 00_default.txt, age_2_renaissance 〜 age_6_revolutions] |
| ゲーム開始日 | 1337年4月1日 | [src: 00_defines.txt, START_DATE] |
| 安定度 | 0以下で対処を始める／-50以下は深刻 | [src: scripted_hints.txt, hint_low_stability] [src: scripted_hints.txt, hint_very_low_stability] |
| 政府力（正統性など） | 50未満で「政府の強化」を検討する | [src: scripted_hints.txt, hint_low_legitimacy] |
| 階級の満足度 | 50%未満は不満（ペナルティ側） | [src: 00_defines.txt, LOW_SATISFACTION_THRESHOLD] [src: scripted_hints.txt, hint_unhappy_estates] |
| 人的資源 | 20%以下なら正規兵で戦う宣戦を控える | [src: scripted_hints.txt, hint_manpower] |
| 州の支配度 | 95%未満の州が「州支配を強化」の対象 | [src: 00_defines.txt, LOW_CONTROL_THRESHOLD_FOR_BEST_TAX] [src: increase_control.txt, increase_control_province] |
| ランクの昇格条件 | 公国：威信25・総人口200／王国：威信50・総人口2000／帝国：列強・威信70・総人口10000（総人口は千人単位。信仰・文化の人口でも代替可） | [src: country_triggers.txt, can_upgrade_country_rank_duchy] [src: country_triggers.txt, can_upgrade_country_rank_kingdom] [src: country_triggers.txt, can_upgrade_country_rank_empire] |
| 国難「慢心による衰退」 | 帝国を15年以上保持し、安定度0未満かつ首都地域の平均支配度が発見45%・宗教改革50%・絶対主義55%・革命60%未満（または非寛容な文化の人口が総人口の3分の1超） | [src: decline_of_empire.txt, can_start] [src: _hardcoded.txt, recently_became_empire_variable] |
| 従属国の忠誠度 | 50未満で不忠。時代補正は絶対主義−10／革命−30 | [src: 00_defines.txt, TOO_DISLOYAL_THRESHOLD] [src: 00_default.txt, age_5_absolutism] [src: 00_default.txt, age_6_revolutions] |
| 国難「革命！」の引き金 | 啓蒙を受容した国で、庶民と市民の満足度がともに35%未満 | [src: revolution_disaster.txt, can_start] |
| 専門化の都市特権 | 指定品の生産+20〜30%、生産効率−5%、付与に政治的影響力20 | [src: 01_discovery.txt, royal_tooling_rights] [src: 01_discovery.txt, royal_textile_rights] [src: default_values.txt, town_right_efficiency_penalty] [src: 00_hardcoded.txt, grant_town_rights] |

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

- 内閣（Cabinet）／内閣アクション（Cabinet Action）
- 国家の安定化（Stabilize Country）／政府の強化（Strengthen Government）／州支配を強化（Increase Province Control）／州の統合（Integrate Province）／制度の推進（Foster Institutions）
- 安定度（Stability）／安定度投資（Stability Investment）／政府力（Government Power）／正統性（Legitimacy）／共和的伝統（Republican Tradition）／献身（Devotion）／遊牧民の結束（Horde Unity）／部族の団結（Tribal Cohesion）
- 階級（Estate）／王室（Crown）／満足度（Satisfaction）／特権（Privilege）／君主力（Crown Power）
- 政府改革（Government Reform）／法律（Law）／ポリシー（Policy）
- 収支（Balance）／貨幣鋳造（Minting）／インフレ（Inflation）／税基盤（Tax Base）
- 制度（Institution）／受容（Embrace）／進歩（Advance）／時代（Age）
- 支配度（Control）／近接性（Proximity）／街道（Road）／ロケーション（Location）／中核地（Core）
- 開戦事由（Casus Belli）／州の請求（Claims on Province）／戦争疲弊（War Exhaustion）／人的資源（Manpower）／指揮官（Commander）／同盟（Alliance）／外交アクション（Diplomatic Action）
- 文化許容量（Cultural Capacity）／交易許容量（Trade Capacity）／外交許容量（Diplomatic Capacity）／食糧（Food）／RGO（R.G.O.）／ミッション（Mission）／自動化パネル（Automation Panel）／アジェンダ（Agenda）
- 国家ランク（Country Rank）／公国（Duchy）／王国（Kingdom）／帝国（Empire）／ライバル（Rival）／威信（Prestige）／政治的影響力（Political Influence）／庶民（Commoners）／市民（Burghers）
- 国難（Disaster）／慢心による衰退（Decline of Empire）／革命！（Revolution!）／繁栄度（Prosperity）／反乱軍の弾圧（Rebel Crackdown）／復興への取り組み（Recovery Effort）／戦争疲弊を軽減（Reduce War Exhaustion）
- 従属国（Subject）／従属国忠誠度（Subject Loyalty）／不忠の従属国（Disloyal Subject）／評価改善（Improve Opinion）／召集軍（Levy）／官僚機構（Bureaucracy）／都市特権（Urban Rights）／自治区特権（Borough Privileges）／探検（Exploration）／植民（Colonization）／啓蒙（Enlightenment）
- 舗装路（Paved Road）／近代的街道（Modern Road）／鉄道（Railroad）
- 進歩名：国政術（Statecraft）／初期行政能力（Early Administrative Capacity）／信仰属地主義（'Cuius Regio, Eius Religio'）／近世の統治（Early Modern Administration）／初期行政改革（Early Administrative Reformation）／君主（The Prince）／執行官僚制度（Executive Bureaucracy）／絶対的支配者（Absolute Rulership）／忠実な従属者（Loyal Subordinates）／立憲主義（The Constitution）／国家（Nation）／現代的代表制度（Modern Representation）／権力の分離（Separation of Powers）／現代的官僚制度（Modern Bureaucracy）

## 9. 出典

### 一次情報（ゲームスクリプト）

- `in_game/common/age/00_default.txt`（時代の開始年）
- `loading_screen/common/defines/00_defines.txt`（開始日、階級の不満の閾値、支配度の閾値）
- `in_game/common/tutorial_lessons/00_tutorial_lesson_basics.txt`、`00_tutorial_lesson_admin.txt`、`00_tutorial_lesson_diplomacy.txt`、`00_tutorial_lesson_military.txt`（公式の手順）
- `in_game/common/alert_descriptions/00_default.txt`（アラートの種類）
- `in_game/common/scriptable_hints/scripted_hints.txt`（ヒントの発動条件）
- `in_game/common/cabinet_actions/stabilize_country.txt`、`strengthen_government.txt`、`increase_control.txt`、`integrate_province.txt`、`study_institutions.txt`（内閣アクション）
- `in_game/common/prices/00_hardcoded.txt`（制度の受容コスト）
- `in_game/common/casus_belli/conquest.txt`（「州の請求」の開戦事由）
- `in_game/gui/economy_lateralview.gui`（安定度投資の置き場所）
- `in_game/common/country_ranks/00_default.txt`、`scripted_triggers/country_triggers.txt`（ランクの効果と昇格条件）
- `in_game/common/disasters/decline_of_empire.txt`、`revolution_disaster.txt`、`on_action/_hardcoded.txt`（国難の発生条件）
- `in_game/common/advances/0_age_of_discovery.txt`、`0_age_of_reformation.txt`、`0_age_of_absolutism.txt`、`0_age_of_revolutions.txt`、`3_road_unlocks.txt`（枠を増やす進歩、街道の解禁）
- `in_game/common/road_types/00_generic.txt`、`town_rights/01_discovery.txt`、`main_menu/common/script_values/default_values.txt`（街道・都市特権の効果）
- `in_game/common/cabinet_actions/reduce_war_exhaustion.txt`、`recovery_effort.txt`、`rebel_crackdown.txt`、`auto_modifiers/country.txt`（内閣アクション、戦争疲弊の自然減）
- `in_game/gui/alertmanager.gui`（アラートのクリック先）
- `main_menu/localization/japanese/tutorial_l_japanese.yml`、`hints_l_japanese.yml`、`game_concepts_l_japanese.yml`、`advances_l_japanese.yml`、`interfaces_l_japanese.yml`（公式の説明文）

### コミュニティ情報

- eu5.paradoxwikis.com/Country_rank（総人口の単位が千人であることをスクリプトの値と照合）
- eu5.paradoxwikis.com/Age（時代ごとの従属国忠誠度の値をスクリプトと照合）
