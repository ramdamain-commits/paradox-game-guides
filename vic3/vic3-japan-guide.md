# VIC3 日本攻略ガイド（Patch 1.13 + EP2 The Great Wave 時点）

> 鎖国下の幕府日本（1836年）から明治維新を経て列強入りまで、EP2 DLC の日本固有メカニクスを軸に整理。
> 2026-05-17 時点のパッチ 1.13（Matcha）+ EP2 The Great Wave（dlc018）に準拠。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。

---

# VIC3 日本攻略ガイド — Section A（Patch 1.13 時点）

> 日本（JAP）→ 明治維新・列強化を狙う序盤の整理。
> 2026-05-17 確認時点。Patch 1.13（Matcha）+ The Great Wave DLC（ep2_content）対応。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳箇所は英語を併記する。

---

## パッチ 1.13 / DLC での日本関連変更点

1.13（Matcha）は海軍刷新と **The Great Wave**（EP2）が主題。日本は今パッチの最大受益国であり、
固有メカニクスの大部分が EP2 コンテンツとして追加・整備されている。

| 変更・追加 | 日本への影響 |
|-----------|------------|
| **The Great Wave DLC（EP2 = dlc018）追加** | 明治維新 JE（je_meiji_restoration）、鎖国 JE（je_sakoku）、岩倉使節団 JE（je_iwakura_mission）、日本固有法律（law_bakufu / law_sakoku / law_warrior_caste 等）、天保の大飢饉イベントが DLC ありで有効化 `[src: dlc_metadata/00_dlc_metadata.txt, dlc018]` |
| **日本固有法律の追加** | law_bakufu（幕府）・law_sakoku（鎖国）・law_terakoya（寺子屋）・law_warrior_caste（武士制度）・law_shinsengumi（新選組）が日本文化専用で実装。通常の孤立主義（law_isolationism）より強力な効果と制限を持つ `[src: common/laws/00_trade_policy.txt:290, common/laws/00_social_hierarchy.txt]` |
| **明治維新 JE の帝政・幕府の2分岐** | 維新側（帝政勝利）と幕府側（公武合体／公議輿論）の2ルートが完全実装。維新失敗時に幕府強化修正値が付与される `[src: common/journal_entries/00_meiji_restoration.txt]` |
| **岩倉使節団 JE（DLC 専用）** | je_meiji_main の外交承認サブ JE の代替として機能。技術研究ボーナス（production / society 両系）を累積付与 `[src: common/journal_entries/07_iwakura_mission.txt]` |
| **天保の大飢饉（Tenpō Crisis）JE** | DLC ありでゲーム開始時に je_tenpo_crisis が付与され、内政・食料危機イベントが発動 `[src: history/countries/jap - japan.txt]` |
| **海軍刷新（全国共通）** | 艦船デザイナー・旗艦（Flagship）・新型艦20種が追加。日本固有の艦船タイプは存在しないが、海軍整備の選択肢が全国で広がる。陸軍主体の日本への直接影響は限定的 `[src: common/ship_types/]`（コミュニティ知見：海軍刷新詳細の裏取りはスクリプト未確認） |
| **プロミネンス（Prominence）導入** | IG 指導者選出の主因が Popularity からプロミネンスに変更。将軍・天皇・大名系キャラクターの採用戦略に影響 `[src: Patch_1.13 wiki]`（コミュニティ知見：日本キャラクターのプロミネンス初期値はスクリプト未確認） |
| **単一指揮官制** | 軍事ユニットグループ（Military Formation）あたり指揮官1名に変更。サムライ訓練（pm_samurai_training）が生きる維新前の軍事運用に影響 `[src: Patch_1.13 wiki]` |

> DLC なし環境では上記の日本固有 JE・法律・イベントの大部分が無効化される。本ガイドは **EP2（The Great Wave）あり**を前提とする。

---

## 開始状況（1836年）

| 項目 | 値 |
|------|-----|
| 国家タグ | JAP |
| 政体 | 君主制（Monarchy） |
| 首都 | 江戸（STATE_KANTO） |
| 主要文化 | 日本（Japanese） |
| 分配法 | 幕府（law_bakufu）※ JAP のみ表示の固有法 |
| 鎖国法 | 鎖国（law_sakoku）※ 日本文化＋九州所持時のみ表示 |
| 国教 | 神道（Shinto）または仏教（Buddhist）（コミュニティ知見：国教の詳細はスクリプト未確認） |
| 識字率（Literacy） | 比較的高い（アジア圏では高水準）（コミュニティ知見） |
| 主要 IG | 地主→大名（ig_daimyo）が強力。ig_landowners プロミネンス +5 加算あり `[src: common/interest_groups/00_landowners.txt:752-761]` |
| 承認状況 | 未承認（Unrecognized）— 列強から国際的承認を得ていない状態 |
| 支配者 | 徳川家斉（JAP_ienari_tokugawa）が ruler として設定 `[src: common/characters/country_jap.txt]` |
| 後継者 | 徳川家慶（JAP_ieyoshi_tokugawa）が heir として設定 `[src: common/characters/country_jap.txt]` |

### 周辺国との関係

| 方角 | 隣国・勢力 | 初期の関係性 |
|------|-----------|------------|
| 北東 | ロシア（RUS） | 列強。不平等条約・強制開国の最大の圧力源候補。サハリン・北海道方面で摩擦 |
| 西 | 清（QNG） | 同じ東アジアの大国。アヘン戦争後の混乱が日本の開国圧力を間接的に高める |
| 南西 | イギリス（GBR） | 最大の列強。砲艦外交（Gunboat Diplomacy）の主な発動元になりやすい（コミュニティ知見） |
| 東 | アメリカ（USA） | 1.13 追加の砲撃外交の主な使い手候補。ペリー来航相当のイベントが発火する（コミュニティ知見） |
| 朝鮮半島 | 朝鮮（KOR） | 江戸期は交流あり。中盤の日本外交の焦点 |

### 初期の強み・弱み

| 強み | 弱み |
|------|------|
| 幕府法（law_bakufu）による正当性（Legitimacy）+30、権力（Authority）+200 `[src: common/laws/00_social_hierarchy.txt]` | 鎖国（law_sakoku）により影響力（Influence）-50%、技術伝播 -20%、交易容量 -75% `[src: common/laws/00_trade_policy.txt:290]` |
| サムライ訓練（pm_samurai_training）で高い訓練効率（+25 unscaled、レベルごと +5）`[src: common/production_methods/05_military.txt:144]` | 未承認（Unrecognized）状態で外交的選択肢が大きく制限される |
| 固有の人物テンプレートが豊富（105件）。明治維新後に多数の近代化人材が登用可能 `[src: common/characters/country_jap.txt]` | 開国すると列強との技術格差・軍事格差が顕在化する |
| 維新完了後に実業家（ig_industrialists）または知識人（ig_intelligentsia）が meiji_favored_ig 修正値で政治力 +50%（very_long）`[src: common/journal_entries/00_meiji_restoration.txt]` | 大名（ig_daimyo）の IG トレイトが不満時・満足時で挙動が正反対（後述） |
| 宗教 JE（神仏分離 / 仏教擡頭）の完了で独自修正値を獲得可能 `[src: common/journal_entries/07_japanese_religion.txt]` | 鎖国中は出島（Dejima）以外での交易拠点（Trade Center）建設が不可 `[src: common/laws/00_trade_policy.txt:290]` |

### IG 構造の特殊性（幕府 / 大名 / 知識人）

日本の IG 構造はゲーム中最も固有色が強い。維新成否を左右するため事前理解が重要。

#### 大名（ig_daimyo）— 地主（Landowners）の日本名称

開始時の地主（ig_landowners）は日本の主文化時に **大名（ig_daimyo）** として表示される。
`[src: common/interest_groups/00_landowners.txt:342-356]`

| IG トレイト | 発動条件 | 効果 |
|------------|---------|------|
| 普代大名支持（ig_trait_fudai_support） | IG が幸福（happy）以上 | 行政力（Bureaucracy）+5%、権威（Authority）+5% `[src: common/interest_groups/00_landowners.txt:342-356]` |
| 外様発言力（ig_trait_outspoken_tozama） | IG が不幸（unhappy）以下 | 権威（Authority）-5%、徴兵率（Conscription Rate）-10% `[src: common/interest_groups/00_landowners.txt:342-356]` |

- 大名 IG は**不満時に外様トレイトで権威（Authority）を削り、満足時に普代トレイトで権威（Authority）を補強する**。
  維新を進める際に大名を与党から外す場合、不満状態を長引かせると権威ペナルティが蓄積する点に注意。
- プロミネンス加算: c:JAP かつ維新未完了（japan_restoration_complete 変数なし）の場合に +5 `[src: common/interest_groups/00_landowners.txt:752-761]`
- 維新完了後: 名称が **華族（ig_kazoku）** に変更され、ideology も通常地主（ideology_hierarchic）と同一になる `[src: common/journal_entries/00_meiji_restoration.txt]`

#### 将軍と徳川家のキャラクター構造

