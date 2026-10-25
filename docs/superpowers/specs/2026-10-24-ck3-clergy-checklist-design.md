# CK3 攻略リセット：聖職者（聖界・神権制）のプレイ中チェックリスト 設計書

- 作成日: 2026-10-24
- 対象: `paradox-game-guides` の CK3 部分のみ（EU5・VIC3 の中身は変更しない）
- 先行事例: VIC3 の同種リセット（`docs/superpowers/specs/2026-10-19-vic3-checklist-reset-design.md`、2026-10-22 公開）と EU5（`docs/superpowers/specs/2026-10-13-eu5-checklist-reset-design.md`）。本書は VIC3 と異なる点を中心に書き、同じ点は VIC3・EU5 の設計書の節を参照する

## 1. 背景と目的

既存の CK3 攻略は、イングランド1066ガイド（約2.7万バイト）・汎用システムガイド（約2.5万バイト）・おすすめMOD記事・用語表で、いずれも 1.19 時点の内容。EU5・VIC3 と同じく、プレイ中に横に置いて「基本は何をするんだっけ」をすぐ引けるチェックリストへ作り直す。

CK3 は政体によって遊び方が大きく変わるため、EU5・VIC3 のような「全勢力共通の1本」ではなく、**政体ごとに1本ずつ**作る。本書はその1本目（聖職者）の設計と、シリーズ全体の決めごとを扱う。

### ユーザーの要件

| 項目 | 決定 | 出どころ |
|---|---|---|
| 方針 | VIC3 と同じ進め方で全面改訂する | ユーザー（2026-10-24） |
| 既存記事 | イングランド1066ガイド・システムガイド・MOD記事の3本とも削除し、チェックリストにする | ユーザー |
| 単位 | 政体ごとに作る | ユーザー |
| 順番 | 最近追加された政体から順に。1本目は聖職者 | ユーザー |
| 1本目の範囲 | キリスト教の聖界に加え、ほかの宗教の神権制（聖職者の領主）も同じ1本に含める | ユーザー |
| 章立て | 本書2章の章立て（段階で区切る案）で進める | ユーザー（案を承認） |
| 目的・使う場面・出典・形式 | VIC3 と同じ（プレイ中に横に置く／数値はスクリプトで裏付けを取り `[src:]` を付ける／チェックを入れられる HTML） | 「VIC3 と同じ」の指示から引き継ぐ |

### 対象パッチ

- **1.20.1 安定版**: `titus_branch.txt` = `release/1.20.1`、`appmanifest_1158310.acf` の `buildid` = **26046173**、`BetaKey` = `public`（2026-10-24 に確認）
- ベータではないので、repo の `CLAUDE.md` の「公開ベータは差分セクション方式」の例外には当たらない。通常どおりインストール版（安定版）を基準にする
- 冒頭の対象パッチ欄は「1.20.1（ビルド 26046173）」と書く
- 作業の最初と最後に `buildid` を確かめる。作業中にホットフィックスで変わったら、`[src:]` の実在確認と数値の裏付けをやり直す

### 前提（ユーザー未確認の仮定）

- 読み手は「CK3 を一通り遊んだが、聖職者プレイは新しい・間が空くと忘れる」レベル。仕組みの解説は最小限にし、行動を中心に書く
- 利用者は本人1人。チェック状態はブラウザ保存（localStorage）で足りる
- **DLC（私の判断）**: インストール済みの DLC（dlc001〜dlc030、By God Alone まで）がすべてある前提で書く。聖界・神権制は By God Alone が無いと操作できない（`common/scripted_rules/00_rules.txt` の `GAME_OVER_CANNOT_PLAY_ECCLESIASTICAL`／`GAME_OVER_CANNOT_PLAY_THEOCRACY`）ので、冒頭に「By God Alone が必要」と1行書く。それ以外の DLC が無いと使えない項目には、行末に「（DLC名 が必要）」と書く（DLC 名は `game/dlc/*/*.dlc` の `name`）

## 2. 構成

### ファイル

| ファイル | 役割 | 状態 |
|---|---|---|
| `ck3/ck3-clergy-play-checklist.md` | 中身の正本（私の判断でこの名前。2本目以降も `ck3/ck3-<政体の英語名>-play-checklist.md`） | 新規 |
| `checklist.html` | 表示用ビューア（EU5・VIC3 と共用） | 既存のまま使う。中身は変えない |
| `scripts/check_checklist.py` | 書式と出典の検証 | 既存を改修（5章） |
| `ck3/localization-reference.md` | 用語の正本 | 既存・残す |

