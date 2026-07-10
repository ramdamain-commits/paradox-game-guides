# EU5 ビザンツ帝国攻略ガイド（Patch 1.3 時点）

> ビザンツ帝国（Byzantine Empire）→ 瀕死の帝国を立て直し、ローマ復興（ROM タグ変形）を目指す序盤サバイバルから帝国再建までの整理。
> 2026-07-11 確認時点の最新パッチ 1.3 安定版（buildid 24075414 = 1.3.10）に合わせて更新。1.2「Echinades」（2026-05-06 リリース）baseline に 1.3 の変更点を統合済み。DLC「Fate of the Phoenix」の内容自体に変更はない。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。
> **本ガイドの主題**: stability -45 / gold -300 / アナトリア大半喪失という極限状態からの「瀕死帝国の逆転劇」。

---

## パッチ 1.2「Echinades」/ DLC Fate of the Phoenix 関連変更点

ガイドの前提が古くならないよう、先にパッチ差分と DLC 追加コンテンツを抜き出しておく。
**DLC Fate of the Phoenix はビザンツ帝国を主役にした最大規模の追加コンテンツ**であり、このガイドの大部分がその内容に依存する。

### パッチ 1.2「Echinades」主要変更（ビザンツ直接影響分）

#### Fate of the Phoenix DLC — ビザンツ専用新コンテンツ

| 変更 | 内容 | src |
|------|------|-----|
| Fate of the Phoenix ディザスター新規追加 | ビザンツ復興の中心メカニクス。ディザスター完了時に Restore Roman Borders CB が解禁 | `[src: disaster/D008_fate_of_the_phoenix.txt]` |
| Restore Roman Borders CB（ローマ国境回復 CB）新規 | `cb_restore_roman_borders`。攻者・守者ともに conquer_cost = 0.5、ticking_war_score = 0.5。バルカン・アナトリア・イタリア等広域が対象 | `[src: casus_belli/D008_restore_roman_borders.txt]` |
| Pronoia（プロノイア）新サブジェクト | BYZ 固有封臣制度。外交キャパ消費 0.75、strength_vs_overlord -0.50、manpower_modifier +0.10 | `[src: subject_types/D008_pronoia.txt]` |
| Katepanata（カテパナタ）政体 | BYZ 固有政府改革。統合速度 +10%、ディザスター完了後さらに +10%（計 +20%） | `[src: government_reforms/country_specific.txt]` |
| Cataphracts（カタフラクト）新ユニット | Age 1 は DLC なし可。Age 2 以降は DLC 必須 + latinization_vs_hellenization 条件。移動速度 -0.25、被強度ダメージ -0.25、士気ダメージ +0.33 | `[src: unit_types/D008_byzantine_unit_types.txt]` |
| Legionaries（レギオナリイ）新ユニット | DLC 必須 + ROM タグ。被強度・士気ダメージ -0.10/-0.10 | `[src: unit_types/D008_byzantine_unit_types.txt]` |
| Greek Fire Ships（ギリシャ火炎船） | DLC + `unlocked_greek_fire` 変数必須。cannons 12/15、強度ダメージ +0.20 | `[src: unit_types/D008_byzantine_unit_types.txt]` |
| Greek Fire Infantry（ギリシャ火炎歩兵） | DLC + `unlocked_greek_fire` 変数 + Age 2 以降。士気ダメージ +0.20、強度ダメージ +0.10 | `[src: unit_types/D008_byzantine_unit_types.txt]` |
| Varangians（ヴァリャーグ親衛隊） | DLC + BYZ タグ + Age 2 以降。max_strength 0.10（最大10%まで）、強度・士気ダメージ +0.20/+0.20。首都でのみ建設可 | `[src: unit_types/D008_byzantine_unit_types.txt]` |
| Latinization vs Hellenization（ラテン化 vs ヘレナイゼーション）Societal Value | BYZ 開始値 80（ヘレナイゼーション寄り）。Cataphracts Age 2・Legionaries の解放条件に関与 | `[src: events/government/D008_latinization_vs_hellenization.txt]` |
| byzantine_succession（ビザンツ継承）固有ルール | BYZ 専用後継者選定システム | `[src: common/disasters/byzantine_succession_crisis.txt]` |
| 失明・肢体切断刑罰インタラクション | 王朝政治の強力なツール。廷臣・継承候補者に使用可能 | `[src: common/character_interactions/d008_mutilations.txt]` |

#### 正教会オーバーホール（1.2 全般）

| 変更 | 内容 | src |
|------|------|-----|
| Rite Power 廃止 → Religious Influence 統合 | 旧来の正教メカニクスが刷新。ビザンツの宗教管理が変化 | `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Patriarch（総主教）キャラクター実装 | エキュメニカル総主教がキャラクターとして機能 | `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| 正教の最大 Religious Influence | 400（カトリックの 900 より大幅に低い） | `[src: religions/christian.txt]` |

#### バルカン地域大幅拡充

| 変更 | 内容 | src |
|------|------|-----|
| 新 Advances 300+、新 DHE 140+ | バルカン関連フレーバー大幅拡充。セルビア・ブルガリア・ヴァラキア情勢が動的化 | `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Latin Culture Movement（ラテン文化運動） | ヴェネツィア・ジェノヴァのバルカン進出が動的化 | `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |

#### 戦争・軍事変更（ビザンツへの影響）

| 変更 | 内容 | src |
|------|------|-----|
| Coalition War が Superiority War 化 | 連合軍が首都占領なしに Superiority Wargoal で勝利可能。ビザンツを支援する連合がオスマンを追い詰めやすくなった | `[src: Patch_1.2 wiki + script verified]` |
| Enforce Peace 双方合意必須 | 一方的な講和強制不可 | `[src: Patch_1.2 wiki + script verified]` |
| 要塞駐屯 Heavy Infantry のみ | 騎兵は要塞守備不可。カタフラクト（重騎兵）は要塞に入れない | `[src: Patch_1.2 wiki + script verified]` |
| ロジ距離 50→30 / 食料消費 10倍 | 補給線管理の徹底が必須。アナトリア遠征でも適用される | `[src: Patch_1.2 wiki + script verified]` |

#### Patch 1.3 主要変更（ビザンツ直接影響分）

1.3 は安定版（buildid 24075414 = 1.3.10）としてリリース済み。1.2「Echinades」baseline に統合した。

| 変更 | 内容 | src |
|------|------|-----|
| 反ジェノヴァ盟約（ヴェネツィアとの連携） | ビザンツ・ヴェネツィア間フレーバーで対ジェノヴァの連携イベントが追加。コンスタンティノープルのジェノヴァ商人勢力への対抗手段になる | `[src: events/DHE/flavor_byz_ven.txt]` |
| Born in the Purple（紫の間に生まれし者） | ビザンツの後継者選定・正統性に関わるメカニクスが整理された。皇位継承の安定性に影響 | `[src: heir_selections/monarchy.txt, events/culture/culture_greek.txt]` |
| 1337 開始国境の修正 | ビザンツ開始時の領土・国境設定が調整された（コミュニティ知見：公式パッチノート由来・スクリプト未確認） | — |
| ジェノヴァ弩兵 → 軽歩兵（兵科再分類） | エーゲ海・バルカン戦線で対峙するジェノヴァ系勢力の編成が変化（兵科の Heavy/Light 分類自体は 1.2 既存） | `[src: unit_types/1_uniques_for_age_2_renaissance.txt:68]` |
| 船コスト増（金 4倍・goods 10倍） | 海軍の建造・維持が大幅に高コスト化。エーゲ海・ボスポラス海峡の制海権確保コストが上昇し、序盤の海軍依存戦略が圧迫される（コミュニティ知見：公式パッチノート由来・スクリプト未確認） | — |
| 海戦致死性の上昇 | 海戦の損耗が増加。少数精鋭の艦隊を温存し不利な海戦を避ける運用が重要になる（コミュニティ知見：公式パッチノート由来・スクリプト未確認） | — |
| Twilight of the Tsardom（ツァーリ国の黄昏）ディザスター新規追加 | ブルガリア等バルカン勢力に崩壊・分裂を引き起こす。ビザンツにとっては北方バルカン再征服の好機 | `[src: disasters/twilight_of_the_tsardom.txt, events/DHE/flavor_BUL.txt]` |

個別の詳細・運用方針は本文各章（開始状況・序盤戦略・中盤戦略・後半戦略・用語表）に統合済み。

### ビザンツプレイヤーが特に注意すべき変更（破壊的）

- **DLC なしでも Cataphracts Age 1 は使用可能**: `country_byz.txt` のアドバンスで解放可能 `[src: unit_types/D008_byzantine_unit_types.txt]`（DLC なし版は age_1 のみ）
- **Pronoia サブジェクトは enable_pronoia_subject モディファイアが必要**: pronoia_system / komnenian_formalization / palaeologan_hereditary_transition / reformed_pronoia_system の各ポリシーから付与される `[src: subject_types/D008_pronoia.txt]`
- **Restore Roman Borders CB はディザスター完了が前提**: Fate of the Phoenix ディザスターのオプション選択後に解禁される `[src: disaster/D008_fate_of_the_phoenix.txt]`
- **Katepanata はディザスター完了でさらに強化**: 初期効果 +0.10 → 完了後 +0.20（integration_speed） `[src: government_reforms/country_specific.txt]`
- **正教の Religious Influence 上限 400 はカトリックの半分以下**: 宗教的影響力の蓄積が遅い。聖職者エステート管理に注意 `[src: religions/christian.txt]`

### 過去パッチ（参考）

**Patch 1.1「ロスバッハ」** — AI 攻撃性低下・統合軍備（Combined Arms）追加・召集軍民兵効率 +25%→+10% 下方・貴族召集軍 +20%→+50% 上方（戦闘効率 +25% は削除）。

**Patch 1.1.10（2026-03-17）** — 建造物レベル 0 残留バグ修正・召集軍の部隊貼り付きバグ修正。

