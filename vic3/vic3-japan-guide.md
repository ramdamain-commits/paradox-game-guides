# VIC3 日本攻略ガイド（Patch 1.13.8 + EP2 The Great Wave 時点）

> 鎖国下の幕府日本（1836年）から明治維新を経て列強入りまで、EP2 DLC の日本固有メカニクスを軸に整理する。
> 2026-06-01 確認時点。インストール版 **Patch 1.13.8（Matcha）+ The Great Wave（dlc018 / ep2_content）** のゲームスクリプトで全数値を再検証済み。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。

---

## パッチ差分（1.13 + EP2 で日本に効いた変更）

1.13（Matcha）は海軍刷新と **The Great Wave**（EP2）が主題。日本は今パッチの最大受益国であり、固有メカニクスの大部分が EP2 コンテンツとして追加・整備された。

| 変更・追加 | 日本への影響 |
|-----------|------------|
| **The Great Wave DLC（EP2 = dlc018）追加** | 明治維新 JE（ジャーナルエントリ / je_meiji_restoration）、鎖国 JE（je_sakoku）、岩倉使節団 JE（je_iwakura_mission）、日本固有法律、宗教 JE が DLC ありで有効化 `[src: dlc_metadata/00_dlc_metadata.txt, dlc018]` |
| **日本固有法律の追加** | 幕府（law_bakufu）・鎖国（law_sakoku）・寺子屋（law_terakoya）・武士階級（law_warrior_caste）・新選組（law_shinsengumi）が日本文化専用で実装。通常の孤立主義（law_isolationism）より強力な制限を持つ `[src: common/laws/00_trade_policy.txt:290, common/laws/00_distribution_of_power.txt:114]` |
| **明治維新 JE の帝政・幕府の2分岐** | 維新側（帝政勝利）と幕府側（公武合体／公議輿論）の2ルートが完全実装 `[src: common/journal_entries/00_meiji_restoration.txt]` |
| **岩倉使節団 JE（DLC 専用）** | 技術研究ボーナス（生産系・社会系）を累積付与 `[src: common/journal_entries/07_iwakura_mission.txt, common/static_modifiers/00_ep2_04_modifiers.txt:156-165]` |
| **海軍刷新（全国共通）** | 艦船デザイナー・旗艦（Flagship）・新型艦が追加。**日本固有の艦種・海軍 modifier は存在しない**（スクリプト全走査で JAP 固有エントリなし）`[src: common/ship_types/, common/ship_modifications/, common/combat_unit_types/]` |
| **プロミネンス（Prominence）導入** | 利益団体（IG = Interest Group）指導者選出の主因が変更。日本では大名キャラクターのリーダー選出重み（magnate_leader_weight）に固有加算あり（後述）`[src: common/interest_groups/00_landowners.txt:751-762]` |
| **単一指揮官制** | 軍事編成（Military Formation）あたり指揮官1名に変更。武士訓練（pm_samurai_training）が生きる維新前の軍事運用に影響（コミュニティ知見：1.13 wiki ベース） |

> DLC なし環境では上記の日本固有 JE・法律・宗教 JE の大部分が無効化される。本ガイドは **EP2（The Great Wave）あり**を前提とする。

---

## 開始状況（1836年）

| 項目 | 値 |
|------|-----|
| 国家タグ | JAP |
| 政体 | 君主制（law_monarchy） |
| 首都 | 関東（STATE_KANTO、江戸） |
| 主要文化 | 日本（Japanese） |
| 統治機構の法 | 幕府（law_bakufu）※ progressiveness -100、正当性 +30、権力 +200 `[src: common/laws/00_distribution_of_power.txt:114]` |
| 貿易政策の法 | 鎖国（law_sakoku）※ 日本文化＋九州（STATE_KYUSHU）所持時のみ表示。前提に伝統主義（law_traditionalism）が必要 `[src: common/laws/00_trade_policy.txt:290-300]` |
| 経済システムの法 | 伝統主義（law_traditionalism） `[src: common/laws/00_economic_system.txt:5]` |
| 承認状況 | 未承認（Unrecognized） |
| 支配者 | 徳川家斉（JAP_ienari_tokugawa、ruler） `[src: common/character_templates/country_jap.txt:187]` |
| 後継者 | 徳川家慶（JAP_ieyoshi_tokugawa、heir） `[src: common/character_templates/country_jap.txt:213]` |

### 周辺国との関係

| 方角 | 隣国・勢力 | 初期の関係性 |
|------|-----------|------------|
| 北 | ロシア（RUS） | 列強。サハリン・北海道方面で摩擦。列強化前の正面衝突は避ける |
| 西 | 清（CHI） | 同じ東アジアの大国。序盤ははるかに格上で、敵対は危険 |
| 南西 | イギリス（GBR） | 最大の列強。開国圧力の主体になりやすい（コミュニティ知見） |
| 東 | アメリカ（USA） | ペリー来航相当の開国圧力の使い手候補（コミュニティ知見） |
| 朝鮮半島 | 朝鮮（KOR） | 中盤の大陸経営の焦点。je_colonize_korea の対象 |

### 初期の強み・弱み

| 強み | 弱み |
|------|------|
| 幕府法で正当性 +30・権力 +200 `[src: common/laws/00_distribution_of_power.txt:114]` | 鎖国法で影響力 -50%・技術伝播 -20%・交易容量 -75% `[src: common/laws/00_trade_policy.txt:290]` |
| 武士訓練（pm_samurai_training）で高い訓練効率（+25 unscaled、レベルごと +5）`[src: common/production_methods/05_military.txt:144]` | 未承認（Unrecognized）状態で外交的選択肢が大きく制限される |
| 固有キャラクターテンプレートが豊富。維新後に近代化人材が多数登用可能 `[src: common/character_templates/country_jap.txt]` | 鎖国は九州外での交易を禁止（country_disallow_trade_outside_kyushu_bool）し、積極的な外交プレイも禁止する `[src: common/laws/00_trade_policy.txt:290]` |
| 維新完了後に実業家（ig_industrialists）または知識人（ig_intelligentsia）へ meiji_favored_ig 修正値で政治力 +50%（very_long）`[src: common/static_modifiers/content_1_modifiers.txt:122]` | 開国すると列強との技術・軍事格差が顕在化する |

