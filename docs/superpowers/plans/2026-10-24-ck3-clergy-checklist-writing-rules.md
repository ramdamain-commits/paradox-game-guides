# CK3 聖職者チェックリスト 執筆タスク共通の手順と合格基準

実装計画 `2026-10-24-ck3-clergy-checklist.md` の Task 3〜6（中身の執筆）に共通する手順。**各タスクの指示書と一緒に必ず渡す**（計画の Task 節だけを抜き出すと、この内容が漏れるため別ファイルにしてある）。

`G` = `C:/Program Files (x86)/Steam/steamapps/common/Crusader Kings III/game`

## 0. 着手前（毎タスク）

```bash
grep -E '"buildid"|BetaKey' "/c/Program Files (x86)/Steam/steamapps/appmanifest_1158310.acf"; cat "/c/Program Files (x86)/Steam/steamapps/common/Crusader Kings III/titus_branch.txt"
```

`buildid` が `26046173`、`titus_branch.txt` が `release/1.20.1` であること。変わっていたら作業を止め、コントローラーに報告する（既存の `[src:]` 行番号と数値の照合をやり直す必要があるため）。

## 1. 一次情報の当たり先

| 何を知りたいか | 見る場所 |
|---|---|
| 政体の定義と取り分け | `G/common/governments/02_theocratic_government_types.txt`、`G/common/scripted_triggers/pam_scripted_triggers.txt`（`theocratic_lay_clergy_trigger` ほか）、`G/common/scripted_rules/00_rules.txt` |
| By God Alone の行動 | `G/common/decisions/dlc_decisions/pam/`、`G/common/character_interactions/pam_interactions.txt`、`G/common/important_actions/pam_actions.txt`、`G/common/activities/activity_types/ecumenical_council.txt`・`pam_investiture_council.txt`、`G/common/situation/`（キリスト教会の状況）、`G/common/puppets/types/pam_puppet_types.txt` |
| 後継 | `G/common/laws/00_succession_laws.txt`（`clerical_appointment_law`・`theocratic_elective_succession_law`・`bishop_theocratic_succession_law`）、`G/common/succession_appointment/`、`designate_theocratic_heir_interaction` |
| 公式が教える手順・注意 | `G/common/important_actions/`（助言。`00_reactive_advice.txt` ほか）、`G/common/tutorial_lessons/`、`G/localization/japanese/tutorial/` |
| 用語の公式説明 | `G/common/game_concepts/pam_game_concepts.txt` と `G/localization/japanese/dlc/pam/pam_game_concepts_l_japanese.yml`（`game_concept_*`・`game_concept_*_desc`）、`G/localization/japanese/game_concepts_l_japanese.yml` |
| 補正値・定数 | `G/common/script_values/`、`G/common/modifiers/`、`G/common/defines/00_defines.txt`、政体定義の `character_modifier` |
| 画面名・ボタン名 | `G/gui/*.gui` のラベルキーとローカライズ |
| DLC 判定 | `has_dlc_feature` を含む条件と `G/common/scripted_triggers/00_has_dlc_scripted_triggers.txt`。DLC 名は `G/dlc/*/*.dlc` の `name` |
| 正式な日本語名 | `G/localization/japanese/` と `ck3/localization-reference.md` |
| コミュニティの定石 | `ck3.paradoxwikis.com`（数値は必ずスクリプトで1件以上照合する。By God Alone 以前の記述や旧版の神権制の記述であることが多い） |

## 2. 書き方

