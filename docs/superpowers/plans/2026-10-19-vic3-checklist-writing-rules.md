# VIC3 チェックリスト 執筆タスク共通の手順と合格基準

実装計画 `2026-10-19-vic3-checklist-reset.md` の Task 3〜6（中身の執筆）に共通する手順。**各タスクの指示書と一緒に必ず渡す**（計画の Task 節だけを抜き出すと、この内容が漏れるため別ファイルにしてある）。

`G` = `C:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game`

## 0. 着手前（毎タスク）

```bash
grep -E '"buildid"|BetaKey' "/c/Program Files (x86)/Steam/steamapps/appmanifest_529340.acf"; cat "/c/Program Files (x86)/Steam/steamapps/common/Victoria 3/caligula_branch.txt"
```

`buildid` が `25629520`、`caligula_branch.txt` が `release/1.14.5` であること。変わっていたら作業を止め、コントローラーに報告する（既存の `[src:]` 行番号と数値の照合をやり直す必要があるため）。

## 1. 一次情報の当たり先

| 何を知りたいか | 見る場所 |
|---|---|
| 公式が教える手順・順序 | `G/common/tutorial_lessons/`、`G/common/tutorial_lesson_chains/`、`G/localization/japanese/tutorial_l_japanese.yml` |
| 用語の公式説明 | `G/localization/japanese/concepts_l_japanese.yml`（`concept_*` と `concept_*_desc`） |
| 「困った状態」の判定 | `G/common/alert_types/`、`G/common/alert_groups/` |
| 内政 | `laws/`、`law_groups/`、`interest_groups/`、`interest_group_traits/`、`political_movements/`、`decrees/`、`institutions/`、`government_types/` |
| 経済 | `buildings/`、`production_methods/`、`production_method_groups/`、`goods/`、`pop_needs/`、`company_types/` |
| 外交・戦争 | `diplomatic_plays/`、`diplomatic_actions/`、`war_goal_types/`、`treaty_articles/`、`power_bloc_principles/`、`subject_types/` |
| 技術と時代・ランク | `technology/technologies/`、`technology/eras/00_eras.txt`、`country_ranks/00_country_ranks.txt` |
| 補正値・定数 | `static_modifiers/`、`script_values/`、`defines/` |
| DLC 判定 | `has_dlc_feature` を含む条件、`G/dlc_metadata/00_dlc_metadata.txt` の `name` |
| 正式な日本語名 | `G/localization/japanese/` と `vic3/localization-reference.md` |
| コミュニティの定石 | `vic3.paradoxwikis.com`（数値は必ずスクリプトで1件以上照合する。1.14 以前の記述であることが多い） |

1.14 で更新されたファイルが多い領域（`war_goal_types`・`journal_entries`・`treaty_articles`・`static_modifiers`・`interest_groups`・`defines`）に関わる項目は、wiki や旧ガイドの記述を信用せず、必ず現物を開いて確かめる。

## 2. 書き方

1. 候補の行動を一次情報から洗い出し、「どの国でも当てはまるか」「その時期にやることか」で絞る。国・文化・政体に固有のもの（明治維新 JE、ドイツ統一など）は載せない
2. 行動文は「〈画面や対象〉で〈操作〉する」「〈状態〉を確認する」の形で、動詞で終える。1行に1つの行動
3. 「なぜ」は判断の根拠を1行で書く。スクリプトが根拠なら `[src: ファイル名:行番号]` か `[src: ファイル名, 識別子]` を付ける。ゲーム内のヒント・チュートリアル・用語説明だけが根拠なら、「（公式の説明）」を付けたうえで `[src:]` も付ける。プレイ報告が根拠なら `（コミュニティ知見）` を付ける
4. **`[src:]` のファイル名が `G` の中に2つ以上あるとき**（`find "$G" -name <名前> | wc -l` が2以上）は、`common/laws/00_x.txt:120` のように `G` からの相対パスで書く。検証スクリプトはファイル名しか照合しないので、パスがないと別のファイルを指していても通ってしまう
5. 数値を書いたら、判断の目安になる数値だけを7章の表にも同じ値で載せる
6. 用語は書く前に `concept_*` キーで正式な訳を確かめる（例: 権力・行政力・影響力・列強）。本文は日本語名だけにし、英語名は8章に「日本語名（English）」の形で集める
7. **DLC が要る項目**: 根拠のスクリプトに `has_dlc_feature` がある、またはファイルが `G/dlc/` の中にあるときは、行動の行末に「（DLC名 が必要）」と書く。DLC 名は `00_dlc_metadata.txt` の `name` をそのまま使う
8. 他タイトルの語を混ぜない。書いたあとに次のコマンドで0件を確かめる: `grep -nE '安定度|ダカット|交易ノード|捏造|諜報網|Coalition|Aggressive Expansion' vic3/vic3-play-checklist.md`
9. 新しく使ったスクリプトファイルは、9章「一次情報」に `G` からの相対パスで追記する。wiki の URL は9章「コミュニティ情報」に書く（本文の `[src:]` に URL は入れない）
10. 旧ガイド（日本・プロイセン）は git 履歴（`git show main:vic3/vic3-japan-guide.md` 等）から発想のもととして読んでよい。ただし数値・`[src:]`・訳語は写さず、すべて 1.14 の現物で取り直す

## 3. 合格基準（各タスクの最後に確かめ、報告に書く）

- `python scripts/check_checklist.py vic3/vic3-play-checklist.md` が `OK` を返す
- そのタスクの章の項目数が予算以内に収まっている
- タスクで書いた数値ごとに「数値 → 確かめたファイル:行 → 実際の値」の対応表を報告に書いてある。`[src:]` が yml（名称）しか指していない数値は、効果値の裏付けになっていないので不合格
- 2章8の grep が0件
- 国・文化・政体に固有の行動が入っていない。入れかけて外したものがあれば、その一覧を報告に書く
- DLC が要る項目に印が付いている。その項目の一覧を報告に書く

## 4. 前のタスクのレビューで分かったこと（Task 3〜4 で実際に出た誤り）

- 画面名・タブ名・ボタン名は、`G/gui/*.gui` のタブのラベルキーとローカライズで確かめる。チュートリアル本文の言い回しをそのまま画面名にしない（チュートリアルは「政府改革タブ」と書くが、実際は「政策」パネルの「政府」タブにある「政府改革」ボタン。確認済みのタブ: 政策パネル＝概要・政府・法律・制度、予算パネル＝概要・州・資産、市場パネルに食料保障タブ）
- 用語説明を言い換えるときに、スクリプトと食い違う一般化をしない（「正当性が低いほど遅い」は誤り。実際は段階ごとの効果なので、段階で書く）
- チュートリアル固有の導線（チュートリアル目標の subgoal 等）を、どの国にも共通の行動として一般化しない
- 1つの主張に1つの `[src:]` を付ける。7章に載せたからといって本文の出典を省かない
- 警告の区分は、スクリプトの `type`（`alert` / `important_action` / `angry_important_action`）で書く。色の印象で書かない
- 訳語はローカライズのとおりにする（例: 「軍隊の給金」「浪費税額」）
- コミット末尾は `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` に固定する（実行モデルに合わせて変えない）
