# Paradox Game Guides — 作業ルール

> **章構成テンプレートの正本は `docs/templates/guide-section-template.md`。** 新規国別ガイド追加の定型手順は `docs/procedures/new-country-guide.md`。このファイルにはルール・制約・スクリプト参照先のみを置く。
> テンプレート適用の模範例: `eu5/eu5-hungary-guide.md`、`eu5/eu5-ottoman-guide.md`

## 対象ゲームと優先度

1. **Europa Universalis V**（EU5）— 最優先
2. **Victoria 3**（VIC3）
3. **Crusader Kings III**（CK3）

---

## ファイル構成

```
{タイトル略称}/
  {タイトル略称}-{国家名}-guide.md   … 攻略ガイド本体
  localization-reference.md           … ローカライズ対照表（ゲームごとに1つ）
```

命名例: `eu5/eu5-brandenburg-guide.md`, `ck3/ck3-england-1066-guide.md`, `vic3/vic3-prussia-guide.md`

CK3 のプレイ単位はキャラクター/王朝だが、ファイル名は「操作する主要勢力名」で統一する。CK3 は同じ勢力でも開始年で状況が大きく異なるため、**開始年をファイル名に含める**（例: `ck3-england-1066-guide.md`）。

---

## ゲーム横断テンプレート（分離済み）

全13セクションの章構成・順序柔軟性・省略ルール・各セクションの書式は `docs/templates/guide-section-template.md` が正本。ガイド執筆・改稿の前に必ず読む。

---

## 情報ソースと優先順位

| 優先度 | ソース | 用途 |
|--------|--------|------|
| 1（最優先） | ゲームスクリプト | 条件、数値、イベント発火ロジックの根拠 |
| 2 | ゲーム内日本語ローカライズ | 用語の正式名称 |
| 3 | 公式 Wiki（*.paradoxwikis.com） | 概要、メカニクス解説 |
| 4 | コミュニティ情報（Steam, Reddit, 攻略サイト） | プレイ報告、体感ベースの知見 |

---

## ゲームスクリプト参照先

### 共通パス

```
Steam デフォルト: C:\Program Files (x86)\Steam\steamapps\common\
ユーザーデータ: C:\Users\ramda\OneDrive\ドキュメント\Paradox Interactive\
```

### EU5

```
ゲーム本体: Europa Universalis V\game\
  in_game/common/advances/                        … 固有進歩の定義
  in_game/events/DHE/                             … 固有イベントのスクリプト
  in_game/common/building_types/                  … 建造物の定義
  in_game/common/casus_belli/                     … 開戦事由の定義
  in_game/common/international_organizations/     … HRE / Catholic Church / 各種IO（皇帝メカニクス・Papal Authority 等）
  in_game/common/parliament_types/                … Imperial Diet 4段階等の議会タイプ定義
  in_game/common/unit_categories/                 … 兵科分類（Light/Heavy 歩兵・騎兵・砲兵）。is_garrison 等のフラグ
  in_game/common/prices/                          … 列聖・破門等の固定コスト（00_hardcoded.txt, 03_diplomacy.txt）
  loading_screen/common/defines/00_defines.txt    … 各種数値定数（NDynasty / NColony 等のブロック）

日本語ローカライズ:
  main_menu/localization/japanese/              … UI用語
  main_menu/localization/japanese/events/DHE/   … イベントテキスト
```

### CK3

```
ゲーム本体: Crusader Kings III\game\
  common/traits/                 … キャラクター特性
  common/lifestyles/             … ライフスタイル定義
  common/lifestyle_perks/        … パーク定義
  common/culture/innovations/    … 文化イノベーション
  common/decisions/              … ディシジョン定義
  events/                        … イベントスクリプト（30+サブディレクトリ）

日本語ローカライズ:
  localization/japanese/          … 全ローカライズ（1164ファイル）
```

### VIC3

