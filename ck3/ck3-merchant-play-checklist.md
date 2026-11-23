# CK3 プレイ中チェックリスト：交易商人
> 対象パッチ: 1.21.0.3（ビルド 26785313） ／ 最終確認日: 2026-11-23

交易商人として遊ぶときの「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。Silk & Silver が必要（無いと交易商人は操作できず、開始ブックマークも選べない）。ほかの DLC はすべてある前提で書き、要る項目には「（DLC名 が必要）」と付ける。「（公式の説明）」は、ゲーム内の助言・チュートリアル・用語説明が根拠で、効果をスクリプトでは確かめていない記述。 [src: 00_rules.txt, GAME_OVER_CANNOT_PLAY_MERCHANT] [src: 00_bookmarks.txt, bm_1066_merchants]

## 1. 開始直後（ポーズ中にやること）

- [ ] 自分のキャラクター画面で、政体名が「交易商人」かを確かめる {#start-gov}
  - なぜ: 交易商人は所領なしで操作でき、本拠地は商会になる。途中からは決断「交易商人になる」でなれる [src: 00_government_types.txt:1559] [src: 00_government_types.txt:1569] [src: gdp_merchant_decisions.txt, become_merchant_decision]
- [ ] 「領国」画面の「概要」タブで、商会規模・本拠地・商会方針を確かめる {#start-overview}
  - なぜ: プレイヤーは方針「交易担当者」、規模「新興事業」から始まる。方針が「交易担当者」のままだと通知が出る [src: game_start.txt:6535] [src: game_start.txt:6546] [src: merchant_actions.txt:268] [src: window_my_realm.gui:355]
- [ ] 商会方針を「職人」「金貸し」「隊商長」に変えるかを決める {#start-purpose}
  - なぜ: 「交易担当者」からの変更は無料、ほかの方針からは威信500。変えると5年は変えられない。方針の違いは7章 [src: 00_realm_laws.txt:3921] [src: 00_realm_laws.txt:22] [src: 00_realm_laws.txt:5]
- [ ] 「領国」画面の「後援者」タブで、後援者と従属商人契約の税率を確かめる {#start-patron}
  - なぜ: 後援者は本拠地のある領地の支配者で、交易の収入の一部を納める（既定は低税率10%）。契約は本拠地を移さない限り破棄できない（公式の説明） [src: merchant.txt:16] [src: merchant.txt:20] [src: window_my_realm.gui:376] [src: gdp_game_concepts_l_japanese.yml, game_concept_client_contract_desc]
- [ ] 後援者に「契約の変更を要求」で、交易支援か婚姻支援を求めるかを決める {#start-contract}
  - なぜ: 交易支援は競争力+15%、婚姻支援は縁談の受諾+25。代わりに後援者の威信が月0.15減る [src: merchant.txt:170] [src: merchant.txt:174] [src: merchant.txt:209] [src: gdp_merchant_values.txt:90] [src: 00_modifiy_vassal_contract.txt, subject_modify_tributary_contract_interaction]
- [ ] 「交易」画面の「交易路」タブで「交易路を作成」を押し、余剰のある市場と需要のある市場を結ぶ {#start-route}
  - なぜ: 営利交易路が金の主な稼ぎ口。最初は1本・市場3つ・交易品1つまで（公式の説明） [src: 00_defines.txt:2006] [src: 00_defines.txt:2011] [src: 00_defines.txt:2014] [src: window_trade.gui:546] [src: gdp_reactive_advice_l_japanese.yml, reactive_advice_trade_route_planner_adding_markets_desc]
- [ ] 交易路に商会員を交易担当者として割り当て、任務を選ぶ {#start-trader}
  - なぜ: 任務は「取引を交渉」（交易知識の伸び）、「競争を管理」（競争力）、「隊商を監督」（輸送量）。技能が高いほど効果が大きい（7章） [src: 00_trade_tasks.txt:5] [src: 00_trade_tasks.txt:24] [src: 00_trade_tasks.txt:44]
- [ ] 所持金がマイナスでないか確かめる {#start-debt}
  - なぜ: 所持金−50未満が12か月続くと商会の洞察力が500減り、その後も6か月ごとに風土が拝金主義側へ5動く [src: gdp_merchant_values.txt:1018] [src: gdp_merchant_values.txt:1020] [src: gdp_merchant_values.txt:1021] [src: gdp_merchant_values.txt:1026] [src: gdp_merchant_values.txt:1027] [src: gdp_merchant_on_actions.txt:385]
- [ ] 「家」画面の「風土」タブで、商会方針（風土）の段階を確かめる {#start-sentiment}
  - なぜ: 最初は「中庸」。貴族の家と婚姻すると「貴族化」側、交易商人と婚姻すると「拝金主義」側に傾く（公式の説明）。段階の効果は7章 [src: 00_house_unities.txt:224] [src: house_view_l_japanese.yml, COMPANY_DIRECTION_TAB_BUTTON] [src: gdp_reactive_advice_l_japanese.yml, reactive_advice_company_direction_panel_desc]

## 2. 交易の基盤づくり

- [ ] 交易路の交易品は、余剰の市場で安く買い、需要の高い市場で高く売れる組み合わせにする {#base-margin}
  - なぜ: 営利交易路の利益は購入価格と販売価格の差（公式の説明） [src: gdp_game_concepts_l_japanese.yml, game_concept_profit_route_desc]
- [ ] ほかの交易商人が多い市場では、自分の競争力と比べてから交易路に入れる {#base-competition}
  - なぜ: 同じ交易品を扱う交易路の中で競争力の合計が高いほど、市場占有率（取引できる量）が上がる。競争力の初期値は10（公式の説明） [src: 00_defines.txt:2003] [src: gdp_game_concepts_l_japanese.yml, game_concept_trade_competitiveness_desc]
- [ ] 主要交易品（交易路の一番左の交易品）を、伸ばしたい商品カテゴリーの品にする {#base-primary}
  - なぜ: 交易知識は主要交易品のカテゴリーにだけ貯まる。月15、150ごとにレベルが上がり、扱わないカテゴリーは月15ずつ減る [src: 00_defines.txt:2046] [src: 00_defines.txt:2047] [src: 00_defines.txt:2048] [src: gdp_game_concepts_l_japanese.yml, game_concept_primary_good_desc]
- [ ] 主要交易品のカテゴリーを、商会方針が交易知識を+20%伸ばすカテゴリーにそろえる {#base-category}
  - なぜ: 「職人」「金貸し」「隊商長」は方針ごとに得意なカテゴリーがある。「交易担当者」は全カテゴリーで+10%（7章） [src: 00_realm_laws.txt:3954] [src: 00_realm_laws.txt:4018]
- [ ] 本拠地で主要建物を「荘園邸宅」に建て替える {#base-manor}
  - なぜ: 営利交易路の上限が1本増え、交易路の長さも+2。費用は金100・威信250、工期365日 [src: 00_merchant_company_buildings.txt:116] [src: 00_merchant_company_buildings.txt:117] [src: gdp_domicile_values.txt:3] [src: gdp_domicile_values.txt:19] [src: 00_merchant_company_buildings.txt:9]
- [ ] 交易担当者の任務を、交易路の弱点に合わせて付け替える {#base-task}
  - なぜ: 競り負けている交易路は「競争を管理」、輸送量が上限の交易路は「隊商を監督」が効く [src: 00_trade_tasks.txt:15] [src: 00_trade_tasks.txt:52]
- [ ] 決断「交易機会を探し求める」を実行し、出た工作を成功させる {#base-opportunity}
  - なぜ: 交易担当者のいる交易路が要る。費用は威信75、待ちは2年。工作が失敗・中止されると機会も失敗する（公式の説明） [src: gdp_merchant_decisions.txt:997] [src: gdp_merchant_decisions.txt:1000] [src: gdp_merchant_decisions.txt:1013] [src: gdp_merchant_trade_opportunity_values.txt:4] [src: 00_basic_values.txt:1051] [src: gdp_game_concepts_l_japanese.yml, game_concept_trade_opportunity_desc]
- [ ] いる場所の領地で、決断「領分を訪れる」を実行する {#base-visit}
  - なぜ: 競争力の上昇、商会員の雇い入れ、金を威信に換える機会などが得られる。費用はかからない（公式の説明） [src: gdp_visit_holding_decision.txt, gdp_visit_holding_decision] [src: gdp_visit_holding_decision_event_l_japanese.yml, gdp_visit_holding_decision_tt]
- [ ] 商会方針が「隊商長」なら、特別契約を受けて遠方へ移動し、本拠地のアーティファクトを手に入れる {#base-luxury}
  - なぜ: 特別契約は「隊商長」の商人に毎年出ることがあり、決断「領分を訪れる」でも見つかる（公式の説明） [src: gdp_game_concepts_l_japanese.yml, game_concept_luxury_contract_desc]
- [ ] 後援者に「頼みごとをする」で、交易の特権を求める {#base-request}
  - なぜ: 受け入れられると本拠地の市場で競争力+15%が10年続く。費用は威信120（後援者が公爵なら240、王なら360）。同じ相手には8か月あける [src: 11_gdp_merchant_interactions.txt:702] [src: 11_gdp_merchant_interactions.txt:879] [src: 11_gdp_merchant_interactions.txt:880] [src: gdp_merchant_trade_opportunity_modifiers.txt:102] [src: gdp_merchant_values.txt:409] [src: 00_basic_values.txt:1052]
- [ ] 交易路の市場の持ち主に「市場税の特例を求める」 {#base-toll}
  - なぜ: 市場税は市場での販売すべてにかかり、軽いほど利益が大きい（公式の説明）。費用は威信150で、同じ相手には2年あける。金を出す・強いフックを使う選択肢もある [src: gdp_game_concepts_l_japanese.yml, game_concept_market_toll_desc] [src: 11_gdp_merchant_interactions.txt:9854] [src: 11_gdp_merchant_interactions.txt:9934] [src: 11_gdp_merchant_interactions.txt:9943] [src: 11_gdp_merchant_interactions.txt:9952]
- [ ] 委託交易路の依頼が来たら、受けるかを決める {#base-commission}
  - なぜ: 依頼主から報酬を受け、期間中は指定の交易品を指定の市場へ届ける。一度に持てるのは1本（公式の説明） [src: gdp_game_concepts_l_japanese.yml, game_concept_commission_route_desc]
- [ ] 方針契約が出たら、提示された問題に対処する {#base-unity}
  - なぜ: 方針契約は風土が下がったときに出る（公式の説明） [src: gdp_game_concepts_l_japanese.yml, game_concept_unity_contract_desc]
- [ ] 縁談は、風土を傾けたい側に合わせて相手を選ぶ {#base-marriage}
  - なぜ: 貴族の家とは「貴族化」側、交易商人とは「拝金主義」側に傾く（公式の説明）。段階の効果は7章 [src: gdp_reactive_advice_l_japanese.yml, reactive_advice_company_direction_panel_desc] [src: 00_house_unities.txt:278] [src: 00_house_unities.txt:428]

## 3. 商会を大きくする

- [ ] 洞察力が1,000に届いたら、「領国」画面で商会規模を「交易組織」に上げる {#grow-size}
  - なぜ: 洞察力は交易で稼いだ金の累計で、使っても減らない（公式の説明）。上げると競争力+20・交易路の長さ+4。費用は威信300で、上げたあと5年は次へ進めない。上の段階の条件は7章 [src: 00_defines.txt:1891] [src: 00_realm_laws.txt:3732] [src: 00_realm_laws.txt:3751] [src: 00_realm_laws.txt:3752] [src: 00_realm_laws.txt:23] [src: 00_realm_laws.txt:3759] [src: gdp_game_concepts_l_japanese.yml, game_concept_trade_acumen_desc]
- [ ] 後援者が公爵以上なら、「交易特許状を要請する」 {#grow-charter}
  - なぜ: 特許状を持てる従属商人は後援者ごとに1人。商会規模は交易組織以上（後援者が王なら有力商会、皇帝なら交易帝国）が要る。費用は威信150（王は2倍、皇帝は3倍）、同じ相手には10年あける [src: 11_gdp_merchant_interactions.txt:5102] [src: 11_gdp_merchant_interactions.txt:5079] [src: 11_gdp_merchant_interactions.txt:5146] [src: 11_gdp_merchant_interactions.txt:5154] [src: 11_gdp_merchant_interactions.txt:5161] [src: gdp_merchant_triggers.txt:2997]
- [ ] 特許状を得たら、決断「現地へ直接投資する」か「特許状の権限を濫用する」を使う {#grow-charter-use}
  - なぜ: 投資は金を出して建物と繁栄度を上げ、濫用は金を絞り取って競争力を上げる（公式の説明）。濫用すると秘密「約束を破る者」を抱える。どちらも名声レベル2以上、5年に1回 [src: gdp_merchant_decisions.txt:354] [src: gdp_merchant_decisions.txt:371] [src: gdp_merchant_decisions.txt:225] [src: gdp_merchant_decisions.txt:242] [src: gdp_merchant_decisions.txt:300] [src: gdp_merchant_scripted_effects.txt:6116] [src: gdp_merchant_decisions_l_japanese.yml, abuse_charter_authority_decision_tooltip] [src: gdp_merchant_decisions_l_japanese.yml, benevolent_charter_authority_decision_tooltip]
- [ ] 所持金が−25以下の領主に「金を貸し付ける」 {#grow-loan}
  - なぜ: 見返りは強いフック（返しきれない借金なら弱いフック）。利子は明示25%・隠して15%・無利子（好感度が上がる）から選ぶ。同じ相手には10年あける [src: 11_gdp_merchant_interactions.txt:2767] [src: gdp_merchant_values.txt:1546] [src: gdp_merchant_values.txt:1603] [src: gdp_merchant_values.txt:1607] [src: 11_gdp_merchant_interactions.txt:2716] [src: gdp_interactions_l_japanese.yml, loan_money_interaction_desc]
- [ ] 競り合いの激しい市場では、市場の持ち主に「交易を独占する」で交易独占権を買う {#grow-monopoly}
  - なぜ: 独占権のある市場では、保有者どうしでしか競争力を比べない（公式の説明）。同じ相手には8か月あける [src: gdp_game_concepts_l_japanese.yml, game_concept_trade_competitiveness_desc] [src: 11_gdp_merchant_interactions.txt:4181] [src: 11_gdp_merchant_interactions.txt:4238]
- [ ] 同じ家の別の商会は「商会を統合する」で吸収する {#grow-merge}
  - なぜ: 相手の商業網を解体し、その市場で自分の競争力を上げる（公式の説明）。5年に1回、同じ相手には15年あける [src: gdp_interactions_l_japanese.yml, merge_company_interaction_desc] [src: 11_gdp_merchant_interactions.txt:6868] [src: 11_gdp_merchant_interactions.txt:6869]
- [ ] ほかの家の商会は「敵対的買収を試みる」（工作）で奪うかを決める {#grow-takeover}
  - なぜ: 自分の商会規模が相手の家長以上でないと使えず、一度使うと50年使えない [src: 11_gdp_merchant_interactions.txt:7465] [src: 11_gdp_merchant_interactions.txt:7416]
- [ ] 条件がそろったら、方針に合った仕上げの決断（「隊商商人としての名声を確立する」など）を実行する {#grow-capstone}
  - なぜ: 名声レベル3以上、特性「交易商人」の方針と同じ道が100以上、商会規模が交易組織以上、どれかの商品カテゴリーの交易知識がレベル25以上。費用は威信1,500 [src: gdp_merchant_decisions.txt:1883] [src: gdp_merchant_decisions.txt:1885] [src: gdp_merchant_decisions.txt:1889] [src: gdp_merchant_decisions.txt:1893] [src: gdp_merchant_triggers.txt:1934] [src: gdp_merchant_decisions.txt:1912] [src: 00_basic_values.txt:1055]

## 4. 所領と後を託す

- [ ] 後継者にしたい子を、称号を持たない商会員として手元に置く {#land-heir}
  - なぜ: 継承法「商会継承」では、商会は最年長の子（いなければ近い親族）のうち、称号を持たない商会員が継ぐ。「後継者を指名」もできる [src: 00_succession_laws.txt:2113] [src: 00_succession_laws.txt:2137] [src: 00_succession_laws.txt:2141] [src: 00_succession_laws.txt:2143] [src: succession_laws_l_japanese.yml, merchant_succession_law_effects]
- [ ] 戦争の前に、傭兵を雇う金を確保する {#land-army}
  - なぜ: 交易商人は常備兵を持てず、傭兵の雇用費が2倍になる [src: 00_government_types.txt:1585] [src: 00_government_types.txt:1589]
- [ ] 所領を得る道を、「共和国に加わる」「土地を購入」「領国奪取」「私有地を取得する」から選ぶ {#land-route}
  - なぜ: 共和国に加わると商会を保ったままパトリシアンになる。土地の購入は所領を持つ支配者に、領国奪取は共和国を樹立する道、私有地は商会を解散して封臣になる道（公式の説明） [src: gdp_interactions_l_japanese.yml, merchant_join_republic_interaction_desc] [src: gdp_interactions_l_japanese.yml, merchant_purchase_land_interaction_desc] [src: gdp_game_concepts_l_japanese.yml, game_concept_seize_realm_cb_desc] [src: gdp_interactions_l_japanese.yml, merchant_procure_estate_interaction_desc]
- [ ] 共和国の支配者に「共和国に加わる」を送る {#land-republic}
  - なぜ: 名声レベル2以上が要る。交易商家ごとパトリシアンになり、商会・交易路・交易独占権は残る（公式の説明）。金（150＋商会規模ごとに100）を添えられる。同じ相手には10年あける [src: 11_gdp_merchant_interactions.txt:2092] [src: 11_gdp_merchant_interactions.txt:2054] [src: gdp_merchant_values.txt:152] [src: gdp_interactions_l_japanese.yml, merchant_join_republic_interaction_desc]
- [ ] 封建制などの領主に「土地を購入」を送る {#land-purchase}
  - なぜ: 伯爵領は金200、公爵領は500に中の伯爵領ごと200を足した額に、自分の文化の時代で0.5〜2倍を掛ける。官僚制・共和制などの相手には送れない。同じ相手には10年あける [src: gdp_merchant_values.txt:37] [src: gdp_merchant_values.txt:41] [src: gdp_merchant_values.txt:46] [src: gdp_merchant_values.txt:3] [src: 11_gdp_merchant_interactions.txt:1231] [src: 11_gdp_merchant_interactions.txt, merchant_purchase_land_interaction]
- [ ] 方針が「金貸し」なら、開戦事由「領国奪取」で領地を奪うかを決める {#land-seize}
  - なぜ: 伯爵領は名声レベル2、公爵領は3、王国は4が要る。勝つと共和国を樹立する。「債務者に参戦を強要する」で、強いフックを使って借り手を味方にできる（公式の説明） [src: gdp_merchant_wars.txt:16] [src: gdp_merchant_wars.txt:20] [src: gdp_merchant_wars.txt:186] [src: gdp_merchant_wars.txt:360] [src: gdp_game_concepts_l_japanese.yml, game_concept_seize_realm_cb_desc]
- [ ] 官僚制などの領主の下に入るなら、「私有地を取得する」を送る {#land-estate}
  - なぜ: 名声レベル2以上、商会規模が交易組織以上が要る。商会を解散し、私有地と貴族家の称号を得て無領の封臣になる（公式の説明）。同じ相手には10年あける [src: 11_gdp_merchant_interactions.txt:2460] [src: 11_gdp_merchant_interactions.txt:2463] [src: 11_gdp_merchant_interactions.txt:2417] [src: gdp_interactions_l_japanese.yml, merchant_procure_estate_interaction_desc]

## 5. 定期ルーチン {.routine}

### 毎年

- [ ] 「交易」画面の「交易路」タブで、交易路ごとの月の利益を見比べ、落ちた交易路を組み替える {#year-profit}
  - なぜ: 利益は交易路ごとに「/月」で出る。落ちた原因は6章 [src: window_trade.gui:1312] [src: trade_windows_l_japanese.yml, TRADE_ROUTE_ENTRY_ACTUAL_PROFIT]
- [ ] 「交易知識」タブで、レベルが下がっているカテゴリーがないか確かめる {#year-expertise}
  - なぜ: 主要交易品で扱っていないカテゴリーは、毎月15ずつ減る [src: window_trade.gui:120] [src: 00_defines.txt:2047]
- [ ] 洞察力が次の商会規模の条件に届いていないか確かめる {#year-size}
  - なぜ: 届いても自動では上がらない。条件は7章、手順は3章 [src: 00_realm_laws.txt:3732] [src: 00_defines.txt:1892] [src: 00_defines.txt:1893]
- [ ] 「家」画面の「風土」タブで、段階が狙いの側にあるか確かめる {#year-sentiment}
  - なぜ: 借金や婚姻で段階が動く（1章・2章）。段階の効果は7章 [src: house_view_l_japanese.yml, COMPANY_DIRECTION_TAB_BUTTON] [src: gdp_merchant_values.txt:1026]
- [ ] 称号を持たない商会員の子がいるか確かめる {#year-heir}
  - なぜ: 「商会継承」で商会を継げるのはその条件を満たす者だけ（4章） [src: 00_succession_laws.txt:2141] [src: succession_laws_l_japanese.yml, merchant_succession_law_effects]

### 2年ごと

- [ ] 決断「交易機会を探し求める」を実行する {#two-opportunity}
  - なぜ: 待ちが2年で、交易担当者のいる交易路を強める工作が出る（2章） [src: gdp_merchant_trade_opportunity_values.txt:4] [src: gdp_merchant_decisions_l_japanese.yml, seek_trade_opportunity_decision_tooltip]

### 通知が出たとき

- [ ] 「交易機会がある」「特別契約が利用可能」「方針契約が利用可能」が出たら、開いて受けるかを決める {#notice-contracts}
  - なぜ: どれも工作か移動を伴い、失敗・中止で契約も失敗する（2章） [src: merchant_actions.txt:357] [src: merchant_actions.txt:409] [src: merchant_actions.txt:442] [src: gdp_game_concepts_l_japanese.yml, game_concept_trade_opportunity_desc]
- [ ] 「商会の移転」が出たら、移転先の後援者と市場の繁栄度を見て、移るかを決める {#notice-move}
  - なぜ: 商会規模が後援者の格に対して大きすぎるときか、近くにもっと繁栄した市場があるときに出る。移ると後援者が替わり、今の従属商人契約は終わる（公式の説明） [src: merchant_actions.txt:665] [src: merchant_actions.txt:729] [src: gdp_interactions_l_japanese.yml, action_move_company_size_desc] [src: gdp_game_concepts_l_japanese.yml, game_concept_client_contract_desc]

### 戦争の前

- [ ] 所持金が−50未満でないか確かめる {#war-debt}
  - なぜ: 商会が借金を抱えている間は宣戦できない（公式の説明） [src: gdp_merchant_values.txt:1020] [src: gdp_interactions_l_japanese.yml, action_merchant_company_in_debt_desc]
- [ ] 傭兵の雇用費を見積もり、金を確保してから宣戦する {#war-merc}
  - なぜ: 常備兵を持てず、傭兵の雇用費が2倍（4章） [src: 00_government_types.txt:1585] [src: 00_government_types.txt:1589]

## 6. 困ったとき

**商会が借金を抱えた（通知「商会の負債」）**
- 見る場所: 通知の説明にある借金レベルの追加の影響と、所持金の月の収支 [src: merchant_actions.txt:237] [src: gdp_interactions_l_japanese.yml, action_merchant_company_in_debt_desc]
- 打ち手: 借金の間は宣戦できず、6か月ごとに風土が拝金主義側へ5動き、12か月続くと洞察力が500減る。赤字の交易路を外し、建設を待ち、貸した相手には「返済を要求する」 [src: gdp_merchant_values.txt:1027] [src: gdp_merchant_values.txt:1021] [src: gdp_merchant_values.txt:1018] [src: gdp_interactions_l_japanese.yml, demand_repayment_interaction_desc]

**交易路の利益が落ちた**
- 見る場所: 交易路の「/月」と、「交易路」タブの「競合相手」 [src: window_trade.gui:1312] [src: window_trade.gui:773]
- 打ち手: 競り負けているなら交易担当者を「競争を管理」にし、「市場税の特例を求める」か「交易を独占する」を使う。それでも駄目なら別の市場へ組み替える（2章・3章） [src: 00_trade_tasks.txt:15] [src: 11_gdp_merchant_interactions.txt:9854] [src: 11_gdp_merchant_interactions.txt:4181]

**交易特許状が要請できない**
- 見る場所: 「交易特許状を要請する」の説明に出る失敗理由 [src: 11_gdp_merchant_interactions.txt:5099]
- 打ち手: 後援者が公爵未満なら「商会の移転」で格の高い後援者の下へ移る。商会規模が足りなければ上げる。ほかの従属商人が特許状を持っていれば要請できない。ただし、その特許状が後援者に対して濫用されたものなら数えない（3章） [src: 11_gdp_merchant_interactions.txt:5102] [src: gdp_merchant_triggers.txt:2997] [src: 11_gdp_merchant_interactions.txt:5125] [src: 11_gdp_merchant_interactions.txt:5132]

**家の成員どうしの好感度が下がっている**
- 見る場所: 「風土」タブの段階。拝金主義は−20、打算は−10 [src: 00_house_unities.txt:278] [src: 00_house_unities.txt:334]
- 打ち手: 貴族の家と婚姻し、家長なら決断「贅沢を奨励する」で貴族化側へ大きく傾ける。打算では、ほかの統治者に商会員を引き抜かれやすい（公式の説明） [src: gdp_reactive_advice_l_japanese.yml, reactive_advice_company_direction_panel_desc] [src: gdp_game_concepts_l_japanese.yml, game_concept_company_sentiment_positive_actions_desc] [src: gdp_game_concepts_l_japanese.yml, game_concept_company_sentiment_fractious_desc]

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

## 9. 出典

### 一次情報

- パスは `Crusader Kings III/game` フォルダからの相対。同名のファイルが複数あるものは相対パスで書く
- `common/governments/00_government_types.txt`（`merchant_government`）
- `common/scripted_rules/00_rules.txt`、`common/bookmarks/bookmarks/00_bookmarks.txt`、`common/on_action/game_start.txt`、`common/on_action/dlc/gdp/gdp_merchant_on_actions.txt`
- `common/laws/00_realm_laws.txt`（商会規模・商会方針）、`common/subject_contracts/contracts/merchant.txt`（従属商人契約）、`common/house_unities/00_house_unities.txt`（`merchant_house_unity`）
- `common/defines/00_defines.txt`（`NTrade`）、`common/trade_tasks/00_trade_tasks.txt`、`common/domiciles/buildings/00_merchant_company_buildings.txt`
- `common/script_values/`（`00_basic_values.txt`・`gdp_domicile_values.txt`・`gdp_merchant_values.txt`・`gdp_merchant_trade_opportunity_values.txt`）、`common/modifiers/gdp_merchant_trade_opportunity_modifiers.txt`
- `common/decisions/dlc_decisions/gdp/`（`gdp_merchant_decisions.txt`・`gdp_visit_holding_decision.txt`）、`common/character_interactions/`（`11_gdp_merchant_interactions.txt`・`00_modifiy_vassal_contract.txt`）、`common/important_actions/merchant_actions.txt`
- `gui/window_my_realm.gui`、`gui/window_trade.gui`
- `common/laws/00_succession_laws.txt`（`merchant_succession_law`）、`common/casus_belli_types/gdp_merchant_wars.txt`（領国奪取）、`common/scripted_triggers/gdp_merchant_triggers.txt`、`common/scripted_effects/gdp_merchant_scripted_effects.txt`
- ローカライズ: `localization/japanese/dlc/gdp/`（`gdp_game_concepts_l_japanese.yml`・`gdp_interactions_l_japanese.yml`・`gdp_merchant_decisions_l_japanese.yml`・`gdp_visit_holding_decision_event_l_japanese.yml`）、`localization/japanese/succession_laws_l_japanese.yml`、`localization/japanese/trade/trade_windows_l_japanese.yml`、`localization/japanese/tutorial/gdp_reactive_advice_l_japanese.yml`、`localization/japanese/gui/house_view_l_japanese.yml`

### コミュニティ情報