### 対象の政体

| 政体（ゲーム内の名前） | 定義 | 主な違い |
|---|---|---|
| 聖界（`ecclesiastical_government`） | `common/governments/02_theocratic_government_types.txt` | キリスト教のみ。所領なしでも操作できる（`landless_playable = yes`）。財源は宝物庫（`treasury = yes`）。司教・大司教・枢機卿・教皇の階梯がある |
| 神権制（`theocracy_government`） | 同上 | キリスト教以外も含む聖職者の領主の政体（定義のコメントに「信仰の長は可能なら常にこれになる」）。所領あり。聖界との取り分け（どの信仰・どの条件でどちらになるか）は書き手が `can_get_government` と信仰側の定義で確かめる |

両方に共通する手順を本文にし、片方だけの手順には項目の行末に「（聖界のみ）」「（神権制のみ）」と書く。

**比重（ユーザー指示）**: 聖界を中心にし、神権制は全体の3割程度にする。目安は、「（神権制のみ）」の項目と、神権制の視点で書いた共通項目を合わせて、1〜5章の項目数と字数のおよそ3割。各章を書き終えた時点で割合を報告し、大きくずれていたら次の章で調整する。

**付け分けの基準（私の判断）**: 聖界の定義にも `government_is_theocracy` フラグと `mechanic_type = theocracy` が付いている（`02_theocratic_government_types.txt` の `ecclesiastical_government` の `flags`）。そのためフラグ名で「神権制」と判断すると、聖界にも効く項目を神権制だけのものと誤読する。ラベルは次の基準で付ける。

| ラベル | 基準 |
|---|---|
| ラベルなし（共通） | 条件が `government_is_theocracy` フラグや `mechanic_type = theocracy` で、両方に効くもの（例: 後継者の指名 `designate_theocratic_heir_interaction` は `government_has_flag = government_is_theocracy` で判定するので共通） |
| （聖界のみ） | 条件が `has_government = ecclesiastical_government`・`government_is_ecclesiastical` フラグ・キリスト教の信仰・キリスト教会の状況（situation）などで、聖界にしか効かないもの |
| （神権制のみ） | 条件が `has_government = theocracy_government` か、聖界を除く条件で、神権制にしか効かないもの |

レビューでは、各ラベルがこの基準と項目の条件に合っているかを照合する。

**入口の違い**: 開始ブックマークで選べる聖職者は聖界だけ（`00_bookmarks.txt` の `government = ecclesiastical_government` の3人）。神権制は地図から領主を選んで始めるか、途中でなる。1章にこの入口の違いを1項目で書く。また、聖職者を平信徒が務める教義（`doctrine_theocracy_lay_clergy`）を持つ信仰では、神権制になれる者が枢機卿・大司教区の保持者・所領のない聖職者に絞られる（`pam_scripted_triggers.txt` の `theocratic_lay_clergy_trigger`）。神権制の項目は、この教義の有無で挙動が変わらないかを確かめて書く。

### 章立て

CK3 は「何年になったか」より「いまの当主の人生のどの段階か」でやることが変わる。さらに聖職者は独身で世襲しないので、VIC3 のように年で区切らず、聖職者としての段階で区切る。

