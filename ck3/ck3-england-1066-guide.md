# CK3 イングランド 1066 攻略ガイド（Patch 1.19.0.1 時点）

> ハロルド・ゴドウィンソン → ノルマン撃退からブリタニア帝国を狙う初代から3代目以降までの整理。
> 2026-04-09 確認時点の最新パッチ 1.19.0.1（Scribe）に合わせて更新。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。

---

## パッチ 1.19 / 1.19.0.1 でのイングランド関連変更点

1.19「Scribe」はイングランド固有イベントよりも、統治システム刷新の影響が大きい。ハロルド 1066 は「開幕の連戦で正統性を稼ぎやすいが、代替わりで崩れやすい」シナリオになった。

| 変更 | 内容 |
|------|------|
| 正統性（Legitimacy）新設 | 開幕2戦の勝敗と即位後の立て直しが直結。敗戦や継承失敗の痛手が大きい |
| 直轄領上限の計算式変更 | 管理スキル依存から教育特性依存へ。ハロルド本人は軍事Lv3で扱いやすいが、後継者の教育差が大きい |
| 封臣のスタンス導入 | ウィテナゲモット選挙制に加えて、封臣の期待値と後継者の相性も見る必要がある |
| 戴冠式（Coronation）と誓約（Oath） | ノルマン撃退後の安定化手段。戦後に金を使い切ると立て直しが遅れる |
| 叙勲（Accolade）刷新 | 優秀な騎士を中長期で育てる価値が上昇。初代の戦後再編に影響 |

---

## 開始状況（1066年）

| 項目 | 値 |
|------|-----|
| キャラクター | ハロルド・ゴドウィンソン（Harold Godwinson、character:122） [src: history/characters/anglo_saxon.txt:122] |
| 爵位 | イングランド王（Kingdom of England、k_england） [src: history/titles/k_england.txt:1066.1.5] |
| 王朝 | ゴドウィン家（dynasty:756） [src: history/characters/anglo_saxon.txt:122] |
| 政体 | 封建政体（Feudal） |
| 宗派（Faith） | カトリック [src: history/characters/anglo_saxon.txt:122] |
| 文化 | アングロサクソン（culture:anglo_saxon） [src: history/characters/anglo_saxon.txt:122] |
| 継承法 | ウィテナゲモット選挙制（saxon_elective_succession_law） [src: history/titles/k_england.txt:927.7.12; common/laws/01_title_succession_laws.txt:saxon_elective_succession_law] |
| 直轄領（Domain） | ウェセックス周辺 |
| 主要能力 | 外交6・管理6・謀略5・軍事4（教育：軍事Lv3。1.19 では直轄領上限 +1 の基礎） [src: history/characters/anglo_saxon.txt:122; common/traits/00_traits.txt:education_martial_3] |

### 開幕の脅威

| 脅威 | 方角 | 詳細 |
|------|------|------|
| ウィリアム征服王（ノルマンディー公） | 南 | **最大の脅威**。イングランド王位を請求。大軍で上陸してくる |
| ハーラル・ハードラーダ（ノルウェー王） | 北 | ヴァイキングの侵攻。二正面作戦を強いられる |
| スコットランド | 北 | 弱いが、ノルマン・ヴァイキング戦で消耗した隙を突かれるリスク |

### 初期の強み・弱み

| 強み | 弱み |
|------|------|
| イングランド王位で大量の徴募兵（Levies）を動員可能 | 二正面作戦の開幕が確定 |
| 開幕2戦に勝てば正統性を一気に稼げる | 分割連合相続制で領土が分散するリスク |
| 島国の地理的優位（大陸からの侵攻は限定的） | ハロルドに後継者問題あり（兄弟に領地が流れる） |
| ハロルド本人は軍事Lv3教育で直轄領上限を維持しやすい | 1.19 では代替わりで正統性・封臣の期待・直轄領上限が同時に崩れやすい |

---

## Day 1（ポーズ解除直後）

### キャラクター設定

