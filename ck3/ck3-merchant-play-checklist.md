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

## 4. 所領と後を託す

## 5. 定期ルーチン {.routine}

## 6. 困ったとき

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
- ローカライズ: `localization/japanese/dlc/gdp/`（`gdp_game_concepts_l_japanese.yml`・`gdp_visit_holding_decision_event_l_japanese.yml`）、`localization/japanese/tutorial/gdp_reactive_advice_l_japanese.yml`、`localization/japanese/gui/house_view_l_japanese.yml`

### コミュニティ情報
