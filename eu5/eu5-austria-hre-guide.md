# EU5 オーストリア — 神聖ローマ帝国運営・婚姻外交・宗教改革 詳細ガイド

> [eu5-austria-guide.md](eu5-austria-guide.md) の本編から分離した詳細セクション。パッチ版・確認日は本編に準拠（1.3安定版 buildid 24075414 = 1.3.10、2026-07-11確認）。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。用語対照表・出典は本編（[eu5-austria-guide.md](eu5-austria-guide.md)）に統合済み。

---

## 神聖ローマ帝国運営（オーストリア特化）

> HRE の汎用メカニクス全体については [統治ガイド](eu5-government-guide.md) を参照。本セクションではオーストリアプレイに特化した運用に焦点を当てる。

### 皇帝ボーナス（leader_modifier）一覧

皇帝であるだけで取得する常時ボーナス。HRE 離脱や廃位で即失効するため、維持が戦略の大前提。

| 効果 | 値 | src |
|------|-----|-----|
| 外交容量 | +1 | [src: hre.txt:139] |
| 最大外交官数 | +2 | [src: hre.txt:140] |
| 外交射程 | +500 | [src: hre.txt:141] |
| 要塞上限 | +1 | [src: hre.txt:143] |
| 芸術家スロット | +1 | [src: hre.txt:145] |
| 文化容量 | +1 | [src: hre.txt:146] |
| 政府規模 | +1 | [src: hre.txt:147] |
| 毎月威信 | +0.1 | [src: hre.txt:148] |
| 毎月外交官（頻度） | +0.5 | [src: hre.txt:157] |
| 列強スコア免除閾値 | 50（最低保証、コミュニティ知見：`hre.txt` に該当識別子なし・スクリプト未確認） | [src: Patch_1.2 wiki] |

> （コミュニティ知見：上記ボーナスは 1.1 系スクリプトに基づく。1.2 でのスクリプト変更は未確認）

### 帝国の権威（IA）管理

IA は 0〜100 で変動。皇帝権力強化ポリシーへのアクセス（`improved_imperial_authority_policy` は emperor_comfort 2個必要、`revoke_privilegia_policy` / `renovatio_policy` は 5個必要）に直接関係するため、序盤から意識して管理する。

**IA を上げる主な行動**:

| アクション | IA 増加 | 備考 |
|-----------|--------|------|
| 帝国内平和の維持 | +0.05/月 | 皇帝が HRE メンバーへ攻撃戦争をしないこと |
| 帝国防衛戦争の勝利（hre.904） | +(敵/自比率)×5（上限+10） | オスマン撃退時に大きく増加 |
| 帝国防衛戦争に参戦（hre.908） | 自軍人口/攻撃国人口 × 5（上限 +10） | 序盤でも効果あり |
| 諸侯が帝国宗教に改宗（hre.903） | +(人口比×100、上限+20) | 宗教統一政策と連動 |
| 諸侯を独立解放（hre.901） | +(人口比×10、上限+20) | 臣下を一度解放して IA を稼ぐ手法 |
| 非HRE諸侯の解放（hre.907） | +(人口比×100、上限+20) | 外国支配下の HRE メンバーを解放 |
| 王朝パワーボーナス | +dynastic_power×0.005/月 | 王朝の管理と連動 |

**IA を下げる主な要因（対策も記載）**:

| 要因 | IA 減少 | 対策 |
|------|--------|------|
| 皇帝が HRE メンバーへ攻撃戦争 | −0.5/月 | 帝国外に宣戦する。HRE メンバーへは `cb_imperial_ban` 等の正当なCBを使う |
| 選帝侯不足（1名欠） | −0.1/月 | 選帝侯枠を常に満員に維持 |
| 属国選帝侯（1名） | −0.05/月 | 選帝侯を独立した HRE メンバーに維持 |
| 異教諸侯 | 宗教乖離度×−0.01/月 | 帝国宗教を統一、または異教諸侯を排除 |
| 皇帝が HRE 防衛不参加（hre.909） | `imperial_authority_strong_penalty` | 防衛戦争には必ず参戦する |