1. **ライフスタイルを軍事（Martial）に設定**
   - 方針は「戦略方針（Strategy Focus）」を推奨（コミュニティ知見） [src: focuses_l_japanese.yml, martial_strategy_focus]
   - 開幕の戦争を生き残るために軍事パークが最優先

2. **評議会（Council）を確認・配置**
   - 元帥（Marshal）: 軍事スキル最高のキャラを任命
   - 宰相（Chancellor）: 外交スキルが高い人物を配置

3. **騎士（Knight）を確認**
   - 武勇の高い廷臣（Courtier）を騎士に任命。戦闘で大きな差が出る

### 戦争準備

4. **軍勢（Army）を集結地（Rally Point）に集める**
   - 全徴募兵 + 常備軍を北部に集結（対ハーラル戦を先に処理）

5. **傭兵団（Mercenary Company）の雇用を検討**
   - 金（Gold）に余裕があれば傭兵で兵力を補強
   - ただし 1.19 では戦後の戴冠式資金も必要。使い切らない

6. **同盟を確認**
   - 婚姻（Marriage）で同盟を組めるなら組む。ただし開幕は時間がないため、既存の関係を活用

---

## 時系列戦略

### 初代ハロルド（1066〜1090頃）: ノルマン撃退と王権安定化

#### 開幕の二正面作戦（コミュニティ知見）

1. **まず北のハーラル・ハードラーダを撃退**
   - ハーラルは兵力が少なめ。全軍で北上して速やかに撃破
   - スタンフォード・ブリッジの戦いを再現

2. **返す刀で南のウィリアムを迎撃**
   - ハーラル撃退後、全軍を南に転進
   - ヘイスティングスでの決戦。ハロルドが戦死すると致命的なので**自ら指揮官にしない選択肢も検討**

3. **両方の戦争に勝利したら内政に移行**

#### 内政の安定化

- **継承法を意識する**: 1066開始時の継承法はウィテナゲモット選挙制（saxon_elective_succession_law）。封臣の選挙で後継者が決まるため、封臣の好感度が重要 [src: history/titles/k_england.txt:927.7.12; common/laws/01_title_succession_laws.txt:saxon_elective_succession_law]。ゲームが進むと分割連合相続制（confederate_partition_succession_law）に変更されるリスクがあるため要確認 [src: succession_laws_l_japanese.yml, confederate_partition_succession_law]。1.19 以降はこれに正統性と封臣のスタンスが重なり、継承直後の安定度は「誰が継ぐか」だけでなく「誰に支持されるか」でも変わる。[src: game_concepts_l_japanese.yml, game_concept_legitimacy / game_concept_vassal_stance]
- **婚姻で後継者を確保**: ハロルドの子供が少ない場合は早めに婚姻
- **封臣（Vassal）の好感度とスタンスを管理**: 戦争直後は不満が溜まりやすい。1.19 では封臣のスタンスが継承時の期待値にも触るため、強力な封臣の性向を見ておく
- **即位直後の正統性回復を意識する**: 1.19 以降は戴冠式（Coronation）と誓約（Oath）が代替わり直後の立て直し手段になる。継承前から金を残しておくと事故が減る。[src: coronation_activity_l_japanese.yml, activity_coronation_host_desc]
- **請求権（Claim）の整理**: ウェールズ、スコットランドへの請求権を確認

### 2代目（1090〜1130頃）: 島内統一とブリタニアへの布石

#### 新キャラクターの初動

- **戴冠式と祝宴で正統性を立て直す**
- **ライフスタイルを選び直す**（管理 or 外交が安定）
- **評議会を再配置**
- **封臣契約（Vassal Contract）と封臣のスタンスを見直す**
- **前代の借金や同盟を整理する**

#### 拡張目標

| 目標 | 方法 |
|------|------|
| ウェールズ征服 | 請求権捏造 or 聖戦。弱い相手から |
| スコットランド征服 or 同君化 | 婚姻外交で請求権を獲得するのが安全 |
| アイルランド支配 | 余裕があれば。直轄領上限に注意 |