---

## 開始状況（1337年）— 瀕死帝国の戦略環境

### 基本ステータス

| 項目 | 値 | src |
|------|-----|-----|
| 国家ランク | 帝国（Empire） | `[src: setup/start/10_countries.txt]` |
| 首都 | コンスタンティノープル（Constantinople） | `[src: setup/start/10_countries.txt]` |
| 技術レベル | L3 | `[src: setup/start/10_countries.txt]` |
| ルーラー | Andronikos III Palaiologos | `[src: setup/start/10_countries.txt]` |
| 初期 gold | -300（赤字スタート） | `[src: setup/start/10_countries.txt]` |
| 初期 stability | -45（最低水準） | `[src: setup/start/10_countries.txt]` |
| 初期 prestige | 20 | `[src: setup/start/10_countries.txt]` |
| 初期 war_exhaustion | 10 | `[src: setup/start/10_countries.txt]` |
| 難易度 | ⚠ 非推奨（上級者向け挑戦枠）（コミュニティ知見） | — |

これは EU5 全国家の中でも**最悪級の初期財政状態**である。金庫は赤字、安定度は底、戦争疲弊度は高く、アナトリアのほぼ全域をすでに失っている。ゲームを通じて最大の逆境からスタートする。

### Societal Values（社会価値観）

| 社会価値 | 初期値 | 意味 | src |
|----------|--------|------|-----|
| latinization_vs_hellenization（ラテン化 vs ヘレナイゼーション） | 80（ヘレナイゼーション寄り） | 80 寄りでギリシャ的。Cataphracts Age 2・Legionaries の解放条件に関与 | `[src: setup/start/10_countries.txt]` |
| traditionalist_vs_innovative（伝統主義 vs 革新主義） | -60（伝統主義寄り） | 伝統的な帝国統治。改革コストに影響 | `[src: setup/start/10_countries.txt]` |
| offensive_vs_defensive（攻勢 vs 守勢） | 50（均衡） | 初期は守勢と攻勢の中間 | `[src: setup/start/10_countries.txt]` |
| outward_vs_inward（外向き vs 内向き） | 70（外向き寄り） | 外交重視の姿勢。貿易・外交に有利 | `[src: setup/start/10_countries.txt]` |

### 初期政府改革・行政システム

| 項目 | 値 | src |
|------|-----|-----|
| 政府改革 | autocracy / theme_system / kritai_katholikoi / katepanata | `[src: setup/start/10_countries.txt]` |
| administrative_system | pronoia_system（プロノイア制） | `[src: setup/start/10_countries.txt]` |
| 後継者選定 | byzantine_succession（固有ビザンツ継承ルール） | `[src: setup/start/10_countries.txt]` |

**1.3 での継承安定性の整理**: Born in the Purple（紫の間に生まれし者）メカニクスが 1.3 で整理され、byzantine_succession と合わせて皇位継承の安定性に影響する `[src: heir_selections/monarchy.txt, events/culture/culture_greek.txt]`。次の後継者候補を確認する際は、この整理された継承ルールを踏まえて評価すること。

### 領土状況（1337年開始）

| 支配状況 | 地域 |
|----------|------|
| 完全支配 | ギリシャ中東部・マケドニア東部・トラキア西部・コンスタンティノープル周辺・ガリポリ・レスボス・レムノス |
| 征服占領（不安定） | テッサリア一帯 |
| コアのみ（他国支配下） | ロドス島・アルバニア海岸部・**アナトリア大部分**（イズニク・ブルサ・ベルガマ・スミルナ等） |

`[src: setup/start/10_countries.txt]`

**アナトリアのコア喪失が最大の問題点**。イズニク・ブルサ等の豊かな地域を奪還するには、オスマン（TUR）との直接対立が避けられない。しかし序盤の戦力では正面衝突は自殺行為に等しい。

**1.3 での 1337 開始国境の修正**: 1.3 でビザンツ開始時の領土・国境設定が調整された（コミュニティ知見：公式パッチノート由来・スクリプト未確認）。瀕死帝国の初期戦略環境が微変する可能性があるため、上表の支配状況は実機で最新版に合わせて確認すること。

### 周辺国との関係

| 国・勢力 | 関係 | 備考 |
|----------|------|------|
| オスマン（TUR） | 最大の脅威。アナトリアを占拠 | コアを持つが兵力が絶対的に劣る。早急に対決しない |
| セルビア（SER） | 潜在的同盟相手。バルカンで隣接 | オスマンの膨張を共同で抑制する利害が一致する |
| ハンガリー（HUN） | 強力な北方大国 | バルカン方面の防衛パートナーとして同盟価値が高い |
| ヴェネツィア（VEN） | 複雑な関係。エーゲ海で利益衝突 | 地中海貿易では競合するが、オスマン対抗で一時的に連携可能 |
| ジェノヴァ（GEN） | 交易パートナー、コンスタンティノープルの商人 | 距離感を保つ。干渉されると内政が複雑化する |
| ブルガリア（BUL） | 弱体化した隣国 | 吸収対象だが急ぎすぎると全方位的な敵を作る |
| セルジューク系小国 | アナトリアに割拠 | オスマンが大ベイリクと競合している間は間接的な恩恵がある |

**1.3 でのジェノヴァ勢力編成の変化**: ジェノヴァ弩兵が軽歩兵へ兵科再分類された `[src: unit_types/1_uniques_for_age_2_renaissance.txt:68]`（兵科の Heavy/Light 分類自体は 1.2 既存）。エーゲ海・バルカン戦線でジェノヴァ系勢力と対峙する際は、この編成変化を踏まえて敵の機動力・要塞駐屯可否を見積もること。

### 初期の強み・弱み

| 区分 | 内容 |
|------|------|
| 強み | Empire ランクからのスタート（外交容量・軍事資源が多い） |
| 強み | DLC 有りなら固有ユニット群（Cataphracts・Greek Fire・Varangians）が段階的に解放される |
| 強み | Restore Roman Borders CB（ローマ国境回復 CB）がディザスター完了後に解禁され、広域奪還が正当化される |
| 強み | Pronoia サブジェクト制度でバルカン再支配を低コストで進められる |
| 弱み | 初期財政 -300 gold・stability -45・war_exhaustion 10 という極限状態 `[src: setup/start/10_countries.txt]` |
| 弱み | アナトリア大部分をオスマンに占拠されており、コアがあっても奪還する余力がない |
| 弱み | 正教の Religious Influence 上限 400 はカトリックの 900 の半分以下 `[src: religions/christian.txt]` |
| 弱み | DLC なしでは固有ユニットの大半が使用不可 |

---

## Day 1（ポーズ解除直後）

ゲーム開始直後は財政と安定度の二重危機への対処が最優先。後手を踏むとオスマンの侵攻が始まる前に内部崩壊する。

### 即座にやること（優先順位順）

1. **財政の応急処置**: 維持費の高い部隊を確認し、現戦力で最低限の守備が保てるラインまで解散。gold -300 でゲームを続けると急速に赤字が拡大する
2. **stability 改善への手順確認**: stability -45 では建物建設・外交行動すべてに制約がかかる。安定度回復コストを確認し、資金確保と並行して最低 0 以上を目指す路線を引く
3. **戦争疲弊の低減**: war_exhaustion 10 は毎月の不満度に影響する。戦争をしていない間は自然低減するが、新たな戦争を始めるとさらに上がる。序盤は戦争を起こさない方針を原則とする
4. **セルビアかハンガリーへの同盟打診**: 最初の外交行動として、バルカンの有力国との同盟を最速で交渉する。孤立したままオスマンと向き合うのは不可能に近い
5. **初期軍の配置確認**: コンスタンティノープルとガリポリを最優先の防衛拠点として軍を配置。テッサリアの征服占領地は一時的に諦めてでも中核部を守る
6. **pronoia_system の確認**: 現在の administrative_system が pronoia_system であることを確認。Pronoia サブジェクトの`enable_pronoia_subject`モディファイアを受けているか確認する
7. **Katepanata の効果確認**: 初期政府改革に含まれる katepanata の統合速度 +0.10 ボーナスを確認。ディザスター完了でさらに強化される `[src: government_reforms/country_specific.txt]`
8. **ビザンツ継承の設定確認**: byzantine_succession の固有後継者選定ルールが機能していることを確認し、次の後継者候補の能力値をチェックする

### 初期の軍編成方針

Cataphracts（カタフラクト）は Cataphracts age_1 アドバンスを取得することで DLC なしでも解放可能 `[src: unit_types/D008_byzantine_unit_types.txt]`。
ただし序盤の gold -300 では新規徴募の余地はほぼない。

- **守備優先**: 首都と主要要塞の守備隊を最低限維持することを最優先とする
- **全面戦争は 1400 年まで厳禁**。ただし以下の条件を満たす限定的奪還戦のみ例外として検討可（→ 後述「奪還戦の注意点」）: 財政・安定度・war_exhaustion の三重苦が改善するまで新たな全面戦争を始めない（コミュニティ知見）
- **要塞守備は Heavy Infantry のみ**: Patch 1.2 で Light Cavalry は要塞駐屯不可 `[src: Patch_1.2 wiki + script verified]`。Cataphracts（重騎兵）は要塞に配置できない点に注意

---

## 序盤戦略（1337〜1400）：生存フェーズ

序盤の目標は**生き残ること**である。ローマ復興は遠い先の話だ。財政再建・安定度回復・同盟構築の三本柱を地道に進め、オスマンとの直接対立を1400年以降まで先送りにする。

### フェーズ 1: 財政・安定度の危機対処（1337〜1350）

**gold -300 からの脱出**が最初の壁。主な手段は以下の通り。

