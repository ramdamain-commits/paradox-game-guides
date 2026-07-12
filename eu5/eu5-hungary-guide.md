# EU5 ハンガリー攻略ガイド（Patch 1.3 時点）

> ハンガリー → 中欧の盟主を狙う序盤から大国化までの整理。
> 2026-07-10 確認時点の最新パッチ 1.3（buildid 24075414 / バージョン 1.3.10、安定版）に合わせて更新。1.2「Echinades」（2026-05-06 リリース）baseline に 1.3 の変更点を統合済み。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。

---

## パッチ 1.2「Echinades」でのハンガリー関連変更点

ガイドの前提が古くならないよう、先にパッチ差分だけを抜き出しておく。

### Patch 1.2「エキナデス」（2026-05-06 リリース、DLC Fate of the Phoenix 同時）

ハンガリーは中欧・バルカン地域カトリック大国であるため、Fate of the Phoenix DLC のビザンツ復興コンテンツおよび HRE 大幅オーバーホールの影響を特に強く受ける。

#### バルカン新規コンテンツ（最大影響）

| 変更 | 内容 |
|------|------|
| 新 Advances 300+ | バルカン関連のフレーバーが大幅に拡充 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| 新 DHE 140+ | ハンガリー周辺のバルカン情勢が動的に変化 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Restore Roman Borders CB 新登場 | ビザンツ用の新 CB。ハンガリー支配下のバルカン領土が標的になりうる最大の脅威 `[src: casus_belli/D008_restore_roman_borders.txt + script verified]` |
| Latin Culture Movement | ハンガリー支配下カトリック文化との連動可能性 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| 新 3D モニュメント（Hagia Sophia 等） | 観光・威信収入の動的変化 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |

#### HRE 関連（ハプスブルク同君連合・継承後）

| 変更 | 内容 |
|------|------|
| Imperial Diet 投票システム | 帝国議会の投票メカニクス新規追加。4 段階（Court Assembly / Early Diet / Bicamerial / Tricamerial）`[src: parliament_types/01_international_organization.txt + script verified]` |
| 皇帝の列強スコア（Great Power Score、以下 GP Score）貢献 250→50 | 帝国皇帝の GP Score 寄与が大幅減少（コミュニティ知見：`hre.txt` に `great_power_score_exempt_from_forfeit` 等の該当識別子は非実在。250/50 とも Patch_1.2 wiki 由来でスクリプト未確認。旧記載の「新値のみscript verified」は誤り） `[src: Patch_1.2 wiki]` |
| Free Cities 自動参戦廃止 | INDEPENDENT Free City のみが皇帝防衛義務を持ち、自動参戦しなくなった `[src: international_organizations/hre.txt + script verified]` |
| Imperial Armories 新建造物 | 帝国兵器庫（gold=500）。自国所有で local_manpower +0.0025、外国所有で manpower_to_building_owner +0.005。設置条件: 皇帝のみ・HRE 加盟領内・law:military_contribution 必須 `[src: building_types/hre_buildings.txt + script verified]` |
| 王朝力上限 200→300 | Dynastic Power の蓄積上限が拡大 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| 1400 年 Golden Bull 未制定なら諸侯離脱可能 | 1400 年以降に golden_bull_policy 未採択の場合、HRE 離脱が可能になる `[src: international_organizations/hre.txt + script verified]` |

#### 戦争・外交

| 変更 | 内容 |
|------|------|
| Claim Throne CB 制限 | 請求者がすでに対象国を統治中なら CB 不発。ハンガリー王位継承戦略の事前確認が必要 `[src: casus_belli/claim_throne.txt + script verified]` |
| Coalition War が Superiority War 化（攻撃側コスト） | 攻撃側 conquer_cost=0.75/release_cost=0.25 `[src: casus_belli/coalition.txt + script verified]` |
| Coalition War が Superiority War 化（防衛側コスト） | 防衛側 conquer_cost=2.5 `[src: casus_belli/coalition.txt + script verified]` |
| Coalition War が Superiority War 化（ticking_war_score） | ticking_war_score=0.5 `[src: wargoals/00_default.txt + script verified]` |
| Enforce Peace 双方合意必須 | 一方的講和強制不可。双方の合意が必要 `[src: Patch_1.2 wiki + script verified]` |
| 好戦的傾向（Belligerent） / Conciliatory 修正 | 年間減衰 4→5 等のバランス修正 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |

#### 軍事

| 変更 | 内容 |
|------|------|
| 要塞駐屯 Heavy Infantry 限定 | Light Infantry は要塞駐屯不可。国境守備の編成見直しが必要 `[src: unit_categories/01_army_heavy_infantry.txt + script verified]` |
| ハイドゥクの兵科分類 | ハイドゥクは Light Infantry 系統。**要塞駐屯不可**を script で確認済み `[src: unit_types/1_uniques_for_age_5_absolutism.txt + script verified]` |
| 兵科 Heavy/Light 分類 | 歩兵・騎兵がそれぞれ Heavy/Light に分類。重騎兵・軽騎兵の使い分けが重要に `[src: unit_categories/00-04_army_*.txt + script verified]` |
| ロジスティクス距離 50→30、食料消費 10倍 | 対オスマン・対モルダヴィア遠征の補給線管理が必須に `[src: Patch_1.2 wiki + script verified]` |
| 傭兵コスト +25% | 黒軍（Black Army）への傭兵依存度の再評価が必要 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |

### ハンガリープレイヤーが特に注意すべき変更

- **Restore Roman Borders CB 新登場** — ビザンツが復興した場合、ハンガリー支配下のバルカン領土が標的化する最大の脅威 `[src: casus_belli/D008_restore_roman_borders.txt + script verified]`
- **300+ Advances・140+ DHE** — バルカン情勢がより動的・複雑化。トランシルヴァニア・ヴァラキア周辺の勢力変動に常に注意 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）
- **Claim Throne CB 制限** — 既に統治中の請求者では CB が不発になるため、ハンガリー王位継承戦略を事前に確認する
- **要塞駐屯 Heavy Infantry 限定** — ハイドゥク（Light Infantry 系統、script verified）を国境要塞守備に置く編成は 1.2 で機能しない
- **ハプスブルク同君連合時は HRE 全面オーバーホールの影響を受ける** — Imperial Diet・GP Score・Imperial Armories 等、モハーチ後ルート全体の戦略見直しが必要

### 過去パッチ（1.1「ロスバッハ」/ 1.1.10）

1.2 でも引き続き有効な 1.1 系の主要変更を要約する。

| 変更 | 概要 |
|------|------|
| 貴族召集軍（Noble Levies） | 召集量 +50%（上方修正）、戦闘効率補正 +25% は削除 |
| 統治者を優遇（Favor the Ruler） | 君主力 20% → 33% に増加 |
| イベント修正 | `flavor_hun.270`（エルデーディ・タマーシュ）選択肢・ローカライズ修正 |
| 不具合修正（1.1.10） | 破産時建造物無限ループ、召集軍の部隊貼り付き、正規部隊 +100% 戦闘ボーナス誤付与を修正 |

### Patch 1.3（buildid 24075414 = 1.3.10、安定版）

ハンガリーへの直接影響が大きい変更を要約する。数値の詳細と運用への落とし込みは「黒軍」「ヴィシェグラード会議」「ポーランド同君連合」「内政・経済」の各節に統合済み。

| 変更 | 概要 |
|------|------|
| 陸軍 goods 需要 2 倍 | 常備軍の goods 消費が約 2 倍に増加。黒軍（Heavy Infantry）中心の常備軍規模は goods 供給（産地確保・交易）とセットで再設計が必要（コミュニティ知見：公式パッチノート由来・スクリプト未確認） |
| 建物維持費の逓増（1 世紀で +50%） | 建造物維持費が時間経過で逓増。要塞網（ヴェグヴァール体制）を厚く積む防衛戦略は長期維持費が増す（コミュニティ知見：公式パッチノート由来・スクリプト未確認） |
| Union of Crowns（王冠連合協定）の女性継承整理 | ポーランドとの PU 協定 `union_of_crowns_pact` まわりの継承ロジックが整理され、女性継承が候補として扱われるケースが追加 `[src: scripted_relations/union_of_crowns_pact.txt, heir_selections/monarchy.txt]`。ただし `no_female_heirs_for_poland` によりポーランド方面は女性継承者が除外される例外あり（→ ポーランド同君連合節） |

---

## 開始状況（1337年）

### 基本ステータス

| 項目 | 値 |
|------|-----|
| 国家ランク | 王国（Kingdom） |
| 政体 | 君主制（Monarchy） |
| 主要文化 | ハンガリー（Hungarian） |
| 宗教 | カトリック |
| 首都 | ブダ（Buda） |
| 主要資源 | 金・銀鉱山（スロバキア、トランシルヴァニア） |
| 従属国 | クロアチア（Personal Union 下） |
| 地形 | パンノニア平原（農地・平原 → 人口増に有利） |
| 人口推定 | 中欧上位。パンノニア平原の農業地帯を中核に、スロバキア鉱山都市・トランシルヴァニア高原を加えた広域人口基盤（コミュニティ知見） |
| GP Score 目安 | 開始時点で中欧 2 位前後。ポーランドと並ぶ大国扱い（コミュニティ知見） |
| 初期収入目安 | 金銀鉱山が安定した収入源。序盤から黒字運営が可能な国力（コミュニティ知見） |

### Societal Values（社会価値観）

ハンガリーの初期 Societal Values は中欧カトリック封建王国としての傾向を反映している。`flavor_hun.200`「[君主名]の軍隊」イベントやマティアス・コルヴィヌス改革（`flavor_hun.110`）でこれらを動かすことができる。

| 社会価値 | 初期傾向 | 意味 | 備考 |
|----------|---------|------|------|
| traditionalist_vs_innovative（伝統主義 vs 革新主義） | やや伝統主義寄り | 改革コストに影響。改革を進めたい場合は革新主義方向に動かす | マティアス改革 B「社会改革」で融和寄り（コミュニティ知見） |
| offensive_vs_defensive（攻勢 vs 守勢） | やや攻勢寄り | バルカン拡張のため攻勢を維持推奨 | 黒軍前身イベント `flavor_hun.200` で質・陸・攻勢寄りに移動 `[src: events/DHE/flavor_HUN.txt]` |
| land_vs_sea（陸重視 vs 海重視） | 陸寄り | 内陸国のため陸軍重視が自然 | 黒軍前身イベント `flavor_hun.200` で陸寄りに移動（コミュニティ知見） |
| quality_vs_quantity（質重視 vs 量重視） | やや質寄り | 黒軍・フサール等の精鋭化に連動 | 黒軍前身イベント `flavor_hun.200` で質寄りに移動（コミュニティ知見） |

### 初期政府改革・行政システム

| 項目 | 値 |
|------|-----|
| 主要政府改革 | `hun_power_to_magnates`（大貴族権力強化改革）を保持。農民反乱イベント `flavor_hun.160` の発火条件に直結するため注意が必要 `[src: events/DHE/flavor_HUN.txt]` |
| 議会 | 中盤以降に議会（Parliament）が登場し、フニャディ登用などのキー判断に関わる（コミュニティ知見：スクリプト未確認） |
| 後継者選定 | 王室婚姻管理が最重要。王朝断絶はポーランド同君連合機会の消滅に直結 |

> **注意**: `hun_power_to_magnates` は農民反乱（`flavor_hun.160`）の発火条件の一つ。安定度 -20 以下になると人口打撃イベントが発生する `[src: events/DHE/flavor_HUN.txt]`。

