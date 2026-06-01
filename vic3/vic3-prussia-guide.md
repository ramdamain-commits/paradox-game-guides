# VIC3 プロイセン攻略ガイド（Patch 1.13.8 + EP2 時点）

> プロイセン（PRU）→ ドイツ統一を狙う序盤から列強運営までの整理。
> 2026-06-01 確認時点。インストール版 **Patch 1.13.8（Matcha）+ EP2** のゲームスクリプトで統一メカニクス・開始状態の数値を再検証済み。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。

---

## パッチ差分（1.13 + EP2 でプロイセンに効いた変更）

1.13（Matcha）は海軍刷新と日本（The Great Wave DLC）が主題。プロイセン固有のコンテンツ追加はないが、外交・指揮官系の仕様変更が統一戦争の進め方に影響する。

| 変更 | プロイセンへの影響 | 確認 |
|------|------|------|
| 海軍刷新（艦船デザイナー・旗艦・新型艦・海戦改編） | 陸軍主体のため直接影響は小。英仏墺の海軍強化に対し封鎖・砲撃外交への対処は要確認 | コミュニティ知見（1.13 wiki ベース） |
| 砲撃外交（Gunboat Diplomacy） | デンマーク等の沿岸国相手の条約交渉で脅迫オプション | `can_threaten_naval_hostilities` ルール `[src: common/scripted_rules/00_scripted_rules.txt:226]` |
| 戦略的関心度（Strategic Interest）のティアド化 | 列強の介入閾値が見えやすくなり、統一戦争の起票タイミングを計りやすい | interest_marker `[src: common/scripted_effects/00_victoria_great_game_scripted_effects.txt]` |
| クーデター扇動（Orchestrate Coup） | ドイツ小国の親プロイセン政権化に使える補助手段 | 専用外交アクション `[src: common/diplomatic_actions/57_orchestrate_coup.txt]`（コスト等はコミュニティ知見） |
| 単一指揮官制 | 軍編成あたり指揮官1名。少数精鋭の将軍運用が基本 | コミュニティ知見（1.13 wiki ベース） |
| プロミネンス（Prominence）導入 | 利益団体（IG = Interest Group）指導者選出の主因が変更 | コミュニティ知見（1.13 wiki ベース） |

---

## 開始状況（1836年）

| 項目 | 値 |
|------|-----|
| 国家タグ | PRU（tier = kingdom） `[src: common/country_definitions/00_countries.txt:58]` |
| 政体 | 君主制（law_monarchy）＋専制政治（law_autocracy） `[src: history/countries/pru - prussia.txt:11-12]` |
| 首都 | ブランデンブルク（STATE_BRANDENBURG、ベルリン） `[src: common/country_definitions/00_countries.txt:66]` |
| 主要文化 | 北ドイツ（north_german） `[src: common/country_definitions/00_countries.txt:65]` |
| 国教 | プロテスタント（north_german 文化のデフォルト宗教） `[src: common/cultures/00_cultures.txt:3]` |
| 与党 IG | 地主（ig_landowners）＋軍部（ig_armed_forces）が開始時の与党 `[src: history/countries/pru - prussia.txt:44-50]` |
| 経済システム法 | 介入主義（law_interventionism）系で開始 `[src: history/countries/pru - prussia.txt:11-25]` |
| 軍制・教育 | 職業軍人（law_professional_army）＋公立学校（law_public_schools）＋官僚任命制（law_appointed_bureaucrats） `[src: history/countries/pru - prussia.txt:11-25]` |
| 経済圏 | **ツォルフェライン（ZOLLVEREIN）** パワーブロックのリーダー（後述） `[src: history/power_blocs/00_power_blocs.txt:52-98]` |

### プロイセン固有の開始ボーナス: プロイセン教育（amendment_prussian_education）

開始時、軍部 IG がスポンサーとなって公立学校法（law_public_schools）に **プロイセン教育修正（amendment_prussian_education）** が付与済み `[src: history/countries/pru - prussia.txt:27-32, common/amendments/00_amendments_enactment_04.txt:728]`。

| 効果 | 数値 |
|------|------|
| 同化率（Assimilation） | +10% |
| 徴兵率（Conscription Rate） | +10% |
| 軍部（ig_armed_forces）政治力 | +10% |