### IG 構造の特殊性（大名・将軍・天皇）

日本の IG 構造はゲーム中最も固有色が強く、維新成否を左右するため事前理解が重要。

**大名（ig_daimyo）— 地主（Landowners）の日本名称**
開始時の地主（ig_landowners）は日本の主文化時に **大名（ig_daimyo）** と表示される `[src: common/interest_groups/00_landowners.txt:342-356]`。大名 IG は状態に応じて 2 つのトレイトを切り替える。

| トレイト | 発動条件 | 効果 |
|------------|---------|------|
| 普代大名支持（ig_trait_fudai_support） | 承認度 happy 以上 | 行政力 +5%・権力（Authority）+5% `[src: common/interest_group_traits/00_landed_interest_traits.txt:123]` |
| 外様発言力（ig_trait_outspoken_tozama） | 承認度 unhappy 以下 | 権力 -5%・徴兵率 -10% `[src: common/interest_group_traits/00_landed_interest_traits.txt:133]` |

- 大名 IG は**不満時に外様トレイトで権力（Authority）を削り、満足時に普代トレイトで権力を補強する**。維新で大名を与党から外す際、不満状態を長引かせると権力ペナルティが蓄積する。
- **指導者選出重みの加算**: c:JAP かつ維新未完了（japan_restoration_complete 変数なし）の場合、大名（magnate）リーダーの選出重み（magnate_leader_weight）に +5 され合計 10.0 になる `[src: common/interest_groups/00_landowners.txt:751-762]`。これは IG のプロミネンス（pop_weight）そのものへの加算ではなく、**大名キャラクターが地主 IG の指導者に選ばれやすくなる**効果である。
- 維新完了後は名称が **華族（ig_kazoku）** に変わり、ideology も通常地主と同じ ideology_hierarchic になる `[src: common/journal_entries/00_meiji_restoration.txt, on_complete]`

**将軍・天皇キャラクター**

- ruler は徳川家斉（11代）。徳川将軍系はイベントで歴史的に交代する `[src: common/character_templates/country_jap.txt]`
- 孝明天皇（JAP_komei_yamato）・明治天皇（JAP_meiji_yamato）は character_role_emperor_of_japan を持ち、`special_character_japanese_emperor` トレイト（正当性 +5）が維新 JE の complete 判定（ruler = 天皇）に使われる `[src: common/character_templates/country_jap.txt:50,79, common/character_traits/special_personality_traits.txt:673]`
- 維新後に登用できる近代化人材: 福沢諭吉・大隈重信・原敬・岩倉具視（知識人系）、山縣有朋・伊藤博文（軍部・政治）、東郷平八郎（提督）・乃木希典（将軍）`[src: common/character_templates/country_jap.txt]`

---

## Day 1（ポーズ解除直後）

1. **維新 JE（je_meiji_restoration）の状態を確認する**
   - 表示条件: c:JAP、君主制（law_monarchy）、幕府法（law_bakufu）、japan_restoration_complete 変数なしの4点 `[src: common/journal_entries/00_meiji_restoration.txt:26-31]`
   - possible 条件は **孤立主義（law_isolationism）でないこと** `[src: common/journal_entries/00_meiji_restoration.txt:33-37]`。鎖国（law_sakoku）は孤立主義の一種（スクリプト上 parent = law_isolationism）として扱われるため、ゲーム開始直後は JE が表示されても可能条件を満たさない
   - まず開国（鎖国法の廃止）を中期目標として設定する

2. **鎖国 JE（je_sakoku）の状態を確認する**
   - DLC あり時は history 経由で開始時に付与される `[src: common/journal_entries/07_sakoku.txt:6]`
   - 失敗すると鎖国維持派 IG に sakoku_entrenched_modifier（政治力 +25%）が付くため、維新路線なら早期に法律変更を進める `[src: common/journal_entries/07_sakoku.txt:66, common/static_modifiers/00_ep2_05_modifiers.txt:32]`

3. **大名 IG（ig_daimyo）の承認度を確認する**
   - happy 以上で普代トレイト（権力・行政力 +5%）、unhappy 以下で外様トレイト（権力 -5%・徴兵率 -10%）が発動 `[src: common/interest_group_traits/00_landed_interest_traits.txt:123-141]`
   - 承認度ラインを把握し、法律改正と並行した IG 管理方針を立てる

4. **建設キューに国内完結型の優先施設を入れる**
   - 鎖国中は交易容量 -75%・九州外の交易禁止のため、建設局・工具工場・農地・大学から始める（コミュニティ知見）

5. **法律改正の順序を計画する**
   - 鎖国廃止（→ law_mercantilism）→ 伝統主義廃止 → 幕府廃止が維新ルートの基本（詳細は「技術・法律」を参照）

6. **将軍と天皇の両キャラクターを把握する**
   - 徳川家斉（ruler）の死亡タイミングと後継者（家慶）を確認。地主 IG リーダーを非徳川にすることが維新カウンター進行の必要条件 `[src: common/journal_entries/00_meiji_restoration.txt:79-108]`

---

## 時系列戦略

各フェーズの概要を示す。メカニクスの完全データは「固有イベント時系列」「技術・法律」を参照。

### 序盤（1836〜1860）: 開国対応と国力蓄積

ゲーム開始時の日本は **鎖国（law_sakoku）**・**幕府（law_bakufu）**・**伝統主義（law_traditionalism）** の三重拘束下にある。鎖国は権力（Authority）+25%（幕府法の +200 とは別系統）と引き換えに交易容量 -75%・影響力 -50%・技術伝播 -20%・輸出入関税 +50% という極端な閉鎖体制であり `[src: common/laws/00_trade_policy.txt:290]`、列強からの開国圧力は時間の問題。

