# CK3 交易商人のプレイ中チェックリスト 設計書（政体別シリーズ2本目）

- 作成日: 2026-11-23
- 対象: `paradox-game-guides` の CK3 部分のみ
- 先行事例: 1本目の聖職者版（設計書 `docs/superpowers/specs/2026-10-24-ck3-clergy-checklist-design.md`、計画 `docs/superpowers/plans/2026-10-24-ck3-clergy-checklist.md`、執筆の共通手順 `docs/superpowers/plans/2026-10-24-ck3-clergy-checklist-writing-rules.md`）。本書は聖職者版と異なる点だけを書き、同じ点は聖職者版の設計書の節を参照する

## 1. 背景と決定事項

| 項目 | 決定 | 出どころ |
|---|---|---|
| 2本目の対象 | Silk & Silver（`dlc031_ep5`）でプレイ可能になった「交易商人」（`merchant_government`） | ユーザー（2026-11-23）。聖職者版設計書8章の「最近追加された政体から順に」に従う。8章の表は DLC 番号順で、1.21 で入った Silk & Silver が載っていなかった |
| 共和制の扱い | 同じ DLC の「共和制」（`republic_government`）は**別の1本**にする（3本目） | ユーザー（2026-11-23）。所領なしの商会と、所領ありの議会・パトリシアンで仕組みが大きく違うため |
| 書式・目的・使う場面・出典 | 聖職者版と同じ（プレイ中に横に置く／数値はスクリプトで裏付けて `[src:]`／`checklist.html` でチェックを入れる） | シリーズの決めごと |

### 対象パッチ

- **1.21.0.3**: `titus_branch.txt` = `release/1.21.0`、`launcher-settings.json` の `rawVersion` = `1.21.0.3`、`appmanifest_1158310.acf` の `buildid` = **26785313**、`BetaKey` = `public`（2026-11-23 に確認）
- 冒頭の対象パッチ欄は「1.21.0.3（ビルド 26785313）」と書く。作業の最初と最後に `buildid` を照合する（聖職者版設計書1章と同じ）

### 現物で確かめたこと（2026-11-23）

| 確かめたこと | 結果 | 根拠 |
|---|---|---|
| DLC の所持 | Silk & Silver の depot（`4232910`）がインストール済み。DLC フォルダは 2026-11-18（1.21 配信日）作成 | `appmanifest_1158310.acf`、`game/dlc/dlc031_ep5/dlc031.dlc` |
| DLC との対応 | 交易商人の開始ブックマークに `requires_dlc_flag = silk_and_silver`。交易商人・共和制のプレイ可否は `has_dlc_feature = playable_republics` で判定 | `00_bookmarks.txt` の `bm_1066_merchants`、`00_rules.txt` の `GAME_OVER_CANNOT_PLAY_MERCHANT` |
| 政体の定義 | `merchant_government`（`00_government_types.txt:1554` 付近）。所領なしで操作できる（`landless_playable = yes`）、拠点は商会（`domicile_type = merchant_company`）、仕組みの種別は `mechanic_type = merchant`、なる条件は所領なしの伯爵級の称号を持つこと（`can_get_government`） | 同ファイル |
| 入口 | 1066年の `bm_1066_merchants` で交易商人6人・共和制1人、1178年の `bm_1178_merchants` にも人物あり。途中からは決断 `become_merchant_decision` でなれる | `00_bookmarks.txt`、`gdp_merchant_decisions.txt` |
| スクリプトの量 | `gdp` の付くファイルが `common/`・`events/` に170本（決断 `common/decisions/dlc_decisions/gdp/`、交流 `11_gdp_merchant_interactions.txt` 等、助言 `merchant_actions.txt`・`gdp_reactive_advice.txt`、チュートリアル `gdp_tutorial_lesson_advice.txt`、用語 `gdp_game_concepts.txt` に108語） | ファイル一覧 |
| ローカライズ | `localization/japanese/dlc/gdp/` に65ファイル。確認済みの訳語: 交易商人 = `game_concept_merchant`、商会 = `game_concept_company`、交易担当者 = `game_concept_trader`、交易品 = `game_concept_trade_good`、交易路 = `game_concept_trade_route`、交易商家 = `game_concept_merchant_family`、パトリシアン = `game_concept_patrician`、市場 = `market`、交易知識 = `trade_expertise`、商会規模 = `company_size`、交易契約 = `trade_contract`、特別契約 = `luxury_contract`、方針契約 = `unity_contract`、後援者契約 = `patron_contract`、交易機会 = `trade_opportunity`、営利交易路 = `profit_route`、委託交易路 = `commission_route`、交易独占権 = `trade_monopoly`、貸し付け = `loan`、領国奪取 = `seize_realm_cb`、交易特許状 = `merchant_charter`（いずれも `game_concept_` を前に付けたキー）、政体名 `merchant_government` = 「交易商人」、交流名「土地を購入」「共和国に加わる」。**`company_purpose` と `company_sentiment` はどちらも「商会方針」**で訳が衝突しているので、本文では片方に英語名を併記するなど書き分ける | `gdp_game_concepts_l_japanese.yml` ほか |
| 共和国への移行 | 交易商人が共和国のパトリシアンになる経路がある（交流 `merchant_join_republic_interaction`、効果 `gdp_merchant_becomes_patrician_effect`） | `11_gdp_merchant_interactions.txt:2255`、`gdp_merchant_scripted_effects.txt:2689` |