- **余剰部隊の解散**: 維持できない部隊を解散し月間支出を削減する。守備最小限の兵力に絞る
- **交易収入の確保**: コンスタンティノープルはエーゲ海交易の要衝。交易商人（Merchant）を適切に配置し、交易収入を最大化する。地中海貿易の海上ルートコストが Patch 1.2 で 1/10 に削減されており `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）、正しく運用すれば交易収入が増加しやすい
- **建造物の維持費確認**: 高コストの建造物を一時的に停止または売却することも検討する
- **stability 回復の優先**: 安定度が低いほど各種ペナルティが累積する。1度に全回復する必要はなく、まず -45 → -20 以上を目指す

**オスマンとの距離の取り方**:

1337年時点でオスマン（TUR）はアナトリアのベイリク群と競合している段階。「オスマンの台頭」シチュエーションが進行中であり、オスマン自身も統一に忙しい。この時期はビザンツに余裕がなく、またオスマンも手が空いていない。**双方が手を出せない安定的な均衡**がしばらく続くことが多い（コミュニティ知見）。

ただし 1360〜1380 年代にオスマンがバルカン方面へ進出し始める歴史的タイムラインに合わせて、AI もガリポリ方面への圧力を高めることがある。ガリポリ要塞の守備は手を抜かないこと。

### フェーズ 2: 同盟構築（1337〜1370）

**最優先同盟: ハンガリー（HUN）またはセルビア（SER）**

| 同盟候補 | 利点 | 欠点 |
|----------|------|------|
| ハンガリー（HUN） | 大国。オスマンの北方進出を牽制できる。軍事力が高い | ハンガリー自身の拡張目標がビザンツと被る場合がある |
| セルビア（SER） | バルカン隣国。地理的に連携しやすい。正教つながり | 自体が弱体で同盟の軍事効果が限定的な場合がある |
| ヴェネツィア（VEN） | 海軍力が高く制海権維持に有効 | 地中海の利益が競合。長期的には摩擦が起きやすい |

ハンガリーとの同盟が最も安定した選択肢。ハンガリー攻略の詳細は `eu5-hungary-guide.md` を参照。ハンガリーとセルビアを同時に同盟できるなら理想的だが、両国の関係が悪ければ片方しか取れない。

**ヴェネツィア・ジェノヴァとの距離感**:

ヴェネツィア（VEN）とジェノヴァ（GEN）はコンスタンティノープルに交易拠点を持つ勢力。Latin Culture Movement（ラテン文化運動）が発動すると、彼らのバルカン進出が動的化する `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）。

- ヴェネツィア: オスマン対抗の一時的パートナーとして使えるが、エーゲ海の覇権で最終的に衝突する
- ジェノヴァ: コンスタンティノープル内の商人コミュニティを抱える。短期的な交易協定が有効

**反ジェノヴァ盟約（1.3）**: ビザンツ・ヴェネツィア間フレーバーで、ジェノヴァに対抗する連携イベントが追加された `[src: events/DHE/flavor_byz_ven.txt]`。コンスタンティノープルのジェノヴァ商人勢力への対抗手段として、ヴェネツィアとの一時的連携を模索する際の選択肢が増えている。

**序盤の海軍運用と船コスト増（1.3）**: 船の建造・維持コストが金 4倍・goods 10倍に増加し（コミュニティ知見：公式パッチノート由来・スクリプト未確認）、序盤の海軍依存戦略が圧迫される。ヴェネツィア・ジェノヴァとの海軍力差を埋めようと序盤から艦隊を拡張する方針は財政負担が大きくなったため、コンスタンティノープル艦隊の最低限維持に絞り、本格的な制海権確保は財政再建後（中盤以降）に先送りするのが無難。

### フェーズ 3: オスマンの内紛を待つ（1370〜1400）

歴史的には 14 世紀末にオスマン内部で後継者争いが起きる。ゲーム内でも AI オスマンが内紛状態（Legitimacy 低下・継承危機等）に入ることがある。この機会を見計らって限定的な反撃を試みる余地が生まれる（コミュニティ知見）。

**オスマン内紛の見極め方**:
- オスマンの Legitimacy が低下している時期を狙う
- 複数の戦線でオスマンが戦っているとき、バルカン方面への圧力が下がる
- バイエジットの捕囚（歴史的には 1402 年のアンカラの戦い）等の歴史的イベントに対応する形で、AI オスマンが弱体化フェーズに入る場合がある（コミュニティ知見）

**序盤に奪還を検討すべき目標（優先度順）**:

**前提条件**: gold が月次黒字、war_exhaustion 5 以下、ハンガリーまたはセルビアと同盟済み。これらを満たさない限り全項目見送り。

1. テッサリア（征服占領地の正式化）: すでに占領中なので、条件が整えば統合できる
2. ブルガリアの弱体領域: オスマンと戦う前に背後を固める
3. アルバニア海岸部（コアあり）: 将来の Adriatic 出口として価値がある

**奪還戦の注意点**:
- テッサリアは占領中だが统合コストがかかる。財政黒字になってから整備する
- ブルガリア領域は他の周辺国が狙っている場合がある。ハンガリーと競合しないよう事前調整
- 戦争する場合でも、同時に 2 本以上の戦争を開かない（財政と人的資源が枯渇する）

**1400 年時点の目標**:
- gold: プラス収支（月間黒字）
- stability: 0 以上（理想は +1）
- war_exhaustion: 5 以下
- 同盟: ハンガリーまたはセルビアと締結済み
- テッサリア: 正式支配に
- pronoia_system: 廃止イベントの発火タイミングをある程度把握済み

これらが揃えば中盤フェーズへの移行準備が整う。

### 序盤の内政サイクル

生存フェーズでも内政は止まらない。以下の優先サイクルを回す:

1. **毎月の確認**: gold 残高・月間収支・war_exhaustion の推移
2. **安定度の段階回復**: -45 → -30 → -15 → 0 → +1 と段階的に上げる。一度に大量のリソースを使わない
3. **Advance の段階取得**: Cataphracts age_1 を優先して取得。軍事的な差別化を図る
4. **交易収入の最適化**: コンスタンティノープルを通る交易ルートの商人配置を見直す。Patch 1.2 の海上ルートコスト削減 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）を活用する
5. **外交評価の維持**: 同盟国との評価を高く保つ。贈り物や婚姻で関係を強化する

**正教の stability_cost 恩恵**:
正教は stability_cost -0.10 を持つ `[src: religions/christian.txt — 正教固有か共通かは未確認]`。これにより安定度回復のコストが 10% 安くなる。sequence -45 から回復する長い道のりで、この割引は積み重ねると大きな節約になる。

---

## 中盤戦略（1400〜1500）：復興開始

序盤を生き延びたなら、中盤は段階的な復興を進める時期。Pronoia サブジェクト網の構築と Fate of the Phoenix ディザスターの完了が中核目標。

### プロノイア制改革と Pronoia サブジェクト網

**pronoia_system（プロノイア制）の廃止**: 現在の administrative_system である pronoia_system は、1360〜1500 年の間に廃止イベントが発生し、代替ポリシーへの移行が促される `[src: events/DHE/flavor_BYZ.txt: L3690-3732]`（コミュニティ知見：スクリプト未確認）。

**廃止後に解禁される 3 つのポリシー**:

| ポリシー | 特徴 | 推奨度 |
|----------|------|--------|
| komnenian_formalization（コムネノス家式整備） | Pronoia サブジェクト向けに最適化 | ★★★（Pronoia 重視なら） |
| palaeologan_hereditary_transition（パレオロゴス家式世襲転換） | 継承安定重視。ROM 変形前のヘレナイゼーション維持に向く | ★★（継承重視なら） |
| reformed_pronoia_system（改革プロノイア制） | Pronoia と統治効率のバランス型 | ★★（バランス重視なら） |

`[src: events/DHE/flavor_BYZ.txt: L3690-3732]`（コミュニティ知見：スクリプト未確認）

いずれのポリシーも `enable_pronoia_subject = yes` モディファイアを付与し、Pronoia サブジェクトの使用を可能にする `[src: subject_types/D008_pronoia.txt]`。

### Pronoia サブジェクトの運用

Pronoia（プロノイア）は BYZ 固有の封臣制度 `[src: subject_types/D008_pronoia.txt]`。

**基本スペック**:

| 項目 | 値 | src |
|------|-----|-----|
| レベル | 3 | `[src: subject_types/D008_pronoia.txt]` |
| 外交キャパ消費 | 0.75 | `[src: subject_types/D008_pronoia.txt]` |
| 宗主国側 modifier | monthly_legitimacy +0.01、月次中央集権度低下 | `[src: subject_types/D008_pronoia.txt]` |
| 臣属国側 modifier | global_manpower_modifier +0.10 | `[src: subject_types/D008_pronoia.txt]` |
| strength_vs_overlord | -0.50（宗主国への反乱強度 -50%） | `[src: subject_types/D008_pronoia.txt]` |
| 支払い | scaled_gold 0.2 / scaled_sailors 0.1 / scaled_manpower 0.1 | `[src: subject_types/D008_pronoia.txt]` |
| 併合条件 | 20 年経過 + 関係 190 | `[src: subject_types/D008_pronoia.txt]` |

**可視条件**: BYZ タグを保有または保有歴あり、かつ `enable_pronoia_subject = yes` モディファイアが必要 `[src: subject_types/D008_pronoia.txt]`。

**運用戦略**:
- Pronoia サブジェクトは manpower_modifier +0.10 を臣属国に与えるため、人的資源の間接確保として機能する
- 宗主国側は monthly_legitimacy +0.01 を得る。複数の Pronoia を持つほど legitimacy 収入が増加する
- strength_vs_overlord -0.50 により、反乱されても力で押さえ込みやすい
- 20 年後に関係 190 で併合できるため、長期的には完全統合への路線として機能する
- バルカンの弱小勢力を Pronoia 化することで、外交キャパを節約しながら間接支配を確立できる

### Fate of the Phoenix ディザスター

