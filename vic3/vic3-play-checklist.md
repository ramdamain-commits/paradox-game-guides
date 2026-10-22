# VIC3 プレイ中チェックリスト
> 対象パッチ: 1.14 オープンベータ（release/1.14.5・ビルド 25629520）・変動注意 ／ 最終確認日: 2026-10-22

どの国でも共通の「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。国ごとの事情は扱わない。DLC はすべてある前提で書き、DLC が要る項目や機能には「（DLC名 が必要）」と付ける。「（公式の説明）」は、ゲーム内のヒント・チュートリアル・用語説明が根拠で、効果をスクリプトでは確かめていない記述。

## 1. 開始直後（ポーズ中にやること）

- [ ] 画面上部の警告アイコンと「現在の状況」のリストを開き、リスト上部の赤いボタンの項目から順に内容を確かめる {#start-alerts}
  - なぜ: 警告は画面中央上部にアイコンで出て、重要アクションは「現在の状況」のリストに出る。リストで赤いボタンのものが「怒りの重要アクション」。このチェックリストの「…が出たら」は、この2つを指す（公式の説明） [src: concepts_l_japanese.yml, concept_alert_settings_alert_desc] [src: concepts_l_japanese.yml, concept_alert_settings_important_action_desc] [src: concepts_l_japanese.yml, concept_alert_settings_angry_important_action_desc] [src: important_actions_list.gui:54] [src: important_actions_list.gui:58]
- [ ] 警告「アクティブな研究がありません」が出ていれば、「技術」パネルで3つの技術ツリーから研究する技術を選ぶ {#start-research}
  - なぜ: 研究していないと、生み出される革新がすべて恒常的な技術の普及に回る（公式の説明） [src: alerts_l_japanese.yml, alert_has_no_research_alert_desc] [src: alerts_l_japanese.yml, alert_has_no_research_alert_hint] [src: 00_alert_types.txt:74]
- [ ] 「予算」パネルの「概要」タブで週間収支を確かめ、赤字なら2章「財政の安定」の手順で歳入を増やすか支出を減らす {#start-budget}
  - なぜ: 収支がマイナスだと金準備が先に減り、尽きると債務が増える。債務が信用枠を超えると債務不履行になり、進行中の建設がすべて止まる（公式の説明） [src: concepts_l_japanese.yml, concept_gold_reserves_desc] [src: concepts_l_japanese.yml, concept_default_desc]
- [ ] 画面上部の行政力・権力・影響力にそれぞれカーソルを合わせ、収支が0未満のものがないか確かめる {#start-capacity}
  - なぜ: 3つは貯めて使うものではなく、毎週の生産と使用の差で決まる。不足すると多大なペナルティを受け、少し余らせると小さなボーナスが付く（公式の説明）。不足と余剰の効果は7章 [src: concepts_l_japanese.yml, concept_capacity_desc] [src: 00_code_static_modifiers.txt:577] [src: 00_code_static_modifiers.txt:590] [src: 00_code_static_modifiers.txt:611]
- [ ] 「政策」パネルの「政府」タブで、政府内の利益集団と正当性の値を確かめる {#start-ig}
  - なぜ: 正当性は、政府内の利益集団と法律の組み合わせがどれだけ合っているかを示す（公式の説明）。効果が変わるのは段階の境目で、25未満は制定に政治運動の支持が要り、25〜49は制定速度 −25%、90以上は +25%。段階ごとの効果は7章 [src: concepts_l_japanese.yml, concept_legitimacy_desc] [src: 00_legitimacy_levels.txt:7] [src: 00_legitimacy_levels.txt:30] [src: 00_legitimacy_levels.txt:81] [src: politics_panel_reform_government.gui:373]
- [ ] 「建設」パネルで推定建設期間を確かめ、そのツールチップで政府の建設と民間の建設それぞれの残り期間を見る {#start-construction}
  - なぜ: 建てる施設は建設キューに入り、資材が使えるようになると先頭から着工する。推定建設期間が長いなら、施設を足しても着工は後になる（公式の説明） [src: concepts_l_japanese.yml, concept_construction_queue_desc] [src: interfaces_l_japanese.yml, QUEUE_CONSTRUCTION_POINTS_SUMMARY_TOOLTIP] [src: construction_queue.gui:106] [src: construction_queue.gui:107]

## 2. 序盤（1836〜1861）

### 財政の安定

到達目標: 週間収支が黒字で、行政力・権力・影響力が0以上、債務が信用枠に迫っていない状態にする。

- [ ] 警告「債務不履行中」が出たとき、または金準備が尽きて赤字が続くときは、「予算」パネルの「概要」タブで課税レベルを上げるか、新しい消費税を課す {#early-deficit}
  - なぜ: 増税は歳入をすぐ増やす最も簡単な方法だが、財力の低下や社会不安の恐れがある（公式の説明）。消費税は課す商品ごとに権力を使い、税の上げ下げは正当性にも響く [src: tutorial_l_japanese.yml, lesson_budget_balance_2_desc] [src: concepts_l_japanese.yml, concept_consumption_tax_desc] [src: concepts_l_japanese.yml, concept_legitimacy_desc] [src: 00_alert_types.txt:35]
- [ ] 増税しても収支が戻らないときは、「予算」パネルの「概要」タブの「すべて一時停止」で、進行中の建設を中断する {#early-build-stop}
  - なぜ: 建設費は固定費ではないが、建設中は国庫の負担になる。赤字を解消してから「すべて再開」できる。民間の建設の資金は常に投資プールから出る（公式の説明） [src: tutorial_l_japanese.yml, lesson_budget_balance_how_3_desc] [src: alerts_l_japanese.yml, alert_country_default_hint] [src: concepts_l_japanese.yml, concept_private_construction_desc] [src: budget_panel.gui:482] [src: interfaces_l_japanese.yml, RESUME_ALL_CONSTRUCTION_BUTTON]
- [ ] 「予算」パネルの「州」タブで支出の大きい政府施設を探して縮小するか、「概要」タブで国家公務員の給金と軍隊の給金を下げる {#early-gov-cost}
  - なぜ: 政府施設の運営費は固定費。縮小すると支出を恒久的に減らせるが、その施設レベルの恩恵を失う。賃金はいつでも戻せるが、変更の結果は説明を読んで確かめる（公式の説明） [src: tutorial_l_japanese.yml, lesson_budget_balance_how_4_desc] [src: tutorial_l_japanese.yml, lesson_budget_balance_how_5_desc] [src: tutorial_l_japanese.yml, lesson_budget_balance_how_6_desc] [src: budget_panel.gui:621] [src: budget_panel.gui:746]
- [ ] 「予算」パネルの「資産」タブで、債務の元金が信用枠に近づいていないか確かめる {#early-debt}
  - なぜ: 元金が信用枠に達すると債務不履行になり、進行中の建設がすべて止まる。施設の生産量にも、時間とともに重くなるペナルティが付く。収支が黒字に戻るか、破産を宣言すると解除される（公式の説明） [src: concepts_l_japanese.yml, concept_default_desc] [src: tutorial_l_japanese.yml, lesson_budget_balance_why_6_desc] [src: tutorial_l_japanese.yml, lesson_budget_balance_why_7_desc]
- [ ] 重要アクション「金の備蓄」が出たら、支出を増やすか税を下げる {#early-gold}
  - なぜ: 収支が黒字のまま金準備が上限を超えると、経済とPOPから資金を奪って財力を減らす（公式の説明）。上限の基本は年間GDPの0.2倍。数値は7章 [src: alerts_l_japanese.yml, alert_stockpiling_gold_alert_hint] [src: 00_alert_types.txt:836] [src: 00_alert_types.txt:841] [src: 00_defines.txt:542]
- [ ] 行政力が0未満なら、行政府を増築するか、行政府の方式をより効率的なものに切り替える {#early-bur}
  - なぜ: 行政力は主に行政府が生み、税の徴収と制度の維持に使われる。不足すると浪費税額が発生し、経済が急に鈍る（公式の説明）。行政府の解禁には技術「官僚制」が要る。数値は7章 [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_3_desc] [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_4_desc] [src: 00_code_static_modifiers.txt:577] [src: common/buildings/07_government.txt:9]
- [ ] 権力が0未満なら、不要な布告を取り消し、課す必要のない消費税を外す {#early-aut}
  - なぜ: 権力は布告・消費税・政治運動の強化と抑圧に使われ、法律（特にリベラル色の低いもの）が生む。不足すると対立側の利益集団の支持が下がり、政治運動と急進派が勢いづく（公式の説明）。長期には、権力を生む厳格な法律も手段になる。数値は7章 [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_5_desc] [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_6_desc] [src: 00_code_static_modifiers.txt:590]
- [ ] 影響力が0未満なら、維持している外交協定のうち不要なものを、条約なら拘束期間が終わったものから破棄する {#early-inf}
  - なぜ: 影響力は外交協定（従属国との関係を含む）の維持に使われる。不足すると威信が下がり、ランクと影響力の生成も落ちる。不足が小さければ、ライバルの確立も手段になる。条約は拘束期間中に離脱するとペナルティがある（公式の説明）。数値は7章 [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_7_desc] [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_8_desc] [src: concepts_l_japanese.yml, concept_rivalry_desc] [src: concepts_l_japanese.yml, concept_binding_period_desc] [src: 00_code_static_modifiers.txt:611]

### 建設の回し方

到達目標: 資材を切らさず、生産性の高い施設に建設を回し、赤字の施設と商品の不足を放置せず、企業の設立枠を使い切った状態にする。

- [ ] 怒りの重要アクション「投資プールのための資材が不足」が出たら、「建設」パネルを開き、建設局を増やすか、建設局の方式を上位に切り替える {#early-sector}
  - なぜ: 投資プールに入ってくる資金を使い切れるだけの資材を作れていない状態（公式の説明）。建設局は技術「都市化」で解禁される [src: alerts_l_japanese.yml, alert_insufficient_construction_for_investment_desc] [src: alerts_l_japanese.yml, alert_insufficient_construction_for_investment_hint] [src: 00_alert_types.txt:621] [src: common/buildings/13_construction.txt:13]
- [ ] 「施設」パネルの一覧で、生産性の高い施設を探し、「+」ボタンか右クリックで拡張する {#early-expand}
  - なぜ: 拡張先は利益でなく生産性で選ぶ。生産性は従業員1人あたりが年間に生む経済価値の目安で、賃金・税・助成・配当の違いに左右されない（公式の説明） [src: tutorial_l_japanese.yml, lesson_expand_productive_building_how_3_desc] [src: tutorial_l_japanese.yml, lesson_expand_productive_building_how_4_desc] [src: concepts_l_japanese.yml, concept_productivity_desc]
- [ ] 拡張した施設の生産性が下がっていないか、しばらくして「施設」パネルで見直し、下がっていれば同じ施設の拡張を止める {#early-oversupply}
  - なぜ: 供給過多になると商品の市場価格が下がり、生産性は時間とともに低下する。生産性の高い施設だけを拡張し続けるのが最適とは限らない（公式の説明） [src: tutorial_l_japanese.yml, lesson_expand_productive_building_why_5_desc]
- [ ] 生産性の低い施設は、詳細パネルで投入商品と産出商品の価格を見て、原因が高い投入か安い産出かを突き止める {#early-unprofitable}
  - なぜ: 投入が高いなら、その商品を作る施設を拡張するか輸入して価格を抑える。産出が安いなら、その商品を使う施設を拡張するか、他国の市場へ輸出する。輸出入には取引所が要る（公式の説明） [src: tutorial_l_japanese.yml, lesson_fix_unproductive_building_how_2_desc] [src: tutorial_l_japanese.yml, lesson_fix_unproductive_building_how_3_desc] [src: tutorial_l_japanese.yml, lesson_fix_unproductive_building_how_4_desc]
- [ ] 怒りの重要アクション「…における（商品）の不足」が出たら、その商品の売り注文を増やす {#early-shortage}
  - なぜ: 使う施設の産出ペナルティは、生産の増加・産地の州のインフラ改善による市場アクセスの向上・世界市場からの輸入（取引所が要る）で売り注文が増えれば解け、電力・サービスなど州内の商品は州の生産量を増やす（公式の説明）。数値は7章 [src: alerts_l_japanese.yml, alert_market_goods_shortage_hint] [src: alerts_l_japanese.yml, alert_state_goods_shortage_hint] [src: 00_alert_types.txt:781] [src: 00_alert_types.txt:797] [src: 00_defines.txt:419]
- [ ] 重要アクション「…の市場アクセスは、…%です」や警告「…は孤立したです」が出たら、その州に港か鉄道を建てる {#early-infra}
  - なぜ: 市場アクセスは州のインフラ使用がインフラを超えると下がり、孤立した州は市場で売買できない。港は技術「航海術」、鉄道は技術「鉄道」で解禁。布告「道路整備」でも補えるが、権力を使うので一時しのぎにとどめる（公式の説明）。数値は7章 [src: concepts_l_japanese.yml, concept_market_access_desc] [src: alerts_l_japanese.yml, alert_low_market_access_alert_hint] [src: alerts_l_japanese.yml, alert_isolated_state_alert_hint] [src: tutorial_l_japanese.yml, lesson_market_access_with_railways_why_2_desc] [src: 00_alert_types.txt:927] [src: 00_alert_types.txt:477] [src: common/buildings/11_private_infrastructure.txt:11] [src: common/buildings/11_private_infrastructure.txt:37] [src: 00_decree.txt:20]
- [ ] 警告「…での飢饉」が出たら、「市場」パネルの「食料保障」タブで被害の州を確かめ、基本的な食料を満たす商品を作る施設を建てるか、その商品を輸入する {#early-food}
  - なぜ: 施設や輸入は効くまで時間がかかり、布告「緊急救援」のほうが早く効くことがある（公式の説明）。ただしこの布告は州の徴税を減らし、技術「中央集権化」で解禁される。数値は7章 [src: alerts_l_japanese.yml, alert_famine_alert_hint] [src: 00_alert_types.txt:459] [src: 00_decree.txt:150]
- [ ] 新しい方式が解禁されたら、投入商品の価格と不足、必要な職業の資格を持つPOPの数を確かめてから切り替える {#early-pm}
  - なぜ: 投入商品が高い・不足しているときや、その方式に必要な資格を持つPOPが乏しいときは、近代化を急がないほうがよい（公式の説明） [src: tutorial_l_japanese.yml, lesson_production_methods_why_5_desc]
- [ ] 重要アクション「…が生活水準の期待値（最小）を下回っています」が出たら、その州の仕事を増やしてPOPの収入を上げる {#early-sol}
  - なぜ: 州のPOPの25%以上が期待値を下回ると出る。仕事が増えて収入が上がれば生活水準が上がる（公式の説明）。数値は7章 [src: alerts_l_japanese.yml, alert_low_expected_sol_in_state_hint] [src: 00_alert_types.txt:989]
- [ ] 警告「新たな企業を設立できる」が出たら、「企業」パネルで設立できる企業の条件を読み、「設立」を押す {#mid-company-new}
  - なぜ: 企業を設立すると、その企業に関連する施設の生産量と建設効率が上がる（公式の説明）。設立できる数は技術「企業チャーター」と「株式会社」でそれぞれ1増える [src: alerts_l_japanese.yml, alert_can_establish_company_hint] [src: concepts_l_japanese.yml, concept_company_desc] [src: tutorial_l_japanese.yml, lesson_establish_company_how_2_desc] [src: 00_alert_types.txt:115] [src: 30_society.txt:189] [src: 30_society.txt:619]

### 最初の法改正

到達目標: 正当性と利益集団の支持を保ったまま、最初の法律を失敗せずに通す。

- [ ] 「政策」パネルの「法律」タブで、制定したい法律の制定成功を確かめる {#early-law-check}
  - なぜ: 制定には、政府内の利益集団の少なくとも1つが支持するか、現在の政治運動が支持するか、制定成功が別の理由でプラスになっている必要がある（公式の説明） [src: concepts_l_japanese.yml, concept_enactment_of_laws_potential] [src: tutorial_l_japanese.yml, lesson_enact_institution_law_how_1_desc] [src: tutorial_l_japanese.yml, lesson_enact_institution_law_how_3_desc]
- [ ] 制定成功がマイナスの法律は、制定を始めない {#early-law-fail}
  - なぜ: 制定成功が0を下回るなどで後退が重なると制定に失敗し、730日たつまでその法律を再び試せない。制定は3つのフェーズを通る（公式の説明）。数値は7章 [src: concepts_l_japanese.yml, concept_enactment_setback_desc] [src: concepts_l_japanese.yml, concept_enactment_phase_desc] [src: 00_defines.txt:171] [src: 00_defines.txt:181]
- [ ] 支持が足りないときは、「政策」パネルの「概要」タブで、通したい法律を支持する政治運動を選んで強化する {#early-bolster}
  - なぜ: 強化された運動は、時間とともに支持者と支持が増え、利益集団の思想に影響して法律を通しやすくする。強化には権力が要り、使えるかは「言論の自由」の法律グループの現行法で決まる（公式の説明）。数値は7章 [src: tutorial_l_japanese.yml, lesson_promote_movement_how_1_desc] [src: tutorial_l_japanese.yml, lesson_promote_movement_how_5_desc] [src: tutorial_l_japanese.yml, lesson_promote_movement_why_3_desc] [src: 00_defines.txt:283] [src: 00_tutorial_lessons_promote_ig.txt:131]
- [ ] 警告「フリー政府改革」が出ている間に、「政策」パネルの「政府」タブで「政府改革」ボタンを押し、政府内の利益集団の構成を見直す {#early-reform-free}
  - なぜ: 最近の選挙により、表示された期限内に行う次の政府改革は急進派を生まない。ふつうは、権力を持っていた集団を政府から外すと急進派が出て、改革を頻繁に行うと政情が大きく不安定になる（公式の説明） [src: alerts_l_japanese.yml, alert_free_government_reform_desc] [src: tutorial_l_japanese.yml, lesson_reform_government_how_5_desc] [src: 00_alert_types.txt:141]
- [ ] 警告「非正規政府」や怒りの重要アクション「不安定な政府」が出たら、「政策」パネルの「政府」タブで「政府改革」ボタンを押し、正当性が上がる利益集団の組み合わせを試す {#early-reform-legit}
  - なぜ: 構成は確定するまで適用されず、試し直せる（公式の説明）。正当性が25〜49なら制定速度 −25%、25未満なら制定に政治運動の支持が要る。段階ごとの効果は7章 [src: tutorial_l_japanese.yml, lesson_reform_government_how_3_desc] [src: alerts_l_japanese.yml, alert_low_legitimacy_alert_hint] [src: 00_alert_types.txt:419] [src: 00_alert_types.txt:741] [src: 00_legitimacy_levels.txt:7] [src: 00_legitimacy_levels.txt:30]

## 3. 中盤（1862〜1886）

### 産業化

到達目標: 企業の繁栄度の低下と移住の流れを見逃さず、産業の効率が落ちる兆しを放置していない状態にする。

- [ ] 怒りの重要アクション「（企業名）の繁栄度が減少」が出たら、その企業に関連する施設のうち生産性の低いものを、2章「建設の回し方」の手順で立て直す {#mid-company-prosperity}
  - なぜ: 繁栄度は施設の生産性などで決まる（公式の説明）。国へのボーナスと、この怒りの重要アクションが出る条件の数値は7章 [src: concepts_l_japanese.yml, concept_prosperity_desc] [src: alerts_l_japanese.yml, alert_company_losing_prosperity_hint] [src: 00_defines.txt:664] [src: 00_defines.txt:665] [src: 00_alert_types.txt:771] [src: 00_alert_types.txt:772]
- [ ] 施設の人手が足りない州は、州にカーソルを合わせて移住求心力を確かめ、低ければ布告「隣の芝は青い運動」を出す {#mid-immigration}
  - なぜ: 同じ市場の中で、移住求心力の低い州から高い州へ人が移り、失業者は求心力を下げる（公式の説明）。布告は求心力を上げ、権力を使う。数値は7章 [src: concepts_l_japanese.yml, concept_migration_desc] [src: concepts_l_japanese.yml, concept_migration_pull_desc] [src: tutorial_l_japanese.yml, lesson_increase_immigration_how_2_desc] [src: 00_decree.txt:897] [src: 00_decree.txt:898] [src: 00_decree.txt:901] [src: 00_decree.txt:903]

### 市場と貿易

到達目標: 貿易キャパシティに余裕があり、行政品の高騰を放置していない状態にする。

- [ ] 「市場」パネルの「貿易」タブ上部で、貿易キャパシティの使用量が総量に近づいていないか確かめ、近ければ取引所を増築する {#mid-trade-capacity}
  - なぜ: 貿易キャパシティは取引所のレベルが生み、世界市場との貿易に使われる。総量が0だと表示されない（公式の説明） [src: concepts_l_japanese.yml, concept_trade_capacity_desc] [src: interfaces_l_japanese.yml, MARKET_COUNTRY_TRADE_CAPACITY] [src: interfaces_l_japanese.yml, MARKET_PANEL_WORLD_MARKET_TRADE] [src: market_panel.gui:155]
- [ ] 重要アクションのグループ「高価な行政品」が出たら、商品パネルを開いて、その行政品の生産を増やすか輸入する {#mid-expensive-goods}
  - なぜ: 行政品は政府の施設が消費し、国庫の資金を使う。価格は、施設や方式で生産量を増やすか他国から手に入れると下がり、関税や消費税の変更が効くこともある（公式の説明） [src: concepts_l_japanese.yml, concept_government_good_desc] [src: alerts_l_japanese.yml, ag_expensive_government_goods_name] [src: alerts_l_japanese.yml, alert_expensive_goods_alert_hint_common] [src: alerts_l_japanese.yml, alert_expensive_government_goods_alert_desc] [src: 00_alert_types.txt:952]

### 政治改革

到達目標: 制度への投資と、急進化する運動・圧力団体の確認を、定期的に回している状態にする。

- [ ] 「政策」パネルの「制度」タブで、解禁済みの制度の投資レベルを確かめ、行政力に余裕があれば上げる {#mid-institution}
  - なぜ: 制度は編入州に利益を与え、維持に行政力を使う。レベルが高いほどコストも効果も大きい（公式の説明）。レベルは1〜5。制度は、対応する法律を制定すると使えるようになる [src: concepts_l_japanese.yml, concept_institution_desc] [src: tutorial_l_japanese.yml, lesson_enact_institution_law_why_4_desc] [src: 00_defines.txt:293] [src: 00_defines.txt:294] [src: politics_panel_institutions.gui:328]
- [ ] 「政策」パネルの「概要」タブで政治運動の運動活動の予測を確かめ、50%に達しそうな運動は、支持者の生活水準を上げて急進派を減らすか、権力で抑圧する {#mid-movement}
  - なぜ: 運動活動が25%以上だと、運動が支持・反対する法律の制定に影響が出る。50%以上で毎月支持者が急進化し、反乱（革命・分離）に変わりやすくなる。急進派は生活水準が期待値を下回ると現れる（公式の説明）。抑圧には権力を使う [src: concepts_l_japanese.yml, concept_activism_desc] [src: concepts_l_japanese.yml, concept_radical_desc] [src: concepts_l_japanese.yml, concept_suppress_desc] [src: 00_defines.txt:98] [src: 00_defines.txt:105] [src: 00_defines.txt:312]
- [ ] 「政策」パネルの「概要」タブの「政治的圧力団体」一覧で宥和の低い圧力団体を探し、その対象国への外交アクションを見直す {#mid-lobby}
  - なぜ: 宥和が上がると、その圧力団体を支える利益集団の支持が増える。支持派は友好的な外交アクションで、反対派は敵対的な外交アクションで宥和が上がる。圧力団体の大きさは、対象国との外交協定にかかる影響力のコストに響く（公式の説明） [src: concepts_l_japanese.yml, concept_political_lobby_appeasement_desc] [src: tutorial_l_japanese.yml, lesson_lobbies_how_3_desc] [src: tutorial_l_japanese.yml, lesson_lobbies_how_4_desc] [src: politics_panel_overview.gui:1612]

### 勢力拡大

到達目標: 狙う地域の関心ランクを満たし、軍・従属国・編入待ちの州が国力を超えていない状態にする。

- [ ] 外交戦を起こしたい戦略的重要地域では、外交レンズの「関心の宣言」を使い、関与を積んで関心ランクを「積極的」以上にする {#mid-interest}
  - なぜ: 関心ランクが十分高いことが、その地域の外交戦を始める・参加する条件になる。関与は軍の駐在・州の所有・請求権・条約などで増える（公式の説明）。「積極的」は関与1000以上 [src: concepts_l_japanese.yml, concept_interest_desc] [src: interfaces_l_japanese.yml, HOW_TO_INCREASE_INVOLVEMENT] [src: interfaces_l_japanese.yml, declare_interest_tooltip] [src: interest_tier_types.txt:40] [src: interest_tier_types.txt:47]
- [ ] 軍事パネルで兵力を確かめ、足りなければ「編隊」パネルの「情報」タブのボタンから、余剰の労働者がいてインフラと軍需品も整った州に兵舎を建てる {#mid-army}
  - なぜ: すべてのユニットは戦力投射に寄与し、威信になる。維持費は軍隊の給金と軍需品が主で、戦争中の大隊の動員で増える。拡張費が国庫で賄える額を超えないようにする（公式の説明） [src: tutorial_l_japanese.yml, lesson_expand_military_how_3_desc] [src: tutorial_l_japanese.yml, lesson_expand_military_why_2_desc] [src: tutorial_l_japanese.yml, lesson_expand_military_why_3_desc] [src: military_formation_panel.gui:1010] [src: military_formation_panel.gui:3949]
- [ ] 戦争で目的を果たすときは、外交レンズの「外交的要求」タブで開始する外交戦を選び、「初動」の間に戦争目標を足す {#mid-play}
  - なぜ: 外交戦は「初動」「外交工作」「戦争へのカウントダウン」の3フェーズで進み、どちらも引かなければ戦争になる。初動の間に戦争目標を足さないと、戦争賠償金の目標が自動で付く（公式の説明） [src: tutorial_l_japanese.yml, lesson_start_diplomatic_play_how_3_desc] [src: alerts_l_japanese.yml, alert_has_no_war_goal_alert_desc] [src: alerts_l_japanese.yml, alert_has_no_war_goal_alert_hint] [src: 00_alert_types.txt:209] [src: interfaces_l_japanese.yml, diplomatic_plays_lens_tab]
- [ ] 戦争で未編入州を得たら、行政力に余裕のあるうちに、政治レンズの「州アクション」タブで「州の編入」を始める {#mid-incorporate}
  - なぜ: 編入した州は税を払い、制度の恩恵を受ける。行政力の全額は開始時にかかり、必要な年数は主要文化との違いで変わる（公式の説明） [src: tutorial_l_japanese.yml, lesson_incorporate_state_how_3_desc] [src: tutorial_l_japanese.yml, lesson_incorporate_state_complete_desc] [src: interfaces_l_japanese.yml, incorporate_state] [src: 00_tutorial_lessons_incorporate_state.txt:27] [src: 00_tutorial_lessons_incorporate_state.txt:28]
- [ ] 外交パネルの「従属国」タブで従属国の自由への願望を確かめ、高い従属国は自治権を拡大し、低い従属国は自治権を縮小する {#mid-subject}
  - なぜ: 願望が高いと、従属国は独立のために外交戦を起こしうる。自治権の拡大・縮小で、願望と支配率を調整できる（公式の説明）。数値は7章 [src: tutorial_l_japanese.yml, lesson_subject_liberty_how_5_desc] [src: tutorial_l_japanese.yml, lesson_subject_liberty_why_1_desc] [src: 00_liberty_desire_levels.txt:17] [src: 00_liberty_desire_levels.txt:27] [src: 00_liberty_desire_levels.txt:38]
- [ ] 非承認大国以上なら、勢力ブロックパネルで「勢力ブロックを形成」を押し、アイデンティティの柱と主要原則グループの原則を選んで形成する {#mid-bloc}
  - なぜ: 影響力が足りず関係を維持できない国とも関係を保て、他のブロックから遠ざけられる（公式の説明）。法律「孤立主義」では形成できない。DLC なしでも形成できるが、2つ目以降の原則枠と多くの原則（Sphere of Influence が必要）は選べない [src: tutorial_l_japanese.yml, lesson_form_power_bloc_how_2_desc] [src: tutorial_l_japanese.yml, lesson_form_power_bloc_why_4_desc] [src: interfaces_l_japanese.yml, FORM_POWER_BLOC] [src: 00_scripted_triggers.txt:56] [src: 00_scripted_triggers.txt:57] [src: 00_scripted_rules.txt:157] [src: 00_scripted_rules.txt:161] [src: 00_power_bloc_principles.txt:10] [src: 00_dlc_metadata.txt, dlc010]
- [ ] 勢力ブロックリーダーなら、重要アクション「権限が利用可能」が出たら、勢力ブロックパネルの「概要」タブで原則を変更・更新・追加する {#late-bloc-mandate}
  - なぜ: 権限は原則の変更・更新・新規追加に使う。強いメンバーがいる、結束力が高いと早く貯まる（公式の説明） [src: alerts_l_japanese.yml, alert_power_bloc_mandates_available_hint] [src: concepts_l_japanese.yml, concept_power_bloc_mandate_desc] [src: 00_alert_types.txt:1042] [src: power_bloc_panel.gui:1552]

## 4. 終盤（1887〜）

### 列強の地位の維持

到達目標: ランクを失う前に威信の不足を埋め、外交協定の更新を取りこぼしていない状態にする。

- [ ] 警告「戦力ランクを失っています」が出たら、外交パネルで威信とランクの維持に必要な威信を比べ、国内総生産・陸海軍の戦力投射・商品の生産のどれかを伸ばす {#late-rank}
  - なぜ: 威信が足りないまま回復しないと、警告に表示された日数でランクが下がる（公式の説明）。ランクが下がると、影響力の生産（列強 +1000、大国 +750）や貸付歩合の優遇（列強 −50%、大国 −25%）などを失う [src: alerts_l_japanese.yml, alert_is_losing_rank_alert_desc] [src: alerts_l_japanese.yml, alert_is_losing_rank_alert_hint] [src: concepts_l_japanese.yml, concept_prestige_desc] [src: 00_alert_types.txt:196] [src: 00_country_ranks.txt:42] [src: 00_country_ranks.txt:44] [src: 00_country_ranks.txt:80] [src: 00_country_ranks.txt:82]
- [ ] 怒りの重要アクションで外交協定や条約の条項が破棄の危機にあると出たら、外交パネルで破棄される条件を読み、重要な協定なら関係を改善するか、危うくしている行動をやめる {#late-treaty}
  - なぜ: 表示された条件が真でなくなると、その協定や条項は破棄される（公式の説明） [src: alerts_l_japanese.yml, alert_diplomatic_pact_in_danger_desc] [src: alerts_l_japanese.yml, alert_diplomatic_pact_in_danger_hint] [src: alerts_l_japanese.yml, alert_treaty_article_in_danger_hint] [src: 00_alert_types.txt:694] [src: 00_alert_types.txt:708]

### 急進派・財政の崩れの予防

到達目標: 分離や革命に育つ前に運動を抑え、戦争の出費で収支が崩れていない状態にする。

- [ ] 警告「分離主義者運動」が出たら、「政策」パネルで該当の政治運動を選び、運動活動と支持を減らす {#late-secession}
  - なぜ: 運動活動は、支持者の急進派を減らし利益集団の支持を増やすと鈍る。育つと、支持者の多い州が分離して外交戦を起こす（公式の説明） [src: alerts_l_japanese.yml, alert_secession_growing_alert_hint] [src: concepts_l_japanese.yml, concept_secession_desc] [src: 00_alert_types.txt:492]
- [ ] 革命や分離の兆しがあるときは、「政策」パネルの「制度」タブで「治安維持」と「法執行機関」の投資レベルを上げる {#late-institution}
  - なぜ: 「治安維持」は革命と分離の進行を遅らせ、「法執行機関」は社会不安の悪影響を減らす。「治安維持」で革命を弱められると、用語説明にもある（公式の説明） [src: concepts_l_japanese.yml, concept_revolution_desc] [src: 00_institutions.txt:35] [src: 00_institutions.txt:48] [src: 00_institutions.txt:49]
- [ ] 戦争中や軍の拡張後は、「予算」パネルの「概要」タブで週間収支を確かめ、赤字なら2章「財政の安定」の手順で戻す {#late-budget-war}
  - なぜ: 軍隊の主な出費は軍隊の給金と軍需品で、戦争中の大隊の動員でさらに増える（公式の説明）。戦争支持率も、長引く戦争と借入・債務不履行で下がり、金準備で上がる。数値は7章 [src: tutorial_l_japanese.yml, lesson_expand_military_why_3_desc] [src: 00_defines.txt:2136] [src: 00_defines.txt:2137] [src: 00_defines.txt:2139] [src: 00_defines.txt:2140] [src: 00_defines.txt:2143]
- [ ] 怒りの重要アクション「低い訓練率」が出たら、「予算」パネルの「概要」タブで軍隊の給金を上げる {#late-training}
  - なぜ: 戦争中に軍隊の給金を下げると、軍事施設の訓練率が下がる（公式の説明） [src: alerts_l_japanese.yml, alert_training_rate_low_desc] [src: alerts_l_japanese.yml, alert_training_rate_low_hint] [src: 00_alert_types.txt:753]

### 戦争の崩れの予防

到達目標: 戦争支持率の低下・戦争目標の失効・無防備な戦線を戦争中に放置せず、戦争目標の強制を進められている状態にする。

- [ ] 警告「Low 戦争支持率」が出たら、戦争パネルで戦争支持率を確かめ、戦闘に勝って戦争目標を掌握するか、和平協定を進める {#late-war-support}
  - なぜ: 戦争支持率が25を下回ると警告が出る。定義では25以下から、戦闘への不利な補正と急進化が始まる。戦闘に勝ち、戦争目標を掌握すると回復する（公式の説明）。警告名の「Low」とヒント本文は日本語訳がなく、英語で表示される [src: 00_defines.txt:1203] [src: alerts_l_english.yml, alert_low_war_support_effects_alert_name] [src: alerts_l_english.yml, alert_low_war_support_effects_alert_hint] [src: 00_alert_types.txt:48]
- [ ] 警告「戦争目標 expiring」が出たら、戦争パネルで該当の戦争目標にカーソルを合わせ、掌握に必要な条件を満たす {#late-goal-risk}
  - なぜ: 長く掌握されていない戦争目標は、表示された日数後に取り下げられる。警告名の「expiring」と本文は日本語訳がなく、英語で表示される（公式の説明）。数値は7章 [src: alerts_l_english.yml, alert_war_goal_at_risk_of_being_dropped_alert_desc] [src: alerts_l_english.yml, alert_war_goal_at_risk_of_being_dropped_alert_hint] [src: 00_alert_types.txt:61] [src: war_goal_types.md, Contestion Type]
- [ ] 戦争中は、戦争目標の掌握に必要な条件（目標の州の占領など）を保ち、戦争パネルで強制の進み具合を確かめる {#late-war-enforce}
  - なぜ: 目標を掌握している間は毎週進み、100で和平を待たずに強制される。掌握をやめると減る。進み具合の表示は英語のみ。数値は7章 [src: 00_defines.txt:2192] [src: 00_defines.txt:2193] [src: 00_defines.txt:2195] [src: war_goal_types.md, Fill per week / Deplete per week] [src: interfaces_l_english.yml, WAR_GOAL_ENFORCEMENT_PROGRESS] [src: war_panel.gui:1901]
- [ ] 警告「無防備な戦線」が出たら、前線パネルを開き、将軍か大隊を配属する {#late-front}
  - なぜ: 将軍も大隊も配属されていない戦線に、敵の将軍が少なくとも1人割り当てられている状態。将軍は「編隊」パネルの「将軍の雇用」ボタンで雇用できる（公式の説明） [src: alerts_l_japanese.yml, alert_vulnerable_front_desc] [src: alerts_l_japanese.yml, alert_vulnerable_front_hint] [src: tutorial_l_japanese.yml, lesson_recruit_promote_commander_how_1_desc] [src: 00_alert_types.txt:226]

## 5. 定期ルーチン {.routine}

### 毎年

- [ ] 毎年と新しい記事が出たときに、ジャーナルパネルで進行中のジャーナル記事を開き、失敗や期限切れの恐れがあるものがないか確かめる {#yearly-journal}
  - なぜ: ジャーナル記事は進行中のイベントを追い、約束の思い出しや危機の警告を示す。失敗や期限切れで消えるものもあり、期限が730日の記事もある（公式の説明） [src: concepts_l_japanese.yml, concept_journal_entry_desc] [src: 01_coup.txt:78] [src: alerts_l_japanese.yml, alert_can_take_decisions_action]
- [ ] 州を右クリックして開くメニューの「布告」で、発令中の布告のうち不要になったものを取り消す {#yearly-decree}
  - なぜ: 布告は有効な間ずっと権力を消費し、取り消すまで州にボーナスを与える（公式の説明） [src: concepts_l_japanese.yml, concept_decree_desc] [src: interfaces_l_japanese.yml, DECREE_REMOVE] [src: right_click_menu.gui:6419] [src: right_click_menu.gui:6445]
- [ ] 外交協定を結びたい国や、外交戦で味方につけたい国は、国パネルの「外交」タブで関係を見直し、下がっていれば外交レンズの「外交アクション」タブで「関係改善」を結ぶか維持する {#yearly-relations}
  - なぜ: 関係は何もしないと中立へ減衰する。維持には影響力を使う。関係は外交協定の可否と、外交戦での承諾に響く（公式の説明） [src: concepts_l_japanese.yml, concept_relations_desc] [src: tutorial_l_japanese.yml, lesson_increase_relations_why_3_desc] [src: tutorial_l_japanese.yml, lesson_increase_relations_how_1_continue] [src: tutorial_l_japanese.yml, lesson_increase_relations_how_2_desc] [src: interfaces_l_japanese.yml, diplomatic_actions_lens_tab] [src: country_panel.gui:184]

### 法律が成立したとき

- [ ] 画面上部の権力にカーソルを合わせ、収支が0未満になっていないか確かめる {#law-authority}
  - なぜ: 権力は自国の法律から得られるので、法律を変えると生産量が変わる（公式の説明）。不足の手順は2章「財政の安定」 [src: concepts_l_japanese.yml, concept_authority_desc] [src: 00_distribution_of_power.txt:35]
- [ ] 「政策」パネルの「政府」タブで利益集団の支持を見直し、支持が「怒り」の集団がいれば、3章「政治改革」の手順で運動活動を確かめる {#law-approval}
  - なぜ: 成立後の支持は一時的に大きく動き、長く残る。支持が「怒り」の集団は政治運動の活動を押し上げる（公式の説明） [src: concepts_l_japanese.yml, concept_approval_desc] [src: interfaces_l_japanese.yml, ig_approval_angry] [src: 00_defines.txt:158] [src: 00_defines.txt:162] [src: politics_panel_reform_government.gui:729]
- [ ] 制度と対応する法律を変えたら、「政策」パネルの「制度」タブで、その制度が使えるか確かめ、投資レベルを見直す {#law-institution}
  - なぜ: 一部の法律は制度を有効にして効果を変え、制度を無効にする法律もある（公式の説明） [src: tutorial_l_japanese.yml, lesson_enact_institution_law_how_2_desc] [src: 00_internal_security.txt:36]

### 新しい技術を獲得したとき

- [ ] 次の技術を選ぶ前に、「技術」パネルで同じ分野の前の時代の未研究の技術を確かめ、コストの上乗せと比べて研究の順を決める {#tech-old-era}
  - なぜ: 同じ分野の前の時代に未研究の技術があると、新しい技術に必要な革新が増える。数値は7章 [src: concepts_l_japanese.yml, concept_technology_era_ahead_of_time_penalty_desc] [src: 00_defines.txt:1862]
- [ ] 「政策」パネルの「法律」タブで解禁された法律を、州を右クリックして開くメニューの「布告」で解禁された布告を確かめる {#tech-unlock}
  - なぜ: 技術は、方式・施設・法律・布告・外交協定を解禁する。例は技術「法執行機関」が解禁する法律「国家警備」（公式の説明） [src: concepts_l_japanese.yml, concept_technology_desc] [src: 00_internal_security.txt:28] [src: right_click_menu.gui:6471]
- [ ] 技術を選ぶとき、警告「企業数の上限を超過」が出ていれば、「企業」パネルで企業を解散するか、上限を増やす技術を優先して研究する {#tech-company-limit}
  - なぜ: 上限を超えると、所有するすべての企業の生産量に厳重なペナルティが課される（公式の説明） [src: alerts_l_japanese.yml, alert_above_company_limit_desc] [src: alerts_l_japanese.yml, alert_above_company_limit_hint] [src: 00_alert_types.txt:128]

### 外交戦の前と後

- [ ] 外交戦を始める前に、標的国の国パネルの「外交」タブで、「以下から恩義があります」の一覧に自国がないか確かめる {#play-obligation}
  - なぜ: 恩義を負う相手には、外交戦を始められない（公式の説明） [src: concepts_l_japanese.yml, concept_obligation_desc] [src: interfaces_l_japanese.yml, OBLIGATIONS_OWED_FROM] [src: country_panel.gui:3765]
- [ ] 平時のうちに、「編隊」パネルの「動員」タブで動員オプションを設定する {#play-option}
  - なぜ: 動員オプションは平時に設定でき、動員時の商品のコストに響く。戦場で切り替えると組織力が一時的に失われることがある（公式の説明） [src: concepts_l_japanese.yml, concept_mobilization_option_desc] [src: alerts_l_japanese.yml, alert_low_organization_active_hint] [src: interfaces_l_japanese.yml, MILITARY_FORMATION_PANEL_MOBILIZATION_TAB]
- [ ] 将軍が足りなければ「編隊」パネルの「将軍の雇用」ボタンで雇用し、指揮上限が足りなければ将軍のパネルで昇進させる {#play-general}
  - なぜ: 昇進は行政力を払えばいつでもでき、将軍の指揮上限が増える（公式の説明） [src: tutorial_l_japanese.yml, lesson_recruit_promote_commander_how_1_desc] [src: tutorial_l_japanese.yml, lesson_recruit_promote_commander_how_6_desc] [src: tutorial_l_japanese.yml, lesson_recruit_promote_commander_how_10_desc] [src: concepts_l_japanese.yml, concept_command_limit_desc] [src: character_panel.gui:1594] [src: interfaces_l_japanese.yml, RECRUIT_GENERAL_BUTTON]
- [ ] 外交戦の初動で戦争目標を足す前に、「戦争目標を追加」の画面で目標ごとの悪名を、外交パネルで自国の悪名を確かめる {#late-infamy}
  - なぜ: 悪名は、革命・分離・統一などを除き、戦争目標を足した時点で付き、引き下がると75%、強制せず和平すると50%が戻る。他国の態度と外交協定の影響力コストにも響く（公式の説明）。段階は7章 [src: concepts_l_japanese.yml, concept_infamy_desc] [src: 00_defines.txt:1172] [src: 00_defines.txt:1174] [src: diplomatic_plays.md:8] [src: add_wargoal_panel.gui:536] [src: diplomatic_overview.gui:1815]
- [ ] 外交工作のフェーズでは、戦略を使って、関心ランクの高い国を懐柔して味方につける {#play-sway}
  - なぜ: 戦略の量はランクで決まる。懐柔では戦争目標や恩義を約束に出せ、AIが受けるかは関係と態度で決まる（公式の説明） [src: concepts_l_japanese.yml, concept_diplomatic_maneuvers_desc] [src: concepts_l_japanese.yml, concept_maneuver_desc] [src: concepts_l_japanese.yml, concept_sway_desc]
- [ ] 警告「…の恩義の失効」が出たら、失効前に、関係改善・外交協定・外交戦のどれかにその恩義を使う {#play-obligation-expiring}
  - なぜ: 恩義を負う国は、こちらに外交戦を始められず、こちらと対立する側にも加われない（公式の説明） [src: concepts_l_japanese.yml, concept_obligation_desc] [src: alerts_l_japanese.yml, alert_obligation_expiring_hint] [src: 00_alert_types.txt:507]
- [ ] 戦争へのカウントダウンに入ったら、軍事パネルの「全ての陸軍を動員」で動員し、将軍に戦線の命令を出す {#play-mobilize}
  - なぜ: 動員は商品を消費し、戦争が終わると自動で解除される。早く解除すると時間も費用もかかる（公式の説明）。戦争中は4章「戦争の崩れの予防」も見る [src: concepts_l_japanese.yml, concept_countdown_to_war_desc] [src: concepts_l_japanese.yml, concept_mobilize_army_desc] [src: concepts_l_japanese.yml, concept_army_desc] [src: interfaces_l_japanese.yml, MOBILIZE_ALL_MILITARY_FORMATIONS]
- [ ] 戦争が終わったら、徴兵された州で失業者が増えていないか確かめ、施設を増やして仕事を作る {#play-jobs}
  - なぜ: 戦後は徴兵された大隊が解散し、POPは元の職に戻れる保証がなく、仕事がなければ移民になりやすい（公式の説明） [src: concepts_l_japanese.yml, concept_conscription_center_desc] [src: concepts_l_japanese.yml, concept_unemployed_desc]

## 6. 困ったとき

**封鎖された州がある（重要アクション「…は…%封鎖されています」）**
- 見る場所: 重要アクションに並ぶ、封鎖された州とその効果 [src: alerts_l_japanese.yml, alert_blockaded_state_alert_desc] [src: 00_alert_types.txt:339]
- 打ち手: 戦闘で敵艦隊に勝てる艦隊に海軍任務「迎撃」を課し、関連する海上ノードへ派遣する。封鎖は隣接する港の世界市場へのアクセスを下げる（公式の説明） [src: alerts_l_japanese.yml, alert_blockaded_state_alert_hint] [src: concepts_l_japanese.yml, concept_blockade_desc]

**軍の組織力が落ちている（警告または怒りの重要アクション「組織力の低下: …」）**
- 見る場所: 並んだ編隊の組織力と、編隊のユニット数に対する指揮上限。戦線の編隊は警告、待機中の編隊は怒りの重要アクションに出る [src: alerts_l_japanese.yml, alert_low_organization_idle_desc] [src: 00_alert_types.txt:574] [src: 00_alert_types.txt:606]
- 打ち手: 将軍を昇進させて指揮上限を増やし、編隊は動かさずに回復を待つ。戦場で動員オプションを切り替えると、一時的に組織力が失われることがある（公式の説明） [src: alerts_l_japanese.yml, alert_low_organization_idle_hint] [src: concepts_l_japanese.yml, concept_organization_desc]

**条約を守れていない（警告「…の不履行」「…に違反しています」）**
- 見る場所: 警告に出た条約と、違反している条項の要件 [src: alerts_l_japanese.yml, alert_treaty_not_fulfilled_desc] [src: alerts_l_japanese.yml, alert_article_contravened_desc] [src: 00_alert_types.txt:1058] [src: 00_alert_types.txt:1073]
- 打ち手: 違反している条項の要件を満たす。無理なら条約から脱退する。違反をやめないと不履行と見なされ、条約が凍結または破棄される（公式の説明） [src: alerts_l_japanese.yml, alert_treaty_not_fulfilled_hint] [src: alerts_l_japanese.yml, alert_article_contravened_hint]

**革命が始まった（警告「革命」）**
- 見る場所: 警告から開く外交戦の画面 [src: alerts_l_japanese.yml, alert_revolution_alert_desc] [src: 00_alert_types.txt:154]
- 打ち手: 内戦でどちら側につくかを選び、味方側を成功させるために、必要なら他国を懐柔する。革命は急進化した政治運動から起こるので、予防は4章「急進派・財政の崩れの予防」（公式の説明） [src: alerts_l_japanese.yml, alert_revolution_alert_hint] [src: concepts_l_japanese.yml, concept_revolution_desc]

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|
| 時代の区切り | 1836〜1861／1862〜1886／1887〜1911／1911〜1936 | [src: 00_eras.txt:7] [src: 00_eras.txt:11] [src: 00_eras.txt:15] [src: 00_eras.txt:19] |
| 正当性の段階 | 0〜24 非正規政府（法律の制定に政治運動の支持が要る）／25〜49 不安定な政府（制定速度 −25%）／50〜74 対立する政府／75〜89 合法政府／90以上 正当なる政府（制定速度 +25%） | [src: 00_legitimacy_levels.txt:2] [src: 00_legitimacy_levels.txt:7] [src: 00_legitimacy_levels.txt:25] [src: 00_legitimacy_levels.txt:30] [src: 00_legitimacy_levels.txt:48] [src: 00_legitimacy_levels.txt:56] [src: 00_legitimacy_levels.txt:77] [src: 00_legitimacy_levels.txt:81] |
| 正当性の警告 | 25未満で警告「非正規政府」／25以上50未満で怒りの重要アクション「不安定な政府」 | [src: 00_alert_types.txt:419] [src: 00_alert_types.txt:741] |
| 正当性と急進派・体制派 | 50未満で毎月急進派が増え、75以上で毎月体制派が増える | [src: 00_legitimacy_levels.txt:10] [src: 00_legitimacy_levels.txt:33] [src: 00_legitimacy_levels.txt:62] [src: 00_legitimacy_levels.txt:84] |
| 行政力の不足／余剰 | 使用量が生産量の2倍で、徴収される税が100%減る（浪費税額 +1）。生産量が使用量の2倍で、州の建設速度 +10%。どちらも定義のコメントによる最大時の値 | [src: 00_code_static_modifiers.txt:573] [src: 00_code_static_modifiers.txt:579] |
| 権力の不足／余剰 | 使用量が生産量の2倍で、対立側の利益集団の支持 −10・政治運動由来の急進派 +20%。生産量が使用量の2倍で、法律の制定速度 +25% | [src: 00_code_static_modifiers.txt:586] [src: 00_code_static_modifiers.txt:592] [src: 00_code_static_modifiers.txt:593] |
| 影響力の不足／余剰 | 使用量が生産量の2倍で、威信 −50%。生産量が使用量の2倍で、悪名が薄れる速さ +25%。どちらも定義のコメントによる最大時の値 | [src: 00_code_static_modifiers.txt:600] [src: 00_code_static_modifiers.txt:613] |
| 金準備の上限 | 基本は年間GDPの0.2倍（最低1000）。超え、収支が黒字だと重要アクションが出る | [src: 00_defines.txt:541] [src: 00_defines.txt:542] [src: 00_alert_types.txt:836] [src: 00_alert_types.txt:841] |
| 商品の不足 | 供給が需要の50%を下回ると、使う施設に産出ペナルティ | [src: 00_defines.txt:419] |
| 市場アクセス | 100%未満で重要アクションが出る | [src: 00_alert_types.txt:927] |
| 生活水準の期待値 | 州のPOPの25%以上が期待値（最小）を下回ると重要アクションが出る | [src: 00_alert_types.txt:989] |
| 法律の制定 | 失敗後は730日、再試行できない。成功までに通るフェーズは3つ | [src: 00_defines.txt:171] [src: 00_defines.txt:181] |
| 政治運動の強化 | 基本の権力コストは200（チュートリアルも、強化の前提に権力200以上を求める） | [src: 00_defines.txt:283] [src: 00_tutorial_lessons_promote_ig.txt:131] |
| 布告「道路整備」 | 権力100。技術「中央集権化」で解禁 | [src: 00_decree.txt:18] [src: 00_decree.txt:20] |
| 布告「緊急救援」 | 州の徴税 −50%。技術「中央集権化」で解禁 | [src: 00_decree.txt:147] [src: 00_decree.txt:150] |
| 企業の繁栄度 | 100でボーナスが有効、75以下で止まる。怒りの重要アクションは繁栄度が100以上で伸びがマイナスのときに出る | [src: 00_defines.txt:664] [src: 00_defines.txt:665] [src: 00_alert_types.txt:771] [src: 00_alert_types.txt:772] |
| 布告「隣の芝は青い運動」 | 移住求心力 +20・+25%、権力100。技術「ロマン主義」で解禁 | [src: 00_decree.txt:897] [src: 00_decree.txt:898] [src: 00_decree.txt:901] [src: 00_decree.txt:903] |
| 制度の投資レベル | 1〜5 | [src: 00_defines.txt:293] [src: 00_defines.txt:294] |
| 運動活動 | 25%以上で運動が法律の制定に影響する／50%以上で毎月支持者が急進化し、反乱に変わりやすい | [src: 00_defines.txt:98] [src: 00_defines.txt:105] [src: 00_defines.txt:312] |
| 関心ランク | 「観察」は関与100以上／「積極的」は関与1000以上（外交戦の開始・参加が可能） | [src: interest_tier_types.txt:25] [src: interest_tier_types.txt:40] [src: interest_tier_types.txt:47] |
| 従属国の自由への願望 | 25未満が低、25〜74が中、75以上が高（高いと従属国の政治運動由来の急進派 +25%） | [src: 00_liberty_desire_levels.txt:2] [src: 00_liberty_desire_levels.txt:17] [src: 00_liberty_desire_levels.txt:27] [src: 00_liberty_desire_levels.txt:38] |
| 勢力ブロックの形成 | ランクが非承認大国以上。法律「孤立主義」では不可 | [src: 00_scripted_triggers.txt:56] [src: 00_scripted_triggers.txt:57] |
| 戦争支持率 | 25を下回ると警告が出る。定義では25以下で戦闘への不利な補正と急進化が始まる（コメントによる）。開戦12か月を過ぎると長引くほど目減りし、借入中と債務不履行中は下がり、金準備があると上がる | [src: 00_alert_types.txt:48] [src: 00_defines.txt:1203] [src: 00_defines.txt:2136] [src: 00_defines.txt:2137] [src: 00_defines.txt:2139] [src: 00_defines.txt:2140] [src: 00_defines.txt:2143] |
| 戦争目標の強制 | 掌握中は毎週5ずつ進み、100で強制される。掌握をやめると毎週5ずつ減る。国有化の強制・自治権の拡大・独立・勢力ブロックを離脱の目標は進むのも減るのも毎週2 | [src: 00_defines.txt:2192] [src: 00_defines.txt:2193] [src: 00_defines.txt:2195] [src: 06_force_nationalization.txt:31] [src: 06_force_nationalization.txt:32] [src: 09_increase_autonomy.txt:32] [src: 09_increase_autonomy.txt:33] [src: 10_independence.txt:33] [src: 10_independence.txt:34] [src: 12_leave_power_bloc.txt:35] [src: 12_leave_power_bloc.txt:36] |
| 戦争目標の取り下げ | 開戦24か月以降、12か月掌握されない目標は取り下げられる。3か月前に警告 | [src: 00_defines.txt:2196] [src: 00_defines.txt:2197] [src: 00_defines.txt:2198] |
| 悪名 | 指標「悪名」が25超で段階「不信」、50超で段階「悪名」、100超で段階「疎外」。毎年5ずつ薄れる。段階「疎外」の国には、列強が外交戦「分相応」を起こせる | [src: 00_defines.txt:1003] [src: 00_defines.txt:1004] [src: 00_defines.txt:1005] [src: 00_defines.txt:1006] [src: diplomacy_l_japanese.yml, infamy_infamous] [src: diplomacy_l_japanese.yml, infamy_notorious] [src: diplomacy_l_japanese.yml, infamy_pariah] [src: 00_diplomatic_plays.txt:678] [src: diplomatic_plays_l_japanese.yml, war_goal_contain_threat_type_name] |
| ランクの優遇 | 貸付歩合は列強 −50%、大国 −25%。影響力の生産は列強 +1000、大国 +750 | [src: 00_country_ranks.txt:42] [src: 00_country_ranks.txt:44] [src: 00_country_ranks.txt:80] [src: 00_country_ranks.txt:82] |
| 同じ分野の前の時代の未研究技術 | 1つにつきコストの0.25倍×時代の差（定義のコメントによる） | [src: 00_defines.txt:1862] |

## 8. 用語

完全版は [用語対照表](viewer.html?file=vic3/localization-reference.md)。

- 警告（Alert）／重要アクション（Important Action）／怒りの重要アクション（Angry Important Action）／現在の状況（Current Situation）
- 行政力（Bureaucracy）／権力（Authority）／影響力（Influence）／キャパシティ（Capacity）／浪費税額（Tax Waste）
- 金準備（Gold Reserves）／債務（Loans）／信用枠（Credit）／債務不履行（Default）
- 課税レベル（Taxation Level）／消費税（Consumption Tax）／国家公務員の給金（Government Wages）
- 建設局（Construction Sector）／資材（Construction）／建設キュー（Construction Queue）／投資プール（Investment Pool）／政府の建設（Government Construction）／民間の建設（Private Construction）
- 生産性（Productivity）／方式（Production Method）／取引所（Trade Center）／売り注文（Sell Order）／行政品（Government Good）
- 市場アクセス（Market Access）／インフラ（Infrastructure）
- 飢饉（Famine）／食料保障（Food Security）／生活水準（Standard of Living）／生活水準の期待値（最小）（Minimum Expected Standard of Living）
- 布告（Decree）／道路整備（Road Maintenance）／緊急救援（Emergency Relief）
- 正当性（Legitimacy）／利益集団（Interest Group）／政治運動（Political Movement）／強化（Bolster）／抑圧（Suppress）
- 法律の制定（Enactment of Laws）／制定成功（Enactment Success）／政府改革（Government Reform）／制度（Institution）
- 非正規政府（Illegitimate Government）／不安定な政府（Unstable Government）／対立する政府（Contested Government）／合法政府（Legitimate Government）／正当なる政府（Righteous Government）
- 革新（Innovation）／技術の普及（Technology Spread）／官僚制（Bureaucracy）
- 企業（Company）／繁栄度（Prosperity）／生産量（Throughput）
- ジャーナル（Journal）／ジャーナル記事（Journal Entry）
- 移住求心力（Migration Attraction）／隣の芝は青い運動（Greener Grass Campaign）
- 貿易キャパシティ（Trade Capacity）
- 投資レベル（Investment Level）／治安維持（Home Affairs）／法執行機関（Law Enforcement）
- 運動活動（Movement Activism）／急進派（Radical）／体制派（Loyalist）／支持（Approval）
- 政治的圧力団体（Political Lobby）／宥和（Appeasement）
- 戦略的重要地域（Strategic Region）／関与（Involvement）／関心（Interest）／関心ランク（Interest Tier）／外交レンズ（Diplomatic Lens）／政治レンズ（Political Lens）
- 外交戦（Diplomatic Play）／外交的要求（Diplomatic Demand）／初動（Opening Moves）／外交工作（Diplomatic Maneuvers）／戦争へのカウントダウン（Countdown to War）／戦争目標を掌握（Controlled War Goal）
- 戦争支持率（War Support）／訓練率（Training Rate）
- 編隊（Formation）／戦力投射（Power Projection）／威信（Prestige）／軍隊の給金（Military Wage）
- 従属国（Subject）／自由への願望（Liberty Desire）
- 勢力ブロック（Power Bloc）／アイデンティティの柱（Central Identity Pillar）／原則（Principle）／権限（Mandate）／勢力ブロックリーダー（Power Bloc Leader）
- ランク（Rank）／列強（Great Power）／大国（Major Power）／非承認大国（Unrecognized Major Power）／悪名（Infamy）／貸付歩合（Loan interest rate）
- 条項（Article）／外交協定（Diplomatic Pact）／関係（Relations）／態度（Attitude）／ライバル（Rivalry）／拘束期間（Binding Period）
- 財力（Wealth）／主要文化（Primary Culture）
- 恩義（Obligation）／戦略（Maneuver）／懐柔（Sway）／不履行（Non-Fulfillment）／違反（Contravention）
- 動員オプション（Mobilization Option）／組織力（Organization）／指揮上限（Command Limit）／海軍任務（Naval Mission）／迎撃（Interception）／海上ノード（Sea Node）

## 9. 出典

### 一次情報

- パスは `Victoria 3/game` フォルダからの相対。同名のファイルが複数あるものは相対パスで書く
- `common/technology/eras/00_eras.txt`（年はコメント表記）
- `common/alert_types/00_alert_types.txt`（警告・重要アクションの発生条件）
- `common/tutorial_lessons/00_tutorial_lessons_promote_ig.txt`（政治運動の強化の前提）
- `common/legitimacy_levels/00_legitimacy_levels.txt`（正当性の段階と効果）
- `common/static_modifiers/00_code_static_modifiers.txt`（キャパシティの不足・余剰の効果）
- `common/defines/00_defines.txt`（金準備の上限・商品の不足・法律の制定・強化のコスト）
- `common/decrees/00_decree.txt`（布告）
- `common/buildings/13_construction.txt`、`common/buildings/07_government.txt`（建設局・行政府の解禁技術）
- `gui/construction_queue.gui`（建設パネルの建設キュー表示）
- `common/technology/technologies/30_society.txt`（企業の設立枠）
- `common/institutions/00_institutions.txt`、`common/interest_tier_types/interest_tier_types.txt`、`common/liberty_desire_levels/00_liberty_desire_levels.txt`、`common/country_ranks/00_country_ranks.txt`、`common/laws/00_distribution_of_power.txt`、`common/laws/00_internal_security.txt`
- `common/scripted_triggers/00_scripted_triggers.txt`（勢力ブロックを形成できる条件）、`common/power_bloc_principles/00_power_bloc_principles.txt`（原則の DLC 条件）、`common/scripted_rules/00_scripted_rules.txt`、`dlc_metadata/00_dlc_metadata.txt`
- `common/tutorial_lessons/00_tutorial_lessons_incorporate_state.txt`（州の編入を行う画面）
- `common/diplomatic_plays/00_diplomatic_plays.txt`、`diplomatic_plays.md`
- `common/war_goal_types/` の `06_force_nationalization.txt`、`09_increase_autonomy.txt`、`10_independence.txt`、`12_leave_power_bloc.txt`、`war_goal_types.md`
- `common/journal_entries/01_coup.txt`
- `gui/` の `market_panel.gui`、`politics_panel_institutions.gui`、`politics_panel_reform_government.gui`、`politics_panel_overview.gui`、`diplomatic_overview.gui`、`country_panel.gui`、`right_click_menu.gui`、`important_actions_list.gui`、`budget_panel.gui`、`military_formation_panel.gui`、`character_panel.gui`、`power_bloc_panel.gui`、`add_wargoal_panel.gui`、`war_panel.gui`（画面の構成）
- `localization/english/alerts_l_english.yml`、`interfaces_l_english.yml`
- `localization/japanese/alerts_l_japanese.yml`、`tutorial_l_japanese.yml`、`concepts_l_japanese.yml`、`interfaces_l_japanese.yml`、`diplomacy_l_japanese.yml`、`diplomatic_plays_l_japanese.yml`（警告・チュートリアル・用語説明・画面の文言）

### コミュニティ情報

- なし