#### 相続対策

- **長子相続制（Primogeniture）への移行を目指す** [src: succession_laws_l_japanese.yml, single_heir_succession_law]
  - 革新性「長子相続（innovation_primogeniture）」で解放される [src: cultural_innovations_l_japanese.yml, innovation_primogeniture]
  - アングロサクソン文化の革新速度に注意
- **後継者の教育を優先する**: 1.19 以降は教育特性 Lv3 以上が直轄領上限に直結する。管理スキルを後から伸ばしても補いにくいため、後見人選びの優先度が上がる。[src: common/traits/00_traits.txt; common/defines/00_defines.txt:NDomain]
- **即位後の戴冠式資金を残す**: 1.19 以降は戴冠式で正統性を回復し、封臣の期待値を下げやすい。戦争直後でも現金を使い切らない方が安定する。[src: coronation_activity_l_japanese.yml, activity_coronation_host_desc]
- **選挙と封臣のスタンスを両方見る**: ウィテナゲモット選挙制では、主要封臣が支持しやすい後継者を育てると継承事故を減らしやすい [src: history/titles/k_england.txt:927.7.12; game_concepts_l_japanese.yml, game_concept_vassal_stance]
- **次男以降への対策**: 公爵領を意図的に作成し、分割の影響を制御する

### 3代目以降: ブリタニア帝国の形成

- **ブリタニア帝国（Empire of Britannia、e_britannia）の形成条件を確認** [src: common/landed_titles/00_landed_titles.txt:e_britannia; common/scripted_triggers/00_game_rule_triggers.txt:rule_title_creation_imperial_power_projection_title_creation_trigger]
  - de jure 称号に k_england・k_wales・k_scotland・k_ireland・k_cornwall・k_mann_the_isles が含まれる（ただし建国の直接条件は `can_create` のゲームルール設定による）
  - 十分な威信点（Prestige）

- **大陸進出**
  - ノルマンディーなどフランス領への請求権を活用
  - ただし大陸領は防衛が困難。優先度は島内統一の後

- **宗教・文化戦略**
  - カトリック維持が安定。教皇との関係で請求権を得やすい
  - 文化の混合（ノルマン文化との統合）は長期的な選択肢

---

## 軍事ドクトリン

### 兵力構成

| 兵種 | 方針 |
|------|------|
| 徴募兵（Levies） | 主力の数合わせ。封臣からの動員が大半 |
| 常備軍（Men-at-Arms） | 精鋭。ハスカール（重歩兵）が序盤の主力 [src: 00_maa_types.txt, 00_cultural_maa_types.txt] |
| 騎士（Knight） | 個人戦闘力が高い。1.19 以降は優秀な騎士を叙勲候補として育てる価値も高い |
| 傭兵（Mercenary） | 金があるときの緊急戦力。開幕の二正面戦争で有用 |

### 常備軍の推奨兵種

| 兵種 | 理由 |
|------|------|
| ハスカール（Huscarls） | アングロサクソン固有の重歩兵。damage=40、toughness=26。槍兵・弓兵・民兵に有利。文化伝統「ハード（tradition_hird）」で解放 [src: 00_cultural_maa_types.txt, huscarl; 00_west_germanic.txt, anglo_saxon] |
| 弓兵（Archers） | damage=25、toughness=10。丘陵・森林ボーナスあり。斥候兵に有利（コミュニティ知見：防衛戦に有効） [src: 00_maa_types.txt, bowmen] |
| 重装騎兵（Armored Horsemen） | damage=100、toughness=35。平原で大幅ボーナス。弓兵・火薬に有利。鐙（innovation_arched_saddle）が必要 [src: 00_maa_types.txt, armored_horsemen] |

---

## 外交・同盟

### 必須外交