ビザンツ中盤最大のイベント群 `[src: events/disaster/D008_fate_of_the_phoenix.txt]`。DLC「Fate of the Phoenix」が必須 `[src: disaster/D008_fate_of_the_phoenix.txt]`。

**ディザスターの意義**:
- 完了後に Restore Roman Borders CB（ローマ国境回復 CB）が解禁される
- Katepanata の統合速度ボーナスが +0.10 → +0.20 に強化される `[src: government_reforms/country_specific.txt]`

**ディザスター完了への準備**:
- 安定度・legitimacy の維持
- Societal Values の管理（特に latinization_vs_hellenization）
- 財政の安定

詳細は「固有イベント時系列」セクション参照。

### Latinization vs Hellenization の管理

BYZ 開始値 80（ヘレナイゼーション寄り）`[src: setup/start/10_countries.txt]`。

**推奨方針: ヘレナイゼーション寄りをキープ**

Cataphracts Age 2 以降および Legionaries の解放条件に latinization_vs_hellenization が関与する `[src: events/government/D008_latinization_vs_hellenization.txt]`。ヘレナイゼーション方向（高い値）を維持することで固有ユニットの段階的解放が可能になる。

ラテン化方向（低い値）に振れると固有ユニット解放の条件が変わる可能性があるため、特別な意図がない限りヘレナイゼーション寄りをキープするのが推奨される（コミュニティ知見）。

### バルカン再征服の段階的進行

Restore Roman Borders CB（ローマ国境回復 CB）の発動前に、隣接する弱小勢力を順番に吸収してバルカンの足場を固める。CB 範囲は scripted_geography `roman_borders_geography`（アナトリア・イタリア・イベリア等広域）`[src: casus_belli/D008_restore_roman_borders.txt]`。

**隣接条件があるため漸進的に進める**:

1. **コアのみ地域のレジティマシー確立**: アルバニア海岸部・ロドス島周辺から段階的に奪還
2. **バルカン内陸の整理**: ブルガリア・セルビアの弱体地域を Pronoia 化または征服
3. **1400〜1450 年のオスマン情勢把握**: オスマン内部の後継者争いや連合形成を観察し、隙を見て限定的攻勢
4. **ガリポリの死守**: ヨーロッパ側からアナトリアへの渡航点。ここを失うとアナトリア奪還が著しく困難になる

**Pronoia 化の優先対象**:
- エピロス・ペロポネソス半島の弱小ギリシャ系国家: 文化・宗教的に近く、統合抵抗が低い
- セルビア系の小侯国: 正教つながりで交渉しやすい
- 外交キャパ 0.75 の消費は複数 Pronoia を持つと累積するため、主要国との同盟を維持できる外交余力を確認してから増やす

**バルカン地域情勢の詳細は `eu5-regional-guide.md` を参照**。オスマンとの直接対立については `eu5-ottoman-guide.md` に相手側の視点がある。

**Twilight of the Tsardom（ツァーリ国の黄昏）— ブルガリア崩壊の機会（1.3）**: 1.3 で追加されたディザスター `[src: disasters/twilight_of_the_tsardom.txt, events/DHE/flavor_BUL.txt]`。ブルガリア（第二次ブルガリア帝国）等のバルカン勢力に崩壊・分裂を引き起こす。ビザンツにとっては**北方バルカンの再征服の好機**であり、ブルガリアが内紛・分裂で弱体化したタイミングで Restore Roman Borders CB や通常征服でバルカン領を回収しやすくなる `[src: disasters/twilight_of_the_tsardom.txt]`。詳細は[eu5-regional-guide.md](eu5-regional-guide.md)の「東欧（ポーランド・ハンガリー・ロシア・バルカン）」章を参照。

### Fate of the Phoenix ディザスター詳細

`[src: events/disaster/D008_fate_of_the_phoenix.txt]`

**ディザスターの進行フェーズ（コミュニティ知見：詳細はスクリプト未確認）**:

1. **ディザスター発火条件の確認**: BYZ タグ + DLC 有りで一定の条件を満たすと発火する
2. **危機の激化フェーズ**: 帝国の内外に様々な圧力が加わる。各種のネガティブイベントが連鎖する
3. **オプション選択**: ディザスターのクライマックスで重要な選択が行われる。この選択が Restore Roman Borders CB 解禁のトリガーになる
4. **ディザスター完了**: Katepanata 追加ボーナス獲得。CB 解禁。帝国再建フェーズへの移行

**ディザスター発火前の準備**:
- legitimacy を高く維持する（低い legitimacy は危機の激化を招く可能性がある）（コミュニティ知見）
- 安定度を 0 以上に保つ
- Societal Values（特に latinization_vs_hellenization）を管理しておく
- 主要な要塞の守備を整備し、内乱リスクに備える

---

## 後半戦略（1500〜1700）：ローマ復興

中盤の準備が整ったなら、後半は本格的なローマ復興フェーズ。Restore Roman Borders CB を使った大規模奪還戦と、ROM タグへの変形が目標。

### Restore Roman Borders CB の発動戦略

CB スペック `[src: casus_belli/D008_restore_roman_borders.txt]`:

| 項目 | 値 |
|------|-----|
| CB 名 | cb_restore_roman_borders |
| wargoal | superiority_restore_roman_borders |
| 攻者 conquer_cost | 0.5 |
| 守者 conquer_cost | 0.5 |
| ticking_war_score | 0.5 /月 |
| 対象範囲 | roman_borders_geography（バルカン・アナトリア・イタリア・イベリア・フランス・エジプト・イングランド諸州等広域） |

**発動の前提**:
- Fate of the Phoenix ディザスター完了 `[src: disaster/D008_fate_of_the_phoenix.txt]`
- DLC「Fate of the Phoenix」保有 `[src: disaster/D008_fate_of_the_phoenix.txt]`

**段階的奪還ロードマップ**:

1. **バルカン先行（1500〜1550）**: CB を使いバルカン残存領土の奪還。Pronoia 網で固める
2. **アナトリア進出（1550〜1620）**: オスマンの弱体化タイミングを見計らって北西アナトリアから奪還
3. **地中海方面（1620〜1700）**: イタリア・エジプト方面への拡張。CB 範囲が広大なため、長期的な戦略目標として設定する

**戦争の限界点管理**:
- conquer_cost が 0.5 と低いため、占領した領土を講和で取得しやすい
- ticking_war_score = 0.5 の時間スコアが蓄積するため、長期戦でも有利に進めやすい
- ただし food 消費 10 倍・ロジ距離 30 の制約 `[src: Patch_1.2 wiki + script verified]` を考慮した補給線設計が必須

### ROM タグへの変形

ROM（ローマ帝国）タグへの変形は、ビザンツプレイの最大の達成目標。

**変形条件**（wiki 由来のコミュニティ知見：スクリプト未確認）:
- BYZ が一定数のコア地域を奪還する
- pronoia_system からの移行後にポリシーが整備されている
- 1360〜1500 年の間に発生する 3 ポリシー解禁イベントが条件の一部とされる（コミュニティ知見：スクリプト未確認）

`[src: events/DHE/flavor_BYZ.txt]`（ROM 変形の正確な達成条件・効果はスクリプト未確認、コミュニティ知見）

**ROM 変形後の変化**:
- Legionaries ユニットが使用可能になる（ROM タグ + DLC 必須） `[src: unit_types/D008_byzantine_unit_types.txt]`
- 帝国としての正統性が強化される（コミュニティ知見：スクリプト未確認）

**ROM 変形のタイミング**:
バルカンとアナトリア北西部をある程度回復した段階で変形を狙う。変形後は Legionaries が使えるため、軍事的にも前後半で戦力が切り替わる節目になる（コミュニティ知見）。

### 後半の海軍戦略

制海権がローマ復興の鍵。エーゲ海・地中海の制海権を保持することで、バルカン側とアナトリア側の兵站を維持できる。

Greek Fire Ships（ギリシャ火炎船）は制海権確保の切り札 `[src: unit_types/D008_byzantine_unit_types.txt]`:

| ユニット種 | cannons 数 | 強度ダメージ修正 |
|----------|-----------|----------------|
| Renaissance Galley（ルネサンス）版 | 12 | +0.20 |
| Discovery Galley（大航海時代）版 | 15 | +0.20 |

Greek Fire Ships は `unlocked_greek_fire` 変数が必要 `[src: unit_types/D008_byzantine_unit_types.txt]`。解禁後はオスマン・ヴェネツィアいずれに対しても海上で優位に立てる。

**制海権の意義**:
- ボスポラス海峡の封鎖: オスマンのバルカン方面への増援を遮断できる
- エーゲ海の島嶼支配: レスボス・レムノスに加え、ロドス島方面への補給線確保
- 地中海東岸の貿易ルート維持: コンスタンティノープルの交易収入の根幹を守る

**海軍整備の優先順位**:

1. **コンスタンティノープル艦隊**: まず首都の海軍力を充実させる。ボスポラス封鎖が最初の目標
2. **Greek Fire Ships 解禁**: `unlocked_greek_fire` 変数解禁後、最優先で切り替える
3. **エーゲ海基地の整備**: ガリポリ・テッサロニキ等に海軍基地を展開し、全エーゲ海をカバー
4. **地中海西部への展開**: ローマ復興で西地中海まで拡大する場合は追加艦隊が必要

Patch 1.2 の海上ルートコスト 1/10 削減 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）により、制海権を持つことで交易収入が向上する効果も期待できる。

**船コスト増・海戦致死性の上昇（1.3）**: 1.3 で船の建造コストが金 4倍・goods 10倍に増加し、維持費も上昇した（コミュニティ知見：公式パッチノート由来・スクリプト未確認）。Greek Fire Ships を含む艦隊の新規建造・更新が大幅に高コスト化するため、後半戦でも艦隊規模の拡張は慎重に計画する必要がある。あわせて海戦の致死性が上昇しており（コミュニティ知見：公式パッチノート由来・スクリプト未確認）、少数精鋭の Greek Fire Ships を温存し、不利な海戦を避ける運用がより重要になる。制海権確保コストの上昇は序盤（フェーズ 2「同盟構築」）から続く傾向であり、後半に入ってからも艦隊は数より質（Greek Fire Ships 優先）で維持するのが得策。

