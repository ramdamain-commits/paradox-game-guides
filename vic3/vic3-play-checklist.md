# VIC3 プレイ中チェックリスト
> 対象パッチ: 1.14 オープンベータ（release/1.14.5・ビルド 25629520）・変動注意 ／ 最終確認日: 2026-10-19

どの国でも共通の「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。国ごとの事情は扱わない。DLC はすべてある前提で書き、DLC が要る項目には「（DLC名 が必要）」と付ける。「（公式の説明）」は、ゲーム内のヒント・チュートリアル・用語説明が根拠で、効果をスクリプトでは確かめていない記述。

## 1. 開始直後（ポーズ中にやること）

- [ ] 画面上部の警告アイコンと「現在の状況」ボタンを開き、赤い項目から順に内容を確かめる {#start-alerts}
  - なぜ: 警告は画面中央上部にアイコンで出て、重要アクションは「現在の状況」のリストに出る。赤いものは「怒りの重要アクション」。このチェックリストの「…が出たら」は、この2つを指す（公式の説明） [src: concepts_l_japanese.yml, concept_alert_settings_alert_desc] [src: concepts_l_japanese.yml, concept_alert_settings_important_action_desc] [src: concepts_l_japanese.yml, concept_alert_settings_angry_important_action_desc]
- [ ] 警告「アクティブな研究がありません」が出ていれば、「技術」パネルで3つの技術ツリーから研究する技術を選ぶ {#start-research}
  - なぜ: 研究していないと、生み出される革新がすべて恒常的な技術拡散に回る（公式の説明） [src: alerts_l_japanese.yml, alert_has_no_research_alert_desc] [src: alerts_l_japanese.yml, alert_has_no_research_alert_hint] [src: 00_alert_types.txt:74]
- [ ] 「予算」パネルの「概要」タブで週間収支を確かめ、赤字なら2章「財政の安定」の手順で歳入を増やすか支出を減らす {#start-budget}
  - なぜ: 収支がマイナスだと金準備が先に減り、尽きると債務が増える。債務が信用枠を超えると債務不履行になり、進行中の建設がすべて止まる（公式の説明） [src: concepts_l_japanese.yml, concept_gold_reserves_desc] [src: concepts_l_japanese.yml, concept_default_desc]
- [ ] 画面上部の行政力・権力・影響力にそれぞれカーソルを合わせ、収支が0未満のものがないか確かめる {#start-capacity}
  - なぜ: 3つは貯めて使うものではなく、毎週の生産と使用の差で決まる。不足すると多大なペナルティを受け、少し余らせると小さなボーナスが付く（公式の説明）。不足と余剰の効果は7章 [src: concepts_l_japanese.yml, concept_capacity_desc] [src: 00_code_static_modifiers.txt:577] [src: 00_code_static_modifiers.txt:590] [src: 00_code_static_modifiers.txt:611]
- [ ] 「政策」パネルで、政府内の利益集団と正当性の値を確かめる {#start-ig}
  - なぜ: 正当性は、政府内の利益集団と法律の組み合わせがどれだけ合っているかを示す（公式の説明）。効果が変わるのは段階の境目で、25未満は制定に政治運動の支持が要り、25〜49は制定速度 −25%、90以上は +25%。段階ごとの効果は7章 [src: concepts_l_japanese.yml, concept_legitimacy_desc] [src: 00_legitimacy_levels.txt:7] [src: 00_legitimacy_levels.txt:30]
- [ ] 「建設」パネルで、建設キューの推定建設期間と、政府の建設・民間の建設の件数を確かめる {#start-construction}
  - なぜ: 建てる施設は建設キューに入り、資材が使えるようになると先頭から着工する。推定建設期間が長いなら、施設を足しても着工は後になる（公式の説明） [src: concepts_l_japanese.yml, concept_construction_queue_desc] [src: interfaces_l_japanese.yml, QUEUE_CONSTRUCTION_POINTS_SUMMARY_TOOLTIP] [src: construction_queue.gui:106]

## 2. 序盤（1836〜1861）

### 財政の安定

到達目標: 週間収支が黒字で、行政力・権力・影響力が0以上、債務が信用枠に迫っていない状態にする。

- [ ] 警告「債務不履行中」が出たとき、または金準備が尽きて赤字が続くときは、「予算」パネルの「概要」タブで課税レベルを上げるか、新しい消費税を課す {#early-deficit}
  - なぜ: 増税は歳入をすぐ増やす最も簡単な方法だが、財力の低下や社会不安の恐れがある（公式の説明）。消費税は課す商品ごとに権力を使い、税の上げ下げは正当性にも響く [src: tutorial_l_japanese.yml, lesson_budget_balance_2_desc] [src: concepts_l_japanese.yml, concept_consumption_tax_desc] [src: concepts_l_japanese.yml, concept_legitimacy_desc] [src: 00_alert_types.txt:35]
- [ ] 増税しても収支が戻らないときは、進行中の政府の建設を中断する {#early-build-stop}
  - なぜ: 建設費は固定費ではないが、建設中は国庫の負担になる。赤字を解消してから再開できる。民間の建設は投資プールの資金で進むので、中断できるのは政府の建設だけ（公式の説明） [src: tutorial_l_japanese.yml, lesson_budget_balance_how_3_desc] [src: alerts_l_japanese.yml, alert_country_default_hint] [src: concepts_l_japanese.yml, concept_private_construction_desc]
- [ ] 「予算」パネルの「州」タブで支出の大きい政府施設を探して縮小するか、国家公務員の給金と軍事賃金を下げる {#early-gov-cost}
  - なぜ: 政府施設の運営費は固定費。縮小すると支出を恒久的に減らせるが、その施設レベルの恩恵を失う。賃金はいつでも戻せるが、変更の結果は説明を読んで確かめる（公式の説明） [src: tutorial_l_japanese.yml, lesson_budget_balance_how_4_desc] [src: tutorial_l_japanese.yml, lesson_budget_balance_how_5_desc] [src: tutorial_l_japanese.yml, lesson_budget_balance_how_6_desc]
- [ ] 「予算」パネルの「資産」タブで、債務の元金が信用枠に近づいていないか確かめる {#early-debt}
  - なぜ: 元金が信用枠に達すると債務不履行になり、進行中の建設がすべて止まる。施設の生産量にも、時間とともに重くなるペナルティが付く。収支が黒字に戻るか、破産を宣言すると解除される（公式の説明） [src: concepts_l_japanese.yml, concept_default_desc] [src: tutorial_l_japanese.yml, lesson_budget_balance_why_6_desc] [src: tutorial_l_japanese.yml, lesson_budget_balance_why_7_desc]
- [ ] 重要アクション「金の備蓄」が出たら、支出を増やすか税を下げる {#early-gold}
  - なぜ: 金準備が上限を超えると、経済とPOPから資金を奪って財力を減らす（公式の説明）。上限の基本は年間GDPの0.2倍。数値は7章 [src: alerts_l_japanese.yml, alert_stockpiling_gold_alert_hint] [src: 00_alert_types.txt:836] [src: 00_defines.txt:542]
- [ ] 行政力が0未満なら、行政府を増築するか、より効率的な生産方式へ切り替える {#early-bur}
  - なぜ: 行政力は主に行政府が生み、税の徴収と制度の維持に使われる。不足すると税の浪費が出て、経済が急に鈍る（公式の説明）。行政府の解禁には技術「官僚制」が要る。数値は7章 [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_3_desc] [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_4_desc] [src: 00_code_static_modifiers.txt:577] [src: common/buildings/07_government.txt:9]
- [ ] 権力が0未満なら、不要な布告を取り消し、課す必要のない消費税を外す {#early-aut}
  - なぜ: 権力は布告・消費税・政治運動の強化と抑圧に使われ、法律（特にリベラル色の低いもの）が生む。不足すると対立側の利益集団の支持が下がり、政治運動と急進派が勢いづく（公式の説明）。長期には、権力を生む厳格な法律も手段になる。数値は7章 [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_5_desc] [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_6_desc] [src: 00_code_static_modifiers.txt:590]
- [ ] 影響力が0未満なら、維持している外交協定のうち不要なものを破棄する {#early-inf}
  - なぜ: 影響力は外交協定（従属国との関係を含む）の維持に使われる。不足すると威信が下がり、ランクと影響力の生成も落ちる（公式の説明）。不足が小さければ、ライバル関係の確立も手段になる。数値は7章 [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_7_desc] [src: tutorial_l_japanese.yml, lesson_fix_capacity_deficit_how_8_desc] [src: 00_code_static_modifiers.txt:611]

### 建設の回し方

到達目標: 資材を切らさず、生産性の高い施設に建設を回し、赤字の施設と商品の不足を放置していない状態にする。

- [ ] 重要アクション「投資プールのための資材が不足」が出たら、「建設」パネルを開き、建設局を増やすか、建設局の生産方式を上位に切り替える {#early-sector}
  - なぜ: 投資プールに入ってくる資金を使い切れるだけの資材を作れていない状態（公式の説明）。建設局は技術「都市化」で解禁され、建てられないときはこの技術が研究済みか確かめる [src: alerts_l_japanese.yml, alert_insufficient_construction_for_investment_desc] [src: alerts_l_japanese.yml, alert_insufficient_construction_for_investment_hint] [src: 00_alert_types.txt:621] [src: common/buildings/13_construction.txt:13]
- [ ] 「施設」パネルの一覧で、生産性の高い施設を探し、「+」ボタンか右クリックで拡張する {#early-expand}
  - なぜ: 拡張先は利益でなく生産性で選ぶ。生産性は従業員1人あたりが年間に生む経済価値の目安で、賃金・税・助成・配当の違いに左右されない（公式の説明） [src: tutorial_l_japanese.yml, lesson_expand_productive_building_how_3_desc] [src: tutorial_l_japanese.yml, lesson_expand_productive_building_how_4_desc] [src: concepts_l_japanese.yml, concept_productivity_desc]
- [ ] 拡張した施設の生産性が下がっていないか、しばらくして「施設」パネルで見直し、下がっていれば同じ施設の拡張を止める {#early-oversupply}
  - なぜ: 供給過多になると商品の市場価格が下がり、生産性は時間とともに低下する。生産性の高い施設だけを拡張し続けるのが最適とは限らない（公式の説明） [src: tutorial_l_japanese.yml, lesson_expand_productive_building_why_5_desc]
- [ ] 生産性の低い施設は、詳細パネルで投入商品と産出商品の価格を見て、原因が高い投入か安い産出かを突き止める {#early-unprofitable}
  - なぜ: 投入が高いなら、その商品を作る施設を拡張するか輸入して価格を抑える。産出が安いなら、その商品を使う施設を拡張するか、他国の市場へ輸出する。輸出入には取引所が要る（公式の説明） [src: tutorial_l_japanese.yml, lesson_fix_unproductive_building_how_2_desc] [src: tutorial_l_japanese.yml, lesson_fix_unproductive_building_how_3_desc] [src: tutorial_l_japanese.yml, lesson_fix_unproductive_building_how_4_desc]
- [ ] 重要アクション「…における（商品）の不足」が出たら、その商品の売り注文を増やす {#early-shortage}
  - なぜ: 供給が需要の50%を下回ると、その商品を使う施設に産出ペナルティが出る。売り注文は、その商品を作る施設の拡張、産地の州のインフラ改善による市場アクセスの向上、世界市場からの輸入（取引所が要る）で増える。電力・サービスなど州内で回る商品の不足は、その州の生産量を増やす（公式の説明）。数値は7章 [src: alerts_l_japanese.yml, alert_market_goods_shortage_hint] [src: alerts_l_japanese.yml, alert_state_goods_shortage_hint] [src: 00_alert_types.txt:781] [src: 00_alert_types.txt:797] [src: 00_defines.txt:419]
- [ ] 重要アクション「…の市場アクセスは、…%です」や警告「…は孤立したです」が出たら、その州に港か鉄道を建てる {#early-infra}
  - なぜ: 市場アクセスは100%から始まり、州のインフラ使用がインフラを超えると下がる。孤立した州は市場で売買できない。布告「道路整備」（技術「中央集権化」、権力100）でも補えるが、権力に限りがあるので一時しのぎにとどめる（公式の説明）。数値は7章 [src: concepts_l_japanese.yml, concept_market_access_desc] [src: alerts_l_japanese.yml, alert_low_market_access_alert_hint] [src: alerts_l_japanese.yml, alert_isolated_state_alert_hint] [src: tutorial_l_japanese.yml, lesson_market_access_with_railways_why_2_desc] [src: 00_alert_types.txt:927] [src: 00_alert_types.txt:477] [src: 00_decree.txt:20]
- [ ] 警告「…での飢饉」が出たら、「市場」パネルの「食料保障」タブで被害の州を確かめ、基本的な食料を満たす商品を作る施設を建てるか、その商品を輸入する {#early-food}
  - なぜ: 施設や輸入が効くまでには時間がかかり、布告「緊急救援」のほうが早く効くことがある（公式の説明）。ただしこの布告は州の徴税を半減させ、技術「中央集権化」で解禁される。数値は7章 [src: alerts_l_japanese.yml, alert_famine_alert_hint] [src: 00_alert_types.txt:459] [src: 00_decree.txt:150]
- [ ] 新しい生産方式が解禁されたら、投入商品の価格と不足、必要な職業の資格を持つPOPの数を確かめてから切り替える {#early-pm}
  - なぜ: 投入商品が高い・不足しているときや、その生産方式に必要な資格を持つPOPが乏しいときは、近代化を急がないほうがよい（公式の説明） [src: tutorial_l_japanese.yml, lesson_production_methods_why_5_desc]
- [ ] 重要アクション「…が生活水準の期待値（最小）を下回っています」が出たら、その州の仕事を増やしてPOPの収入を上げる {#early-sol}
  - なぜ: 州のPOPの25%以上が期待値を下回ると出る。仕事が増えて収入が上がれば生活水準が上がる（公式の説明）。数値は7章 [src: alerts_l_japanese.yml, alert_low_expected_sol_in_state_hint] [src: 00_alert_types.txt:989]

### 最初の法改正

到達目標: 正当性と利益集団の支持を保ったまま、最初の法律を失敗せずに通す。

- [ ] 「政策」パネルの「法律」タブで、制定したい法律の制定成功率を確かめる {#early-law-check}
  - なぜ: 制定には、政府内の利益集団の少なくとも1つが支持するか、現在の政治運動が支持するか、成功率が別の理由でプラスになっている必要がある（公式の説明） [src: concepts_l_japanese.yml, concept_enactment_of_laws_potential] [src: tutorial_l_japanese.yml, lesson_enact_institution_law_how_1_desc] [src: tutorial_l_japanese.yml, lesson_enact_institution_law_how_3_desc]
- [ ] 制定成功率がマイナスの法律は、制定を始めない {#early-law-fail}
  - なぜ: 成功率が0を下回るなどで後退が重なると制定に失敗し、730日たつまでその法律を再び試せない。制定は3つのフェーズを通る（公式の説明）。数値は7章 [src: concepts_l_japanese.yml, concept_enactment_setback_desc] [src: concepts_l_japanese.yml, concept_enactment_phase_desc] [src: 00_defines.txt:171] [src: 00_defines.txt:181]
- [ ] 支持が足りないときは、「政策」パネルの「概要」タブで、通したい法律を支持する政治運動を選んで強化する {#early-bolster}
  - なぜ: 強化された運動は、時間とともに支持者と支持が増え、利益集団の思想に影響して法律を通しやすくする。強化には権力が要り、使えるかは「言論の自由」の法律グループの現行法で決まる（公式の説明）。数値は7章 [src: tutorial_l_japanese.yml, lesson_promote_movement_how_1_desc] [src: tutorial_l_japanese.yml, lesson_promote_movement_how_5_desc] [src: tutorial_l_japanese.yml, lesson_promote_movement_why_3_desc] [src: 00_defines.txt:283] [src: 00_tutorial_lessons_promote_ig.txt:131]
- [ ] 警告「フリー政府改革」が出ている間に、「政策」パネルの「政府」タブで「政府改革」ボタンを押し、政府内の利益集団の構成を見直す {#early-reform-free}
  - なぜ: 最近の選挙により、表示された期限内に行う次の政府改革は急進派を生まない。ふつうは、権力を持っていた集団を政府から外すと急進派が出て、改革を頻繁に行うと政情が大きく不安定になる（公式の説明） [src: alerts_l_japanese.yml, alert_free_government_reform_desc] [src: tutorial_l_japanese.yml, lesson_reform_government_how_5_desc] [src: 00_alert_types.txt:141]
- [ ] 警告「非正規政府」や重要アクション「不安定な政府」が出たら、「政策」パネルの「政府」タブで「政府改革」ボタンを押し、正当性が上がる利益集団の組み合わせを試す {#early-reform-legit}
  - なぜ: 構成は確定するまで適用されず、試し直せる（公式の説明）。正当性が25〜49なら制定速度 −25%、25未満なら制定に政治運動の支持が要る。段階ごとの効果は7章 [src: tutorial_l_japanese.yml, lesson_reform_government_how_3_desc] [src: alerts_l_japanese.yml, alert_low_legitimacy_alert_hint] [src: 00_alert_types.txt:419] [src: 00_alert_types.txt:741] [src: 00_legitimacy_levels.txt:7] [src: 00_legitimacy_levels.txt:30]

## 3. 中盤（1862〜1886）

### 産業化

到達目標: 企業の設立枠と移住の流れを使い切り、産業の効率が落ちる兆しを放置していない状態にする。

- [ ] 警告「新たな企業を設立できる」が出たら、「企業」パネルで設立できる企業の条件を読み、「設立」を押す {#mid-company-new}
  - なぜ: 企業を設立すると、その企業に関連する施設の生産量と建設効率が上がる（公式の説明）。設立できる数は技術「企業チャーター」と「株式会社」でそれぞれ1増える [src: alerts_l_japanese.yml, alert_can_establish_company_hint] [src: concepts_l_japanese.yml, concept_company_desc] [src: tutorial_l_japanese.yml, lesson_establish_company_how_2_desc] [src: 00_alert_types.txt:115] [src: 30_society.txt:189] [src: 30_society.txt:619]
- [ ] 怒りの重要アクション「（企業名）の繁栄度が減少」が出たら、その企業に関連する施設のうち生産性の低いものを、2章「建設の回し方」の手順で立て直す {#mid-company-prosperity}
  - なぜ: 繁栄度は施設の生産性などで決まる（公式の説明）。国へのボーナスは100で有効になり、75以下で止まる。この警告は、繁栄度が100以上で伸びがマイナスの企業に出る [src: concepts_l_japanese.yml, concept_prosperity_desc] [src: alerts_l_japanese.yml, alert_company_losing_prosperity_hint] [src: 00_defines.txt:664] [src: 00_defines.txt:665] [src: 00_alert_types.txt:771] [src: 00_alert_types.txt:772]
- [ ] 施設の人手が足りない州は、州にカーソルを合わせて移住求心力を確かめ、低ければ布告「隣の芝は青い運動」を出す {#mid-immigration}
  - なぜ: 同じ市場の中で、移住求心力の低い州から高い州へ人が移り、失業者は求心力を下げる（公式の説明）。布告は求心力を +20 かつ +25% 上げ、権力100を使う。技術「ロマン主義」で解禁される [src: concepts_l_japanese.yml, concept_migration_desc] [src: concepts_l_japanese.yml, concept_migration_pull_desc] [src: tutorial_l_japanese.yml, lesson_increase_immigration_how_2_desc] [src: 00_decree.txt:897] [src: 00_decree.txt:898] [src: 00_decree.txt:901] [src: 00_decree.txt:903]

### 市場と貿易

到達目標: 貿易キャパシティに余裕があり、政府が買う商品の高騰を放置していない状態にする。

- [ ] 「市場」パネルの「貿易」タブ上部で、貿易キャパシティの使用量が総量に近づいていないか確かめ、近ければ取引所を増築する {#mid-trade-capacity}
  - なぜ: 貿易キャパシティは取引所のレベルが生み、世界市場との貿易に使われる（公式の説明） [src: concepts_l_japanese.yml, concept_trade_capacity_desc] [src: interfaces_l_japanese.yml, MARKET_COUNTRY_TRADE_CAPACITY] [src: interfaces_l_japanese.yml, MARKET_PANEL_WORLD_MARKET_TRADE] [src: market_panel.gui:155]
- [ ] 重要アクションで、政府の施設が使う商品が高価だと出たら、商品パネルを開いて、その商品の生産を増やすか輸入する {#mid-expensive-goods}
  - なぜ: 価格は、施設や生産方式で生産量を増やすか他国から手に入れると下がる。関税や消費税の変更が効くこともある（公式の説明） [src: alerts_l_japanese.yml, alert_expensive_goods_alert_hint_common] [src: alerts_l_japanese.yml, alert_expensive_government_goods_alert_desc] [src: 00_alert_types.txt:952]

### 政治改革

到達目標: 制度への投資と、急進化する運動・圧力団体の確認を、定期的に回している状態にする。

- [ ] 「政策」パネルの「制度」タブで、解禁済みの制度の投資レベルを確かめ、行政力に余裕があれば上げる {#mid-institution}
  - なぜ: 制度は編入州に利益を与え、維持に行政力を使う。レベルが高いほどコストも効果も大きい（公式の説明）。レベルは1〜5。制度は、対応する法律を制定すると使えるようになる [src: concepts_l_japanese.yml, concept_institution_desc] [src: tutorial_l_japanese.yml, lesson_enact_institution_law_why_4_desc] [src: 00_defines.txt:293] [src: 00_defines.txt:294] [src: politics_panel_institutions.gui:328]
- [ ] 「政策」パネルの「概要」タブで政治運動の運動活動の予測を確かめ、50%を超えそうな運動は、支持者の生活水準を上げて急進派を減らすか、権力で抑圧する {#mid-movement}
  - なぜ: 運動活動が25%以上だと、運動が支持・反対する法律の制定に影響が出る。50%以上で毎月支持者が急進化し、反乱（革命・分離）に変わりやすくなる。急進派は生活水準が期待値を下回ると現れる（公式の説明）。抑圧には権力を使う [src: concepts_l_japanese.yml, concept_activism_desc] [src: concepts_l_japanese.yml, concept_radical_desc] [src: concepts_l_japanese.yml, concept_suppress_desc] [src: 00_defines.txt:105] [src: 00_defines.txt:98] [src: 00_defines.txt:312]
- [ ] 「政策」パネルの「概要」タブの「政治的圧力団体」一覧で宥和の低い圧力団体を探し、その対象国への外交アクションを見直す {#mid-lobby}
  - なぜ: 宥和が上がると、その圧力団体を支える利益集団の支持が増える。支持派は友好的な外交アクションで、反対派は敵対的な外交アクションで宥和が上がる。圧力団体の大きさは、対象国との外交協定にかかる影響力のコストに響く（公式の説明） [src: concepts_l_japanese.yml, concept_political_lobby_appeasement_desc] [src: tutorial_l_japanese.yml, lesson_lobbies_how_3_desc] [src: tutorial_l_japanese.yml, lesson_lobbies_how_4_desc] [src: politics_panel_overview.gui:1612]

### 勢力拡大

到達目標: 狙う地域の関心ランクを満たし、軍・従属国・編入待ちの州が国力を超えていない状態にする。

- [ ] 外交戦を起こしたい戦略的重要地域では、外交レンズの「関心の宣言」を使い、関与を積んで関心ランクを「積極的」以上にする {#mid-interest}
  - なぜ: 関心ランクが十分高いことが、その地域の外交戦を始める・参加する条件になる。関与は軍の駐在・州の所有・請求権・条約などで増える（公式の説明）。「積極的」は関与1000以上 [src: concepts_l_japanese.yml, concept_interest_desc] [src: interfaces_l_japanese.yml, HOW_TO_INCREASE_INVOLVEMENT] [src: interfaces_l_japanese.yml, declare_interest_tooltip] [src: interest_tier_types.txt:40] [src: interest_tier_types.txt:47]
- [ ] 軍事パネルで兵力を確かめ、足りなければ編隊パネルのボタンから、余剰の労働者がいてインフラと軍需品も整った州に兵舎を建てる {#mid-army}
  - なぜ: すべてのユニットは戦力投射に寄与し、威信になる。維持費は軍隊の給金と軍需品が主で、戦争中の大隊の動員で増える。拡張費が国庫で賄える額を超えないようにする（公式の説明） [src: tutorial_l_japanese.yml, lesson_expand_military_how_3_desc] [src: tutorial_l_japanese.yml, lesson_expand_military_why_2_desc] [src: tutorial_l_japanese.yml, lesson_expand_military_why_3_desc]
- [ ] 戦争で目的を果たすときは、外交レンズの「外交戦」タブで開始する外交戦を選び、「初動」の間に戦争目標を足す {#mid-play}
  - なぜ: 外交戦は「初動」「外交工作」「戦争へのカウントダウン」の3フェーズで進み、どちらも引かなければ戦争になる。初動の間に戦争目標を足さないと、戦争賠償金の目標が自動で付く（公式の説明） [src: tutorial_l_japanese.yml, lesson_start_diplomatic_play_how_3_desc] [src: alerts_l_japanese.yml, alert_has_no_war_goal_alert_desc] [src: alerts_l_japanese.yml, alert_has_no_war_goal_alert_hint] [src: 00_alert_types.txt:209]
- [ ] 戦争で未編入州を得たら、行政力に余裕のあるうちに、政治レンズの「州アクション」タブで「州の編入」を始める {#mid-incorporate}
  - なぜ: 編入した州は税を払い、制度の恩恵を受ける。行政力の全額は開始時にかかり、必要な年数は主要文化との違いで変わる（公式の説明） [src: tutorial_l_japanese.yml, lesson_incorporate_state_how_3_desc] [src: tutorial_l_japanese.yml, lesson_incorporate_state_complete_desc] [src: interfaces_l_japanese.yml, incorporate_state] [src: 00_tutorial_lessons_incorporate_state.txt:27] [src: 00_tutorial_lessons_incorporate_state.txt:28]
- [ ] 外交パネルの「従属国」タブで従属国の自由への願望を確かめ、高い従属国は自治権を拡大し、低い従属国は自治権を縮小する {#mid-subject}
  - なぜ: 願望が高いと、従属国は独立のために外交戦を起こしうる。自治権の拡大・縮小で、願望と支配率を調整できる（公式の説明）。願望は25未満が低、75以上が高で、高いと従属国の政治運動由来の急進派が +25% になる [src: tutorial_l_japanese.yml, lesson_subject_liberty_how_5_desc] [src: tutorial_l_japanese.yml, lesson_subject_liberty_why_1_desc] [src: 00_liberty_desire_levels.txt:17] [src: 00_liberty_desire_levels.txt:27] [src: 00_liberty_desire_levels.txt:38]
- [ ] 大国以上なら、勢力ブロックパネルで「勢力ブロックを形成」を押し、名前・アイデンティティの柱・主要原則を選んで形成する（Sphere of Influence が必要） {#mid-bloc}
  - なぜ: 影響力が足りず関係を維持できない国とも関係を保て、他のブロックから遠ざけられる（公式の説明）。形成できるのは非承認大国以上で、法律「孤立主義」では形成できない。原則はこの DLC の機能がないと選べない [src: tutorial_l_japanese.yml, lesson_form_power_bloc_how_2_desc] [src: tutorial_l_japanese.yml, lesson_form_power_bloc_why_4_desc] [src: interfaces_l_japanese.yml, FORM_POWER_BLOC] [src: 00_scripted_triggers.txt:56] [src: 00_scripted_triggers.txt:57] [src: 00_power_bloc_principles.txt:10]

## 4. 終盤（1887〜）

### 列強の地位の維持

到達目標: ランクを失う前に威信の不足を埋め、外交協定と勢力ブロックの更新を取りこぼしていない状態にする。

- [ ] 警告「戦力ランクを失っています」が出たら、外交パネルで威信とランクの維持に必要な威信を比べ、国内総生産・陸海軍の戦力投射・商品の生産のどれかを伸ばす {#late-rank}
  - なぜ: 威信が足りないまま回復しないと、警告に表示された日数でランクが下がる（公式の説明）。降格までの基本の日数は365。ランクが下がると貸付歩合の優遇（列強 −50%、大国 −25%）などを失う [src: alerts_l_japanese.yml, alert_is_losing_rank_alert_desc] [src: alerts_l_japanese.yml, alert_is_losing_rank_alert_hint] [src: concepts_l_japanese.yml, concept_prestige_desc] [src: 00_alert_types.txt:196] [src: 00_defines.txt:1295] [src: 00_country_ranks.txt:44] [src: 00_country_ranks.txt:82]
- [ ] 怒りの重要アクションで外交協定や条約の条項が破棄の危機にあると出たら、外交パネルで破棄される条件を読み、重要な協定なら関係を改善するか、危うくしている行動をやめる {#late-treaty}
  - なぜ: 警告に出た条件が真でなくなると、その協定や条項は破棄される（公式の説明） [src: alerts_l_japanese.yml, alert_diplomatic_pact_in_danger_desc] [src: alerts_l_japanese.yml, alert_diplomatic_pact_in_danger_hint] [src: alerts_l_japanese.yml, alert_treaty_article_in_danger_hint] [src: 00_alert_types.txt:694] [src: 00_alert_types.txt:708]
- [ ] 勢力ブロックリーダーなら、重要アクション「権限が利用可能」が出たら、勢力ブロックパネルで原則を変更・更新・追加する（Sphere of Influence が必要） {#late-bloc-mandate}
  - なぜ: 権限は原則の変更・更新・新規追加に使う。強いメンバーがいる、結束力が高いと早く貯まる（公式の説明） [src: alerts_l_japanese.yml, alert_power_bloc_mandates_available_hint] [src: concepts_l_japanese.yml, concept_power_bloc_mandate_desc] [src: 00_alert_types.txt:1042] [src: 00_power_bloc_principles.txt:10]

### 急進派・財政の崩れの予防

到達目標: 分離や革命に育つ前に運動を抑え、戦争の出費で収支が崩れていない状態にする。

- [ ] 警告「分離主義者運動」が出たら、「政策」パネルで該当の政治運動を選び、運動活動と支持を減らす {#late-secession}
  - なぜ: 運動活動は、支持者の急進派を減らし利益集団の支持を増やすと鈍る。育つと、支持者の多い州が分離して外交戦を起こす（公式の説明） [src: alerts_l_japanese.yml, alert_secession_growing_alert_hint] [src: concepts_l_japanese.yml, concept_secession_desc] [src: 00_alert_types.txt:492]
- [ ] 革命や分離の兆しがあるときは、「政策」パネルの「制度」タブで「治安維持」と「法執行機関」の投資レベルを上げる {#late-institution}
  - なぜ: 「治安維持」は革命と分離の進行を遅らせ、「法執行機関」は社会不安の悪影響を減らす。「治安維持」で革命を弱められると、用語説明にもある（公式の説明） [src: concepts_l_japanese.yml, concept_revolution_desc] [src: 00_institutions.txt:35] [src: 00_institutions.txt:48] [src: 00_institutions.txt:49]
- [ ] 戦争中や軍の拡張後は、「予算」パネルの「概要」タブで週間収支を確かめ、赤字なら2章「財政の安定」の手順で戻す {#late-budget-war}
  - なぜ: 軍隊の主な出費は軍隊の給金と軍需品で、戦争中の大隊の動員でさらに増える（公式の説明） [src: tutorial_l_japanese.yml, lesson_expand_military_why_3_desc]
- [ ] 怒りの重要アクション「低い訓練率」が出たら、「予算」パネルで軍隊の給金を上げる {#late-training}
  - なぜ: 戦争中に軍隊の給金を下げると、軍事施設の訓練率が下がる（公式の説明） [src: alerts_l_japanese.yml, alert_training_rate_low_desc] [src: alerts_l_japanese.yml, alert_training_rate_low_hint] [src: 00_alert_types.txt:753]

### 戦争の崩れの予防

到達目標: 戦争支持率の低下・戦争目標の失効・無防備な戦線・悪名の積み上がりを、戦争中に放置していない状態にする。

- [ ] 警告「Low War Support」が出たら、戦争パネルで戦争支持率を確かめ、戦闘に勝って戦争目標を掌握するか、和平協定を進める {#late-war-support}
  - なぜ: 戦争支持率が25以下だと、戦闘への不利な補正と急進化が始まる。戦闘に勝ち、戦争目標を掌握すると回復する（公式の説明）。この警告には日本語訳がなく、英語で表示される [src: 00_defines.txt:1203] [src: alerts_l_english.yml, alert_low_war_support_effects_alert_hint] [src: concepts_l_japanese.yml, concept_war_support_desc] [src: 00_alert_types.txt:48]
- [ ] 警告「戦争目標 expiring」が出たら、戦争パネルで該当の戦争目標にカーソルを合わせ、掌握に必要な条件を満たす {#late-goal-risk}
  - なぜ: 長く掌握されていない戦争目標は、表示された日数後に取り下げられる。この警告にも日本語訳がなく、英語で表示される（公式の説明） [src: alerts_l_english.yml, alert_war_goal_at_risk_of_being_dropped_alert_desc] [src: alerts_l_english.yml, alert_war_goal_at_risk_of_being_dropped_alert_hint] [src: 00_alert_types.txt:61]
- [ ] 警告「無防備な戦線」が出たら、前線パネルを開き、将軍か大隊を配属する {#late-front}
  - なぜ: 将軍も大隊も配属されていない戦線に、敵の将軍が少なくとも1人割り当てられている状態。将軍は軍事パネルで雇用できる（公式の説明） [src: alerts_l_japanese.yml, alert_vulnerable_front_desc] [src: alerts_l_japanese.yml, alert_vulnerable_front_hint] [src: 00_alert_types.txt:226]
- [ ] 和平協定で戦争目標を主張する前に、外交パネルで自国の悪名を確かめる {#late-infamy}
  - なぜ: 悪名は外交事件や、和平協定での戦争目標の主張で増え、他国の態度と外交協定の影響力コストに響く（公式の説明）。25超で「不信」、50超で「悪名」、100超で「疎外」。年5ずつ薄れる [src: concepts_l_japanese.yml, concept_infamy_desc] [src: 00_defines.txt:1003] [src: 00_defines.txt:1004] [src: 00_defines.txt:1005] [src: 00_defines.txt:1006] [src: diplomatic_overview.gui:1815]

## 5. 定期ルーチン {.routine}

## 6. 困ったとき

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|
| 時代の区切り | 1836〜1861／1862〜1886／1887〜1911／1911〜1936 | [src: 00_eras.txt, era_2 〜 era_5] |
| 正当性の段階 | 0〜24 非正規政府（法律の制定に政治運動の支持が要る）／25〜49 不安定な政府（制定速度 −25%）／50〜74 対立する政府／75〜89 合法政府／90以上 正当なる政府（制定速度 +25%） | [src: 00_legitimacy_levels.txt:2] [src: 00_legitimacy_levels.txt:7] [src: 00_legitimacy_levels.txt:25] [src: 00_legitimacy_levels.txt:30] [src: 00_legitimacy_levels.txt:48] [src: 00_legitimacy_levels.txt:56] [src: 00_legitimacy_levels.txt:77] [src: 00_legitimacy_levels.txt:81] |
| 正当性の警告 | 25未満で警告「非正規政府」／25以上50未満で重要アクション「不安定な政府」 | [src: 00_alert_types.txt:419] [src: 00_alert_types.txt:741] |
| 行政力の不足／余剰 | 使用量が生産量の2倍で、徴収される税が100%減る（税の浪費 +1）。生産量が使用量の2倍で、州の建設速度 +10%。どちらも定義のコメントによる最大時の値 | [src: 00_code_static_modifiers.txt:573] [src: 00_code_static_modifiers.txt:579] |
| 権力の不足／余剰 | 使用量が生産量の2倍で、対立側の利益集団の支持 −10・政治運動由来の急進派 +20%。生産量が使用量の2倍で、法律の制定速度 +25% | [src: 00_code_static_modifiers.txt:586] [src: 00_code_static_modifiers.txt:592] [src: 00_code_static_modifiers.txt:593] |
| 影響力の不足 | 使用量が生産量の2倍で、威信 −50%（定義のコメントによる最大時の値） | [src: 00_code_static_modifiers.txt:613] |
| 金準備の上限 | 基本は年間GDPの0.2倍（最低1000）。超えると警告が出る | [src: 00_defines.txt:541] [src: 00_defines.txt:542] |
| 商品の不足 | 供給が需要の50%を下回ると、使う施設に産出ペナルティ | [src: 00_defines.txt:419] |
| 市場アクセス | 100%未満で重要アクションが出る | [src: 00_alert_types.txt:927] |
| 生活水準の警告 | 州のPOPの25%以上が期待値（最小）を下回ると出る | [src: 00_alert_types.txt:989] |
| 法律の制定 | 失敗後は730日、再試行できない。成功までに通るフェーズは3つ | [src: 00_defines.txt:171] [src: 00_defines.txt:181] |
| 政治運動の強化 | 基本の権力コストは200（チュートリアルも、強化の前提に権力200以上を求める） | [src: 00_defines.txt:283] [src: 00_tutorial_lessons_promote_ig.txt:131] |
| 布告「道路整備」 | 権力100（国のランクで増減）。技術「中央集権化」で解禁 | [src: 00_decree.txt:18] [src: 00_decree.txt:20] |
| 布告「緊急救援」 | 州の徴税 −50%。技術「中央集権化」で解禁 | [src: 00_decree.txt:147] [src: 00_decree.txt:150] |
| 企業の繁栄度 | 100 でボーナスが有効、75 以下で止まる。警告は繁栄度が100以上で伸びがマイナスのときに出る | [src: 00_defines.txt:664] [src: 00_defines.txt:665] [src: 00_alert_types.txt:771] [src: 00_alert_types.txt:772] |
| 布告「隣の芝は青い運動」 | 移住求心力 +20 と +25%、権力100（国のランクで増減）。技術「ロマン主義」で解禁 | [src: 00_decree.txt:897] [src: 00_decree.txt:898] [src: 00_decree.txt:901] [src: 00_decree.txt:903] |
| 制度の投資レベル | 1〜5 | [src: 00_defines.txt:293] [src: 00_defines.txt:294] |
| 運動活動 | 25%以上で運動が法律の制定に影響する／50%以上で毎月支持者が急進化し、反乱に変わりやすい | [src: 00_defines.txt:105] [src: 00_defines.txt:98] [src: 00_defines.txt:312] |
| 関心ランク | 「観察」は関与100以上／「積極的」は関与1000以上（外交戦の開始・参加が可能） | [src: interest_tier_types.txt:25] [src: interest_tier_types.txt:40] [src: interest_tier_types.txt:47] |
| 従属国の自由への願望 | 25未満が低、25〜74が中、75以上が高（高いと従属国の政治運動由来の急進派 +25%） | [src: 00_liberty_desire_levels.txt:2] [src: 00_liberty_desire_levels.txt:17] [src: 00_liberty_desire_levels.txt:27] [src: 00_liberty_desire_levels.txt:38] |
| 勢力ブロックの形成 | ランクが非承認大国以上。法律「孤立主義」では不可 | [src: 00_scripted_triggers.txt:56] [src: 00_scripted_triggers.txt:57] |
| 戦争支持率 | 25以下で戦闘への不利な補正と急進化が始まる | [src: 00_defines.txt:1203] |
| 悪名 | 25超で「不信」、50超で「悪名」、100超で「疎外」。毎年5ずつ薄れる | [src: 00_defines.txt:1003] [src: 00_defines.txt:1004] [src: 00_defines.txt:1005] [src: 00_defines.txt:1006] |
| ランクの降格と優遇 | 降格までの基本の日数は365。貸付歩合は列強 −50%、大国 −25% | [src: 00_defines.txt:1295] [src: 00_country_ranks.txt:44] [src: 00_country_ranks.txt:82] |

## 8. 用語

完全版は [用語対照表](viewer.html?file=vic3/localization-reference.md)。

- 警告（Alert）／重要アクション（Important Action）／怒りの重要アクション（Angry Important Action）／現在の状況（Current Situation）
- 行政力（Bureaucracy）／権力（Authority）／影響力（Influence）／キャパシティ（Capacity）
- 金準備（Gold Reserves）／債務（Loans）／信用枠（Credit）／元金（Principal）／債務不履行（Default）／破産（Bankruptcy）
- 課税レベル（Taxation Level）／消費税（Consumption Tax）／国家公務員の給金（Government Wages）／政府施設（Government Building）
- 建設局（Construction Sector）／資材（Construction）／建設キュー（Construction Queue）／投資プール（Investment Pool）／政府の建設（Government Construction）／民間の建設（Private Construction）
- 生産性（Productivity）／生産方式（Production Method）／市場価格（Market Price）／不足（Shortage）／取引所（Trade Center）
- 市場アクセス（Market Access）／インフラ（Infrastructure）／孤立した州地域（Isolated State Region）／港（Port）／鉄道（Railway）
- 飢饉（Famine）／食料保障（Food Security）／生活水準（Standard of Living）／生活水準の期待値（最小）（Minimum Expected Standard of Living）
- 布告（Decree）／道路整備（Road Maintenance）／緊急救援（Emergency Relief）
- 正当性（Legitimacy）／利益集団（Interest Group）／政府内（In Government）／対立側（In Opposition）／政治運動（Political Movement）／強化（Bolster）／抑圧（Suppress）
- 法律の制定（Enactment of Laws）／制定成功（Enactment Success）／政府改革（Government Reform）／制度（Institution）／法律（Law）
- 非正規政府（Illegitimate Government）／不安定な政府（Unstable Government）／対立する政府（Contested Government）／合法政府（Legitimate Government）／正当なる政府（Righteous Government）
- 技術（Technology）／革新（Innovation）／技術拡散（Technology Spread）／都市化（Urbanization）／官僚制（Bureaucracy）／中央集権化（Centralization）
- 企業チャーター（Corporate Charters）／株式会社（Joint-Stock Companies）／ロマン主義（Romanticism）
- 企業（Company）／繁栄度（Prosperity）／生産量（Throughput）／労働者（Workforce）／州（State）／市場（Market）／商品（Good）
- 移住（Migration）／移住求心力（Migration Attraction）／失業者（Unemployed）／隣の芝は青い運動（Greener Grass Campaign）
- 貿易キャパシティ（Trade Capacity）／世界市場（World Market）／関税（Tariffs）
- 投資レベル（Investment Level）／治安維持（Home Affairs）／法執行機関（Law Enforcement）／社会不安（Turmoil）
- 運動活動（Movement Activism）／急進派（Radical）／革命（Revolution）／分離（Secession）／分離主義者（Secessionist）／支持（Approval）
- 政治的圧力団体（Political Lobby）／宥和（Appeasement）
- 戦略的重要地域（Strategic Region）／関与（Involvement）／関心（Interest）／関心ランク（Interest Tier）／外交レンズ（Diplomatic Lens）／政治レンズ（Political Lens）／請求権（Claim）
- 外交戦（Diplomatic Play）／初動（Opening Moves）／外交工作（Diplomatic Maneuvers）／戦争へのカウントダウン（Countdown to War）／戦争目標（War Goal）／戦争目標を掌握（Controlled War Goal）／戦争賠償金（War Reparations）
- 戦争（War）／戦争支持率（War Support）／和平協定（Peace Deal）／戦線（Front）／将軍（General）／大隊（Battalion）／大隊の動員（Mobilize Battalion）／訓練率（Training Rate）
- 軍事施設（Military Building）／兵舎（Barracks）／編隊（Formation）／戦力投射（Power Projection）／威信（Prestige）／軍隊の給金（Military Wage）／軍需品（Military Good）
- 未編入州（Unincorporated State）／編入（Incorporate）
- 従属国（Subject）／自由への願望（Liberty Desire）／自治権（Autonomy）
- 勢力ブロック（Power Bloc）／アイデンティティの柱（Central Identity Pillar）／原則（Principle）／権限（Mandate）／勢力ブロックリーダー（Power Bloc Leader）
- ランク（Rank）／列強（Great Power）／大国（Major Power）／非承認大国（Unrecognized Major Power）／悪名（Infamy）／国内総生産（Gross Domestic Product）／貸付歩合（Loan interest rate）
- 条約（Treaty）／条項（Article）／外交協定（Diplomatic Pact）／外交アクション（Diplomatic Action）／孤立主義（Isolationism）

## 9. 出典

### 一次情報

- `common/technology/eras/00_eras.txt`
- `common/alert_types/00_alert_types.txt`（警告・重要アクションの発生条件）
- `common/tutorial_lessons/00_tutorial_lessons_promote_ig.txt`（政治運動の強化の前提）
- `common/legitimacy_levels/00_legitimacy_levels.txt`（正当性の段階と効果）
- `common/static_modifiers/00_code_static_modifiers.txt`（キャパシティの不足・余剰の効果）
- `common/defines/00_defines.txt`（金準備の上限・商品の不足・法律の制定・強化のコスト）
- `common/decrees/00_decree.txt`（布告）
- `common/buildings/13_construction.txt`、`common/buildings/07_government.txt`（建設局・行政府の解禁技術）
- `gui/construction_queue.gui`（建設パネルの建設キュー表示）
- `common/technology/technologies/30_society.txt`（企業の設立枠）
- `common/institutions/00_institutions.txt`、`common/interest_tier_types/interest_tier_types.txt`、`common/liberty_desire_levels/00_liberty_desire_levels.txt`、`common/country_ranks/00_country_ranks.txt`
- `common/scripted_triggers/00_scripted_triggers.txt`（勢力ブロックを形成できる条件）、`common/power_bloc_principles/00_power_bloc_principles.txt`（原則の表示条件に DLC の機能が要る）
- `common/tutorial_lessons/00_tutorial_lessons_incorporate_state.txt`（州の編入を行う画面）
- `gui/market_panel.gui`、`gui/politics_panel_institutions.gui`、`gui/politics_panel_overview.gui`、`gui/diplomatic_overview.gui`（画面の構成）
- `localization/english/alerts_l_english.yml`（日本語訳がない警告の文言）
- `localization/japanese/alerts_l_japanese.yml`、`tutorial_l_japanese.yml`、`concepts_l_japanese.yml`、`interfaces_l_japanese.yml`（警告・チュートリアル・用語説明の文言）

### コミュニティ情報