| 対象 | 行動 | 理由 |
|------|------|------|
| フランス王 | 中立〜友好維持 | ノルマンディー問題を刺激しない |
| スコットランド王 | 婚姻外交 | 将来の統合に向けた請求権獲得 |
| 教皇 | 好感度維持 | 聖戦の許可、請求権の獲得に有利 |
| 神聖ローマ帝国（HRE）皇帝 | 中立 | 不干渉が理想 |

### 婚姻戦略

- ハロルドの子供を有力な王家と婚姻させ、同盟を確保
- 2代目以降は請求権獲得のための戦略的婚姻を重視
- **王朝の威信点（Prestige）を意識**: 格下との婚姻は威信点がマイナス（最低 -100）になる。格上との婚姻ほど高い威信点が得られる（最大 +900） [src: common/defines/00_defines.txt:NDynasty:MARRIAGE_PRESTIGE]（「栄誉点」ではなく「威信点」が正確）
- **低正統性の時期は婚姻受諾が落ちる**: 代替わり直後や敗戦直後は、先に正統性を立て直してから大型婚姻を狙う方が通しやすい [src: game_concepts_l_japanese.yml, game_concept_legitimacy]

---

## 内政・経済

### 直轄領管理

| 優先事項 | 内容 |
|----------|------|
| 直轄領上限の確認 | 1.19 では管理スキルではなく教育特性レベルが主要因。ハロルドは軍事Lv3で直轄領上限 +1 を持つため、王位ベース3と合わせて直轄領4前後を基準に見やすい。後継者の教育が低いと即座に超過しやすい [src: common/defines/00_defines.txt:NDomain; common/modifiers/00_basic_modifiers.txt:king_modifier; common/traits/00_traits.txt:education_martial_3; history/characters/anglo_saxon.txt:122] |
| 開発度の高い伯爵領を直轄に | ウェセックス、ロンドン周辺が候補 |
| 戴冠式資金を確保 | 代替わり直後の戴冠式・祝宴のため、拡張前に現金を残す |
| 建造物の建設 | 収入と徴募兵を増やす建造物を優先 |

### 封臣管理

| 対策 | 方法 |
|------|------|
| 好感度（Opinion）を維持 | 恩赦、祝宴、贈り物で管理 |
| 正統性を維持 | 1.19 以降は低正統性で婚姻・同盟・派閥管理が悪化する。継承直後ほど祝宴・戦争勝利・戴冠式で立て直したい。[src: common/legitimacy/00_legitimacy.txt:legitimacy_level_1; coronation_activity_l_japanese.yml, activity_coronation_host_desc] |
| 封臣のスタンスを確認 | 1.19 以降は各封臣のスタンスが継承直後の期待値と後継者支持に影響する。強力な封臣だけでなく「礼節」「名誉追求者」「地方主義」などの傾向も見る。[src: game_concepts_l_japanese.yml, game_concept_vassal_stance; vassal_stances_l_japanese.yml] |
| 強力な封臣を牽制 | フック（Hook）の活用、封臣契約の見直し |
| 派閥（Faction）を監視 | 不満が溜まると反乱。恐怖（Dread）で抑制も可 |

---

## 固有イベント時系列