```
ゲーム本体: Victoria 3\game\
  common/technology/technologies/ … Era別技術定義（20_military.txt 等）
  common/interest_groups/        … 利益団体定義
  common/interest_group_traits/  … IGトレイト定義（普代/外様等の効果値）
  common/laws/                   … 法律定義（00_distribution_of_power.txt に law_bakufu 等）
  common/journal_entries/        … JE定義（00_meiji_restoration.txt / 00_german_unification.txt 等。完了条件の正本）
  common/country_formation/      … 建国可能タグ要件（GER/NGF/SGF 等）
  common/power_bloc_identities/  … パワーブロックのidentity（ツォルフェライン=identity_trade_league 等）
  common/static_modifiers/       … modifier効果値（00_ep2_04/05/06_modifiers.txt に日本/独統一系）
  common/character_templates/    … 国別キャラ（country_jap.txt / country_pru.txt。characters/ ではない）
  common/diplomatic_plays/ , common/diplomatic_actions/ , common/scripted_rules/ … 外交プレイ/アクション/砲撃外交ルール
  events/                        … イベントスクリプト

バージョン確認: ルート直下 `caligula_branch.txt`（例 release/1.13.8）/ `clausewitz_branch.txt`

日本語ローカライズ:
  localization/japanese/          … 全ローカライズ。ステータス訳語は concept_*（concept_authority="権力" 等）
```

---

## スクリプト参照時のルール