- ゲーム開始時の ruler は **徳川家斉**（11代）`[src: common/characters/country_jap.txt, JAP_ienari_tokugawa]`
- 徳川将軍系は家斉→家慶→家定→家茂→慶喜→家達の順でテンプレートが定義されており、歴史的な将軍交代がイベントで起きる `[src: common/characters/country_jap.txt]`
- ig_landowners のリーダーが**非徳川**であることが維新 JE の complete 条件の一つ `[src: common/journal_entries/00_meiji_restoration.txt:54]`

#### 天皇キャラクター

| テンプレートID | 人物 |
|--------------|------|
| JAP_komei_yamato | 孝明天皇（維新期の天皇） |
| JAP_meiji_yamato | 明治天皇（睦仁） |

- `special_character_japanese_emperor` トレイトが付与されており、これを持つキャラクターが ruler の場合に維新 JE の complete 判定（ruler = 天皇 emperor trait 持ち）を満たす `[src: common/character_traits/special_personality_traits.txt:673]`
- トレイト効果: 正当性（Legitimacy）+5 `[src: common/character_traits/special_personality_traits.txt:673]`

#### 知識人（Intelligentsia）と近代化人材

維新後に登用できる知識人系キャラクター:

| 人物 | テンプレートID | 役割 |
|------|--------------|------|
| 福沢諭吉 | JAP_fukuzawa_yukichi | 知識人（Intelligentsia） |
| 大隈重信 | JAP_okuma_shigenobu | PM（親西洋派） |
| 原敬 | JAP_hara_takashi | 知識人（初の平民宰相） |
| 岩倉具視 | JAP_iwakura_tomomi | 対外使節、岩倉使節団 JE 関連 |

`[src: common/characters/country_jap.txt]`

---

## 開国の軛（Unrecognized 脱却・不平等条約・関税）

日本が外交的な制約から脱するには、段階的なプロセスが必要になる。

### 鎖国（law_sakoku）の制約

| 効果 | 数値 |
|------|------|
| 権力（Authority）加算 | +25% |
| 影響力（Influence） | -50% |
| 技術伝播（Tech Spread） | -20% |
| 交易容量（Trade Capacity） | -75% |
| 輸入・輸出関税（Tariff） | +50% |
| 交易拠点（Trade Center） | 出島（Dejima）のみ建設可 |

`[src: common/laws/00_trade_policy.txt:290]`

鎖国法は parent = law_isolationism（孤立主義）を持つが、通常の孤立主義より輸出入関税が大幅に高い。
国内権力は安定する一方で、外部との経済・外交チャネルがほぼ遮断された状態になる。

### 鎖国 JE（je_sakoku）

ゲーム開始時（DLC あり）に自動付与される JE。

| 項目 | 内容 |
|------|------|
| 完了条件 | law_sakoku でも law_closed_borders でもない状態（開国） |
| 完了効果 | イベント ep2_sakoku.4 トリガー、法変更賛成 IG に the_picked_lock_modifier 付与 |
| 失敗条件 | 君主制廃止、または japan_emperor_restored 変数あり（維新成立） |
| 失敗効果 | sakoku_entrenched_modifier 付与（鎖国定着ペナルティ） |

`[src: common/journal_entries/07_sakoku.txt]`

### 不平等条約・条約港（Treaty Port）

- 列強は **dp_take_treaty_port** 外交戦の戦争目標（war_goal = take_treaty_port）で日本に条約港を強制取得できる `[src: common/treaty_articles/14_treaty_port.txt]`
- 条約港の押し付けは **je_meiji_imperial_marriage**（公武合体ルート）の完了を妨害する。完了条件に「本土州に条約港なし」が含まれるため `[src: common/journal_entries/00_meiji_restoration.txt:88]`
- 条約が解除・強制終了された場合、その州に領有権主張が自動付与される `[src: common/treaty_articles/14_treaty_port.txt]`

### 強制開国修正値（forced_market_opening）

列強から条約条件を強制された場合に付与される。

| 効果 | 数値 |
|------|------|
| 威信（Prestige） | -25% |

`[src: common/static_modifiers/00_code_static_modifiers.txt:861]`

### Unrecognized 脱却の流れ（コミュニティ知見 + スクリプト確認の組み合わせ）

1. **開国**（鎖国法の廃止）: je_sakoku の完了条件。影響力・外交選択肢が回復する
2. **伝統主義（traditionalism）廃止**: je_meiji_diplomacy（外交承認サブ JE）の完了条件の一つ `[src: common/journal_entries/00_meiji_restoration.txt:79]`
3. **認知（Recognized）獲得**: je_meiji_diplomacy の完了後に recognized 状態が達成される。recognized は完了の結果であり、je_meiji_diplomacy の完了条件に「recognized であること」という循環参照はない（完了条件は「traditionalism 廃止・非従属」の 2 点）
4. DLC あり時: **岩倉使節団 JE（je_iwakura_mission）** が外交承認サブ JE の代替として機能し、技術ボーナスも同時に獲得できる `[src: common/journal_entries/07_iwakura_mission.txt]`

> **注意**: VIC3 の「関税（Tariff）」は鎖国法の state_tariff_import_add / state_tariff_export_add で実装された VIC3 固有の経済システムであり、EU4 の交易ノード関税とは別物。`[src: common/laws/00_trade_policy.txt:290]`（章8 grep 確認済み）

---

## Day 1（ポーズ解除直後）

1. **維新 JE（je_meiji_restoration）の発動条件を確認する**
   - 表示（is_shown_when_inactive）条件: c:JAP = THIS、君主制（law_monarchy）、幕府法（law_bakufu）、japan_restoration_complete 変数なしの 4 点 `[src: common/journal_entries/00_meiji_restoration.txt]`
   - 可能（possible）条件に「鎖国系法律でないこと（law_sakoku / law_closed_borders でないこと）」が含まれる `[src: common/journal_entries/00_meiji_restoration.txt]`
   - ゲーム開始直後は鎖国中のため **JE は表示されるが可能条件を満たさない**
   - まず開国（鎖国法の廃止）を中期目標として設定する

2. **鎖国 JE（je_sakoku）の状態を確認する**
   - DLC あり時は開始時に自動付与済み
   - 失敗すると sakoku_entrenched_modifier が付与されるため、維新路線なら早期に法律変更を進める

3. **大名 IG（ig_daimyo）の承認度を確認する**
   - 承認度が happy 以上で普代大名支持（権威・行政力 +5%）、unhappy 以下で外様発言力（権威 -5%、徴兵率 -10%）が発動
   - 開始直後に承認度ラインを確認し、維新 JE 進行中の IG 管理方針を立てる `[src: common/interest_groups/00_landowners.txt:342-356]`

4. **天保の大飢饉 JE（je_tenpo_crisis）の状況を確認する**
   - DLC あり時はゲーム開始から付与される
   - 緊急対応が必要な場合は経済・食料インフラの建設を最優先にする（コミュニティ知見）

5. **建設キューに優先施設を入れる**
   - 鎖国中は交易容量が -75% で交易拠点（Trade Center）が出島以外建設不可
   - 国内の工業基盤（建設局・兵舎）の拡張から始める
   - 大学（Universities）を建設して技術伝播の遅れを補う（鎖国による技術伝播 -20% の対策）（コミュニティ知見）

6. **法律改正の順序を計画する**
   - 鎖国廃止 → 伝統主義廃止 → 幕府法廃止の順が維新ルートの基本
   - ただし各法律改正は大名 IG・信者（Devout）等の反対を受けやすい。承認度管理と並行して進める（コミュニティ知見）

7. **将軍キャラクターと天皇キャラクターの両方を確認する**
   - 徳川家斉（ruler）の死亡タイミングと後継者（家慶 heir）を把握する
   - ig_landowners のリーダーが非徳川かどうかが維新 JE complete の必要条件 `[src: common/journal_entries/00_meiji_restoration.txt:54]`

---

## 時系列戦略

### 序盤（1836〜1860）: 開国対応と国力蓄積

ゲーム開始時の日本は **鎖国法（law_sakoku）** と **幕府法（law_bakufu）** の二重拘束下にある。
`law_sakoku` の効果は貿易容量 -75%・国内権力 +25%・技術伝播 -20%・輸出入関税 +50% という極端な閉鎖体制であり（`common/laws/00_trade_policy.txt:290`）、列強国に押しつけられる開国圧力は時間の問題だ。

| 時期 | 目標 |
|------|------|
| 1836-1840 | 建設局を即時拡張。`law_terakoya`（寺子屋）の識字率補正を活かして技術研究を開始 |
| 1840-1850 | 外交戦に備えて権力（Authority）と正当性（Legitimacy）を蓄積。`law_bakufu` の legitimacy +30・authority +200 補正を序盤の盾として活用（`common/laws/...` bakufu 記述） |
| 1850-1860 | 列強から条約港（treaty port）の強要が来る前に貿易政策を見直す。鎖国廃止と同時に `je_sakoku` が完了し、法変更賛成 IG に `the_picked_lock_modifier` が付与される（`common/journal_entries/07_sakoku.txt`） |

**鎖国解除の判断基準**（コミュニティ知見）