`[src: common/amendments/00_amendments_enactment_04.txt:738-742]`。さらに開始時に学校制度（institution_schools）が level 2 で稼働しており `[src: history/countries/pru - prussia.txt:34-37]`、プロテスタント文化と合わせて識字率（Literacy）でドイツ圏最高水準に立つ。

### ツォルフェライン（パワーブロック）

プロイセンは関税同盟ツォルフェラインを **パワーブロック** のリーダーとして開始する（旧来の「関税同盟」は 1.13 ではパワーブロック・システムで実装）。

| 項目 | 内容 |
|------|------|
| 名称 / リーダー | ZOLLVEREIN（1834 結成）/ PRU `[src: history/power_blocs/00_power_blocs.txt:52]` |
| アイデンティティ | 通商同盟（identity_trade_league、`power_bloc_customs_union_bool = yes` の市場共有型） `[src: common/power_bloc_identities/00_power_bloc_identities.txt:1]` |
| リーダーボーナス | 交易容量（Trade Capacity）+25% `[src: common/power_bloc_identities/00_power_bloc_identities.txt]` |
| 初期原則 | principle_internal_trade_1（港湾処理量 +0.05・州インフラ +10%）。DLC 有効時は principle_police_coordination_1 も付与 `[src: history/power_blocs/00_power_blocs.txt:60]` |
| 開始メンバー | バイエルン・ザクセン・ハンブルク等のドイツ小国 23 か国 `[src: history/power_blocs/00_power_blocs.txt:52-98]` |

### 周辺国との関係

| 方角 | 隣国 | 関係性 |
|------|------|--------|
| 南 | オーストリア（AUS） | ドイツ統一の最大ライバル。中盤で必ず対決 |
| 西 | フランス（FRA） | 終盤の敵。普仏戦争が統一の最終段階 |
| 東 | ロシア（RUS） | 中立〜友好を維持し二正面作戦を避ける |
| 北 | デンマーク（DEN） | シュレスヴィヒ＝ホルシュタイン問題。統一の前提となる JE |

### 初期の強み・弱み

| 強み | 弱み |
|------|------|
| 識字率が高く技術で先行しやすい（公立学校 + プロイセン教育 + institution_schools lv2）`[src: history/countries/pru - prussia.txt:27-37]` | 列強には及ばない中堅規模 |
| 軍部 IG が与党で陸軍に強い `[src: history/countries/pru - prussia.txt:48-50]` | 地主 IG も与党で強く、経済・選挙系の法律改正が重い |
| ツォルフェラインのリーダーで交易容量 +25% の経済圏を保持 `[src: common/power_bloc_identities/00_power_bloc_identities.txt]` | 海軍が弱く海戦では不利 |
| 鉄・石炭が豊富で工業化に向く | オーストリアとの主導権争いが序盤から発生 |

---

## Day 1（ポーズ解除直後）

1. **建設局（Construction Sector）を拡張する** — 全経済発展の基盤。最優先（コミュニティ知見）
2. **技術研究を産業系から開始** — 識字率の高さを活かして技術先行を維持。統一の技術ゲート（後述の nationalism → pan-nationalism）への道を意識する
3. **与党 IG（地主・軍部）と育てたい IG を確認** — 知識人（ig_intelligentsia）・実業家（ig_industrialists）を中長期で伸ばし、法律改正の推進力を作る
4. **ツォルフェラインの維持を確認** — メンバー国が離脱しないよう関係を保つ。統一の経済的な囲い込みの土台
5. **シュレスヴィヒ＝ホルシュタイン問題 JE（je_schleswig_holstein_question）を確認** — 北/南ドイツ連邦 JE の必須前提（後述）。対デンマーク戦の準備を視野に入れる

---

## 時系列戦略

各フェーズの概要。統一メカニクスの完全データは「固有イベント時系列」、技術ゲートは「技術・法律」を参照。

### 序盤（1836〜1860）: 経済基盤と統一の前提づくり

| 時期 | 目標 |
|------|------|
| 1836-1840 | 建設局拡張、鉄鋼・工具の生産基盤構築 |
| 1840-1850 | ツォルフェライン拡大で小国を経済的に囲い込む。技術先行を維持し法律改正を開始 |
| 1850-1860 | **シュレスヴィヒ＝ホルシュタイン問題 JE** を解決（対デンマーク戦 or 外交）。これが北/南ドイツ連邦 JE の前提になる `[src: common/journal_entries/00_german_unification.txt:88-94]` |