- 数値や条件を記載する場合、出典として**ファイル名:行番号**を明記する
- ローカライズファイルで正式な日本語名を確認してから記載する
- **ガイドを書き直す/パッチ更新するときは、検証基準を「インストール版」に固定する**（公開ベータの最新パッチを追わない）。プレイヤーが実際に遊ぶ版＝スクリプト最優先ソースであり、版ズレ検証は無意味。VIC3 は `caligula_branch.txt`、EU5/CK3 も同様のブランチファイルで版を確認する。実例（2026-06-01 VIC3 日本/プロイセン書き直し）: インストール版 1.13.8 を基準に固定
- **スクリプトに実値が無い数値（エンジン内部 defines）の「パッチ変更か否か」は、新旧2バージョンのパッチノート突き合わせで確定する**。EU5 の経済目玉値（船コスト倍率・利益率・建物維持費逓増・mills_employment・陸軍goods需要・正規兵vs徴募兵ダメボ等）は `building_types/` `prices/` `goods_demand/` `loading_screen/common/defines/00_defines.txt` を全走査しても実値が無く、C++側エンジン値のためスクリプト検証も版間 diff も不可。この場合「対象パッチのノートに変更が明記され、かつ旧バージョンのノートに同項目が無い」ことを確認すれば真正な変更と確定でき、`（コミュニティ知見：x.y、公式パッチノート由来・スクリプト未確認）` 出典で記載してよい。実例（2026-06-16 EU5 1.3 beta 更新案）: 「Prikazi/Collegium 0.15/0.20→0.10」「船コスト4x金/10x goods」等を1.2ノート未記載＋1.3ノート明記で1.3真正変更と確定。逆に「兵科Heavy/Light分割は1.2／個別ユニット(ジェノヴァ弩兵等)の再分類は1.3」「Infiltrate Administrationは1.2既存／spy網fog解除は1.3新規」のように、似た機能の導入時期をノート差分で切り分けることで過剰反映を防げる
- **公開ベータ（open beta）への対応は「純追記・差分セクション」方式を採る**。「インストール版固定」ルールは"本体章の書き換え禁止"の趣旨であり、専用の差分セクションを純追記する（①本体章を一切変更しない ②beta起源の数値を本文に昇格させない ③安定版リリース後に昇格フローで本文統合）ならルール趣旨と両立する。新マーカーは単体使用せず既存体系に重ねる（`[src:...]（x.y beta・変動注意）` / `（コミュニティ知見：x.y beta）`）。公開ガイドの読者多数派は安定版でプレイしている点に留意し、安定版(=live)を baseline として維持する。実例（2026-06-16 EU5 1.3 open beta）: 案A確定、spec `docs/superpowers/specs/2026-06-16-eu5-patch13-update-design.md`
- **前セッションの `[src:]` マーカーも誤りうる前提で、書き直し時は全数値を再検証する**。実例（同セッション）: 既存 [src:] 付きでも `law_free_ports`（実在せず→law_mercantilism）・`force_recognition`（CB 不在）・law_bakufu の所在ファイル誤り・岩倉社会技術 +0.25%→実値+1%・「プロミネンス+5」→実は magnate_leader_weight、と複数の実誤りが発覚。特に「[src:] がローカライズ yml を指しているだけでメカニクス未検証」のケースに注意（yml は名称の裏取りであって効果値の裏取りではない）
- **ステータス（Authority/Prestige 等）の訳語は本文に書く前に `concept_*` ローカライズキーで確認する**。実例（同セッション）: VIC3 の Authority はゲーム内 `concept_authority = "権力"`。「権威」は誤訳で、IGトレイト表だけ「権威」になり同一ガイド内で訳語分裂していた。ステータス名は1ガイド内で必ず統一する
- **イベント/JE の「ID 未確認（—）」を放置せず、不在なら「スクリプト上に存在しない」と確定まで詰める**。実例（同セッション）: VIC3 プロイセンの「ツォルフェライン拡大イベント」「ビスマルク社会立法イベント」は events/ 全走査で不在＝未実装と確定し、「拡大は外交・社会立法は法律改正で行う」と代替手段を明示した
- **他タイトルの用語を混ぜない**（EU4 用語を EU5 に使う、CK2 用語を CK3 に使う等は禁止）
- パッチで変動しうる数値には、冒頭のパッチ版で一括免責する
- **EU5 スクリプトファイルは BOM 付きが多く、`grep -cE "^[a-zA-Z_]+ = \{"` 等の行頭アンカー検索は先頭1件を見落とす**。件数の断定（「全N件」）をガイドに書く前に `sed 's/^\xEF\xBB\xBF//' file.txt | grep -c ...` で BOM を剥がしてから数える。実例（2026-07-12 EU5 1.3 フェーズ3）: `country_bra.txt`/`country_pru.txt` の先頭進歩（`expansive_policies`/`teutonic_legacy`）が BOM のため grep に掛からず、ガイド本文の「全24件（BRA12・PRU12）」が実際は「全26件（BRA13・PRU13）」だった。reviewer も同じ見落としをした
- **本文中の `[src: ...]` が指すファイル名は、Read/grep で実在確認してからコミットする**。実例（2026-07-12 EU5 1.3 フェーズ3）: austria ガイドに `hab-advances.md`/`hab-hre-mechanics.md`/`hab-union-mechanics.md`/`hab-events-part1/2.md` という、ゲーム内にもリポジトリ内にも存在しないファイル名を指す出典が31箇所混入していた（過去セッションの internal staging ファイル名が本文に残留したとみられる）。値自体は概ね正確だったため実害は限定的だったが、信頼性マーカーの根幹に関わる欠陥だった。reviewer 委任のチェック観点に「`[src:]` のファイル名が実在するか」を毎回含める

---

## 信頼性マーカー

ガイド本文中で情報の信頼性を明示する。出典セクションでの分離と併用する。

### 本文中のマーカー

スクリプト出典はフルパスだと可読性が下がるため、**ショートマーカー + 出典セクションで詳細**の二層方式を採用する。

| マーカー | 意味 | 使い方 |
|---------|------|--------|
| `[src: ファイル名:行番号]` | スクリプト確認済み | 数値・条件。短いファイル名で本文に埋め込む |
| `（コミュニティ知見）` | プレイ報告ベース | 体感・戦略論・タイミング推奨 |
| `（未検証）` | 情報源不明 or 裏取り未了 | 暫定記載。検証後にマーカーを変更 |

例: 「騎兵戦力 +20% `[src: country_HUN.txt, hun_composite_light_cavalry]`」
- ファイル名 + スクリプト内識別子（変数名 or イベントID）を併記する
- 行番号はパッチで変わるため、**識別子を優先**し行番号は補助情報とする

