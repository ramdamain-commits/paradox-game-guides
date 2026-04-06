# VIC3 プロイセン攻略ガイド（Patch 1.12.4 時点）

> プロイセン → ドイツ統一を狙う序盤から列強化までの整理。
> 2026-03-31 確認時点の最新パッチ 1.12.4（Iberian Twilight）に合わせて更新。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。

---

## パッチ 1.12 / 1.12.4 でのプロイセン関連変更点

1.12 はイベリア半島が主題。プロイセン固有の変更は確認されていない。

| 変更 | 内容 |
|------|------|
| GDP 再投資乗数の削除 | 外国投資の実装に伴い、世界 GDP 成長が緩やかに。プロイセンの経済優位は序盤に集中しやすくなった |
| 百姓（Peasants）の早期消滅緩和 | 農業国との経済差が縮小。工業化の相対優位はやや低下 |
| 封鎖必要海軍力の調整 | 海軍戦略に影響（プロイセンは陸軍主体なので間接的） |
| AI 外交戦の陣営切替修正 | 外交戦（Diplomatic Play）で敵味方が安定しやすくなった |

### 次期パッチ 1.13（2026-04-28 予定）

海軍の全面刷新が予告されている。プロイセンの海軍戦略に大きな影響が出る可能性あり。本ガイドは 1.12.4 時点の内容。

---

## 開始状況（1836年）

| 項目 | 値 |
|------|-----|
| 国家タグ | PRU |
| 政体 | 君主制（Monarchy） |
| 首都 | ベルリン（Berlin） |
| 主要文化 | 北ドイツ（North German） |
| 国教 | プロテスタント |
| 識字率（Literacy） | 高い（ドイツ圏最高水準） |
| 主要利益団体（IG） | 地主（Landowners）、軍部（Armed Forces）が強力 [src: interest_groups_l_japanese.yml, ig_landowners / ig_armed_forces] |
| 従属国 | なし |
| 経済圏 | プロイセン関税同盟（Zollverein）のリーダー |

### 周辺国との関係

| 方角 | 隣国 | 関係性 |
|------|------|--------|
| 南 | オーストリア | ドイツ統一の最大のライバル。中盤で必ず対決 |
| 西 | フランス | 終盤の敵。普仏戦争がドイツ統一の最終段階 |
| 東 | ロシア | 中立〜友好を維持。二正面作戦を避ける |
| 北 | デンマーク | シュレスヴィヒ＝ホルシュタイン問題。統一の第一歩 |

### 初期の強み・弱み

| 強み | 弱み |
|------|------|
| 識字率が高く技術（Technology）で先行しやすい | 列強には及ばない中堅規模 |
| 軍部（Armed Forces）が強力で陸軍に有利 | 地主（Landowners）が強すぎて法律改正が困難 |
| 関税同盟で経済圏を構築済み | 海軍が弱い。海戦では不利 |
| 鉄・石炭の資源が豊富 | オーストリアとの主導権争いが序盤から発生 |

---

## Day 1（ポーズ解除直後）

1. **建設局（Construction Sector）のレベルを上げる**
   - VIC3 の最重要アクション。建設速度が全ての経済発展の基盤（コミュニティ知見）

2. **技術研究を開始: 産業系を優先**
   - 識字率の高さを活かして技術先行を維持

3. **利益団体（IG）の勢力バランスを確認**
   - 地主と軍部が強い。知識人（Intelligentsia）や実業家（Industrialists）の影響力を育てる

4. **関税同盟（Customs Union）の維持を確認**
   - 加盟国が離脱しないよう関係を維持

5. **兵舎（Barracks）を確認し、陸軍編成を把握**
   - 序盤は大規模な軍拡不要。既存戦力で十分

---

## 時系列戦略

### 序盤（1836〜1860）: 経済基盤の構築

| 時期 | 目標 |
|------|------|
| 1836-1840 | 建設局の拡張、鉄鋼・工具の生産基盤構築 |
| 1840-1850 | 関税同盟の拡大。技術で先行。法律改正を開始 |
| 1850-1860 | 対デンマーク戦争（シュレスヴィヒ問題）。北ドイツ連邦の布石 |

### 中盤（1860〜1880）: ドイツ統一戦争

| 時期 | 目標 |
|------|------|
| 1860-1866 | 北ドイツ連邦を形成。対オーストリア戦争 |
| 1866-1871 | 普仏戦争。ドイツ帝国を宣言 |
| 1871-1880 | 統一後の内政安定化。法律改正の推進 |

### 終盤（1880〜1936）: 列強としての運営