- 列強の外交戦で条約港を強制される前に自発的に鎖国を廃止すると、`forced_market_opening`（威信 -25%、`common/static_modifiers/00_code_static_modifiers.txt:861`）を回避できる。
- 鎖国廃止後は貿易政策を `law_isolationism` 経由で段階的に自由化する。一気に開放すると IG 不満が急増するため、1〜2 段階ずつ進める。

**幕府期の IG バランス**

序盤の ig_landowners は日本文化時に「大名（ig_daimyo）」名称に切り替わり、プロミネンスに +5 の補正が付く（`common/interest_groups/00_landowners.txt:752-761`）。大名IG は内部に **普代大名（ig_trait_fudai_support）** と **外様大名（ig_trait_outspoken_tozama）** の 2 トレイトが共存する。

- 普代大名トレイトは満足度 happy 以上で効果が発動（行政力・権威 +5%）
- 外様大名トレイトは満足度 unhappy 以下でのみ発動（権威 -5%・徴兵率 -10%）

大名 IG を不満にすると外様トレイトが活性化して権力が削られる。維新前は大名 IG の承認を「happy だが過度に満足させない」水準に保つことが安定運用の基本となる。

---

### 中盤（1860〜1880）: 明治維新と内戦処理

このフェーズが日本プレイの最重要局面だ。明治維新ジャーナルエントリ（`je_meiji_restoration`）が発動するには以下の前提条件が必要となる（`common/journal_entries/00_meiji_restoration.txt`）。

**維新 JE 発動条件（is_shown_when_inactive）**

- c:JAP = THIS
- `law_monarchy`・`law_bakufu` を保持
- `japan_restoration_complete` 変数がないこと
- 鎖国系法律（`law_sakoku` / `law_isolationism`）でないこと（possible 条件）

JE が表示されると同時に `movement_meiji_restorationist`（尊皇攘夷運動）が生成され、`restoration_timer_var` のカウントが始まる。

**維新カウンターの進め方**

毎月のパルスで `restoration_timer_var` がインクリメントされる条件は以下の 4 点をすべて満たすこと（`common/journal_entries/00_meiji_restoration.txt` 月次パルス記述）。

1. 天皇が統治者（ruler）であること
2. `law_bakufu` が廃止されていること
3. 内戦がないこと
4. ig_landowners（大名 IG）のリーダーが **非徳川** であること

`restoration_timer_var >= 6`（連続 6 ヶ月の条件維持）で維新完了判定が発動する。

**維新成立（帝政勝利）の報酬**（`on_complete` 記述）

- 首都が STATE_KANTO に移動し東京に改称
- ig_landowners が **華族（ig_kazoku）** に名称変更、ideology が `ideology_hierarchic` に更新
- 優先 IG（ig_industrialists または ig_intelligentsia）に `meiji_favored_ig` modifier（政治力 +50%、very_long 期間）付与
- `japan_display_add_meiji_reforms = yes` による改革表示の有効化

**幕府勝利分岐**（コミュニティ知見 + スクリプト確認）

維新 JE は帝政一択ではなく、幕府側が勝利する 2 つの分岐がある。

| 分岐名 | 条件概要 | 勝利結果 |
|--------|----------|----------|
| 公武合体（kobu_gattai） | `law_bakufu` 維持＋天皇婚姻完了＋幕府更新 | `modifier_court_and_shogunate`（権威 +10%・士官政治力 +25%・貴族（Aristocrats）政治力 -25%）`[src: common/static_modifiers/00_ep2_04_modifiers.txt]` |
| 公議輿論（kogi_yoron） | 選挙権あり・天皇復位・大名IG与党（徳川リーダー） | `modifier_continuity_and_enlightenment`（正当性 +10・技術伝播 +25%・近代主義者 pop support +15%）または `modifier_taikun_monarchy`（正当性 +5・影響力 +10%）`[src: common/static_modifiers/00_ep2_04_modifiers.txt]` |

いずれの幕府ルート分岐も、別途 `je_sakoku` が fail に至ると `sakoku_entrenched_modifier` が付与される。`sakoku_entrenched_modifier` は `je_sakoku` の失敗効果であり、`je_meiji_restoration` の失敗効果ではない点に注意（`[src: common/journal_entries/07_sakoku.txt, fail]`）。

**内戦処理の注意点**（コミュニティ知見）

維新進行中に内戦が発生すると `restoration_timer_var` のインクリメントが止まる。内戦を早期に終結させることが維新完了の近道だ。内戦を抑止するためには、維新運動の IG 満足度と急進化（Radicalism）水準を同時に管理する必要がある。

**岩倉使節団 JE（DLC 時）**

The Great Wave DLC（ep2_content）が有効な場合、`je_meiji_diplomacy`（外交承認サブ JE）の代替として `je_iwakura_mission` が機能する（`common/journal_entries/07_iwakura_mission.txt`）。使節団の進行に応じて `iwakura_mission_tech_learnings` が蓄積され、生産技術・社会技術の研究速度ボーナスが得られる。

| ボーナス modifier | 効果 |
|------------------|------|
| `modifier_iwakura_mission_production_tech_bonus` | 生産技術研究速度 +1%/スタック |
| `modifier_iwakura_mission_society_tech_bonus` | 社会技術研究速度 +0.25%/スタック、法律制定時間 -0.25%/スタック |

---

### 終盤（1880〜1936）: 列強入りと帝国運営

維新完了後は `je_meiji_main`（維新改革 JE）の 3 つのサブ JE を順次完了させることが最優先となる（`common/journal_entries/00_meiji_restoration.txt`）。

| サブ JE | 完了条件 | 戦略メモ |
|---------|----------|----------|
| `je_meiji_economy` | 70%以上の州に level 5+ 都市中枢＋鉄道 | 建設局の継続拡張が前提 |
| `je_meiji_army` | 農奴制/徴兵農民廃止・軍部野党化・ナポレオン戦術技術・サムライ訓練 PM 廃止・不規則歩兵 25% 未満 | 法律改正と軍制改革を連動させる |
| `je_meiji_diplomacy` | 伝統主義廃止・非従属・列強認知 | 外交戦で条約港を解消しておくこと（後述） |

タイムアウトは 4380 日（約 12 年）。全サブ JE 未完了でタイムアウトすると `meiji.14` イベント（ペナルティ）が発動する。

**列強入りの外交戦略**（コミュニティ知見）

- 列強認知を得るには GDP・軍事力・技術水準の三指標を総合した「列強ランク」上位 8 に入る必要がある。
- 維新後に `je_meiji_diplomacy` を進める際、条約港が残っていると外交承認の障害になる。事前に交渉で条約港を返還させるか、外交戦で撤回を勝ち取ること。

**朝鮮・大陸経営（DLC 時）**

`je_colonize_korea`（朝鮮植民地化 JE）は朝鮮州への鉄道建設で進行する（`common/journal_entries/07_korea_colonization.txt`）。建設 AI の優先重みが日本に付与されているため（`common/buildings/11_private_infrastructure.txt:195`）、自動建設に任せても一定程度進む。

**宗教 JE の選択**

終盤の安定化フェーズで以下 2 つの宗教 JE が選択肢に上がる（`common/journal_entries/07_japanese_religion.txt`）。

| JE | 目標 | 完了 modifier |
|----|------|--------------|
| `je_shinbutsu_bunri`（神仏分離） | 本土州の神道人口 60% 以上 | `arahitogami`（権力 +20%・正当性 +5） |
| `je_elevate_buddhism`（仏教振興） | 60 ヶ月間 ig_devout 強力維持 | `extended_danka_system`（行政コスト -20%・税容量 +15%） |

権力・正当性を重視するなら神仏分離、行政効率を重視するなら仏教振興が選択肢となる（コミュニティ知見）。

---

## 内政・経済

> VIC3 は経済がゲームの中心。日本の場合、鎖国解除と維新完了のフェーズによって建設優先順位が変化する点が特徴的だ。

### 建設の優先順位

**鎖国期（1836〜開国まで）**

鎖国期は `law_sakoku` の効果で貿易容量が著しく制限される。国内完結型の産業基盤を優先する。

| 順位 | 施設 | 理由 |
|------|------|------|
| 1 | 建設局（Construction Sector） | 全経済発展の基盤。最優先（コミュニティ知見） |
| 2 | 農地・農場（Farms / Rice Paddies） | 食料と百姓の維持。人口増加基盤 |
| 3 | 工具工場（Tool Workshops） | 建設に必要な工具を国内調達 |
| 4 | 大学（Universities） | 寺子屋の識字率補正と組み合わせて技術研究を加速 |

**開国後〜維新前**

貿易が開放されると輸入品で需要の一部を補えるが、維新完了を見据えた都市中枢整備を始める。

| 順位 | 施設 | 理由 |
|------|------|------|
| 1 | 建設局 | 継続拡張 |
| 2 | 都市中枢（Urban Center） | `je_meiji_economy` の条件（70%州 level 5+ 都市中枢）の先行投資 |
| 3 | 鉄道（Railway） | `je_meiji_economy` の条件（70%州 railway）の先行投資 |
| 4 | 製鉄所・鉄山（Steel Mill / Iron Mine） | 鉄道・工場建設に必要な鋼材を確保 |
| 5 | 兵舎（Barracks）改修 | `je_meiji_army` 向けにサムライ訓練 PM を廃止できるよう兵舎を整理 |