### 領土状況（1337年）

| 地域 | 状況 |
|------|------|
| ブダ・ペスト | 首都圏。パンノニア平原の中核。経済・政治の拠点 |
| スロバキア鉱山地帯 | バニスカー・ビストリツァ（Banská Bystrica）等。金・銀・銅の産地。序盤収入の柱 |
| トランシルヴァニア | 東部の山岳高原。コア保持。ブラン城（`flavor_hun.520`）建設でセルビア・ワラキアへの防衛線を張る |
| クロアチア | PU（Personal Union）下。アドリア海への通路。統合を長期的に進める |
| バルカン方面 | セルビア・ボスニア・ワラキアと国境を接する。第一の拡張方向 |

### 周辺国との関係

| 方角 | 隣国 | 関係性 |
|------|------|--------|
| 西 | オーストリア・ボヘミア（神聖ローマ帝国） | 中立〜友好。ボヘミアと良好なら西は安泰 |
| 北 | ポーランド | 同君連合の候補。**絶対に宣戦しない**（後述） |
| 南 | セルビア・ボスニア・ワラキア | 最初の拡張先 |
| 南東 | オスマン帝国 | 最大の脅威。中盤以降の主敵 |

### 初期の強み・弱み

| 強み | 弱み |
|------|------|
| 王国ランクで序盤から外交力が高い | 王朝断絶リスク（序盤の婚姻管理が重要） |
| 金銀鉱山による経済基盤 | バルカン方面の山岳地帯は支配度（Control）維持が困難 |
| 固有進歩で騎兵戦力 +20% `[src: advances/country_HUN.txt + script verified]` | 南東のオスマンが中盤以降に圧迫 |
| パンノニア平原の人口増加ポテンシャル | `hun_power_to_magnates` 改革が農民反乱リスクを内包 |
| 中盤以降の黒軍・フサールという強力な固有ユニット群 | 湖による近接障壁（橋の建設が必須） |

---

## Day 1（ポーズ解除直後）

### 即座にやること

1. **ペストの市場（Marketplace）ツリーを強化**
   - 市場中心は首都ブダではなく隣接の **ペスト**（Pest、`raw_material = wheat`）。Entrepot / Trading Hub 系はペスト側に積む `[src: map_data/location_templates.txt, pest/buda]`
   - ブダ（`raw_material = wine`、首都・宮廷拠点）は `is_market_center` フラグを持たない想定のため、市場系はそもそも建造不可。ペスト未保有の例外時のみブダ建造を検討
   - コミュニティ知見：交易収入の土台は「ペストの市場ツリー＋スロバキア鉱山との内陸ルート」

2. **内閣（Cabinet）を安定度（Stability）投資に割り当て**
   - 序盤の安定度維持が内政の土台

3. **不要な要塞（Fortification）を削除**
   - 維持費を浮かせて経済基盤を作る
   - 対オスマン防衛に重要なベオグラード方面の要塞は残す

4. **ライバル設定: セルビア、ワラキア**（ボスニアは含めない）
   - ライバル指定で `cb_conquer_enemy`（敵対関係を条件とする征服 CB、コア不要）を解放し、戦争の正当性を得る `[src: casus_belli/conquer_enemy.txt + script verified]`
   - 一方の **`cb_conquer_province`（「Claims on Province」）はコア（`integration_level = core`）取得後にのみ使用可能**。征服後に `cabinet_actions/integrate_province.txt` でコアを育てる流れになる
   - **EU5 にはスパイによる Claim 捏造（EU4 の fabricate_claim）は存在しない**（1.2 スクリプト確認、`spy_actions/` 自体が存在せず `scripted_relations/` のスパイ網にも Claim 付与効果はない）。「請求権捏造」前提の戦略は通用しないため注意 `[src: scripted_relations/sow_discontent.txt, corrupt_officials.txt + script verified]`
   - **ボスニアは開始時 HUN の属国**（`flavor_BOS.txt:28` で `is_subject_of = c:HUN` トリガー確認）。属国にはライバル指定そのものが通常不可。継続属国化 → 統合（Integrate）か、離反時の `disloyal_subject` CB で再征服する `[src: events/DHE/flavor_BOS.txt + script verified]`

5. **ポーランドとの関係改善（Improve Relations）を開始**
   - 王室間の婚姻（Royal Marriage）を結び、同君連合チャンスに備える
   - **絶対にポーランドに宣戦しない**：1437 年のフニャディ登用（`flavor_hun.1`）までの 100 年間、ポーランド関係を最重要外交と位置付ける

6. **金銀の輸出禁止を検討**
   - イベント「[国名]の金」（`flavor_hun.340`）が発火した際、「禁令を延長しろ」を選択
   - Gold +2（scale）を得て国内で活用

7. **フニャディ登用に向けた貯金と関係構築の布石**
   - フニャディ・ヤーノシュは 1430-1443 年に月 5% で発火する招聘イベント（`flavor_hun.1`）のキー人物
   - 採用コスト Gold -1（scale）に備えて財政的余裕を確保しておく
   - 採用後は adm 84-94 / dip 70-80 / mil 90-100 という最高水準の将軍候補になる `[src: events/DHE/flavor_HUN.txt + script verified]`

### 軍編成の基本方針（→ 詳細は[軍事ドクトリン](#軍事ドクトリン)を参照）

- ハンガリーの固有進歩「複合弓軽騎兵」で騎兵戦力 +20% `[src: country_HUN.txt, hun_composite_light_cavalry + script verified]`。序盤から**騎兵比率を 40〜50%** に保つ
- 将軍は騎兵戦力に寄与する特性（Trait）を重視
- 統合軍備（Combined Arms）ボーナスにより、歩兵・砲兵も混ぜるメリットがある

---

## 序盤戦略（1337〜1400）

### フェーズ1: バルカン南下の前準備（1337〜1345）

まず外交基盤を整え、戦争の正当性を確保する。

**やること:**