### 中盤（1860〜1880）: ドイツ統一

統一は **「シュレスヴィヒ解決 → 北ドイツ連邦（NGF）形成 → ドイツ帝国（GER）形成」** の段階を踏む。

| 時期 | 目標 |
|------|------|
| 1860-1866 | **nationalism 技術**を取得し、北ドイツ連邦 JE を完了して NGF へ改名。対オーストリア戦でドイツ圏主導権を確保 `[src: common/journal_entries/00_german_unification.txt:280-337]` |
| 1866-1871 | **pan-nationalism 技術**を取得し、major power ランクで je_german_unification を進める。対フランス戦（普仏戦争）を経て GER 形成 `[src: common/journal_entries/00_german_unification.txt:401-453]` |
| 1871-1880 | 統一後の内政安定化。ビスマルク登用後の realpolitik 修正値（悪名減衰 +20%）を活かして拡張 `[src: events/german_unification.txt:256-337]` |

### 終盤（1880〜1936）: 列強運営

- 植民地獲得（アフリカ分割）と社会制度の整備
- 海軍は陸軍主体の方針下で最低限。艦船デザイナーで主力艦を整え、旗艦（Flagship）を1隻指定して威信獲得を狙う（コミュニティ知見）
- 大戦への備えまたは回避

---

## 内政・経済

> VIC3 は経済がゲームの中心。軍事・外交より先にこのセクションを固める。

### 建設の優先順位

| 順位 | 施設 | 理由 |
|------|------|------|
| 1 | 建設局（Construction Sector） | 建設速度の基盤。最優先（コミュニティ知見） |
| 2 | 鉄山・製鉄所（Iron Mine / Steel Mills） | 資材供給。プロイセンの鉄・石炭資源を活用 |
| 3 | 工具工場（Tool Workshops） | 全施設の建設に必要な工具を生産 |
| 4 | 織物・消費財工場 | 人口の需要を満たし GDP を伸ばす |
| 5 | 大学（Universities） | 革新（Innovation）を加速。識字率を維持 |

### 利益団体（IG）管理

| IG | 戦略 |
|----|------|
| 地主（ig_landowners） | 開始時の与党だが保守的。経済・選挙系の改正で徐々に弱体化。急ぎすぎると内戦リスク `[src: history/countries/pru - prussia.txt:44-46]` |
| 軍部（ig_armed_forces） | 開始時の与党。統一戦争で必要なため味方に保つ `[src: history/countries/pru - prussia.txt:48-50]` |
| 実業家（ig_industrialists） | 工業化で自然に伸びる。支持して地主を相対的に弱める |
| 知識人（ig_intelligentsia） | 法律改正の推進力。影響力を育てたい |
| 労働組合（ig_trade_unions） | 中盤以降に台頭。急進化させない範囲で配慮 |

#### プロミネンスの活用（1.13）

1.13 で各政治家に **プロミネンス（Prominence）** が追加され、IG 内の政治力寄与と次期指導者の選出確率に影響する（大衆人気 Popularity とは別概念）。

- 育てたい IG の指導者を、プロミネンスの高い人物に交代させたい場合は人物プールから登用する。任務のない政治家もプールに残る（コミュニティ知見）
- **ビスマルク（PRU_otto_von_bismarck）は ig_landowners 所属の政治家**で、`german_unification.3`（鉄血宰相）イベント経由の「首相任命」で登用するのが基本。登用には pan-nationalism 研究済みが前提 `[src: common/character_templates/country_pru.txt:5-42]`

---

## 外交・同盟

### 必須外交

| 対象 | 行動 | 理由 |
|------|------|------|
| ツォルフェライン加盟国 | 関係維持 | 離脱されると経済圏とドイツ統一の土台が縮む |
| ロシア（RUS） | 友好維持 | 東方の安全確保。二正面作戦を避ける |
| オーストリア（AUS） | 対決準備 | ドイツ統一のためいずれ主導権を奪う |
| イギリス（GBR） | 中立維持 | 海戦で勝てない。敵に回さない |

### ドイツ統一の外交ルート