### ルール

- **数値**は必ず出典を付ける
- **イベント推奨選択**はスクリプト確認済みの効果とコミュニティ知見（どちらを選ぶべきか）を区別する
- **`（未検証）`** のまま放置しない。検証できなければ「コミュニティ知見」に格下げするか削除する
- 出典セクションでも一次情報とコミュニティ情報を分離する
- **URL を本文の `[src:]` に直接埋め込まない**。`[src: Patch_X.Y wiki]` のショートマーカーで本文に置き、URL は末尾の出典セクションに集約する
- **新パッチ対応で wiki パッチノート1点しか出典がない記述は断定で書かない**。「コミュニティ知見：...はスクリプト未確認」を併記し、後日検証する余地を残す（議論エージェントの批判派指摘で必ず引っかかるため）
- **wiki 由来の数値は最低でも 1 つはスクリプト検証して整合性をチェックする**。実例（2026-05-10、EU5 1.2 検証）: wiki ベースで「Light Cavalry 移動速度 7.00」と記載していたが、`unit_categories/02_army_light_cavalry.txt` の実値は `movement_speed = 3.0`。wiki だけを信じると誤値が混入する
- **`script verified` マーカーは「行内の特定クレーム」単位で付ける**。1行内に「verified な事実 + 未確認な閾値・数値」が混在する場合は行を分割する。同一行に `[src: ... + script verified]` と `（コミュニティ知見：閾値ボーナスの具体値はスクリプト未確認）` を併記すると批判派指摘で必ず矛盾扱いになる
- **ガイド末尾の一括免責文と本文中の個別 `script verified` を整合させる**。「1.2 はすべてスクリプト未確認、wiki ベース」と末尾に書いた状態で本文に `script verified` が混在すると矛盾になる。末尾免責は「verified 済み項目」と「コミュニティ知見項目」を分けて書く
- **マーカー昇格時、パッチ差分テーブルだけでなく本文セクション内の同一クレーム再掲箇所も同時に昇格する**。1次バッチでテーブルだけ verified 化して本文セクションを放置すると、2nd レビューで「同一ファイル内 verified vs 未確認」整合性指摘が高頻度発生する。実例（2026-05-16 EU5 1.2 追加検証）: castile-guide 行 50/52-53 はテーブルで verified なのに行 363/375 の本文セクションで「スクリプト未確認」残存、hungary-guide 行 23/58 で Restore Roman Borders CB が verified と未確認に分裂。implementer 委任時に「該当クレームの全出現箇所を漏れなく昇格」と明示する
- **総括ブロック（複数クレームを1行に詰めた表現）は最初から行内分割する**。「1.2 更新: A、B、C、D、E `[src: ...]`」のような一括マーカー行は、サブエージェントレビューで必ず「クレーム単位の verified 状態が判別不能」指摘になる。最初から各クレームを別行・別マーカーで書く（regional-guide の旧行 136 の総括ブロック → 6行分割で解決した実例）
- **`scales_with multiply = N` ブロックを伴う auto_modifiers の効果値は「スケール変数が最大値（通常 100）の時の値」であり「1 ポイントあたり」ではない**。線形スケールするため、表ヘッダに「X 100（最大）時の値」と明記する。実例（2026-05-16 EU5 universal-guide Complacency 修正）: `scales_with = { value = complacency multiply = 0.01 }` により列挙効果は慢心値 × 0.01 で線形適用。「1 ポイントあたり -50%」と記載すると 2 ポイントで -100% という誤読を生む
- **「wiki 数値が誤りそう」と思ったら、まず stat 名そのものを script で grep する**。同名でも別 stat の可能性がある。実例（2026-05-16 EU5 Cavalry 二重確認）: 「Light Cavalry 移動速度 3.0」を疑って検証したら、`movement_speed`（戦略マップ移動）は実値 3.0 で正しく、別 stat の `combat_speed`（戦闘内速度）= 5 と混同しかけた。`grep -E "movement_speed|combat_speed"` のように全候補 stat を列挙して同定する
- **EU5 ユニット定義の `impact` と `combat` は意味が異なる**。`impact = { terrain = -0.X }` は進軍コスト減（=移動しやすい、戦闘ボーナスではない）、`combat = { terrain = +0.X }` のみ戦闘力修正。両者を script verify する際に混同しない。実例（2026-05-16 EU5 ハンガリー軍事章）: ハンガリー・フサールの `impact = { flatland = -0.25 mountains = -0.25 }` を「平地・山岳での戦闘ボーナス」と誤読しかけたが、`impact` は進軍コスト系で戦闘ボーナスではない
- **「固有ユニット」と書く前に解禁経路の advance ファイルを確認する**。ユニット定義（`unit_types/`）が国固有でも、解禁する advance が**地域 advance**（`advances/region_*.txt`）にある場合は複数文化グループで取得可能。`country_XXX.txt` 経由か `region_XXX.txt` 経由かで「固有」「地域共有」が分かれる。実例（2026-05-16 EU5 ハイドゥク検証）: `a_hajduk` 自体に HUN 専用フラグはなく、`balkan_hajduks` 地域 advance（バルカン・カルパティア圏首都が条件、POL・SER・ワラキア等も対象）経由で解禁される。「ハンガリー固有」と書くと不正確
- **EU4 派生メカニクスが EU5 ガイドに混入していないか定期的に横断スキャンする**。同じ "Paradox grand strategy" 感覚で書くと EU4 固有のシステムが残る。実例（2026-05-17 EU5 ハンガリーガイド）: ①「諜報→請求権捏造（fabricate_claim）」を 1.2 で前提に書いていたが、EU5 には `spy_actions/` ディレクトリ自体が存在せず、`scripted_relations/` のスパイ網にも Claim 付与効果なし。②「ライバル設定で Claims on Province の CB を確保しやすい」と書いていたが、EU5 の `cb_conquer_province` 条件は `is_core_of = root`（コア取得後）であり、ライバルだけでは確保不可。ライバル相手は `cb_conquer_enemy`（コア不要）が正しい。新規ガイド執筆時・パッチ更新時の用語チェックに `fabricate_claim`, `forge_claim`, `spy_network`, `Claim 捏造`, `領有権主張を捏造` のキーワード grep を含める
- **EU5 の市場（Market）は首都ではなく特定 location の `is_market_center` フラグで設定される**。「首都に市場を建てる」は EU4 由来の感覚で、EU5 では市場系建造物（Entrepot/Trading Hub）が `location_potential = { is_market_center = yes }` を要求する。実例（2026-05-17 EU5 ハンガリー）: HUN の首都ブダ（wine 産地）ではなく隣接のペスト（wheat 穀倉地）が市場中心。`location_templates.txt` の `raw_material` だけでは判別できないので、ユーザー報告か内部 binary（`nodes.dat`）の参照で確認する。`location_ranks/00_default.txt` の `megalopolis allow` 句に `is_market_center = yes` 必須条件あり
- **属国スタートの直接定義ファイルは EU5 に無い**。EU4 の `history/countries/` 相当が存在せず、属国関係は flavor イベントの `is_subject_of = c:XXX` トリガーから間接確認するしかない。実例（2026-05-17 ボスニア検証）: BOS の HUN 属国は `events/DHE/flavor_BOS.txt:28` の `is_subject_of = c:HUN` トリガーで確認。新規ガイドで開始時属国関係を書く場合、`grep "is_subject_of = c:<TAG>" events/DHE/flavor_*.txt` で間接確認する。`setup/countries/*.txt` には liege/subject_of フィールドは無い
- **メイン側でユーザー指摘の「他にも似た誤謬がありそう」を受けたら、まず researcher で横断 grep してから implementer 委任する**。実例（2026-05-17 EU5 1.2 メカニクスドリフト調査）: ユーザー指摘 2 件（ボスニア属国・請求権捏造）から researcher が staging ファイルに ①該当行番号 + ②現行 EU5 ルート + ③推奨修正 をまとめ、メイン側で Edit ツール 3 箇所適用。「指摘点だけ修正」より波及効果が大きいため、サブエージェント1回で他の EU4 派生表記（AE/Coalition/Trade Node/Idea Group/Tariff/Liberty Desire 等）を一括スキャンする方が効率良い