| イベント名 | ID | 発生期間/条件 | 推奨選択 | 効果 |
|------------|-----|--------------|----------|------|
| ヴァイキング侵攻（ハーラル）戦争開始 | CB: `norwegian_invasion_cb` | 1066.8.1〜（歴史的戦争として自動開始） | 全軍北上で先に撃退 | イングランド王位 (k_england) 防衛戦 [src: history/wars/00_wars.txt, war_1066_Harald_Invasion] |
| ノルマン征服（ウィリアム）戦争開始 | CB: `norman_conquest_cb` | 1066.9.8〜（歴史的戦争として自動開始） | 全力で迎撃。ハロルド戦死を防ぐ | イングランド王位 (k_england) 防衛戦 [src: history/wars/00_wars.txt, war_1066_Norman_Conquest] |
| 戦闘：スタンフォード・ブリッジ（ハロルド勝利） | `game_rule.1101` | ハーラル侵攻戦争中、「ノルマン征服の結果」ゲームルールが「ハロルド勝利」に設定されている場合 | 選択肢A: イングランドはヴァイキングの支配から解放される | ハーラル撃退。ゲームルール依存で発火 [src: game_rule_events.txt, game_rule.1101] |
| 戦闘：ヘイスティングス（ハロルド勝利） | `game_rule.1103` | ウィリアム征服戦争中、「ハロルド勝利」ルール有効時 | 選択肢A: 庶子の僭称者に勝利した！ | ウィリアム撃退 [src: game_rule_events.txt, game_rule.1103] |
| 戦闘（ウィリアム勝利/ハロルド敗北） | `game_rule.1121` | ウィリアム征服戦争中、「ウィリアム勝利」ルール有効時 | — | ハロルド敗北イベント。選択肢: 「身の程を知れ、簒奪者め。」 [src: game_rule_events.txt, game_rule.1121] |
| 戦闘（ハーラル勝利/ハロルド敗北） | `game_rule.1111` | ハーラル侵攻戦争中、「ハーラル勝利」ルール有効時 | — | ハロルド敗北 [src: game_rule_events.txt, game_rule.1111] |
| 封臣の不満イベント | — | 初代〜 / 戦争後の不安定期 | 懐柔策を優先（好感度維持）（コミュニティ知見） | 汎用イベントのため固有IDなし |

> **注記**: `game_rule.1101` 〜 `game_rule.1122` 系は「ノルマン征服の結果（rule_historicity_norman_conquest）」ゲームルールが「システム的（デフォルト）」以外に設定されている場合のみ発火する決定論的イベント。デフォルト設定では戦争はゲームシステムで決定され、これらのイベントは発火しない。発火起点は `on_action/army_on_actions.txt` 経由で `game_rule.1021` が戦闘ごとに評価する。[src: game_rule_events.txt, game_rule.1021; common/on_action/game_start.txt]

---

## ライフスタイル・革新性

### 推奨ライフスタイル（世代別）（コミュニティ知見）

| 世代 | 推奨 | 理由 |
|------|------|------|
| 初代（ハロルド） | 軍事（Martial）→ 戦略方針 [src: focuses_l_japanese.yml, martial_strategy_focus] | 開幕の戦争を生き残る |
| 2代目 | 管理（Stewardship）→ 直轄領方針 or 富方針 [src: focuses_l_japanese.yml, stewardship_domain_focus / stewardship_wealth_focus] | 経済基盤の構築。1.19 以降も収入系パークは強いが、直轄領上限自体は教育特性レベルで決まる |
| 3代目 | 外交（Diplomacy）→ 外政方針 [src: focuses_l_japanese.yml, diplomacy_foreign_affairs_focus] | ブリタニア帝国形成に向けた外交 |

### 文化の革新性（Innovation）

- アングロサクソン文化は革新速度が標準
- **長子相続制の解放**が最優先の革新性目標
- 学識ライフスタイルの「学識方針」で革新速度を加速可能

---

### 信仰・文化戦略

- **カトリック維持が安定路線**: 教皇との関係で聖戦 CB が使える
- ノルマン文化との対立: 征服後にノルマン系封臣が増える場合、文化の融合（Hybrid Culture）を検討
- 宗派の変更は基本不要。カトリックの信条（Tenet）で十分なボーナスが得られる

---

## よくあるミス

（コミュニティ知見）

### イングランド 1066 固有

| NG 行動 | 理由 |
|---------|------|
| ハロルドを最前線に立たせる | 戦死するとゲーム終了に近い。指揮官にしない or 後方配置を検討 |
| 南のウィリアムを先に攻撃する | 北のハーラルが暴れて領土を荒らされる。北を先に処理 |
| 戴冠式資金まで使い切る | 1.19 では継承直後の正統性回復が遅れ、封臣管理が苦しくなる |
| 相続対策を怠る | 分割連合相続制に加え、2代目で正統性と直轄領上限も崩れやすい |
| 封臣の不満とスタンスを放置する | 戦争直後や継承直後の反乱・選挙事故が起きやすい |
| 大陸領を優先する | 防衛困難。まず島内を統一してから |

