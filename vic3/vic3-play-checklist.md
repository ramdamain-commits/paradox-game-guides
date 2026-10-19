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
  - なぜ: 正当性は、政府内の利益集団と法律の組み合わせがどれだけ合っているかを示す。低いほど法律の制定に時間がかかる。段階ごとの効果は7章 [src: concepts_l_japanese.yml, concept_legitimacy_desc] [src: 00_legitimacy_levels.txt:7] [src: 00_legitimacy_levels.txt:30]
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
  - なぜ: 施設や輸入が効くまでには時間がかかる。布告「緊急救援」のほうが早く効くことがあるが、その州の徴税が半減する（技術「中央集権化」で解禁）。数値は7章 [src: alerts_l_japanese.yml, alert_famine_alert_hint] [src: 00_alert_types.txt:459] [src: 00_decree.txt:150]
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
- [ ] 警告「フリー政府改革」が出ている間に、「政策」パネルの「政府改革」タブで政府内の利益集団の構成を見直す {#early-reform-free}
  - なぜ: 最近の選挙により、表示された期限内に行う次の政府改革は急進派を生まない。ふつうは、権力を持っていた集団を政府から外すと急進派が出て、改革を頻繁に行うと政情が大きく不安定になる（公式の説明） [src: alerts_l_japanese.yml, alert_free_government_reform_desc] [src: tutorial_l_japanese.yml, lesson_reform_government_how_5_desc] [src: 00_alert_types.txt:141]
- [ ] 警告「非正規政府」や重要アクション「不安定な政府」が出たら、「政策」パネルの「政府改革」タブで、正当性が上がる利益集団の組み合わせを試す {#early-reform-legit}
  - なぜ: 構成は確定するまで適用されないので、試し直せる。正当性が低いと法律の制定が遅くなり、25未満では制定に政治運動の支持が要る。段階ごとの効果は7章 [src: tutorial_l_japanese.yml, lesson_reform_government_how_3_desc] [src: alerts_l_japanese.yml, alert_low_legitimacy_alert_hint] [src: 00_alert_types.txt:419] [src: 00_alert_types.txt:741] [src: 00_legitimacy_levels.txt:7] [src: 00_legitimacy_levels.txt:30]
- [ ] 行政力と収支に余裕があるときに、「学校なし」「警察なし」など「〜なし」の法律が有効な法律グループがあれば、「法律」タブで同じグループの別の法律の制定を始める {#early-institution}
  - なぜ: 「〜なし」の法律はその制度を無効にする。制度は恩恵と権限をもたらすが、行政力を使い、編入州の人口に応じた支出が国庫にかかる（公式の説明） [src: tutorial_l_japanese.yml, lesson_enact_institution_law_how_2_desc] [src: tutorial_l_japanese.yml, lesson_enact_institution_law_why_4_desc] [src: 00_subgoals_tutorial.txt:1067]

## 3. 中盤（1862〜1886）

## 4. 終盤（1887〜）

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

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

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

## 9. 出典

### 一次情報

- `common/technology/eras/00_eras.txt`
- `common/alert_types/00_alert_types.txt`（警告・重要アクションの発生条件）
- `common/tutorial_lessons/00_tutorial_lessons_promote_ig.txt`（政治運動の強化の前提）
- `common/objective_subgoals/00_subgoals_tutorial.txt`（制度を有効にする法律）
- `common/legitimacy_levels/00_legitimacy_levels.txt`（正当性の段階と効果）
- `common/static_modifiers/00_code_static_modifiers.txt`（キャパシティの不足・余剰の効果）
- `common/defines/00_defines.txt`（金準備の上限・商品の不足・法律の制定・強化のコスト）
- `common/decrees/00_decree.txt`（道路整備・緊急救援）
- `common/buildings/13_construction.txt`、`common/buildings/07_government.txt`（建設局・行政府の解禁技術）
- `gui/construction_queue.gui`（建設パネルの建設キュー表示）
- `localization/japanese/alerts_l_japanese.yml`、`tutorial_l_japanese.yml`、`concepts_l_japanese.yml`、`interfaces_l_japanese.yml`（警告・チュートリアル・用語説明の文言）

### コミュニティ情報