1. 候補の行動を一次情報から洗い出し、「聖界か神権制のプレイヤーが繰り返し、またはその段階で必ずやることか」で絞る。特定の人物・地域・ブックマークに固有の筋道は載せない
2. 行動文は「〈画面や対象〉で〈操作〉する」「〈状態〉を確認する」の形で、動詞で終える。1行に1つの行動
3. 「なぜ」は判断の根拠を1行で書く。スクリプトが根拠なら `[src: ファイル名:行番号]` か `[src: ファイル名, 識別子]` を付ける。ゲーム内の助言・チュートリアル・用語説明だけが根拠なら、「（公式の説明）」を付けたうえで `[src:]` も付ける。プレイ報告が根拠なら `（コミュニティ知見）` を付ける
4. **`[src:]` のファイル名が `G` の中に2つ以上あるとき**（`find "$G" -name <名前> | wc -l` が2以上）は、`common/laws/00_x.txt:120` のように `G` からの相対パスで書く。検証スクリプトはファイル名しか照合しないので、パスがないと別のファイルを指していても通ってしまう
5. 数値を書いたら、判断の目安になる数値だけを7章の表にも同じ値で載せる
6. 用語は書く前に `game_concept_*` キーで正式な訳を確かめる。本文は日本語名だけにし、英語名は8章に「日本語名（English）」の形で集める
7. **ラベルの付け分け**（設計書2章の表）: 項目の根拠の条件を開き、`government_is_theocracy` フラグや `mechanic_type = theocracy` で判定しているならラベルなし（共通）、`has_government = ecclesiastical_government`・`government_is_ecclesiastical`・キリスト教・キリスト教会の状況が条件なら「（聖界のみ）」、`has_government = theocracy_government` か聖界を除く条件なら「（神権制のみ）」。名前に theocratic と付いているだけで「（神権制のみ）」にしない。付けた根拠の条件は報告に書く
8. **比重**: 聖界中心、神権制は全体の3割程度（設計書2章）。「（神権制のみ）」の項目と、神権制の視点で書いた共通項目の数・字数をタスクごとに報告に書く
9. **DLC が要る項目**: By God Alone は冒頭で前提にしているので印を付けない。それ以外の DLC の `has_dlc_feature` が条件にあるときは、行動の行末に「（DLC名 が必要）」と書く
10. 他タイトル・旧版の語を混ぜない。書いたあとに次のコマンドで0件を確かめる: `grep -nE '安定度|ダカット|交易ノード|列強|利益団体|正統性|諜報網|Coalition|Aggressive Expansion' ck3/ck3-clergy-play-checklist.md`（「正統性」は CK3 にもある語なので、ヒットしたら `game_concept_legitimacy` の訳と一致するかを確かめ、一致すれば残してよい）
11. 新しく使ったスクリプトファイルは、9章「一次情報」に `G` からの相対パスで追記する。wiki の URL は9章「コミュニティ情報」に書く（本文の `[src:]` に URL は入れない）
12. 旧ガイド（イングランド・システム）は聖職者プレイを扱っていないうえ 1.19 時点の内容。読むなら `git show main:ck3/ck3-systems-guide.md` 等で発想のもととしてだけ使い、数値・`[src:]`・訳語は写さない

## 3. 合格基準（各タスクの最後に確かめ、報告に書く）

- `python scripts/check_checklist.py ck3/ck3-clergy-play-checklist.md` が `OK` を返す
- そのタスクの章の項目数と字数が予算以内に収まっている（字数は `[src:]` を除いて章ごとに数える。数え方は計画の Global Constraints）
- タスクで書いた数値ごとに「数値 → 確かめたファイル:行 → 実際の値」の対応表を報告に書いてある。`[src:]` が yml（名称）しか指していない数値は、効果値の裏付けになっていないので不合格
- ラベルを付けた項目ごとに「項目 id → ラベル → 根拠の条件（ファイル:行）」の一覧を報告に書いてある
- 神権制の比重（項目数・字数）を報告に書いてある
- 2章10の grep が0件（または「正統性」が正式訳と一致）
- DLC が要る項目に印が付いている。その項目の一覧を報告に書く

## 4. VIC3 のレビューで分かったこと（同じ誤りを避ける）

- 画面名・タブ名・ボタン名は `G/gui/*.gui` のラベルキーとローカライズで確かめる。チュートリアルや助言の言い回しをそのまま画面名にしない
- 用語説明を言い換えるときに、スクリプトと食い違う一般化をしない（段階ごとの効果は段階で書く）
- 1つの主張に1つの `[src:]` を付ける。7章に載せたからといって本文の出典を省かない
- 助言の区分は、スクリプトの種類で書く。色の印象で書かない
- 訳語はローカライズのとおりにする
- コミット末尾は `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` に固定する（実行モデルに合わせて変えない）