> **1.2 注記**: 皇帝の Great Power Score 貢献が 250 → 50 に削減されたことで、IA 管理だけでは大国維持ができなくなった可能性がある（コミュニティ知見：`hre.txt` に該当識別子なし・スクリプト未確認） `[src: Patch_1.2 wiki]`。列強スコアは軍事力・経済力・外交実績で積み上げる必要があり、皇帝地位に依存した従来の大国維持戦略の見直しが必要。

### 皇帝アクション（使いどころ）

| アクション（日本語） | 用途 | 使いどころ |
|---------------------|------|-----------|
| ラント平和令を強制 | 諸侯間戦争を中止させる | 有力諸侯が消耗戦を始めたときに仲裁し IA を守る。1.2 で諸侯間戦争への自動仲裁オプションが Imperial Diet 経由に変更された可能性（コミュニティ知見） |
| 宗教統一の強制 | 諸侯に帝国宗教への改宗を求める | hre.903 を発火させて IA を稼ぐ |
| 不法領土を要求 | 非HRE国が保有する HRE 領土の返還要求 | IA を使って HRE 境界を守る。失敗しても IA ダメージは限定的 |
| 帝国軍を強化 | 諸侯に対オスマン参戦を要請 | 大規模侵攻時に帝国全体を動員 |
| 帝国の禁令（cb_imperial_ban） | 法律侵犯者への宣戦 CB | 大国への CB として利用。HRE 内の問題諸侯を合法的に叩く |
| Imperial Armories 建造（1.2 新規） | 皇帝が HRE 構成員領土内に建造（皇帝のみ建設可・HRE 加盟領内・law:military_contribution 必須）。建造コスト gold=500（HRE Treasury 支出）。自国所有: local_manpower=+0.0025・can_recruit_regiment_in_this_location=yes。外国所有: manpower_to_building_owner=+0.005。皇帝交代時に新皇帝へ移転 | HRE 構成国の軍事力補強 `[src: Patch_1.2 wiki + script verified]`（hre_buildings.txt 行 1-90） |
| 土地剥奪（1.3 新規） | 帝国内の領土剥奪・再分配の権限が皇帝側に集約 | 諸侯統制の手札として使えるが、行使すると諸侯側の反発が生じるため IA・関係値を見ながら慎重に運用する（コミュニティ知見：公式パッチノート由来・スクリプト未確認） |

### 帝国法ロードマップ（集権化路線）

オーストリアが目指す最終形は `renovatio_policy`（帝国の復活、level 5）。以下の順序で段階的に進める。

> **1.2 注記**: 1.2 で Imperial Diet の投票システムが大幅刷新された（Diet 発展段階別の投票権重テーブル）`[src: Patch_1.2 wiki]`。本ロードマップは 1.1 系の経路に基づくため、1.2/1.3 環境での有効性は未検証（コミュニティ知見）。

**前提: 金印勅書（`golden_bull`）の成立**
- HRE に加盟し皇帝になった直後に制定。これがないと他の帝国法に一切アクセスできない

**集権化ポイント（emperor_comfort_policies_counter）の積み方**:

| ステップ | 法律・ポリシー | comfort +1 | 累積 | 解放効果 |
|---------|--------------|-----------|------|---------|
| 1 | `complete_imperial_contribution`（帝国税法 level 3） | ○ | 1 | 国庫・直接貢物の両方解放 |
| 2 | `emperor_successor_preference_policy`（選挙 level 4）または `erbkaisertum_policy`（level 5 世襲） | ○ | 2 | **improved_imperial_authority_policy が解放** |
| 3 | `integrated_electors_policy`（選挙組織 level 5） | ○ | 3 | 皇帝が選帝侯に。選帝侯数−2 |
| 4 | 任意のcomfort改革（例: `great_imperial_army`） | ○ | 4 | — |
| 5 | もう1つのcomfort改革 | ○ | 5 | **revoke_privilegia/renovatio が解放** |