| 時期 | 目標 |
|------|------|
| 1836-1840 | 建設局を即時拡張。寺子屋（law_terakoya）の識字補正を活かして技術研究を開始 |
| 1840-1850 | 外交戦に備え権力・正当性を蓄積。幕府法の正当性 +30・権力 +200 を序盤の盾に使う |
| 1850-1860 | 列強に条約港を強要される前に貿易政策を見直す。自発的に鎖国を廃止すれば je_sakoku が完了し、鎖国廃止支持 IG に the_picked_lock_modifier（政治力 +25%）が付く `[src: common/journal_entries/07_sakoku.txt:32]` |

**鎖国解除の判断基準**（コミュニティ知見）
- 列強の外交戦で条約港を強制される前に自発的に鎖国を廃止すると、forced_market_opening（威信 -25%）を回避できる `[src: common/static_modifiers/00_code_static_modifiers.txt:863]`
- 鎖国の廃止先は law_mercantilism が最も移行しやすい。一気に自由化すると IG 不満が急増するため段階的に進める `[src: common/laws/00_trade_policy.txt:5]`

### 中盤（1860〜1880）: 明治維新と内戦処理

日本プレイの最重要局面。維新 JE が表示されると尊皇攘夷運動が生まれ、月次パルスで restoration_timer_var が進む。**天皇が統治者・幕府廃止・内戦なし・地主 IG リーダーが非徳川**の4条件を満たす月だけカウントが進み、累積 6 に達した月のパルスで維新完了判定が立つ `[src: common/journal_entries/00_meiji_restoration.txt:79-128]`。条件を満たさない月があるとカウントは進まないため、実時間では 6 ヶ月以上かかりうる。完全な分岐・報酬データは「固有イベント時系列」を参照。

- 維新を急いで大名 IG を壊滅させると内戦リスクが上がる。維新前は大名を「happy だが過度に満足させない」水準に保つのが安定運用（コミュニティ知見）
- 内戦中は restoration_timer_var のインクリメントが止まる。早期終結が維新完了の近道（コミュニティ知見）
- DLC あり時は岩倉使節団 JE で技術研究を加速できる（後述）

### 終盤（1880〜1936）: 列強入りと帝国運営

維新完了後は je_meiji_main の 3 サブ JE（経済・軍制・外交）を 4380 日（約 12 年）以内に完了させるのが最優先 `[src: common/journal_entries/00_meiji_restoration.txt:640-742]`。

- 列強認知（recognized）を得るには je_meiji_diplomacy を完了させる。条約港が残っていると外交承認の障害になるため事前に解消する
- 朝鮮・大陸経営（je_colonize_korea）は朝鮮州への鉄道建設で進む `[src: common/journal_entries/07_korea_colonization.txt:132]`
- 宗教 JE（神仏分離 / 仏教振興）で長期修正値を獲得する（後述）

---

## 内政・経済

> VIC3 は経済がゲームの中心。日本は鎖国解除と維新完了のフェーズによって建設優先順位が変化する。

### 建設の優先順位

**鎖国期（1836〜開国まで）** — 交易が制限されるため国内完結型の産業基盤を優先

| 順位 | 施設 | 理由 |
|------|------|------|
| 1 | 建設局（Construction Sector） | 全経済発展の基盤（コミュニティ知見） |
| 2 | 農地・水田（Farms / Rice Paddies） | 食料と農民の維持。人口増加基盤 |
| 3 | 工具工場（Tool Workshops） | 建設用工具を国内調達 |
| 4 | 大学（Universities） | 寺子屋の識字補正と組み合わせ、技術伝播 -20% を補う |

**開国後〜維新前** — 維新を見据えた都市中枢・鉄道の先行投資を開始

| 順位 | 施設 | 理由 |
|------|------|------|
| 1 | 建設局 | 継続拡張 |
| 2 | 都市中枢（Urban Center） | je_meiji_economy 条件（incorporated 州の 70% 超に level 5+ 都市中枢）の先行投資 `[src: common/journal_entries/00_meiji_restoration.txt:754]` |
| 3 | 鉄道（Railway） | je_meiji_economy 条件（同 70% 超に鉄道）の先行投資 |
| 4 | 製鉄所・鉄山（Steel Mill / Iron Mine） | 鉄道・工場建設の鋼材確保 |

**維新完了後** — meiji_favored_ig（実業家または知識人の政治力 +50%）の追い風を活かす

| 順位 | 施設 | 理由 |
|------|------|------|
| 1 | 鉄道 | 大陸鉄道（朝鮮 JE 含む）と je_meiji_economy の完結 |
| 2 | 工場系全般 | 実業家が与党になれば近代化を牽引 |
| 3 | 港湾・海軍基地 | 海軍整備と対外貿易の拡大 |
| 4 | 大学 | 岩倉使節団ボーナスと合算して技術研究を最大化 |

### 利益団体（IG）管理

日本の IG 管理は維新前後で構造が大きく異なり、大名（ig_daimyo）→ 華族（ig_kazoku）の遷移を軸に立てる。

**維新前: 大名 IG の扱い**（普代/外様トレイトの数値は「開始状況」参照）
- 維新完了には「大名 IG リーダーを非徳川」にする必要がある。徳川リーダーが続く場合、IG 内の別人物の指導者選出を狙う。大名は magnate_leader_weight +5 で指導者になりやすい構造のため、徳川以外の大名キャラクターを育てる `[src: common/interest_groups/00_landowners.txt:751-762]`
- 大名を野党に置くと維新カウンターは進むが急進化が高まる。関係を壊しすぎると内戦リスクが上がる（コミュニティ知見）

**維新後: 華族（ig_kazoku）への遷移**
- 維新完了で ig_landowners が ig_kazoku に変わり ideology_hierarchic に更新 `[src: common/journal_entries/00_meiji_restoration.txt, on_complete]`
- 優先 IG（実業家または知識人）が政治力 +50% を得るため、華族は相対的に弱体化する。優先 IG と連立して法律改正を一気に進めるウィンドウを活かす

**その他の主要 IG**