1. ツォルフェラインを拡大し、ドイツ小国を経済的に囲い込む
2. シュレスヴィヒ＝ホルシュタイン問題 JE を解決（対デンマーク戦 or 外交）
3. nationalism 技術取得 → 北ドイツ連邦（NGF）形成。対オーストリア戦でドイツ圏の主導権を確保
4. pan-nationalism 技術取得 → major power ランクで je_german_unification を進め、対フランス戦を経て GER 形成
5. 統一戦争の外交プレイには征服（dp_conquer_state）・州返還（dp_return_state）等を使う `[src: common/diplomatic_plays/00_diplomatic_plays.txt:104,129]`

### 1.13 で増えた外交手段の活用

| 手段 | プロイセンでの使い道 |
|------|---------------------|
| 戦略的関心度（Strategic Interest） | 北ドイツ圏に対する英仏墺の関心度ティアを確認し、低い時期を狙って外交戦を起こす `[src: common/scripted_effects/00_victoria_great_game_scripted_effects.txt]` |
| クーデター扇動（Orchestrate Coup） | 友好ロビーを持つドイツ小国の政体を親プロイセン政権に挿げ替える補助手段。直接戦争・外交戦より悪名コストが低い場合がある `[src: common/diplomatic_actions/57_orchestrate_coup.txt]`（コスト・条件はコミュニティ知見） |
| 砲撃外交（Gunboat Diplomacy） | デンマーク等の沿岸国との条約交渉の脅迫オプション。専用 DP ではなく `can_threaten_naval_hostilities` ルール経由 `[src: common/scripted_rules/00_scripted_rules.txt:226]`。プロイセンは海軍が弱いため過信は禁物（必要海軍規模はコミュニティ知見） |

---

## 軍事ドクトリン

### 陸軍重視

プロイセンの強みは陸軍。海軍には大きな投資をしない。

| 兵種 | 方針 |
|------|------|
| 歩兵（戦列歩兵・散兵 等） | 主力。技術でアップグレードを優先 `[src: common/combat_unit_types/00_land_combat_unit_types.txt]` |
| 砲兵（カノン砲・榴散弾砲 等） | 重要。技術が進むほど有利 `[src: common/combat_unit_types/00_land_combat_unit_types.txt]` |
| 騎兵（軽騎兵・竜騎兵 等） | 序盤は有用。中盤以降は比重低下 |
| 海軍 | 最低限。海戦は避ける。艦船デザイナーは使えるが優先は陸軍 |

### 将軍の選び方（1.13 単一指揮官制）

1.13 で軍編成（Military Formation）あたりの指揮官は **1名のみ**。階級（Commander Rank）の指揮限界が技術で拡張されるため、少数精鋭の将軍を昇進させて運用するのが基本（コミュニティ知見 / 1.13 wiki ベース）。

- 軍事スキル + 特性の質を最優先。多数の凡庸な将軍より優秀な 1〜2 名
- 不必要な昇進は軍部 IG の承認低下を招くため、必要になってから階級を上げる
- 指揮官は編成間で再配置できるが移動に時間がかかり、移動中は特性ボーナスが失われる

### 統一戦争での注意

- オーストリア戦は単独 or ロシアと共闘で。フランス戦はオーストリアとの講和後に速やかに
- 外交戦（Diplomatic Play）で味方を増やしてから開戦する
- 悪名（Infamy）管理に注意。包囲網を招くと統一が頓挫する。ビスマルクの realpolitik 修正値（悪名減衰 +20%）は拡張期の生命線 `[src: events/german_unification.txt:256-337]`
- 複数前線になる場合は編成を分け、各編成に専任の優秀な将軍を割り当てる

---

## 固有イベント時系列

### ドイツ統一 JE チェーン

統一は4段の JE を順に進める。**シュレスヴィヒ解決 → 統一理念 → 北/南ドイツ連邦 → ドイツ帝国**。

