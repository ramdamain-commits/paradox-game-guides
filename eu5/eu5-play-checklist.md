# EU5 プレイ中チェックリスト
> 対象パッチ: 1.4 オープンベータ（ビルド 25606497）・変動注意 ／ 最終確認日: 2026-10-13

どの国でも共通の「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。国ごとの事情は扱わない。「（公式の説明）」は、ゲーム内のヒント・チュートリアル・用語説明が根拠で、効果をスクリプトでは確かめていない記述。

## 1. 開始直後（ポーズ中にやること）

- [ ] 「アジェンダ」を開き、自国の歴史的背景と状況別のヒントを読む {#start-agenda}
  - なぜ: 公式チュートリアルが、ゲームを始めるたびに一読するよう勧めている [src: tutorial_l_japanese.yml, lesson_basics_wrap_up_6_desc]
- [ ] 「自動化」パネルを開き、ゲームに任せる項目と自分で管理する項目を決める {#start-automation}
  - なぜ: 自動化した項目はアラートに出なくなるため、何を見るかを先に決めておく [src: tutorial_l_japanese.yml, lesson_basics_wrap_up_3b_desc]
- [ ] 「実施可能な改革」のアラートが出ていれば、「政府」パネルの「国家」タブにある「階級」タブで、王室カード下の＋ボタンから政府改革を選ぶ {#start-reform}
  - なぜ: 政府改革は国の姿を大きく変えるので、新規ゲームでは最初に設定する [src: tutorial_l_japanese.yml, lesson_admin_6b_desc] [src: hints_l_japanese.yml, hint_has_possible_reform_hint_text_2]
- [ ] 「成文化されていない法律」のアラートが出ていれば、「政府」パネルの「国家」タブにある「法律」タブでポリシーを設定する {#start-laws}
  - なぜ: ポリシーが空のままだと得られる恩恵を逃す。設定にはダカットと安定度がかかる（公式の説明） [src: hints_l_japanese.yml, hint_has_possible_law_hint_text_1] [src: hints_l_japanese.yml, hint_has_possible_law_hint_text_3]
- [ ] 「経済」パネルの「収支」タブで、課税スライダー横の歯車を押して全階級への課税を自動化する {#start-tax-auto}
  - なぜ: 自動化すると、各階級の満足度が50%以上になるよう課税される（公式の説明） [src: tutorial_l_japanese.yml, lesson_core_loop_4_desc] [src: 00_tutorial_lesson_basics.txt, lesson_core_loop_4]
- [ ] 「収支」タブで月間収支がプラスか確認し、赤字ならスライダーを調整して黒字にする {#start-balance}
  - なぜ: 月間収支がマイナスのままだと、負債や破産につながる（公式の説明） [src: scripted_hints.txt, hint_in_deficit] [src: hints_l_japanese.yml, hint_in_deficit_hint_text_1]
- [ ] 「進歩」パネルを開き、研究する進歩を選ぶ {#start-research}
  - なぜ: 研究は常に1つ進めておく。使わなかった研究ポイントは上限まで蓄積され、それを超えると無駄になる（公式の説明） [src: hints_l_japanese.yml, hint_can_do_more_research_hint_text_1] [src: hints_l_japanese.yml, hint_can_do_more_research_hint_text_3]
- [ ] 「政府」パネルの「内閣」タブで、空いている閣僚ポストにキャラクターを割り当てる {#start-cabinet}
  - なぜ: 内閣アクションは国を動かす最も強力な道具で、利用できる閣僚ポストはすべて使うべきとされている（公式の説明） [src: hints_l_japanese.yml, hint_has_possible_cabinet_action_hint_text_1]
- [ ] 首都のパネルから街道ビルダーを開き、首都に隣接するロケーションへ街道の敷設を始める {#start-road}
  - なぜ: 街道は首都からの近接性の低下を減らして支配度を保つ。国の大小を問わず重要な施策とされている（公式の説明） [src: tutorial_l_japanese.yml, lesson_road_3_desc]
- [ ] ミッションが有効なら、「コンテンツ」パネルの「ミッション」タブでミッションツリーを1つ選んで開始する {#start-mission}
  - なぜ: ミッションは序盤を導く目標と報酬を出し、各パネルの使い方の練習にもなる [src: tutorial_l_japanese.yml, lesson_basics_final_desc] [src: tutorial_l_japanese.yml, lesson_admin_28_desc]

## 2. 序盤：伝統〜ルネサンス（1337〜1437）

### 安全確保

到達目標: 赤字・不安定・階級の不満・飢えのどれも放置していない状態にする。

- [ ] 「破産リスク」のアラートが出たら、「経済」パネルのスライダーで税を上げるか支出を下げて黒字に戻す {#early-deficit}
  - なぜ: 月間収支がマイナスのままだと、負債や破産につながる（公式の説明） [src: scripted_hints.txt, hint_in_deficit]
- [ ] インフレのアラートが出たら、「経済」パネルの貨幣鋳造スライダーを最小にする {#early-inflation}
  - なぜ: 鋳造はインフレを加速させ、いったん進んだインフレは減速させにくい（公式の説明） [src: hints_l_japanese.yml, hint_inflation_hint_text_1] [src: hints_l_japanese.yml, hint_inflation_hint_text_2]
- [ ] 安定度が0以下になったら、「経済」パネルで安定度投資を増やす {#early-stability}
  - なぜ: 安定度が低いと、POPの反乱参加や階級の内戦の危険が高まる（公式の説明） [src: scripted_hints.txt, hint_low_stability] [src: hints_l_japanese.yml, hint_low_stability_hint_text_1] [src: economy_lateralview.gui, MODIFIER_TYPE_NAME_stability_investment]
- [ ] 投資しても安定度が戻らないときは、内閣アクション「国家の安定化」を実行する {#early-stability-cabinet}
  - なぜ: 安定度を上げる手段として、公式ヒントが投資の次に挙げている [src: hints_l_japanese.yml, stability_raise_actions] [src: stabilize_country.txt, stabilize_country]
- [ ] 政府力（正統性など）が50未満なら、内閣アクション「政府の強化」を実行する {#early-govpower}
  - なぜ: 正統性が低いと君主力の恩恵が損なわれ、反乱や階級満足度の低下を招く（公式の説明）。共和的伝統・献身・遊牧民の結束・部族の団結も同じ50未満で警告される [src: scripted_hints.txt, hint_low_legitimacy] [src: strengthen_government.txt, strengthen_government]
- [ ] 満足度が50%未満の階級があれば、「政府」パネルの「国家」タブにある「階級」タブで特権を見直すか、課税を下げる {#early-estates}
  - なぜ: 不満な階級は国にペナルティを与え、その階級のPOPが反乱に加わりやすくなる（公式の説明） [src: scripted_hints.txt, hint_unhappy_estates] [src: 00_defines.txt, LOW_SATISFACTION_THRESHOLD]
- [ ] 「食糧市場在庫の少ない市場」のアラートが出たら、食糧を作るRGOを拡大するか、食糧を輸入する {#early-food}
  - なぜ: 市場の食糧備蓄が足りないと、その州のロケーションが飢饉に陥る（公式の説明） [src: hints_l_japanese.yml, hint_low_food_in_market_hint_text_1] [src: hints_l_japanese.yml, hint_low_food_in_market_hint_text_2]
- [ ] 「指揮官の不在」のアラートが出たら、アラートから軍に指揮官を任命する {#early-leader}
  - なぜ: 指揮官がいないと、軍は戦闘で力を発揮できない（公式の説明） [src: hints_l_japanese.yml, hint_has_army_without_leader_hint_text_1]
- [ ] 同盟国がいなければ、「外交アクション」パネルの友好アクションで「同盟を提案する」の候補を探し、あまりに弱い国を避けて結ぶ {#early-alliance}
  - なぜ: 同盟は攻撃されたときに味方を呼べるが、弱すぎる国と結ぶと無関係の戦争で敗戦国になることがある（公式の説明） [src: scripted_hints.txt, hint_no_allies] [src: hints_l_japanese.yml, hint_no_allies_hint_text_3]

### 安定化

到達目標: 研究・制度・支配度・建造物・交易が止まったり遊んだりしていない状態にする。

- [ ] 「進行中の研究なし」「研究上限が間近」のアラートが出たら、「進歩」パネルで次の進歩を選ぶ {#early-research}
  - なぜ: 研究ポイントは上限までしか蓄積されず、超えた分は無駄になる（公式の説明） [src: 00_default.txt, has_nearly_maxed_out_stored_research_progress] [src: hints_l_japanese.yml, hint_can_do_more_research_hint_text_3]
- [ ] 「受容可能な制度」のアラートが出たら、その制度を受容する {#early-institution}
  - なぜ: 制度を受容すると、その時代の新しい進歩を研究できる（公式の説明）。受容にはダカットと安定度がかかる [src: game_concepts_l_japanese.yml, game_concept_institution_desc] [src: 00_hardcoded.txt, embrace_institution]
- [ ] 制度が自国に広がるのが遅いときは、内閣アクション「制度の推進」を実行する（部族政体では不可） {#early-institution-push}
  - なぜ: 公式の説明が、伝播が足りない場合の手段として挙げている。部族政体は実行できない [src: game_concepts_l_japanese.yml, game_concept_institution_desc] [src: study_institutions.txt, study_institutions]
- [ ] 支配度が95%未満で税基盤の大きい州に、内閣アクション「州支配を強化」を実行する {#early-control}
  - なぜ: 支配が及ばない富には課税できず、そのまま階級の取り分になる（公式の説明） [src: tutorial_l_japanese.yml, lesson_location_4_desc] [src: increase_control.txt, increase_control_province]
- [ ] 街道ビルダーで、首都から外へ向けて街道を延ばし続ける {#early-roads}
  - なぜ: 支配度は首都からの近接性で決まり、街道がその低下を減らす（公式の説明） [src: tutorial_l_japanese.yml, lesson_road_3_desc]
- [ ] 「赤字の建造物」のアラートが出たら、投入物資の輸入で供給を確保するか、不要な建造物を閉鎖する {#early-buildings}
  - なぜ: 投入物資の合計コストが生産物の利益を上回る建造物は赤字になる（公式の説明） [src: hints_l_japanese.yml, hint_unprofitable_buildings_hint_text_1] [src: hints_l_japanese.yml, hint_unprofitable_buildings_hint_text_2]
- [ ] 「文化許容量超過」のアラートが出たら、「社会」パネルの「文化」タブで重要度の低い文化の地位を下げる {#early-culture-cap}
  - なぜ: 文化許容量が足りない国はペナルティを受ける（公式の説明） [src: scripted_hints.txt, hint_cultural_capacity] [src: hints_l_japanese.yml, hint_cultural_capacity_hint_text_2]
- [ ] 「未使用の交易許容量」のアラートが出たら、市場カードの歯車ボタンで交易を自動化する {#early-trade-auto}
  - なぜ: 交易許容量は使い切るのが基本で、慣れるまでは自動化したままにするよう勧められている（公式の説明） [src: hints_l_japanese.yml, hint_unused_trade_capacity_hint_text_1] [src: hints_l_japanese.yml, hint_unused_trade_capacity_hint_text_2] [src: tutorial_l_japanese.yml, lesson_economy_4_desc]
- [ ] 「関係過多」のアラートが出たら、評価改善を止めるか、一部の同盟や条約を破棄する {#early-diplo-cap}
  - なぜ: 外交許容量を超えて関係を結ぶと、外交評判と威信にペナルティを受ける（公式の説明） [src: scripted_hints.txt, hint_over_diplo_capacity] [src: hints_l_japanese.yml, hint_over_diplo_capacity_hint_text_2]
- [ ] 選択中のミッションを完了したら、「新しいミッションツリーを開始しよう！」の表示から次のツリーを選ぶ {#early-mission}
  - なぜ: ミッションは序盤を導く目標と報酬を出す [src: 00_default.txt, start_new_mission] [src: tutorial_l_japanese.yml, lesson_basics_final_desc]

### 拡大の開始

到達目標: 統合できる速さで、備えの整った戦争だけを始める。

- [ ] 正規兵で戦う予定なら、人的資源が20%以下の間は宣戦布告を控える {#early-manpower}
  - なぜ: 人的資源が少ないと、軍の補充能力が著しく制限される（公式の説明） [src: scripted_hints.txt, hint_manpower] [src: hints_l_japanese.yml, hint_manpower_hint_text_2]
- [ ] 宣戦布告の前に、自国の中核地を領有している国に対して使える開戦事由を確認する {#early-cb}
  - なぜ: 開戦事由なしだと安定度と近隣国の評価が下がる（公式の説明）。「州の請求」の開戦事由は、相手が自国の中核地を領有していることが条件 [src: tutorial_l_japanese.yml, lesson_military_war_0_desc] [src: conquest.txt, cb_conquer_province]
- [ ] 征服した土地は、内閣アクション「州の統合」で統合する {#early-integrate}
  - なぜ: 統合するまで、征服した土地は国に貢献せず厳しいペナルティを受ける（公式の説明）。進歩「改善された統合」の取得後は使えなくなり、4章の「地域の統合」に置き換わる [src: hints_l_japanese.yml, hint_has_conquered_provinces_hint_text_1] [src: integrate_province.txt, integrate_province] [src: 3_cabinet_actions_unlocks.txt, integrate_area_advance]
- [ ] 戦争疲弊のアラートが出ている間は、新しい宣戦布告を控えて平和状態にし、下がるのを待つ {#early-war-exhaustion}
  - なぜ: 戦争疲弊が高いと軍の戦闘力が落ち、POPの増加が鈍り、経済が破綻する（公式の説明） [src: 00_default.txt, has_high_war_exhaustion] [src: hints_l_japanese.yml, hint_war_exhaustion_hint_text_1] [src: hints_l_japanese.yml, hint_war_exhaustion_hint_text_2] [src: hints_l_japanese.yml, hint_war_exhaustion_hint_text_3]

## 3. 中盤：発見〜宗教改革（1437〜1637）

### 本格拡大

- [ ] 統合を進めている征服地で他文化のPOPが多いときは、内閣アクション「POPを我々の文化に同化させる」を実行し、その州を自国の主要文化または受容文化へ同化させる {#mid-assimilate}
  - なぜ: 自国の文化がそのロケーションの支配的な文化になると統合が大幅に加速する（公式の説明）。同化中は、その州への移住の誘引が下がる [src: hints_l_japanese.yml, hint_has_conquered_provinces_hint_text_3] [src: promote_culture.txt, promote_culture]
- [ ] 首都から遠く富が多いのに支配度の低い都は、街道で首都と結んだうえで、建造物「地方総督府」を建設する {#mid-governor}
  - なぜ: 地方総督府は近接性の新たな供給源になる。隣接するロケーションの近接性も上げ、首都から高い近接性を得ている場所では効果がない（公式の説明）。維持費も高い。数値は7章 [src: capital_buildings.txt, local_governor] [src: modifier_types_l_japanese.yml, MODIFIER_TYPE_DESC_local_proximity_source] [src: hints_l_japanese.yml, hint_control_hint_text_2]

### 国家の格と外交

- [ ] 「国家ランクをアップグレード可能」のアラートが出たら、クリックして「新しい国家に変容」パネルでランクを上げる {#mid-rank}
  - なぜ: ランクが上がるほど外交許容量・毎月の威信・ライバル枠が増え、一度上げたランクは失われない（公式の説明）。条件は7章（帝国には宗教・HRE絡みの追加条件がある。上げられないときは同パネルで条件を確認する） [src: 00_default.txt, rank_kingdom] [src: 00_default.txt, rank_empire] [src: game_concepts_l_japanese.yml, game_concept_country_rank_upper_desc]
- [ ] 帝国ランクの国は、マップモード「支配度」で首都のある地方に支配度の低いロケーションがないか確認し、あれば内閣アクション「州支配を強化」を実行する {#mid-empire-guard}
  - なぜ: 帝国は安定度0未満かつ首都がある地方の平均支配度が基準未満（または受容文化・容認文化のどちらでもない文化の人口が総人口の3分の1超）だと、国難「慢心による衰退」で研究速度が半減する。基準は7章 [src: decline_of_empire.txt, can_start] [src: decline_of_empire.txt, research_speed_modifier]
- [ ] 「ライバル候補たち」「不十分なライバル」のアラートが出たら、クリックしてライバル選択画面を開き、自国を脅かす強い国を「ライバルに指定」する {#mid-rival}
  - なぜ: ライバル枠はランクが上がるほど増える。脅威とならないライバルは威信を毎月失わせ、脅威となるライバルは威信をもたらす（公式の説明） [src: 00_default.txt, num_possible_rivals] [src: hints_l_japanese.yml, hint_has_inadequate_rivals_hint_text_1]
- [ ] 「不忠の従属国」のアラートが出たら、クリックして「従属国の管理」パネルを開き、対象国に外交アクション「評価改善」を実行する {#mid-subjects}
  - なぜ: 従属国忠誠度が基準を下回ると、従属国は戦争を支援せず併合もできない（公式の説明）。公式ヒントは評価の改善を最優先に勧める。基準は7章 [src: game_concepts_l_japanese.yml, game_concept_disloyal_subjects_desc] [src: hints_l_japanese.yml, hint_has_disloyal_subjects_hint_text_2]

### 進歩と内政

- [ ] 「進歩」パネルで、君主力を増やす進歩と、続く閣僚ポストを増やす進歩を優先して研究する（発見は「国政術」→「初期行政能力」、宗教改革は「信仰属地主義」→「近世の統治」） {#mid-adv-crown}
  - なぜ: 君主力が高いほど内閣の効率が上がり、法律を制定しやすくなる（公式の説明）。続く進歩で閣僚ポストも1つ増える [src: hints_l_japanese.yml, hint_crown_power_hint_text_1] [src: 0_age_of_discovery.txt, government_size_discovery] [src: 0_age_of_reformation.txt, early_modern_administation]
- [ ] 「進歩」パネルで、政府改革保有数が増える進歩（発見は「初期行政改革」、宗教改革は「君主」）を研究する {#mid-adv-reform}
  - なぜ: 公式ヒントは可能なかぎりの政府改革を実施すべきとしている。保有数は各時代に1つ増える [src: hints_l_japanese.yml, hint_has_possible_reform_hint_text_1] [src: 0_age_of_discovery.txt, gov_reform_discovery_a] [src: 0_age_of_reformation.txt, gov_reform_reformation_a]
- [ ] 進歩「舗装路」を研究したら、街道ビルダーで主要な街道を舗装路にアップグレードする {#mid-road-upgrade}
  - なぜ: 舗装路は砂利道より近接性の補正が大きく、首都からの距離による支配度の低下を和らげる [src: 00_generic.txt, paved_road] [src: interfaces_l_japanese.yml, ROAD_BUILDER_UPGRADE_ROADS] [src: game_concepts_l_japanese.yml, game_concept_proximity_desc] [src: game_concepts_l_japanese.yml, game_concept_control_desc]
- [ ] 「官僚機構の空きスロット」のアラートが出たら、クリックして「官僚機構」パネルで「官僚機構を追加」する {#mid-bureau}
  - なぜ: 官僚機構は維持費を払いきれればマイナス補正が出ず、払えないとマイナス補正だけが出る（公式の説明）。スロットは進歩「執行官僚制度」などで増える [src: game_concepts_l_japanese.yml, game_concept_bureaucracy_maintenance_desc] [src: 0_age_of_reformation.txt, generic_bureaucracy_4_advance]
- [ ] 進歩「自治区特権」を研究したら、「都市特権」パネルでその品の産地にある都市に専門化の都市特権を付与する {#mid-town-rights}
  - なぜ: 指定した品の生産量が増える代わりに、その都市の生産効率が下がる。数値は7章 [src: 01_discovery.txt, royal_textile_rights] [src: default_values.txt, town_right_efficiency_penalty] [src: hints_l_japanese.yml, hint_town_rights_hint_text_3]

### 戦争と反乱の後始末

- [ ] 戦争が始まったら、「未動員の召集軍」のアラートから「軍事」パネルの「召集軍を動員」で召集軍を動員する {#mid-levy}
  - なぜ: 序盤の数世紀は軍の大部分が召集軍で、戦争中は常に動員するのが推奨される（公式の説明） [src: hints_l_japanese.yml, hint_has_unraised_levies_in_war_hint_text_1]
- [ ] 平和になっても戦争疲弊が残るときは、内閣アクション「戦争疲弊を軽減」を実行する {#mid-war-exh}
  - なぜ: 自然減に上乗せして毎月の戦争疲弊を減らせる。戦争疲弊が0を超えていれば実行できる [src: country.txt, country_base_values] [src: reduce_war_exhaustion.txt, reduce_war_exhaustion]
- [ ] 「荒廃したロケーション」のアラートが出たら、荒廃したロケーションのある州に内閣アクション「復興への取り組み」を実行する {#mid-recovery}
  - なぜ: 繁栄度がマイナスのロケーションは人口に壊滅的な影響を受ける（公式の説明）。このアクションは繁栄度がマイナスの州にだけ実行できる [src: game_concepts_l_japanese.yml, game_concept_prosperity_desc] [src: recovery_effort.txt, recovery_effort]
- [ ] 「反乱運動」のアラートが出たら、クリックして「混乱」パネルで反乱軍を確認し、内閣アクション「反乱軍の弾圧」を実行する {#mid-rebels}
  - なぜ: 反乱の支持が最大に達すると反乱または内戦が起きる（公式の説明）。弾圧は反乱の進行を抑える [src: hints_l_japanese.yml, hint_rebels_growing_hint_text_1] [src: hints_l_japanese.yml, hint_rebels_growing_hint_text_2] [src: rebel_crackdown.txt, rebel_crackdown]

## 4. 終盤：絶対主義〜革命（1637〜）

### 維持と仕上げ

- [ ] 進歩「改善された統合」を研究したら、征服地の統合は内閣アクション「地域の統合」で行う {#late-integrate-area}
  - なぜ: この進歩を研究すると「州の統合」は使えなくなり、地域単位の「地域の統合」に置き換わる。進歩は「立憲主義」の次 [src: integrate_province.txt, integrate_province] [src: integrate_area.txt, integrate_area] [src: 3_cabinet_actions_unlocks.txt, integrate_area_advance]
- [ ] 進歩「統制力の広範な強化」を研究したら、平均支配度が95%未満の地域に、内閣アクション「地域支配を強化」を実行する {#late-control-area}
  - なぜ: 「州支配を強化」より広い範囲に効き、支配度の上限の引き上げ幅も大きい。ただし毎月の上昇は遅い。数値は7章 [src: increase_control_area.txt, increase_control_area] [src: increase_control.txt, increase_control_province] [src: 0_age_of_absolutism.txt, increase_control_area_advance]
- [ ] 進歩「緊張の緩和」を研究したら、他国の敵対心が残っているとき内閣アクション「懸念の軽減」を実行する {#late-alleviate}
  - なぜ: 敵対心は他国の評価を下げ、外交に消極的にさせるが、時間とともに薄れる（公式の説明）。このアクションは敵対心の減少を毎月速める [src: game_concepts_l_japanese.yml, game_concept_antagonism_desc] [src: government_l_japanese.yml, alleviate_concerns_desc] [src: alleviate_concerns.txt, alleviate_concerns]
- [ ] 閣僚ポストに空きがあり急ぎのアクションがないときは、内閣アクション「州の開発」で開発度を伸ばしたい州を選んで実行する {#late-develop}
  - なぜ: 開発度が高いほど多くの人が住め、土地の利用価値も高まる（公式の説明）。急務がないときの実行が勧められている [src: game_concepts_l_japanese.yml, game_concept_development_desc] [src: government_l_japanese.yml, develop_province_desc] [src: develop_province.txt, develop_province]

### 進歩の取り方

- [ ] 「進歩」パネルで、君主力を大きく増やす進歩（絶対主義は「絶対的支配者」、革命は「国家」）と、閣僚ポストを増やす進歩（「忠実な従属者」「現代的代表制度」）を優先して研究する {#late-adv-crown}
  - なぜ: 君主力は、絶対主義に進むと進歩によって顕著に増える（公式の説明） [src: game_concepts_l_japanese.yml, game_concept_crown_power_desc] [src: 0_age_of_absolutism.txt, absolute_rulership] [src: 0_age_of_revolutions.txt, crown_power_advance_revolutions]
- [ ] 「進歩」パネルで、政府改革保有数や官僚機構のスロットが増える進歩（絶対主義は「立憲主義」、革命は「権力の分離」「現代的官僚制度」）を研究する {#late-adv-reform}
  - なぜ: 公式ヒントは可能なかぎりの政府改革を実施すべきとしている [src: hints_l_japanese.yml, hint_has_possible_reform_hint_text_1] [src: 0_age_of_absolutism.txt, the_constitution] [src: 0_age_of_revolutions.txt, modern_bureaucracy]
- [ ] 進歩「近代的街道」「鉄道」を研究したら、街道ビルダーで主要な街道をアップグレードする {#late-road-upgrade}
  - なぜ: 近接性の補正は街道の種別が上がるほど大きい [src: 00_generic.txt, railroad] [src: 3_road_unlocks.txt, modern_road_advance]

### 崩れの予防

- [ ] 絶対主義の時代に入ったら、「従属国の管理」パネルで従属国忠誠度が基準に近い従属国がないか確認し、あれば外交アクション「評価改善」を実行する {#late-subjects-age}
  - なぜ: 従属国忠誠度は絶対主義で下がり、革命でさらに下がる。数値は7章 [src: 00_default.txt, age_5_absolutism] [src: 00_default.txt, age_6_revolutions]
- [ ] 革命の時代に制度「啓蒙」を受容したら、「政府」パネルの「国家」タブにある「階級」タブで庶民と市民の満足度を確認し、下回りそうなら課税を下げるか特権を見直す {#late-revolution}
  - なぜ: 啓蒙を受容した国は、庶民と市民の満足度がともに基準を下回ると国難「革命！」の対象になりうる（ほかに識字率や列強などの条件あり）。始まると安定度投資に大きなペナルティがつく。基準は7章 [src: revolution_disaster.txt, can_start] [src: revolution_disaster.txt, stability_investment]

## 5. 定期ルーチン {.routine}

### 毎年

- [ ] 「経済」パネルの「収支」タブで月間収支を確認し、マイナスなら税や支出を調整して黒字に戻す {#yearly-balance}
  - なぜ: マイナスのままだと負債や破産につながる（公式の説明） [src: scripted_hints.txt, hint_in_deficit] [src: hints_l_japanese.yml, hint_in_deficit_hint_text_1]
- [ ] 安定度を確認し、0以下なら「経済」パネルで安定度投資を増やす {#yearly-stability}
  - なぜ: 0以下でヒントが出て、-50以下は深刻とされる。数値は7章 [src: scripted_hints.txt, hint_low_stability] [src: scripted_hints.txt, hint_very_low_stability] [src: economy_lateralview.gui, MODIFIER_TYPE_NAME_stability_investment]
- [ ] 「政府」パネルの「国家」タブにある「階級」タブで各階級の満足度を確認し、50%未満の階級があれば特権を見直すか課税を下げる {#yearly-estates}
  - なぜ: 25%未満になった階級は召集軍を提供しなくなる。数値は7章 [src: 00_defines.txt, LOW_SATISFACTION_THRESHOLD] [src: 00_defines.txt, ESTATE_LEVY_SATISFACTION_THRESHOLD] [src: hints_l_japanese.yml, hint_estates_hint_text_1]
- [ ] 「進歩」パネルで進行中の研究を確認し、無いか上限が間近なら次の進歩を選ぶ {#yearly-research}
  - なぜ: 研究ポイントは上限までしか貯まらず、超えた分は無駄になる（公式の説明） [src: hints_l_japanese.yml, hint_can_do_more_research_hint_text_3]
- [ ] 「内閣」タブで閣僚ポストの埋まり具合を確認し、空きがあればキャラクターを割り当てる {#yearly-cabinet}
  - なぜ: 内閣アクションは適切なキャラクターがいないと効率よく働かない（公式の説明） [src: hints_l_japanese.yml, hint_lack_cabinet_for_cabinet_action_hint_text_1]
- [ ] 「投入物資不足の建設」「投入物資不足の建造物」のアラートが出たら、アラートから不足する交易品のRGOか建造物を増やすか、他の市場から輸入する {#yearly-input}
  - なぜ: 物資が足りないと、建設は中断され、建造物は生産量が減る（公式の説明） [src: hints_l_japanese.yml, hint_has_constructions_missing_input_hint_text_1] [src: hints_l_japanese.yml, hint_has_buildings_missing_input_hint_text_1] [src: hints_l_japanese.yml, hint_address_shortage_text]

### 10年ごと

- [ ] 同盟国に、弱すぎて自国を無関係の戦争に巻き込みかねない国がないか見直す {#decade-alliance}
  - なぜ: 弱すぎる国との同盟は、無関係の戦争で敗戦国になる原因になる（公式の説明）。破棄すると相手の評価と信頼度が下がるので慎重に。数値は7章 [src: hints_l_japanese.yml, hint_no_allies_hint_text_3] [src: 00_opinion_hardcoded.txt, opinion_broke_alliance] [src: 04_trust_hardcoded.txt, trust_broke_alliance]
- [ ] 「交易」パネルで、赤字の交易路がないか確認し、戦略上不要なら廃止して黒字の交易路に置き換える {#decade-trade}
  - なぜ: 建設用の木材や食糧の供給路など、戦略上重要な物資なら赤字でも意味がある（公式の説明） [src: hints_l_japanese.yml, hint_unprofitable_trade_route_hint_text_1] [src: hints_l_japanese.yml, hint_unprofitable_trade_route_hint_text_2]
- [ ] 安定度が高いときに、「階級」タブで最も強力な階級の特権を見直す {#decade-privileges}
  - なぜ: 階級の権力のぶんだけ君主力が下がる。ただし特権を剥奪された階級は不満を抱くので、満足度を確認する（公式の説明） [src: hints_l_japanese.yml, hint_estates_hint_text_2] [src: hints_l_japanese.yml, hint_crown_power_hint_text_2]

### 時代が変わったとき

- [ ] 時代の始まりのイベントで、「統治フォーカス」「外交フォーカス」「軍事フォーカス」の説明にある進歩を見比べ、この時代の方針に合う1つを選ぶ {#age-focus}
  - なぜ: 選んだフォーカスが、その時代の自国の進歩ツリーを決める。選ばなかったフォーカス専用の進歩は、その時代には現れない [src: game_concepts_l_japanese.yml, game_concept_age_lower_desc] [src: ages.txt, ages_of_eu.1] [src: 4_choices_adm.txt, innovativeness] [src: effects_l_japanese.yml, WE_SET_AGE_PREFERENCE_EFFECT]
- [ ] 「進歩」パネルで、新しい時代のツリーから研究する進歩を選ぶ {#age-research}
  - なぜ: 各時代に独自の進歩ツリーがある [src: game_concepts_l_japanese.yml, game_concept_age_upper_desc]
- [ ] 「政府」パネルの「国家」タブにある「法律」タブで、新しく解禁された法律とポリシーを確認し、空いているポリシーを設定する {#age-laws}
  - なぜ: 時代が進むと多くの新しい法律とポリシーが解禁される。ポリシーが空のままだと恩恵を逃すが、ダカットと安定度を使えばいつでも変更できる（公式の説明） [src: hints_l_japanese.yml, hint_has_possible_law_hint_text_1] [src: hints_l_japanese.yml, hint_has_possible_law_hint_text_3]
- [ ] 「内閣」タブで、新しく解禁された内閣アクションがないか確認する {#age-cabinet}
  - なぜ: 時代が進むと新たな内閣アクションが解禁される（公式の説明） [src: hints_l_japanese.yml, hint_has_possible_cabinet_action_hint_text_3]
- [ ] 新しい連隊タイプを解禁する進歩を研究したら、友好的なロケーションにいる陸軍へ「陸軍の強化」を実行する {#age-upgrade-army}
  - なぜ: 強化すると現在の士気が0になり、召集軍と傭兵は強化できない（公式の説明）。連隊タイプには上位の連隊タイプが定められている [src: 2_army_unlocks.txt, unlock_halberdiers_advance] [src: 2_unlocked_through_tech.txt, a_men_at_arms] [src: units_l_japanese.yml, UPGRADE_ARMY_INFO_NO] [src: units_l_japanese.yml, UPGRADE_ARMY_LEVIES_ARE_RUBBISH] [src: units_l_japanese.yml, UPGRADE_ARMY_MERCS_ARENT_YOURS]
- [ ] 新しい船のタイプを解禁する進歩を研究したら、自国か従属国の港にいる海軍へ「海軍の強化」を実行する {#age-upgrade-navy}
  - なぜ: 強化すると現在の士気が0になり、召集軍は強化できない（公式の説明）。船のタイプにも上位のタイプが定められている [src: 2_ship_unlocks.txt, unlock_carrack_advance] [src: navy_heavy_ship.txt, n_early_carrack] [src: units_l_japanese.yml, UPGRADE_FLEET_NOT_IN_OWNED_PORT] [src: units_l_japanese.yml, UPGRADE_FLEET_INFO_NO] [src: units_l_japanese.yml, UPGRADE_FLEET_LEVIES_ARE_RUBBISH]

### 戦争の前と後

- [ ] 宣戦布告の前に、相手と停戦中でないか確認する {#war-truce}
  - なぜ: 停戦中の相手に宣戦布告すると、厳しい罰則が科される（公式の説明） [src: game_concepts_l_japanese.yml, game_concept_truce_desc]
- [ ] 宣戦布告の前に、「経済」パネルで陸軍維持費の戦争開始時の自動増額を有効にするか、維持費を上げておく {#war-maintenance}
  - なぜ: 維持費をかけないと士気と兵の有効性が下がる（公式の説明）。戦争中に低いままだと「少ない陸軍維持費」のアラートが出る [src: game_concepts_l_japanese.yml, game_concept_army_maintenance_desc] [src: 00_default.txt, has_low_army_maintenance] [src: interfaces_l_japanese.yml, TOGGLE_AUTO_ARMY_MAINTENANCE_TOOLTIP_OFF_TT] [src: economy_lateralview.gui, AutoRaiseMaintenanceAtWar]
- [ ] 戦争が始まったら、開戦事由の戦争目標を確認し、達成に向けて軍を動かす {#war-goal}
  - なぜ: 戦争目標の達成が戦勝点を生み、有利な和平条約に欠かせない。ほかに首都の占領・請求権をもつロケーションの支配・要塞の占領・敵軍の撃破・港の封鎖でも戦勝点を稼げる（公式の説明） [src: hints_l_japanese.yml, hint_war_hint_text_2]
- [ ] 「和平の呼びかけ」のアラートが出たら、「和平条約」パネルで要求を減らし、戦争疲弊が致命的になる前に署名する {#war-peace}
  - なぜ: 早めの署名で失ったものは、将来の別の戦争で取り戻せる（公式の説明） [src: hints_l_japanese.yml, hint_call_for_peace_hint_text_2] [src: hints_l_japanese.yml, hint_call_for_peace_hint_text_3]
- [ ] 「平時の召集陸軍動員」「平時の召集海軍動員」のアラートが出たら、召集軍を解散する {#war-disband}
  - なぜ: 動員中は募集元のPOPが減り、解散すると生き残った者はPOPに戻る（公式の説明） [src: game_concepts_l_japanese.yml, game_concept_army_levy_desc] [src: interfaces_l_japanese.yml, DISBAND_ALL_LEVIES]
- [ ] 「追放状態の陸軍」のアラートが出たら、その陸軍を自国へ帰還させる {#war-exiled}
  - なぜ: 追放状態の陸軍は、自国へ戻るまで再び戦えない（公式の説明） [src: alerts_l_japanese.yml, ALERT_EXILED_UNITS]
- [ ] 「停戦協定がまもなく終了」のアラートが出たら、期限までに軍の編成と同盟関係を確認する {#war-truce-end}
  - なぜ: 停戦が終わると、再び宣戦布告されるかもしれない（公式の説明） [src: alerts_l_japanese.yml, ALERT_TRUCE_EXPIRES]

## 6. 困ったとき

**飢饉の州が出ている（「飢饉の州」「飢饉の危機にある州」）**
- 見る場所: 「市場」パネルの「食糧」ボタンから開く「食糧生産」パネルで、飢饉の危険がある州 [src: 00_default.txt, has_starving_provinces] [src: hints_l_japanese.yml, hint_food_hint_text_2]
- 打ち手: その州のRGOを拡大するか、別の市場から食糧を輸入する。冬は食糧生産が減るので、数ヵ月のマイナスで慌てない（公式の説明） [src: hints_l_japanese.yml, hint_food_hint_text_2] [src: hints_l_japanese.yml, hint_food_hint_text_3]

**軍の兵が減り続ける（「食糧不足」「深刻な食糧不足」）**
- 見る場所: アラートに並ぶ、食糧が不足している陸軍の一覧 [src: 00_default.txt, has_army_with_very_low_food] [src: alerts_l_japanese.yml, ALERT_VERY_LOW_FOOD]
- 打ち手: 消耗の主因である食糧切れ・場所の供給限界の超過・冬や地形から、軍を外す（公式の説明） [src: game_concepts_l_japanese.yml, game_concept_attrition_desc]

**従業員が足りない建造物やRGOがある（「従業員不足の建造物」「従業員不足のRGO」）**
- 見る場所: 「ロケーション」パネルの「人口統計」タブにあるPOP昇格速度 [src: 00_default.txt, lack_pop_promotion_to_fill_buildings] [src: hints_l_japanese.yml, hint_lack_pop_promotion_to_fill_buildings_hint_text_3]
- 打ち手: 従業員が足りない場所に新しい建造物を建てず、安定度・識字率・支配度を上げる。重要な場所には図書館と大学を建てる（公式の説明） [src: hints_l_japanese.yml, hint_lack_pop_promotion_to_fill_buildings_hint_text_2]

**POPの必需品が足りない（「満たされないPOP」）**
- 見る場所: アラートに並ぶ、不足している交易品とその市場 [src: 00_default.txt, has_pop_needs] [src: alerts_l_japanese.yml, ALERT_POPS_WITH_NEEDS_ENTRY]
- 打ち手: 「交易品生産」パネルから不足品のRGOや建造物を増やすか、別の市場から輸入する。反乱に向かっていなければ過度に心配しない（公式の説明） [src: hints_l_japanese.yml, hint_pops_with_needs_yellow_hint_text_2] [src: hints_l_japanese.yml, hint_pops_with_needs_yellow_hint_text_3]

**原因の分からないペナルティが付いている（「ペナルティが有効」）**
- 見る場所: アラートに並ぶ、補正ごとの効果と有効な理由 [src: 00_default.txt, static_modifier_active] [src: alerts_l_japanese.yml, ALERT_STATIC_MODIFIER_ENTRY]
- 打ち手: 有効な理由に挙がった条件を解消する（公式の説明）

**従属国が独立戦争を起こしそうだ（「差し迫る独立戦争」）**
- 見る場所: アラートに並ぶ従属国と、「従属国の管理」パネル [src: 00_default.txt, has_imminent_independence_war] [src: alerts_l_japanese.yml, ALERT_HAS_IMMINENT_INDEPENDENCE_WAR]
- 打ち手: 陸軍を増やして相手の勝利の推定確率を下げるか、従属国忠誠度が50未満なら開戦事由「不忠の従属国」で先制するか、従属国忠誠度を改善する（公式の説明）。数値は7章 [src: hints_l_japanese.yml, hint_has_imminent_independence_war_hint_text_2] [src: disloyal_subject.txt, cb_disloyal_subject]

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|
| 時代の開始年 | ルネサンス1342／発見1437／宗教改革1537／絶対主義1637／革命1737 | [src: 00_default.txt, age_2_renaissance 〜 age_6_revolutions] |
| ゲーム開始日 | 1337年4月1日 | [src: 00_defines.txt, START_DATE] |
| 安定度 | 0以下で対処を始める／-50以下は深刻 | [src: scripted_hints.txt, hint_low_stability] [src: scripted_hints.txt, hint_very_low_stability] |
| 政府力（正統性など） | 50未満で「政府の強化」を検討する | [src: scripted_hints.txt, hint_low_legitimacy] |
| 階級の満足度 | 50%未満は不満（ペナルティ側）／25%未満の階級は召集軍を提供しなくなる | [src: 00_defines.txt, LOW_SATISFACTION_THRESHOLD] [src: scripted_hints.txt, hint_unhappy_estates] [src: 00_defines.txt, ESTATE_LEVY_SATISFACTION_THRESHOLD] |
| 人的資源 | 20%以下なら正規兵で戦う宣戦を控える | [src: scripted_hints.txt, hint_manpower] |
| 州の支配度 | 95%未満の州が「州支配を強化」の対象。「地域支配を強化」は地域の平均支配度が95%未満 | [src: 00_defines.txt, LOW_CONTROL_THRESHOLD_FOR_BEST_TAX] [src: increase_control.txt, increase_control_province] [src: increase_control_area.txt, increase_control_area] |
| ランクの昇格条件 | 公国：威信25・総人口200／王国：威信50・総人口2000／帝国：列強・威信70・総人口10000（総人口は千人単位。代わりに、主要宗教の人口が公国150・王国1500・帝国7500、受容文化の人口が公国100・王国1000・帝国5000でもよい）。帝国はさらに、カトリック（ローマ自身を除く）は教皇の国ローマからの評価が100超であること、HRE（神聖ローマ帝国）の加盟国でないこと、カトリックはHREが存在しないことが必要。王国もHRE加盟国はゲームルール「神聖ローマ帝国のランク制限」の設定で制限される | [src: country_triggers.txt, can_upgrade_country_rank_duchy] [src: country_triggers.txt, can_upgrade_country_rank_kingdom] [src: country_triggers.txt, can_upgrade_country_rank_empire] [src: 00_default.txt, rank_empire] [src: christian.txt, block_from_change_to_empire_rank_catholic] [src: hre.txt, block_from_change_to_empire_rank] [src: hre.txt, block_from_change_to_kingdom_rank] |
| 国難「慢心による衰退」 | 帝国を15年以上保持し、安定度0未満かつ首都がある地方の平均支配度が発見45%・宗教改革50%・絶対主義55%・革命60%未満（または受容文化・容認文化のどちらでもない文化の人口が総人口の3分の1超） | [src: decline_of_empire.txt, can_start] [src: _hardcoded.txt, recently_became_empire_variable] |
| 同盟の破棄 | 相手の評価−50・信頼度−15（どちらも毎年1回復）。相互に停戦が成立する | [src: 00_opinion_hardcoded.txt, opinion_broke_alliance] [src: 04_trust_hardcoded.txt, trust_broke_alliance] [src: alliance.txt, cancel_effect] |
| 従属国忠誠度 | 50未満で不忠（開戦事由「不忠の従属国」も50未満の従属国に使える）。時代補正は絶対主義−10／革命−30 | [src: 00_defines.txt, TOO_DISLOYAL_THRESHOLD] [src: disloyal_subject.txt, cb_disloyal_subject] [src: 00_default.txt, age_5_absolutism] [src: 00_default.txt, age_6_revolutions] |
| 国難「革命！」の引き金 | 啓蒙を受容した国で、庶民と市民の満足度がともに35%未満 | [src: revolution_disaster.txt, can_start] |
| 専門化の都市特権 | 指定品の生産+20〜30%、生産効率−5%、付与に政治的影響力20 | [src: 01_discovery.txt, royal_tooling_rights] [src: 01_discovery.txt, royal_textile_rights] [src: default_values.txt, town_right_efficiency_penalty] [src: 00_hardcoded.txt, grant_town_rights] |
| 地方総督府 | 近接性の供給源80。建設できる数は基本1で、進歩と王国・帝国のランクで増える。首都との街道が必要 | [src: capital_buildings.txt, local_governor] [src: country.txt, country_base_values] [src: 1_building_unlocks.txt, local_governor_advance] [src: 00_default.txt, rank_kingdom] [src: 00_default.txt, rank_empire] |
| 支配度強化の内閣アクション | 州版は上限+0.10・毎月+0.01、地域版は上限+0.15・毎月+0.005 | [src: increase_control.txt, increase_control_province] [src: increase_control_area.txt, increase_control_area] |

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

- 内閣（Cabinet）／内閣アクション（Cabinet Action）
- 国家の安定化（Stabilize Country）／政府の強化（Strengthen Government）／州支配を強化（Increase Province Control）／州の統合（Integrate Province）／制度の推進（Foster Institutions）
- 安定度（Stability）／安定度投資（Stability Investment）／政府力（Government Power）／正統性（Legitimacy）／共和的伝統（Republican Tradition）／献身（Devotion）／遊牧民の結束（Horde Unity）／部族の団結（Tribal Cohesion）
- 階級（Estate）／王室（Crown）／満足度（Satisfaction）／特権（Privilege）／君主力（Crown Power）
- 政府改革（Government Reform）／法律（Law）／ポリシー（Policy）
- 収支（Balance）／貨幣鋳造（Minting）／インフレ（Inflation）／税基盤（Tax Base）
- 制度（Institution）／受容（Embrace）／進歩（Advance）／時代（Age）
- 支配度（Control）／近接性（Proximity）／街道（Road）／ロケーション（Location）／中核地（Core）／首都（Capital）
- 開戦事由（Casus Belli）／州の請求（Claims on Province）／戦争疲弊（War Exhaustion）／人的資源（Manpower）／指揮官（Commander）／同盟（Alliance）／外交アクション（Diplomatic Action）
- 文化許容量（Cultural Capacity）／交易許容量（Trade Capacity）／外交許容量（Diplomatic Capacity）／食糧（Food）／RGO（Resource Gathering Operations）／ミッション（Mission）／「自動化」パネル（Automation Panel）／アジェンダ（Agenda）
- 国家ランク（Country Rank）／公国（Duchy）／王国（Kingdom）／帝国（Empire）／ライバル（Rival）／威信（Prestige）／政治的影響力（Political Influence）／庶民（Commoners）／市民（Burghers）／列強（Great Power）／神聖ローマ帝国（Holy Roman Empire）／ローマ（Rome。教皇の国）／受容文化（Accepted Culture）／容認文化（Tolerated Culture）
- 国難（Disaster）／慢心による衰退（Decline of Empire）／革命！（Revolution!）／繁栄度（Prosperity）／反乱軍の弾圧（Rebel Crackdown）／復興への取り組み（Recovery Effort）／戦争疲弊を軽減（Reduce War Exhaustion）
- 従属国（Subject）／従属国忠誠度（Subject Loyalty）／不忠の従属国（Disloyal Subject）／評価改善（Improve Opinion）／召集軍（Levy）／官僚機構（Bureaucracy）／都市特権（Urban Rights）／自治区特権（Borough Privileges）／啓蒙（Enlightenment）
- 舗装路（Paved Road）／近代的街道（Modern Road）／鉄道（Railroad）
- 地方（Region）／地域（Area）／都（City）／開発度（Development）／敵対心（Antagonism）／評価（Opinion）
- 地方総督府（Local Governor）／地域の統合（Integrate Area）／地域支配を強化（Increase Area Control）／州の開発（Develop Province）／懸念の軽減（Alleviate Concerns）／POPを我々の文化に同化させる（Assimilate Pops into our Culture）
- 統治フォーカス（Administrative Focus）／外交フォーカス（Diplomatic Focus）／軍事フォーカス（Military Focus）／閣僚ポスト（Cabinet Seat。進歩や補正の表示では「閣僚議席」）／外交評判（Diplomatic Reputation）／信頼度（Trust）
- 陸軍（Army）／海軍（Navy）／連隊（Regiment）／士気（Morale）／召集陸軍（Army Levy）／陸軍維持費（Army Maintenance）／陸軍の強化（Upgrade Army）／海軍の強化（Upgrade Navy）／追放（Exiled）／消耗（Attrition）／供給限界（Supply Limit）
- 停戦（Truce）／和平条約（Peace Treaty）／戦争目標（Wargoal）／戦勝点（Warscore）／傭兵（Mercenary）／要塞（Fort）／封鎖（Blockade）
- 市場（Market）／交易（Trade）／交易品（Goods）／建造物（Building）／州（Province）／飢饉（Starvation）／昇格（Promotion）／識字率（Literacy）／図書館（Library）／大学（University）／ダカット（Ducats）／POP（Pop）
- 時代名：伝統（Traditions）／ルネサンス（Renaissance）／発見（Discovery）／宗教改革（Reformation）／絶対主義（Absolutism）／革命（Revolutions）
- 進歩名：国政術（Statecraft）／初期行政能力（Early Administrative Capacity）／信仰属地主義（'Cuius Regio, Eius Religio'）／近世の統治（Early Modern Administration）／初期行政改革（Early Administrative Reformation）／君主（The Prince）／執行官僚制度（Executive Bureaucracy）／絶対的支配者（Absolute Rulership）／忠実な従属者（Loyal Subordinates）／立憲主義（The Constitution）／国家（Nation）／現代的代表制度（Modern Representation）／権力の分離（Separation of Powers）／現代的官僚制度（Modern Bureaucracy）／改善された統合（Better Integration）／統制力の広範な強化（Increase Control Widely）／緊張の緩和（Deflating Tensions）

## 9. 出典

### 一次情報（ゲームスクリプト）

- `in_game/common/age/00_default.txt`（時代の開始年）
- `loading_screen/common/defines/00_defines.txt`（開始日、階級の不満の閾値、階級が召集軍を提供する閾値、支配度の閾値）
- `in_game/common/tutorial_lessons/00_tutorial_lesson_basics.txt`、`00_tutorial_lesson_admin.txt`、`00_tutorial_lesson_diplomacy.txt`、`00_tutorial_lesson_military.txt`（公式の手順）
- `in_game/common/alert_descriptions/00_default.txt`（アラートの種類）
- `in_game/common/scriptable_hints/scripted_hints.txt`（ヒントの発動条件）
- `in_game/common/cabinet_actions/stabilize_country.txt`、`strengthen_government.txt`、`increase_control.txt`、`integrate_province.txt`、`study_institutions.txt`（内閣アクション）
- `in_game/common/prices/00_hardcoded.txt`（制度の受容コスト）
- `in_game/common/casus_belli/conquest.txt`（「州の請求」の開戦事由）
- `in_game/gui/economy_lateralview.gui`（安定度投資・陸軍維持費の置き場所）
- `in_game/common/country_ranks/00_default.txt`、`scripted_triggers/country_triggers.txt`（ランクの効果と昇格条件）
- `in_game/common/disasters/decline_of_empire.txt`、`revolution_disaster.txt`、`on_action/_hardcoded.txt`（国難の発生条件）
- `in_game/common/advances/0_age_of_discovery.txt`、`0_age_of_reformation.txt`、`0_age_of_absolutism.txt`、`0_age_of_revolutions.txt`、`3_road_unlocks.txt`（枠を増やす進歩、街道の解禁）
- `in_game/common/road_types/00_generic.txt`、`town_rights/01_discovery.txt`、`main_menu/common/script_values/default_values.txt`（街道・都市特権の効果）
- `in_game/common/cabinet_actions/reduce_war_exhaustion.txt`、`recovery_effort.txt`、`rebel_crackdown.txt`、`auto_modifiers/country.txt`（内閣アクション、戦争疲弊の自然減）
- `in_game/gui/alertmanager.gui`（アラートのクリック先）
- `in_game/common/cabinet_actions/promote_culture.txt`、`integrate_area.txt`、`increase_control_area.txt`、`alleviate_concerns.txt`、`develop_province.txt`（本格拡大・終盤の内閣アクション）
- `in_game/common/building_types/capital_buildings.txt`、`in_game/common/advances/1_building_unlocks.txt`、`3_cabinet_actions_unlocks.txt`（地方総督府、内閣アクションを解禁する進歩）
- `in_game/common/religions/christian.txt`、`in_game/common/international_organizations/hre.txt`（帝国化・王国化の禁止条件）
- `in_game/events/ages.txt`、`in_game/common/advances/4_choices_adm.txt`（`4_choices_dip.txt`、`4_choices_mil.txt` も同形式）（時代の始まりのフォーカス選択と、フォーカスごとの進歩）
- `in_game/common/advances/2_army_unlocks.txt`、`2_ship_unlocks.txt`、`in_game/common/unit_types/2_unlocked_through_tech.txt`、`navy_heavy_ship.txt`（連隊・船のタイプの解禁と上位タイプ）
- `in_game/common/casus_belli/disloyal_subject.txt`（開戦事由「不忠の従属国」の条件）
- `in_game/common/biases/00_opinion_hardcoded.txt`、`04_trust_hardcoded.txt`、`in_game/common/scripted_relations/alliance.txt`（同盟を破棄したときの評価・信頼度の減点と停戦）
- `main_menu/localization/japanese/tutorial_l_japanese.yml`、`hints_l_japanese.yml`、`game_concepts_l_japanese.yml`、`advances_l_japanese.yml`、`interfaces_l_japanese.yml`、`government_l_japanese.yml`、`modifier_types_l_japanese.yml`、`alerts_l_japanese.yml`、`units_l_japanese.yml`、`effects_l_japanese.yml`（公式の説明文）

### コミュニティ情報

- eu5.paradoxwikis.com/Country_rank（総人口の単位が千人であることをスクリプトの値と照合）
- eu5.paradoxwikis.com/Age（時代ごとの従属国忠誠度の値をスクリプトと照合）
