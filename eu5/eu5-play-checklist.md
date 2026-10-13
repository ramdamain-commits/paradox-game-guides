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

## 4. 終盤：絶対主義〜革命（1637〜）

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
- `main_menu/localization/japanese/tutorial_l_japanese.yml`、`hints_l_japanese.yml`、`game_concepts_l_japanese.yml`（公式の説明文）

### コミュニティ情報
