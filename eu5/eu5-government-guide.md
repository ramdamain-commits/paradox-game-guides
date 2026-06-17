# EU5 政府タイプ別攻略ガイド（Patch 1.2 時点）

> 5つの政府タイプ（君主制・共和国・神権制・ステップ遊牧民・部族）の特性と運用方針を整理したリファレンス。
> 2026-05-09 確認時点の最新パッチ 1.2「Echinades」（2026-05-06 リリース）に合わせて更新。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。
> 基本メカニクスは [汎用攻略ガイド](eu5-universal-guide.md) を参照。

---

## 概要：5タイプ比較表

| 政府タイプ | 権力リソース | デフォルト階級 | 主な特徴 | 向いているプレイ志向 |
|-----------|------------|--------------|---------|-------------------|
| 君主制（Monarchy） | 正統性（Legitimacy） | 貴族（Nobles） | 王朝婚姻・同君連合（PU）が可能 | 外交・王朝拡大・大国化 |
| 共和国（Republic） | 共和的伝統（Republican Tradition） | 商人（Burghers） | 選挙で安定した統治者を獲得できる | 経済・貿易・都市国家的プレイ |
| 神権制（Theocracy） | 献身（Devotion） | 聖職者（Clergy） | 宗教改宗ボーナス・列強への独自の立ち位置 | 宗教戦略・外交の安定化 |
| ステップ遊牧民（Steppe Horde） | 遊牧民の結束（Horde Unity） | 貴族（Nobles） | 略奪・無名戦争コスト軽減・戦争主体の国家 | 軍事拡張・征服ロールプレイ |
| 部族（Tribe） | 部族の団結（Tribal Cohesion） | 貴族（Nobles） | 農業コスト安い・初期の柔軟性・外交費用削減 | 小国・辺境スタート・改革パス選択 |

> `[src: government_types/00_default.txt:27,58,82,99,127]` — 各 government_power 値はスクリプト確認済み

---

## 君主制（Monarchy）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 正統性（Legitimacy） `[src: government_types/00_default.txt:27]` |
| デフォルト階級 | 貴族階級（Nobles Estate） `[src: government_types/00_default.txt:31]` |
| 継承システム | 長子相続・サリカ法典・分割相続など多数 |
| 宮廷言語ボーナス | なし（基本） |
| 革命的対立（Revolutionary Antagonism） | 20 `[src: government_types/00_default.txt:29]` |
| 嫡子確保モディファイア | あり（care_about_producing_heirs） `[src: government_types/00_default.txt:34]` |

### 強み

| 強み | 詳細 |
|------|------|
| 王朝婚姻・同君連合（PU） | 他国と婚姻を結んで後継者を共有し、継承による同君連合を狙える |
| 継承パスの多様性 | 長子相続・選挙制・サリカ法典など状況に合わせた継承法を選択可能 |
| 貴族階級の強力な召集軍 | Patch 1.1 で Noble Levies の召集量 +50% に上方修正 |
| 政府改革の豊富さ | 封建制・中央集権・絶対王政など多数の改革パスが存在 |

### 弱み

| 弱み | 詳細 |
|------|------|
| 継承危機リスク | 後継者不在・正統性低下時の内乱・摂政政治が発生しやすい |
| 正統性の維持コスト | 正統性が低いと各種ペナルティが発生（コミュニティ知見） |
| 革命的拮抗 | 革命国家との関係に 20 の対立ペナルティ `[src: government_types/00_default.txt:29]` |

### 主要政府改革

| 改革名 | 効果概要 | 備考 |
|--------|---------|------|
| 専制政治（Autocracy） | 王領権力 +10%・貴族向け社会価値ドリフト | デフォルト改革 `[src: government_reforms/monarchy.txt:1]` |
| 封建的貴族（Feudal Nobility） | 臣下忠誠 +5・貴族満足度ボーナス | 仏系特定改革と相互排他 `[src: government_reforms/monarchy.txt:12]` |
| 高貴な生まれ（Of Noble Bearing） | 貴族最大識字 +10 | 時代2（ルネサンス期）から利用可 `[src: government_reforms/monarchy.txt:67]` |

### 序盤の優先事項

1. 後継者を確保する（婚姻・継承法の確認）
2. 正統性を安定域（50以上が目安）に保つ（コミュニティ知見）
3. 貴族階級の権力バランスをチェック。序盤は貴族が強すぎると拡張が鈍化する
4. 同君連合の候補国を早期に特定し、王朝婚姻を仕込む

### 階級（Estate）管理の注意点

- 君主制の標準階級は **貴族（Nobles）**。貴族の権力が高すぎると召集軍は増えるが内政コスト増
- 聖職者・商人との三角バランスを崩さない（コミュニティ知見）
- Patch 1.1 より建造物は貴族が建てられなくなったため、建造物は王領または別階級に発注する

### おすすめ国家

| 国家 | 理由 |
|------|------|
| フランス（France） | 特有改革群で中央集権化・絶対王政への道が整っている |
| カスティーリャ（Castile） | 強力な初期統治者・スペイン形成への足掛かり |
| ハンガリー（Hungary） | 中欧拡大・同君連合の選択肢が豊富（詳細は eu5-hungary-guide.md） |
| オーストリア（Austria） | HRE 帝位保持・婚姻外交の典型例 |
| オスマン帝国（Ottomans） | 強力な継承法・多民族支配のモデルケース |

> HRE 運営の詳細は [オーストリアガイド](eu5-austria-guide.md) を参照。

