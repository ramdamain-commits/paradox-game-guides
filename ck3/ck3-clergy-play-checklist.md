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

## 4. 教会を動かす・後を託す

## 5. 定期ルーチン {.routine}

## 6. 困ったとき

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|
| 霊的充足度 | 範囲は−100〜100。ストレス獲得は−30以下で+10%、−65以下で+25%。0未満で告白が効き、30以上（「赦免」）で宮廷聖職者、65以上（「安寧」）で流派指導者への親睦工作と「信仰心を誇示する」、95以上（「恩寵」）で宗教指導者への親睦工作 | [src: 00_defines.txt:890] [src: 00_defines.txt:891] [src: 00_spiritual_fulfillment_types.txt:46] [src: 00_spiritual_fulfillment_types.txt:29] [src: pam_actions.txt:694] [src: 00_spiritual_fulfillment_types.txt:62] [src: pam_values.txt:2143] [src: pam_values.txt:2144] |
| 個人的信条の枠 | 基本1。献身レベル4で+1、5でもう+1。外す・入れ替えたあとは1,095日（3年）変えられない | [src: 00_defines.txt:904] [src: 00_defines.txt:906] [src: 00_basic_modifiers.txt:159] [src: 00_basic_modifiers.txt:163] |
| 貸与の取り分 | 上位者へは、徴募兵が15%、税は聖界で5%（最低限）・10%（中程度）・20%（高度。宗教指導者にも1%）、神権制で25%。主君の上限は税25%・徴募兵50%（聖界の固定義務は税15%） | [src: 00_theocracy_lease.txt:68] [src: 00_theocracy_lease.txt:313] [src: 00_theocracy_lease.txt:142] [src: 00_theocracy_lease.txt:166] [src: 00_theocracy_lease.txt:179] [src: 00_theocracy_lease.txt:207] [src: 00_theocracy_lease.txt:26] [src: 00_theocracy_lease.txt:70] [src: 00_theocracy_lease.txt:212] [src: 00_theocracy_lease.txt:283] |
| 教会の支配権 | 段階2は封臣の納付+10%、段階3は+25%。必要な献身レベルは段階1・2・3で1・2・3。上げたあとは20年待つ | [src: 00_realm_laws.txt:655] [src: 00_realm_laws.txt:739] [src: common/scripted_triggers/00_law_triggers.txt:631] [src: common/scripted_triggers/00_law_triggers.txt:636] [src: common/scripted_triggers/00_law_triggers.txt:641] [src: 00_realm_laws.txt:4] |
| 封臣の納付（神権制・聖界） | 税は5%＋10%×主君の献身レベル、徴募兵は10%×レベル。宗派が違えばどちらも10% | [src: theocratic.txt:21] [src: theocratic.txt:24] [src: theocratic.txt:11] [src: theocratic.txt:7] |
| 敬虔点の費用 | 霊的な助言100、教会の国庫から金を求める100、下位者に金を求める100〜250、信仰心を誇示する250、神権制統治の採用500（と威信点750） | [src: 00_basic_values.txt:1133] [src: 00_basic_values.txt:1134] [src: 00_basic_values.txt:1135] [src: spiritual_counsel_interaction.txt:17] [src: pam_interactions.txt:21720] [src: pam_values.txt:9765] [src: pam_values.txt:9766] [src: pam_decisions.txt:555] [src: pam_decisions.txt:556] |

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

- 聖界（Ecclesiastical）／神権制（Theocracy）／教会領（Church Holdings）／寺院領（Temple Holding）／聖界所領（Ecclesiastical Estate）
- 上位者（Superior）／主君（Liege）／宗教指導者（Head of Faith）／流派指導者（Head of Rite）／宮廷聖職者（Court Chaplain）／枢機卿（Cardinal）
- 貸与契約（Lease Contract）／借手（Lessee）／教会の義務（Church Obligations）／教会の中央集権化（Church Centralization）／世俗の義務（Secular Obligations）／国庫（Treasury）
- キリスト教会（The Christian Church）／局面（Chapter）／聖職管区（Clerical Region）／大司教区（Archdiocese）／流派（Rite）／教義（Doctrine）
- 敬虔点（Piety）／献身レベル（Level of Devotion）／霊的充足度（Spiritual Fulfillment）／個人的信条（Personal Tenet）／個人的信念（Personal Beliefs）
- 教会の支配権（Church Authority）／フック（Hook）／破門（Excommunication）／威信点（Prestige）／名声レベル（Level of Fame）
- 通知（スクリプト上の important action。個別のアイコンで出る alert と、一覧に出る action がある）

## 9. 出典

### 一次情報

- パスは `Crusader Kings III/game` フォルダからの相対。同名のファイルが複数あるものは相対パスで書く
- `common/governments/02_theocratic_government_types.txt`
- `common/religion/religion_types/`（`00_christianity.txt`・`_religion_types.info`）、`common/bookmarks/bookmarks/00_bookmarks.txt`
- `common/lease_contracts/00_theocracy_lease.txt`、`common/subject_contracts/contracts/theocratic.txt`、`common/laws/00_realm_laws.txt`
- `common/spiritual_fulfillment/00_spiritual_fulfillment_types.txt`、`common/hook_types/00_hook_types.txt`、`common/modifiers/00_basic_modifiers.txt`
- `common/defines/00_defines.txt`、`common/script_values/`（`00_basic_values.txt`・`pam_values.txt`）
- `common/scripted_triggers/`（`00_councillor_triggers.txt`・`00_law_triggers.txt`・`00_scheme_triggers.txt`・`pam_scripted_triggers.txt`）
- `common/important_actions/pam_actions.txt`、`common/decisions/dlc_decisions/pam/pam_decisions.txt`、`events/dlc/pam/pam_decision_events.txt`
- `common/character_interactions/`（`pam_interactions.txt`・`spiritual_counsel_interaction.txt`）
- `common/domiciles/`（`types/00_domicile_types.txt`・`buildings/11_ecclesiastical_domicile_buildings.txt`）
- `gui/`（`window_character.gui`・`hud.gui`）、`localization/japanese/`（ゲーム概念・重要アクション・チュートリアル・PAM 関連）

### コミュニティ情報