| IG | 維新前の役割 | 維新後の役割 |
|----|------------|------------|
| 軍部（ig_armed_forces） | 維新支持派に取り込む | je_meiji_army では一時的に野党化が必要。改革完了後に与党へ戻す |
| 実業家（ig_industrialists） | 工業化で徐々に育てる | meiji_favored_ig 付与時に与党化、近代化を牽引 |
| 知識人（ig_intelligentsia） | 維新運動の知的バック | meiji_favored_ig 対象なら法律制定時間が短縮 |
| 信者（ig_devout） | 宗教 JE の選択次第で重要度が変化 | 仏教振興 JE では 60 ヶ月分の強力維持が必要 |

---

## 外交・同盟

### 必須外交

| 対象 | 行動 | 理由 |
|------|------|------|
| 清（CHI） | 中立〜友好を維持 | 序盤ははるかに格上。敵対は即戦争リスク |
| 朝鮮（KOR） | 影響力確保 → 属国化を検討 | je_colonize_korea は朝鮮州への鉄道建設で進行 `[src: common/journal_entries/07_korea_colonization.txt:132]` |
| イギリス（GBR） | 好意的中立を維持 | 開国圧力・条約港強要の主体になりやすい列強筆頭（コミュニティ知見） |
| ロシア（RUS） | 勢力圏の重複に注意 | 北方・朝鮮半島で利害が衝突。列強化前の正面衝突は避ける |
| アメリカ（USA） | 開国・通商交渉の窓口 | ペリー来航相当の開国圧力の使い手候補（コミュニティ知見） |

> **大原則**: 日本は未承認（Unrecognized）で開始する。承認国（Recognized）になるまで攻撃的な外交戦の起票が制限される。最優先は承認ルートの確保。

### 開国 → 承認（Recognized）への道

日本が外交的制約から脱するには段階的プロセスが必要。

1. **開国（鎖国法の廃止）**: je_sakoku の完了条件。影響力・外交選択肢が回復する `[src: common/journal_entries/07_sakoku.txt:25]`
2. **伝統主義（law_traditionalism）廃止**: je_meiji_diplomacy の完了条件の一つ `[src: common/journal_entries/00_meiji_restoration.txt:856]`
3. **非従属（non-subject）かつ認知（recognized）の達成**: je_meiji_diplomacy の完了で recognized 状態に到達する `[src: common/journal_entries/00_meiji_restoration.txt:856-860]`
4. **DLC あり時**: 岩倉使節団 JE（je_iwakura_mission）で外交承認の流れに技術加速が伴う（後述）

> **承認の取得経路に注意**: VIC3 1.13.8 には「force_recognition」という外交プレイ／開戦事由は**存在しない**（diplomatic_plays・war_goal_types のいずれにも該当 ID なし）`[src: common/diplomatic_plays/00_diplomatic_plays.txt, common/war_goal_types/]`。日本の承認は基本的に **je_meiji_diplomacy の完了**で達成する。「承認の強要」はゲーム内の慣用表現であってスクリプト ID ではない（コミュニティ知見）。

### 条約港（Treaty Port）対策

- 列強は外交プレイ dp_take_treaty_port（戦争目標 take_treaty_port）で日本に条約港を強制取得できる `[src: common/diplomatic_plays/00_diplomatic_plays.txt:315, common/war_goal_types/25_take_treaty_port.txt]`
- 条約港は **公武合体ルート（je_meiji_imperial_marriage）** の完了を妨害する。完了条件に「本土州に条約港なし」が含まれる `[src: common/journal_entries/00_meiji_restoration.txt:572]`
- 条約港が強制履行・撤回されると、その州に領有権主張（claim）が自動付与される `[src: common/treaty_articles/14_treaty_port.txt:216-229]`
- 強制開国を受けると forced_market_opening（威信 -25%）が付与される。鎖国の解除タイミングを慎重に選ぶ `[src: common/static_modifiers/00_code_static_modifiers.txt:863]`

### 1.13 で増えた外交手段

| 手段 | 日本での使い道 | スクリプト確認 |
|------|--------------|------|
| 砲撃外交（Gunboat Diplomacy） | 沿岸国への条約交渉時の脅迫オプション。海軍が整い次第、朝鮮への影響力確保に活用 | 専用 DP ではなく `can_threaten_naval_hostilities` ルール経由 `[src: common/scripted_rules/00_scripted_rules.txt:226]`（必要海軍規模はコミュニティ知見） |
| 戦略的関心度（Strategic Interest） | 列強の関与が低い時期を狙って沿岸地域へ外交戦 | interest_marker として実在 `[src: common/scripted_effects/00_victoria_great_game_scripted_effects.txt]` |
| クーデター扇動（Orchestrate Coup） | 友好ロビーを持つ弱小国の政体転換に活用 | 専用外交アクションとして実在 `[src: common/diplomatic_actions/57_orchestrate_coup.txt]`（コストはコミュニティ知見） |

---

## 軍事ドクトリン（陸軍・海軍）

### 指揮官運用（1.13 単一指揮官制）

1.13 で軍事編成（Military Formation）あたりの指揮官は **1 名のみ**になった。少数精鋭の将軍・提督を昇進させて運用するのが基本（コミュニティ知見 `[src: Patch_1.13 wiki]`）。陸軍将軍と海軍提督は兼任できないため、両系統のキャラクターラインを分けて育てる。

| テンプレートID | 人物 | 用途 |
|---|---|---|
| JAP_yamagata_aritomo | 山縣有朋 | 陸軍。軍制改革の主導者 `[src: common/character_templates/country_jap.txt:1896]` |
| JAP_ito_hirobumi | 伊藤博文 | 政治家兼軍人 `[src: common/character_templates/country_jap.txt:1923]` |
| JAP_nogi_maresuke | 乃木希典 | 陸軍将軍 `[src: common/character_templates/country_jap.txt:2399]` |
| JAP_togo_heihachiro | 東郷平八郎 | 海軍提督 `[src: common/character_templates/country_jap.txt:2370]` |