### 後半の大陸戦略

**バルカン安定化（1500〜1550）**:
Restore Roman Borders CB を使いながら、まずバルカンを完全掌握する。Pronoia サブジェクト網が整っていれば、征服後の統合が早い（Katepanata の integration_speed +0.20 が有効になる）。バルカン安定化後は tax base が十分に育ち、アナトリア遠征の資金基盤が整う。

**アナトリア奪還（1550〜1620）**:
アナトリア北西部（イズニク・ブルサ周辺）から始める。オスマンが多方面戦争中の隙を狙う。補給線の長さに注意——ロジ距離 30・食料消費 10 倍 `[src: Patch_1.2 wiki + script verified]` のため、補給基地を設置してから進軍する。

**ROM タグ変形後のビジョン**:
ROM 変形後は Legionaries が使えるようになり、軍事的にも新たな段階に入る。Legionaries（被強度・士気ダメージ -0.10/-0.10）`[src: unit_types/D008_byzantine_unit_types.txt]` を主力にした防御型重歩兵軍団で、バルカン・アナトリアの要塞線を堅固に保持しながら漸進的に拡大する。

---

## 軍事ドクトリン — Cataphracts / Greek Fire / Varangians / Legionaries

DLC「Fate of the Phoenix」が提供するビザンツ固有ユニット群は、歴史的モチーフと戦術的ニッチを組み合わせている。適切に使い分けることで、数的劣勢でも戦えるユニーク軍団が完成する。

### Cataphracts（カタフラクト）—— 重騎兵の柱

スクリプト検証済みスペック `[src: unit_types/D008_byzantine_unit_types.txt]`:

| 項目 | 値 |
|------|-----|
| ベース | heavy cavalry の copy from |
| 移動速度修正 | -0.25（通常の重騎兵より遅い） |
| 被強度ダメージ修正 | -0.25（非常に高い生存性） |
| 士気ダメージ修正 | +0.33（士気攻撃が強力） |
| 地形ペナルティ | 湿地・丘・山岳に地形ペナルティあり |
| build_time_modifier（Age 2 以降） | +0.50（建設時間 +50%） |

**Age 別解放条件**:

| Age | DLC 要件 | その他条件 |
|-----|----------|-----------|
| Age 1 | 不要 | country_byz.txt アドバンスで解放 |
| Age 2〜6 | DLC 必須 | `latinization_vs_hellenization` 条件 |

`[src: unit_types/D008_byzantine_unit_types.txt]`

**運用方針**:
- 被ダメージ -0.25 は極めて高い生存率を意味する。正面会戦の中核として配置
- 士気ダメージ +0.33 により、敵の戦闘意欲を素早く崩壊させられる
- 移動速度 -0.25 により機動戦は苦手。平原での正面会戦を中心に使う
- 湿地・丘・山岳では能力が落ちるため、地形を選んで投入する
- 要塞駐屯は不可（Patch 1.2 で Heavy Infantry のみ駐屯可 `[src: Patch_1.2 wiki + script verified]`）

### Greek Fire Infantry（ギリシャ火炎歩兵）—— 攻撃的歩兵

スクリプト検証済みスペック `[src: unit_types/D008_byzantine_unit_types.txt]`:

| 項目 | 値 |
|------|-----|
| DLC 要件 | DLC 必須 + `unlocked_greek_fire` 変数 |
| 解放条件 | Age 2（Renaissance）以降 |
| initiative | -1（先手が遅い） |
| 士気ダメージ修正 | +0.20 |
| 強度ダメージ修正 | +0.10 |

**運用方針**:
- initiative -1 のため先手が遅いが、ダメージが高い。後手から反撃する戦闘スタイルに向く
- Cataphracts と組み合わせると、歩兵が火で道を開き騎兵が士気崩壊した敵を追撃するパターンが強力（コミュニティ知見）
- `unlocked_greek_fire` 変数の解禁が前提。固有ディザスター・イベントチェーンとの連動を確認する

### Greek Fire Ships（ギリシャ火炎船）—— 制海権の要

スクリプト検証済みスペック `[src: unit_types/D008_byzantine_unit_types.txt]`:

| 世代 | cannons 数 | 強度ダメージ修正 |
|------|-----------|----------------|
| Renaissance Galley | 12 | +0.20 |
| Discovery Galley | 15 | +0.20 |

必要条件: DLC + `unlocked_greek_fire` 変数 `[src: unit_types/D008_byzantine_unit_types.txt]`。

**運用方針**:
- 制海権維持が最優先用途。エーゲ海・ボスポラス海峡の封鎖でオスマンの欧州進出を遅らせられる
- cannons 数が高く、海戦での射撃戦に強い
- 強度ダメージ +0.20 で敵艦の沈没速度が上がる
- 海軍中心戦略を選択した場合、これが最強の切り札になる

### Varangians（ヴァリャーグ親衛隊）—— 首都の守護者

スクリプト検証済みスペック `[src: unit_types/D008_byzantine_unit_types.txt]`:

| 項目 | 値 |
|------|-----|
| DLC 要件 | DLC 必須 + BYZ タグ |
| 解放条件 | Age 2〜6 |
| max_strength | 0.10（最大 10% まで） |
| 強度ダメージ修正 | +0.20 |
| 士気ダメージ修正 | +0.20 |
| 建設場所制限 | **首都のみ** |

**運用方針**:
- 首都コンスタンティノープルでのみ建設可能。コンスタンティノープルを守る特権部隊
- max_strength 0.10 のためユニット数は少ないが、強度・士気ダメージが高い精鋭
- 首都防衛が最大の役割。コンスタンティノープルを奪われないための最後の盾として機能する
- 首都に常駐配置し、包囲戦に備える

### Legionaries（レギオナリイ）—— ROM 変形後の主力

スクリプト検証済みスペック `[src: unit_types/D008_byzantine_unit_types.txt]`:

| 項目 | 値 |
|------|-----|
| DLC 要件 | DLC 必須 |
| タグ条件 | ROM タグ必須 |
| Hellenization 閾値条件 | `latinization_vs_hellenization` 必要 |
| 段階 | 6 段階 |
| 被強度ダメージ修正 | -0.10 |
| 被士気ダメージ修正 | -0.10 |
| initiative | -1 |
| combat_speed | -1 |

**運用方針**:
- ROM タグ変形後に解放されるため、後半戦の主力歩兵
- 被ダメージ -0.10/-0.10 により高い耐久性。正面の消耗戦で強い
- initiative -1・combat_speed -1 で機動性は低い。防衛線を張る戦い方が合う
- Greek Fire Infantry と組み合わせると、耐久型（Legionaries）+ 攻撃型（Greek Fire Infantry）の相互補完ができる（コミュニティ知見）

### ビザンツ軍の推奨編成（時期別）

| 時期 | 推奨編成 | 備考 |
|------|----------|------|
| 序盤（1337〜1400） | 汎用 Heavy Infantry + Cataphracts Age 1 少数 | 財政制約で大規模徴募は不可 |
| 中盤（1400〜1500） | Cataphracts Age 2+ / Greek Fire Infantry / 汎用歩兵 | ユニット解放後は段階的に切り替え |
| 後半（1500〜） | Legionaries / Cataphracts / Greek Fire Infantry / Greek Fire Ships | ROM 変形後に Legionaries を主力に |
| 海軍 | Greek Fire Ships を主力に、汎用ガレー船で補完 | 制海権確保が最優先 |

**統合軍備（Combined Arms）ボーナス**:
歩兵（Greek Fire Infantry / Legionaries）+ 騎兵（Cataphracts）+ 砲兵の三兵科混成で統合軍備ボーナスが発生。Patch 1.1 で追加されたこのボーナスをビザンツ軍でも活用する `[src: コミュニティ知見・スクリプト未確認]`。

### 兵科別の地形適性

ビザンツ固有ユニットは地形の影響を強く受ける。バルカン・アナトリアの地形に合わせた運用が鍵。

| 地形 | Cataphracts | Greek Fire Infantry | Legionaries | Varangians |
|------|-------------|---------------------|-------------|-----------|
| 平原 | ★★★（最強） | ★★ | ★★★ | — |
| 丘陵 | ★（ペナルティあり） | ★★ | ★★ | — |
| 山岳 | ★（ペナルティあり） | ★★ | ★★ | — |
| 湿地 | ★（ペナルティあり） | ★★ | ★★ | — |
| 要塞（駐屯） | ✕（Heavy Cavalry 不可） | ★★ | ★★★ | 首都のみ |

`[src: unit_types/D008_byzantine_unit_types.txt]`（地形ペナルティ詳細）

Cataphracts の地形ペナルティは `[src: unit_types/D008_byzantine_unit_types.txt]` に記載（湿地・丘・山岳に適用）。バルカンの丘陵地帯での戦いでは、Cataphracts を後方待機させ歩兵主体の戦闘を優先することがある。

### 傭兵の活用

ビザンツは固有ユニットが充実するまでの間、財政に余裕があれば傭兵で兵力を補完できる。
Patch 1.2 で傭兵コストが +25% 上昇した `[src: Patch_1.2 wiki + script verified]` ため、傭兵の多用は財政を圧迫する。

- 序盤: 財政が厳しい間は傭兵を避け、最小限の正規軍で運用
- 中盤: 重要な攻勢時に短期的な傭兵雇用で数的優位を確保。戦争終了後は即解散
- 後半: 固有ユニットが揃えば傭兵依存度を下げられる

傭兵は維持費が高いため、戦争中以外は雇用しないことを原則とする（コミュニティ知見）。

---

## 外交・同盟