**帝国法（皇帝路線）のポリシー選択指針**:

| 法カテゴリ | 推奨ポリシー | 理由 |
|-----------|------------|------|
| 帝国税法 | `complete_imperial_contribution`（level 3） | comfort +1 かつ国庫・貢物の二重恩恵 |
| 帝国宗教 | `hre_religion_catholic`（または `hre_religion_christian`） | IA ペナルティ回避。プロテスタント多数なら `hre_religion_christian` で妥協も |
| 皇位継承 | `hre_pragmatic_sanction_policy`（国事詔書） | 女性君主を許可。女性相続人が生まれた場合の保険 |
| 皇帝選挙 | `erbkaisertum_policy`（level 5 世襲）が理想。無理なら `emperor_successor_preference_policy`（level 4） | comfort +1＋再選リスク排除 |
| 選挙組織 | `integrated_electors_policy`（level 5） | comfort +1＋皇帝が選帝侯になり投票を掌握 |
| ラント平和令 | `landfriede_rank_4_policy`（永久平和令、level 5） | 諸侯間戦争を永久禁止。HRE 内を完全安定化 |
| 帝国議会 | `hre_tri_camerial_imperial_diet_policy`（三院制） | IA +medium/月。`perpetual_diet_policy` と組み合わせて最大化 |
| 皇帝の権力 | `revoke_privilegia_policy`（level 4）→ `renovatio_policy`（level 5） | 最終目標。全HRE に制度成長+10%。renovatio で帝国統一オプション発火 |

### 選帝侯管理の具体策

**選帝侯枠を満員に維持する**:
- 公・選帝侯（elector）は最大4名 `[src: hre.txt:133]`
- 大司教・選帝侯（archbishop_elector）は最大3名 `[src: hre.txt:134]`
- 1名欠けるごとに IA −0.1/月、属国化すると −0.05/月の追加ペナルティ

**選帝侯の確保策**:
1. 選帝侯が臣下や属国になると枠が消えるため、独立した HRE メンバーとして維持
2. `integrated_electors_policy` を採用すると皇帝自身が選帝侯になり、投票をコントロールしやすくなる
3. 選帝侯が敵国に吸収されそうなら帝国禁令（cb_imperial_ban）や防衛支援で救出

**再選挙のコントロール**:
- `emperor_dynastic_preference_policy`（皇帝王朝優先）で同一王朝に `reasons_to_elect +50` を付与
- `emperor_successor_preference_policy` でさらに +50、合計 +100 の優位で再選が現実的
- 最終的には `erbkaisertum_policy`（世襲制）で選挙そのものを廃止

> **1.2 新規**: Diet UI がタブ化され、投票前のツールチップで可決見込みが確認可能になった `[src: Patch_1.2 wiki]`（コミュニティ知見：UI 変更により選帝侯買収の効率化が期待できる）

> **1.2 新規**: 同一王朝再選で +5 Imperial Authority のボーナスが追加 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）。ハプスブルク家が連続して皇帝を保持し続けることの価値がさらに高まった。

### 帝国防衛のフロー

オスマン帝国など外敵がHREメンバーを攻撃してきたとき:

1. **hre.909 を発動させない** — 防衛戦争に参加しないと IA 強ペナルティ。原則として参戦推奨（資金・消耗状況により例外判断もあり得る）
2. **参戦すると hre.908** — 自軍/敵軍比率 × 5（上限 +10）の IA ボーナス
3. **勝利すると hre.904** — 敵/自比率 × 5（上限 +10）の追加 IA ボーナス
4. **flavor_hab.39（対オスマン支援税）** — オスマン交戦中に発火。選択肢bを選んで威信ボーナス＋IA を守るか、選択肢aで追加税収を得るか判断

#### 重要な変更（1.2）