- 不要な昇進は軍部（Armed Forces）IG の承認低下を招くため、必要になってから階級を上げる（コミュニティ知見）
- 旗艦（Flagship）を指定した艦隊の提督が戦死すると威信喪失リスクが高い。旗艦艦隊には最も能力の高い提督を充てる（コミュニティ知見）

### 日本固有の陸軍 PM（製造方法 / Production Method）: 武士訓練（pm_samurai_training）

- 武士階級法（law_warrior_caste）が有効な間のみアンロック `[src: common/production_methods/05_military.txt:144]`
- 訓練効率 building_training_rate_add = +25（unscaled）、レベルごと +5。士官 25% / 兵士 75%
- **維新後の注意**: je_meiji_army の完了条件に「pm_no_organization または pm_samurai_training を持つ兵舎が存在しないこと」が含まれる `[src: common/journal_entries/00_meiji_restoration.txt:797-823]`。維新を完成させるには武士訓練 PM を停止し近代兵制へ切り替える

### 兵科方針（陸軍）

| 兵種 | 序盤方針 | 備考 |
|------|---------|------|
| 非正規軍（Irregular Infantry） | 維新前の主力。安価だが弱い | je_meiji_army は**各軍編成の**非正規歩兵 25% 未満を要求（全軍合計ではない）。維新後は早期に置換 `[src: common/journal_entries/00_meiji_restoration.txt:797]` |
| 戦列歩兵（Line Infantry） | 維新後の主力。技術でアップグレード優先 | ナポレオン戦争技術（napoleonic_warfare）が je_meiji_army 条件 `[src: common/technology/technologies/20_military.txt:118]` |
| 騎兵 | 機動力補完として少数維持 | 島嶼地形では効果が限定的 |
| 大砲（カノン砲 → 後装砲） | 技術が進むほど有利 | Era 2 の後装砲技術を優先 |

### 海軍ドクトリン（1.13 海軍改修）

1.13 で艦船デザイナー・旗艦・新型艦・砲撃外交が追加された。ただし **日本固有の艦種・海軍 modifier・海軍 decision はスクリプト上に一切存在しない** `[src: common/ship_types/, common/ship_modifications/, common/combat_unit_types/, common/static_modifiers/00_ep2_04_modifiers.txt, 00_ep2_06_modifiers.txt]`。日本は全国共通の海軍システムをそのまま使い、強化は技術研究・建造物投資・艦船デザイナーのカスタマイズで行う。

| フェーズ | 優先度 | 方針 |
|---------|--------|------|
| 序盤（1836〜1860） | 低 | 鎖国解除・維新優先。海軍は沿岸防衛最小限。鎖国中は外洋展開が事実上不可 |
| 中盤（1860〜1900） | 中 | 維新後に中型艦を整備。対清・対朝鮮の制海権確保。朝鮮 JE の補給路防衛に制海権が効く |
| 終盤（1900〜1936） | 高 | 艦船デザイナーで主力艦を最適化。旗艦を1隻指定して威信獲得を狙う |

> 陸軍主体の維新序盤に海軍投資を急ぐと建設キューを圧迫する。内政・法律改正が一段落してから本格整備に移るのが安定する（コミュニティ知見）。

---

## 固有イベント時系列

### 明治維新 JE（je_meiji_restoration）攻略チャート

#### 発動条件

| 条件 | 説明 | 出典 |
|------|------|------|
| 表示（is_shown_when_inactive） | c:JAP / law_monarchy / law_bakufu / japan_restoration_complete 変数なし | `[src: 00_meiji_restoration.txt:26-31]` |
| 可能（possible） | 孤立主義（law_isolationism）でないこと。鎖国は law_isolationism を parent とするため、開国が前提 | `[src: 00_meiji_restoration.txt:33-37]` |

#### 維新カウンター（月次パルス）

毎月、以下の4条件をすべて満たす月だけ restoration_timer_var が +1 され、**累積 6 で完了判定**が立つ `[src: 00_meiji_restoration.txt:79-128]`。

1. 天皇が統治者（ruler が special_character_japanese_emperor trait 持ち）
2. 幕府法（law_bakufu）が廃止されている
3. 内戦がない
4. 地主 IG（大名）のリーダーが**非徳川**（house_tokugawa 変数なし）

#### 主要分岐

| 分岐 | 前提条件 | 達成期限 | 勝利結果 |
|------|---------|---------|--------|
| **帝政（維新）勝利** | 天皇が ruler、幕府廃止、内戦なし、地主リーダー非徳川を 6 ヶ月分維持 | — | 首都→東京、ig_landowners → ig_kazoku（華族・ideology_hierarchic）、meiji_favored_ig（実業家 or 知識人の政治力 +50%、very_long）`[src: 00_meiji_restoration.txt:130-240, content_1_modifiers.txt:122]` |
| **公武合体（幕府ルートA）** | 幕府維持 + 天皇婚姻完了 + 本土州に条約港なし | je_meiji_imperial_marriage タイムアウト 1825 日（5年）`[src: 00_meiji_restoration.txt:633]` | modifier_court_and_shogunate: 権力 +10%・士官政治力 +25%・貴族政治力 -25% `[src: 00_ep2_04_modifiers.txt:125-130]` |
| **公議輿論（幕府ルートB）** | 選挙権あり + 天皇復位 + 地主 IG 与党かつ徳川リーダー | 維新 JE の fail 分岐 | modifier_continuity_and_enlightenment（正当性 +10・技術伝播 +25%・近代主義者 pop support +15%）または modifier_taikun_monarchy（正当性 +5・影響力 +10%）`[src: 00_ep2_04_modifiers.txt:137-148]` |

#### 維新本体完了後のサブ JE（je_meiji_main）

je_meiji_restoration 完了で je_meiji_main が発動。meiji_var を 0→3 にするのが目標。タイムアウト 4380 日（約 12 年）。完了済みサブ JE があれば meiji.2、全未完了なら meiji.14 イベント `[src: 00_meiji_restoration.txt:640-742]`。