---

## ガイド章追加時のチェックリスト

新章・新セクションを追加するとき、以下を**同じコミット内で**完了させる:

1. 本文に新用語が登場したら、ガイド末尾の用語対照表に追加（事後追加は議論エージェント指摘で必ず手戻りになる）
2. 出典セクションに新規参照URL・スクリプトファイルを追記
3. パッチ差分テーブルに章追加の根拠となるパッチ変更を記載（パッチ対応の場合）
4. CHANGELOG.md にエントリ追加

---

## バージョン管理

### パッチ更新フロー

1. 新パッチがリリースされたら、対象ゲームの攻略ガイドを確認
2. パッチ差分セクションを更新
3. 変更された数値・メカニクスをガイド本文で修正
4. ローカライズ対照表の用語変更がないか確認
5. 冒頭のパッチ版と確認日を更新

### 最新バージョン確認の手順

ガイド作成・更新時は以下の順で最新パッチを確認する:

1. **公式 Wiki のパッチ一覧ページ** — 最も信頼性が高い
   - EU5: `eu5.paradoxwikis.com/Patches`
   - CK3: `ck3.paradoxwikis.com/Patches`
   - VIC3: `vic3.paradoxwikis.com/Patches`
2. **SteamDB のパッチノート** — 細かい Hotfix も追跡
3. **ゲーム内のバージョン表示** — 起動画面右下