### CK3 全般

| NG 行動 | 理由 |
|---------|------|
| ストレス（Stress）を無視する | 精神崩壊イベントでキャラクターが弱体化 |
| 直轄領上限を超える | 収入と好感度が大幅低下。1.19 では教育の低い後継者で突然超過しやすい |
| 暴政（Tyranny）を溜める | 封臣が一斉に反乱 |
| 同盟なしで大国に宣戦する | 兵力差で蹂躙される |
| 後継者の教育を放置する | 2代目の能力だけでなく直轄領上限まで落ちる |

---

## 用語対照表

> 完全版は [localization-reference.md](localization-reference.md) を参照。以下はこのガイドで使う用語の抜粋。

| 日本語 | 英語 | 補足 |
|--------|------|------|
| 金 | Gold | 通貨 |
| 威信点 | Prestige | 外交・軍事行動に使うリソース |
| 正統性 | Legitimacy | 統治者の支配権の正当性 |
| 戴冠式 | Coronation | 正統性を獲得する活動 |
| 誓約 | Oath | 戴冠式で宣言する統治方針 |
| 敬虔点 | Piety | 宗教行動に使うリソース |
| 栄誉点 | Renown | 王朝全体のリソース |
| ストレス | Stress | キャラクターの精神負荷 |
| 恐怖 | Dread | 封臣への威圧値 |
| 伯爵領 | County | 基本的な支配単位 |
| 王国 | Kingdom | 公爵領の上位称号 |
| 帝国 | Empire | 最大の称号 |
| 封建政体 | Feudal | 西欧の標準政体 |
| 評議会 | Council | 統治補佐機関 |
| 元帥 | Marshal | 軍事担当の評議員 |
| 宰相 | Chancellor | 外交担当の評議員 |
| 密偵頭 | Spymaster | 諜報担当の評議員 |
| 徴募兵 | Levies | 領地から徴集する兵 |
| 常備軍 | Men-at-Arms | 職業軍人。兵種選択可 |
| 騎士 | Knight | 個人戦闘力の高い廷臣 |
| 傭兵 | Mercenary | 金で雇う軍 |
| 封臣 | Vassal | 臣従する領主 |
| 封臣のスタンス | Vassal Stance | 封臣の態度分類 |
| 主君 | Liege | 封臣の上位者 |
| 好感度 | Opinion | キャラクター間の関係値 |
| フック | Hook | 交渉に使える弱み |
| 暴政 | Tyranny | 不当な行為への反発値 |
| 直轄領 | Domain | 自分で直接支配する領地 |
| 叙勲 | Accolade | 騎士への栄誉 |
| 継承 | Succession | 称号の引き継ぎ |
| 分割連合相続制 | Confederate Partition | 最も分散する相続法 |
| 長子相続制 | Primogeniture | 長子が全て継承 |
| 宗派 | Faith | 具体的な信仰 |
| 文化 | Culture | 民族文化 |
| 革新性 | Innovation | 文化が解放する技術 |
| 請求権 | Claim | 称号への権利主張 |
| 開戦事由 | Casus Belli | 略称 CB |
| 聖戦 | Holy War | 宗教的な CB |
| 工作 | Scheme | 暗殺、誘惑等の秘密行動 |
| 決断 | Decision | 特定条件で実行可能なアクション |
| ライフスタイル | Lifestyle | キャラクター成長の方向性 |
| 方針 | Focus | ライフスタイルの方向性 |
| パーク | Perk | ライフスタイルの能力 |

---

## 出典

### 一次情報（ゲームスクリプト・公式）