- 植民地獲得（アフリカ分割）
- 海軍の拡張（1.13 で仕様変更予定に注意）
- 社会制度の整備（社会保障、教育、医療）
- 大戦への備えまたは回避

---

## 内政・経済

> VIC3 は経済がゲームの中心。軍事・外交より先にこのセクションを固める。

### 建設の優先順位

| 順位 | 施設（Building） | 理由 |
|------|-----------------|------|
| 1 | 建設局（Construction Sector）[src: buildings_l_japanese.yml, building_construction_sector] | 建設速度の基盤。最優先（コミュニティ知見） |
| 2 | 鉄鋼関連（Iron Mine, Steel Mills）[src: buildings_l_japanese.yml, building_iron_mine / building_steel_mill] | 資材と商品の供給。プロイセンの資源を活用 |
| 3 | 工具工場（Tool Workshops）[src: buildings_l_japanese.yml, building_tooling_workshop] | 全施設の建設に必要な工具を生産 |
| 4 | 織物工場系 | 人口の消費需要を満たし GDP を伸ばす |
| 5 | 大学（Universities）[src: buildings_l_japanese.yml, building_university] | 革新（Innovation）を加速。識字率を維持 |

### 利益団体（IG）管理

| IG | 序盤の戦略 |
|----|-----------|
| 地主（Landowners） [src: 00_landowners.txt, ig_landowners] | 初期は強すぎる。法律改正で徐々に弱体化させるが、急ぎすぎると内戦リスク |
| 軍部（Armed Forces） [src: 00_armed_forces.txt, ig_armed_forces] | 味方につけておく。統一戦争で必要 |
| 実業家（Industrialists） [src: 00_industrialists.txt, ig_industrialists] | 工業化で自然に影響力が伸びる。支持する |
| 知識人（Intelligentsia） [src: 00_intelligentsia.txt, ig_intelligentsia] | 法律改正の推進力。影響力を育てたい |
| 労働組合（Trade Unions） [src: 00_trade_unions.txt, ig_trade_unions] | 中盤以降に台頭。急進化させない程度に配慮 |

### 法律改正ロードマップ（コミュニティ知見）

序盤から計画的に進める。一度に多くの法律を変えると急進派が増える。

| 優先度 | 法律 | 理由 |
|--------|------|------|
| 高 | 徴兵法の改正（職業軍人→大規模徴兵）[src: laws_l_japanese.yml, law_professional_army / law_mass_conscription] | 統一戦争に備えて動員力を確保 |
| 高 | 教育制度の拡充（民間学校→公共学校）[src: laws_l_japanese.yml, law_private_schools / law_public_schools] | 識字率を維持し革新を加速 |
| 中 | 経済法の自由化 | 実業家の影響力を伸ばし地主を弱体化 |
| 中 | 労働法の改善 | 急進派の抑制と生活水準の向上 |
| 低 | 選挙法の改正 | 終盤の政治安定に寄与。急ぐ必要はない |

---

## 外交・同盟

### 必須外交

| 対象 | 行動 | 理由 |
|------|------|------|
| 関税同盟加盟国 | 関係維持 | 離脱されると経済圏が縮小 |
| ロシア | 友好維持 | 東方の安全確保。二正面作戦を避ける |
| オーストリア | 対決準備 | ドイツ統一のためにいずれ排除する |
| イギリス | 中立維持 | 海戦で勝てない。敵に回さない |

### ドイツ統一の外交ルート

ドイツ統一は「北ドイツ連邦（North German Federation）→ ドイツ帝国（Germany）」のルートで達成する。

1. 関税同盟を拡大し、ドイツ小国を経済的に囲い込む
2. シュレスヴィヒ＝ホルシュタイン問題で対デンマーク戦争（序盤〜中盤）
3. 北ドイツ連邦を形成（外交戦 or 戦争）
4. 対オーストリア戦争でドイツ圏の主導権を確保
5. 対フランス戦争（普仏戦争）でドイツ帝国を宣言

---

## 軍事ドクトリン

### 陸軍重視

プロイセンの軍事的強みは陸軍。海軍には大きな投資をしない。

| 兵種 | 方針 |
|------|------|
| 歩兵 | 主力。技術でアップグレードを優先 |
| 砲兵 | 重要。技術が進むほど有利 |
| 騎兵 | 序盤は有用。中盤以降は比重低下 |
| 海軍 | 最低限。海戦は避ける方針 |

### 将軍の選び方

- 軍事スキルの高い将軍を優先
- 利益団体との繋がりも確認（軍部出身が安定）
- 統一戦争では複数方面の将軍が必要