| サブ JE | 完了条件 | 出典 |
|---------|---------|------|
| je_meiji_economy（経済近代化） | incorporated 州の 70% **超**（>0.7、ちょうど 70% は不可）に level 5+ 都市中枢かつ鉄道 | `[src: 00_meiji_restoration.txt:754-766]` |
| je_meiji_army（軍制改革） | 農奴制/徴兵農民廃止、軍部野党化、ナポレオン戦争技術（napoleonic_warfare）、武士訓練 PM・pm_no_organization の兵舎なし、各軍編成の非正規歩兵 < 25% | `[src: 00_meiji_restoration.txt:797-823]` |
| je_meiji_diplomacy（外交承認） | 伝統主義（law_traditionalism）廃止、非従属（is_subject = no）、認知（recognized） | `[src: 00_meiji_restoration.txt:856-860]` |

### 鎖国 JE（je_sakoku）

維新発動の前提となる開国フロー。

| 項目 | 内容 | 出典 |
|------|------|------|
| 付与タイミング | ゲーム開始時（history 経由、DLC あり時） | `[src: 07_sakoku.txt:6]` |
| 完了条件 | law_sakoku でも law_closed_borders でもない（開国） | `[src: 07_sakoku.txt:25]` |
| 完了効果 | イベント ep2_sakoku.4。鎖国廃止支持 IG（law_isolationism に value < neutral）に the_picked_lock_modifier（政治力 +25%） | `[src: 07_sakoku.txt:32-53]` |
| 失敗条件 | 君主制廃止、または japan_emperor_restored 変数あり（帝政ルートで維新が先に成立） | `[src: 07_sakoku.txt:54-64]` |
| 失敗効果 | イベント ep2_sakoku.5。鎖国維持派 IG（law_isolationism に value > neutral）に sakoku_entrenched_modifier（政治力 +25%） | `[src: 07_sakoku.txt:66-87, 00_ep2_05_modifiers.txt:32]` |

> the_picked_lock_modifier と sakoku_entrenched_modifier は同じ +25% 政治力だが、**付与対象 IG が逆**（鎖国反対派 vs 鎖国維持派）。

### 宗教 JE（任意・どちらか一方）

| JE | 目標 | 完了 modifier |
|----|------|--------------|
| je_shinbutsu_bunri（神仏分離） | 本土 10 州すべてで神道人口 60% 以上 `[src: 07_japanese_religion.txt:1-154]` | arahitogami: 権力 +20%・正当性 +5 `[src: 00_ep2_06_modifiers.txt:85-90]` |
| je_elevate_buddhism（仏教振興・檀家） | ig_devout が is_powerful な月を累計 60 回（連続不要、marginal 化で fail）`[src: 07_japanese_religion.txt:155-232]` | extended_danka_system: 行政コスト -20%・税容量 +15% `[src: 00_ep2_06_modifiers.txt:92-97]` |

権力・正当性を重視するなら神仏分離、行政効率を重視するなら仏教振興（コミュニティ知見）。

### 朝鮮植民地化 JE（je_colonize_korea）

- 朝鮮州への鉄道（building_railway）建設で進行する `[src: common/journal_entries/07_korea_colonization.txt:132]`
- 別ファイルの 03_korea.txt は東学党の乱など朝鮮内乱系 JE であり、植民地化 JE とは別物 `[src: common/journal_entries/03_korea.txt]`

---

## 技術・法律

### 技術優先順位（日本）

| Era | 優先分野 | 日本固有の理由 |
|-----|---------|-------------|
| Era 1 | 産業系（鉄・工具）+ 軍事（戦列歩兵・銃工・ナポレオン戦争） | je_meiji_army がナポレオン戦争技術（napoleonic_warfare）を要求 `[src: common/technology/technologies/20_military.txt:118]` |
| Era 2 | 鉄道（Railway）+ 後装砲 + 社会系 | je_meiji_economy が鉄道を要求 `[src: 00_meiji_restoration.txt:754]` |
| Era 2-3 | 岩倉使節団 JE 継続中は研究加速 | 生産技術 +1%/stack、社会技術 +1%/stack、法律制定時間 -0.25%/stack `[src: common/static_modifiers/00_ep2_04_modifiers.txt:156-165]` |
| Era 3 | 電力・内燃機関 + 国民皆兵 | 列強対抗の軍拡 |
| Era 4-5 | バランスよく | 列強として全方位の発展 |

### 法律改正ロードマップ

日本は開始時に幕府（law_bakufu）・鎖国（law_sakoku）・伝統主義（law_traditionalism）という固有性の強い法を持つ。これらの段階的廃止が維新の核心。

| 優先度 | 法律変更 | タイミング | 理由 |
|--------|---------|-----------|------|
| 最高 | 鎖国（law_sakoku）→ 重商主義（law_mercantilism） | 維新発動前 | je_sakoku 完了 → 維新の possible 条件（孤立主義でないこと）を解除。**law_free_ports という移行先は存在しない** `[src: common/laws/00_trade_policy.txt:5]` |
| 高 | 伝統主義（law_traditionalism）廃止 | 維新後・列強化前 | je_meiji_diplomacy（外交承認）の完了条件 `[src: 00_meiji_restoration.txt:856]` |
| 高 | 武士階級（law_warrior_caste）→ 近代軍制 | 維新後・je_meiji_army 進行中 | 武士訓練 PM 廃止が軍制改革の完了条件 `[src: 00_meiji_restoration.txt:797]` |
| 高 | 農奴制（serfdom）廃止 | 維新後 | je_meiji_army の完了条件 `[src: 00_meiji_restoration.txt:797]` |
| 最高 | 幕府（law_bakufu）廃止 | 維新カウンター進行のため | 月次パルス条件「幕府法なし」に直結。progressiveness -100 で支持 IG を揃えないと制定が極めて遅い `[src: common/laws/00_distribution_of_power.txt:114]` |
| 中 | 世襲官僚 → 実力制官僚 | 中盤 | 行政効率の向上。知識人 IG の支持が必要 |
| 中 | 寺子屋（law_terakoya）→ 公共学校 | 中盤 | 識字率向上 `[src: history/countries/jap - japan.txt]` |
| 低 | 選挙制度の段階的拡張 | 終盤 | 政治安定に寄与。急がない |