| 段 | JE | 主な前提 | 完了条件 | 完了効果 | 出典 |
|----|----|---------|---------|---------|------|
| 0 | je_schleswig_holstein_question | 北/南ドイツ文化（AUS 除外） | ドイツ系国家がシュレスヴィヒ＝ホルシュタイン全域を支配（または HOL/SCH が独立） | schleswig_holstein_question_solver（**威信 +25%**）＋ global 変数セット。**NGF/SGF JE の必須前提** | `[src: 00_german_unification.txt:1-107]` |
| 1 | je_german_unification_idea | 北/南ドイツ文化（PRU 含む） | 北ドイツ文化の熱情（fervor）≥40（南ドイツは ≥30） | 統一理念変数セット、german_unification.5 を発火 → NGF/SGF JE を付与 | `[src: 00_german_unification.txt:109-278]` |
| 2 | je_north_german_unification（北）/ je_south_german_unification（南） | german_unification.5 で付与 | schleswig_holstein_question_solved＋**nationalism 技術**＋GER 統一候補（is_unification_candidate=GER）＋連邦内で唯一の候補 | german_unification.1 を発火 → タグが **NGF / SGF** に変化 | `[src: 00_german_unification.txt:280-399]` |
| 3 | je_german_unification | german_unification.1 で変数セット | major power ランク＋**pan-nationalism 技術**＋非従属。GER を形成すれば完了 | german_unification.4（ドイツ統一）を表示 | `[src: 00_german_unification.txt:401-453]` |

> **技術ゲートの要点**: NGF/SGF JE には **nationalism（era_2）**、最終の je_german_unification には **pan-nationalism（era_3、ID はハイフン表記）** が必須 `[src: common/technology/technologies/30_society.txt]`。pan-nationalism は NGF 段階では不要。

#### GER（ドイツ帝国）形成要件

| 項目 | 値 |
|------|-----|
| 地域 | greater_germany（大ドイツ地域） |
| 必要州割合 | **73%**（required_states_fraction = 0.73） |
| possible 条件 | pan-nationalism 研究済み **または** 統一理念変数（je_german_unification_idea）あり。RHN（ライン連邦）非存在、二重/三重君主制でないこと |
| 統一外交プレイ | dp_unify_germany |

`[src: common/country_formation/00_major_formables.txt:1-50]`。NGF/SGF は文化州の **75%** で形成可能（NGF は nationalism ゲートあり、SGF は技術ゲートなし）`[src: common/country_formation/00_formable_countries.txt:484-505]`。

### 統一イベント（german_unification.1〜5）

| イベント | ID | トリガー | 推奨選択と効果 |
|---------|-----|---------|--------------|
| ドイツの国民意識 | german_unification.5 | je_german_unification_idea 完了 | A: 北ドイツなら je_north_german_unification、南ドイツなら je_south_german_unification を付与 `[src: events/german_unification.txt:400-457]` |
| 北/南ドイツ連邦 | german_unification.1 | NGF/SGF JE 完了 | A（既定）: 与党 IG 全指導者に支持率 +50、タグを NGF/SGF へ。AI かつ「ツォルフェライン加盟 or GER 支持」の同文化小国は自動併合、それ以外には .2 を発火 `[src: events/german_unification.txt:4-174]` |
| 小国の合流要請 | german_unification.2 | .1 が非 AI/非同君の小国に送る | A（合流・AI 重み9）: 併合受諾。**B（拒否）: 急進派増・関係 -50・相手が自国全州に請求権** `[src: events/german_unification.txt:177-253]` |
| 鉄血宰相 | german_unification.3 | ビスマルク登場時 | **A（現実政治・AI 95%）: realpolitik（悪名減衰 +20%）＋ビスマルク支持率 +75、在任 30〜45 年**。B（積極拡張）: germany_aggressive_expansion（関係改善速度 +50%・影響力 +10%） `[src: events/german_unification.txt:256-337]` |
| ドイツ統一 | german_unification.4 | je_german_unification 完了 | A（既定）: 元首に special_character_german_unifier_ruler トレイト＋ドイツ地域への請求権。B: ドイツ文化への忠誠心 +10% `[src: events/german_unification.txt:340-397]` |

> **存在しないイベントに注意**: 「ツォルフェライン拡大イベント」「ビスマルクの社会立法（疾病/災害/年金保険）イベント」は**スクリプト上に存在しない**（歴史条約の記録コメントのみで、発火するゲームイベントは未実装）`[src: events/ 全走査, common/history/treaties/00_historical_treaties.txt]`。ツォルフェライン拡大は外交（パワーブロック招待）で、社会立法は通常の法律改正で行う。

---

## 技術・法律

### 技術の優先順位