- **Free Cities 戦争への自動参戦が廃止**: INDEPENDENT Free City（臣属化された Free City は対象外）が攻撃された場合、皇帝は手動で参戦判断が必要 `[src: Patch_1.2 wiki + script verified]`（hre.txt 自動参戦トリガーが存在しないことを確認。オーストリアの帝国防衛意識が変わる重要変更。防衛戦争への手動参戦フローを組み込む必要がある）
- **皇帝は HRE 構成国戦争の指揮権を自動取得しなくなった** `[src: Patch_1.2 wiki]`（コミュニティ知見：連合軍指揮の手動操作が増え、大規模帝国防衛戦での軍管理が複雑化する）

---

## ハプスブルク婚姻外交

### 3段階フロー

```
王室婚姻（royal_marriage）
  ↓ 共通後継者が生まれると自動
結婚連合（marriage_union）= 共同防衛同盟として機能
  ↓ その後継者が複数国を継承すると自動
同君連合（Personal Union）= 統合への第一歩
  ↓ 統合法律を段階的に施行（最短50年＋各要件）
併合（Annexation）
```

**重要**: EU5 の婚姻→連合メカニクスは確認できる範囲では**確定ロジック**（コミュニティ知見：完全網羅未確認）。条件を満たすと自動成立する（コミュニティ知見：ランダムロールは確認されていない）`[src: union.txt, marriage_union.txt]`。

### 同君連合の5つの成立経路

> **1.2 重要変更**: Claim Throne CB は請求者（ruler または heir）が既に対象国を統治中の場合は発行されない `[src: Patch_1.2 wiki]`（コミュニティ知見：継承順位の操作戦略に影響）。婚姻 → 直系相続人空白 → Claim Throne の戦略は条件確認が必要。ハプスブルク家で既に対象国君主を兼任している場合はこの CB が使えないため、別の成立経路（継承法・戦争 CB）を検討すること。

| 経路 | 仕組み | HAB での活用 |
|------|--------|------------|
| ①継承 | 君主交代時に複数国が同一キャラクターを君主として共有すると自動成立 `[src: union.txt:270-295]` | ボヘミア・ハンガリー継承が典型。共通後継者を事前に作ること |
| ②継承法「王位連合」 | `union_of_crowns_succession` — 相互に pact を持つ他国の候補者を継承対象に含める `[src: heir_selections/monarchy.txt]` | 外交的に pact を締結してから後継者共有を狙う |
| ③戦争 | 同君連合戦争（cb_union_war_for_seniority / cb_union_independence）の勝者が自動取得 `[src: _hardcoded.txt:1484-1528]` | 弱体化したBOH/HUNに対して CB を行使 |
| ④平和条約 | 特定 CB の平和条約に `create_union` が直書き | flavor_hab.46（HUNへのCB付与）から発展 |
| ⑤スクリプト効果 | イベント・決定から `create_union_of_integration_level` が呼ばれる `[src: country_effects.txt:2261]` | Privilegium Maius 取得後の特殊経路 |

### 主要3経路の戦略評価

#### ブルゴーニュ継承（flavor_hab.2300〜2303）

| 項目 | 内容 |
|------|------|
| 発火条件 | 1400-1500、BUR存在・非敵対、HAB君主独身男性、BUR女性君主独身後継者なし |
| 戦略価値 | 高い。BUR を通じて低地諸国（ベルギー・オランダ）を取得できる。西欧への足がかり |
| 注意点 | BUR 側が拒否した場合（2303）は opinion 低下。BUR が早期消滅すると発火しない |
| 推奨アクション | 2300 発火前に BUR との好感度を上げておく。ルイ11世（FRA）に BUR が潰される前に動く |

#### ボヘミア継承（flavor_hab.2400〜2403）

| 項目 | 内容 |
|------|------|
| 発火条件 | 1350-1450、BOH存在・非敵対、HAB君主独身男性、BOH君主の成人未婚娘あり |
| 戦略価値 | 最優先。BOH は HRE 内の大国で、同君連合化すると帝国の権威の安定化に直結 |
| 注意点 | BOH が先に他国と婚姻を結ぶと発火しない。早期確保が重要 |
| 推奨アクション | 2400 の発火条件を常に監視。BOH と平和を維持し、好感度を高めておく |