> **幕府法の使いどころ**: 廃止前は正当性 +30・権力 +200 の強力な統治ボーナスを序盤の盾に使える `[src: common/laws/00_distribution_of_power.txt:114]`。帝政ルートでは月次パルス条件を整えてから廃止する。

### 宗教法律の選択（維新後）

- 神仏分離路線（je_shinbutsu_bunri → arahitogami）は信者 IG の支持を確保しつつ神道人口を拡大
- 仏教振興路線（je_elevate_buddhism → extended_danka_system）は信者 IG を is_powerful に保つ時間を確保する

---

## よくあるミス

### 日本固有

| NG 行動 | 理由 |
|---------|------|
| 維新 JE 発動前に鎖国を解除しない | 鎖国は law_isolationism を parent とするため、開国しないと維新の possible 条件（孤立主義でないこと）を満たせない `[src: 00_meiji_restoration.txt:33-37]` |
| 鎖国の移行先として law_free_ports を探す | **そんな法律は存在しない**。鎖国の廃止先は law_mercantilism `[src: common/laws/00_trade_policy.txt:5]` |
| 「force_recognition」で承認を取ろうとする | スクリプト上に存在しない ID。承認は je_meiji_diplomacy の完了で得る `[src: 00_meiji_restoration.txt:856-860]` |
| 条約港を放置する（特に幕府ルートを残す場合） | 公武合体ルート（je_meiji_imperial_marriage）の完了条件「本土州に条約港なし」を阻害する。加えて強制開国 modifier で威信 -25% も付くため、どのルートでも早期解消が望ましい `[src: 00_meiji_restoration.txt:572, common/static_modifiers/00_code_static_modifiers.txt:863]` |
| 大名（ig_daimyo）を急激に壊滅させる | 月次パルス条件は「リーダーが非徳川」であって大名 IG の壊滅ではない。壊すと急進化・内戦リスクが上がる。維新完了後は ig_kazoku に変わる `[src: common/interest_groups/00_landowners.txt:751-762]` |
| 武士訓練 PM を維新後も放置する | je_meiji_army の完了条件として武士訓練・pm_no_organization 兵舎の不在が要求される `[src: 00_meiji_restoration.txt:797-823]` |
| je_meiji_economy で「ちょうど 70%」を狙う | 条件は >0.7（70% 超）で、ちょうど 70% は不可。余裕を持って整備する `[src: 00_meiji_restoration.txt:754]` |
| 君主制を廃止して je_sakoku を失敗させる | 鎖国維持派 IG に sakoku_entrenched_modifier（政治力 +25%）が付く `[src: 07_sakoku.txt:54-87]` |

### VIC3 全般

| NG 行動 | 理由 |
|---------|------|
| 建設キューを空にする | 常に何か建てていないと成長が止まる |
| 法律を一度に大量に変える | 急進派が爆発して内戦になる |
| 外交戦を無計画に始める | 味方が少ないと不利 |
| 未承認のまま攻撃的に拡張する | 攻撃的な外交戦の起票が制限される。承認昇格を優先 |
| 商品価格を無視する | 供給過多・不足で経済が崩壊する |

---

## 用語対照表

> 完全版は [localization-reference.md](localization-reference.md) を参照。以下は日本攻略ガイド固有の用語のみ抜粋。

| 日本語（ゲーム内） | 英語 / スクリプトキー | 補足 |
|-----------------|----------------------|------|
| 幕府 | law_bakufu | 統治機構の法。progressiveness -100、正当性 +30、権力 +200 `[src: common/laws/00_distribution_of_power.txt:114]` |
| 鎖国 | law_sakoku | 日本文化＋九州所持時のみ表示の貿易政策法。parent = law_isolationism、前提に law_traditionalism `[src: common/laws/00_trade_policy.txt:290-300]` |
| 伝統主義 | law_traditionalism | 経済システムの法。je_meiji_diplomacy の廃止対象 `[src: common/laws/00_economic_system.txt:5]` |
| 重商主義 | law_mercantilism | 鎖国の最も移行しやすい廃止先 `[src: common/laws/00_trade_policy.txt:5]` |
| 大名（維新前の地主 IG 名称） | ig_daimyo | 日本文化時の ig_landowners 表示名。維新後は ig_kazoku `[src: common/interest_groups/00_landowners.txt:342]` |
| 華族 | ig_kazoku | 維新後の地主 IG 名称。ideology → ideology_hierarchic `[src: common/journal_entries/00_meiji_restoration.txt, on_complete]` |
| 武士階級 | law_warrior_caste | 日本文化のみ表示の軍制法。pm_samurai_training をアンロック |
| 武士訓練 | pm_samurai_training | law_warrior_caste 時のみ利用可能な兵舎 PM `[src: common/production_methods/05_military.txt:144]` |
| 寺子屋 | law_terakoya | 日本固有の初期教育法 `[src: history/countries/jap - japan.txt]` |
| 出島 | Dejima | 鎖国時に交易が許される九州内の交易拠点。鎖国は country_disallow_trade_outside_kyushu_bool で九州外交易を禁止 `[src: common/laws/00_trade_policy.txt:290]` |
| 条約港 | Treaty Port / take_treaty_port | 列強が dp_take_treaty_port で強制設置。公武合体ルートを阻害 `[src: common/war_goal_types/25_take_treaty_port.txt, common/journal_entries/00_meiji_restoration.txt:572]` |
| 強制開国 | forced_market_opening | 市場を強制された時の修正値。威信 -25% `[src: common/static_modifiers/00_code_static_modifiers.txt:863]` |
| 公武合体 | je_meiji_imperial_marriage / kobu_gattai | 幕府勝利ルートA（条約港なしが完了条件） |
| 公議輿論 | kogi_yoron | 幕府勝利ルートB |
| 神仏分離 | je_shinbutsu_bunri | 神道優先の宗教 JE。arahitogami modifier `[src: common/journal_entries/07_japanese_religion.txt]` |
| 仏教振興（檀家） | je_elevate_buddhism | 仏教優先の宗教 JE。extended_danka_system modifier `[src: common/journal_entries/07_japanese_religion.txt]` |
| 現人神 | arahitogami | 神仏分離 JE 完了 modifier。権力 +20%・正当性 +5 `[src: common/static_modifiers/00_ep2_06_modifiers.txt:85]` |
| 檀家制度（拡張） | extended_danka_system | 仏教振興 JE 完了 modifier。行政コスト -20%・税容量 +15% `[src: common/static_modifiers/00_ep2_06_modifiers.txt:92]` |
| 岩倉使節団 | je_iwakura_mission | DLC 専用の技術加速 JE `[src: common/journal_entries/07_iwakura_mission.txt]` |
| プロミネンス | Prominence | 1.13 追加。IG 指導者選出の主因。日本では大名の magnate_leader_weight に +5 `[src: common/interest_groups/00_landowners.txt:751-762]` |
| 砲撃外交 | Gunboat Diplomacy / can_threaten_naval_hostilities | 1.13 追加。条約交渉時の海上敵対脅迫ルール `[src: common/scripted_rules/00_scripted_rules.txt:226]` |
| 未承認 | Unrecognized | 攻撃的な外交戦の起票が制限される |
| 承認国 | Recognized | je_meiji_diplomacy の完了で到達 |