| Era | 優先分野 | 理由 |
|-----|---------|------|
| Era 1 | 産業系（工業化） | 経済基盤の構築が最優先 |
| Era 2 | 軍事系 + **民族主義（nationalism）** | 統一戦争に備える。NGF/SGF JE の完了条件 `[src: common/technology/technologies/30_society.txt]`（効果: 権力 +10%・投票力 +10%） |
| Era 3 | 産業・社会系 + **汎民族主義（pan-nationalism）** | je_german_unification の完了条件。ID はハイフン表記 `[src: common/technology/technologies/30_society.txt]`（効果: 権力 +10%・分離主義強度 +25%・投票力 +10%） |
| Era 4-5 | バランスよく | 列強として全方位の発展 |

### 法律改正ロードマップ

序盤から計画的に進める。一度に多くの法律を変えると急進派が増える。

| 優先度 | 法律 | 理由 |
|--------|------|------|
| 高 | 徴兵法の改正（law_professional_army → law_mass_conscription） | 統一戦争に備えて動員力を確保 `[src: common/laws/00_army_model.txt:112,267]` |
| 高 | 教育制度の維持・拡充（law_public_schools 系） | 識字率と革新を維持。プロイセン教育修正の徴兵・同化ボーナスを活かす `[src: common/laws/00_education_system.txt:299]` |
| 中 | 経済法の自由化 | 実業家 IG を伸ばし地主を相対的に弱める |
| 中 | 労働法の改善 | 急進派抑制と生活水準向上 |
| 低 | 選挙法の改正 | 終盤の政治安定。急がない |

---

## よくあるミス

### プロイセン固有

| NG 行動 | 理由 |
|---------|------|
| 建設局を後回しにする | 経済発展が致命的に遅れる |
| 与党の地主を急激に弱体化させる | 内戦リスク。段階的に進める `[src: history/countries/pru - prussia.txt:44-46]` |
| nationalism 技術なしで連邦化を狙う | NGF/SGF JE は nationalism が完了条件。技術を先に取る `[src: common/journal_entries/00_german_unification.txt:293]` |
| pan-nationalism なしで GER を狙う | je_german_unification の前提は pan-nationalism 研究済み（または統一理念変数）。major power ランクも必要 `[src: common/journal_entries/00_german_unification.txt:414-419]` |
| シュレスヴィヒ問題を放置する | NGF/SGF JE の必須前提。未解決だと連邦化に進めない `[src: common/journal_entries/00_german_unification.txt:287]` |
| オーストリアより先にフランスと戦う | 順序を誤ると統一が頓挫する |
| 「ツォルフェライン拡大イベント」「ビスマルク社会立法イベント」を待つ | どちらもスクリプト上に存在しない。拡大は外交、社会立法は法律改正で行う `[src: events/ 全走査]` |
| 海軍に大量投資する | 強みは陸軍。海軍はコスパが悪い |

### VIC3 全般

| NG 行動 | 理由 |
|---------|------|
| 建設キューを空にする | 常に何か建てていないと成長が止まる |
| 法律を一度に大量に変える | 急進派が爆発して内戦になる |
| 外交戦を無計画に始める | 味方が少ないと不利 |
| 商品価格を無視する | 供給過多・不足で経済が崩壊する |

---

## 用語対照表

> 完全版は [localization-reference.md](localization-reference.md) を参照。以下はこのガイド固有の用語の抜粋。