- ローカルのゲームスクリプトと日本語ローカライズを照合
  - `common/legitimacy/00_legitimacy.txt` — 正統性レベル・効果
  - `common/defines/00_defines.txt:NDomain` — STEWARDSHIP_SKILL_FOR_DOMAIN_LIMIT_INCREASE=200（1.19 直轄領上限）
  - `common/traits/00_traits.txt` — 教育特性の domain_limit 値
  - `common/accolade_types/00_accolade_categories.txt` — 叙勲カテゴリ
  - `localization/japanese/game_concepts_l_japanese.yml` — 基本用語
  - `localization/japanese/succession_laws_l_japanese.yml` — 相続法
  - `localization/japanese/focuses_l_japanese.yml` — ライフスタイル方針名
  - `localization/japanese/game_rules_l_japanese.yml` — ノルマン征服ゲームルール・戦闘イベント名
  - `localization/japanese/regiment_l_japanese.yml` — 兵種名（ハスカール等）
  - `localization/japanese/accolades/accolades_l_japanese.yml` — 叙勲用語
  - `localization/japanese/culture/cultural_innovations_l_japanese.yml` — 文化革新性名
  - `localization/japanese/culture/cultural_maa_innovations_l_japanese.yml` — 兵種解放伝統名
  - `localization/japanese/culture/traditions/cultural_traditions_l_japanese.yml` — 文化伝統名
  - `localization/japanese/activities/coronation_activity_l_japanese.yml` — 戴冠式・誓約
  - `localization/japanese/vassal_stances_l_japanese.yml` — 封臣のスタンス名
  - `common/men_at_arms_types/00_maa_types.txt` — 基本兵種ステータス（bowmen, armored_horsemen 等）
  - `common/men_at_arms_types/00_cultural_maa_types.txt` — 文化固有兵種（huscarl ステータス）
  - `common/culture/cultures/00_west_germanic.txt` — アングロサクソン文化定義（tradition_hird 保有確認）
  - `common/script_values/00_men_at_arms_values.txt` — 兵種コスト値
  - `common/laws/00_succession_laws.txt` — 継承法定義
  - `history/wars/00_wars.txt` — 1066 年歴史的戦争定義（開始日・CB）
  - `events/game_rule_events.txt` — ノルマン征服決定論的イベント（game_rule.1021, 1031, 1032, 1041, 1042, 1051, 1101〜1122）
  - `common/on_action/game_start.txt` — ゲーム開始時の決定論的征服セットアップ
  - `common/casus_belli_types/00_event_war.txt` — norman_conquest_cb / norwegian_invasion_cb 定義
  - `history/characters/anglo_saxon.txt` — Harold Godwinson (character:122) の初期スキル・特性・出生死亡日
  - `history/titles/k_england.txt` — k_england の1066保持者・継承法（saxon_elective_succession_law）設定
  - `common/laws/01_title_succession_laws.txt` — saxon_elective_succession_law 定義（ウィテナゲモット選挙制）
  - `common/landed_titles/00_landed_titles.txt` — e_britannia de jure 定義・can_create 条件
  - `common/scripted_triggers/00_game_rule_triggers.txt` — rule_title_creation_imperial_power_projection_title_creation_trigger 定義
  - `common/defines/00_defines.txt:NDynasty` — MARRIAGE_PRESTIGE 配列（婚姻による威信点増減）
  - `common/modifiers/00_basic_modifiers.txt` — 称号ティア別 domain_limit ボーナス（count/duke/king/emperor）
- [Patch 1.19 Scribe - CK3 Wiki](https://ck3.paradoxwikis.com/Patches)
- [England - CK3 Wiki](https://ck3.paradoxwikis.com/England)
- [1066 Bookmark - CK3 Wiki](https://ck3.paradoxwikis.com/1066)

### コミュニティ情報（補足知見）

プレイ報告・体感ベースの情報。条件の裏取りには一次情報を参照のこと。

- ハロルドの二正面作戦処理（北→南の順序）は CK3 コミュニティの定番戦略
- 世代別ライフスタイル推奨は経験則ベース
- 常備軍の兵種推奨（ハスカール優先）はコミュニティで広く共有