### 統一戦争での注意（コミュニティ知見）

- オーストリア戦は**単独 or ロシアと共闘**で挑む
- フランス戦は**オーストリアとの講和後に速やかに**
- 外交戦（Diplomatic Play）で味方を増やしてから開戦する
- 悪名（Infamy）管理に注意。包囲網を招くとドイツ統一が頓挫する

---

## 固有イベント時系列

> プロイセン固有イベントの詳細はゲームスクリプト `events/` で確認可能。以下は主要なもの。

| イベント名 | ID | 発生期間/条件 | 推奨選択 | 効果 |
|-----------|-----|--------------|---------|------|
| ドイツの国民意識 | german_unification.5 | 北ドイツまたは南ドイツ文化の国が je_german_unification_idea を完了したとき | a: 「ただならぬ時代がやって来る」 — JEを進める | 北/南ドイツ連邦JEをジャーナルに追加 [src: german_unification.txt, german_unification.5] |
| ドイツのリーダーシップ | german_unification.1 | je_north_german_unification または je_south_german_unification 完了時 | a: 「責任ある政治家は国民的英雄である」— NGF/SGFに改名 | 統一候補小国が自動的に合流または german_unification.2 を受け取る [src: german_unification.txt, german_unification.1] |
| …との連合（小国合流） | german_unification.2 | german_unification.1 で小国が拒否しなかった場合 | a: 「ドイツのために！」— 合流を受け入れる | 拒否すると関係-50 + 請求権が付与される [src: german_unification.txt, german_unification.2] |
| 鉄血宰相 | german_unification.3 | PRU_otto_von_bismarck キャラクタースポーン時（クールダウンあり） | a: 「ビスマルクを首相に任命せよ」— realpolitik モディファイア獲得 | b 選択で germany_aggressive_expansion モディファイア付与 [src: german_unification.txt, german_unification.3] |
| ドイツ統一 | german_unification.4 | je_german_unification 完了時（GER 形成） | a: 「[元首称号]万歳」— special_character_german_unifier_ruler トレイト付与 | b 選択でドイツ文化に忠誠心+10% [src: german_unification.txt, german_unification.4] |
| シュレスヴィヒ＝ホルシュタイン問題（JE） | je_schleswig_holstein_question | ゲーム開始〜中盤。北/南ドイツ文化が前提条件 | STATE_SCHLESWIG_HOLSTEIN をドイツ系が支配するか HOL/SCH が独立 | 完了すると schleswig_holstein_question_solver モディファイアを取得。北ドイツ連邦JEの前提条件 [src: 00_german_unification.txt, je_schleswig_holstein_question] |
| ツォルフェライン（関税同盟）イベント | — | ドイツ小国との関係（コミュニティ知見） | 加盟国を増やす選択肢を優先 | 専用イベントファイル未確認 |
| ビスマルクの社会立法 | — | ドイツ統一後（1880以降）（コミュニティ知見） | 社会保障を導入（急進派の抑制） | 専用イベントファイル未確認 |

> **注記**: `[src:]` マーカーが付いた項目はスクリプトで確認済み。ID が `—` の項目はコミュニティ知見ベースで一次情報での裏取りが未完了。

---

## 技術・法律

### 技術の優先順位（コミュニティ知見）

| Era | 優先分野 | 理由 |
|-----|---------|------|
| Era 1 | 産業系（工業化） | 経済基盤の構築が最優先 |
| Era 2 | 軍事系 + 民族主義（Nationalism）[src: 30_society.txt, nationalism] | 統一戦争に備える。北ドイツ連邦JEの完了条件に nationalism 研究が必要 |
| Era 3 | 産業 + 社会系 + 汎民族主義（Pan-nationalism）[src: 30_society.txt, pan-nationalism] | 統一後の内政安定化。je_german_unification の完了条件に pan-nationalism 研究が必要 |
| Era 4-5 | バランスよく | 列強として全方位の発展 |

---

## よくあるミス

### プロイセン固有

| NG 行動 | 理由 |
|---------|------|
| 建設局を後回しにする | 経済発展が致命的に遅れる |
| 地主を急激に弱体化させる | 内戦（Civil War）リスク。段階的に進める |
| オーストリアより先にフランスと戦う | 順序を間違えると統一が頓挫する |
| 悪名（Infamy）を無視して拡張���る | 包囲網を招き、統一どころか防衛戦になる |
| 海軍に大量投資する | プロイセンの強みは陸軍。海軍はコスパが悪い |
| ロシアを敵に回す | 二正面作戦は致命的 |