| 日本語（ゲーム内） | 英語 / スクリプトキー | 補足 |
|-----------------|----------------------|------|
| ツォルフェライン | Zollverein / identity_trade_league | PRU がリーダーの関税同盟型パワーブロック。交易容量 +25% `[src: common/power_bloc_identities/00_power_bloc_identities.txt]` |
| プロイセン教育 | amendment_prussian_education | 開始時付与の修正。同化 +10%・徴兵率 +10%・軍部政治力 +10% `[src: common/amendments/00_amendments_enactment_04.txt:728]` |
| 民族主義 | nationalism | era_2 社会技術。NGF/SGF JE の完了条件 `[src: common/technology/technologies/30_society.txt]` |
| 汎民族主義 | pan-nationalism | era_3 社会技術（ID ハイフン表記）。je_german_unification の前提 `[src: common/technology/technologies/30_society.txt]` |
| 北ドイツ連邦 | NGF / North German Confederation | nationalism + シュレスヴィヒ解決で形成。文化州 75% |
| 南ドイツ連邦 | SGF / South German Confederation | 南ドイツ文化国のルート。技術ゲートなし |
| ドイツ帝国 | GER / German Empire | 大ドイツ地域 73% + pan-nationalism（または統一理念）で形成 |
| シュレスヴィヒ＝ホルシュタイン問題 | je_schleswig_holstein_question | 統一の前提 JE。完了で威信 +25% |
| 現実政治 | realpolitik | 鉄血宰相 A 選択の修正。悪名減衰 +20% `[src: events/german_unification.txt:256-337]` |
| 権力 | Authority | 政府の統治力（VIC3 ローカライズは「権力」） `[src: localization/japanese, concept_authority]` |
| 威信 | Prestige | 国家の格 |
| 悪名 | Infamy | 外交的な悪評 |
| プロミネンス | Prominence | 1.13 追加。IG 指導者選出の主因 |
| クーデター扇動 | Orchestrate Coup | 1.13 の外交アクション `[src: common/diplomatic_actions/57_orchestrate_coup.txt]` |
| 砲撃外交 | Gunboat Diplomacy / can_threaten_naval_hostilities | 1.13 の海上脅迫ルール `[src: common/scripted_rules/00_scripted_rules.txt:226]` |

---

## 出典

### 一次情報（ゲームスクリプト・公式）

2026-06-01 にインストール版 Victoria 3 **1.13.8 + EP2** のスクリプトで統一メカニクス・開始状態を再検証した。

- `common/journal_entries/00_german_unification.txt` — 統一 JE チェーン（je_schleswig_holstein_question:1-107、je_german_unification_idea:109-278、je_north/south_german_unification:280-399、je_german_unification:401-453）
- `events/german_unification.txt` — 統一イベント（german_unification.1:4-174、.2:177-253、.3:256-337、.4:340-397、.5:400-457）
- `common/country_formation/00_major_formables.txt` — GER 形成要件（greater_germany 73%、dp_unify_germany）
- `common/country_formation/00_formable_countries.txt` — NGF:484-494 / SGF:496-505（文化州 75%）
- `common/technology/technologies/30_society.txt` — nationalism（era_2）/ pan-nationalism（era_3）
- `common/country_definitions/00_countries.txt` — PRU 定義（タグ:58、文化:65、首都:66）
- `history/countries/pru - prussia.txt` — 開始法律・与党 IG（:44-50）・institution_schools lv2（:34-37）・プロイセン教育付与（:27-32）
- `common/cultures/00_cultures.txt` — north_german の国教 protestant（:3）
- `history/power_blocs/00_power_blocs.txt` — ツォルフェライン（ZOLLVEREIN、:52-98）
- `common/power_bloc_identities/00_power_bloc_identities.txt` — identity_trade_league（交易容量 +25%）
- `common/amendments/00_amendments_enactment_04.txt` — amendment_prussian_education（:728、効果:738-742）
- `common/laws/00_army_model.txt` — law_professional_army:112 / law_mass_conscription:267
- `common/laws/00_education_system.txt` — law_public_schools:299 / law_private_schools:156
- `common/character_templates/country_pru.txt` — PRU_otto_von_bismarck（:5、ig_landowners 所属、登用に pan-nationalism 必要）
- `common/diplomatic_plays/00_diplomatic_plays.txt` — dp_conquer_state:104 / dp_return_state:129
- `common/diplomatic_actions/57_orchestrate_coup.txt` — クーデター扇動
- `common/scripted_rules/00_scripted_rules.txt` — 砲撃外交ルール（can_threaten_naval_hostilities:226）
- `common/combat_unit_types/00_land_combat_unit_types.txt` — 陸軍ユニット種別
- [Patch 1.13 - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Patch_1.13)
- [Prussia - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Prussia)

### コミュニティ情報（補足知見）

プレイ報告・体感ベースの情報。条件の裏取りには一次情報を参照のこと。

- 建設局優先・統一の順序（デンマーク→オーストリア→フランス）・法律改正の段階化は VIC3 コミュニティの定石
- 単一指揮官制の運用論（少数精鋭・再配置コスト）は 1.13 wiki + プレイ報告ベース
- クーデター扇動・砲撃外交の発動コスト・必要海軍規模・許可日数の具体値はスクリプト未確認
- 海軍最小限・旗艦による威信獲得の運用はプレイ報告ベース