| 章 | 内容 | チェック | 字数予算（目安） |
|---|---|---|---|
| 冒頭 | 対象パッチ・最終確認日・「By God Alone が必要」・DLC 前提の一文 | — | 200 |
| 1. 開始直後（ポーズ中にやること） | 自分の政体の確認、2人の上位者（宗教上の上位者・世俗の主君）、貸与契約、教会の義務、財源の確認。10項目以内 | あり | 1,600 |
| 2. 聖職者の基盤づくり | 信仰心と精神的充足の維持、個人の教義、主君・上位者との関係、収入の回し方 | あり | 3,000 |
| 3. 位を上げる | 司教 → 大司教 → 枢機卿 → 教皇（教皇候補スコア・枢機卿団）。神権制は聖職称号と信仰の長への道筋 | あり | 3,400 |
| 4. 教会を動かす・後を託す | 勅書、公会議、教会分裂への対応、聖戦の扇動、後を託す準備（自分が死んだあと誰を操作するか。後継者の指名と、継承法ごとの違い: 聖職任命 `clerical_appointment_law`・神権制の選挙 `theocratic_elective_succession_law`・司教の神権継承 `bishop_theocratic_succession_law`） | あり | 3,000 |
| 5. 定期ルーチン `{.routine}` | 毎年／教皇選挙の前／公会議があるとき／戦争の前と後。グループの最終的な分け方は書き手が調べた結果で決めてよい | あり（グループ単位でリセット） | 1,900 |
| 6. 困ったとき | 症状 → 見る場所 → 打ち手（1症状3行） | なし | 2,100 |
| 7. 判断の目安 | 本文の判断に使う数値だけの表。全行に出典 | なし | 1,300 |
| 8. 用語 | このページに出る語のみ。`ck3/localization-reference.md` へリンク | なし | 1,300 |
| 9. 出典 | スクリプトとコミュニティ情報を分けて記載 | なし | 700 |
| 余白 | レビュー反映用 | — | 1,500 |

- 字数予算の合計は20,000字。VIC3 では1〜4章を書き終えた時点で残り約4,300字しか無く、裁定が要った。その反省から、レビュー反映用の余白を最初から1,500字取る。章ごとの予算を超えそうなら、その章を書き終えた時点で報告し、ほかの章から融通するかを決める
- **後を託す準備は必ず入れる（私の判断）**。聖職者は世襲しないので、自分の死後に誰へ操作が移るかでプレイが続くかどうかが決まる。4章の予算に収まらなければ余白から回してよい
- **傀儡（puppet）**: By God Alone の傀儡・傀儡使いの仕組み（`common/puppets/types/pam_puppet_types.txt`、`game_concept_puppet`）を基本の動作に入れるかは、書き手が調べて決める（私の判断）。聖職者プレイで繰り返し使う手段なら2〜4章のどこかに置き、使う場面が限られるなら載せない
- 2〜4章の小見出しの立て方と、上の「内容」欄に挙げた事項の取捨は書き手に任せる。スクリプトと公式の説明を調べた結果、上の段階の分け方が実際の遊び方と合わないと分かったら、章の中身を入れ替えてよい（章番号と「1〜4章は進捗、5章はルーチン、6章以降はチェックなし」の枠組みは変えない）
- `checklist.html` の前提（チェックは1〜5章、進捗バーは1〜4章、`{.routine}`）は EU5 と同じ書式を守ることで満たす

### 載せないもの

- 聖職者以外の政体（封建・氏族・部族・官僚制・冒険者・遊牧・中華圏など）。それぞれ別のチェックリストで扱う
- 特定の人物・地域の攻略の筋道（例: 特定のブックマークの人物で何年までに何をするか）
- 過去パッチとの差分の履歴（1.20.1 の1つだけを書く）
- プレイスタイル別の戦略論、仕組みの長い解説

### 分量の上限（EU5・VIC3 と同じ）

- チェック項目: 100以内（1〜5章の合計）
- 文字数: `[src:]` マーカーを除いた本文で20,000字以内（除去範囲は `\[src:[^\]]*\]`）
- 1項目: 行動1行＋「なぜ」1行まで

## 3. Markdown 書式

EU5 の設計書3章と同じ。冒頭行だけ CK3 用に置き換える。

```markdown
# CK3 プレイ中チェックリスト：聖職者（聖界・神権制）
> 対象パッチ: 1.20.1（ビルド 26046173） ／ 最終確認日: YYYY-MM-DD
```