> **1.2 更新**: 君主制特有の HRE 関連変更が大量。皇帝（君主制限定）の Great Power Score 貢献 250→50 `[src: Patch_1.2 wiki + script verified]`、王朝力上限 200→300、Imperial Diet 投票システム、Free Cities 自動参戦廃止、Imperial Armories 新建造物 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認）。Claim Throne CB は請求者が既統治の場合不発 `[src: Patch_1.2 wiki + script verified]`（PU 継承戦略に影響）

### 1.2 君主制への影響

#### HRE 関連変更（皇帝は君主制限定）

| 変更内容 | 詳細 |
|---------|------|
| Imperial Diet 投票システム | Diet 4段階（Court Assembly → Early Diet → Bicamerial → Tricamerial）`[src: Patch_1.2 wiki + script verified]`（hre.txt 行 15-38, 90-113, 160-183）。各身分の投票権重（実値）: 皇帝 150、選帝侯（世俗）75、大司教選帝侯 75、自由都市 25、首座司教/legatus_natus 4。Diet 段階乗数: Court Assembly は皇帝×1.25・選帝侯×1.5・自由都市×0.1・首座司教×10 / Early Diet は皇帝×1・選帝侯×1.5・自由都市×0.25・首座司教×1 / Bicamerial は皇帝×1・選帝侯×1.25・自由都市×0 / Tricamerial は皇帝×1・選帝侯×1・自由都市×2 `[src: Patch_1.2 wiki + script verified]`（hre.txt 行 15-38, 266-286） |
| 皇帝の Great Power Score 貢献 250→50 | 大幅な弱体化。帝位保持による Great Power 維持戦略を見直す必要あり `[src: Patch_1.2 wiki + script verified]` |
| 王朝力（Dynastic Power）上限 200→300 | 王朝外交の継続選択肢が増加 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Imperial Armories（帝国兵器庫） | 皇帝のみ建設可能な新建造物（HRE 加盟領内・law:military_contribution 必須）。自国所有時 local_manpower +0.0025、外国所有時 manpower_to_building_owner +0.005。建造コスト gold=500。皇帝交代時に移転 `[src: Patch_1.2 wiki + script verified]`（hre_buildings.txt 行 1-90, prices/01_buildings.txt 行 21） |
| Free Cities 自動参戦廃止 | INDEPENDENT Free City への攻撃に限り皇帝が防衛義務を負う仕様に精緻化。皇帝が自由都市の戦争に無条件で自動参戦する挙動は廃止 `[src: Patch_1.2 wiki + script verified]`（hre.txt） |
| HRE 戦争指揮権の自動取得廃止 | 皇帝は HRE 構成国の戦争の指揮権を自動取得しなくなった `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| 同一王朝再選ボーナス | 同一王朝が皇帝に再選されると +5 Imperial Authority `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| 皇帝の政体変更で再選挙 | 皇帝が政体を変更すると再選挙が発生する `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Golden Bull 未制定による諸侯離脱 | 1400 年以降に golden_bull_policy 未採択の場合、HRE 諸侯が離脱可能になった `[src: Patch_1.2 wiki + script verified]`（hre.txt 行 275-277） |
| 軍事政策の不満対象変更 | HRE の軍事政策は全構成員への不満に変更（旧: 自由都市・選帝侯のみ）`[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |

#### Claim Throne CB 制限

- 請求者（ruler または heir）が既に対象国を統治中の場合、Claim Throne CB が使用不可になった `[src: Patch_1.2 wiki + script verified]`
- 同君連合（PU）獲得を Claim Throne で狙うルートは要戦略見直し `[src: Patch_1.2 wiki + script verified]`

> HRE 運営の 1.2 詳細は [eu5-austria-guide.md](eu5-austria-guide.md) を参照。

---

## 共和国（Republic）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 共和的伝統（Republican Tradition） `[src: government_types/00_default.txt:58]` |
| デフォルト階級 | 商人階級（Burghers Estate） `[src: government_types/00_default.txt:60]` |
| 継承システム | 2年/4年任期選挙・ドージェ選挙・籤引き選挙など |
| 宮廷言語ボーナス | 市場言語が宮廷言語の場合に重要度ボーナス（+1） `[src: government_types/00_default.txt:63]` |

### 強み

| 強み | 詳細 |
|------|------|
| 選挙による統治者更新 | 数年ごとに優秀なキャラクターを選出できる。継承危機が発生しない |
| 商人階級のデフォルト強化 | 商人階級がデフォルトで強くなるため、貿易収入が安定しやすい |
| 宮廷言語と市場言語の連携 | 市場言語が宮廷言語と一致している場合のボーナス効果 |
| 商人共和国（Merchant Republic）改革 | 商人容量 +50%・貿易収入 +25%・商人維持費 -25% `[src: government_reforms/republic.txt:28]` |

### 弱み

| 弱み | 詳細 |
|------|------|
| 王朝外交不可 | 婚姻による同君連合・王朝主張は原則不可能 |
| 共和的伝統の低下リスク | 同じ統治者が連続当選すると共和的伝統が低下する。0 近くになると独裁政治へ転落の危機 `[src: game_concepts_l_japanese.yml:874]` |
| 農奴制との相性 | 農民共和国改革は「農奴制 vs 自由農民」社会価値 80 超が条件 `[src: government_reforms/republic.txt:57]` |

### 主要政府改革

| 改革名 | 効果概要 | 備考 |
|--------|---------|------|
| 貴族エリート（Noble Elite） | 貴族権力 +10%・召集軍戦闘効率 +5%・内閣効率 +10% | 主要改革 `[src: government_reforms/republic.txt:1]` |
| くじ引き制（Sortition） | 商人権力 +10%・課税収入ボーナス | 商人方向の社会価値ドリフト `[src: government_reforms/republic.txt:16]` |
| 商人共和国（Merchant Republic） | 商人容量 +50%・貿易収入 +25%・外国建造物コスト -50% | 統合速度 -25% の注意 `[src: government_reforms/republic.txt:28]` |
| 農民共和国（Peasant Republic） | 農民権力 +100%・生産効率ボーナス・議会スロット +1 | 農奴制社会価値 80 超が条件 `[src: government_reforms/republic.txt:46]` |
| ダイナスティック・シニョーリア（Dynastic Signoria） | 政府改革スロット +1・精鋭召集・徴収コスト -10% | イタリア系言語国家専用 `[src: government_reforms/republic.txt:132]` |

### 序盤の優先事項

1. 最初の選挙で最高スコアの候補者を選ぶ習慣をつける
2. 共和的伝統を高い水準（50〜70 以上推奨）で維持する（コミュニティ知見）
3. 商人階級の権力を適切に維持し、貿易収入を最大化する
4. 貿易中心地への投資を序盤から進める

### 選挙の活用法

- 統治者が連続当選すると共和的伝統が下がるため、意図的に交代させるのも選択肢（コミュニティ知見）
- 選挙スコアが高い候補者（高い統治者能力値）を優先する
- 4年任期制より2年任期制のほうが更新頻度が高く、機動的に優秀な統治者を選べる（コミュニティ知見）

### おすすめ国家

| 国家 | 理由 |
|------|------|
| ヴェネツィア（Venice） | ドージェ選挙・商人共和国改革が噛み合う典型例 |
| ホラント（Holland） | 北海貿易の拠点・商人共和国への道が近い |
| ジェノヴァ（Genova） | 二頭政治改革（Diarchy Republic）の固有スタート |
| ディトマルシェン（Dithmarschen） | 農民共和国の固有タグ |

> **1.2 更新**: 新政府改革・特権が追加（具体的内容はスクリプト未確認） `[src: Patch_1.2 wiki]`。共和国プレイは貿易改修（海上ルートコスト 1/10、Maritime Presence が経路コスト反映）の恩恵が大きい（コミュニティ知見：ヴェネツィア・ジェノヴァ・オランダで顕著）

### 1.2 共和国への影響

| 変更内容 | 詳細 |
|---------|------|
| 貿易改修の恩恵 | 海上ルートコスト 1/10・距離影響 50%・Maritime Presence が経路コストに反映。商業共和国（Venice・Genova・Holland）で特に顕著 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Urban Rights（都市特権） | 1.2 新規追加。商業共和国の首都育成戦略に直結する特権 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Megalopolis（メガロポリス） | 首都人口 40 万超で昇格。人口容量・建造物レベルが倍増。商業共和国の首都を優先育成することで中盤以降の経済力が大幅強化 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Heavy/Light 兵科分類 | 共和国も兵科改編の影響を受ける。歩兵・騎兵の Heavy/Light 分類が戦闘計算に影響 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |

---

## 神権制（Theocracy）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 献身（Devotion） `[src: government_types/00_default.txt:82]` |
| デフォルト階級 | 聖職者階級（Clergy Estate） `[src: government_types/00_default.txt:84]` |
| 継承システム | 司教選挙・神権選挙・大修道院長選挙など |
| 改宗ボーナス | 従属国を自動的に自国の宗教に改宗させる `[src: government_types/00_default.txt:87]` |
| 典礼言語ボーナス | 典礼言語が宮廷言語の場合に重要度 +10 `[src: government_types/00_default.txt:88]` |

### 強み

| 強み | 詳細 |
|------|------|
| 自動改宗 | 従属国を強制的に自国の宗教へ改宗（force_convert_created_subjects） `[src: government_types/00_default.txt:87]` |
| 典礼言語ボーナス | 典礼言語が宮廷言語と一致する場合に外交・文化面で有利 |
| 聖職者階級のデフォルト強化 | 宗教インフラへの投資効率が高い |
| 宗教的影響力の高さ | 月次宗教的影響力ボーナスが得やすい |

### 弱み

| 弱み | 詳細 |
|------|------|
| 選挙制継承の固定 | 選挙で後継者が決まるため、優秀な統治者を常に確保できるとは限らない |
| 献身の維持 | 献身が低いと神権制の効率が落ちる。宗教的失政が痛い（コミュニティ知見） |
| 王朝外交の制限 | 婚姻は存在するが、王朝継承ベースの外交は限定的 |

### 主要政府改革

| 改革名 | 効果概要 | 備考 |
|--------|---------|------|
| 修道騎士団（Military Order Reform） | 聖職者の軍指揮権・召集軍 +25%・要塞上限 +25% | カトリック＋修道士政策が必要 `[src: government_reforms/theocracy.txt:1]` |
| 修道院改革（Abbey Reform） | 宗教研究速度ボーナス・改宗ブロック | 首都に修道院の建造物が必要 `[src: government_reforms/theocracy.txt:31]` |
| 教皇特使（Legatus Natus） | 月次宗教的影響力 +0.1・聖職者満足度ボーナス・改革スロット +1 | 固有ロック条件あり `[src: government_reforms/theocracy.txt:53]` |
| 司教公（Prince Bishopric） | 封建型神権制 | 主要改革 `[src: government_reforms/theocracy.txt:77]` |

### 序盤の優先事項

1. 献身の状態を確認し、宗教的な政策・政府改革で安定させる
2. 聖職者階級の満足度を高めて、宗教的影響力を最大化する
3. 宗教改革が始まる前に自国の宗教的統一を固める（コミュニティ知見）
4. 典礼言語と宮廷言語の一致を目指す

### 宗教戦略との連携

- 神権制の自動改宗機能（force_convert_created_subjects）は征服後の従属国を即座に同化できる強力な特性 `[src: government_types/00_default.txt:87]`
- 宗教的影響力（Religious Influence）の蓄積が国内安定・外交に直結（コミュニティ知見）
- カトリック系神権制は教皇との関係管理が重要。教皇の支持が得られると選挙で優位に立てる（コミュニティ知見）

> **1.2 更新（破壊的）**: 正教オーバーホール — Patriarch がキャラクターとして実装、Rite Power 廃止 → Religious Influence 統合、Law/Tenet 刷新 `[src: Patch_1.2 wiki]`（コミュニティ知見：正教系神権制の運用は再検証必要、スクリプト未確認）。詳細は [eu5-religion-guide.md](eu5-religion-guide.md) を参照

### 1.2 神権制への影響

#### カトリック神権制（教皇国・テウトン騎士団等）

| 変更内容 | 詳細 |
|---------|------|
| 列聖コスト 150→75 | Papal Authority 消費コストが半減。聖人候補の推進が容易に `[src: Patch_1.2 wiki + script verified]` |
| 外交破門コスト 100→50 | 破門のコストが半減。対抗手段として使いやすくなった `[src: Patch_1.2 wiki + script verified]` |
| Papal States の制限 | 既に破門された対象への重複破門不可、単独での Resolution 起動不可 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |

#### 正教神権制（コンスタンティノープル総主教国等）

| 変更内容 | 詳細 |
|---------|------|
| Patriarch のキャラクター実装 | 総主教がキャラクターとして存在するようになった。能力値・特性が運用に影響 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Rite Power 廃止 | 旧 Rite Power は廃止され、Religious Influence へ統合 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| Law/Tenet 刷新 | 正教の法律・教義体系が全面改訂。既存の正教神権制プレイは再設計が必要 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |

---

## ステップ遊牧民（Steppe Horde）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 遊牧民の結束（Horde Unity） `[src: government_types/00_default.txt:99]` |
| デフォルト階級 | 貴族階級（Nobles Estate） `[src: government_types/00_default.txt:101]` |
| 統治者死亡ペナルティ | 遊牧民の結束 -50 `[src: government_types/00_default.txt:105]` |
| 無名戦争コスト修正 | -50%（無名開戦コスト半減） `[src: government_types/00_default.txt:106]` |
| 略奪量修正 | +33% `[src: government_types/00_default.txt:107]` |
| 農村集落降格コスト | -75% `[src: government_types/00_default.txt:108]` |
| 戦争スコアコスト | -20% `[src: government_types/00_default.txt:109]` |
| 統合軍備上限閾値 | 0.2（低め）`[src: government_types/00_default.txt:112]` |
| 統合軍備ボーナス/タイプ | -0.01（ペナルティ） `[src: government_types/00_default.txt:113]` |

### 強み

| 強み | 詳細 |
|------|------|
| 無名戦争コスト -50% | 宣戦布告なしの戦争コストが半減。隣接地を容易に攻撃できる `[src: government_types/00_default.txt:106]` |
| 略奪ボーナス | 略奪量 +33%。戦争中の収入確保が容易 `[src: government_types/00_default.txt:107]` |
| 戦争スコアコスト削減 | 講和時に必要な戦争スコアが -20% で、割安に領土を奪取できる `[src: government_types/00_default.txt:109]` |
| 農村降格コスト大幅削減 | -75% で農村集落を降格させやすい。占領地整理に有利 `[src: government_types/00_default.txt:108]` |

### 弱み

| 弱み | 詳細 |
|------|------|
| 統治者死亡で結束 -50 | 統治者が死ぬたびに遊牧民の結束が -50 の大打撃。老齢統治者は要注意 `[src: government_types/00_default.txt:105]` |
| 平時の結束維持が困難 | 結束は時間経過で低下する。戦争・略奪で補充が必要（コミュニティ知見） |
| 統合軍備のペナルティ | 多兵科混成時の Combined Arms ボーナスが他政府タイプより弱い `[src: government_types/00_default.txt:112-113]` |
| 定住化国への転換コスト | 君主制への移行には 15 年かかる `[src: actions_l_japanese.yml:352]` |

### 主要政府改革

| 改革名 | 効果概要 | 備考 |
|--------|---------|------|
| チンギス・ハーンの遺産（Legacy of Genghis） | 騎兵維持費 -10%・宮廷費 -2% | モンゴル文化またはボルジギン王朝のみ。army タイプ国家が条件 `[src: government_reforms/steppe_horde.txt:1]` |

### 序盤の優先事項

1. 結束（Horde Unity）の初期値を確認。開幕直後は積極的に戦争を仕掛けて結束を補充する
2. 無名戦争コスト半減を利用して隣接する弱小国を次々と侵略する
3. 略奪で金収入を確保しつつ、部隊の維持費を賄う（コミュニティ知見）
4. 統治者の年齢に注意。高齢統治者の死亡時に -50 ショックへの備えが必要

### 定住化パスの判断基準

| 状況 | 判断 |
|------|------|
| 広大な草原地帯を支配・騎兵重視継続 | ステップ遊牧民のまま維持 |
| 農耕地帯の支配が中心になってきた | 君主制への移行を検討（15年かかる） `[src: actions_l_japanese.yml:352]` |
| ペルシャ・中東・東欧の強国と競合 | 内政ボーナスの高い君主制への移行でスケールアップ（コミュニティ知見） |

### おすすめ国家

| 国家 | 理由 |
|------|------|
| 元（Yuan） | チンギス・ハーンの遺産改革が使える・広大な初期領土 |
| カザン（Kazan） | モスクワへの対抗・草原の拠点 |
| 白羊朝（Aq Qoyunlu） | 中東進出の足掛かり |
| モゴリスタン（Moghulistan） | 中央アジア拡大のプラットフォーム |

> **1.2 更新**: ロジスティクス距離 50→30（army_logistics_distance=30）・軍の食料消費 10 倍で大規模遊牧軍の補給管理が難化。騎兵主力の大部隊運用は再検討が必要 `[src: Patch_1.2 wiki + script verified]`（auto_modifiers/country.txt 行 90, unit_categories food_consumption_per_strength）

### 1.2 ホード/部族への影響

| 変更内容 | 詳細 |
|---------|------|
| 騎兵の Light Cavalry 分類 | ホード騎兵は Light Cavalry 系統に分類される可能性が高い。Heavy/Light 分類変更が戦闘・編成効率に影響 `[src: Patch_1.2 wiki]`（コミュニティ知見：スクリプト未確認） |
| 軍の食料消費 10 倍 | 大規模遊牧軍の補給コストが大幅増加。分散進軍・略奪ルートの計画が重要に `[src: Patch_1.2 wiki + script verified]`（unit_categories food_consumption_per_strength） |
| ロジスティクス距離 50→30 | army_logistics_distance=30。補給可能距離が大幅縮小。遠征ルートの見直しが必要 `[src: Patch_1.2 wiki + script verified]`（auto_modifiers/country.txt 行 90） |

---

## 部族（Tribe）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 部族の団結（Tribal Cohesion） `[src: government_types/00_default.txt:127]` |
| デフォルト階級 | 貴族階級（Nobles Estate） `[src: government_types/00_default.txt:129]` |
| 農村集落降格コスト | -50% `[src: government_types/00_default.txt:133]` |
| 貴族の食料消費 | -25%（維持コスト削減） `[src: government_types/00_default.txt:134]` |
| 外交維持費修正 | -75%（外交スロットの維持コストが大幅に安い） `[src: government_types/00_default.txt:135]` |
| 共通言語重要度ボーナス | +10 `[src: government_types/00_default.txt:132]` |

### 強み

| 強み | 詳細 |
|------|------|
| 外交維持費 -75% | 外交スロットの維持コストが大幅に安い。多くの関係を低コストで維持できる `[src: government_types/00_default.txt:135]` |
| 農村降格コスト -50% | ステップ遊牧民ほどではないが農村の降格コストが低い `[src: government_types/00_default.txt:133]` |
| 貴族食料消費 -25% | 貴族維持コストが安く、辺境スタートでの国内安定に寄与 `[src: government_types/00_default.txt:134]` |
| 柔軟な改革パス | 君主制・ステップ遊牧民への転換オプションがあり、将来の方針変更がしやすい |

### 弱み

| 弱み | 詳細 |
|------|------|
| 部族の団結の維持 | 団結が低いと国内が不安定になる。宗教・文化の統一が鍵 `[src: game_concepts_l_japanese.yml:883]` |
| 中央集権化の遅さ | 内政インフラの整備が君主制より遅い傾向（コミュニティ知見） |
| 政府改革の少なさ | 部族専用の改革はステップ遊牧民や君主制と比べて少ない |

### 主要政府改革

| 改革名 | 効果概要 | 備考 |
|--------|---------|------|
| ハウデノサニー氏族母たち（Haudenosaunee Clan Mothers） | 全階級満足度ボーナス・文化的伝統 +0.1 | ハウデノサニー文化圏専用・部族の団結 80 以上で使用可 `[src: government_reforms/country_specific.txt:1592]` |

### 序盤の優先事項

1. 部族の団結（Tribal Cohesion）の初期値を確認。文化・宗教の統一度が反映される
2. 外交維持費の安さを活かして、早期に同盟・従属関係を広く構築する（コミュニティ知見）
3. 部族の団結が高いうちに政府改革パスを選択しておく
4. 君主制への移行時期を早めに計画する（農耕化が進んだら切り替えが有利）

### 改革パスの選択肢

| パス | 条件 | メリット |
|------|------|---------|
| 君主制（Monarchy）への移行 | 条件を満たした時点で実行可 | 内政・外交の全機能にアクセス可能 |
| ステップ遊牧民（Steppe Horde）への転換 | army タイプ国家として条件を満たす場合（未検証） | 略奪・無名戦争コスト削減が加わる |
| 部族のまま維持 | 特定の固有改革がある場合 | 外交コスト削減の恩恵を享受し続ける |

> **1.2 更新**: 新政府改革・特権が追加（具体的内容はスクリプト未確認）`[src: Patch_1.2 wiki]`（コミュニティ知見）。ロジスティクス距離縮小（army_logistics_distance=30）・食料消費増加の影響はホードと共通 `[src: Patch_1.2 wiki + script verified]`（auto_modifiers/country.txt 行 90, unit_categories food_consumption_per_strength）

---

## 政府変更の判断基準と手順

### 変更コスト

| コスト | 値 | 出典 |
|--------|-----|------|
| 安定度（Stability） | -50 | `[src: prices/00_hardcoded.txt:1101-1103]` |
| 政府権力（Government Power）または正統性など | -25 | `[src: prices/00_hardcoded.txt:1101-1103]` |

> `change_government_type_price = { stability = 50, legitimacy = 25 }` — スクリプト確認済み

### 政府改革の削除コスト

| コスト | 値 | 出典 |
|--------|-----|------|
| 安定度（Stability） | -20 | `[src: prices/00_hardcoded.txt:64-67]` |
| 義（Righteousness） | -10 | `[src: prices/00_hardcoded.txt:64-67]` |

> `remove_government_reform = { stability = 20, righteousness = 10 }` — スクリプト確認済み

### いつ政府を変更すべきか

| 状況 | 推奨アクション |
|------|--------------|
| 部族 → 君主制 | 農耕地帯が中心になり、内政インフラの充実が必要になったとき |
| ステップ遊牧民 → 君主制 | 騎馬遊牧のメリットが薄れ、定住化した領土が多くなったとき（移行に 15 年） |
| 君主制 → 共和国 | 貴族階級が弱く、商人・貿易中心の国家運営をしたいとき |
| 君主制 → 神権制 | 宗教的一体化・改宗戦略を主軸にした場合 |

### 変更しない方がいい場合

- 安定度が低い（-2 〜 0 付近）ときは変更コストがさらに痛くなる（コミュニティ知見）
- 継承危機・内乱イベント発生中は変更後のペナルティが重複する恐れがある（コミュニティ知見）
- 現在の政府タイプ固有の固有改革・特権でロックされている改革がある場合は、まず削除コストを支払う必要がある

---

## Patch 1.2「Echinades」政府タイプ別変更まとめ

Patch 1.2（2026-05-06 リリース）で確認された政府タイプ関連の主要変更一覧。各セクションの詳細節を参照。

| 対象 | 内容 |
|------|------|
| 君主制 | HRE 大幅オーバーホール（Imperial Diet・Armories・GP Score 減少・王朝力上限拡大など） |
| 君主制 | Claim Throne CB：請求者が既統治の場合不発 |
| 共和国 | 新政府改革・特権追加、貿易改修恩恵、Urban Rights / Megalopolis 追加 |
| 神権制（カトリック） | Papal Authority コスト半減（列聖 150→75、破門 100→50）、Papal States 制限追加 |
| 神権制（正教） | 正教オーバーホール（Patriarch キャラクター実装、Rite Power 廃止） |
| ステップ遊牧民・部族 | ロジスティクス距離 50→30（army_logistics_distance=30）・食料消費 10 倍で大規模軍運用難化 `[src: Patch_1.2 wiki + script verified]`（auto_modifiers/country.txt 行 90, unit_categories food_consumption_per_strength） |
| 全政府タイプ | 官僚制（Bureaucracies）— 1.2 では実装されなかった（コミュニティ知見：将来パッチでの実装可能性は未確定） |

> 情報元: EU5 Wiki パッチノート（Patch 1.2「Echinades」、2026-05-06）

---

## 1.3 オープンベータ差分（政府タイプ別・純追記）

> **本セクションは 1.3 オープンベータ（buildid 23683141 / BetaKey `1.3-open-beta`）のローカルスクリプトと公式 1.3.0 / 1.3.2 パッチノートを独立検証基準とする。上位の 1.2「Echinades」baseline とは独立であり、1.2 本体章の数値・記述には一切手を加えていない。**
> 1.3 はオープンベータのため数値が変動しうる。安定版リリースまで本セクション内に封じ込め、本文（1.2 baseline）には昇格させない。
> マーカー: `[src: ...]（1.3 beta）` = ローカル 1.3 スクリプトで実値確認 / `（コミュニティ知見：1.3 beta、公式パッチノート由来・スクリプト未確認）` = エンジン内部値でスクリプトに実値がなく、1.2/1.3 パッチノート突き合わせで真正な変更と確定した項目。

### 身分・官僚制

- 身分（Estate）に文化・宗教の属性が付与され、全政体で身分の文化・宗教が管理対象になった `[src: common/estates/00_default.txt]（1.3 beta）`。異文化・異宗教の身分は満足度・反乱挙動に影響する。
- **官僚制（Bureaucracies）が 1.3 で実装された**（1.2 では未実装だった項目）。汎用 10 種・ビザンツ固有 10 種・中華固有 4 種が定義されている `[src: common/bureaucracies/generic.txt（10 種）, byz.txt（10 種）, china.txt（4 種）]（1.3 beta）`。
- 新規政府改革が多数追加（公式ノートでは新規 17 種）（コミュニティ知見：1.3 beta、公式パッチノート由来・スクリプト未確認。「新規」判定は版間ノート差分による）。

### 権力リソースのペナルティ

- **低 Devotion（献身）ペナルティ**: 献身が低い君主制（devotion 型）で月次の宗教的影響力 `monthly_religious_influence = -0.1`、身分満足度ペナルティが発生 `[src: auto_modifiers/country.txt low_devotion ブロック]（1.3 beta）`。
- **低 Republican Tradition（共和的伝統）ペナルティ**: 共和的伝統が低い共和制で republican_tradition にスケールするペナルティが発生 `[src: auto_modifiers/country.txt low_republican_tradition ブロック（scales_with republican_tradition）]（1.3 beta）`。

### 国家固有改革・コスト

- **Prikazi 改革 / Collegium 改革**（ロシア系 MOS/RUS）の内閣効率（country_cabinet_efficiency）が現値 **0.10**（1.2 ノートでは 0.15 / 0.20 → 1.3 で 0.10 に引き下げ）`[src: government_reforms/country_specific.txt prikazi_reform 行 2407 / collegium_reform 行 2932: country_cabinet_efficiency = 0.10]（1.3 beta）`。旧値 0.15 / 0.20 は 1.2 → 1.3 パッチノート差分で確認。
- **Voivode 改革**（ポーランド/カルパチア系）が政府改革として存在 `[src: government_reforms/country_specific.txt]（1.3 beta）`。地域章（regional ガイド）の Voivode 記述と相互参照。
- **退位（Abdicate）コスト**: 威信 50 + 正統性 40 `[src: prices/03_diplomacy.txt:115 abdicate_price（prestige=50, legitimacy=40）]（1.3 beta）`。

### 内閣（Cabinet）と自動化

- 内閣の 2 長（2 名の長官職）同時封鎖が制限される変更（コミュニティ知見：1.3 beta、公式パッチノート由来・スクリプト未確認）。
- 内閣自動化が Members（内閣メンバー）と Actions（内閣アクション）の 2 系統に分割（コミュニティ知見：1.3 beta、公式パッチノート由来・スクリプト未確認）。汎用ガイドの 1.3 差分も参照。

### 宮廷芸術家（Court Artists）の廷臣管理

- 宮廷芸術家が **12 種**（彫刻家・作曲家・作家・建築家・哲学者・法学者・科学者・イコン画家・金属細工師・書家・語り部・医師）に整理された `[src: artist_types/00_default.txt（12 種）]（1.3 beta）`。
- 芸術家の招聘は専用の国家インタラクションで行い、条件・コストの制約がかかる `[src: country_interactions/invite_artist.txt]（1.3 beta）`。廷臣（Courtier）枠として宮廷を圧迫するため、政体ごとの宮廷管理方針に影響する。

---

## 1.2 新規用語（政府タイプ別ガイド範囲）

Patch 1.2 で追加・変更された政府タイプ関連の用語。完全版は [ローカライズ対照表](localization-reference.md) へ。

| 日本語（仮称・英語併記） | 英語 | 備考 |
|----------------------|------|------|
| 帝国議会 | Imperial Diet | 投票システム。Diet 発展段階（Court Assembly→Early Diet→Bicamerial→Tricamerial）別の投票権重。身分ごとの基本値と段階乗数はHRE関連変更テーブル参照 `[src: Patch_1.2 wiki + script verified]`（hre.txt 行 15-38, 266-286）。1.2 更新 |
| 帝国兵器庫 | Imperial Armories | 1.2 新規建造物。皇帝のみ建設可（HRE 加盟領内・law:military_contribution 必須）。Manpower 提供、皇帝交代時に移転 `[src: Patch_1.2 wiki + script verified]` |
| 教皇権威 | Papal Authority | 神権制カトリック国に影響。1.2 でコスト変更（列聖 150→75、破門 100→50） |
| 王朝力 | Dynastic Power | 上限が 1.2 で 200→300 に拡大 |
| ローマ国境回復 CB | Restore Roman Borders | 1.2 新規ビザンツ用 CB `[src: Patch_1.2 wiki + script verified]` |
| 都市特権 | Urban Rights | 1.2 新規。共和国・首都育成に影響 |
| メガロポリス | Megalopolis | 1.2 新規。首都人口 40 万超で昇格。人口容量・建造物レベルが倍増 |
| プロノイア | Pronoia | 1.2 新規ビザンツ用サブジェクト。君主制下位互換の従属形態 |
| カテパナタ | Katepanata | 1.2 新規ビザンツ用政体改革 |

---

## 用語対照表

このガイドで使用した主要用語。完全版は [ローカライズ対照表](localization-reference.md) へ。

| 日本語（ゲーム内表記） | 英語 | 備考 |
|----------------------|------|------|
| 君主制 | Monarchy | `[src: government_names_l_japanese.yml:900]` |
| 共和国 | Republic | `[src: government_names_l_japanese.yml:903]` |
| 神権制 | Theocracy | `[src: government_names_l_japanese.yml:904]` |
| ステップ遊牧民 | Steppe Horde | `[src: government_names_l_japanese.yml:902]` |
| 部族 | Tribe | `[src: government_names_l_japanese.yml:901]` |
| 正統性 | Legitimacy | `[src: government_l_japanese.yml:27]` |
| 共和的伝統 | Republican Tradition | `[src: government_l_japanese.yml:28]` |
| 献身 | Devotion | `[src: government_l_japanese.yml:29]` |
| 遊牧民の結束 | Horde Unity | `[src: government_l_japanese.yml:30]` |
| 部族の団結 | Tribal Cohesion | `[src: government_l_japanese.yml:31]` |
| 政府改革 | Government Reform | — |
| 政府タイプ変更 | Change Government Type | — |
| 安定度 | Stability | — |
| 同君連合 | Personal Union (PU) | — |
| 階級 | Estate | — |
| 貴族階級 | Nobles Estate | — |
| 商人階級 | Burghers Estate | — |
| 聖職者階級 | Clergy Estate | — |
| 宮廷言語 | Court Language | — |
| 典礼言語 | Liturgical Language | — |
| 無名戦争 | War with No CB | CB = 開戦事由（Casus Belli） |
| 官僚制（**1.3 beta 仮登録**） | Bureaucracies | 1.3 で実装。汎用10/ビザンツ10/中華4 種 `[src: common/bureaucracies/]（1.3 beta）` |
| Voivode 改革（**1.3 beta 仮登録**） | Voivode Reform | ポーランド/カルパチア系の政府改革 `[src: government_reforms/country_specific.txt]（1.3 beta）` |
| 退位（**1.3 beta 仮登録**） | Abdicate | 威信50+正統性40 `[src: prices/03_diplomacy.txt:115]（1.3 beta）` |
| 宮廷芸術家（**1.3 beta 仮登録**） | Court Artists | 1.3 刷新。12 種 `[src: artist_types/00_default.txt]（1.3 beta）` |

> 上記「1.3 beta 仮登録」の用語は安定版リリース後に中央 `localization-reference.md` へ正式昇格する。

---

## 出典

### 一次情報（スクリプト確認済み）

| ファイル | 内容 |
|--------|------|
| `in_game/common/government_types/00_default.txt` | 各政府タイプの権力リソース・デフォルト階級・固有モディファイア |
| `in_game/common/government_reforms/monarchy.txt` | 君主制の政府改革定義 |
| `in_game/common/government_reforms/republic.txt` | 共和国の政府改革定義 |
| `in_game/common/government_reforms/theocracy.txt` | 神権制の政府改革定義 |
| `in_game/common/government_reforms/steppe_horde.txt` | ステップ遊牧民の政府改革定義 |
| `in_game/common/government_reforms/common.txt` | 全政府タイプ共通の改革定義 |
| `in_game/common/government_reforms/country_specific.txt` | 国家固有の政府改革（部族改革含む） |
| `in_game/common/prices/00_hardcoded.txt:1101-1104` | 政府タイプ変更コスト（安定度 -50、正統性 -25） |
| `in_game/common/prices/00_hardcoded.txt:64-67` | 政府改革削除コスト（安定度 -20、義 -10） |
| `in_game/common/international_organizations/hre.txt` | 皇帝 Great Power Score 免除閾値（`great_power_score_exempt_from_forfeit = 50`）; Imperial Diet 各段階の投票権重（行 15-38: Court Assembly, 90-113: Early Diet, 160-183: Bicamerial, 266-286: Tricamerial）; Golden Bull 未採択時の諸侯離脱条件（行 275-277: `current_year > 1400`） |
| `in_game/common/casus_belli/claim_throne.txt` | Claim Throne CB 発動制限（`not = { this = scope:target.ruler }`） |
| `in_game/common/parliament_types/01_international_organization.txt` | Imperial Diet 4段階定義（Court Assembly → Early Diet → Bicamerial → Tricamerial） |
| `in_game/common/casus_belli/D008_restore_roman_borders.txt` | Restore Roman Borders CB 定義 |
| `in_game/common/building_types/hre_buildings.txt` | Imperial Armories 建造物定義（建造コスト gold=500、local_manpower +0.0025、manpower_to_building_owner +0.005、設置条件: 皇帝のみ・HRE 加盟領内・law:military_contribution） |
| `in_game/common/prices/01_buildings.txt` | Imperial Armories 建造コスト（行 21） |
| `in_game/common/auto_modifiers/country.txt` | ロジスティクス距離定数（行 90: army_logistics_distance=30）; 低 Devotion ペナルティ（low_devotion: monthly_religious_influence=-0.1）; 低 Republican Tradition ペナルティ（low_republican_tradition 行 573, 1.3 beta） |
| `in_game/common/bureaucracies/` | 官僚制定義（generic 10種・byz 10種・china 4種、1.3 beta） |
| `in_game/common/estates/00_default.txt` | 身分の文化・宗教属性（1.3 beta） |
| `in_game/common/government_reforms/country_specific.txt` | Prikazi/Collegium 改革の country_cabinet_efficiency=0.10（行 2407/2932）、Voivode 改革（1.3 beta） |
| `in_game/common/prices/03_diplomacy.txt:115` | 退位コスト（abdicate_price: prestige=50, legitimacy=40、1.3 beta） |
| `in_game/common/artist_types/00_default.txt` | 宮廷芸術家 12 種の定義（1.3 beta） |
| `in_game/common/country_interactions/invite_artist.txt` | 宮廷芸術家招聘の制約（1.3 beta） |
| `in_game/common/unit_categories/` | food_consumption_per_strength（兵科別食料消費係数） |
| `main_menu/localization/japanese/government_l_japanese.yml` | 権力リソース・継承システムの日本語ローカライズ |
| `main_menu/localization/japanese/government_names_l_japanese.yml` | 政府タイプ名の日本語ローカライズ |
| `main_menu/localization/japanese/game_concepts_l_japanese.yml` | 権力リソースの説明テキスト |
| `main_menu/localization/japanese/actions_l_japanese.yml` | 政府変更アクションのテキスト（15年移行期間等） |

### Wiki 参照（Patch 1.2）

| 内容 | URL |
|------|-----|
| Patch 1.2 パッチノート | `https://eu5.paradoxwikis.com/Patch_1.2` |
| Patch 1.3 パッチノート（1.3 beta 差分の出典） | `https://eu5.paradoxwikis.com/Patch_1.3` |
| Holy Roman Empire メカニクス | `https://eu5.paradoxwikis.com/Holy_Roman_Empire` |
| Fate of the Phoenix（ビザンツ関連） | `https://eu5.paradoxwikis.com/Fate_of_the_Phoenix` |

### コミュニティ情報

| 内容 | 出典 |
|------|------|
| 正統性の安定域（50以上）の目安 | EU5 コミュニティ知見（Steam フォーラム・Reddit r/eu5） |
| 共和的伝統の維持目安（50〜70 以上） | EU5 コミュニティ知見 |
| 部族から君主制への移行タイミング | EU5 コミュニティ知見 |
| ステップ遊牧民の結束補充戦略 | EU5 コミュニティ知見 |
| Patch 1.2 変更情報（script verified 済み） | Imperial Armories（hre_buildings.txt, prices/01_buildings.txt）・Free Cities 自動参戦廃止（hre.txt）・ロジスティクス距離/食料消費（auto_modifiers/country.txt, unit_categories）は EU5 スクリプト実値確認済み |
| Patch 1.2 変更情報（コミュニティ知見） | 共和国新政府改革・特権・部族新特権（具体値スクリプト未確認）、王朝力上限 200→300（スクリプト未確認）、HRE 戦争指揮権廃止・同一王朝再選ボーナス・皇帝政体変更再選挙（スクリプト未確認）は EU5 Wiki パッチノートおよびコミュニティ知見に基づく |