---

## 用語ルール

- 日本語は**ゲーム内ローカライズ準拠**。未翻訳の箇所は英語を併記する
- **各ゲームの `localization-reference.md` がローカライズの正本**
- 初出時に「日本語名（English Name）」の形式で英語を併記する
- 略語（HRE、CB、IG 等）は初出で展開する
- 用語対照表をガイド末尾に必ず置き、完全版への参照リンクを含める
- **他タイトルの訳語を流用しない**（同じ英語でもゲームごとにローカライズが異なることがある）
- **行内マーカー（パッチ重大度・破壊的変更等）は「文脈別ルール」で統一する**。表セル・箇条書きでは括弧＋太字（例: `（**破壊的変更**）`）、見出しと地の文では裸の語、と使い分ける。全箇所同形式に統一しようとすると地の文が不自然になる。実例（2026-05-16 EU5 「破壊的変更」表記統一）: 6 箇所のうち 3 箇所を `（**破壊的変更**）` に統一、見出し 2 箇所と地の文 1 箇所はそのまま

---

## ローカライズ対照表の管理

- ゲームごとに `{タイトル略称}/localization-reference.md` を1つ作成
- 新しい用語を追加する場合、**必ずゲーム内ローカライズファイルで確認**してから追加
- 各ガイドの用語対照表は対照表から該当分を抜粋し、完全版へのリンクを付ける
- パッチ更新時にローカライズ変更がないか確認する

---

## レビュー

- 完成後に 3 名のレビュワーで確認する
  - **熟練者**: 戦略の正確性、パッチ対応、抜け漏れ
  - **プレイヤー（中級者想定）**: 用語の正確性、ゲーム内表記との一致
  - **テクニカルライター**: 構成統一、表記揺れ、保守性
- レビュー結果は別ファイルに残さず、ガイド本体に反映して完了とする

---

## 新規国別ガイド追加の手順（分離済み）

ファイル探索→Plan生成→調査→執筆→付随更新4点セットの定型フローは `docs/procedures/new-country-guide.md` が正本。新規ガイド着手前に必ず読む（ブレスト・Spec が必要になる例外ケースも同書に記載）。

---