### 序盤（1337〜1400）の優先関係

| 国・勢力 | 推奨 | 理由 |
|----------|------|------|
| ハンガリー（HUN） | **最優先同盟** | 強大な北方大国。オスマン牽制の主力 |
| セルビア（SER） | 同盟検討 | バルカン隣国。正教つながり。軍事力は HUN より劣る |
| ヴェネツィア（VEN） | 慎重に接触 | 海軍力を借りたいが、地中海利益で競合 |
| ブルガリア（BUL） | 将来の征服 / Pronoia 化対象 | 弱体化しているが急ぎすぎると摩擦 |
| ジェノヴァ（GEN） | 交易協定のみ | 内政干渉を避けつつ交易ルートは維持 |
| オスマン（TUR） | 戦争回避。静観 | 序盤は圧倒的に不利。1400 年以降まで軍事対立を避ける |

### 中盤（1400〜1500）の外交転換

**オスマン対抗連合の形成を模索**:

オスマンが強大化してくる中盤では、単独での対決を避け連合を組む。Patch 1.2 の Coalition War が Superiority War 化したことで `[src: Patch_1.2 wiki + script verified]`、連合がビザンツ側についた場合にオスマンへの圧力が増す。

- ハンガリー・ポーランド・モルダヴィアとの北方連携
- セルビアが弱体化した場合、Pronoia 化して事実上の臣属国に
- ヴェネツィアとの一時的な反オスマン連携（長期では競合するが短期的には有効）

**Belligerent（好戦性）の管理**:

Restore Roman Borders CB（ローマ国境回復 CB）を多用すると Belligerent が蓄積しやすい。
Coalition War が Superiority War 化し、首都占領なしに連合が勝利できるようになった `[src: Patch_1.2 wiki + script verified]`。
高い Belligerent は連合結成→優位性戦争による敗北リスクとなる。Belligerent は定期的に Conciliatory（融和的）行動で解消することを推奨する（コミュニティ知見）。

**外交コストの計算**:
- Pronoia サブジェクトを増やすほど外交キャパが減少（0.75/体）
- 同盟維持にも外交リソースが必要
- CB の多用は外交評価にも影響する可能性がある（コミュニティ知見）
- 外交官の数は帝国ランクで多めに確保されている。有効活用する

**Claim Throne CB の制限**:
Patch 1.2 で請求者が既に対象国を統治中なら CB が不発になった `[src: Patch_1.2 wiki + script verified]`。ビザンツは Restore Roman Borders CB を主要な開戦事由とするため、この制限は直接影響しないが、補助的な CB 戦略には注意が必要。

### 後半（1500〜）の大国外交

ROM タグへの変形後は、「ローマ帝国」としての正統性外交が可能になる。

- イタリア半島の諸国との外交: ローマ帝位の正統性を主張できる（コミュニティ知見：スクリプト未確認）
- 教皇（Papacy）との関係: 正教国であるためカトリックとの関係は構造的に難しいが、ローマという象徴的な文脈でつながりを持てる可能性（コミュニティ知見：スクリプト未確認）
- オスマン（TUR）との最終決戦: アナトリア奪還に向けた本格的な対決。`eu5-ottoman-guide.md` にオスマン側の防衛戦略があり、参照することで相手の行動を予測しやすくなる

---

## 内政・経済 — Pronoia 運用 / Katepanata / 正教

### 正教（Orthodox）の管理

正教の詳細メカニクスは `eu5-religion-guide.md` を参照。ここではビザンツ固有の注意点を記載する。

| 項目 | 値 | src |
|------|-----|-----|
| 最大 Religious Influence | 400 | `[src: religions/christian.txt]` |
| stability_cost | -0.10 | `[src: religions/christian.txt]` |
| global_max_literacy | +5 | `[src: religions/christian.txt]` |
| 聖職者結婚 | 不可 | `[src: religions/christian.txt]` |