**維新完了後**

`meiji_favored_ig`（実業家または知識人の政治力 +50%）が付与されるため、優先 IG が支持する産業に追い風が吹く。

| 順位 | 施設 | 理由 |
|------|------|------|
| 1 | 鉄道（Railway） | 大陸鉄道（朝鮮 JE 含む）と国内 je_meiji_economy の完結 |
| 2 | 工場系全般 | 実業家（ig_industrialists）が与党になれば建設コスト補助が期待できる |
| 3 | 港湾（Port）・海軍基地 | 海軍整備と対外貿易の拡大 |
| 4 | 大学（Universities） | 岩倉使節団ボーナスと合算して技術研究を最大化 |

---

### 利益団体（IG）管理（維新前後の変化）

日本の IG 管理は維新前後で構造が大きく異なる。大名（ig_daimyo）から華族（ig_kazoku）への遷移を軸に戦略を立てる。

**維新前: 大名 IG（普代/外様）の扱い**

大名 IG は維新前の ig_landowners の別名であり、以下 2 つのトレイトが状態に応じて有効化される（`common/interest_groups/00_landowners.txt:342-356`）。

| トレイト | 有効条件 | 効果 |
|---------|----------|------|
| `ig_trait_fudai_support`（普代大名支持） | 満足度 happy 以上 | 行政力 +5%・権力 +5% |
| `ig_trait_outspoken_tozama`（外様発言力） | 満足度 unhappy 以下 | 権力 -5%・徴兵率 -10% |

大名 IG のプロミネンスには「c:JAP = owner かつ維新未完了時 +5」の固有補正があるため（`common/interest_groups/00_landowners.txt:752-761`）、維新前は大名が IG 指導者になりやすい構造になっている。

**大名 IG の満足度管理方針**（コミュニティ知見）

- 維新完了に向けて「大名 IG リーダーを徳川以外」にする必要がある。徳川リーダーが続く場合は IG 内の別人物のプロミネンスを育てる。
- 大名 IG を野党（Opposition）に置くと維新カウンターが進む代わりに急進化が高まる。
- 維新を急ぐあまり大名 IG との関係を壊しすぎると内戦リスクが上昇する。

**維新後: 華族（ig_kazoku）への遷移**

維新完了時に ig_landowners の名称が ig_kazoku（華族）に変わり、ideology が `ideology_hierarchic` に更新される（`common/journal_entries/00_meiji_restoration.txt` on_complete 記述）。

- 華族 IG の基本行動方針は通常の Landowners と同様（土地所有・農業利益の保護）だが、維新報酬の優先 IG（実業家または知識人）が政治力 +50% を得ているため相対的に弱体化する。
- 維新後は優先 IG と連立を組み、法律改正を一気に進めるウィンドウを活かす。

**その他の主要 IG**

| IG | 維新前の役割 | 維新後の役割 |
|----|------------|------------|
| 軍部（Armed Forces / ig_armed_forces） | 維新支持派に取り込む。`je_meiji_army` では一時的に野党化が必要 | 軍制改革完了後に与党に戻す |
| 実業家（Industrialists / ig_industrialists） | 工業化で徐々に育てる | `meiji_favored_ig` 付与時に与党化。近代化を牽引 |
| 知識人（Intelligentsia / ig_intelligentsia） | 維新運動の知的バック。法律改正の推進力 | `meiji_favored_ig` 付与対象になれば法律制定時間が短縮される |
| 信者（Devout / ig_devout） | 宗教 JE の選択次第で重要度が変わる | 仏教振興 JE を選ぶ場合は 60 ヶ月間の強化維持が必要 |

---

#### プロミネンスの活用（1.13）

1.13 で各政治家に **プロミネンス（Prominence）** ステータスが追加され、IG 指導者の選出確率を左右する主要因となった。[src: Patch_1.13 wiki]

- プロミネンスは大衆人気（Popularity）とは別概念で、IG 内の政治力寄与と次期指導者選出の確率に直接影響する。
- 大名 IG（維新前）では固有の +5 プロミネンス補正があるため、スクリプト上は大名キャラクターが指導者になりやすい（`common/interest_groups/00_landowners.txt:752-761`）。
- 維新完了を目指す場合は、「徳川以外の ig_landowners（大名）リーダー」が必要条件となる。徳川キャラクターのプロミネンスを相対的に下げ、別の大名キャラクターのプロミネンスを引き上げることで指導者交代を誘導できる。
- 1.13 のプロミネンス詳細（パラメータ値）はゲームスクリプトでの裏取り未実施のため、本ガイドでは操作方針をコミュニティ知見として示す（スクリプト数値は wiki 参照を推奨）。

---

### 法律改正ロードマップ（維新前/維新後で分岐）

日本の法律改正は「維新成立を目指す経路」と「維新完了後の近代化」で目標が変わる。

**【維新前】幕府法廃止と維新条件の整備**

維新カウンター開始に必要な `law_bakufu` の廃止は、大名 IG の同意なしには困難だ。段階的に IG の支持を調整しながら進める。

| 優先度 | 法律 | 目的 |
|--------|------|------|
| 最高 | 鎖国廃止 → 孤立主義（`law_isolationism`）系への移行（`law_free_ports` という法律 ID はスクリプト未確認。（未検証）） | 維新 JE の可能条件を解除（鎖国系でないこと） |
| 高 | `law_warrior_caste` 廃止（他 army_model への移行） | 維新後に `je_meiji_army` で必要。`pm_samurai_training` 廃止の前提（`common/laws/...` warrior_caste 記述） |
| 高 | `law_hereditary_bureaucrats` → より近代的な官僚制 | 行政力の安定確保 |
| 中 | `law_serfdom` → `law_tenant_farmers` | 農村部の急進化を抑制し、維新後の経済基盤整備 |
| 中 | `law_bakufu` 廃止 | 維新完了条件の中核。大名 IG の野党化・非徳川リーダー化と組み合わせる |

> 注意: `law_bakufu` は progressiveness -100 であり（スクリプト確認済み）、支持 IG を揃えないと制定速度が極めて遅い。

**【維新後】近代化改革の推進**

維新完了後に `meiji_favored_ig`（実業家または知識人 +50%政治力）が付与されるウィンドウを活かして一気に近代化法律を積み上げる。

| 優先度 | 法律 | 目的 |
|--------|------|------|
| 最高 | `law_compulsory_primary_school`（義務教育系） | 識字率と技術伝播を強化 |
| 高 | `law_professional_army` または `law_mass_conscription` | `je_meiji_army` 完了条件（農奴制・徴兵農民の廃止連動） |
| 高 | `law_market_economy` / 経済自由化 | 実業家 IG の支持を確保しつつ経済効率を向上 |
| 中 | `law_multicultural` または市民権系の段階的緩和 | 朝鮮・台湾経営時の pop 統合コスト削減 |
| 中 | 選挙権系（`law_wealth_voting` → 段階的拡張） | 知識人・労働組合の満足度を長期管理 |
| 低 | `law_freedom_of_press` / 報道系 | 急進化が落ち着いた終盤に対応 |

> `je_meiji_diplomacy` の条件に「traditionalism 廃止」が含まれるため、対象法律は早めに廃止対象に組み込むこと。廃止すべき具体的な法律 ID（`law_traditionalism` 等）はスクリプト未確認のため実ゲームで確認すること。（未検証）

**宗教法律の選択（維新後）**

- 神仏分離路線（`je_shinbutsu_bunri` 完了 → `arahitogami` modifier 獲得）を狙う場合は、信者 IG の支持を確保しつつ神道人口拡大を促進する。
- 仏教振興路線（`je_elevate_buddhism` 完了 → `extended_danka_system` modifier 獲得）は 60 ヶ月間の信者 IG 強化維持が必要。法律改正の中で信者 IG を与党に置く時間を確保する。


<!-- VIC3 日本攻略ガイド Section C -->
<!-- 担当範囲: 外交・同盟 / 軍事ドクトリン（陸軍）/ 固有イベント時系列 / 技術・法律 / よくあるミス / 用語対照表 / 出典 -->

## 外交・同盟

### 必須外交

| 対象 | 行動 | 理由 |
|------|------|------|
| 清（CHI） | 中立〜友好を維持 | ゲーム序盤は日本よりはるかに大きい。敵対すると即戦争リスク |
| 朝鮮（KOR） | 影響力確保 → 属国化を検討 | je_colonize_korea JE の進行に必要。railway 建設で JE が進む `[src: common/journal_entries/07_korea_colonization.txt]` |
| イギリス（GBR） | 好意的中立を維持 | 開国圧力の主体。砲艦外交（Gunboat Diplomacy）で条約を強制してくる列強筆頭 |
| ロシア（RUS） | 勢力圏の重複に注意 | 北方・朝鮮半島での利害が衝突しやすい。列強化前に正面衝突は避ける |
| アメリカ（USA） | 承認国化の外交ルートとして活用 | 認識の強要（Force Recognition）または独自外交で承認を得る候補 |

