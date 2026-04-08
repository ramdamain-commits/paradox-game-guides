# EU5 政府タイプ別攻略ガイド（Patch 1.1 時点）

> 5つの政府タイプ（君主制・共和国・神権制・ステップ遊牧民・部族）の特性と運用方針を整理したリファレンス。
> 2026-04-08 確認時点の最新パッチ 1.1.10 に合わせて更新。
> 日本語は原則としてゲーム内ローカライズ準拠。未翻訳の箇所は英語を併記する。

---

## 概要：5タイプ比較表

| 政府タイプ | 権力リソース | デフォルト身分 | 主な特徴 | 向いているプレイ志向 |
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
| デフォルト身分 | 貴族身分（Nobles Estate） `[src: government_types/00_default.txt:31]` |
| 継承システム | 長子相続・サリカ法典・分割相続など多数 |
| 宮廷言語ボーナス | なし（基本） |
| 革命的対立（Revolutionary Antagonism） | 20 `[src: government_types/00_default.txt:29]` |
| 嫡子確保モディファイア | あり（care_about_producing_heirs） `[src: government_types/00_default.txt:34]` |

### 強み

| 強み | 詳細 |
|------|------|
| 王朝婚姻・同君連合（PU） | 他国と婚姻を結んで後継者を共有し、継承による同君連合を狙える |
| 継承パスの多様性 | 長子相続・選挙制・サリカ法典など状況に合わせた継承法を選択可能 |
| 貴族身分の強力な召集軍 | Patch 1.1 で Noble Levies の召集量 +50% に上方修正 |
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
3. 貴族身分の権力バランスをチェック。序盤は貴族が強すぎると拡張が鈍化する
4. 同君連合の候補国を早期に特定し、王朝婚姻を仕込む

### エステート（身分）管理の注意点

- 君主制の標準身分は **貴族（Nobles）**。貴族の権力が高すぎると召集軍は増えるが内政コスト増
- 聖職者・商人との三角バランスを崩さない（コミュニティ知見）
- Patch 1.1 より建造物は貴族が建てられなくなったため、建造物は王領または別身分に発注する

### おすすめ国家

| 国家 | 理由 |
|------|------|
| フランス（France） | 特有改革群で中央集権化・絶対王政への道が整っている |
| カスティーリャ（Castile） | 強力な初期統治者・スペイン形成への足掛かり |
| ハンガリー（Hungary） | 中欧拡大・同君連合の選択肢が豊富（詳細は eu5-hungary-guide.md） |
| オーストリア（Austria） | HRE 帝位保持・婚姻外交の典型例 |
| オスマン帝国（Ottomans） | 強力な継承法・多民族支配のモデルケース |

> ⚠ **1.2 更新候補**: 官僚制（Bureaucracies）システム導入で、君主制の内閣スロット運用に新たな選択肢が加わる可能性あり

---

## 共和国（Republic）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 共和的伝統（Republican Tradition） `[src: government_types/00_default.txt:58]` |
| デフォルト身分 | 商人身分（Burghers Estate） `[src: government_types/00_default.txt:60]` |
| 継承システム | 2年/4年任期選挙・ドージェ選挙・籤引き選挙など |
| 宮廷言語ボーナス | 市場言語が宮廷言語の場合に重要度ボーナス（+1） `[src: government_types/00_default.txt:63]` |

### 強み

| 強み | 詳細 |
|------|------|
| 選挙による統治者更新 | 数年ごとに優秀なキャラクターを選出できる。継承危機が発生しない |
| 商人身分のデフォルト強化 | 商人身分がデフォルトで強くなるため、貿易収入が安定しやすい |
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
3. 商人身分の権力を適切に維持し、貿易収入を最大化する
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

> ⚠ **1.2 更新候補**: 新政府改革・特権の追加で共和国プレイの選択肢が広がる可能性あり

---

## 神権制（Theocracy）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 献身（Devotion） `[src: government_types/00_default.txt:82]` |
| デフォルト身分 | 聖職者身分（Clergy Estate） `[src: government_types/00_default.txt:84]` |
| 継承システム | 司教選挙・神権選挙・大修道院長選挙など |
| 改宗ボーナス | 従属国を自動的に自国の宗教に改宗させる `[src: government_types/00_default.txt:87]` |
| 典礼言語ボーナス | 典礼言語が宮廷言語の場合に重要度 +10 `[src: government_types/00_default.txt:88]` |

### 強み

| 強み | 詳細 |
|------|------|
| 自動改宗 | 従属国を強制的に自国の宗教へ改宗（force_convert_created_subjects） `[src: government_types/00_default.txt:87]` |
| 典礼言語ボーナス | 典礼言語が宮廷言語と一致する場合に外交・文化面で有利 |
| 聖職者身分のデフォルト強化 | 宗教インフラへの投資効率が高い |
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
2. 聖職者身分の満足度を高めて、宗教的影響力を最大化する
3. 宗教改革が始まる前に自国の宗教的統一を固める（コミュニティ知見）
4. 典礼言語と宮廷言語の一致を目指す

### 宗教戦略との連携

- 神権制の自動改宗機能（force_convert_created_subjects）は征服後の従属国を即座に同化できる強力な特性 `[src: government_types/00_default.txt:87]`
- 宗教的影響力（Religious Influence）の蓄積が国内安定・外交に直結（コミュニティ知見）
- カトリック系神権制は教皇との関係管理が重要。教皇の支持が得られると選挙で優位に立てる（コミュニティ知見）