### 前提（ユーザー未確認の仮定）

- 読み手・利用者・DLC の前提は聖職者版設計書1章と同じ。冒頭に「Silk & Silver が必要」と1行書く
- フォーラムと Wiki は自動取得できない。配信から日が浅くコミュニティ情報も少ないので、`（コミュニティ知見）` は無理に埋めない。スクリプトと「（公式の説明）」で書ける範囲を本文にする

## 2. 構成

### ファイル

| ファイル | 役割 | 状態 |
|---|---|---|
| `ck3/ck3-merchant-play-checklist.md` | 中身の正本 | 新規 |
| `checklist.html` | 表示用ビューア | 変更しない（`checklist.html?file=ck3/ck3-merchant-play-checklist.md` で開く） |
| `scripts/check_checklist.py` | 書式と出典の検証 | 変更しない（`ck3/` は聖職者版で対応済み） |
| `ck3/localization-reference.md` | 用語の正本 | このチェックリストで使う語だけ足す・直す |

政体は1つなので、聖職者版の「（聖界のみ）」のような政体ラベルは使わない。共和国へ移ったあとの話は4章の入口までに留め、共和制の運営は3本目で扱う。

### 章立てと字数予算

聖職者版と同じく、年ではなく「商会の段階」で区切る。字数予算は、聖職者版の実測（`[src:]` を除き計18,450字）を基準に割った。聖職者版は1〜4章が予算より約2,500字少なく、7章（+1,090）・8章（+590）・9章（+1,690）が予算を大きく超えた。そのため今回は7〜9章を実測並みに取り、1〜4章を絞る。

| 章 | 内容（取捨と小見出しは書き手が調べて決めてよい） | 項目数 | 字数予算 | 聖職者版の実測 |
|---|---|---|---|---|
| 冒頭 | 対象パッチ・最終確認日・「Silk & Silver が必要」・DLC 前提 | — | 400 | 359 |
| 1. 開始直後（ポーズ中にやること） | 政体の確認、商会と拠点の位置、商会方針（`company_purpose`）、交易担当者の割り当て、最初の交易路、交易特許状の要請、借金の有無 | 10以内 | 1,600 | 1,612 |
| 2. 交易の基盤づくり | 交易品・市場・交易路の選び方（営利交易路・委託交易路）、交易知識、交易契約（特別契約・方針契約・後援者契約）、交易機会、商会方針（`company_sentiment`） | 13 | 2,400 | 2,151 |
| 3. 商会を大きくする | 商会規模と移転、交易特許状の活用、交易独占権、貸し付け・戦争への出資、合併と敵対的買収、仕上げの決断（`merchant_caravaneer/artisan/creditor_capstone_decision` の3種） | 12 | 2,400 | 2,061 |
| 4. 所領と後を託す | 「土地を購入」、「共和国に加わる」（パトリシアンへ）、領国奪取、交易商家と家の結束（`merchant_house_unity`）、後継者 | 12 | 2,300 | 2,310 |
| 5. 定期ルーチン `{.routine}` | 毎年／契約・機会が出たとき／戦争の前と後 など。分け方は書き手が決めてよい | 12 | 1,900 | 1,935 |
| 6. 困ったとき | 症状 → 見る場所 → 打ち手（1症状3行） | — | 1,400 | 1,348 |
| 7. 判断の目安 | 本文の判断に使う数値だけの表。全行に出典 | — | 2,300 | 2,390 |
| 8. 用語 | このページに出る語のみ。`ck3/localization-reference.md` へリンク。交易の語が多いので聖職者版より増える見込み | — | 2,000 | 1,892 |
| 9. 出典 | スクリプトとコミュニティ情報を分けて記載 | — | 2,300 | 2,392 |
| 余白 | レビュー反映用 | — | 1,000 | （聖職者版は 1,550 残し） |
| **計** | | **59** | **20,000** | 18,450 |