- 信頼性マーカーは repo の `CLAUDE.md`「信頼性マーカー」節に従う。「（公式の説明）」も EU5・VIC3 と同じ意味で使う。CK3 では用語説明（`game_concept_*_desc`、By God Alone 分は主に `pam_game_concepts.txt` に定義された語）、チュートリアル（`common/tutorial_lessons/`）、助言（`common/important_actions/00_reactive_advice.txt` など）が主な対象
- `[src:]` の書式は repo の `CLAUDE.md` に従い、スクリプトは `ファイル名:行番号` か `ファイル名, 識別子`、ローカライズは `ファイル名, キー` にする
- 訳語は本文に書く前に `game_concept_*` キーで確かめる（確認済みの例: 聖界 = `game_concept_ecclesiastical`、聖職称号 = `game_concept_clerical_title`、司教 = `game_concept_bishop`、大司教 = `game_concept_archbishop`、貸与契約 = `game_concept_lease_contract`、教会の義務 = `game_concept_church_obligations`、キリスト教会 = `game_concept_the_christian_church`。政体名は `ecclesiastical_government` = 「聖界」、`theocracy_government` = 「神権制」）
- 画面名・タブ名・ボタン名は GUI 定義（`gui/*.gui`）とローカライズで確かめる（repo の `CLAUDE.md` の規則）
- **他タイトル・旧版の用語を混ぜない**。CK2 の聖職者プレイや、1.19 以前の CK3 の神権制の仕組みと混同しない

## 4. `checklist.html`

変更しない。CK3 のチェックリストは `checklist.html?file=ck3/ck3-clergy-play-checklist.md` で開く。保存キーはファイルパスごとに分かれる（`checklist:<file>`）ので、EU5・VIC3 や、今後の CK3 の別の政体のチェック状態とは混ざらない。

確かめること: このファイルで開いて、EU5 の設計書4章の HTML 確認項目（再読込でチェックが残る・リセット・出典トグル・幅375px・ダークモード）が通ること。加えて、EU5・VIC3 のチェック状態が CK3 側の操作で消えないこと。

## 5. `scripts/check_checklist.py` の改修

| 変更 | 内容 |
|---|---|
| ゲームの自動選択 | `GAME_DIRS` に `"ck3": Path("C:/Program Files (x86)/Steam/steamapps/common/Crusader Kings III/game")` を足す。選び方（パスの最初のフォルダ名・`--game-dir` 優先・不明なら終了コード2）は変えない |
| 使い方の表示 | 冒頭の docstring と `--help` に CK3 の例を足す |
| テスト | `tests/test_check_checklist.py` に、`ck3/` のパスで CK3 のフォルダが選ばれるケースを足す。既存の `test_select_unknown_folder` は `ck3/` を「未知のフォルダ」の例にしているので、ゲームに対応しない別のフォルダ名（例: `docs/`）に差し替える |

チェック内容は EU5・VIC3 と同じで変えない。`[src:]` の実在確認はファイル名だけで照合するので、CK3 のように同じ名前のファイルが複数のフォルダにある場合（`00_*.txt` など）は「どれか1つにあれば通る」ことに注意する。数値の裏付けは別途レビューで行う。

コミット前に必ず次を通す。

```
python scripts/check_checklist.py ck3/ck3-clergy-play-checklist.md
python -m unittest discover -s tests
```

## 6. 中身の検証

- 書く前に `buildid` と `titus_branch.txt` を確かめ、冒頭に書く
- 数値はすべて 1.20.1 のスクリプトで裏付けを取る。旧ガイド（イングランド・システム）の数値や `[src:]` はそのまま写さない（1.19 時点の値で、`CLAUDE.md` の「前セッションのマーカーも誤りうる」に当たる。さらに旧ガイドは聖職者プレイを扱っていない）
- By God Alone の追加分（`pam_*` のファイル群: `common/decisions/dlc_decisions/pam/`、`common/character_interactions/pam_interactions.txt`、`common/scripted_triggers/pam_scripted_triggers.txt`、`common/game_concepts/pam_game_concepts.txt`、`common/activities/activity_types/ecumenical_council.txt` など）と、神権制の定義（`02_theocratic_government_types.txt`）は特に現物で確かめる
- 「1.20 で新しくなった」という書き方はしない（1章の「載せないもの」のとおり差分の履歴は書かない）。書く必要が出たら、repo の `CLAUDE.md` に従いパッチ履歴で導入パッチを確かめる
- 完成後に3名のレビュー（熟練者・プレイヤー・テクニカルライター）を行う。レビューでは `[src:]` 全件の実在と主要な数値、「（聖界のみ）」「（神権制のみ）」の付け分けが政体の条件と合っているかを照合する

## 7. 削除と付随変更

### 削除