### VIC3 全般

| NG 行動 | 理由 |
|---------|------|
| 建設キューを空にする | 常に何か建てていないと成長が止まる |
| 法律を一度に大量に変える | 急進派が爆発して内戦になる |
| 外交戦を無計画に始める | 味方が少ないと戦争で不利 |
| 商品価格を無視する | 供給過多 or 不足で経済が崩壊する |

---

## 用語対照表

> 完全版は [localization-reference.md](localization-reference.md) を参照。以下はこのガイドで使う用語の抜粋。

| 日本語 | 英語 | 補足 |
|--------|------|------|
| 威信 | Prestige | 国家の格 |
| 悪名 | Infamy | 外交的な悪評 |
| 権力 | Authority | 政府の統治力 |
| 正当性 | Legitimacy | 政府の正当性 |
| 行政力 | Bureaucracy | 制度運営に必要なリソース |
| 国内総生産 | GDP | 経済規模の指標 |
| 識字率 | Literacy | 技術伝播速度に影響 |
| 革新 | Innovation | 技術進歩の速度 |
| 利益団体 | Interest Group | 略称 IG。政治勢力 |
| 地主 | Landowners | 保守的な IG |
| 実業家 | Industrialists | 工業化推進の IG |
| 軍部 | Armed Forces | 軍事重視の IG |
| 知識人 | Intelligentsia | 進歩的な IG |
| 労働組合 | Trade Unions | 労働者の IG |
| 施設 | Building | 経済・軍事の建造物 |
| 建設局 | Construction Sector | 建設を担う施設 |
| 法律 | Law | 国家の法制度 |
| 制度 | Institution | 法律で設置する組織 |
| 技術 | Technology | 研究対象 |
| 時代 | Era | 技術の時代区分 |
| 陸軍 | Army | 地上軍 |
| 将軍 | General | 陸軍指揮官 |
| 外交戦 | Diplomatic Play | 戦争前の外交的駆���引き |
| 戦争目標 | War Goal | 戦争で達成すべき目標 |
| 同盟 | Alliance | 軍事同盟 |
| 関税同盟 | Customs Union | 経済統合 |
| 従属国 | Subject | 従属国の総称 |

---

## 出典

### 一次情報（ゲームスクリプト・公式）

- ローカルのゲームスクリプトと日本語ローカライズを照合
  - `events/german_unification.txt` — ドイツ統一イベント（german_unification.1〜5）
  - `common/journal_entries/00_german_unification.txt` — ジャーナルエントリー（je_schleswig_holstein_question, je_german_unification_idea, je_north_german_unification, je_south_german_unification, je_german_unification）
  - `common/interest_groups/00_armed_forces.txt` — 軍部（ig_armed_forces）
  - `common/interest_groups/00_landowners.txt` — 地主（ig_landowners）
  - `common/interest_groups/00_industrialists.txt` — 実業家（ig_industrialists）
  - `common/interest_groups/00_intelligentsia.txt` — 知識人（ig_intelligentsia）
  - `common/interest_groups/00_trade_unions.txt` — 労働組合（ig_trade_unions）
  - `common/technology/technologies/30_society.txt` — nationalism / pan-nationalism
  - `events/law_events/education_laws.txt` — プロイセン教育修正案（amendment_prussian_education）
  - `localization/japanese/interest_groups/interest_groups_l_japanese.yml` — IG 日本語名
  - `localization/japanese/buildings_l_japanese.yml` — 建造物日本語名
  - `localization/japanese/laws_l_japanese.yml` — 法律日本語名
  - `localization/japanese/inventions_l_japanese.yml` — 技術日本語名（nationalism=民族主義, pan-nationalism=汎民族主義）
  - `localization/japanese/amendments_ip4_l_japanese.yml` — 修正案日本語名（amendment_prussian_education=プロイセン教育）
  - `localization/japanese/content_1_l_japanese.yml` — イベント・JE 日本語名（german_unification.1〜5, je_*）
- [Patches - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Patches)
- [Patch 1.12.X - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Patch_1.12.X)
- [Prussia - Victoria 3 Wiki](https://vic3.paradoxwikis.com/Prussia)

### コミュニティ情報（補足知見）

プレイ報告・体感ベースの情報。条件の裏取りには一次情報を参照のこと。

- 建設局優先の戦略は VIC3 コミュニティで広く共有されている定石
- ドイツ統一の順序（デンマーク→オーストリア→フランス）は歴史ルートに沿ったプレイの定番
- 法律改正の段階的アプローチは内戦回避の経験則