- 各章を書き終えるたびに `[src:]` を除いた字数を測り、予算との差を報告する（測り方は聖職者版と同じ `\[src:[^\]]*\]` を除いた文字数。章ごとの数え方は `## ` 見出しで区切る）。章の予算を300字超えたら、その時点でほかの章から融通するかを決める
- **後を託す準備は必ず入れる**（聖職者版と同じ理由。交易商人は `rulers_should_have_dynasty = yes` の家で続くので、跡継ぎと家の結束が操作の継続を左右する）
- 2〜4章の段階の分け方が実際の遊び方と合わないと分かったら、章の中身を入れ替えてよい（章番号と「1〜4章は進捗、5章はルーチン、6章以降はチェックなし」の枠組みは変えない）

### 載せないもの

- 共和制の運営（議会・投票・布告・パトリシアンの家の野望など）。3本目で扱う
- 交易商人以外の政体、特定の人物の攻略の筋道、過去パッチとの差分の履歴、長い仕組みの解説（聖職者版と同じ）
- 交易の仕組みのうち交易商人に限らない部分（交易路の地図の見方の詳細など）は、交易商人の行動に要る範囲だけ書く

### 分量の上限

聖職者版設計書2章と同じ（チェック項目100以内・本文2万字以内・1項目は行動1行＋「なぜ」1行まで）。

## 3. 書式と中身の検証

- 書式は聖職者版設計書3章と同じ。冒頭行は次のとおり

```markdown
# CK3 プレイ中チェックリスト：交易商人
> 対象パッチ: 1.21.0.3（ビルド 26785313） ／ 最終確認日: YYYY-MM-DD
```

- 訳語は本文に書く前に `game_concept_*` キーで確かめる（1章の表の確認済みの語以外は未確認。2026-11-23 の確認では、推測で置いた訳語の多くが実際と違った。例: 「贅沢品の契約」→ 正しくは「特別契約」、「結束の契約」→「方針契約」）
- 画面名・ボタン名は `gui/*.gui` とローカライズで確かめる
- 「（公式の説明）」の主な当たり先: `gdp_game_concepts.txt` の用語説明、チュートリアル `gdp_tutorial_lesson_advice.txt`、助言 `merchant_actions.txt`・`gdp_reactive_advice.txt`
- 完成後に3名のレビュー（熟練者・プレイヤー・テクニカルライター）。`[src:]` 全件の実在と行番号・主要な数値を照合する（`check_checklist.py` はファイル名しか見ないため）
- 書き終えたら `buildid` を再照合する

## 4. 執筆の進め方

聖職者版の計画（Task 3〜8）と執筆の共通手順（`2026-10-24-ck3-clergy-checklist-writing-rules.md`）をそのまま使う。違いだけ書く。

| タスク | 内容 | 合格の目安 |
|---|---|---|
| 1 | 骨組み（冒頭・9つの `##` 見出し・出典の小見出し）を作る | `check_checklist.py` が通る |
| 2 | 1章・2章 | 予算 1,600 / 2,400 字の±300字以内、項目 10 / 13 前後 |
| 3 | 3章・4章 | 予算 2,400 / 2,300 字の±300字以内。ここで1〜4章の合計を報告し、5〜9章の予算を見直す |
| 4 | 5章・6章 | 予算 1,900 / 1,400 字 |
| 5 | 7〜9章の仕上げ・用語表・全体の整合・ブラウザ確認（聖職者版設計書4章の確認項目） | 本文 19,000字以内（余白 1,000 字を残す） |
| 6 | 3名レビューと反映 | 本文 20,000字以内、`[src:]` 全件の実在と行番号 |
| 7 | 付随更新（`index.html` のカード、`README.md`、`CHANGELOG.md`、repo の `CLAUDE.md` の CK3 段落と基準パッチの記述、`ck3/localization-reference.md`） | `check_checklist.py` と `python -m unittest discover -s tests` が通る |

各タスクの前に `buildid` を照合する。委任する場合は、委任先に本体を直接書かせるか置換リストで返させるかを聖職者版と同じ方式で決める。