#### スペイン継承（flavor_hab.2600〜2603）

| 項目 | 内容 |
|------|------|
| 発火条件 | 1350-1600、CAS/SPA存在、FRA が共通ライバル、HAB君主独身男性、CAS/SPA に未婚娘あり |
| 戦略価値 | 高い。スペインとの同盟で対仏包囲網が完成。新世界の収入も間接的に恩恵 |
| 注意点 | FRA がライバルでない場合は発火しない。FRA との対立関係を維持する必要あり |
| 推奨アクション | FRA とのライバル設定を維持しながら CAS/SPA と外交を進める |

### 同君連合の維持・強化

**統合レベル（Integration Level）の上げ方**:

| 法律・ポリシー | 統合レベル変化 | 前提条件 | src |
|--------------|--------------|---------|-----|
| `union_senior_succession_law`（継承法の成文化） | +1 | 連合10年以上＋成立条件 | [src: laws/40_personal_unions.txt] |
| `union_unified_treasury_policy`（統一財政） | +1 | 連合20年以上＋前提法 | [src: laws/40_personal_unions.txt] |
| `union_unified_external_diplomacy_policy`（統一外交） | +1 | 連合30年以上＋統一財政 | [src: laws/40_personal_unions.txt] |
| `union_aligned_legislature_policy`（議会統一） | +1 | 連合40年以上＋統一外交 | [src: laws/40_personal_unions.txt] |
| `union_crown_unification_policy`（王冠統合） | +1 | 連合50年以上＋議会統一 | [src: laws/40_personal_unions.txt] |
| 併合（annex） | — | シニアが非subject、統合レベル充足、連合50年以上 | [src: union.txt:23-48] |

**シニアパートナーの地位維持**:
- great_power_score（列強スコア）が最大のメンバーが自動的にシニアに `[src: union.txt:213-222]`
- ジュニアの great_power_score がシニアの 125% 以上になると `take_over_seniority` アクションが解放される
- 常に HAB の国力をジュニア国家を上回る水準に維持すること

**独立戦争への対処**:
- ジュニアが `cb_union_independence` を宣言した場合、敗北すると連合離脱
- 勝利すると HAB が `create_union` で再吸収（確定） `[src: _hardcoded.txt:1484-1528]`
- ジュニアの不満を高める前に統合レベルを上げ、抵抗力を削ぐのが有効

> **1.2 注記**: 王朝力（Dynastic Power）の上限が 200 → 300 に拡大 `[src: Patch_1.2 wiki]`。ハプスブルク家の王朝管理範囲が広がり、PU 維持が容易化した可能性がある（コミュニティ知見：王朝力収入式は未確認）。

### 婚姻連合（Marriage Union）の特徴

- **共同防衛同盟として機能**: 外敵の攻撃に対して常時参戦（`join_defensive_wars_always = yes`） `[src: marriage_union.txt:19-21]`
- **中央集権化は不可**: 統合レベルがないため、Personal Union に昇格させることが目標
- **自動解消条件**: 王室婚姻が切れると自動解散 `[src: marriage_union.txt:64-78]`。婚姻を切らないよう注意

---

## 宗教改革への対応

宗教改革イベント（flavor_hab.1600〜1609、flavor_hab.16・17・34・65・88）は HAB 固有の分量が多く、かつカトリック vs. プロテスタントの選択が HRE 運営全体に直結するため、独立セクションとして記載する。

### Papal Authority（教皇権威）の活用（1.2 新システム）

1.2 で新たに追加された 0〜100 のリソース。カトリック帝国オーストリアにとって戦略的価値が高い `[src: Patch_1.2 wiki]`（コミュニティ知見：以下は未確認情報を含む）。