| 対象 | 備考 |
|---|---|
| `ck3/ck3-england-1066-guide.md`、`ck3/ck3-systems-guide.md`、`ck3/ck3-recommended-mods.md` | git 履歴から復元可（ユーザー了承済み 2026-10-24） |
| `docs/superpowers/specs/2026-04-09-ck3-systems-guide-design.md`、`docs/superpowers/plans/2026-04-09-ck3-systems-guide.md` | git 履歴から復元可。VIC3 で国別ガイドの仕様書・計画を消したのと同じ扱い（私の判断） |

`2026-03-31-recommended-mods` の仕様書・計画は3タイトル共通なので残す。`CHANGELOG.md` の過去のエントリは書き換えない。

`_staging/ck3-1.19-factcheck.md`（削除する3本の 1.19 照合メモ。git 管理外のため消すと復元できない）は、ユーザーの了承が無いので残す。了承が出たら削除する。

### 更新

- `index.html`: CK3 セクションのカードを「聖職者（聖界・神権制）のプレイ中チェックリスト（`checklist.html?file=ck3/ck3-clergy-play-checklist.md`）」と「用語対照表（`viewer.html?file=ck3/localization-reference.md`）」にする
- `README.md`: CK3 の表を新しい構成にし、「おすすめMOD」の行を外す。命名例 `ck3/ck3-england-1066-guide.md` をチェックリストの例に差し替える
- `CHANGELOG.md`: リセットのエントリを追加する
- `CLAUDE.md`（repo）
  - 「ファイル構成」に、CK3 も国別ガイドを置かず、政体ごとのチェックリスト（`ck3/ck3-<政体>-play-checklist.md`）であることを書く。「CK3 のファイル名は勢力名＋開始年」の段落は外す
  - 命名例と、テンプレートの模範例の参照（4行目）から `ck3/ck3-england-1066-guide.md` を外す。3タイトルとも国別ガイドが無くなるので、模範例は「git 履歴の `ck3/ck3-england-1066-guide.md`（削除コミットの1つ前）」と書く（私の判断）
  - CK3 の参照先リストに、By God Alone の主なファイル（`pam_*`）と、神権制の定義ファイル、バージョン確認の `titus_branch.txt` を足す
  - `index.html` のカードの例外の記述に、CK3 のチェックリストも `checklist.html?file=...` 形式であることを足す
- `docs/templates/guide-section-template.md`、`docs/procedures/new-country-guide.md`: 模範例の参照を、上の `CLAUDE.md` と同じ書き方に差し替える
- `docs/templates/country-guide-plan-template.md`: 冒頭の注意書きに CK3 も国別ガイドを置かないことを足す
- `ck3/localization-reference.md`: チェックリストで使う語は 1.20.1 のローカライズで確かめ、無ければ足し、ずれていれば直す。それ以外の行はこの作業では見直さない（冒頭の基準バージョン表記はそのまま。全面的な見直しは範囲外）
- 削除後に `grep -rn "ck3-england-1066-guide\|ck3-systems-guide\|ck3-recommended-mods" .` が0件になることを確かめる（`CHANGELOG.md` の過去のエントリ、3タイトル共通の `2026-03-31-recommended-mods` の仕様書・計画、git 履歴として参照する `CLAUDE.md`・テンプレートの模範例の記述、VIC3 の過去の仕様書・計画を除く）

## 8. シリーズの今後（範囲外・記録のみ）

2本目以降は、それぞれ別の設計書で扱う。順番はユーザーの指示（最近追加された政体から）。下の表は DLC の番号順で並べたもので、どのパッチで入ったかは確かめていない。2本目に入る前に、公式 Wiki のパッチ履歴で追加順と、マンダラ・ワヌア・科挙制ハン国がどの DLC のものかを確かめる。

| 順 | 政体（ゲーム内の名前） | 追加した DLC |
|---|---|---|
| 1（本書） | 聖界・神権制 | By God Alone |
| 2 | 天上・律令制・惣領制（中華圏・日本） | All Under Heaven |
| 3 | 遊牧・遊牧集団 | Khans of the Steppe |
| 4 | 官僚制・冒険者 | Roads to Power |
| 5 | 封建制・氏族制・部族制 | 本体 |

## 9. 範囲外

- 聖職者以外の政体のチェックリスト（8章）
- `ck3/localization-reference.md` の全面的な見直し
- 1.20.1 より後のパッチでの再検証
- 複数セーブごとのチェック状態の保持