> **外交方針の大原則**: 日本は Unrecognized（非承認国家）としてゲームを開始する。Recognized（承認国）になるまでは外交戦の起票権が制限される。最優先は昇格ルートの確保。

### Unrecognized → Recognized 昇格ルート

日本は開始時に非承認国家（Unrecognized）。国際社会での承認（Recognized）を得るには以下のいずれかを満たす:

1. **je_meiji_diplomacy サブ JE の完了**
   - 完了条件: traditionalism 廃止、非従属状態、recognized `[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_diplomacy]`
   - 維新完了後に発動する je_meiji_main の外交承認サブ JE として機能する
   - DLC（ep2_content）あり時は岩倉使節団 JE（je_iwakura_mission）が外交承認サブ JE の代替として機能 `[src: common/journal_entries/07_iwakura_mission.txt]`

2. **岩倉使節団（je_iwakura_mission）ルート（DLC: The Great Wave 必須）**
   - iwakura_mission_tech_learnings を蓄積し、技術ボーナスも同時取得可能 `[src: common/journal_entries/07_iwakura_mission.txt]`
   - modifier_iwakura_mission_production_tech_bonus: 生産技術研究速度 +1% per stack `[src: common/journal_entries/07_iwakura_mission.txt]`
   - modifier_iwakura_mission_society_tech_bonus: 社会技術研究速度 +0.25% per stack、法律制定時間 -0.25% per stack `[src: common/journal_entries/07_iwakura_mission.txt]`
   - 外交承認と同時に技術加速も狙えるため、DLC ありプレイでは最優先で進める

3. **認識の強要（Force Recognition）外交戦目標**
   - 列強に対して外交戦を仕掛け、Force Recognition 外交戦目標で承認を勝ち取る（未検証：VIC3 外交戦目標の正確なスクリプト ID `force_recognition` については `common/diplomatic_plays/` での確認が必要）
   - 列強化前に開戦すると支援国が集まり不利。維新完了後の軍制改革が前提（コミュニティ知見）

> **注意**: je_meiji_diplomacy の完了条件に「non-subject（非従属）」が含まれる。いずれかの列強の属国・保護国になっている間は完了できない `[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_diplomacy]`。

### 1.13 で増えた外交手段

| 手段 | 日本での使い道 |
|------|--------------|
| **砲撃外交（Gunboat Diplomacy）** | 沿岸国（朝鮮・琉球等）への条約交渉時の脅迫オプション。海軍が整い次第、朝鮮への影響力確保に活用（コミュニティ知見：必要海軍規模・威信要件はスクリプト未確認） |
| **戦略的関心度（Strategic Interest）のティアド化** | 列強の日本周辺への関与度ティアを確認し、列強が低関心の時期を狙って朝鮮・沿岸地域への外交戦を起こす `[src: Patch_1.13 wiki]` |
| **クーデター扇動（Orchestrate Coup）** | 友好的なロビーを持つ弱小国の政体転換に活用。直接戦争より悪名コストが低い場合がある（コミュニティ知見：具体的な発動条件・コストはスクリプト未確認） `[src: Patch_1.13 wiki]` |
| **条約港（Treaty Port）対策** | 日本が条約港を強制設置された場合、je_meiji_imperial_marriage の完了条件が阻害される。NOT = { any_state_in_home_islands = { is_treaty_port = yes } } `[src: common/treaty_articles/14_treaty_port.txt]`。条約港を解除する外交交渉を優先する |

> **条約港の注意点**: 強制開国修正値（forced_market_opening）が付与されると威信 -25% のペナルティが持続する `[src: common/static_modifiers/00_code_static_modifiers.txt:861]`。列強に条約港を押し付けられないよう、鎖国（law_sakoku）の解除タイミングを慎重に選ぶ。

---

## 軍事ドクトリン（陸軍）

### 将軍の選び方（1.13 単一指揮官制）

1.13 で軍事ユニットグループ（Military Formation）あたりの指揮官は **1 名のみ** になった。少数精鋭の将軍を昇進させて運用するのが基本。`[src: Patch_1.13 wiki]`

#### 日本固有の将軍候補

| テンプレートID | 人物 | 所属 IG | 備考 |
|---|---|---|---|
| JAP_yamagata_aritomo | 山縣有朋 | Armed Forces | 軍制改革の主導者 `[src: common/characters/country_jap.txt]` |
| JAP_ito_hirobumi | 伊藤博文 | Armed Forces | 政治家としても重要 `[src: common/characters/country_jap.txt]` |
| JAP_togo_heihachiro | 東郷平八郎 | — | 提督。海軍指揮官候補 `[src: common/characters/country_jap.txt]` |
| JAP_nogi_maresuke | 乃木希典 | — | 将軍 `[src: common/characters/country_jap.txt]` |

#### 将軍運用の基本方針

- 軍事スキル + 特性（trait）の質を最優先。多数の凡庸な将軍より優秀な将軍 1〜2 名を昇進させる方が有効
- 不必要な昇進は軍部（Armed Forces）IG の承認低下ペナルティを招くため、必要になってから階級を上げる `[src: Patch_1.13 wiki]`
- 指揮官は編成間で再配置可能だが移動に時間がかかる。移動中は特性ボーナスが失われる `[src: Patch_1.13 wiki]`
- 複数前線（朝鮮・台湾・本土防衛等）になる場合は、各編成に専任の将軍を割り当てる

#### 日本固有の陸軍 PM: pm_samurai_training

- law_warrior_caste（武士階級）法が有効な間のみアンロック `[src: common/production_methods/05_military.txt:144]`
- building_training_rate_add = +25（unscaled）、レベルごとに +5
- 士官 25% / 兵士 75% の比率で訓練
- **維新後の注意**: je_meiji_army（軍制改革サブ JE）の完了条件に「pm_samurai_training を持つ兵舎が存在しないこと」が含まれる `[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_army]`。維新を完成させるには、武士訓練 PM を停止し近代兵制に切り替える必要がある

#### 兵科方針

| 兵種 | 序盤方針 | 備考 |
|------|---------|------|
| 非正規軍（Irregular Infantry） | 維新前の主力。安価だが戦力は低 | 維新後は早期に置換を目指す |
| 戦列歩兵（Line Infantry） | 維新後の主力。技術でアップグレード優先 | |
| 騎兵（軽騎兵・竜騎兵等） | 機動力補完として少数維持 | 海島地形では効果が限定的 |
| 大砲（カノン砲 → 後装砲） | 技術が進むほど有利 | Era 2 の後装砲技術（Breech-Loading Artillery）を優先 |

## 海軍ドクトリン（1.13 海軍改修）

> このセクションは VIC3 1.13（Matcha）以降の海軍システムに基づく。
> スクリプト確認済みの情報は `[src: ...]` を付与し、体感・戦略論はすべて「コミュニティ知見」として明示する。

---

### 1.13 海軍改修の構造変更点

1.13（Matcha）ではゲーム全体の海軍システムが刷新された。主な変更点は以下のとおり。

| 変更点 | 概要 |
|--------|------|
| 艦船デザイナー（Ship Designer）の追加 | 各艦に装甲・武装・推進力・補給能力の4軸でモジュールを割り当て可能になった。性能と維持費のトレードオフを設計段階で調整できる [src: Patch_1.13 wiki] |
| 旗艦（Flagship）の追加 | 艦隊内の1隻を旗艦に指定できる。旗艦の生存・撃沈が威信（Prestige）の獲得・喪失に直結する [src: Patch_1.13 wiki] |
| 新型艦20種の追加 | 装甲艦・蒸気フリゲート・モニター等、時代に対応した艦種が拡充された [src: Patch_1.13 wiki] |
| 砲撃外交（Gunboat Diplomacy）の追加 | 沿岸国相手に条約交渉時の圧力手段として利用できる外交アクション。（コミュニティ知見：180日という許可期間はスクリプト未確認）`[src: Patch_1.13 wiki]` |
| 海戦システムの改編 | 砲撃・魚雷・拿捕等の交戦プロセスが整理された [src: Patch_1.13 wiki] |

**日本固有の艦船・海軍改修エントリについて**

スクリプト確認の結果、`common/ship_types/`・`common/ship_modifications/`・`common/combat_unit_types/` に JAP 固有エントリは存在しない。
[src: common/ship_types/ 全体, common/ship_modifications/ 全体, common/combat_unit_types/ 全体]

日本は 1.13 の全国共通艦船システムをそのまま使用する。日本専用の艦種・固有海軍 modifier は現状不在。また 1.12 以前の海軍ファイルは手元にないため旧構造との差分比較は不可とする。

---

### 艦隊編成・配備

VIC3 1.13 の海軍は「編成（Formation）」単位で管理し、複数の艦船をまとめて一つの戦闘グループとして扱う。

#### 基本の艦種分類（1.13 全国共通）

| 艦種カテゴリ | 用途 |
|------------|------|
| 主力艦（Capital Ships）| 海戦の主軸。装甲艦・戦列艦等。旗艦指定に適する |
| フリゲート・コルベット | 通商保護・偵察・港湾封鎖支援に使う中型艦 |
| モニター・沿岸防衛艦 | 浅海・沿岸域での防衛に特化した低機動力艦 |
| 輸送艦 | 海上での部隊移動に使用。戦闘力はない |