| Papal Authority 値 | 効果（全カトリック国に均等適用） |
|-------------------|------|
| 75 以上 | monthly_devotion +0.05、monthly_legitimacy +0.02、tolerance_heretic +1.0 `[src: Patch_1.2 wiki + script verified]`（religion.txt 行 776-791） |
| 25 未満 | monthly_devotion -0.1、monthly_legitimacy -0.03 `[src: Patch_1.2 wiki + script verified]`（religion.txt 行 776-791） |

**1.2 でのコスト変更**:
- 列聖（Canonization）コスト: Religious Influence 150 → 75（半額）`[src: Patch_1.2 wiki + script verified]`
- 外交破門コスト: 100 → 50（半額）`[src: Patch_1.2 wiki + script verified]`。プロテスタント諸侯への破門が安価化したことで、早期破門による IA 防衛が従来より低コストで実施可能

**Papal States の制限（1.2）**:
- Papal States は既破門対象への重複破門不可
- Papal States が単独で破門 Resolution を起動することも不可 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）

**オーストリアへの戦略的示唆**: Papal Authority を 75 以上に維持しながら外交破門コストの低下を活用することで、プロテスタント諸侯への早期破門 → IA 防衛のサイクルが以前より安定する（コミュニティ知見）。

### 2つのルート

**カトリック強化路線（史実型）**:
- 目標: 帝国宗教をカトリックに維持し、edict_of_restitution（復旧令進歩）でプロテスタントを再改宗
- キーイベント: flavor_hab.1604（イエズス会支援）→ flavor_hab.1609（再カトリック化）→ flavor_hab.1603 aで妥協し HRE 安定化
- 推奨アドバンス: `edict_of_restitution`（全国改宗速度+10%）を優先取得
- 注意: 三十年戦争（ボチカイ→ベトレン→ラコーツィ連鎖）を避けるため、安定度を常に60以上に維持する

**宗教的寛容路線**:
- 目標: 帝国宗教を `hre_religion_christian`（キリスト教グループ全体）に変更し、プロテスタント諸侯との対立を回避
- キーイベント: flavor_hab.1603 aで妥協支持 → flavor_hab.1602 aで信仰保障承認 → プロテスタント諸侯の IA ペナルティを回避
- 推奨アドバンス: `edict_of_restitution` は取得しなくてよい。`austrian_court` と `geheimrat` を優先
- 注意: 聖職者満足度が低下するため、聖職者 PoP の管理に注意

### 宗教改革イベントチェーン

```
宗教改革勃発
  ├── flavor_hab.1600（オーフェン法令）→ 1601（プファウザー宮廷説教師）
  │       ↓
  │   flavor_hab.1602（ルター派貴族の信仰保障要求）
  │       ↓
  │   flavor_hab.1603（アウクスブルク和議）— a: 妥協 / b: カトリック / c: ルター派
  │       ↓
  ├─[b選択] flavor_hab.1609（再カトリック化）
  │         ↓
  │     flavor_hab.1604（イエズス会学院）→ 1605（苦情）or 1606（カトリック反発）
  │         ↓
  │     flavor_hab.65（シュタイアーマルクの使徒）
  │
  ├── flavor_hab.1607（修道院評議会）— 単独発火
  └── flavor_hab.1608（ボヘミアの信仰告白）— BOH条件
```

### 三十年戦争連鎖への備え

- flavor_hab.84（ボチカイ蜂起）: スロバキア地方20州以上＋カルヴァン派有効＋宗教的寛容改革なし（1600-1630）
- 宗教的寛容改革（tolerance_heretic）を1以上にするか、カルヴァン派が普及する前にスロバキアを安定させると回避可能
- 回避できない場合は安定度を高め、蜂起後の鎮圧に備えて軍事力を温存する

---

## 関連ガイド

- [eu5-austria-guide.md](eu5-austria-guide.md) — 本編（序盤〜終盤戦略、軍事ドクトリン、内政・経済、固有イベント時系列、固有進歩、用語対照表、出典）
- [eu5-government-guide.md](eu5-government-guide.md) — HRE の汎用メカニクス
