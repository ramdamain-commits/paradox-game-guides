# CK3 プレイ中チェックリスト：聖職者（聖界・神権制）
> 対象パッチ: 1.20.1（ビルド 26046173） ／ 最終確認日: 2026-10-24

聖職者として遊ぶときの「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。By God Alone が必要（無いと聖界・神権制は操作できない）。ほかの DLC はすべてある前提で書き、要る項目には「（DLC名 が必要）」と付ける。片方の政体だけの項目には「（聖界のみ）」「（神権制のみ）」と付ける。「（公式の説明）」は、ゲーム内の助言・チュートリアル・用語説明が根拠で、効果をスクリプトでは確かめていない記述。

## 1. 開始直後（ポーズ中にやること）

- [ ] 自分のキャラクター画面で、政体名が「聖界」か「神権制」かを確かめる {#start-gov}
  - なぜ: 政体は宗教で決まり、キリスト教は聖界、ほかの宗教は神権制になる。開始ブックマークの聖職者は聖界だけで、神権制は地図から領主を選んで始めるか、途中でなる。途中でなるには、神権制になる前の封建制などの伯爵か公爵が、献身レベル「信心深い」以上で敬虔点500と威信点750を払い、決断「神権制統治を採用する」を実行する（組織化された宗派が条件。宗教指導者が聖界の宗派では出ない） [src: common/religion/religion_types/00_christianity.txt:5] [src: _religion_types.info:11] [src: 00_bookmarks.txt:1196] [src: pam_decisions.txt:438] [src: pam_decisions.txt:451] [src: pam_decisions.txt:465] [src: pam_decisions.txt:555] [src: pam_decisions.txt:556] [src: pam_decisions.txt:570]
- [ ] 宗派の画面で、教義「聖職者の伝統」が「神権制」か「世俗の聖職者」かを確かめる {#start-doctrine}
  - なぜ: 「世俗の聖職者」の宗派には教会領がなく、神権制や聖界になれるのは枢機卿、聖職管区（大司教区）の保持者、所領のない聖職者だけ。そうなら教会領の項目は飛ばす（公式の説明） [src: game_concepts_l_japanese.yml, game_concept_church_property_desc] [src: pam_scripted_triggers.txt:6765] [src: 00_theocracy_lease.txt:6]
- [ ] 自分のキャラクター画面で、「上位者」と「主君」の肖像を確かめる {#start-superior}
  - なぜ: 上位者は宗教上の管轄を持つ聖職者、主君は世俗の領主で、別の人物にもなる。上位者が誰かは貸与契約が決める（公式の説明） [src: window_character.gui:549] [src: pam_game_concepts_l_japanese.yml, game_concept_lease_contract_desc]
- [ ] 自分のキャラクター画面の教会領のアイコンにカーソルを合わせ、貸与の収入、「教会の義務」の支払い、徴募兵を確かめる {#start-lease}
  - なぜ: 貸与された寺院領の税と徴募兵は、上位者と世俗の主君にも分かれて渡る。上位者には徴募兵の15%、神権制の貸与なら税の25%も出る（聖界の税は下の項目）。主君の取り分の上限は税25%・徴募兵50%で、強いフックを持たれるとそこまで上がりうる。借手でなければアイコンは出ない [src: window_character.gui:1709] [src: 00_theocracy_lease.txt:26] [src: 00_theocracy_lease.txt:28] [src: 00_theocracy_lease.txt:68] [src: 00_theocracy_lease.txt:70] [src: 00_theocracy_lease.txt:212] [src: 00_theocracy_lease.txt:313] [src: 00_theocracy_lease.txt:315] [src: 00_councillor_triggers.txt:198]
- [ ] 状況「キリスト教会」を開き、現在の局面の「教会の中央集権化」と「世俗の義務」の種類を確かめる（聖界のみ） {#start-church}
  - なぜ: 借手が上位者に納める割合は、最低限5%・中程度10%・高度20%（高度は宗教指導者にも1%）。主君の取り分は、個人の義務なら好感度やフックで最大25%、固定義務なら15%（公式の説明） [src: pam_christian_situation_l_japanese.yml, situation_parameter_the_christian_church_strong_centralization] [src: 00_theocracy_lease.txt:142] [src: 00_theocracy_lease.txt:166] [src: 00_theocracy_lease.txt:179] [src: 00_theocracy_lease.txt:207] [src: 00_theocracy_lease.txt:283]
- [ ] 画面上部の国庫にカーソルを合わせ、月の収入と支出の内訳を確かめる（聖界のみ） {#start-treasury}
  - なぜ: 国庫は統治にしか使えない資産で、聖界では金の費用が国庫払いに置き換わる（公式の説明） [src: dlc_tgp_china_game_concepts_l_japanese.yml, game_concept_treasury_desc] [src: 02_theocratic_government_types.txt:83] [src: hud.gui:6512]
- [ ] 宗派のアイコンにカーソルを合わせて霊的充足度のレベルを確かめ、個人的信条の空き枠があれば2章で埋める {#start-sf}
  - なぜ: 霊的充足度は−100〜100で、低いとストレスが増え、高いと選べる行動が増える（公式の説明） [src: 00_defines.txt:890] [src: tutorial_reactive_l_japanese.yml, reactive_advice_personal_beliefs_desc] [src: hud.gui:3814]

## 2. 聖職者の基盤づくり

### 敬虔点と霊的充足度

到達目標: 霊的充足度が0以上で、個人的信条の枠を使い切り、献身レベルを伸ばしている状態にする。

- [ ] 通知「新たな個人的信条を選択できる」が出たら、「個人的信念」ウィンドウの空き枠の「個人的信条を採用」から選ぶ {#base-tenet}
  - なぜ: 枠は基本1つで、献身レベル4「美徳の模範者」と5「宗派の象徴」で1つずつ増える。中核か容認の信条なら霊的充足度が上がり、禁止の信条は秘密になる（公式の説明）。外す・入れ替えると3年は変えられない [src: 00_defines.txt:904] [src: 00_defines.txt:906] [src: 00_basic_modifiers.txt:159] [src: 00_basic_modifiers.txt:163] [src: pam_game_concepts_l_japanese.yml, game_concept_personal_tenet_desc]
- [ ] 通知「決断が利用可能：告解を受ける」が出たら、決断「己の罪を告白する」を実行する（聖界のみ） {#base-confession}
  - なぜ: 霊的充足度が0未満のときに出て、霊的充足度+5とストレスの軽減が得られる。宮廷聖職者が要り、5年に1回。信条「告解の秘跡」が容認以上の流派だけに出る。−30以下でストレス獲得+10%、−65以下で+25% [src: pam_actions.txt:694] [src: pam_decisions.txt:61] [src: pam_decisions.txt:72] [src: pam_decisions.txt:85] [src: pam_decision_events.txt:333] [src: pam_values.txt:2177] [src: 00_spiritual_fulfillment_types.txt:46] [src: 00_spiritual_fulfillment_types.txt:29]
- [ ] 霊的充足度が65以上のレベル「安寧」になったら、決断「信仰心を誇示する」を実行する（聖界のみ） {#base-devotion}
  - なぜ: 敬虔点250を払い、威信点を得るか、名声レベルが「輝かしい名声」より低ければ献身レベル1段と引き換えに威信点と名声レベル1段を得る。10年に1回 [src: pam_decisions.txt:157] [src: pam_decisions.txt:171] [src: pam_decisions.txt:174] [src: pam_decision_events.txt:682] [src: pam_decision_events.txt:685] [src: pam_values.txt:2143]
- [ ] 通知「（聖典名）を学ぶことができる」が出たら、決断「（聖典名）を学ぶ」を実行する {#base-study}
  - なぜ: 通知はストレスがない間だけ出る。敬虔点、特性「宗教学者」とその経験、学識・管理・外交の技能（最大8）が得られ、ストレスが増えることもある。5年に1回（公式の説明） [src: pam_actions.txt:1170] [src: pam_decisions.txt:6116] [src: pam_study_scripture_l_japanese.yml, pam_study_scripture_decision_tt]

### 宗教指導者と世俗の統治者

到達目標: 宗教指導者に破門されず、世俗の統治者に使えるフックを持つ。

- [ ] 「破門のリスク」が出たら、宗教指導者への好感度を上げ、罪悪の特性を減らす {#base-excomm}
  - なぜ: 教義「秘跡」が「中心的」の宗派（キリスト教など）で出る。宗教指導者のライバルや宿敵、交戦相手だと直接破門されうる。好感度が負なら、敬虔点を持つ敵対的な隣国の同宗派の統治者に破門を要請されうる（公式の説明） [src: pam_actions.txt:104] [src: pam_scripted_triggers.txt:1143] [src: important_actions_l_japanese.yml, action_excommunication_at_risk_desc]
- [ ] 霊的充足度が65以上のレベル「安寧」になったら、流派指導者に工作「親睦工作」を使う（聖界のみ） {#base-befriend}
  - なぜ: 宮廷聖職者には30以上、宗教指導者には95以上のレベル「恩寵」が要る。宗教指導者の好感度は破門の判断に効く（公式の説明） [src: 00_spiritual_fulfillment_types.txt:62] [src: 00_spiritual_fulfillment_types.txt:75] [src: 00_spiritual_fulfillment_types.txt:93] [src: 00_scheme_triggers.txt:433] [src: 00_scheme_triggers.txt:439] [src: 00_scheme_triggers.txt:445] [src: pam_actions.txt:104]
- [ ] 同じ宗派で神権制でない相手に、「霊的な助言を授ける」を使う {#base-counsel}
  - なぜ: 献身レベル1以上で使え、敬虔点100と金（聖界は国庫）を払って弱いフックを10年得る。相手には敬虔点と好感度が入る。1年に1回、同じ相手には10年に1回 [src: spiritual_counsel_interaction.txt:45] [src: spiritual_counsel_interaction.txt:68] [src: spiritual_counsel_interaction.txt:17] [src: spiritual_counsel_interaction.txt:28] [src: spiritual_counsel_interaction.txt:40] [src: 00_hook_types.txt:252] [src: 00_hook_types.txt:255]

### 収入

到達目標: 頼める先と、毎月増やせる先の両方を持つ。

- [ ] 宗教上の上位者か下位者の国庫に余裕があれば、「教会の国庫から金を求める」を使う（聖界のみ） {#base-treasury}
  - なぜ: 敬虔点100を払い、相手の国庫から収入に連動する額を得る。フックを使えば断られない。同じ相手には5年に1回。上位者とその上位者、下位者とその下位者まで届く [src: pam_interactions.txt:21651] [src: pam_interactions.txt:21720] [src: pam_interactions.txt:21637] [src: pam_interactions.txt:21760] [src: pam_scripted_triggers.txt:1484]
- [ ] 下位者に余裕があれば、「下位者に金を求める」を使う {#base-subs}
  - なぜ: 聖界、枢機卿、聖職管区の保持者、所領のない聖職者が使える。所領を持つ神権制の領主は、枢機卿か聖職管区の保持者でなければ使えない。敬虔点100〜250を払って金を得る。1年に1回、同じ相手には5年に1回 [src: pam_interactions.txt:22025] [src: pam_scripted_triggers.txt:6784] [src: pam_values.txt:9759] [src: pam_interactions.txt:22015] [src: pam_interactions.txt:22016]
- [ ] 聖職管区の称号を持つなら聖界所領を開き、空きの枠に建造物を建てる（聖界のみ） {#base-estate}
  - なぜ: 建造物は私的な収入、敬虔点、霊的充足度を増やす（公式の説明）。主建造物の聖堂は月に金2と敬虔点0.3 [src: pam_game_concepts_l_japanese.yml, game_concept_ecclesiastical_estate_building_desc] [src: 11_ecclesiastical_domicile_buildings.txt:25] [src: 11_ecclesiastical_domicile_buildings.txt:62] [src: 11_ecclesiastical_domicile_buildings.txt:107] [src: 11_ecclesiastical_domicile_buildings.txt:108] [src: 00_domicile_types.txt, ecclesiastical_domicile]
- [ ] 封臣がいるなら法律「教会の支配権」を確かめ、条件が揃ったら上げる {#base-authority}
  - なぜ: 段階2は封臣の税と徴募兵の納付+10%、段階3は+25%。段階1・2・3は献身レベル1・2・3以上と、民会・年代記の筆記・神権のイノベーションが要り、上げるたびに20年待つ [src: 00_realm_laws.txt:655] [src: 00_realm_laws.txt:739] [src: common/scripted_triggers/00_law_triggers.txt:629] [src: 00_realm_laws.txt:4]
- [ ] 神権制か聖界の封臣がいるなら、自分の献身レベルを確かめ、敬虔点を稼ぐ行動で上げる {#base-piety}
  - なぜ: 封臣が納める税は5%＋10%×主君の献身レベル、徴募兵は10%×レベル（宗派が違えばどちらも10%）。敬虔点を獲得するたびに次のレベルへ近づく（公式の説明） [src: theocratic.txt:11] [src: theocratic.txt:21] [src: theocratic.txt:24] [src: theocratic.txt:7] [src: game_concepts_l_japanese.yml, game_concept_piety_desc]

## 3. 位を上げる

### 聖職管区の称号を得る

到達目標: 聖職管区の称号を持ち、上位の称号の候補者に入っている状態にする。

- [ ] 通知「新たな聖職管区を要請できる」が出たら、「聖職称号の創設を要請する」を実行する（聖界のみ） {#rank-create}
  - なぜ: 宗教指導者（いなければ流派指導者）に頼む。主称号が公爵未満の所領持ちで、主君の主称号が王国、自分は管区を持たないときに使える。敬虔点は、選んだ称号の首都伯爵領が属する王国で、管区に入っていないキリスト教の伯爵領1つにつき50 [src: 01_puppet_interactions.txt:340] [src: 01_puppet_interactions.txt:461] [src: 01_puppet_interactions.txt:464] [src: 01_puppet_interactions.txt:473] [src: 01_puppet_interactions.txt:488] [src: pam_values.txt:8224] [src: pam_values.txt:8227] [src: 00_basic_values.txt:1132] [src: pam_actions.txt:303]
- [ ] 通知「大司教区の拡張を要請する」が出たら、「聖職称号の拡張を要請する」で隣の公爵領を足す（聖界のみ） {#rank-expand}
  - なぜ: 管区に隣り合い、管区に入っていない伯爵領を含む公爵領を選ぶ。敬虔点は公爵領内のキリスト教の伯爵領1つにつき50で、同じ要請は5年に1回 [src: pam_scripted_triggers.txt:3498] [src: pam_values.txt:8256] [src: pam_values.txt:8258] [src: 01_puppet_interactions.txt:948] [src: pam_actions.txt:393]
- [ ] 通知「大司教区の後継者」が出たら、その称号の候補者に「聖職称号の候補者に影響を与える」を使う（聖界のみ） {#rank-candidacy}
  - なぜ: 管区の称号は、保持者が死ぬと候補者スコアが最も高い者が継ぐ（公式の説明）。中程度の支援は敬虔点250でスコア+20、大規模は500で+50。「聖職叙任権闘争」の局面は敬虔点が半分。管区を持つ者が自分を推せるのは、宗教指導者の称号など限られた称号だけ [src: succession_laws_l_japanese.yml, clerical_appointment_law_effects] [src: pam_interactions.txt:1021] [src: pam_interactions.txt:1024] [src: pam_values.txt:2516] [src: pam_values.txt:2520] [src: pam_christian_situation_l_japanese.yml, situation_parameter_the_christian_church_cheaper_clerical_appointment] [src: pam_scripted_triggers.txt:545] [src: 00_important_actions_triggers.txt:20]
- [ ] 候補者の一覧を候補者スコア順に並べ、ツールチップの内訳で足りない項目を確かめる {#rank-score}
  - なぜ: 聖界でも神権制でも、任命制の称号は候補者スコアで決まる。学識の値がそのまま入り、所領を持つ統治者で+25、聖職者で+25、献身レベル2以上ならレベル×10、徳の特性1つにつき+10、罪の特性1つにつき−10。候補に入るのは保持者の評議員・宮廷役職・家臣と同じ管区の聖職者 [src: clerical_christian.txt:12] [src: clerical_christian.txt:18] [src: clerical_christian.txt:133] [src: clerical_christian.txt:143] [src: clerical_christian.txt:180] [src: clerical_christian.txt:202] [src: clerical_christian.txt:213] [src: clerical_christian.txt:233] [src: clerical_christian.txt:238] [src: interaction_templates.gui:3025]
- [ ] 枢機卿職を目指すなら、宗教指導者に「枢機卿職を要請する」を実行する（聖界のみ） {#rank-cardinal}
  - なぜ: 聖職者本人が頼む。敬虔点は基準が1000で、宗教指導者より献身レベルが高いと1段につき−100、低いと+250。強いフックを使えば自動で受け入れられる。枢機卿は全体で70人まで [src: 01_puppet_interactions.txt:2299] [src: 01_puppet_interactions.txt:2308] [src: 01_puppet_interactions.txt:2333] [src: 01_puppet_interactions.txt:2391] [src: pam_values.txt:8745] [src: pam_values.txt:8751] [src: pam_values.txt:8764] [src: pam_scripted_triggers.txt:3080] [src: pam_scripted_triggers.txt:3099]
- [ ] HUD の「枢機卿団」ボタンで画面を開き、「枢機卿団」タブで3つの席の評価、「継承」タブで次の教皇になる可能性を確かめる（聖界のみ） {#rank-college}
  - なぜ: 教皇が死ぬと、最も多くの支持者を持つ席（民衆派・敬虔派・有力者）で評価が最高の枢機卿が教皇になる。敬虔派は献身レベルと学識、民衆派は名声レベルと外交と枢機卿団内の友人、有力者は自分の流派の伯爵領数と聖地と栄光レベルで決まる（公式の説明） [src: hud.gui:448] [src: window_cardinals.gui:911] [src: cardinals_window_l_japanese.yml, CARDINALS_VIEW_COLLEGE_DESCRIPTION] [src: cardinals_window_l_japanese.yml, theocratic_elective_pious_desc] [src: cardinals_window_l_japanese.yml, theocratic_elective_populist_desc] [src: cardinals_window_l_japanese.yml, theocratic_elective_powerful_desc] [src: cardinals_window_l_japanese.yml, CARDINALS_VIEW_TAB_SUCCESSION]
- [ ] 評価を上げたい枢機卿に「教皇候補スコアを高める」を使う（聖界のみ） {#rank-papabile}
  - なぜ: 敬虔点250でスコア+10、金も払えば+20。同じ相手には3年に1回。有力者の席は、敬虔点（差1点につき5）を足して首位に立てる [src: pam_interactions.txt:15013] [src: pam_interactions.txt:15054] [src: pam_interactions.txt:15057] [src: pam_values.txt:1673] [src: pam_values.txt:1674] [src: pam_interactions.txt:14911] [src: pam_values.txt:1631]
- [ ] 枢機卿で聖界所領に尚書局があるなら、決断「敬虔な善行を広く知らしめる」で教皇職を選ぶ（聖界のみ） {#rank-pious}
  - なぜ: 敬虔点500で一度だけ使える。教皇職を選ぶと選出スコアが+30され、威信点も得る [src: pam_decisions.txt:3127] [src: pam_decisions.txt:3139] [src: pam_decisions.txt:3143] [src: pam_decisions.txt:3159] [src: pam_decision_events.txt:2142] [src: pam_decision_events.txt:2145] [src: 11_ecclesiastical_domicile_buildings.txt:2105]
- [ ] 教皇選挙が近いなら、枢機卿に「枢機卿団の投票に影響を与える」を使い、自分の推す者へ投票させる（聖界のみ） {#rank-vote}
  - なぜ: 献身レベル3以上と敬虔点250が要る。強いフックを使うと確実に通り、相手の票は20年間その候補に固定される。同じ相手には10年に1回 [src: pam_interactions.txt:14512] [src: pam_interactions.txt:14550] [src: pam_interactions.txt:14571] [src: pam_interactions.txt:14598] [src: pam_interactions.txt:14600] [src: pam_interactions.txt:14463]

### 信仰の長への道筋

到達目標: 信仰の長の称号を自分で創るか、任命で継げる位置に付く。

- [ ] 自分の信仰に宗教指導者がいなければ、決断「（宗教指導者）の称号を創設する」を実行する {#rank-hof-create}
  - なぜ: 聖職的な宗教指導者の信仰は、領国内の聖地1か所以上と献身レベル2（本流の流派以外は3）が要り、敬虔点200（本流以外は2倍）と金（聖界は国庫）を払う。世俗的な宗教指導者の信仰は献身レベル3と敬虔点250。キリスト教は大分裂のあとにだけ出る。宗教指導者は可能なら神権制になる [src: pam_decisions.txt:1160] [src: pam_decisions.txt:1167] [src: pam_decisions.txt:1171] [src: pam_decisions.txt:1172] [src: 00_religious_triggers.txt:1524] [src: 00_religious_triggers.txt:1532] [src: 00_religious_triggers.txt:1535] [src: 00_religious_triggers.txt:1519] [src: 00_religious_triggers.txt:1492] [src: 02_religion_values.txt:4095] [src: 02_religion_values.txt:4097] [src: 02_religion_values.txt:4124] [src: 02_religion_values.txt:4131] [src: 02_theocratic_government_types.txt:2]
- [ ] 宗教指導者の称号が任命制なら、「宗教指導者の候補者に影響を与える」で自分か頼れる者を押し上げる {#rank-hof-candidacy}
  - なぜ: 対象は同じ信仰の保持者がいる任命制の称号。敬虔点250でスコア+20、500で+50と、聖職称号の候補者への支援と同じ [src: pam_interactions.txt:1247] [src: pam_scripted_triggers.txt:446] [src: pam_scripted_triggers.txt:454] [src: pam_interactions.txt:1409] [src: pam_interactions.txt:1406] [src: pam_interactions.txt:1444] [src: pam_interactions.txt:1458]

## 4. 教会を動かす・後を託す

### 教会を動かす

到達目標: 局面を読み、勅書・公会議・聖戦で教会の方向を決める。

- [ ] 決断「キリスト教会を導く」を実行し、状況の局面を進めたい方向へ押す（聖界のみ） {#church-steer}
  - なぜ: 宗教指導者・流派指導者・枢機卿・管区の保持者などが実行でき、敬虔点250で10年に1回。「聖職叙任権闘争」の最中は出ない。局面ごとに効果が違い、「改宗」「十字軍」は聖戦の誘発が楽に、「聖職叙任権闘争」は候補者への支援が半額になる [src: pam_decisions.txt:1594] [src: pam_decisions.txt:1607] [src: pam_decisions.txt:1610] [src: pam_decisions.txt:1614] [src: pam_decisions.txt:1618] [src: pam_decisions.txt:1636] [src: pam_decisions.txt:1639] [src: pam_christian_situation.txt:920] [src: pam_christian_situation.txt:1331] [src: pam_christian_situation.txt:1538]
- [ ] 教皇なら、決断「教皇勅書を制定する」で十字軍の招集・異端の宣言・信条の容認か禁止を選ぶ（聖界のみ） {#church-bull}
  - なぜ: 教会の支配権が段階1以上で、敬虔点500。種類ごとに5年に1回 [src: bulls_decisions.txt:31] [src: bulls_decisions.txt:38] [src: bulls_decisions.txt:40] [src: pam_values.txt:10329] [src: bulls_decisions.txt:256] [src: bulls_decisions.txt:321] [src: bulls_decisions.txt:475] [src: bulls_decisions.txt:736] [src: pam_scripted_triggers.txt:4085]
- [ ] 同じ信仰の公爵を王にしたいなら、「王国を聖別する」を使う {#church-consecrate}
  - なぜ: 使えるのは宗教指導者で、宗教指導者がいない信仰では公爵以上の神権制の流派指導者。献身レベル3以上が要り、金（聖界は国庫）500、敬虔点750（相手の献身レベル1につき−50）を払う。相手が神権制なら威信点500も要る。相手は同じ信仰の所領持ちの公爵で、独立しているか主君が皇帝 [src: pam_interactions.txt:23338] [src: pam_interactions.txt:23352] [src: pam_interactions.txt:23407] [src: pam_interactions.txt:23448] [src: pam_values.txt:9976] [src: pam_values.txt:10069] [src: pam_values.txt:10072] [src: pam_values.txt:10118]
- [ ] 信条や教義を決めるなら、活動「公会議」を主催する（聖界のみ） {#church-council}
  - なぜ: 主催できるのは宗教指導者、「主勢力（聖職）」、聖界の統治者、領国祭司の傀儡を持つ者のいずれかで、25年に1回。聖職管区の保持者が5人以上出席しないと成立せず（主催者が保持者なら出席者4人以上）、開催地は聖地・大聖堂などの重要な宗教施設がある郡。費用は金（聖界は国庫）で基本500、時代とともに増える [src: ecumenical_council.txt:9] [src: ecumenical_council.txt:28] [src: ecumenical_council.txt:29] [src: ecumenical_council.txt:30] [src: ecumenical_council.txt:31] [src: ecumenical_council.txt:337] [src: pam_values.txt:1882] [src: pam_values.txt:1884] [src: pam_scripted_triggers.txt:179] [src: ecumenical_council.txt:134] [src: ecumenical_council.txt:139] [src: ecumenical_council.txt:143] [src: pam_values.txt:1911]
- [ ] 状況「キリスト教会」の大分裂の進行が13に達したら、宗教指導者か流派指導者で王国以上の者は「大分裂を防ぐ」か「大分裂を引き起こす」を実行する（聖界のみ） {#church-schism}
  - なぜ: 献身レベル4以上・聖地1か所以上・同2か所以上・事前の立場・聖職者の支持7以上の5条件のうち4つが要る [src: pam_values.txt:9400] [src: pam_decisions.txt:2569] [src: pam_decisions.txt:2581] [src: pam_decisions.txt:2604] [src: pam_decisions.txt:2606] [src: pam_decisions.txt:2607] [src: pam_decisions.txt:2633] [src: pam_decisions.txt:2760]
- [ ] 他の信仰の統治者を攻めさせたいなら、「聖戦の誘発」を使う {#church-holywar}
  - なぜ: 使えるのは聖界の統治者と宗教指導者。同じ信仰で神権制でない隣の統治者が攻め手になり、敬虔点は対象の称号が伯爵領100・公爵領200・王国300。必要な献身レベルは伯爵領2・公爵領3・王国4で、「主勢力（聖職）」は「改宗」「十字軍」の局面で1段下がる。同じ相手には5年に1回 [src: pam_scripted_triggers.txt:4588] [src: pam_scripted_triggers.txt:4087] [src: pam_values.txt:9811] [src: pam_values.txt:9819] [src: 00_title_tiers_values.txt:3] [src: pam_interactions.txt:12402] [src: pam_interactions.txt:12408] [src: pam_interactions.txt:12426] [src: pam_interactions.txt:12432] [src: pam_interactions.txt:12443] [src: pam_interactions.txt:12446] [src: pam_christian_situation.txt:920] [src: pam_interactions.txt:12309]
- [ ] 通知「教会継承を要請する」が出たら、「教会継承の要求」を使う {#church-demand}
  - なぜ: 神権制の領主（宗教指導者を除く）が、同じ信仰の封建制・氏族制・部族制などの統治者に使える。相手が正当な後継者なく死ぬと、領地が代替後継者として自分の主称号の保持者へ渡る。敬虔点500（相手の主称号が王国なら15倍、帝国なら30倍）と国庫の金が要り、献身レベル2以上。選挙制の相手には使えず、同じ相手には10年に1回 [src: 00_demand_church_succession_interactions.txt:15] [src: 00_demand_church_succession_interactions.txt:42] [src: 00_demand_church_succession_interactions.txt:47] [src: 00_demand_church_succession_interactions.txt:55] [src: 00_demand_church_succession_interactions.txt:60] [src: 00_demand_church_succession_interactions.txt:82] [src: pam_values.txt:8667] [src: pam_values.txt:8673] [src: pam_values.txt:8680] [src: 00_religious_triggers.txt:2838] [src: pam_actions.txt:602]
- [ ] 通知「世俗統治者を傀儡にできる」が出たら、「世俗統治者を傀儡にする」を実行し、「策略」ウィンドウの「傀儡」タブから行動を命じる {#church-puppet}
  - なぜ: 傀儡は種類ごとに1人。聖職者の主な条件は自分が相手の封臣であること（特性による別の条件もある）で、相手は聖職者でない所領持ちの統治者（AI）。献身レベル3以上かフックが要り（王国以上は4以上か強いフック）、威信点は相手の称号が伯爵領なら75・公爵領なら150・王国なら225。教会の支配権が高いほど傀儡にしやすい [src: 00_puppet_interactions.txt:708] [src: 00_puppet_interactions.txt:793] [src: pam_scripted_triggers.txt:7113] [src: pam_scripted_triggers.txt:7114] [src: pam_scripted_triggers.txt:7243] [src: pam_scripted_triggers.txt:7244] [src: pam_puppet_types.txt, external_ruler_puppet] [src: window_intrigue.gui:117] [src: laws_l_japanese.yml, church_authority_3_effects]

### 後を託す

到達目標: 自分が死んだあとに操作する人物を決め、継承順位の1位に置く。

- [ ] 領国の継承法が「聖職者の任命」「神権選挙制」「神権制」のどれかを確かめる {#church-law}
  - なぜ: ゲームは聖職者に後継者がいない警告を出さない。郡以上の聖職者は「聖職者の任命」（候補者スコア最高の者が継ぐ）、教皇は「神権選挙制」、男爵領だけの者や借手は「神権制」で、教義が後継者を決める [src: 00_inheritance_actions.txt:17] [src: 00_inheritance_actions.txt:63] [src: common/scripted_triggers/00_law_triggers.txt:514] [src: common/scripted_triggers/00_law_triggers.txt:521] [src: common/scripted_triggers/00_law_triggers.txt:534] [src: succession_laws_l_japanese.yml, bishop_theocratic_succession_law_effects]
- [ ] 王朝がなければ、決断「王朝を創設する」を実行する {#church-dynasty}
  - なぜ: 後継者の指名には自分の王朝が要る。教会の支配権が段階2で、名声レベル3以上、威信点750を払う [src: pam_decisions.txt:375] [src: pam_decisions.txt:380] [src: pam_decisions.txt:383] [src: pam_decisions.txt:398] [src: 00_realm_laws.txt:658] [src: pam_interactions.txt:67] [src: 00_basic_values.txt:1004]
- [ ] 「神権制の後継者を指名」で後継者を決め、称号の継承順位が1位になったか確かめる {#church-designate}
  - なぜ: 相手は自分より年下で所領のない同信仰の成人（評議員・廷臣・同じ家の者・近親・拡大家族）で、指名すると養子になる。敬虔点250と、王朝の当主は栄誉点、当主でなければ威信点150。「聖職者の任命」の領国だけで使える。指名と同時に、現在の1位の1.1倍に届くスコアが足される [src: pam_interactions.txt:47] [src: pam_interactions.txt:48] [src: pam_interactions.txt:75] [src: pam_interactions.txt:79] [src: pam_interactions.txt:183] [src: pam_interactions.txt:198] [src: pam_interactions.txt:235] [src: pam_values.txt:9945]
- [ ] 他の候補者に追い抜かれそうなら、「候補者を支援する」を重ねる {#church-support}
  - なぜ: 対象は指名後継者・廷臣・近親・拡大家族で、所領を持たない者。敬虔点250でスコア+20、500で+50。「聖職叙任権闘争」の局面は敬虔点が半分 [src: pam_interactions.txt:480] [src: pam_interactions.txt:485] [src: pam_interactions.txt:545] [src: pam_values.txt:9919] [src: pam_values.txt:9921] [src: pam_values.txt:9924] [src: pam_values.txt:2516] [src: pam_values.txt:2520] [src: pam_values.txt:189]
- [ ] 教皇なら、通知「枢機卿を任命可能」が出たら「枢機卿を任命」で頼れる者を枢機卿にする（聖界のみ） {#church-cardinal}
  - なぜ: 次の教皇は枢機卿の中から選ばれる。国庫の金を払い、敬虔点100を得る。同じ相手には10年に1回、枢機卿は70人まで。通知は枢機卿が15人未満の間に出る [src: pam_interactions.txt:4644] [src: pam_interactions.txt:4656] [src: pam_interactions.txt:4668] [src: pam_interactions.txt:4674] [src: pam_actions.txt:933] [src: succession_laws_l_japanese.yml, theocratic_elective_candidates]

## 5. 定期ルーチン {.routine}

### 毎年

- [ ] 画面上部の国庫にカーソルを合わせ、月の収支が赤字で残りが少なければ、横の「国庫に資金追加」で金を移す（聖界のみ） {#year-treasury}
  - なぜ: 国庫が0を下回ると債務になり、戦争を宣言できない（公式の説明）。影響は6章 [src: important_actions_l_japanese.yml, action_in_treasury_debt_desc] [src: 00_realm_actions.txt:447] [src: hud.gui:6511] [src: hud.gui:6605]
- [ ] 宗教指導者（自分以外）の画面を開き、自分が好敵手・宿敵・交戦相手になっていないか、好感度が負でないかを確かめる {#year-head}
  - なぜ: 好敵手・宿敵・交戦相手なら宗教指導者に直接破門されうる。好感度が負なら、敵対する隣国の要請でも破門されうる。好感度が50以上なら、前者でない限り警告「破門のリスク」は出ない [src: pam_actions.txt:128] [src: pam_actions.txt:134] [src: pam_actions.txt:154] [src: important_actions_l_japanese.yml, action_excommunication_at_risk_desc]
- [ ] 称号のウィンドウで継承順位を開き、1位が望む者のままか確かめ、入れ替わっていれば4章「後を託す」の支援を重ねる {#year-heir}
  - なぜ: 聖職者に後継者がいなくてもゲームは警告を出さず、「聖職者の任命」の順位は候補者スコアで決まる（公式の説明） [src: 00_inheritance_actions.txt:17] [src: succession_laws_l_japanese.yml, clerical_appointment_law_effects]

### 局面が変わったとき

- [ ] 状況「キリスト教会」を開き、新しい局面の名前と、自分の参加者グループ（主勢力・副勢力・異端の聖職）を確かめる（聖界のみ） {#phase-group}
  - なぜ: 局面ごとに宗教・臣下・外交・戦争の効果があり、グループで付く効果が違う。主勢力（聖職）は、最も郡の多いキリスト教の宗派の聖界か神権制の統治者（公式の説明） [src: pam_christian_situation_l_japanese.yml, the_christian_church_participant_group_christian_clerical_main_power_rulers_desc] [src: pam_christian_situation.txt:69]
- [ ] 状況の自分のグループのアイコンにカーソルを合わせ、「臣下」の中央集権化と義務の行が前の局面から変わっていれば、教会領のアイコンで貸与の取り分を見直す（聖界のみ） {#phase-lease}
  - なぜ: 局面で、上位者へ納める割合と、主君の取り分の決まり方（個人の義務か固定義務か）が替わる。数値は1章（公式の説明） [src: pam_christian_situation_l_japanese.yml, situation_parameter_the_christian_church_minimal_centralization] [src: pam_christian_situation.txt:363] [src: 00_theocracy_lease.txt:283]
- [ ] 状況の「すべてに対する効果」と、自分のグループの「外交」で、コストが下がる行動の行を探し、先に使う（聖界のみ） {#phase-cheap}
  - なぜ: 暗黒時代は公会議の開催コストが下がる。主勢力（聖職）は、改宗と十字軍の局面で宗教指導者の勅書が50%安く、聖職叙任権闘争では候補者への支援の敬虔点が半分になる [src: pam_christian_situation_l_japanese.yml, situation_parameter_the_christian_church_cheaper_ecumenical_councils] [src: pam_christian_situation_l_japanese.yml, situation_parameter_the_christian_church_cheaper_bulls] [src: pam_christian_situation.txt:551] [src: pam_christian_situation.txt:869] [src: pam_christian_situation.txt:1492] [src: pam_christian_situation.txt:1331]
- [ ] 局面が「聖職叙任権闘争」なら、「次回の叙任権会議」までの残りと、投票が教会と王冠のどちらに傾くかを確かめる（聖界のみ） {#phase-investiture}
  - なぜ: 期限が来ると叙任権会議が開かれ、「聖職者任命制」の教義が置き換わる。世俗の統治者は聖職者に反対票を強制できる。候補者への支援は期限の前に（公式の説明） [src: pam_christian_situation_l_japanese.yml, CHRISTIAN_CHURCH_INVESTITURE_TIME_REMAINING_TT] [src: pam_christian_situation_l_japanese.yml, CHRISTIAN_CHURCH_INVESTITURE_VOTE_CHURCH_AHEAD]

### 公会議があるとき

- [ ] 主催者なら、第1・第2の討議の選択肢にカーソルを合わせ、可決したときの信条の位置づけを読んでから、議題の信条を中核にする・禁止する・容認する・認知する提案から選ぶ（聖界のみ） {#council-propose}
  - なぜ: 提案は賛成票が反対票以上で可決する（同数も可）。流派の中核の信条や教義を取り除く票は、教会分裂の進捗を押し上げる [src: pam_ecumenical_council_events.txt:1533] [src: pam_ecumenical_council_events.txt:1678] [src: pam_ecumenical_council_events.txt:1712] [src: pam_ecumenical_council_events.txt:1735] [src: pam_ecumenical_council_events.txt:4234] [src: pam_christian_situation_l_japanese.yml, CHRISTIAN_CHURCH_SCHISM_PROGRESS_TT]
- [ ] 議題の提案の通知が来たら、立場を決めて「変革に賛成する」か「反対だ」を選ぶ（聖界のみ） {#council-vote}
  - なぜ: 投票権は聖職者、領国祭司の傀儡を持つ統治者、主催者にある。選んだ側が革新派か保守派に数えられる（公式の説明） [src: pam_game_concepts_l_japanese.yml, game_concept_ecumenical_council_groups_help] [src: pam_ecumenical_council_events.txt:2387] [src: pam_ecumenical_council_events.txt:2394]
- [ ] 公会議が終わったら、宗派の画面で議題の信条の位置づけを確かめ、自分の個人的信条が禁止になっていないか見る（聖界のみ） {#council-after}
  - なぜ: 公会議は信条を容認・禁止・中核に動かし、教義も決める。個人的信条は、中核か容認なら霊的充足度が上がり、禁止なら秘密が生じる（公式の説明） [src: pam_game_concepts_l_japanese.yml, game_concept_ecumenical_council_desc] [src: pam_game_concepts_l_japanese.yml, game_concept_personal_tenet_desc]

### 戦争の前

- [ ] 宣戦する前に、相手が宗教指導者でないか確かめる {#war-head}
  - なぜ: 宗教指導者と交戦中だと、好敵手や宿敵と同じく、宗教指導者に直接破門されうる（公式の説明） [src: pam_actions.txt:130] [src: important_actions_l_japanese.yml, action_excommunication_at_risk_desc]
- [ ] 常備軍の連隊の数と規模、傭兵の雇用費を確かめ、聖界の補正を織り込んで兵力を見積もる（聖界のみ） {#war-force}
  - なぜ: 聖界は常備軍連隊の規模と最大数、騎士の上限が−3、傭兵の雇用費が+200% [src: 02_theocratic_government_types.txt:123] [src: 02_theocratic_government_types.txt:124] [src: 02_theocratic_government_types.txt:125] [src: 02_theocratic_government_types.txt:126] [src: modifiers_l_japanese.yml, MOD_MEN_AT_ARMS_LIMIT] [src: modifiers_l_japanese.yml, MOD_MEN_AT_ARMS_CAP]

## 6. 困ったとき

**破門された（重要アクション「破門」）**
- 見る場所: 重要アクションの説明と、修正「最近の破門」が残っているか。残っている間は赦しを求められず、通常は365日続く [src: important_actions_l_japanese.yml, action_excommunicated_recovery_desc] [src: common/scripted_effects/00_religion_effects.txt:541]
- 打ち手: 悔悛が明けたら、公爵以下は有効な聖職者（上位の聖職者がいなければ宗教指導者）に「改心の宣言」を使う。神権制の領主は献身レベル2以上が要る。宗教指導者に破門された者と、王国か帝国の統治者は、宗教指導者へ請願して「破門の解除」を選ぶ（公式の説明） [src: important_actions_l_japanese.yml, action_excommunicated_recovery_desc] [src: 00_religious_interactions.txt:2893] [src: 11_petition_head_of_faith_triggers.txt:62]

**霊的充足度が低く、ストレスが増える**
- 見る場所: 宗派のアイコンにカーソルを合わせた数値と内訳。基準は特性の罪と徳で決まる（公式の説明） [src: pam_game_concepts_l_japanese.yml, game_concept_spiritual_fulfillment_desc] [src: hud.gui:3814]
- 打ち手: 罪の特性を減らし、中核か容認の信条を個人的信条に入れる。聖界は決断「己の罪を告白する」も使う（2章）。−30以下でストレス獲得が10%、−65以下で25%、−95以下で50%（キリスト教）増えるので早めに戻す [src: pam_game_concepts_l_japanese.yml, game_concept_spiritual_fulfillment_desc] [src: 00_spiritual_fulfillment_types.txt:46] [src: 00_spiritual_fulfillment_types.txt:29] [src: 00_spiritual_fulfillment_types.txt:5] [src: 00_spiritual_fulfillment_types.txt:7]

**国庫が0を下回った（重要アクション「あなたは負債を抱えています」）（聖界のみ）**
- 見る場所: 重要アクションの説明にある債務レベルの影響と、国庫の月の収支 [src: important_actions_l_japanese.yml, action_in_treasury_debt_desc] [src: 00_realm_actions.txt:447]
- 打ち手: 債務の間は戦争を宣言できず、国庫が要る常備軍を強化できず、領地に腐敗が広がり、封臣が派閥に加わりやすい。軍の解散、常備軍の縮小、宮廷役職の剥奪で支出を減らし、金があれば「国庫に資金追加」で移す（公式の説明） [src: important_actions_l_japanese.yml, action_in_treasury_debt_desc] [src: hud.gui:6605]

**教会分裂の進捗が上がっている（聖界のみ）**
- 見る場所: 状況「キリスト教会」の「教会分裂の進捗」（n/13） [src: pam_christian_situation_l_japanese.yml, CHRISTIAN_CHURCH_SCHISM_PROGRESS] [src: pam_values.txt:9400]
- 打ち手: 公会議での中核の信条や教義の削除、王国以上の統治者どうしの流派間の戦争、聖地の改宗や格下げ、他方の流派による流派指導者の殺害が1点ずつ足される。自分で足さないようにし、13に達したら4章の決断を使う（公式の説明） [src: pam_christian_situation_l_japanese.yml, CHRISTIAN_CHURCH_SCHISM_PROGRESS_TT] [src: pam_values.txt:9402] [src: pam_values.txt:9406]

**公会議が開けない、または途中で解散した（聖界のみ）**
- 見る場所: 活動「公会議」の開始画面に出る失敗理由と、解散のときの通知 [src: ecumenical_council.txt:17] [src: ecumenical_council_activity_l_japanese.yml, ecumenical_council_no_quorum_toast_tt]
- 打ち手: 理由ごとに直す。前回から25年未満、同じ信仰で別の公会議が開催中、叙任権会議が保留中なら待つ。聖職管区の保持者が信仰全体で5人未満、または出席者が5人未満（主催者が保持者なら4人未満）なら、人数がそろってから開く [src: ecumenical_council.txt:11] [src: ecumenical_council.txt:19] [src: ecumenical_council.txt:22] [src: ecumenical_council.txt:40] [src: ecumenical_council.txt:337] [src: pam_values.txt:1882] [src: pam_scripted_triggers.txt:179]

**「神権制の後継者を指名」が選べない、またはボタンが出ない**
- 見る場所: 相互作用ウィンドウの赤字の失敗理由。ボタン自体が出ないなら、領国の継承法が「聖職者の任命」か（教皇の「神権選挙制」では出ない） [src: pam_interactions.txt:47] [src: pam_interactions.txt:48]
- 打ち手: 失敗理由ごとに直す。王朝がなければ決断で創設する。相手は、自分より年上でなく、所領を持たず、同じ信仰で、流派の「聖職者の性別」の教義に合う成人にする（4章「後を託す」） [src: pam_interactions.txt:66] [src: pam_interactions.txt:73] [src: pam_interactions.txt:78] [src: pam_interactions.txt:82] [src: pam_interactions.txt:86]

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|
| 霊的充足度 | 範囲は−100〜100。ストレス獲得は−30以下で+10%、−65以下で+25%、−95以下で+50%（キリスト教）。0未満で告白が効き、30以上（「赦免」）で宮廷聖職者、65以上（「安寧」）で流派指導者への親睦工作と「信仰心を誇示する」、95以上（「恩寵」）で宗教指導者への親睦工作 | [src: 00_defines.txt:890] [src: 00_defines.txt:891] [src: 00_spiritual_fulfillment_types.txt:46] [src: 00_spiritual_fulfillment_types.txt:29] [src: 00_spiritual_fulfillment_types.txt:5] [src: pam_actions.txt:694] [src: 00_spiritual_fulfillment_types.txt:62] [src: pam_values.txt:2143] [src: pam_values.txt:2144] |
| 個人的信条の枠 | 基本1。献身レベル4で+1、5でもう+1。外す・入れ替えたあとは1,095日（3年）変えられない | [src: 00_defines.txt:904] [src: 00_defines.txt:906] [src: 00_basic_modifiers.txt:159] [src: 00_basic_modifiers.txt:163] |
| 貸与の取り分 | 上位者へは、徴募兵が15%、税は聖界で5%（最低限）・10%（中程度）・20%（高度。宗教指導者にも1%）、神権制で25%。主君の上限は税25%・徴募兵50%（聖界の固定義務は税15%） | [src: 00_theocracy_lease.txt:68] [src: 00_theocracy_lease.txt:313] [src: 00_theocracy_lease.txt:142] [src: 00_theocracy_lease.txt:166] [src: 00_theocracy_lease.txt:179] [src: 00_theocracy_lease.txt:207] [src: 00_theocracy_lease.txt:26] [src: 00_theocracy_lease.txt:70] [src: 00_theocracy_lease.txt:212] [src: 00_theocracy_lease.txt:283] |
| 教会の支配権 | 段階2は封臣の納付+10%、段階3は+25%。必要な献身レベルは段階1・2・3で1・2・3。上げたあとは20年待つ | [src: 00_realm_laws.txt:655] [src: 00_realm_laws.txt:739] [src: common/scripted_triggers/00_law_triggers.txt:631] [src: common/scripted_triggers/00_law_triggers.txt:636] [src: common/scripted_triggers/00_law_triggers.txt:641] [src: 00_realm_laws.txt:4] |
| 封臣の納付（神権制・聖界） | 税は5%＋10%×主君の献身レベル、徴募兵は10%×レベル。宗派が違えばどちらも10% | [src: theocratic.txt:21] [src: theocratic.txt:24] [src: theocratic.txt:11] [src: theocratic.txt:7] |
| 敬虔点の費用 | 霊的な助言100、教会の国庫から金を求める100、下位者に金を求める100〜250、信仰心を誇示する250、神権制統治の採用500（と威信点750） | [src: 00_basic_values.txt:1133] [src: 00_basic_values.txt:1134] [src: 00_basic_values.txt:1135] [src: spiritual_counsel_interaction.txt:17] [src: pam_interactions.txt:21720] [src: pam_values.txt:9765] [src: pam_values.txt:9766] [src: pam_decisions.txt:555] [src: pam_decisions.txt:556] |
| 候補者への支援 | 中程度は敬虔点250でスコア+20、大規模は500で+50。「聖職叙任権闘争」の局面は敬虔点が半分。教皇候補スコアは250で+10（金も払えば+20） | [src: pam_values.txt:2516] [src: pam_values.txt:2520] [src: pam_interactions.txt:1024] [src: pam_interactions.txt:1021] [src: pam_christian_situation.txt:1331] [src: pam_values.txt:1674] [src: pam_values.txt:1673] [src: pam_interactions.txt:15013] |
| 位を上げる費用 | 管区の創設・拡張は伯爵領1つにつき敬虔点50。枢機卿職の要請は基準1000（宗教指導者より献身レベルが1段高いと−100、低いと+250）で、枢機卿は70人まで。投票への影響は250、敬虔な善行の周知は500 | [src: pam_values.txt:8227] [src: pam_values.txt:8258] [src: pam_values.txt:8745] [src: pam_values.txt:8751] [src: pam_values.txt:8764] [src: 01_puppet_interactions.txt:2333] [src: pam_interactions.txt:14550] [src: pam_decisions.txt:3159] |
| 教会を動かす費用 | 勅書500、聖戦の誘発は称号が伯爵領100・公爵領200・王国300、王国の聖別は金500と敬虔点750（相手の献身レベル1につき−50）、教会継承の要求は500、王朝の創設は威信点750。公会議は金500で25年に1回、聖職管区の保持者5人が要る | [src: pam_values.txt:10329] [src: pam_values.txt:9811] [src: pam_values.txt:9819] [src: pam_values.txt:9976] [src: pam_values.txt:10069] [src: pam_values.txt:10072] [src: pam_values.txt:8667] [src: pam_decisions.txt:398] [src: pam_values.txt:1911] [src: ecumenical_council.txt:337] [src: pam_values.txt:1882] |
| 破門と好感度 | 宗教指導者への好感度が50以上なら、好敵手・宿敵・交戦相手でない限り警告は出ない。悔悛は通常365日。神権制の領主の「改心の宣言」は献身レベル2以上 | [src: pam_actions.txt:154] [src: common/scripted_effects/00_religion_effects.txt:541] [src: 00_religious_interactions.txt:2893] |
| 聖界の軍事補正 | 常備軍連隊の規模・最大数と騎士の上限が−3、傭兵の雇用費が+200% | [src: 02_theocratic_government_types.txt:123] [src: 02_theocratic_government_types.txt:126] |
| 公会議と教会分裂 | 提案は賛成が反対以上で可決。成立には聖職管区の保持者の出席が5人（主催者が保持者なら4人）。教会分裂の進捗は13で決着。主勢力（聖職）の宗教指導者の勅書は改宗・十字軍の局面で50%安い | [src: pam_ecumenical_council_events.txt:4234] [src: pam_values.txt:1882] [src: pam_values.txt:1884] [src: pam_values.txt:9400] [src: pam_christian_situation.txt:869] [src: pam_christian_situation.txt:1492] |

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

- 聖界（Ecclesiastical）／神権制（Theocracy）／教会領（Church Holdings）／寺院領（Temple Holding）／聖界所領（Ecclesiastical Estate）
- 上位者（Superior）／主君（Liege）／宗教指導者（Head of Faith）／流派指導者（Head of Rite）／宮廷聖職者（Court Chaplain）／枢機卿（Cardinal）
- 貸与契約（Lease Contract）／借手（Lessee）／教会の義務（Church Obligations）／教会の中央集権化（Church Centralization）／世俗の義務（Secular Obligations）／国庫（Treasury）
- キリスト教会（The Christian Church）／局面（Chapter）／聖職管区（Clerical Region）／大司教区（Archdiocese）／流派（Rite）／教義（Doctrine）
- 敬虔点（Piety）／献身レベル（Level of Devotion）／霊的充足度（Spiritual Fulfillment）／個人的信条（Personal Tenet）／個人的信念（Personal Beliefs）
- 教会の支配権（Church Authority）／フック（Hook）／破門（Excommunication）／威信点（Prestige）／名声レベル（Level of Fame）
- 聖職称号（Clerical Title）／枢機卿団（College of Cardinals）／枢機卿職（Cardinalate）／教皇候補スコア（Papabile Score）／候補者スコア（Candidate Score）
- 勅書（Bull）／公会議（Ecumenical Council）／大分裂（Great Schism）／聖戦（Holy War）／傀儡（Puppet）／傀儡使い（Puppeteer）／世俗統治者の傀儡（External Ruler Puppet）
- 後継者（Heir）／指名後継者（Designated Heir）／代替後継者（Fallback Heir）／王朝（Dynasty）／王朝の当主（Dynast）／栄誉点（Dynasty Prestige）／名声レベル（Prestige Level）
- 状況（Situation）／主勢力（聖職）（Main Power (Clerical)）／暗黒時代（Saeculum Obscurum）／聖職叙任権闘争（Investiture Controversy）／教会分裂（Schism）／革新派（Innovator）／保守派（Conservative）
- 好感度（Opinion）／好敵手（Rival）／宿敵（Nemesis）／改心の宣言（Declaration of Repentance）／国庫債務（Treasury Debt）／常備軍（Men-at-Arms）／傭兵（Mercenary）／継承順位（Line of Succession）
- 通知（スクリプト上の important action。個別のアイコンで出る alert と、一覧に出る action がある）

## 9. 出典

### 一次情報

- パスは `Crusader Kings III/game` フォルダからの相対。同名のファイルが複数あるものは相対パスで書く
- `common/governments/02_theocratic_government_types.txt`
- `common/religion/religion_types/`（`00_christianity.txt`・`_religion_types.info`）、`common/bookmarks/bookmarks/00_bookmarks.txt`
- `common/lease_contracts/00_theocracy_lease.txt`、`common/subject_contracts/contracts/theocratic.txt`、`common/laws/00_realm_laws.txt`
- `common/spiritual_fulfillment/00_spiritual_fulfillment_types.txt`、`common/hook_types/00_hook_types.txt`、`common/modifiers/00_basic_modifiers.txt`
- `common/defines/00_defines.txt`、`common/script_values/`（`00_basic_values.txt`・`00_title_tiers_values.txt`・`02_religion_values.txt`・`pam_values.txt`）
- `common/scripted_triggers/`（`00_councillor_triggers.txt`・`00_important_actions_triggers.txt`・`00_law_triggers.txt`・`00_religious_triggers.txt`・`00_scheme_triggers.txt`・`pam_scripted_triggers.txt`）
- `common/important_actions/`（`00_inheritance_actions.txt`・`00_realm_actions.txt`・`pam_actions.txt`）、`common/decisions/dlc_decisions/pam/`（`bulls_decisions.txt`・`pam_decisions.txt`）、`events/dlc/pam/pam_decision_events.txt`
- `common/character_interactions/`（`00_demand_church_succession_interactions.txt`・`00_puppet_interactions.txt`・`01_puppet_interactions.txt`・`pam_interactions.txt`・`spiritual_counsel_interaction.txt`）
- `common/domiciles/`（`types/00_domicile_types.txt`・`buildings/11_ecclesiastical_domicile_buildings.txt`）
- `common/activities/activity_types/ecumenical_council.txt`、`common/situation/situations/pam_christian_situation.txt`、`common/puppets/types/pam_puppet_types.txt`、`common/succession_appointment/clerical_christian.txt`、`common/laws/00_succession_laws.txt`
- `common/scripted_effects/`（`00_religion_effects.txt`・`pam_ecumenical_council_effects.txt`）、`common/character_interactions/00_religious_interactions.txt`、`common/scripted_triggers/11_petition_head_of_faith_triggers.txt`、`events/activities/ecumenical_council_activity/pam_ecumenical_council_events.txt`
- `gui/`（`window_character.gui`・`hud.gui`・`window_cardinals.gui`・`window_intrigue.gui`・`interaction_templates.gui`）、`localization/japanese/`（ゲーム概念・重要アクション・チュートリアル・PAM 関連）

### コミュニティ情報