> 「flotilla」という単位は 1.13 スクリプト上での確認が取れていないため本文では使用しない。編成管理の詳細な内部ラベルはスクリプト未確認。（コミュニティ知見：実プレイ上の UI では複数艦を1グループとして運用するのが一般的）

#### 日本の艦隊配備指針（コミュニティ知見）

- **序盤（1836〜1860）**: 鎖国（law_sakoku）時は海外展開が制限される。国内整備優先。開国後に最低限の沿岸防衛艦隊を編成する
- **中盤（1860〜1900）**: 維新完了後に近代的海軍の整備が現実的になる。対清・対朝鮮への制海権確保のため中型艦中心の艦隊を整備する
- **終盤（1900〜1936）**: 太平洋での影響力拡大に向けて主力艦・装甲艦を重点整備する

---

### 製造拠点と location 条件

VIC3 の造船所（Shipyard）系建造物は、建造物定義に `location_potential` 条件が設定されており、すべての州に建設できるわけではない。

> 造船所の `location_potential` に関する具体的なスクリプトエントリ（`common/buildings/` 内の造船所定義行番号）は今回の調査では確認していない。以下はスクリプト未確認。（コミュニティ知見）

#### 日本の造船拠点として有力な州（コミュニティ知見）

| 州 / 地域 | 理由 |
|-----------|------|
| 九州（STATE_KYUSHU 周辺） | 開始から所有。港湾アクセスが高い |
| 瀬戸内海沿岸（本州西部・中国地方） | 内海航路。造船業の歴史的集積地 |
| 関東（STATE_KANTO） | 維新後の首都圏。経済規模に比例してインフラが集積 |
| 北海道・東北沿岸 | 中盤以降に開発が進めば太平洋側の前進基地になり得る |

> 具体的な `location_potential = { is_coastal = yes }` や港湾建造物の解禁条件は `common/buildings/` スクリプトの該当行番号で確認することを推奨する。現状の記述は体感ベース（コミュニティ知見）。

---

### 進出ルート（序盤→中盤→終盤）

以下のルートはすべてコミュニティ知見ベース。スクリプトで確認できた条件には個別に `[src: ...]` を付与する。

#### 序盤（1836〜1860）: 沿岸防衛の確立

- 鎖国法（law_sakoku）下では外洋展開が事実上不可能。海軍整備よりも法律改正と内政基盤を優先する `[src: common/laws/00_trade_policy.txt:290, law_sakoku]`
- 出島（Dejima）のみ通商据点（Trade Center）設置が可能な制約がある `[src: common/laws/00_trade_policy.txt:290, law_sakoku]`
- 強制開国（外交プレイ）を受けると `forced_market_opening` modifier が付与され、威信が低下する。開国のタイミングをコントロールすることが序盤の鍵 `[src: common/static_modifiers/00_code_static_modifiers.txt:861, forced_market_opening]`
- 沿岸防衛用に少数のフリゲートを整備しておくことで、外国艦隊の砲撃外交（Gunboat Diplomacy）への対処力を持つ（コミュニティ知見）

#### 中盤（1860〜1900）: 東アジアの制海権確保

- 維新完了後（`japan_restoration_complete` 変数セット）は法律・外交制限が緩和され、本格的な海軍整備が可能になる `[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_restoration on_complete]`
- **対清制海権**: 朝鮮・台湾方面への影響力投射のため、中型艦中心の艦隊を黄海・東シナ海に展開する（コミュニティ知見）
- **朝鮮植民地化 JE**: `je_colonize_korea` は朝鮮への鉄道（Railway）建設で進行する。鉄道建設中の補給路防衛のために制海権が重要になる `[src: common/journal_entries/07_korea_colonization.txt, je_colonize_korea]`
- 岩倉使節団 JE（`je_iwakura_mission`）完了で得られる技術ボーナスは海軍技術研究の加速にも使える `[src: common/journal_entries/07_iwakura_mission.txt, modifier_iwakura_mission_production_tech_bonus]`

#### 終盤（1900〜1936）: 太平洋進出

- 列強化後は太平洋への影響力拡大が現実的になる。主力艦・装甲艦を中核とした艦隊を整備し、旗艦（Flagship）を1隻指定して威信獲得を狙う（コミュニティ知見）
- 艦船デザイナー（Ship Designer）で主力艦の装甲・武装を最大化し、補給能力を長距離航行に対応させるカスタマイズが有効（コミュニティ知見）
- 砲撃外交（Gunboat Diplomacy）を活用して太平洋島嶼国や東南アジア沿岸国への圧力手段として使える `[src: Patch_1.13 wiki]`（コミュニティ知見：発動に必要な最低海軍規模はスクリプト未確認）

---

### 提督の運用と単一指揮官制の海軍適用範囲

1.13 で陸軍・海軍ともに **単一指揮官制** が導入された。艦隊編成ごとに指揮官1名のみ配置できる。

#### 日本の著名提督テンプレート

| テンプレート ID | 人物 | 備考 |
|---------------|------|------|
| `JAP_togo_heihachiro` | 東郷平八郎 | 海軍提督として定義 [src: common/character_templates/country_jap.txt, JAP_togo_heihachiro] |

> 東郷平八郎は中盤〜終盤に登用機会が来る見込み。具体的な登用年・前提条件はスクリプト未確認（コミュニティ知見）。

#### 指揮官運用の指針（コミュニティ知見）

- 複数の艦隊を同時運用する場合、各艦隊に1名ずつ提督を充てる必要がある。提督の育成・スカウトを内政フェーズで並行して進める
- 海軍提督と陸軍将軍は兼任できないため、海軍に特化したキャラクターラインを意識して育てる
- 旗艦を指定した艦隊の提督が戦死すると威信喪失リスクが高まる。旗艦艦隊の提督には最も能力値の高いキャラクターを充てる

---

### 日本固有の海軍 modifier・decision

スクリプト調査（`common/ship_types/`・`common/ship_modifications/`・`common/static_modifiers/`・`common/decisions/`）の結果:

**日本固有の海軍 modifier は現状不在。**
`common/static_modifiers/00_ep2_04_modifiers.txt` および `00_ep2_06_modifiers.txt` に定義されている日本固有 modifier はすべて陸軍・内政・外交系であり、海軍に特化した modifier はない。
[src: common/static_modifiers/00_ep2_04_modifiers.txt, 00_ep2_06_modifiers.txt]

日本固有の海軍 decision（造船促進・海軍拡張系）も現状スクリプト上では確認されていない。
[src: common/ship_types/ 全体, common/ship_modifications/ 全体, common/combat_unit_types/ 全体]

海軍の強化は全国共通の技術研究（Technology）・建造物投資・艦船デザイナーのカスタマイズで行う。日本固有のショートカットはない。

---

### まとめ：日本の海軍優先順位

| フェーズ | 優先度 | 方針 |
|---------|--------|------|
| 序盤（1836〜1860）| 低 | 鎖国解除・維新優先。海軍は沿岸防衛最小限 |
| 中盤（1860〜1900）| 中 | 維新後に中型艦整備。対清・朝鮮の制海権確保 |
| 終盤（1900〜1936）| 高 | 艦船デザイナーで主力艦を最適化。旗艦指定で威信獲得 |

> 陸軍主体の維新序盤に海軍投資を急ぎすぎると建設キューを圧迫する。内政・法律改正が一段落してから本格整備に移行するのが安定する（コミュニティ知見）。

---

### 出典

#### 一次情報（スクリプト確認済み）

| ファイル | 参照内容 |
|---------|---------|
| `common/ship_types/` 全体 | JAP 固有艦船エントリなし |
| `common/ship_modifications/` 全体 | JAP 固有艦船改修エントリなし |
| `common/combat_unit_types/` 全体 | JAP 固有海軍戦闘ユニットエントリなし |
| `common/laws/00_trade_policy.txt:290` | law_sakoku の効果・制限 |
| `common/static_modifiers/00_code_static_modifiers.txt:861` | forced_market_opening の効果 |
| `common/journal_entries/00_meiji_restoration.txt` | 維新完了変数（japan_restoration_complete） |
| `common/journal_entries/07_korea_colonization.txt` | je_colonize_korea の発動条件 |
| `common/journal_entries/07_iwakura_mission.txt` | 岩倉使節団技術ボーナス modifier |
| `common/static_modifiers/00_ep2_04_modifiers.txt` | 日本固有 modifier 一覧（海軍系なし） |
| `common/static_modifiers/00_ep2_06_modifiers.txt` | 日本固有 modifier 一覧（海軍系なし） |
| `common/character_templates/country_jap.txt` | 東郷平八郎テンプレート（JAP_togo_heihachiro） |

#### コミュニティ情報

- 艦隊編成の実運用・造船拠点の選定・提督育成タイミングはプレイ報告ベース
- 造船所の `location_potential` スクリプト未確認
- 砲撃外交の発動に必要な最低海軍規模はスクリプト未確認
- 東郷平八郎の登用年・前提条件はスクリプト未確認