- **セルビア・ワラキア**をライバル設定して `cb_conquer_enemy` を確保（ボスニアは属国のためライバル不可）。請求権捏造メカニクスは 1.2 でも存在しないため、コア育成は征服後の `Integrate` で進める
- ポーランドへの王室婚姻を早期に実施
- ヴィシェグラード会議（`flavor_hun.330`、→ 詳細は[固有イベント時系列](#固有イベント時系列)参照）の発火を待ちながら対 POL 関係を維持（注意: 現君主がカローイ・ロベルト `character:hun_karoly_robert`、かつ POL の君主がカジミェシュ 3 世 `character:pol_casimir_iii_piast` である必要がある。1337〜1370 内にどちらかが死亡・交代するとイベントが不発になる）
- **ペスト**の市場ツリー強化を最優先（市場中心はブダではなくペスト）。ブダには製材所など非市場系のインフラを積み、スロバキア鉱山地帯の開発を並行
- 不要要塞の削除で維持費を抑制

**避けること:**

- ポーランドへの宣戦・敵国同盟（同君連合チャンスが永久に消滅する）
- オスマンとの早期接触（1350 年代はまだ序盤の拡張フェーズ）
- 過剰な借金（鉱山収入があるため、初期は借金なしで運営できるはず）

**関連イベント:**

- `flavor_hun.330` ヴィシェグラード会議（1337-1370）→「あの合意を成文化しよう」でポーランド関係強化 + PU pact 契機 `[src: events/DHE/flavor_HUN.txt]`（トリガー条件: 現君主 `character:hun_karoly_robert`・POL 君主 `character:pol_casimir_iii_piast`。カローイ・ロベルトの早期死亡か POL 君主交代でイベント不発になる）
- `flavor_hun.340` [国名]の金（1340-1390）→「禁令を延長しろ」で Gold +2 scale `[src: events/DHE/flavor_HUN.txt]`
- `flavor_hun.350` 1222 年の金印勅書（1340-1440）→ 状況次第（コミュニティ知見：効果詳細未確認）`[src: events/DHE/flavor_HUN.txt]`

### フェーズ2: バルカン拡張（1345〜1370）

準備が整ったらバルカン南下を開始する。

**やること:**

| 順位 | 対象 | 方法 | 備考 |
|------|------|------|------|
| 1 | セルビア | ライバル指定 → `cb_conquer_enemy` で征服 → コア化 | 弱小国。最初の拡張先 |
| 1' | ボスニア | **開始時属国**。継続属国化 → 統合、離反時のみ `disloyal_subject` CB で再征服 | ライバル設定・征服 CB 直接利用は不可 |
| 2 | ワラキア | 辺境伯領（March）化 | オスマンとの緩衝地帯。属国に留める |
| 3 | ダルマチア海岸 | 状況次第で征服 | ヴェネツィア領と接するため外交注意 |

**ポイント:**

- クロアチアは PU 下なので征服不要。統合（Integrate）を長期的に進める
- バルカンの山岳地帯は支配度維持が困難 → **辺境伯領（March）化**が効率的
- 属国は 2〜3 個まで。過剰な従属国は**階級権力**のバランスを崩す
- セルビア征服後は `flavor_hun.220` セルビア陥落が発火する可能性。セルビア人移民でベオグラードの人口が補われる
- ボスニア問題（`flavor_hun.600`）への対応も並行して発生しうる

**避けること:**

- バルカン整理前にオスマンに挑む（兵力・経済とも不足）
- セルビア征服後に別の戦争を同時に開かない（兵力分散で各個撃破される）

**関連イベント:**

- `flavor_hun.600` ボスニア問題（1340-1500）→ 外交対応
- `flavor_hun.220` セルビア陥落（SER 消滅後）→ セルビア人移民（amount 0.2、20 年）`[src: events/DHE/flavor_HUN.txt]`（スクリプト上は `from=1337.1.1` だが実質的な発火は SER 消滅後に限定される）
- `flavor_hun.520` ブラン城（1377-1420）→ ブラショフ所有時にトランシルヴァニア要塞建設

### フェーズ3: 黒死病対策と中盤準備（1370〜1400）

バルカン拡張後は内政強化フェーズに入る。同時に中盤の重要イベント群の準備を進める。

**やること:**

| 項目 | やること |
|------|---------|
| 病院建設 | 主要都市に**病院（Hospital）**を建設（1340年代までに可能ならさらに早く） |
| 街道整備 | **街道（Road）**を全土に敷設。近接ペナルティを軽減 |
| 橋の建設 | **橋（Bridge）**を湖上に建設。ハンガリーの湖が近接障壁になっている |
| 鉱山開発 | 金銀鉱山（スロバキア・トランシルヴァニア）の開発を優先 |
| ドラゴン騎士団の準備 | `flavor_hun.410`（1400-1450）に備え、騎士団法律（Knights Order Law）の整備と Gold 余剰を確保 |

**関連イベント:**

- `flavor_hun.370` 聖ゲオルギウス騎士団（1337-1437）→「騎士団を拡大させるのだ！」で軍事ボーナス（コミュニティ知見：効果詳細未確認）
- `flavor_hun.400` ペーチの大学（1350-1400）→ 文化・教育ボーナス（コミュニティ知見：効果詳細未確認）
- `flavor_hun.460` 彩飾年代記（1358-1375）→ 文化イベント
- `flavor_hun.360` ヴラフ法（1337-1600）→ 文化・民族管理

---

## 中盤戦略（1400〜1500）

### フニャディ・ヤーノシュの登用（1430〜1443）

中盤最大のターニングポイント。イベント `flavor_hun.1` は 1430-1443 年の間、月 5% で発火する（fire_only_once）。

**イベント内容（`flavor_hun.1`）:**

| 選択肢 | 効果 | 推奨 |
|--------|------|------|
| A「採用」 | Gold -1 scale、adm 84-94 / dip 70-80 / mil 90-100、特性: bold_fighter | **推奨**（コミュニティ知見：最高水準の将軍候補） |
| B「拒否」 | prestige_weak_penalty、banish_character | 非推奨 |

`[src: events/DHE/flavor_HUN.txt]`

フニャディは欧州でも有数の能力値を持つ将軍候補。Gold -1（scale）のコストは少額であり、即座に採用すること。採用後は対オスマン防衛の要となる。

### 議会と摂政問題（1444〜1470）

以下の条件がすべて揃うと `flavor_hun.2` が発火する（月 50%）。`[src: events/DHE/flavor_HUN.txt, flavor_hun.2]`

- 議会（Parliament）を保有している（`has_parliament = yes`）
- 摂政状態である（`has_regent = yes`）
- 戦争中である（`at_war = yes`）
- フニャディ・ヤーノシュが存命（`character:hun_janos_hunyadi is_alive`）
- 現君主がフニャディでない
- 現摂政がフニャディでない

**イベント内容（`flavor_hun.2`）:**

| 選択肢 | 効果 | 推奨 |
|--------|------|------|
| A「フニャディを摂政に」 | 名声 weak_bonus、貴族満足度 weak_penalty | **推奨**（コミュニティ知見：軍事優先なら） |
| B「現評議会維持」 | 貴族満足度 mild_bonus | 内政安定優先なら |
| C「フニャディを新国王に」 | 正統性 weak_penalty、フニャディ君主化 | 状況次第（コミュニティ知見） |

`[src: events/DHE/flavor_HUN.txt]`

### ヴィシェグラード会議

イベント「[年]年のヴィシェグラード会議」（`flavor_hun.330`）で外交ボーナスが得られる。

- 選択肢「あの合意を成文化しよう」を選ぶとポーランドとの関係が強化される。POL に `hun.331` が送られ、POL が合意すれば `union_of_crowns_pact` が成立する `[src: events/DHE/flavor_HUN.txt]`
  - 成立時（`flavor_hun.332`）の追加効果:
    - `union_of_crowns_pact` リレーションが形成される
    - **継承法が `union_of_crowns_succession` に変更**される（内政・後継者選定に大きく影響するため注意）
    - POL との Opinion modifier `agreed_second_congress_of_visegrad` が付与される
    - **1.3 で継承ロジックが整理**され、女性継承者が継承候補として扱われるケースが追加された `[src: scripted_relations/union_of_crowns_pact.txt, heir_selections/monarchy.txt]`（対ポーランドの例外あり。→ 次節「ポーランド同君連合」参照）
- ポーランドが出席すれば第 2 回会議（`flavor_hun.331/.332`）につながる
- ポーランドが拒否した場合（`flavor_hun.18`）は関係に影を落とすが、致命的ではない

### ポーランド同君連合

- ポーランドとの**王室間の婚姻**と**高い評価（Opinion）**を維持し続ける
- **絶対にポーランドに宣戦しない**（同君連合の機会が消滅する）
- ポーランドの敵国と同盟しない（参戦要請でポーランドとの戦争に引きずり込まれるのを防ぐ）
- 同君連合成立後 → **統合（Integrate）**で外交コストを毎月消費し、約 50 年で完了
- 統合を進めるには `union_integration_level` と `union_senior_succession_law` の整備が必要 `[src: laws/40_personal_unions.txt + script verified]`
- **⚠ 対ポーランド PU の女性継承除外例外**: 継承資格ルールに `no_female_heirs_for_poland` が定義されており、ポーランド方面の継承では女性継承者が資格から除外される `[src: heir_selections/monarchy.txt:1206（custom_eligibility_rules = no_female_heirs_for_poland）]`。前節（ヴィシェグラード会議）の「1.3 で女性継承が継承候補として扱われるケースが追加された」を「対ポーランド PU にも一般に適用される」と早合点して女性後継者で繋ごうとすると不発になりうる。ヤギェウォ朝・ポーランド王冠連合ルートを狙う場合は男性後継者の確保を引き続き計画に入れること。

### マティアス・コルヴィヌスの改革（1466〜1470）

ハンガリアディ家の君主が存在する場合に発火（月 10%）。`flavor_hun.110`。

> **注:** スクリプト上のトリガーは `dynasty = dynasty:hunyadi_dynasty` による王朝判定であり、マティアス固有のキャラクター ID は存在しない（コミュニティ知見: `hun_karoly_robert` のような固有スクリプト ID ではマティアスを個別に特定できない）。

**3 択の効果:**

| 選択肢 | 効果 | 推奨 |
|--------|------|------|
| A「行政改革」 | Gold -2、中央集権寄りに Societal Value 移動 | **推奨**（コミュニティ知見：中央集権化を進めたいなら） |
| B「社会改革」 | Gold -2、融和寄りに Societal Value 移動 | 安定優先なら |
| C「改革不要」 | コスト 0、革新→伝統主義寄りに | 非推奨（コミュニティ知見：機会損失） |

`[src: events/DHE/flavor_HUN.txt]`

### オスマン対策

中盤の最大課題。正面衝突は避け、段階的に対抗する。

| 段階 | 行動 |
|------|------|
| 1 | バルカンの緩衝地帯を固める — ワラキア・モルダヴィアを辺境伯領化 |
| 2 | ベオグラード防衛を強化（イベント `flavor_hun.210`「ハンガリーの要」で「国費をさらに投入しよう」選択推奨） |
| 3 | 同盟網を構築 — オーストリア、ポーランド（同君連合済みなら不要）と共闘体制 |
| 4 | 騎兵主力の軍を整備 — 固有進歩のボーナスを最大活用 |
| 5 | **オスマンがアナトリアまたはマムルーク方面で戦争中**に、同盟軍と共に宣戦するのが最適タイミング |

### ベオグラード防衛（`flavor_hun.210`）

1450-1500 年の間に、ベオグラード所有・TUR 隣接・TUR 都市数 > HUN・ベオグラード要塞有りという条件で発火。

| 選択肢 | 効果 |
|--------|------|
| A「国費をさらに投入しよう」 | `hun_frontier_fortresses` 法律解禁 + `vegvar_system`（ヴェグヴァール体制）政策 |
| B「現状維持」 | `hun_frontier_fortresses` 法律解禁 + `not_maintained` 政策 |

`[src: events/DHE/flavor_HUN.txt]`

**推奨:** 選択肢 A。`vegvar_system` はベオグラードを中核とした国境要塞防衛体制で、対オスマン防衛線の基幹となる（コミュニティ知見）。

### セルビア陥落とセルビア人移民（`flavor_hun.220`）

SER 消滅後、ベオグラード保有・キリスト教・TUR 非同盟・ベオグラードがセルビア文化という条件で発火。なおスクリプト上の `from=1337.1.1` との乖離に注意（実際の発火タイミングは SER 消滅依存であり 1337 年とは限らない）。

- TUR セルビア文化都市 1か所からベオグラードへ移民（amount 0.2、20 年継続）
- セルビア系人口の流入がベオグラードの人的資源・人口を補強する

`[src: events/DHE/flavor_HUN.txt]`

### ドラゴン騎士団（1400〜1450）

`flavor_hun.410`：**騎士団法律（`order_of_chivalry_law`）保持**・非戦時・君主在位・バルカンにオスマン文化イスラム都市 5 以上という条件で発火（月 5%）。`[src: events/DHE/flavor_HUN.txt, flavor_hun.410 + laws/04_order_of_chivalry.txt]`

| 選択肢 | 効果 |
|--------|------|
| A「結成」 | `order_of_the_dragon_policy` 解禁、君主騎士団加入、Gold -6、名声 mild_bonus、ルーマニア・ハンガリー・セルビアクロアチア・アルバニア語国家に hun.411 を送信 |
| B「自力で戦う」 | 名声 weak_penalty |

`[src: events/DHE/flavor_HUN.txt]`

**推奨:** 選択肢 A（コミュニティ知見）。Gold -6 は中盤の出費として重いが、周辺国との対オスマン連携強化は長期的な安全保障に直結する。

### 宗教改革への対応（1500 年前後〜）

イベント「[デブレツェン]の教会会議」（`flavor_hun.230`）でカルヴァン派拡大への対応を迫られる。

| 選択肢 | 効果 |
|--------|------|
| 「イエズス会を招致しよう」 | カトリック維持。`jesuits_allowed` 政策、宗教影響力 mild_bonus、教皇 opinion 双方向 bonus |
| 「改革の時だ！」 | 上位 10% 都市の人口 10% をカルヴァン派改宗 |

`[src: events/DHE/flavor_HUN.txt]`

- カトリック維持なら固有進歩「カトリックの盾」（月間宗教的影響力 +0.1、自国宗教寛容度 +1）
- カルヴァン派転向なら「ハンガリー宗教改革」（国教会権力コスト -20%、自国宗教寛容度 +1）
- どちらでもない宗教なら「多宗教の地」（異端寛容度 +1、異教寛容度 +1）
- 宗教分岐は 3 つの固有進歩のうち 1 つだけ取得可能（排他）

---

## 後半戦略（1500〜1700）

### Mohács 相当の局面とリスク管理

**Mohács 専用ディザスター: 存在しない** — mohacs を全 events ファイルで検索した結果、location 定義のみで、ディザスター・専用イベントは存在しない `[src: events/DHE/ 全ファイル検索 + script verified]`。モハーチ的な大敗北は**通常の戦闘結果**として処理される。

ただし `flavor_hun.150`「[国名]の進出」（破滅イベント）は別途存在し、これがハンガリー最大のゲームオーバー候補である。

**`flavor_hun.150`「[国名]の進出」（1550〜1650）:**

発火条件: HAB が HRE 皇帝 + HUN が TUR 休戦中 + HUN 都市数 < 5 + TUR がカルパティア旧 HUN 領保有。

唯一の選択肢: HUN 全所有地（HAB コア以外）に HAB コアが付与される。

**防止策:**
- TUR との戦争で大敗北しない（戦争継続または有利な講和）
- 都市数を 5 以上維持する
- HAB が HRE 皇帝になる前に友好関係を構築するか、HUN が HRE に加盟する

### HRE / ハプスブルク同君連合ルート

#### ハプスブルク家からの王位請求 CB

`flavor_hab.46`「ハンガリー陥落（HAB 視点）」が 1500-1600 年の間に月 1% で発火しうる。

**発火条件:** HAB-HUN 王家婚姻 + HUN-TUR 休戦 + TUR がカルパティア旧 HUN 領保有 + HAB-HUN PU なし `[src: events/DHE/flavor_HAB.txt + script verified]`

| 選択肢（HAB 視点） | 効果 |
|-------------------|------|
| A（歴史的） | HAB に HUN への `cb_claim_throne` 付与 + 近隣諸国から `hab_claimed_hungary` opinion 修正 |
| B | 名声 mild_penalty のみ |

**HUN 側の対応:**
- このイベントが発火した時点で HAB は`cb_claim_throne` を保持している
- `cb_claim_throne` の発動条件: 君主制同士、対象請求者が存在・生存、**対象請求者が現君主でない**こと `[src: casus_belli/claim_throne.txt + script verified]`
- 対抗策: HAB との同盟・PU 締結・または HRE 加盟で攻撃の大義を消す

#### cb_claim_throne（王位請求 CB）の制約

`[src: casus_belli/claim_throne.txt + script verified]`

| 項目 | 値 |
|------|-----|
| 発動可否 | 君主制同士、請求者が存在・生存、**請求者が現君主でない**こと（制約は `not = { this = scope:target.ruler }` として script verified。1.2 で追加された変更点であることはコミュニティ知見）`[src: casus_belli/claim_throne.txt + script verified（制約の存在）]` |
| 戦争目標 | take_capital_claim_throne（conquer_cost = 2、antagonism = 0.25） |
| AI 優先度 | +100 |

#### 同君連合（union）メカニクス

`[src: international_organizations/union.txt + laws/40_personal_unions.txt + script verified]`

| 項目 | 値 |
|------|-----|
| 最低加盟年数 | 50 年 |
| Opinion 閾値 | 未確認（コミュニティ知見：高い Opinion が PU 成立の前提とされるが数値はスクリプト未確認） |
| 統合前提 | `integrated_in_union` 変数 + `union_integration_level` 達成 |
| 統合レベル変動 | `union_senior_succession_law` 制定で +1、廃止で -1 |
| IO 自動解散 | 構成員 2 名未満 |
| 関連 CB | `cb_union_independence`（junior が独立宣戦）、`cb_union_war_for_seniority`（junior が seniority 逆転宣戦） |

#### Imperial Diet と HRE への参加

HUN が HRE に加盟する（またはハプスブルク同君連合後に HRE の一部となる）場合、以下の HRE メカニクスが関与する。

`[src: international_organizations/hre.txt + laws/20_hre.txt + script verified]`

**Imperial Diet（帝国議会）4 段階:**

| 段階 | 構成 |
|------|------|
| 1: `hre_court_assembly` | 選帝侯・大司教選帝侯・自由都市・Primas Germaniae |
| 2: `hre_early_imperial_diet` | +帝国諸侯 |
| 3: `hre_bi_camerial_imperial_diet` | +Legatus Natus・帝国高位聖職者 |
| 4: `hre_tri_camerial_imperial_diet` | +自由都市（完全三院制） |

一方通行（前段階に戻れない）。

**Golden Bull と離脱条件:**

- Golden Bull 制定 → `hre_enable_leave_hre_peace_treaty = yes` → 平和条約経由のみ離脱可
- Golden Bull 未制定 + 1400 年超 → 離脱可（`hre.txt:284-285`）`[src: international_organizations/hre.txt + script verified]`
- 皇帝空位時 `LONG_IMPERIAL_REGENCY_YEARS` 経過で離脱可

**Imperial Armory（帝国兵器庫）:**

`[src: building_types/hre_buildings.txt + script verified]`

| 項目 | 値 |
|------|-----|
| 建設コスト | gold = 500 |
| 建設条件 | 皇帝のみ・HRE 所属地のみ・`military_contribution` 法必須 |
| 自国版効果 | local_manpower +0.0025 + 連隊補充可 |
| 外国版効果 | manpower_to_building_owner +0.005 |
| HRE 離脱時 | 自動削除 |

### オーストリア＝ハンガリー逆転ルート

#### 新首都ウィーン（`flavor_hun.550`）

ウィーン占領後にハンガリーがオーストリアを逆吸収する歴史的逆転劇への道。

**発火条件（1470-1490、月 2%）:** ウィーン所有・支配・コア + 非首都 + HRE 存在 `[src: events/DHE/flavor_HUN.txt + script verified]`

| 選択肢 | 効果 |
|--------|------|
| A「ウィーンへ移転」 | 首都をウィーンへ移転、`new_hungarian_capital` modifier 10 年 |
| B「ブダ死守」 | 現首都に development_mild + prosperity_severe bonus |

**推奨:** A（コミュニティ知見）。史実マチャーシュ 1 世のウィーン占領（1485）と一致。ウィーンを首都とすることで HRE 中核国としての地位を確立できる。

#### オーストリア貴族の反乱（`flavor_hun.480`）

HUN がオーストリアを統合した後、1700-1836 年の間に発火しうる。

**発火条件:** HAB が存在しない + オーストリア地域に HUN 所有地 + danube_bavarian 文化 Pop 平均満足度 < 50% `[src: events/DHE/flavor_HUN.txt + script verified]`

| 選択肢 | 効果 |
|--------|------|
| A | 中央集権→分権寄り、政府権力 severe_bonus |
| B | HAB を cores から再建 + HUN の vassal 化（HAB 再建ルート） |

**推奨:** 選択肢 A（コミュニティ知見）。HAB を再建（選択肢 B）すると自身が vassal 化する逆転シナリオになるため、通常プレイでは避ける。

### 首都避難計画

`flavor_hun.580`：ブダが圧迫される最悪のシナリオへの備え。

**発火条件（1526-1600、月 10%）:** ブダ首都・コア・支配 + ブダ隣接にオスマン + ブラチスラバ自国コア・支配・非首都 `[src: events/DHE/flavor_HUN.txt + script verified]`

| 選択肢 | 効果 |
|--------|------|
| A「ブラチスラバへ移転」 | 首都移転、ブラチスラバ rural→town 格上げ or dev/prosperity bonus |
| B「ブダ死守」 | 安定度 weak_bonus、ブダに dev/prosperity bonus |

**推奨:** オスマンに圧倒されている状況なら A を選択して国家の継続を優先する（コミュニティ知見）。ブダを死守できる戦力があるなら B も選択肢。

### 吸血鬼イベントと聖冠

#### 吸血鬼（`flavor_hun.140`）

1600-1650 年の間に月 5% で発火（fire_only_once）。trigger: 君主制 + 自国ハンガリー文化の成人女性が ruler/consort/heir でない状態で存在。史実のバートリ・エルジェーベト（Báthory Erzsébet）に対応するフレーバーイベント。

`[src: events/DHE/flavor_HUN.txt + script verified]`

| 選択肢 | 効果 |
|--------|------|
| A「止めろ」 | 貴族満足度 mild_penalty（`estate_satisfaction_mild_penalty`）、対象キャラクター処刑（execution） |
| B「ただの噂だ」 | 農民満足度 mild_penalty（`estate_satisfaction_mild_penalty`） |

**推奨:** 選択肢 A（コミュニティ知見）。農民満足度ペナルティより貴族満足度ペナルティの方が管理しやすい状況が多い。

#### 歪んだ聖冠と壊れた伝統

`[src: events/DHE/flavor_HUN.txt + script verified]`

- `flavor_hun.430` 歪んだ聖冠（trigger: 1600 年以降・君主制・`holy_crown_of_hungary` 所有）: 選択肢 A（Gold -5・正統性 weak_penalty）/ 選択肢 B（Gold -10・威信 weak_bonus・正統性 weak_penalty）/ 選択肢 C（聖冠損傷・威信 severe_penalty・正統性 weak_penalty）/ 選択肢 D（cruel/malevolent 君主のみ：内閣要員処刑・聖冠損傷）
- `flavor_hun.440` 壊れた伝統（trigger: 聖冠を自国が所有していない + 歪み/通常のいずれかが他国に）: 唯一の選択肢 → 聖冠の所在地へ征服 CB 付与・貴族満足度 extreme_penalty・正統性 ultimate_penalty

---

## 軍事ドクトリン

### 概論「騎兵王国」

ハンガリーは**騎兵王国**である。固有進歩「複合弓軽騎兵」（`hun_composite_light_cavalry`）により Age 1 から `army_light_cavalry_power +0.20`（騎兵戦力 +20%）が付与される `[src: advances/country_HUN.txt + script verified]`。これがハンガリー軍の根幹であり、序盤から騎兵比率を高く保つことが基本方針。

中盤以降は**黒軍（a_the_black_army）**と**ハンガリー・フサール（a_hungarian_hussars）**という 2 つの固有ユニットが加わり、歩兵・騎兵の両軸で精強な軍を形成できる。後半は**ハイドゥク（a_hajduk）**が加わるが、これは HUN 専用ではなく地形特化型の補助戦力と位置付ける。

### 複合弓軽騎兵（hun_composite_light_cavalry）—— Age 1 からの騎兵主力化

`[src: advances/country_HUN.txt + script verified]`

- 解禁 Advance: `hun_composite_light_cavalry`（Age 1、`feudalism_advance` 要）
- 効果: `army_light_cavalry_power +0.20`（全 Light Cavalry ユニットに +20%）
- 開始時点から騎兵主力化の正当性がある

Light Cavalry のベース数値（参考）:

| 項目 | 値 | src |
|------|-----|-----|
| 移動速度 | 3.0 | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |
| 戦闘速度 | 5 | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |
| initiative | 5 | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |
| flanking_ability | 2.1（210%） | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |
| damage_taken | 0.75（被ダメ -25%） | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |
| is_garrison | なし（要塞駐屯不可） | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |

### 黒軍（a_the_black_army）—— Heavy Infantry の主柱

`[src: unit_types/1_uniques_for_age_3_discovery.txt + script verified]`

黒軍（Black Army）はマティアス・コルヴィヌス王が創設した精鋭常備軍の象徴。Age 3 解禁で取得できる EU5 最強クラスの Heavy Infantry ユニット。

| 項目 | 値 |
|------|-----|
| 系統 | Heavy Infantry（copy_from = a_age_3_discovery_heavy_infantry） |
| 解禁 | Age 3（`hun_found_the_black_army` Advance が必要） |
| build_time_modifier | 0.5（建設時間 **50% 短縮**） |
| strength_damage_taken | -0.10（体力ダメージ **10% 軽減**） |
| 建設可能地域 | `dominant_culture = culture:hungarian`（**ハンガリー文化圏のみ**） |
| ベース max_strength | 1.5 |
| ベース combat_power | 1.0 |
| is_garrison | **yes**（要塞駐屯可能） |

**Heavy Infantry ベース数値（参考）:**

| 項目 | 値 | src |
|------|-----|-----|
| 移動速度 | 2.0 | `[src: unit_categories/01_army_heavy_infantry.txt + script verified]` |
| initiative | 1 | `[src: unit_categories/01_army_heavy_infantry.txt + script verified]` |
| is_garrison | **yes** | `[src: unit_categories/01_army_heavy_infantry.txt + script verified]` |

**運用方針:**

- 建設時間 50% 短縮により、素早く国境要塞・都市の守備を強化できる
- ハンガリー文化地にしか建設できないため、コア領土の要塞守備を担当させる
- is_garrison = yes で要塞駐屯可能。1.2 で Light Infantry が要塞駐屯不可になった環境では、黒軍の価値がさらに上昇する
- 体力ダメージ軽減 -10% で長期包囲戦・消耗戦に強い
- **1.3 で陸軍 goods 需要が約 2 倍に増加**。goods 消費の重い黒軍を中心とした常備軍規模は、goods 供給（産地確保・交易）とセットで再設計する必要がある（コミュニティ知見：公式パッチノート由来・スクリプト未確認）

### ハンガリー・フサール（a_hungarian_hussars）—— Light Cavalry

`[src: unit_types/1_uniques_for_age_4_reformation.txt + script verified]`

歴史的なハンガリー・フサールを体現する Age 4 の精鋭軽騎兵。**旧版は「Heavy Cavalry」と誤記していたが、実スクリプトは `copy_from = a_age_4_reformation_light_cavalry` で Light Cavalry 系統**（訂正）。貴族 Pop に依存するため、貴族階級の満足度・人口管理が重要。

| 項目 | 値 |
|------|-----|
| 系統 | Light Cavalry（copy_from = a_age_4_reformation_light_cavalry） |
| 解禁 | Age 4（`hun_hungarian_hussars` Advance が必要） |
| initiative | **2**（Light Cavalry カテゴリ base 5 を絶対値上書き＝**低下**。旧記載「base2+2=4」は誤り） |
| impact（進軍コスト） | flatland -0.25、mountains -0.25（**平地・山岳での進軍コスト 25% 減**） |
| mercenaries_per_location | nobles pop × 0.3（**貴族 Pop 依存**） |
| ベース max_strength | 0.8 |
| ベース combat_power | 4.0 |
| is_garrison | なし（Light Cavalry カテゴリ上、要塞駐屯不可。旧記載「Heavy Cavalryカテゴリ上」は誤り） |

> **注意:** `impact` のマイナス値は**進軍コスト削減**（= 移動しやすい）を意味し、戦闘力ボーナスとは別。フサールは平地・山岳でより機動的に動ける `[src: unit_types/1_uniques_for_age_4_reformation.txt + script verified]`。

**Light Cavalry ベース数値（参考。フサールの initiative は上記の通り 2 に上書きされる点に注意）:**

| 項目 | 値 | src |
|------|-----|-----|
| 移動速度 | 3.0 | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |
| initiative（カテゴリ base、フサールは 2 に上書き） | 5 | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |
| flanking_ability | 2.1 | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |
| damage_taken | 0.75（被ダメ -25%） | `[src: unit_categories/02_army_light_cavalry.txt + script verified]` |

**運用方針:**

- combat_power 4.0 は高水準。正面会戦での騎兵突撃に最適
- 貴族 Pop に依存するため、進歩「農民の自由の制限」（`hun_curtailed_peasantry`）等で貴族 Pop を圧迫しすぎないよう注意
- 要塞駐屯は不可（Light Cavalry はカテゴリ上 is_garrison なし）
- 平地・山岳での機動コスト削減を活かし、バルカンの山岳地帯でも追撃戦をこなせる。initiative が Light Cavalry base(5)より低い(2)ため、先手を取る戦術より機動力・追撃戦での運用が向く

### ハイドゥク（a_hajduk）—— Light Infantry

`[src: unit_types/1_uniques_for_age_5_absolutism.txt + script verified]`

Age 5 解禁の地形特化型軽装歩兵。重要注意点が 2 点ある。

| 項目 | 値 |
|------|-----|
| 系統 | Light Infantry（copy_from = a_age_5_absolutism_light_infantry）→ **要塞駐屯不可** |
| 解禁経路 | **HUN 固有 Advance ではない**。`balkan_hajduks`（`advances/region_balkans.txt` 地域 Advance）経由。バルカン・カルパティア圏の首都国共通で取得可能（POL・SER・ワラキア等も対象） |
| initiative | カテゴリ base 5 に +2 = 計 **7** |
| strength_damage_taken | +0.10（体力ダメージ **+10%**、平地戦闘では脆い） |
| combat 補正 | hills +0.15、plateau +0.15、mountains +0.10 |
| ベース max_strength | 2.5 |
| ベース combat_power | 2.25 |

`[src: advances/region_balkans.txt + script verified]`

> **注意点 1:** ハイドゥクは Light Infantry 系統のため**要塞駐屯不可**（is_garrison なし）。1.2 の要塞守備強化文脈では、要塞守備には黒軍（Heavy Infantry）を使うこと。
>
> **注意点 2:** `balkan_hajduks` は HUN 専用 Advance ではない。バルカン地域の複数国家も取得可能。

**Light Infantry ベース数値（参考）:**

| 項目 | 値 | src |
|------|-----|-----|
| 移動速度 | 2.5 | `[src: unit_categories/00_army_light_infantry.txt + script verified]` |
| initiative | 5 | `[src: unit_categories/00_army_light_infantry.txt + script verified]` |
| flanking_ability | 1.1 | `[src: unit_categories/00_army_light_infantry.txt + script verified]` |
| is_garrison | なし | `[src: unit_categories/00_army_light_infantry.txt + script verified]` |

**運用方針:**

- 丘陵・高原・山岳地形（バルカン内陸・トランシルヴァニア・スロバキア山岳地帯）での攻略戦に特化
- 平地では strength_damage_taken +10% で脆い。平地会戦ではフサール・黒軍を主力に回す
- initiative 7 という高い値で先手が取りやすい

### HUN 軍の推奨編成（時期別）

`[src: 中間データ A-7 ベース。兵科比率はコミュニティ知見]`

| 時期 | 重装歩兵（Heavy Inf） | 軽装歩兵（Light Inf） | 軽装騎兵（Light Cav） | 砲兵 | 備考 |
|------|---------------------|---------------------|---------------------|------|------|
| 序盤（Age 1-2） | 30-40% | 0%（ハイドゥクは Age 5 解禁のため未投入） | 40-60% | 10-20% | 複合弓軽騎兵ボーナスを最大活用 |
| 中盤（Age 3-4） | 30-40%（黒軍主体） | 0%（ハイドゥクは Age 5 解禁のため未投入） | 40-60%（フサール主体） | 10-20% | 黒軍で要塞守備、フサールで機動戦 |
| 後半（Age 5-6） | 25-35%（黒軍） | 20-25%（ハイドゥク） | 20-30%（フサール） | 15-25% | ハイドゥクは山岳・丘陵戦のみ投入 |

### 兵科別の地形適性

| 兵科 / 地形 | 平原 | 丘陵 | 山岳 | 湿地 | 備考 |
|------------|------|------|------|------|------|
| 黒軍（Heavy Inf） | ○ | △ | △ | × | 要塞守備に最適。移動速度が低い |
| フサール（Light Cav） | ◎ | △（コスト減） | △（コスト減） | × | 進軍コスト減で山岳機動に対応 |
| ハイドゥク（Light Inf） | △（脆い） | ◎ | ◎ | ○ | 丘陵・高原・山岳での攻略戦に特化 |
| 複合弓軽騎兵（Light Cav） | ◎ | ○ | △ | × | 序盤の機動主力。+20% ボーナスが常時有効 |

`（コミュニティ知見：地形適性の○×評価は定性的）`

### Combined Arms（統合軍備）

`[src: auto_modifiers/country.txt + script verified]`

| 項目 | 値 |
|------|-----|
| 最小発動閾値 | 10%（各兵科 10% 以上で発動） |
| 最大ボーナス閾値 | 50%（一兵科 50% 超でボーナス上限ヒット） |
| ボーナス（Age 1-3） | 兵科ごと +2.5%（3 兵科で最大 7.5%） |
| ボーナス（Age 4-5） | 兵科ごと +3.5%（3 兵科で最大 10.5%） |
| ボーナス（Age 6） | 兵科ごと +4.5%（3 兵科で最大 13.5%） |

**ハンガリーでの適用:**

騎兵偏重になりがちだが、歩兵・砲兵をそれぞれ 10% 以上保てば Combined Arms ボーナスが発動する。黒軍（Heavy Inf）・フサール（Light Cav）・砲兵を 10% 以上ずつ混ぜた編成でボーナスを確保する（コミュニティ知見）。

**Advance での強化:**

- Age 4 Advance `combined_arms_advance_reformation`: `combined_bonus_per_type = 0.01`（Advance 取得後の合計: 兵科ごと +3.5%） `[src: advances/0_age_of_reformation.txt + script verified]`
- Age 6 Advance `combined_arms_advance_revolutions`: `combined_bonus_per_type = 0.01`（Advance 取得後の合計: 兵科ごと +4.5%） `[src: advances/0_age_of_revolutions.txt + script verified]`

### 黒軍政策（black_army_policy）—— HUN 固有軍事政策

`[src: laws/01_military_laws.txt + script verified]`

| 項目 | 値 |
|------|-----|
| 発動条件 | ハンガリー文化（`culture = culture:hungarian`） |
| 解禁時代 | Age 3 以降（Age 1・2 では利用不可） |
| 効果 | discipline +0.025（規律 +2.5%） |
| 追加効果 | mercenary_maintenance_efficiency +0.1（傭兵維持費効率 +10%）、monthly_towards_quality（質方向へ毎月移動） |
| 階級嗜好 | burghers_estate（市民階級） |
| 更新期間 | 2 年ごと |

**運用:** Age 3 で黒軍解禁と同時に `black_army_policy` を採択する。discipline +2.5% は全軍の戦闘力に直結する重要なボーナス。

### 召集軍（Levy）の運用

| 項目 | 召集軍 | 正規（Regulars） |
|------|--------|------------------|
| コスト | 無料 | 高い |
| 補充 | 戦闘中は増援しない | 人的資源（Manpower）から補充 |
| 経験値 | 毎月減少、解散で喪失 | 維持される |
| 後半補正 | 絶対主義・革命時代に +10% | 特になし |

- 序盤は召集軍で数合わせ、中盤以降は正規軍中心へ移行
- 1.1 で貴族召集軍は量が +50% に増えた一方、戦闘効率補正は削除された
- **Noble Levies 君主法**（`nobles_estate_levy_size +0.50`）を採択するとさらに召集量が増加 `[src: laws/00_monarchy.txt + script verified]`

### 傭兵の活用

- 1.2 で傭兵コスト +25%（コミュニティ知見：スクリプト未確認）。傭兵に依存した戦略は長期コストが高くなる
- 黒軍政策（`black_army_policy`）の `mercenary_maintenance_efficiency +0.1` で傭兵維持費を 10% 削減できる `[src: laws/01_military_laws.txt + script verified]`
- 緊急の兵力補填や特殊な戦争（2 正面戦争時の片方への増援など）に傭兵を活用し、傭兵単独での長期運用は避ける（コミュニティ知見）

---

## 外交・同盟

### 必須同盟

| 国家 | 理由 |
|------|------|
| ポーランド | 同君連合候補。王室間の婚姻＋関係改善を最優先 |
| オーストリア | 対オスマン共闘。HRE 加盟後は特に重要 |

### 推奨関係

| 国家 | 理由 |
|------|------|
| ボヘミア | 西方の安全確保。友好関係なら西を無視できる。イベント「カトリック信者からの支援要請」（`flavor_hun.180`）でボヘミア王位を得るルートもある |
| ヴェネツィア | 交易パートナー。序盤の物資輸入で制度伝播を加速 |

### 外交方針

- **君主力（Crown Power）**を高めて中央集権化を進める
- 1.1 で「統治者を優遇」の君主力補正が 20% → 33% に強化され、序盤の君主力確保がさらに重要に
- 王室間の婚姻は早期に結び後継者を確保する（王朝断絶を防ぐ）
- 摂政期間中は宣戦できないため、重要な戦争の直前に王が高齢なら開戦を急ぐ

---

## 内政・経済

### インフラ建設の優先順位

| 順位 | 建設物 | ゲーム内名称 | 理由 |
|------|--------|-------------|------|
| 1 | 市場 | Marketplace | 交易収入の基盤 |
| 2 | 街道 | Road | 近接ペナルティ軽減 |
| 3 | 橋 | Bridge | ハンガリーの湖が近接障壁。必須インフラ |
| 4 | 製材所 | Lumber Mill | 建設資材の確保 |
| 5 | 病院 | Hospital | 黒死病対策（1340年代までに建設） |

> **1.3 で建物維持費が時間経過で逓増**（1 世紀で約 +50%）する。要塞網（ヴェグヴァール体制）を厚く積む防衛戦略は長期的に維持費が増すため、収入とのバランスを意識する（コミュニティ知見：公式パッチノート由来・スクリプト未確認）。

### 階級（Estate）管理

| 階級 | 注意点 |
|------|--------|
| 貴族 | 騎兵ボーナスの源泉。満足度を維持しつつ、権力が暴走しないよう調整 |
| 聖職者 | 宗教改革前はカトリック維持に貢献。改宗するなら権力を抑制 |
| 市民 | 交易収入に貢献。市場建設と連動。黒軍政策との親和性が高い |
| 庶民 | 人口と食料の基盤。課税を上げすぎると農民反乱イベント（`flavor_hun.160`）のリスク増 |

---

## 固有イベント時系列

出典: `events/DHE/flavor_HUN.txt`、`events/DHE/flavor_HUN_SER.txt`

### 序盤（1337〜1400）

| ID | イベント名 | 発火条件 | おすすめ選択肢 | 効果 |
|----|-----------|---------|--------------|------|
| `flavor_hun.330` | [年]年のヴィシェグラード会議 | 1337-1370（月 75%、POL カジミェシュ 3 世 + HUN カーロイ・ロベルト） | 「あの合意を成文化しよう」（コミュニティ知見） | POL に hun.331 送信、PU pact 契機 |
| `flavor_hun.340` | [国名]の金 | 1340-1390（月 100%、カーロイ・ロベルト没後 + gold_export_ban 有効） | 「禁令を延長しろ」（コミュニティ知見：長期的な内需優先） | Gold +2 scale |
| `flavor_hun.350` | 1222年の金印勅書 | 1340-1440（月 1%、君主 adm/dip/mil 全て < 50 + 未付与） | 状況次第（コミュニティ知見） | 「復活させよう」で貴族特権 `golden_bull_of_1222` 付与・貴族満足度 mild_bonus vs 「拒否」で安定度・統治力ペナルティ |
| `flavor_hun.370` | 聖ゲオルギウス騎士団 | 1337-1437 | 「騎士団を拡大させるのだ！」（コミュニティ知見） | 軍事ボーナス（未確認） |
| `flavor_hun.400` | ペーチの大学 | 1350-1400 | 「これはわが国の利益となるだろう……」（コミュニティ知見） | 文化・教育ボーナス（未確認） |
| `flavor_hun.600` | ボスニア問題 | 1340-1500 | 外交優先（コミュニティ知見） | （未確認） |
| `flavor_hun.460` | 彩飾年代記 | 1358-1375 | 受諾推奨（コミュニティ知見） | 文化イベント（未確認） |
| `flavor_hun.360` | ヴラフ法 | 1337-1600 | 状況次第（コミュニティ知見） | 文化・民族管理（未確認） |
### 中盤（1400〜1550）

| ID | イベント名 | 発火条件 | おすすめ選択肢 | 効果 |
|----|-----------|---------|--------------|------|
| `flavor_hun.1` | ヤーノシュ・フニャディ登用 | 1430-1443（月 5%、fire_only_once） | 「採用」 | Gold -1 scale、adm 84-94/dip 70-80/mil 90-100 の最高水準将軍候補 `[src: events/DHE/flavor_HUN.txt + script verified]` |
| `flavor_hun.2` | [年]年の議会 | 1444-1470（月 50%、議会 + 摂政 + 戦争 + フニャディ存命） | 「フニャディを摂政に」（コミュニティ知見） | 軍事力強化（未確認） |
| `flavor_hun.110` | マティアス・コルヴィヌスの改革 | 1466-1470（月 10%、ハンガリアディ家君主）`[src: events/DHE/flavor_HUN.txt]` | 「行政改革」（コミュニティ知見） | 中央集権化（未確認） |
| `flavor_hun.120` | アカデミア・イストロポリターナ | 1465-1470 | 「これはわが国の利益となるだろう……」（コミュニティ知見） | 威信＋大学建設（未確認） |
| `flavor_hun.130` | ブダの印刷所 | 1473-1500 | 「素晴らしい！」（コミュニティ知見） | 芸術作品「クロニカ・ハンガロルム」生成（品質 85）（未確認） |
| `flavor_hun.200` | [王名]の軍隊 | 1455-1470（月 5%、摂政なし） | 唯一選択肢 | 質・陸・攻勢寄りに Societal Value 移動（黒軍前身）`[src: events/DHE/flavor_HUN.txt]` |
| `flavor_hun.210` | ハンガリーの要（ベオグラード） | 1450-1500（ベオグラード + TUR 隣接 + 要塞有り）`[src: events/DHE/flavor_HUN.txt]` | 「国費をさらに投入しよう」（コミュニティ知見） | vegvar_system 解禁（未確認） |
| `flavor_hun.220` | セルビア陥落 | 1337-1600（SER 消滅後） | 唯一選択肢 | TUR セルビア文化都市からの移民（amount 0.2、20 年）`[src: events/DHE/flavor_HUN.txt]` |
| `flavor_hun.180` | ボヘミア・カトリックからの支援要請 | 連鎖発火 | 「デウス・ウルト」（コミュニティ知見） | BOH 支援要請 + ズノイモ等に征服 CB（未確認） |
| `flavor_hun.410` | ドラゴン騎士団 | 1400-1450（月 5%、騎士団法律 + バルカンにオスマン文化イスラム 5 都市以上）`[src: events/DHE/flavor_HUN.txt]` | 「いまこそドラゴン騎士団を結成するのだ」（コミュニティ知見） | Gold -6、対オスマン同盟強化（未確認） |
| `flavor_hun.510` | ビブリオテカ・コルヴィニアーナ | 1450-1490（月 2%、fire_only_once） | 「素晴らしい！」（コミュニティ知見） | 首都に bibliotheca_corviniana 建物（未確認） |
| `flavor_hun.520` | ブラン城 | 1377-1420（月 2%、ブラショフ所有 + castle 未建設） | 「素晴らしい案だ！」（コミュニティ知見） | ブラショフに castle 建設（50% off）（未確認） |
| `flavor_hun.550` | 新首都ウィーン | 1470-1490（月 2%、ウィーン占領・HRE 存在）`[src: events/DHE/flavor_HUN.txt + script verified]` | オーストリア逆転ルートなら「素晴らしい案だ！」（コミュニティ知見） | （未確認） |
| `flavor_hun.560` | 三部法書 | 1517-1530 | 状況次第（コミュニティ知見） | 法律イベント（未確認） |
| `flavor_hun.450` | ブダ城拡張 | 1430-1460 | 状況次第（コミュニティ知見） | 建設イベント（未確認） |
| `flavor_hun.470` | スラブ人特権令 | 1381-1391 | 状況次第（コミュニティ知見） | 民族管理（未確認） |
| `flavor_hun.490` | バラージュ・マジャル | 1435-1450（黒軍前提） | 状況次第（コミュニティ知見） | 人物イベント（未確認） |
| `flavor_hun.500` | パール・キニジ | 1460-1470（黒軍前提） | 状況次第（コミュニティ知見） | 人物イベント（未確認） |
| `flavor_hun.590` | ユサールの起源 | 1400-1500（`hun_composite_light_cavalry` 取得後） | 状況次第（コミュニティ知見） | 軍事・フレーバー（未確認） |
| `flavor_hun.170` | バコーツ・タマーシュ | 1490-1520 | 状況次第（コミュニティ知見） | 外交イベント（未確認） |
| `flavor_hun.190` | 北ハンガリー地方に盗賊横行 | 1430-1440 代（中盤） | 「盗賊どもを叩き潰せ！」（コミュニティ知見） | 治安回復（未確認） |

### 中盤〜終盤（1500〜）

| ID | イベント名 | 発火条件 | おすすめ選択肢 | 効果 |
|----|-----------|---------|--------------|------|
| `flavor_hun.230` | [デブレツェン]の教会会議 | 1560-1570（カトリック + カルヴァン派人口 > 0）`[src: events/DHE/flavor_HUN.txt]` | 宗教方針次第（[宗教改革への対応](#宗教改革への対応1500-年前後)を参照） | （未確認） |
| `flavor_hun.270` | エルデーディ・タマーシュ | 1583-1610（月 10%、ザグレブ所有、fire_only_once） | 唯一選択肢 | adm 80/dip 80/mil 83 のキャラクター採用 `[src: events/DHE/flavor_HUN.txt + script verified]` |
| `flavor_hun.240` | トマーシュ・ナーダシュディ | 1530-1555 | 状況次第（コミュニティ知見） | 人物イベント（未確認） |
| `flavor_hun.160` | ハンガリーの農民反乱 | 1450-1650（`hun_power_to_magnates` 保持 + 安定度 < -20。中盤〜終盤にまたがって発火）`[src: events/DHE/flavor_HUN.txt]` | 安定度を整えておく。「反乱分子のクズどもめ！」（コミュニティ知見） | 鎮圧（未確認） |
| `flavor_hun.540` | トランシルヴァニア改革 | 1530-1550 | 状況次第（コミュニティ知見） | 宗教イベント（未確認） |
| `flavor_hun.140` | [国名]の吸血鬼 | 1600-1650（月 5%、fire_only_once） | 「止めろ」（農民ペナルティより管理しやすい） | 貴族満足度 mild_penalty・対象処刑 `[src: events/DHE/flavor_HUN.txt + script verified]` |
| `flavor_hun.150` | [国名]の進出 | 1550-1650（HAB が HRE 皇帝 + HUN 都市数 < 5 + TUR 休戦 + TUR がカルパティア旧 HUN 領保有） | **発生させないのが最善**（オスマンに敗北しない、都市 5 以上維持） | （未確認）`[src: events/DHE/flavor_HUN.txt + script verified]` |
| `flavor_hun.320` | [王名]の絶対的統治 | 後半 | 「国家は[王名]の支配下にある」（コミュニティ知見） | 中央集権化の推進（未確認） |
| `flavor_hun.580` | 首都避難計画 | 1526-1600（ブダ首都 + ブダ隣接オスマン + ブラチスラバ保有）`[src: events/DHE/flavor_HUN.txt + script verified]` | オスマン圧迫中なら「ブラチスラバへ」（コミュニティ知見） | （未確認） |
| `flavor_hun.430` | 歪んだ聖冠 | 1600 年以降（月不定期、君主制 + 聖冠所有） | 選択肢 A 推奨。選択肢 C/D は聖冠損傷で追加ペナルティ | Gold -5・正統性 weak_penalty（選択肢 A） `[src: events/DHE/flavor_HUN.txt + script verified]` |
| `flavor_hun.440` | 壊れた伝統 | 聖冠喪失後（常時 trigger） | 唯一選択肢 | 聖冠所在地への征服 CB 付与・貴族満足度 extreme_penalty・正統性 ultimate_penalty `[src: events/DHE/flavor_HUN.txt + script verified]` |
| `flavor_hun.300` | 北ハンガリー地方の都市同盟 | 中盤 | 「彼らの特権を守ってやろう」（コミュニティ知見） | 鉱山都市の経済安定（未確認） |
| `flavor_hun.480` | オーストリア貴族の反乱 | 1700-1836（HAB 消滅後、オーストリア領保有）`[src: events/DHE/flavor_HUN.txt + script verified]` | 「中央集権路線」推奨（コミュニティ知見） | （未確認） |
| `flavor_hun.530` | スロヴァキア民族覚醒 | 1750-1810 | 状況次第（コミュニティ知見） | 民族管理（未確認） |
| `flavor_hun.570` | アダム・フランティシェク・コッラール | 1760-1780 | 状況次第（コミュニティ知見） | 人物イベント（未確認） |

### 連鎖イベント（参考）

| ID | イベント名 | 発火条件 | おすすめ選択肢 | 効果 |
|----|-----------|---------|--------------|------|
| `flavor_hun.181` | BOH 通知 | hun.180 の連鎖 | — | ボヘミア支援連鎖 |
| `flavor_hun.331/.332` | ヴィシェグラード第 2・3 回 | hun.330 の連鎖 | — | ヴィシェグラード合意の継続交渉（未確認） |
| `flavor_hun.18` | ヴィシェグラード拒否 | POL が会議を拒否した場合 | — | （未確認） |
| `flavor_hun.411` | ドラゴン騎士団参加要請 | hun.410 の連鎖 | — | 周辺国への参加打診 |
| `flavor_hun.421/.422` | 馬上槍試合 | 中盤フレーバー連鎖 | — | （未確認） |
| `flavor_hun_ser.1000` | ベオグラードの提案（SER 視点） | SER 連動 | — | （未確認） |
| `flavor_hun_ser.1001` | ベオグラードの提案（HUN 視点） | SER 連動 | — | （未確認） |
| `flavor_hun_ser.1002` | ポジティブ応答 | SER 連動 | — | （未確認） |
| `flavor_hun_ser.1003` | ネガティブ応答 | SER 連動 | — | （未確認） |

---

## 固有進歩（Advance）

出典: `advances/country_HUN.txt`、`advances_l_japanese.yml`（スクリプト検証済み）

### 伝統の時代

| 進歩名 | ID | 効果 | requires |
|--------|----|------|---------|
| 複合弓軽騎兵 | `hun_composite_light_cavalry` | `army_light_cavalry_power +0.20`（騎兵戦力 +20%） | `feudalism_advance` |
| 城郭戦士 | `hun_castle_warriors` | `levy_recovery_modifier +0.10`、`global_levy_recruitment_speed_modifier +0.33` `[src: advances/country_HUN.txt + script verified]` | `hun_composite_light_cavalry` |

### ルネサンスの時代

| 進歩名 | ID | 効果 |
|--------|----|------|
| 多文化の地 | `hun_multi_culturalism` | 受容文化枠 +2、受容文化追加コスト -10% |
| ルネサンス君主 | `hun_renaissance_knowledge` | 芸術家給与 -20%、制度伝播速度 +20% |

### 大航海の時代

| 進歩名 | ID | 効果 |
|--------|----|------|
| 黒軍の設立 | `hun_found_the_black_army` | ユニット「黒軍（a_the_black_army）」を解放 `[src: advances/country_HUN.txt + script verified]` |
| 貨幣制度の改革 | `hun_reformed_coinage` | 月間インフレ -0.001 |

### 宗教改革の時代

| 進歩名 | ID | 効果 | 条件 |
|--------|----|------|------|
| キリスト教徒の防波堤 | `hun_bulwark_of_christianity` | `global_manpower_modifier +0.10`（人的資源 +10%） | なし |
| ハンガリー・フサール | `hun_hungarian_hussars` | ユニット「ハンガリー・フサール（a_hungarian_hussars）」を解放 `[src: advances/country_HUN.txt + script verified]` | `unlock_pistoleers_advance` |
| ハンガリー宗教改革 | `hun_hungarian_reformation` | 国教会権力コスト -20%、自国宗教寛容度 +1 | カルヴァン派/ルター派/英国国教会/ロラード派/フス派 |
| カトリックの盾 | `hun_the_catholic_shield` | 月間宗教的影響力 +0.1、自国宗教寛容度 +1 | カトリック |
| 多宗教の地 | `hun_realm_of_many_religions` | 異端寛容度 +1、異教寛容度 +1 | 上記いずれでもない |

> 宗教改革の 3 進歩（宗教改革/カトリックの盾/多宗教の地）は排他。宗教選択で 1 つだけ取得可能。

### 絶対主義の時代

| 進歩名 | ID | 効果 |
|--------|----|------|
| 農民の自由の制限 | `hun_curtailed_peasantry` | 庶民最大課税 +0.1、RGO（資源採取）規模 +20% |
| 軍事戦術の革命 | `hun_revolutionized_military_tactics` | `possible_frontage_modifier +0.10`（戦力前線幅 +10%）`[src: advances/country_HUN.txt + script verified]` |

### 革命の時代

| 進歩名 | ID | 効果 |
|--------|----|------|
| 町への支援 | `hun_strengthened_towns` | 都市望ましい人口 +0.5、貴族権力 -50% |
| ハンガリー人の団結 | `hun_hungarian_unity` | `land_morale_modifier +0.15`（陸軍士気 +15%。旧記載+10%は誤り）`[src: advances/country_HUN.txt + script verified]` |

---

## アドバンス取得ロードマップ

`[src: advances/country_HUN.txt + script verified（ID・効果）、推奨順序はコミュニティ知見]`

### 時代別推奨取得順序

| 時代 | 推奨順序 | 理由 |
|------|---------|------|
| Age 1（伝統の時代） | `hun_composite_light_cavalry` → `hun_castle_warriors` | 騎兵ボーナスが即効性最高。城郭戦士で序盤召集軍の補充を加速 |
| Age 2（ルネサンス） | `hun_renaissance_knowledge` → `hun_multi_culturalism` | 制度伝播 +20% で中欧諸制度の早期取得。多文化は拡張後の文化管理に |
| Age 3（大航海） | `hun_found_the_black_army` → `hun_reformed_coinage` | 黒軍解禁が最優先。貨幣制度は経済安定のため早めに |
| Age 4（宗教改革） | `hun_bulwark_of_christianity` → `hun_hungarian_hussars` → 宗教分岐 1 つ | 人的資源 +10% で大軍維持、フサール解禁で騎兵精鋭化、宗教分岐は方針に応じて選択 |
| Age 5（絶対主義） | `hun_curtailed_peasantry` → `hun_revolutionized_military_tactics` | RGO +20% が庶民収入の底上げに有効。戦力前線幅 +10% で大軍の展開力向上 |
| Age 6（革命） | `hun_hungarian_unity` → `hun_strengthened_towns` | 士気 +15% が最終段階の戦闘力強化の要。都市強化は後回し可 |

### 組合せのポイント

- **Age 1-2 コンボ**: 騎兵ボーナス（Age 1）+ 制度伝播（Age 2）で軍事・内政を両立。序盤の最速進歩
- **Age 3-4 コンボ**: 黒軍（Age 3）+ フサール（Age 4）で歩兵・騎兵の精鋭化が完成。中盤の軍事基盤
- **Age 4 宗教分岐は 1 つだけ**: カトリックのまま vs 宗教改革を決めてから取得する。後戻り不可
- **Age 5 後半 + Age 6 前半**: `hun_revolutionized_military_tactics` の戦力前線幅 +10% は Combined Arms との相乗効果が大きい

---

## よくあるミス

### ハンガリー固有

| NG 行動 | 理由 |
|---------|------|
| ポーランドに宣戦する | 同君連合チャンスが永久に消滅。ポーランドの敵国との同盟にも注意 |
| 橋の建設を後回しにする | 湖による近接ペナルティで内政効率が大幅低下 |
| 歩兵だけの軍を編成する | 騎兵戦力 +20% ボーナスを無駄にしている |
| 従属国を作りすぎる | 辺境伯領化でペナルティ軽減できるが、3 個超は管理負担が重い |
| バルカン整理前にオスマンに挑む | 兵力・経済とも不足。オスマンが他方面で消耗しているタイミングを待つ |
| 病院建設を忘れる | 黒死病で人口壊滅 → 回復に数十年 |
| 君主力を軽視する | 中央集権化が遅れて中盤以降の選択肢が狭まる |
| 宗教改革を無視する | 固有進歩の宗教分岐を逃す。どの宗教にするか事前に方針を決めておく |
| ハイドゥクを国境要塞守備に配置する | Light Infantry 系統のため要塞駐屯不可（1.2 script verified）。守備には黒軍（Heavy Infantry）を使う |
| フニャディ登用を遅らせる | 1430-1443 の発火ウィンドウ内に必ず採用。fire_only_once のため次がない |
| `flavor_hun.150`「[国名]の進出」を放置する | オスマン敗北 + 都市数減少で HAB にコアが付く破滅イベント。TUR 戦での大敗を避け、都市 5 以上を維持する |
| 黒軍をハンガリー文化地以外に建設しようとする | `dominant_culture = culture:hungarian` 制約があり建設不可（script verified） |

### EU5 全般

| NG 行動 | 理由 |
|---------|------|
| 複数戦線で同時に戦う | 兵力分散で各個撃破される |
| 人口の薄い土地に生産施設を先置きする | 労働力不足で稼働しない |
| 新領土の再建を急いで借金を膨らませる | 利息で経済が悪化 |

---

## 用語対照表

> 完全版は [eu5/localization-reference.md](localization-reference.md) を参照。以下はこのガイドで使う用語の抜粋。

| 日本語 | 英語 | 補足 |
|--------|------|------|
| 支配度 | Control | 州の実効支配度 |
| 威信 | Prestige | 国家威信 |
| 正統性 | Legitimacy | 君主の正統性 |
| 君主力 | Crown Power | 君主と階級の力関係 |
| 好感度 | Favor | 同盟国との蓄積関係値 |
| 敵対心 | Antagonism | 拡張に対する反発 |
| 包囲網 | Coalition | 敵対心が高い相手の連合 |
| 評価 | Opinion | 国家間の関係値 |
| 信頼度 | Trust | 同盟の信頼蓄積 |
| 属国 | Vassal | 代表的な従属国形態 |
| 辺境伯領 | March | 軍事特化の従属国形態 |
| 同君連合 | Personal Union | 同じ統治者を戴く連合 |
| 統合 | Integrate | 従属国を自国に吸収 |
| 召集軍 | Levy | 人口から直接動員する軍 |
| 階級 | Estate | 貴族、聖職者、市民、庶民 |
| 内閣 | Cabinet | 高官による統治機構 |
| 進歩 | Advance | 技術・制度・国家固有ツリー |
| 統合軍備 | Combined Arms | 多兵科混成のボーナス `[src: auto_modifiers/country.txt + script verified]` |
| 戦闘幅 | Frontage | 戦場に展開できる部隊幅 |
| 士気 | Morale | 部隊の戦意 |
| 人的資源 | Manpower | 兵士の補充プール |
| 安定度 | Stability | 国家の安定性 |
| 制度 | Institution | 技術伝播の仕組み |
| 市場 | Marketplace | 交易収入を増やす建造物 |
| 病院 | Hospital | 疫病対策の建造物 |
| 街道 | Road | 近接ペナルティを軽減する建造物 |
| 橋 | Bridge | 湖・河川の近接障壁を解消する建造物 |
| 製材所 | Lumber Mill | 建設資材を生産する建造物 |
| 要塞 | Fortification | 防衛施設。支配領域（ZoC）を発生させる |
| 州の請求 | Claims on Province / `cb_conquer_province` | **コア取得後に使える** 汎用征服 CB。EU4 の「Claim」概念とは別物（EU5 は core/integration_level で管理）`[src: casus_belli/conquest.txt + script verified]` |
| 州の請求（根拠なし） | Dubious Claims / `cb_fabricated_conquer_province` | コア取得を前提とする外交ペナルティ付き征服 CB。**EU4 のスパイ「請求権捏造」は EU5 1.2 に存在しない**（`spy_actions/` 自体なし、`scripted_relations/` のスパイ網にも Claim 付与効果なし）`[src: casus_belli/fabricated_conquest.txt + scripted_relations/sow_discontent.txt + script verified]` |
| 敵対国の征服 | Conquer Enemy / `cb_conquer_enemy` | **ライバル相手専用、コア不要** の征服 CB。序盤の主力 `[src: casus_belli/conquer_enemy.txt + script verified]` |
| 不忠な属国 | Disloyal Subject / `cb_disloyal_subject` | 属国が離反した場合の再征服 CB。ボスニア（開始時 HUN 属国）の対応経路 `[src: casus_belli/disloyal_subject.txt + events/DHE/flavor_BOS.txt:28 + script verified]` |
| 王室間の婚姻 | Royal Marriage | 王族同士の婚姻外交 |
| 関係改善 | Improve Relations | 外交アクション |
| RGO | Resource Gathering Operations | 資源採取。ゲーム内でも「RGO」とアルファベット表記 |
| 階級権力 | Estate Power | 各階級の権力値 |
| 黒軍 | Black Army / a_the_black_army | ハンガリー固有 Heavy Infantry ユニット。Age 3 解禁 `[src: unit_types/1_uniques_for_age_3_discovery.txt + script verified]` |
| ハンガリー・フサール | Hungarian Hussars / a_hungarian_hussars | ハンガリー固有 Light Cavalry ユニット（旧記載「Heavy Cavalry」は誤り・訂正済み）。Age 4 解禁 `[src: unit_types/1_uniques_for_age_4_reformation.txt + script verified]` |
| ハイドゥク | Hajduk / a_hajduk | Light Infantry ユニット。Age 5 解禁。HUN 専用ではなくバルカン地域 Advance（balkan_hajduks）経由 `[src: unit_types/1_uniques_for_age_5_absolutism.txt + script verified]` |
| ヴェグヴァール体制 | vegvar_system | ベオグラード防衛イベント選択肢 A で解禁される国境要塞体制 |
| 黒軍政策 | black_army_policy | ハンガリー固有軍事政策。discipline +2.5% `[src: laws/01_military_laws.txt + script verified]` |
| フニャディ・ヤーノシュ | János Hunyadi | 1430-1443 に招聘可能な伝説的将軍候補 |
| ドラゴン騎士団 | Order of the Dragon | `flavor_hun.410` で設立可能な対オスマン騎士団 |
| 金印勅書 | Golden Bull of 1222 | ハンガリー固有の貴族特権勅書。`flavor_hun.350` で復活可能 |
| ヴィシェグラード会議 | Visegrád Congress | `flavor_hun.330`。ポーランドとの王冠連合協定への起点 |
| 王冠連合協定 | union_of_crowns_pact | ヴィシェグラード会議連鎖で成立するポーランドとの PU 協定 `[src: events/DHE/flavor_HUN.txt]` |
| 王位請求 CB | cb_claim_throne | 君主制間で使用可能な王位請求の開戦事由。1.2 で「請求者が統治中なら不発」`[src: casus_belli/claim_throne.txt + script verified]` |
| 帝国議会 | Imperial Diet | HRE の 4 段階議会システム `[src: parliament_types/01_international_organization.txt + script verified]` |
| 帝国兵器庫 | Imperial Armory | HRE 皇帝のみ建設可能な軍事建造物（gold=500）`[src: building_types/hre_buildings.txt + script verified]` |
| 黄金大勅書（HRE） | Golden Bull（HRE） | HRE 皇帝が制定する帝国法。未制定だと 1400 年以降に諸侯が離脱可能 `[src: international_organizations/hre.txt + script verified]` |
| 戦力前線幅 | possible_frontage_modifier | 戦場に展開できる兵力幅の修正値 `[src: advances/country_HUN.txt]` |
| 対ポーランド女性継承除外 | no_female_heirs_for_poland | 1.3。継承資格ルール。ポーランド方面の継承で女性継承者を資格から除外 `[src: heir_selections/monarchy.txt:1206]` |
| 好戦的傾向 | Belligerent | 社会価値軸 `belligerent_vs_conciliatory` の一方向 |

---

## 出典

### 一次情報（ゲームスクリプト・公式）

条件や数値の根拠はこちらを優先。

- ローカルのゲームスクリプトと日本語 localization を照合
  - `events/DHE/flavor_HUN.txt` — ハンガリー固有イベントのスクリプト
  - `parliament_types/01_international_organization.txt` — Imperial Diet 4 段階定義（Court Assembly / Early Diet / Bicamerial / Tricamerial）
  - `events/DHE/flavor_HUN_SER.txt` — ハンガリー＝セルビア関連イベント
  - `advances/country_HUN.txt` — ハンガリー固有進歩の定義
  - `advances_l_japanese.yml` — 進歩名の日本語訳
  - `game_concepts_l_japanese.yml` — ゲーム内用語の日本語訳
  - `unit_types/1_uniques_for_age_3_discovery.txt` — 黒軍（a_the_black_army）
  - `unit_types/1_uniques_for_age_4_reformation.txt` — ハンガリー・フサール（a_hungarian_hussars）
  - `unit_types/1_uniques_for_age_5_absolutism.txt` — ハイドゥク（a_hajduk）
  - `unit_categories/00_army_light_infantry.txt` — Light Infantry 兵科定義
  - `unit_categories/01_army_heavy_infantry.txt` — Heavy Infantry 兵科定義（is_garrison = yes）
  - `unit_categories/02_army_light_cavalry.txt` — Light Cavalry 兵科定義
  - `unit_categories/03_army_heavy_cavalry.txt` — Heavy Cavalry 兵科定義
  - `unit_categories/04_army_artillery.txt` — Artillery 兵科定義
  - `unit_types/00_age_templates_land.txt` — 兵科ベース値テンプレート
  - `auto_modifiers/country.txt` — Combined Arms 閾値（min 0.1 / max 0.5 / bonus +2.5%）
  - `laws/01_military_laws.txt` — 黒軍政策（black_army_policy）
  - `advances/region_balkans.txt` — balkan_hajduks（ハイドゥク地域 Advance）
  - `casus_belli/claim_throne.txt` — cb_claim_throne（王位請求 CB・1.2 制限）
  - `international_organizations/union.txt` — 同君連合 IO
  - `laws/40_personal_unions.txt` — PU 法律・統合レベル
  - `events/DHE/flavor_HAB.txt` — flavor_hab.46（HAB 視点ハンガリー陥落）
  - `international_organizations/hre.txt` — HRE 1.2 オーバーホール（Golden Bull・GP Score）
  - `laws/20_hre.txt` — HRE 法律（Golden Bull 効果）
  - `building_types/hre_buildings.txt` — Imperial Armory コスト・効果
  - `scripted_relations/union_of_crowns_pact.txt` — Union of Crowns 協定の継承ロジック整理（1.3）
  - `heir_selections/monarchy.txt` 行 1206 — `no_female_heirs_for_poland`（対ポーランド継承の女性除外ルール、1.3）
- [Hungary - EU5 Wiki](https://eu5.paradoxwikis.com/Hungary)
- [Hungarian content - EU5 Wiki](https://eu5.paradoxwikis.com/Hungarian_content)
- [Patch 1.1 "Rossbach" - EU5 Wiki](https://eu5.paradoxwikis.com/Patch_1.1)
- [Patch 1.1.X Hotfixes - EU5 Wiki](https://eu5.paradoxwikis.com/Patch_1.1.X)
- [Patch 1.2 "Echinades" - EU5 Wiki](https://eu5.paradoxwikis.com/Patch_1.2)
- [Patch 1.3 - EU5 Wiki](https://eu5.paradoxwikis.com/Patch_1.3)

**スクリプト検証済み項目（`script verified`）:**

- `unit_types/1_uniques_for_age_3_discovery.txt`: 黒軍（build_time 50% 短縮・strength_damage_taken -0.1・ハンガリー文化地のみ建設・is_garrison = yes）
- `unit_types/1_uniques_for_age_4_reformation.txt`: ハンガリー・フサール（initiative +2・impact flatland/mountains -0.25・貴族 Pop 依存）
- `unit_types/1_uniques_for_age_5_absolutism.txt`: ハイドゥク（Light Infantry 系統・要塞駐屯不可・hills/plateau +0.15/mountains +0.10）
- `unit_categories/00-04_army_*.txt`: 兵科分類（is_garrison は Heavy Infantry のみ）
- `auto_modifiers/country.txt`: Combined Arms（閾値 0.1-0.5・bonus +2.5%/兵科）
- `laws/01_military_laws.txt`: 黒軍政策（discipline +2.5%・傭兵維持費効率 +10%）
- `advances/region_balkans.txt`: balkan_hajduks（HUN 専用ではなくバルカン地域 Advance）
- `casus_belli/claim_throne.txt`: cb_claim_throne（請求者が統治中なら不発）
- `international_organizations/union.txt + laws/40_personal_unions.txt`: 同君連合（最低 50 年・統合レベル）
- `events/DHE/flavor_HAB.txt`: flavor_hab.46（HAB への cb_claim_throne 付与イベント）
- `international_organizations/hre.txt + laws/20_hre.txt`: HRE（Golden Bull 離脱条件）。GP Score 250→50 の変更はスクリプト上に該当識別子なく、Patch_1.2 wiki 由来のコミュニティ知見にとどまる
- `building_types/hre_buildings.txt`: Imperial Armory（gold=500・military_contribution 法必須）
- `events/DHE/flavor_HUN.txt`: flavor_hun.150（発火条件全文）・flavor_hun.210（vegvar_system）・flavor_hun.220（移民 amount 0.2）・flavor_hun.480（HAB 再建条件）・flavor_hun.550（ウィーン首都条件）・flavor_hun.580（ブラチスラバ条件）
- `casus_belli/D008_restore_roman_borders.txt`: Restore Roman Borders CB 存在（BYZ 用・HUN 領土への脅威）
- `parliament_types/01_international_organization.txt`: Imperial Diet 4 段階定義（Court Assembly / Early Diet / Bicamerial / Tricamerial）
- `laws/00_monarchy.txt`: Noble Levies 君主法（nobles_estate_levy_size = 0.50）

**コミュニティ知見項目（スクリプト未確認）:**
新 Advances 300+・新 DHE 140+・Latin Culture Movement・新 3D モニュメント・Imperial Diet 投票システム・王朝力上限 200→300・Belligerent/Conciliatory 修正・傭兵コスト +25%・Societal Values 初期値（詳細）・推奨選択の「どちらを選ぶか」判断・編成比率・タイミング推奨全般・陸軍 goods 需要 2 倍（1.3）・建物維持費逓増（1.3、エンジン内部値のためスクリプト実値未確認）

### コミュニティ情報（補足知見）

プレイ報告・体感ベースの情報。条件の裏取りには一次情報を参照のこと。

- [Hungary EU5 Guide — Bastion of Christendom | eu5.guide](https://eu5.guide/guides/hungary)
- [Best Nations to Play As in EU5 - Game Rant](https://gamerant.com/europa-universalis-5-eu5-best-nations-to-play-as/)
- [6 Best Countries To Play in EU5 | 2026 - Eneba](https://www.eneba.com/hub/games-guides/best-countries-to-play-europa-universalis-5/)