## エージェント作業ルール

- ガイドのリバイズ（構造変更）は sed/Edit の差分編集を優先し、全書き直しは最終手段にする（トークン節約）
- 全書き直しが必要な場合は、事前に変更前後のセクション見出し比較表をユーザーに提示してから着手する
- **ガイド追加時は `index.html` にカードを追加する**（ゲームセクション内の `card-list` に `<li>` を追加、リンクは `viewer.html?file=パス` 形式）
- **ローカライズ対照表の拡充をエージェントに委任するときはカテゴリを3つ以下に分割する**（全カテゴリ一括は走査ファイル数が多すぎてタイムアウトする）
- **ガイド本体の用語対照表更新と中央 `localization-reference.md` 更新は別タスク**。implementer は本体側を更新するが、中央対照表はメイン側で確認すべき。新規追加用語のうち「他ガイドでも使う可能性のある汎用語（HRE 系・PU 系・CB 系・兵科系）」だけを中央に転載し、勢力固有用語（黒軍・フサール等）は本体のみで完結させる
- **implementer 3 並列で staging ファイル直書きさせるとき、各 implementer に「ガイド末尾セクション（用語対照表・出典）を独自に書かない」を明示する**。Section 担当の implementer が各自「Section 内で使った用語の小規模対照表」「Section 内で参照したファイルの小規模出典」を staging に含めると、メインで結合した時に本文中に重複セクションが残る。実例（2026-05-17 VIC3 日本ガイド執筆）: Section A 担当 implementer が「Section A で使用した用語」と限定タイトルで `## 用語対照表` `## 出典` を末尾に書き、結合後に本文中央に重複セクションが残った（sed で 56 行削除して対応）。指示テンプレートに「用語対照表・出典は Section C 担当の implementer のみが書く。他の Section 担当は本文中の `[src: ...]` インライン出典のみ」と明記する
- **新規ガイドのコミット境界は plan に従わず staging 経由で 1 コミットに統合してよい**。plan では「海軍以外の本体執筆」と「海軍ドクトリン執筆」を別コミット境界としていたが、staging 経由で組み立てる方式では一度の結合で全体が完成するため、別コミットの利得が乏しい。実例（同セッション）: Task 4 + Task 5 を「本体執筆」1 コミットに統合した方が履歴が読みやすい。サブエージェント並列で staging に書かせる場合、各 staging の結合タイミングをコミット境界に揃える運用が現実的
- **複数ガイドを同一セッションで並列統合するとき、ガイド間の相互参照は Wave 分割で解決する**。他ガイドの記述を参照しない自己完結組を先行実施（Wave1）し、そこで確定した見出し名を、他ガイドを参照する組（Wave2）への implementer 指示に反映する。同一 batch で相互参照するガイドを同時に投入すると、参照先の見出し名がまだ確定していない状態でリンクを書くことになりリンク切れが残る。実例（2026-07-11 EU5 1.3 安定版昇格 Task1-3）: byzantium⇄ottoman・austria⇄brandenburg の相互参照を Wave1（byzantium/austria/hungary=自己完結組）→Wave2（ottoman/brandenburg/castile=参照組）に分けて解決。逆方向（Wave1 完了前から存在した regional 側の byzantium 参照等）は Wave1 完了後に別途張り直しが必要になる点も見込んでおく
- **大規模計画書は改訂を重ねるとタスクリストと、レビュー反映済みの実行ガイド（セッション分割メモ等）が矛盾することがある。着手前にタスク番号だけでなく周辺の詳細な運用メモも突き合わせる**。実例（2026-07-11 EU5 1.3 安定版昇格 Task1-2）: 計画書のタスク定義は「Task 1-2 = regional + byzantium」だったが、同計画書内のレビュー反映済みセッション分割ガイド（「regional 単独で1セッション・byzantium と同居させない」という具体的根拠付きの記述）と矛盾していた。より具体的な根拠を持つ後者を優先し、タスク番号を実運用に合わせて計画書側を修正した