> ⚠ **1.2 更新候補**: 東方正教会の詳細メカニクス追加により、正教系神権制（コンスタンティノープル総主教国など）の運用が大きく変わる可能性あり

---

## ステップ遊牧民（Steppe Horde）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 遊牧民の結束（Horde Unity） `[src: government_types/00_default.txt:99]` |
| デフォルト身分 | 貴族身分（Nobles Estate） `[src: government_types/00_default.txt:101]` |
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

> ⚠ **1.2 更新候補**: 新政府改革・特権の追加でステップ遊牧民の運用改善が見込まれる。兵站の見直しも騎兵主力編成に影響する可能性あり

---

## 部族（Tribe）

### 基本情報

| 項目 | 値 / 内容 |
|------|---------|
| 権力リソース | 部族の団結（Tribal Cohesion） `[src: government_types/00_default.txt:127]` |
| デフォルト身分 | 貴族身分（Nobles Estate） `[src: government_types/00_default.txt:129]` |
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
| ハウデノサニー氏族母たち（Haudenosaunee Clan Mothers） | 全身分満足度ボーナス・文化的伝統 +0.1 | ハウデノサニー文化圏専用・部族の団結 80 以上で使用可 `[src: government_reforms/country_specific.txt:1592]` |

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

> ⚠ **1.2 更新候補**: 新政府改革・特権の追加で部族の改革パスが拡充される可能性あり

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
| 君主制 → 共和国 | 貴族身分が弱く、商人・貿易中心の国家運営をしたいとき |
| 君主制 → 神権制 | 宗教的一体化・改宗戦略を主軸にした場合 |

### 変更しない方がいい場合

- 安定度が低い（-2 〜 0 付近）ときは変更コストがさらに痛くなる（コミュニティ知見）
- 継承危機・内乱イベント発生中は変更後のペナルティが重複する恐れがある（コミュニティ知見）
- 現在の政府タイプ固有の固有改革・特権でロックされている改革がある場合は、まず削除コストを支払う必要がある

---

## 1.2 更新候補まとめ

以下は本文中の各セクションに埋め込んだ `⚠ 1.2 更新候補` の一覧。Patch 1.2「エキナデス」正式リリース後に要確認。

| 対象 | 内容 |
|------|------|
| 全政府タイプ | 官僚制（Bureaucracies）新システム導入で内閣スロット運用に変化が生じる可能性 |
| 全政府タイプ | 新政府改革・特権の追加（各タイプに何が追加されるか要確認） |
| 神権制 | 東方正教会メカニクス追加による正教系神権制の運用変化 |
| ステップ遊牧民 | 兵站の見直しによる騎兵主力編成への影響 |

> 情報元: EU5 開発日記（Tinto Talks #100〜101）・オープンベータ（2026-04-08 確認）

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
| 身分 | Estate | — |
| 貴族身分 | Nobles Estate | — |
| 商人身分 | Burghers Estate | — |
| 聖職者身分 | Clergy Estate | — |
| 宮廷言語 | Court Language | — |
| 典礼言語 | Liturgical Language | — |
| 無名戦争 | War with No CB | CB = 開戦事由（Casus Belli） |

---

## 出典

### 一次情報（スクリプト確認済み）

| ファイル | 内容 |
|--------|------|
| `in_game/common/government_types/00_default.txt` | 各政府タイプの権力リソース・デフォルト身分・固有モディファイア |
| `in_game/common/government_reforms/monarchy.txt` | 君主制の政府改革定義 |
| `in_game/common/government_reforms/republic.txt` | 共和国の政府改革定義 |
| `in_game/common/government_reforms/theocracy.txt` | 神権制の政府改革定義 |
| `in_game/common/government_reforms/steppe_horde.txt` | ステップ遊牧民の政府改革定義 |
| `in_game/common/government_reforms/common.txt` | 全政府タイプ共通の改革定義 |
| `in_game/common/government_reforms/country_specific.txt` | 国家固有の政府改革（部族改革含む） |
| `in_game/common/prices/00_hardcoded.txt:1101-1104` | 政府タイプ変更コスト（安定度 -50、正統性 -25） |
| `in_game/common/prices/00_hardcoded.txt:64-67` | 政府改革削除コスト（安定度 -20、義 -10） |
| `main_menu/localization/japanese/government_l_japanese.yml` | 権力リソース・継承システムの日本語ローカライズ |
| `main_menu/localization/japanese/government_names_l_japanese.yml` | 政府タイプ名の日本語ローカライズ |
| `main_menu/localization/japanese/game_concepts_l_japanese.yml` | 権力リソースの説明テキスト |
| `main_menu/localization/japanese/actions_l_japanese.yml` | 政府変更アクションのテキスト（15年移行期間等） |

### コミュニティ情報

| 内容 | 出典 |
|------|------|
| 正統性の安定域（50以上）の目安 | EU5 コミュニティ知見（Steam フォーラム・Reddit r/eu5） |
| 共和的伝統の維持目安（50〜70 以上） | EU5 コミュニティ知見 |
| 部族から君主制への移行タイミング | EU5 コミュニティ知見 |
| ステップ遊牧民の結束補充戦略 | EU5 コミュニティ知見 |
| Patch 1.2 変更情報 | 開発日記 Tinto Talks #100〜101（2026-04-08 時点のオープンベータ情報） |