#### パッチ参照

- Patch_1.13 wiki: [vic3.paradoxwikis.com/Patch_1.13](https://vic3.paradoxwikis.com/Patch_1.13)（1.13 海軍刷新・艦船デザイナー・旗艦・砲撃外交）

---

---

## 固有イベント時系列

### 明治維新 JE 攻略チャート

維新 JE（je_meiji_restoration）は発動から帝政勝利まで最低でも 6 ヶ月の連続条件維持が必要。分岐条件を早期に把握して準備する。

#### 発動条件チェック

| 条件 | 説明 | 対処 |
|------|------|------|
| c:JAP = THIS | 日本プレイヤー限定 | — |
| has_law = law_monarchy | 君主制であること | 政体を維持 |
| has_law = law_bakufu | 幕府法が有効 | 初期から有効 |
| 鎖国系法律でないこと | law_sakoku でも law_closed_borders でもない | je_sakoku を進めて鎖国解除が前提 `[src: common/journal_entries/00_meiji_restoration.txt]` |

#### JE 本体：主要分岐チャート

| 分岐 | 前提条件 | 達成期限 | 主な判定条件 | 勝利結果 |
|------|---------|---------|------------|--------|
| **帝政（維新）勝利** | 天皇が ruler かつ special_character_japanese_emperor trait 持ち | 連続 6 ヶ月維持後に完了 `[src: common/journal_entries/00_meiji_restoration.txt]` | bakufu 法なし、内戦なし、ig_landowners リーダーが非徳川 | 首都→東京、ig_landowners → ig_kazoku（華族）、meiji_favored_ig 修正値（IG 政治力 +50%、very_long 期間）`[src: common/journal_entries/00_meiji_restoration.txt, on_complete]` |
| **公武合体（幕府ルートA）** | bakufu 法継続 + 天皇婚姻完了 + bakufu 更新 | je_meiji_imperial_marriage タイムアウト 1825 日（5 年）`[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_imperial_marriage]` | 有害条約の破棄、closed_borders、treaty_port なし | イベント ep2_meiji.8、modifier_court_and_shogunate: 権威（Authority）+10%、士官（Officers）政治力 +25%、貴族（Aristocrats）政治力 -25% `[src: common/static_modifiers/00_ep2_04_modifiers.txt]` |
| **公議輿論（幕府ルートB）** | 選挙権あり + 天皇復位 + ig_landowners 与党かつ徳川リーダー | 維新 JE fail 分岐 `[src: common/journal_entries/00_meiji_restoration.txt, fail]` | 上記 kobu_gattai / kogi_yoron 変数セット条件 | イベント ep2_meiji.9、modifier_continuity_and_enlightenment（正当性 +10、技術普及 +25%、近代主義者 pop support +15%）または modifier_taikun_monarchy（正当性 +5、影響力 +10%）`[src: common/static_modifiers/00_ep2_04_modifiers.txt]` |

#### 帝政ルート：維新本体 JE 完了後のサブ JE

je_meiji_restoration 完了後、je_meiji_main が発動。meiji_var（0→3）の達成が目標。タイムアウト 4380 日（約 12 年）`[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_main]`。

| サブ JE | 英語名 | 完了条件 | 未達時ペナルティ |
|---------|--------|---------|----------------|
| je_meiji_economy | 経済近代化 | 70% 以上の州に level 5+ urban_center かつ railway `[src: common/journal_entries/00_meiji_restoration.txt]` | タイムアウト後 meiji.2 または meiji.14 トリガー |
| je_meiji_army | 軍制改革 | serfdom/peasant_levies 廃止、Armed Forces 野党化、ナポレオン戦争技術、武士訓練 PM 廃止、非正規軍 < 25% `[src: common/journal_entries/00_meiji_restoration.txt]` | 同上 |
| je_meiji_diplomacy | 外交承認 | traditionalism 廃止、非従属、recognized `[src: common/journal_entries/00_meiji_restoration.txt]` | 同上。DLC あり時は je_iwakura_mission が代替 |

#### 宗教サブ JE（任意）

宗教方針の選択で長期修正値が変わる。どちらか一方を選ぶ。

| JE | 目標 | 完了効果 |
|----|------|---------|
| je_shinbutsu_bunri | 全本土州の神道人口 60% 以上 `[src: common/journal_entries/07_japanese_religion.txt]` | arahitogami: 権力 +20%、正当性 +5 `[src: common/static_modifiers/00_ep2_06_modifiers.txt]` |
| je_elevate_buddhism | 60 ヶ月間 ig_devout が強力（progressbar）`[src: common/journal_entries/07_japanese_religion.txt]` | extended_danka_system: 官僚コスト -20%、税容量 +15% `[src: common/static_modifiers/00_ep2_06_modifiers.txt]` |

#### 鎖国解除 JE（je_sakoku）

維新 JE 発動の前提となる開国フロー。

| 項目 | 内容 |
|------|------|
| 付与タイミング | ゲーム開始時（DLC あり時）`[src: common/journal_entries/07_sakoku.txt]` |
| 完了条件 | law_sakoku でも law_closed_borders でもない状態 |
| 完了効果 | イベント ep2_sakoku.4、法変更賛成 IG に the_picked_lock_modifier 付与 `[src: common/journal_entries/07_sakoku.txt]` |
| 失敗条件 | 君主制廃止、または japan_emperor_restored 変数あり（帝政ルートで維新が先に成立した場合） |
| 失敗効果 | sakoku_entrenched_modifier 付与（保守化ペナルティ） |

> **鎖国法（law_sakoku）の効果**: 権力 +25%、影響力 -50%、技術普及 -20%、取引所容量 -75%、輸入関税 +50%、輸出関税 +50% `[src: common/laws/00_trade_policy.txt:290]`。開国は経済・外交両面に大きく影響する。急いで解除すると IG の反発（急進化）を招く。ig_landowners の承認に注意しながら進める。

---

## 技術・法律

### 技術優先順位（日本）

| Era | 優先分野 | 日本固有の理由 |
|-----|---------|-------------|
| Era 1 | 産業系（鉄・工具）+ 軍事（戦列歩兵・銃工） | 維新 JE 軍制改革サブ JE の完了にナポレオン戦争技術が必要（コミュニティ知見：「ナポレオン戦争技術」の正確なスクリプト ID は未確認） |
| Era 2 | 鉄道（Railway）+ 後装砲 + 社会系（分離権力）| je_meiji_economy の完了条件に railway が必要 `[src: common/journal_entries/00_meiji_restoration.txt]` |
| Era 2-3 | 岩倉使節団 JE 継続中は技術研究速度が上昇 | production_tech +1%/stack、society_tech +0.25%/stack `[src: common/journal_entries/07_iwakura_mission.txt]` |
| Era 3 | 電力・内燃機関 + 国民皆兵（Mandatory Service） | 列強対抗に向けて軍拡 |
| Era 4-5 | バランスよく | 列強として全方位の発展 |

### 法律改正ロードマップ（日本固有）

日本は開始時に **law_bakufu**（幕府）と **law_sakoku**（鎖国）という日本固有の法律を持つ。これらの解除が維新の核心。

| 優先度 | 法律 | タイミング | 理由 |
|--------|------|-----------|------|
| 最高 | law_sakoku → 孤立主義 or 保護主義への変更 | 維新 JE 発動前 | je_sakoku 完了 → 維新 JE 発動の前提。鎖国のまま維新 JE は可能条件を満たさない `[src: common/journal_entries/00_meiji_restoration.txt]` |
| 最高 | law_bakufu 廃止 | 維新 JE 帝政勝利後 | 帝政勝利の月次パルス条件「bakufu 法なし」に直結 `[src: common/journal_entries/00_meiji_restoration.txt]` |
| 高 | law_warrior_caste → 近代的軍制 | 維新後・je_meiji_army 進行中 | 武士訓練 PM 廃止が軍制改革サブ JE の完了条件 `[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_army]` |
| 高 | serfdom（農奴制）廃止 | 維新後 | je_meiji_army の完了条件 `[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_army]` |
| 高 | traditionalism（伝統主義）廃止 | 維新後・列強化前 | je_meiji_diplomacy（外交承認）の完了条件 `[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_diplomacy]` |
| 中 | law_hereditary_bureaucrats → 実力制の官僚 | 中盤 | 行政効率の向上。ig_intelligentsia の支持が必要 |
| 中 | 教育制度（寺子屋 → 公共学校） | 中盤 | 識字率向上。law_terakoya は日本固有の初期学制 `[src: history/countries/jap - japan.txt]` |
| 低 | 選挙制度改正 | 終盤 | 政治安定に寄与。急ぐ必要なし |

> **幕府特性**: law_bakufu は progressiveness -100 だが、正当性 +30、権力 +200 という強力な統治ボーナスを持つ（コミュニティ知見：law_bakufu の正当性 +30・権力 +200 はスクリプト確認済みの数値だが、該当ファイルの行番号は未確認のため `[src: common/laws/00_social_hierarchy.txt]`（行番号未検証））。帝政ルートを狙う場合は月次パルス条件を満たした上で廃止する。

---

## よくあるミス

### 日本固有

| NG 行動 | 理由 |
|---------|------|
| 維新 JE を発動する前に鎖国を解除しない | je_sakoku 未完了のまま進めると維新 JE の可能条件（鎖国系法律でないこと）を満たせない `[src: common/journal_entries/00_meiji_restoration.txt]` |
| 帝政ルート中に条約港を受け入れる | je_meiji_imperial_marriage（公武合体ルート専用 JE）の完了条件に treaty_port なしが必要。帝政ルート中でも条約港の存在が JE フローの邪魔になる `[src: common/journal_entries/00_meiji_restoration.txt, je_meiji_imperial_marriage]` |
| ig_landowners（大名）を急激に弱体化させる | 維新 JE の月次パルス条件「ig_landowners リーダーが非徳川」は必要だが、大名 IG 自体を壊滅させると不安定化する。維新完了後は ig_kazoku（華族）に変わるため段階的対応で十分 `[src: common/interest_groups/00_landowners.txt:342-356]` |
| 武士訓練 PM を維新後も放置する | je_meiji_army の完了条件として「武士訓練 PM を持つ兵舎の不在」が要求される。早めに PM を切り替える `[src: common/production_methods/05_military.txt:144]` |
| 維新完了後に ig_industrialists / ig_intelligentsia の承認を無視する | 帝政勝利報酬として meiji_favored_ig 修正値（IG 政治力 +50%）が付与される IG が優先 IG として選ばれる。維新後の法律改正を推し進めるためにこれらの IG の支持を維持する `[src: common/journal_entries/00_meiji_restoration.txt, on_complete]` |
| je_sakoku fail 条件（君主制廃止）を無視する | 君主制を廃止すると je_sakoku が失敗し sakoku_entrenched_modifier（保守化ペナルティ）が付与される `[src: common/journal_entries/07_sakoku.txt]` |

### VIC3 全般

| NG 行動 | 理由 |
|---------|------|
| 建設キューを空にする | 常に何か建てていないと成長が止まる |
| 法律を一度に大量に変える | 急進派が爆発して内戦になる |
| 外交戦を無計画に始める | 味方が少ないと戦争で不利 |
| 非承認国家（Unrecognized）のまま拡張する | 外交戦の起票権が制限される。Recognized 昇格を最優先に |
| 商品価格を無視する | 供給過多 or 不足で経済が崩壊する |

---

## 用語対照表

> 完全版は [localization-reference.md](../vic3/localization-reference.md) を参照。以下は日本攻略ガイド固有の用語のみ抜粋。

| 日本語（ゲーム内） | 英語 / スクリプトキー | 補足 |
|-----------------|----------------------|------|
| 幕府 | law_bakufu | 日本のみ表示の政体法。progressiveness -100、正当性 +30、権力 +200 `[src: common/laws/00_social_hierarchy.txt]`（行番号未検証） |
| 鎖国 | law_sakoku | 日本文化専用の貿易政策法。Dejima のみ取引所建設可 `[src: common/laws/00_trade_policy.txt:290]` |
| 大名（→ 維新前の地主 IG 名称） | ig_daimyo | 維新完了後は ig_kazoku（華族）に変わる `[src: common/interest_groups/00_landowners.txt:342]` |
| 華族 | ig_kazoku | 維新後の地主 IG 名称。ideology → ideology_hierarchic `[src: common/journal_entries/00_meiji_restoration.txt]` |
| 武士階級 | law_warrior_caste | 日本文化のみ表示の軍制法。pm_samurai_training をアンロック |
| 武士訓練 | pm_samurai_training | law_warrior_caste 時のみ利用可能な兵舎の製造方法 `[src: common/production_methods/05_military.txt:144]` |
| 寺子屋 | law_terakoya | 日本固有の初期教育法 `[src: history/countries/jap - japan.txt]` |
| 新選組 | law_shinsengumi | 治安法。law_bakufu 時にアンロック `[src: common/laws/00_internal_security.txt, law_shinsengumi]`（行番号未検証） |
| 出島 | Dejima | law_sakoku 時に唯一取引所を建設可能な場所 `[src: common/laws/00_trade_policy.txt:290]` |
| 条約港 | Treaty Port / treaty_port | 列強が強制設置できる外交合意。je_meiji_imperial_marriage の完了を阻害 `[src: common/treaty_articles/14_treaty_port.txt]` |
| 強制開国 | forced_market_opening | 条約で市場を強制された時の修正値。威信 -25% `[src: common/static_modifiers/00_code_static_modifiers.txt:861]` |
| 公武合体 | kobu_gattai | 幕府勝利分岐A の変数名 `[src: common/journal_entries/00_meiji_restoration.txt]` |
| 公議輿論 | kogi_yoron | 幕府勝利分岐B の変数名 `[src: common/journal_entries/00_meiji_restoration.txt]` |
| 神仏分離 | je_shinbutsu_bunri | 神道優先の宗教 JE `[src: common/journal_entries/07_japanese_religion.txt]` |
| 檀家制度 | je_elevate_buddhism | 仏教優先の宗教 JE `[src: common/journal_entries/07_japanese_religion.txt]` |
| 岩倉使節団 | je_iwakura_mission | DLC 専用の外交承認 + 技術加速 JE `[src: common/journal_entries/07_iwakura_mission.txt]` |
| プロミネンス | Prominence | 1.13 追加。政治家の政治機構内での影響力。IG 指導者選出の主因 `[src: common/interest_groups/00_landowners.txt:752-761]`（プロミネンス補正の詳細パラメータはスクリプト未確認。`[src: Patch_1.13 wiki]` も参照） |
| 砲撃外交 | Gunboat Diplomacy | 1.13 追加。条約交渉時に海上敵対行動を脅迫オプションとして提示 `[src: Patch_1.13 wiki]` |
| 戦略的関心度 | Strategic Interest | 1.13 でティアド化。地域への関与度の階層指標 `[src: Patch_1.13 wiki]` |
| 非承認国家 | Unrecognized | 国際社会で承認されていない国家。外交戦起票権が制限される |
| 承認国 | Recognized | 国際社会で承認された国家 |

---

## 出典

### 一次情報（ゲームスクリプト・公式）

Section A / B / C 全体で参照したスクリプトファイルを一括収録する。

- `common/journal_entries/00_meiji_restoration.txt` — 明治維新 JE 本体（je_meiji_restoration, je_meiji_main, je_meiji_economy, je_meiji_army, je_meiji_diplomacy, je_meiji_imperial_marriage）
- `common/journal_entries/07_sakoku.txt` — 鎖国 JE（je_sakoku）
- `common/journal_entries/07_japanese_religion.txt` — 宗教 JE（je_shinbutsu_bunri, je_elevate_buddhism）
- `common/journal_entries/07_iwakura_mission.txt` — 岩倉使節団 JE（je_iwakura_mission）
- `common/journal_entries/07_korea_colonization.txt` — 朝鮮植民地化 JE（je_colonize_korea）
- `common/laws/00_trade_policy.txt` — 貿易政策法律定義（law_sakoku:290、law_isolationism:159）
- `common/production_methods/05_military.txt` — 武士訓練 PM（pm_samurai_training:144）
- `common/interest_groups/00_landowners.txt` — 大名 IG 定義（:342-356）、プロミネンス加算（:752-761）
- `common/character_traits/special_personality_traits.txt` — 天皇 trait（special_character_japanese_emperor:673）
- `common/static_modifiers/00_code_static_modifiers.txt` — forced_market_opening（:861）
- `common/static_modifiers/00_ep2_04_modifiers.txt` — modifier_court_and_shogunate, modifier_continuity_and_enlightenment, modifier_taikun_monarchy, modifier_veiled_by_awe, modifier_namamugi_incident_prestige_loss, modifier_tairo_assassinated, modifier_shinsengumi_crackdown, meiji_favored_ig
- `common/static_modifiers/00_ep2_06_modifiers.txt` — arahitogami, extended_danka_system
- `common/treaty_articles/14_treaty_port.txt` — 条約港定義
- `common/characters/country_jap.txt` — 日本固有キャラクターテンプレート（105 件）
- `history/countries/jap - japan.txt` — 日本の開始法律セット、je_sakoku 付与（行 43）
- `dlc_metadata/00_dlc_metadata.txt` — DLC 構成確認（dlc018 = The Great Wave / ep2_content）
- [Patch 1.13 - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Patch_1.13)
- [Japan - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Japan)

### コミュニティ情報（補足知見）

プレイ報告・体感ベースの情報。条件の裏取りには一次情報を参照のこと。

- 砲撃外交・クーデター扇動の具体的な発動条件・コストはスクリプト未確認。パッチノート（1.13 wiki）からの推測ベース
- ナポレオン戦争技術（je_meiji_army 完了条件）の正確なスクリプト ID は未確認。一次情報で後日確認予定
- 列強化前の Force Recognition 開戦リスクはコミュニティの経験則。具体的な介入閾値はスクリプト未確認
- Recognized 昇格後の外交戦起票権拡大の範囲はコミュニティ知見ベース