---

## 出典

### 一次情報（ゲームスクリプト・公式）

2026-06-01 にインストール版 Victoria 3 **1.13.8 + EP2** のスクリプトで全数値を再検証した。

- `common/journal_entries/00_meiji_restoration.txt` — 明治維新 JE 本体（je_meiji_restoration:26-240、je_meiji_imperial_marriage:539-633、je_meiji_main:640-742、je_meiji_economy:754-766、je_meiji_army:797-823、je_meiji_diplomacy:856-860）
- `common/journal_entries/07_sakoku.txt` — 鎖国 JE（je_sakoku:6-87）
- `common/journal_entries/07_japanese_religion.txt` — 宗教 JE（je_shinbutsu_bunri:1-154、je_elevate_buddhism:155-232）
- `common/journal_entries/07_iwakura_mission.txt` — 岩倉使節団 JE
- `common/journal_entries/07_korea_colonization.txt` — 朝鮮植民地化 JE（je_colonize_korea、鉄道条件:132）
- `common/journal_entries/03_korea.txt` — 朝鮮内乱系 JE（植民地化 JE とは別物）
- `common/laws/00_trade_policy.txt` — 貿易政策法（law_mercantilism:5、law_isolationism:159、law_sakoku:290-350）
- `common/laws/00_distribution_of_power.txt` — 幕府法（law_bakufu:114-181）
- `common/laws/00_economic_system.txt` — 伝統主義（law_traditionalism:5）
- `common/production_methods/05_military.txt` — 武士訓練 PM（pm_samurai_training:144-165）
- `common/interest_groups/00_landowners.txt` — 大名表示ロジック（:342-356）、magnate_leader_weight 加算（:751-762）
- `common/interest_group_traits/00_landed_interest_traits.txt` — 普代/外様トレイト（:123-141）
- `common/character_traits/special_personality_traits.txt` — 天皇 trait（special_character_japanese_emperor:673）
- `common/character_templates/country_jap.txt` — 日本固有キャラクターテンプレート（家斉:187、家慶:213、孝明:50、明治:79 ほか）
- `common/static_modifiers/00_code_static_modifiers.txt` — forced_market_opening（:863）
- `common/static_modifiers/00_ep2_04_modifiers.txt` — 維新分岐 modifier（court_and_shogunate:125、continuity_and_enlightenment/taikun_monarchy:137-148）、岩倉使節団 modifier（:156-165）
- `common/static_modifiers/00_ep2_05_modifiers.txt` — sakoku_entrenched_modifier（:32）
- `common/static_modifiers/00_ep2_06_modifiers.txt` — arahitogami（:85-90）、extended_danka_system（:92-97）
- `common/static_modifiers/content_1_modifiers.txt` — meiji_favored_ig（:122-125）
- `common/treaty_articles/14_treaty_port.txt` — 条約港（撤回時 add_claim:216-229）
- `common/diplomatic_plays/00_diplomatic_plays.txt` — dp_take_treaty_port（:315）、force_recognition は不在
- `common/war_goal_types/25_take_treaty_port.txt` — 戦争目標 take_treaty_port
- `common/diplomatic_actions/57_orchestrate_coup.txt` — クーデター扇動
- `common/scripted_rules/00_scripted_rules.txt` — 砲撃外交ルール（can_threaten_naval_hostilities:226）
- `common/technology/technologies/20_military.txt` — ナポレオン戦争技術（napoleonic_warfare:118）
- `common/ship_types/`・`common/ship_modifications/`・`common/combat_unit_types/` — JAP 固有海軍・陸戦ユニットエントリなし（全走査で確認）
- `history/countries/jap - japan.txt` — 日本の開始法律セット、je_sakoku 付与
- `dlc_metadata/00_dlc_metadata.txt` — DLC 構成（dlc018 = The Great Wave / ep2_content）

### コミュニティ情報（補足知見）

プレイ報告・体感ベースの情報。条件の裏取りには一次情報を参照のこと。

- 鎖国解除・開国のタイミング判断、IG 満足度の運用水準、内戦回避の立ち回りはプレイ報告ベース
- 砲撃外交・クーデター扇動の発動に必要な海軍規模・コストはスクリプト未確認
- 「承認の強要（force recognition）」はゲーム内慣用表現であってスクリプト ID ではない
- 列強認知に必要な GDP・軍事・技術の総合ランク水準はコミュニティ知見
- 単一指揮官制の運用論（少数精鋭・再配置コスト）は 1.13 wiki + プレイ報告ベース

### パッチ参照

- [Patch 1.13 - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Patch_1.13)（海軍刷新・艦船デザイナー・旗艦・砲撃外交・プロミネンス）
- [Japan - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Japan)