**正教の課題**:
- Religious Influence 上限 400 はカトリックの 900 の半分以下 `[src: religions/christian.txt]`。宗教的影響力の蓄積が遅いため、宗教的な外交・改宗活動に制約がある
- 1.2 で Patriarch（総主教）がキャラクターとして実装された `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）。エキュメニカル総主教との関係管理が必要になる可能性がある

**stability_cost -0.10 の恩恵**:
- 安定度回復コストが 10% 低減される
- 序盤の stability -45 からの回復に直接的に有効

### Katepanata（カテパナタ）政体の活用

Katepanata は BYZ 固有の政府改革 `[src: government_reforms/country_specific.txt]`:

| フェーズ | integration_speed ボーナス |
|----------|--------------------------|
| 通常時 | +0.10（global_integration_speed_modifier） |
| Fate of the Phoenix ディザスター完了後 | +0.20（追加 +0.10） |

**その他のボーナス**:
- 月次中央集権度低下
- 月次防御寄り（offensive_vs_defensive に影響）
- 政府改革スロット +1

`[src: government_reforms/country_specific.txt]`

**運用戦略**:
- ディザスター完了前から integration_speed +0.10 が機能している
- Pronoia サブジェクトの 20 年後併合をこのボーナスで加速できる
- ディザスター完了を急ぐ理由の一つが、Katepanata の強化にある

### 経済管理の優先順位

| 優先度 | 項目 | 理由 |
|--------|------|------|
| ★★★ | コンスタンティノープルの交易収入 | 序盤の主要収入源。エーゲ海交易の要衝 |
| ★★★ | 安定度の維持（0 以上） | stability -45 からの回復が最優先 |
| ★★ | Pronoia 支払いの受取（scaled_gold 0.2） | 複数 Pronoia で収入が積み上がる |
| ★★ | 建造物の整備 | コンスタンティノープル・テッサロニキ等の主要都市から |
| ★ | 軍事力の増強 | 財政が安定してから。序盤の過剰投資は禁物 |

**政府効率の数値詳細は `eu5-government-guide.md` を参照**。軍事ドクトリンの詳細数値は `eu5-universal-guide.md` を参照。

### 階級（Estate）管理

ビザンツは帝国という性質上、複数の階級を抱える。

| 階級 | 管理のポイント | 優先度 |
|------|-------------|--------|
| 聖職者（Clergy） | 正教会の宗教的影響力管理。Patriarch との関係 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） | ★★★ |
| 貴族（Nobility） | 召集軍の供給源。特権は慎重に与える | ★★ |
| 市民（Burghers） | コンスタンティノープルの交易収入に関連。商人の供給 | ★★ |

**聖職者（Clergy）のポイント**:
正教の maximum_religious_influence が 400 `[src: religions/christian.txt]` と低いため、聖職者エステートの宗教的影響力管理が重要。聖職者の満足度が低いと宗教的影響力の回復が遅れる可能性がある（コミュニティ知見）。

**貴族（Nobility）の管理**:
Pronoia サブジェクト制度は元々封建的な土地割当制度に由来する。ゲーム内でも貴族との関係が Pronoia 運用に影響する可能性がある（コミュニティ知見：スクリプト未確認）。

### 建造物の整備優先順位

| 建造物 | 場所 | 優先度 | 理由 |
|--------|------|--------|------|
| 正教会修道院（Orthodox Monastery） | 主要都市 | ★★★ | 改宗速度 +0.1、聖職者識字率 +10 `[src: eu5-religion-guide.md]` |
| 海軍系建造物 | コンスタンティノープル・ガリポリ | ★★★ | 制海権維持の基盤 |
| 要塞強化 | コンスタンティノープル・テッサロニキ | ★★★ | オスマン・ブルガリア方面への防衛線 |
| 交易系建造物 | コンスタンティノープル | ★★ | 主要交易ノードの収入最大化 |
| 徴兵施設 | 主要地域 | ★★ | 人的資源の充実。Pronoia manpower と合わせて活用 |

---

## 固有イベント時系列

### 序盤（1337〜1400）

| ID | イベント名 | 発火条件 | 推奨選択 | 効果 |
|----|----------|---------|---------|------|
| flavor_BYZ 系 | ビザンツ固有フレーバー（通常版） | 様々 | 状況次第 | 帝国の日常的な政治イベント |
| D008_flavor_BYZ 系 | DLC 追加フレーバー（DLC ゲート付き） | DLC 有り | 状況次第 | DLC 固有コンテンツ |
| byzantine_succession_crisis | ビザンツ継承危機 | 後継者問題発生時 | 事前に継承候補を整理しておく | 内乱リスク・継承権問題 |
| d008_mutilations 系 | 失明・肢体切断インタラクション | DLC + BYZ タグ | 慎重に使用 | 政敵の政治的中立化。やり過ぎると legitimacy 低下（コミュニティ知見） |

`[src: events/DHE/flavor_BYZ.txt]` / `[src: events/DHE/D008_flavor_BYZ.txt]`

### 中盤（1400〜1500）

| ID | イベント名 | 発火条件 | 推奨選択 | 効果 |
|----|----------|---------|---------|------|
| flavor_BYZ.L3690-3732 | pronoia_system 廃止イベント | 1360〜1500 年 | komnenian_formalization 推奨（Pronoia 重視） | 3 ポリシーから選択して Pronoia サブジェクト解禁 |
| D008_fate_of_the_phoenix 系 | Fate of the Phoenix ディザスター | DLC + BYZ | オプション選択でディザスター完了を目指す | Restore Roman Borders CB 解禁・Katepanata 強化 |
| D008_latinization_vs_hellenization 系 | ラテン化 vs ヘレナイゼーション | 文化揺り戻し | ヘレナイゼーション寄りを維持 | Cataphracts Age 2 / Legionaries 解放条件 |

`[src: events/DHE/flavor_BYZ.txt: L3690-3732]`（コミュニティ知見：スクリプト未確認）
`[src: events/disaster/D008_fate_of_the_phoenix.txt]`
`[src: events/government/D008_latinization_vs_hellenization.txt]`

### 後半（1500〜）

| ID | イベント名 | 発火条件 | 推奨選択 | 効果 |
|----|----------|---------|---------|------|
| ROM 変形イベント | ROM タグへの変形 | 奪還条件達成 | 変形実行 | Legionaries 解放・帝国正統性強化 |
| ギリシャ火発見 | `unlocked_greek_fire` 付与 | イベントまたはアドバンス | 必ず取得 | Greek Fire Ships / Infantry 解放 |

（ROM 変形の詳細はスクリプト未確認。コミュニティ知見）

### ビザンツ継承危機（`byzantine_succession_crisis`）

`[src: common/disasters/byzantine_succession_crisis.txt]`

ビザンツ固有の継承危機ディザスター。以下の状況で発火しやすい:
- 複数の有力後継者候補が存在する
- legitimacy が低下している
- 宮廷政治の派閥対立が高まっている

**対処法**:
- d008_mutilations（失明・肢体切断インタラクション）`[src: common/character_interactions/d008_mutilations.txt]` を使って政治的ライバルを事前に無力化する
- legitimacy を高く維持する
- byzantine_succession（固有継承ルール）に従い、最も能力の高い後継者を選定する

---

## 固有アドバンス（Advance）

### 伝統の時代（Age 1）

| アドバンス名 | 効果 | 取得優先度 | 備考 |
|-------------|------|-----------|------|
| Cataphracts age_1 | Cataphracts（DLC なし可）解放 | ★★★ | DLC なしでも利用できる唯一の固有重騎兵 |

`[src: common/advances/country_byz.txt]`

### ルネサンスの時代（Age 2）

| アドバンス名 | 効果 | 取得優先度 | 備考 |
|-------------|------|-----------|------|
| Cataphracts age_2 | DLC + ヘレナイゼーション条件が必要。建設時間 +50% | ★★★（DLC 有り） | `[src: unit_types/D008_byzantine_unit_types.txt]` |
| Greek Fire 関連 | `unlocked_greek_fire` 解放への道 | ★★★（DLC 有り） | Greek Fire Ships / Infantry 使用への前提 |
| Varangians | 首都に Varangian 親衛隊配置可能に | ★★（DLC 有り） | 首都防衛専用 |

### 大航海の時代（Age 3）〜以降

| アドバンス名 | 効果 | 取得優先度 | 備考 |
|-------------|------|-----------|------|
| Cataphracts age_3〜6 | 段階的強化。各 Age で DLC + ヘレナイゼーション必要 | ★★★ | 継続取得を優先 |
| ROM 変形関連 | ROM タグへの変形を可能にする | ★★★（ROM 目標の場合） | Legionaries 解放のための必須条件 |
| Byzantine 固有進歩（bureaucracies） | ビザンツ固有官僚制アドバンス | ★★ | `[src: common/bureaucracies/byz.txt]` |

`[src: common/advances/country_byz.txt]`
`[src: common/bureaucracies/byz.txt]`

**取得優先度の指針**:
- **DLC 有り**: Cataphracts age_1 → Greek Fire 解禁 → Cataphracts age_2 → Varangians の順が基本
- **DLC なし**: Cataphracts age_1 のみ取得可能。他は汎用アドバンスで補う

### アドバンス取得ロードマップ（全体）

| 時期 | 推奨アドバンス | 理由 |
|------|-------------|------|
| 序盤（Age 1） | Cataphracts age_1 | DLC 不要。即座に差別化できる唯一の固有ユニット |
| 中盤前半（Age 2） | Cataphracts age_2（DLC）/ Varangians（DLC）/ Greek Fire 前提（DLC） | DLC コンテンツの段階的解放 |
| 中盤後半（Age 3） | Greek Fire 解禁 / Cataphracts age_3 | Greek Fire Ships / Infantry を解禁し海・陸の固有戦力を充実 |
| 後半（Age 4〜6） | Cataphracts 継続 / ROM 変形条件 / Legionaries 解放 | 最終戦力への移行 |

アドバンスは時代（Age）で解禁されるため、時代が進むにつれて選択肢が増える。各時代で汎用アドバンスとの優先度を比較し、固有アドバンスを過度に優先して汎用ボーナスを取り逃がさないよう注意する（コミュニティ知見）。

### DLC なしのビザンツプレイ

DLC「Fate of the Phoenix」なしの場合、利用できる固有コンテンツは大幅に制限される。

**DLC なしで利用可能なもの**:
- Cataphracts age_1（country_byz.txt のアドバンスで解放） `[src: unit_types/D008_byzantine_unit_types.txt]`
- 通常の BYZ フレーバーイベント（`flavor_BYZ.txt`）`[src: events/DHE/flavor_BYZ.txt]`
- Byzantine Succession Crisis（`byzantine_succession_crisis.txt`）`[src: common/disasters/byzantine_succession_crisis.txt]`

**DLC なしで利用できないもの**:
- Cataphracts age_2〜6
- Greek Fire Ships / Greek Fire Infantry
- Varangians
- Legionaries
- Pronoia サブジェクト（enable_pronoia_subject を付与するポリシーが DLC ゲート付き）
- Restore Roman Borders CB（Fate of the Phoenix ディザスターが DLC ゲート付き）
- D008_flavor_BYZ.txt の DLC 追加イベント群
- 失明・肢体切断インタラクション

DLC なしでは Cataphracts age_1 を活かした限定的な固有軍事戦略に留まり、ローマ復興（ROM タグ変形）も実質的に達成できない難易度になる（コミュニティ知見）。

---

## よくある失敗パターン

### ビザンツ固有の失敗

- **序盤に無理やり戦争を始める**: gold -300・stability -45 の状態で戦争を始めると即崩壊する。1400 年まで防衛専念が鉄則（コミュニティ知見）
- **同盟なしでオスマンと向き合う**: ハンガリーかセルビアとの同盟締結前にオスマンと衝突すると、軍事的にも外交的にも詰む（コミュニティ知見）
- **コンスタンティノープルの交易収入を放置**: 序盤の主要収入源。商人の配置とルートを最適化しないと財政回復が遅れる
- **Cataphracts を要塞に配置する**: Patch 1.2 で Heavy Infantry のみ要塞駐屯可能 `[src: Patch_1.2 wiki + script verified]`。Cataphracts は重騎兵であり要塞守備に使えない
- **ヘレナイゼーション寄りを維持しない**: Cataphracts Age 2 以降と Legionaries の解放条件。ラテン化方向に振れると固有ユニットが使えなくなる `[src: events/government/D008_latinization_vs_hellenization.txt]`
- **pronoia_system 廃止を準備なしに迎える**: 廃止イベントまでに 3 ポリシーの選択肢を理解しておく。突然の廃止で混乱しないよう事前準備が必要（コミュニティ知見）
- **Fate of the Phoenix ディザスターを放置する**: ディザスター完了なしには Restore Roman Borders CB が解禁されない。Katepanata の追加ボーナスも得られない `[src: disaster/D008_fate_of_the_phoenix.txt]`
- **`unlocked_greek_fire` 変数の解禁を後回しにする**: Greek Fire Ships と Greek Fire Infantry の前提条件。DLC 有りプレイでは早めに解禁を進める `[src: unit_types/D008_byzantine_unit_types.txt]`
- **Varangian 親衛隊を首都以外に配置しようとする**: 首都（コンスタンティノープル）でのみ建設・配置可能 `[src: unit_types/D008_byzantine_unit_types.txt]`
- **ビザンツ継承危機を軽視する**: `byzantine_succession_crisis` は適切に処理しないと内乱リスクが跳ね上がる。失明・肢体切断インタラクションを事前に使って政敵を無力化しておく `[src: common/disasters/byzantine_succession_crisis.txt]`
- **Restore Roman Borders CB の隣接条件を無視して広域に使う**: CB 範囲は広大だが、実際の征服には隣接条件がある。バルカン → アナトリアの順に漸進的に進める（コミュニティ知見）

### EU5 全般の失敗（ビザンツで特に顕著）

- **補給線を軽視した遠征**: Patch 1.2 でロジ距離 30・食料消費 10 倍 `[src: Patch_1.2 wiki + script verified]`。アナトリア奪還戦は補給線が非常に伸びる。中間補給基地なしに大軍を送ると壊滅的損耗
- **Coalition War Superiority 化を無視する**: Belligerent が高い状態でビザンツが連合を組まれると、首都占領なしに敗北する `[src: Patch_1.2 wiki + script verified]`
- **Enforce Peace の変更を忘れる**: 一方的講和強制が不可能になった `[src: Patch_1.2 wiki + script verified]`。戦争の終わらせ方を計画的に考える必要がある
- **召集軍を常備軍として維持し続ける**: 維持費が高い。必要な戦争が終わったら即解散

---

## 用語表（1.2 / DLC 用語の和英対照）

> 完全版は [`localization-reference.md`](./localization-reference.md) を参照。

### ビザンツ固有用語

| 日本語 | 英語 | カテゴリ | 備考 |
|--------|------|---------|------|
| カタフラクト | Cataphracts | ユニット | ビザンツ重騎兵。被強度ダメージ -0.25・士気ダメージ +0.33 |
| ギリシャ火炎船 | Greek Fire Ships | 海軍ユニット | cannons 12/15、強度ダメージ +0.20 |
| ギリシャ火炎歩兵 | Greek Fire Infantry | 陸軍ユニット | 士気ダメージ +0.20・強度ダメージ +0.10 |
| ヴァリャーグ親衛隊 | Varangians | ユニット | 首都のみ建設可。強度・士気ダメージ +0.20 |
| レギオナリイ | Legionaries | ユニット | ROM タグ解放後使用可。被強度・士気ダメージ -0.10 |
| プロノイア | Pronoia | サブジェクト | BYZ 固有封臣。外交キャパ 0.75、manpower +0.10 |
| カテパナタ | Katepanata | 政体 | BYZ 固有政体。統合速度 +0.10（完了後 +0.20） |
| ビザンツ継承 | Byzantine Succession | 継承システム | 固有後継者選定ルール |
| ローマ国境回復 CB | Restore Roman Borders CB | 開戦事由 | ディザスター完了後解禁。conquer_cost 0.5 |
| ヘレナイゼーション | Hellenization | Societal Value | latinization_vs_hellenization の高値側 |
| ラテン化 | Latinization | Societal Value | latinization_vs_hellenization の低値側 |
| ラテン文化運動 | Latin Culture Movement | イベント | ヴェネツィア・ジェノヴァのバルカン介入（コミュニティ知見：スクリプト未確認） |
| ビザンツ継承危機 | Byzantine Succession Crisis | ディザスター | 継承問題が内乱リスクになる |
| 失明・肢体切断 | Mutilations | キャラクターインタラクション | DLC 専用の政治的無力化手段 |
| プロノイア制 | Pronoia System | administrative_system | BYZ 初期行政制度。廃止後に 3 ポリシーが解禁 |
| コムネノス家式整備 | Komnenian Formalization | ポリシー | pronoia_system 廃止後選択肢の一つ |
| パレオロゴス家式世襲転換 | Palaeologan Hereditary Transition | ポリシー | pronoia_system 廃止後選択肢の一つ |
| 改革プロノイア制 | Reformed Pronoia System | ポリシー | pronoia_system 廃止後選択肢の一つ |
| 紫の間に生まれし者 | Born in the Purple | 継承メカニクス | 1.3。後継者選定・正統性 `[src: heir_selections/monarchy.txt]` |
| ツァーリ国の黄昏 | Twilight of the Tsardom | ディザスター | 1.3。ブルガリア等バルカン勢力の崩壊。ビザンツの再征服機会 `[src: disasters/twilight_of_the_tsardom.txt]` |
| 反ジェノヴァ盟約 | （ヴェネツィア連携フレーバー） | イベント | 1.3。対ジェノヴァのビザンツ・ヴェネツィア連携 `[src: events/DHE/flavor_byz_ven.txt]` |

### パッチ 1.2 / DLC 共通用語

| 日本語 | 英語 | カテゴリ | 備考 |
|--------|------|---------|------|
| 不滅の鳳凰（DLC） | Fate of the Phoenix | DLC | ビザンツ固有大型 DLC |
| ディザスター | Disaster | システム | 大規模固有イベント群 |
| 社会価値観 | Societal Values | システム | 国家の価値観スライダー |
| 優位性戦争 | Superiority War | 戦争目標 | Coalition War が 1.2 で変更。首都占領なしに勝利可能 |
| 宗教的影響力 | Religious Influence | 正教システム | 1.2 で Rite Power を廃止・統合 |
| 総主教 | Patriarch | キャラクター | 1.2 で正教オーバーホール。キャラクターとして実装 |
| ロマノス国境地理 | Roman Borders Geography | スクリプト地理 | Restore Roman Borders CB の対象範囲 |

### 共通用語（抜粋）

| 日本語 | 英語 | カテゴリ | 備考 |
|--------|------|---------|------|
| 召集軍 | Levy | システム | 一時的な徴兵 |
| 支配度 | Control | システム | 州支配度（占領度） |
| 進歩 | Advance | システム | 国家技術ツリー |
| 階級 | Estate | システム | 社会階層 |
| 統合軍備 | Combined Arms | システム | 多兵科混成ボーナス（Patch 1.1 追加） |
| 開戦事由 | Casus Belli（CB） | 外交 | 戦争の正当な理由 |
| 安定度 | Stability | システム | 国内の政治安定指標 |
| 戦争疲弊度 | War Exhaustion | システム | 戦争による国民負担の蓄積 |
| 正統性 | Legitimacy | システム | 君主・政権の正当性 |

---

## 出典

### 一次情報（ゲームスクリプト確認済み）

以下のファイルからスクリプト検証を実施し `[src: ...]` マーカーを付与した。

| ファイル | 検証内容 |
|---------|---------|
| `game/main_menu/setup/start/10_countries.txt` | BYZ 初期設定（首都・ランク・テック・ルーラー・財政・Societal Values・リフォーム・行政システム・占領状態） |
| `game/in_game/common/casus_belli/D008_restore_roman_borders.txt` | Restore Roman Borders CB（conquer_cost・ticking_war_score・対象範囲・解禁条件） |
| `game/in_game/common/subject_types/D008_pronoia.txt` | Pronoia サブジェクト（レベル・外交キャパ・modifier 群・strength_vs_overlord・併合条件・支払い・可視条件） |
| `game/in_game/common/government_reforms/country_specific.txt` | Katepanata 政体（potential 条件・基本効果・ディザスター完了後追加効果） |
| `game/in_game/common/unit_types/D008_byzantine_unit_types.txt` | Cataphracts（全 Age）・Legionaries・Greek Fire Ships・Greek Fire Infantry・Varangians の全スペック |
| `game/in_game/events/government/D008_latinization_vs_hellenization.txt` | Latinization vs Hellenization Societal Value の定義 |
| `game/in_game/common/religions/christian.txt` | 正教の maximum_religious_influence・stability_cost・global_max_literacy 等 |
| `game/in_game/events/disaster/D008_fate_of_the_phoenix.txt` | Fate of the Phoenix ディザスター・DLC ゲート・CB 解禁トリガー |
| `game/in_game/common/advances/country_byz.txt` | Cataphracts age_1 アドバンス（DLC なし可）の確認 |
| `game/in_game/common/casus_belli/coalition.txt` 行 13 | Coalition War conquer_cost 確認 |
| `game/in_game/common/wargoals/00_default.txt` 行 244-261 | Superiority War ticking_war_score 確認 |
| `game/in_game/common/auto_modifiers/country.txt` 行 90 | ロジスティクス距離定義 |
| `game/in_game/common/bureaucracies/byz.txt` | ビザンツ固有官僚制アドバンス（スクリプト確認済み） |
| `game/in_game/common/disasters/twilight_of_the_tsardom.txt` | Twilight of the Tsardom ディザスター（1.3。ブルガリア等バルカン崩壊） |
| `game/in_game/events/DHE/flavor_BUL.txt` | Twilight of the Tsardom のブルガリア側フレーバー（1.3） |
| `game/in_game/events/DHE/flavor_byz_ven.txt` | 反ジェノヴァ盟約（ビザンツ・ヴェネツィア連携、1.3） |
| `game/in_game/common/heir_selections/monarchy.txt` | Born in the Purple 継承メカニクス（1.3） |
| `game/in_game/common/unit_types/1_uniques_for_age_2_renaissance.txt` 行 68 | ジェノヴァ弩兵の軽歩兵化（1.3） |

> **1.3 補足**: 上記「1.3」マーカー付きファイルはインストール版 1.3 安定版（buildid 24075414 = 1.3.10）のローカルスクリプトで実体を確認したもの。「1.3 新規か否か」の最終判定は 1.2/1.3 パッチノート差分による。船コスト増・海戦致死性・1337 国境修正はエンジン内部値/フレーバー調整でスクリプト実値未確認のため `（コミュニティ知見：公式パッチノート由来・スクリプト未確認）` 扱い。Patch 1.3 wiki: eu5.paradoxwikis.com/Patch_1.3。

### 参照ファイル（スクリプト未確認、wiki / コミュニティ知見）

| ファイル | 内容 |
|---------|------|
| `game/in_game/events/DHE/flavor_BYZ.txt` | BYZ 通常フレーバー（L3690-3732 pronoia_system 廃止イベント含む） |
| `game/in_game/events/DHE/D008_flavor_BYZ.txt` | DLC 追加 BYZ フレーバー |
| `game/in_game/common/disasters/byzantine_succession_crisis.txt` | ビザンツ継承危機ディザスター |
| `game/in_game/common/character_interactions/d008_mutilations.txt` | 失明・肢体切断インタラクション |

### コミュニティ知見（スクリプト未確認項目一覧）

以下は `（コミュニティ知見：スクリプト未確認）` マーカー付きの項目のまとめ:

- Latin Culture Movement のヴェネツィア・ジェノヴァ介入の具体的影響度
- DHE 140+ 追加の内訳詳細
- ROM タグ変形の正確な達成条件・効果
- pronoia_system 廃止後 3 ポリシー（komnenian_formalization 等）のスクリプト上の詳細効果
- Patriarch（総主教）キャラクター実装の具体的なゲームメカニクスへの反映
- 正教 Rite Power 廃止後の Patriarch との関係詳細
- ROM 変形後の帝国正統性外交の詳細

### 公式 Wiki（パッチ・DLC 情報）

- [Patch 1.2 — EU5 Wiki](https://eu5.paradoxwikis.com/Patch_1.2)
- [Fate of the Phoenix — EU5 Wiki](https://eu5.paradoxwikis.com/Fate_of_the_Phoenix)
- [Byzantine content — EU5 Wiki](https://eu5.paradoxwikis.com/Byzantine_content)

### コミュニティ情報（補足知見）

- [Steam Workshop: EU5](https://steamcommunity.com/app/3450310/workshop/)
- Reddit r/eu5

上記出典テーブルを参照

### 関連ガイド

| ガイド | 参照する場面 |
|--------|-------------|
| `eu5-ottoman-guide.md` | ビザンツ復興を阻止する側（オスマン）の視点。相手の行動パターンを理解するために参照 |
| `eu5-religion-guide.md` | 正教メカニクスの詳細（Patriarch・Religious Influence・Rite Power 廃止の影響） |
| `eu5-universal-guide.md` | 軍事数値の詳細・基本メカニクス |
| `eu5-government-guide.md` | 政府効率・行政システムの詳細数値 |
| `eu5-regional-guide.md` | バルカン地域情勢・周辺国の詳細 |
| `eu5-hungary-guide.md` | 最有力同盟候補ハンガリーの攻略視点 |
