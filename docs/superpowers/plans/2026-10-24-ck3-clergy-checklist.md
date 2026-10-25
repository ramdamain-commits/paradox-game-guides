# CK3 聖職者（聖界・神権制）プレイ中チェックリスト 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 既存の CK3 攻略（イングランド1066・システム・MOD）を廃止し、聖職者（聖界・神権制）のプレイ中チェックリストを 1.20.1 安定版基準でゼロから作る。政体ごとのシリーズの1本目。

**Architecture:** 中身は `ck3/ck3-clergy-play-checklist.md` に EU5・VIC3 と同じ書式で書き、既存の `checklist.html` で表示する（HTML は変更しない）。`scripts/check_checklist.py` は `GAME_DIRS` に CK3 を足すだけで、書式と `[src:]` の実在の検証はそのまま使う。

**Tech Stack:** Markdown、既存の `checklist.html`、Python 3.13 標準ライブラリ（unittest）、GitHub Pages（main への push で公開）

**Spec:** `docs/superpowers/specs/2026-10-24-ck3-clergy-checklist-design.md`（実装前に必ず通読する）。書式の詳細は `docs/superpowers/specs/2026-10-13-eu5-checklist-reset-design.md` の3章。完成例は `vic3/vic3-play-checklist.md`

**執筆タスク（Task 3〜6）の共通手順:** `docs/superpowers/plans/2026-10-24-ck3-clergy-checklist-writing-rules.md`。**Task 3〜6 の指示書には必ずこのファイルを添える**

## Global Constraints

- 作業は repo `C:\Users\ramda\projects\paradox-game-guides` の作業ブランチ `ck3-clergy-checklist` で行う。main へのマージと push は Task 8 の最後に、ユーザーの了承を得てから行う（main への push で即公開されるため）
- 対象パッチ: 1.20.1 安定版（`titus_branch.txt` = `release/1.20.1`、`appmanifest_1158310.acf` の `buildid` = `26046173`、`BetaKey` = `public`）。冒頭の表記は「1.20.1（ビルド 26046173）」
- ゲームスクリプトの場所: `C:/Program Files (x86)/Steam/steamapps/common/Crusader Kings III/game`
- DLC は dlc001〜dlc030（By God Alone まで）がすべてある前提。By God Alone は冒頭で必須と書き、項目ごとの印は付けない。ほかの DLC が要る項目は行末に「（DLC名 が必要）」
- 両政体に共通の項目はラベルなし、片方だけの項目は行末に「（聖界のみ）」「（神権制のみ）」。付け分けの基準は設計書2章の表（共通手順2-7）
- 比重: 聖界中心、神権制は1〜5章の項目数・字数のおよそ3割
- チェック項目は1〜5章の合計で100以内。本文は `[src:]` マーカーを除いて20,000字以内
- 章ごとの字数予算（`[src:]` を除く）: 冒頭200／1章1,600／2章3,000／3章3,400／4章3,000／5章1,900／6章2,100／7章1,300／8章1,300／9章700／余白1,500。章を書き終えて予算を超えていたら、その時点でコントローラーに報告する（融通はコントローラーが決める）
- 章ごとの字数は次で数える（全体の字数は検証スクリプトの値が正）

```bash
cd /c/Users/ramda/projects/paradox-game-guides && python - ck3/ck3-clergy-play-checklist.md <<'EOF'
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
for p in re.split(r"(?m)^(?=## )", t):
    print(p.splitlines()[0][:40], len(re.sub(r"\[src:[^\]]*\]", "", p)))
EOF
```

- 1項目は「行動1行（`- [ ] … {#id}`）＋任意の『なぜ』1行（`  - なぜ: …`）」まで。id は `^[a-z0-9]+(-[a-z0-9]+)*$`、ファイル内で一意、一度付けたら変えない
- 特定の人物・地域・ブックマークに固有の筋道は書かない。過去パッチとの差分（「1.20 で新しくなった」等）も書かない
- 旧 CK3 ガイドの数値・`[src:]`・訳語は写さない（1.20.1 の現物で取り直す）
- ドキュメント・コミットメッセージは日本語。コミット末尾に `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
- `git add` と `git commit` は別コマンドにし、間で `git diff --cached --stat` を確認する
- 実装担当は、引数なしの `python`/`cat` を起動しない。プロセスを名前一括（`taskkill /IM`）で止めない。変異確認は scratchpad の複製で行い、`git checkout <file>` で戻さない
- `checklist.html` のブラウザ確認と wiki の閲覧はコントローラー（メインセッション）が Playwright で行う（implementer / reviewer にはブラウザが無い）
- `_staging/ck3-1.19-factcheck.md` は消さない（ユーザー未了承）

## Review Focus

1. **ラベルの誤付け**: 聖界にも `government_is_theocracy` が付いているため、名前で「（神権制のみ）」と付けると聖界のプレイヤーが使える行動を見落とす → 共通手順2-7、Task 3〜5 の合格基準のラベル一覧、Task 7 のレビュー観点
2. **神権制の入口**: 開始ブックマークに神権制の人物はいない。1章が聖界の開始だけを前提にすると、神権制のプレイヤーは最初の手順から迷う → Task 3 Step 3
3. **プレイヤーの死**: 聖職者は世襲しないので、後を託す準備が抜けると操作する人物がいなくなる → Task 4 Step 4、Task 7 の熟練者の観点
4. **同名ファイル**: CK3 には `00_*.txt` など同じファイル名が複数のフォルダにあり、ファイル名だけの実在確認は別ファイルを指していても通る → 共通手順2-4と Task 6 Step 3 の重複名チェック
5. **保存状態の混線**: CK3 のチェック操作やリセットで、EU5・VIC3 のチェック状態が消えたり混ざったりしないこと → Task 6 Step 5 の (e)

---

### Task 1: 検証スクリプトを CK3 に対応させる

**Files:**
- Modify: `scripts/check_checklist.py`（冒頭 docstring、`GAME_DIRS`、`--game-dir` の help 文）
- Test: `tests/test_check_checklist.py`（`SelectGameDirTests`）

**Interfaces:**
- Produces: `GAME_DIRS["ck3"] = Path("C:/Program Files (x86)/Steam/steamapps/common/Crusader Kings III/game")`。`select_game_dir` と CLI の挙動は変えない

- [ ] **Step 1: テストを直して足す**（`SelectGameDirTests`）

```python
    def test_select_ck3(self):
        self.assertEqual(cc.select_game_dir(cc.REPO_ROOT / "ck3" / "x.md", None), cc.GAME_DIRS["ck3"])

    def test_select_unknown_folder(self):  # 既存。ck3/ を docs/ に差し替える
        self.assertIsNone(cc.select_game_dir(cc.REPO_ROOT / "docs" / "x.md", None))
```

- [ ] **Step 2: 失敗を確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest tests.test_check_checklist -v`
Expected: `test_select_ck3` が `KeyError: 'ck3'` で ERROR。ほかは PASS

- [ ] **Step 3: `GAME_DIRS` に `ck3` を足す**。docstring の使い方に `python scripts/check_checklist.py ck3/ck3-clergy-play-checklist.md` の例を足し、「eu5/・vic3/」と書いている2か所（docstring と `--game-dir` の help）を「eu5/・vic3/・ck3/」にする

- [ ] **Step 4: 全テストが通ることを確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest discover -s tests -v`
Expected: 全件 PASS

- [ ] **Step 5: 変異で落ちることを確かめる**。scratchpad に `scripts/` と `tests/` を複製し、複製で次の変異を入れて複製側のテストが落ちることを確かめる（本体は書き換えない）。報告に「変異 → 落ちたテスト名」を書く
  - `GAME_DIRS["ck3"]` に VIC3 のパスを入れる → `test_select_ck3` が落ちる

- [ ] **Step 6: EU5・VIC3 で回帰がないことを確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python scripts/check_checklist.py eu5/eu5-play-checklist.md && python scripts/check_checklist.py vic3/vic3-play-checklist.md`
Expected: 2つとも `OK`

- [ ] **Step 7: コミット**（`git add scripts/check_checklist.py tests/test_check_checklist.py` → `git diff --cached --stat` → メッセージ `scripts: check_checklist.py を CK3 に対応させる`）

---

### Task 2: 対象パッチの確定とチェックリストの骨組み

**Files:**
- Create: `ck3/ck3-clergy-play-checklist.md`

**Interfaces:**
- Consumes: Task 1 の CLI
- Produces: 冒頭と見出しだけの `ck3/ck3-clergy-play-checklist.md`。章見出しの文言は以下で固定（後続タスクはこの見出しの下に書く）

- [ ] **Step 1: ビルドを確かめる**（共通手順0のコマンド）。違っていたら作業を止めてユーザーに報告する
- [ ] **Step 2: 骨組みを書く**（`<日付>` は作業日）

```markdown
# CK3 プレイ中チェックリスト：聖職者（聖界・神権制）
> 対象パッチ: 1.20.1（ビルド 26046173） ／ 最終確認日: <日付>

聖職者として遊ぶときの「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。By God Alone が必要（無いと聖界・神権制は操作できない）。ほかの DLC はすべてある前提で書き、要る項目には「（DLC名 が必要）」と付ける。片方の政体だけの項目には「（聖界のみ）」「（神権制のみ）」と付ける。「（公式の説明）」は、ゲーム内の助言・チュートリアル・用語説明が根拠で、効果をスクリプトでは確かめていない記述。

## 1. 開始直後（ポーズ中にやること）

## 2. 聖職者の基盤づくり

## 3. 位を上げる

## 4. 教会を動かす・後を託す

## 5. 定期ルーチン {.routine}

## 6. 困ったとき

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

## 9. 出典

### 一次情報

- `common/governments/02_theocratic_government_types.txt`

### コミュニティ情報
```

- [ ] **Step 3: 検証する**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python scripts/check_checklist.py ck3/ck3-clergy-play-checklist.md`
Expected: `OK: 項目数 0 / …`

- [ ] **Step 4: コミット**（`git add ck3/ck3-clergy-play-checklist.md` → `git diff --cached --stat` → メッセージ `ck3: 聖職者チェックリストの骨組みを追加（1.20.1 基準）`）

---

### Task 3: 1章「開始直後」と2章「聖職者の基盤づくり」

**Files:**
- Modify: `ck3/ck3-clergy-play-checklist.md`（1・2章。必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: Task 2 の見出し、共通手順ファイル
- Produces: 1章（10項目以内、id 接頭辞 `start-`）、2章（22項目以内、id 接頭辞 `base-`、`###` で2〜4グループ。グループの軸は書き手が決める）

- [ ] **Step 1: 着手前の確認**（共通手順0）
- [ ] **Step 2: 一次情報を集める**。政体の取り分け（`02_theocratic_government_types.txt` の両政体の `can_get_government`・`flags`・`character_modifier`、`theocratic_lay_clergy_trigger`）、貸与契約・教会の義務・宗教上の上位者の用語説明、`pam_actions.txt` と `00_reactive_advice.txt` の聖職者向け助言、精神的充足（`spiritual_fulfillment`）と個人の教義（`personal_tenet`）の定義。候補一覧を scratchpad に書く
- [ ] **Step 3: 1章を書く**（ポーズ中に済む確認・設定だけ。時間を進めないとできないことは2章へ回す）。入口の違いを1項目で書く: 開始ブックマークの聖職者は聖界だけ（`00_bookmarks.txt` の `government = ecclesiastical_government`）で、神権制は地図から領主を選ぶか途中でなる
- [ ] **Step 4: 2章を書く**（信仰心と精神的充足、個人の教義、主君・上位者との関係、収入。各グループの冒頭に到達目標を1行の通常文で書いてよい）
- [ ] **Step 5: 7〜9章へ追記する**（共通手順2-5・2-6・2-11）
- [ ] **Step 6: 合格基準を確かめる**（共通手順3。1章1,600字・2章3,000字以内）
- [ ] **Step 7: コミット**（メッセージ `ck3: 聖職者チェックリストの開始直後・基盤づくりの章を執筆`。手順は Task 2 Step 4 と同じ）

---

### Task 4: 3章「位を上げる」と4章「教会を動かす・後を託す」

**Files:**
- Modify: `ck3/ck3-clergy-play-checklist.md`（3・4章。必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: Task 3 で使った id（重複させない）と8章の用語
- Produces: 3章（22項目以内、`rank-`）、4章（18項目以内、`church-`）。1〜4章の合計は70項目以内（5章の枠を残すため）

- [ ] **Step 1: 着手前の確認**（共通手順0）
- [ ] **Step 2: 一次情報を集める**。聖職称号の階梯（司教・大司教・枢機卿・教皇。`appoint_cardinal_interaction`・`increase_papabile_score_interaction`・`influence_papal_vote_interaction`・`request_ecclesiastical_title_expansion_interaction` など）、枢機卿団と教皇候補スコアの定義、神権制の聖職称号と信仰の長への道筋、勅書（`enact_a_bull_decision`）、公会議（`ecumenical_council.txt`）、教会分裂（`pam_*_great_schism_decision`）、聖戦の扇動（`ecclesiastic_incite_holy_war_interaction`）、後継の3系統（共通手順1「後継」）、傀儡（`pam_puppet_types.txt`）
- [ ] **Step 3: 3章を書く**（聖界の階梯を中心に、神権制の道筋を含める）
- [ ] **Step 4: 4章を書く**。後を託す準備（自分が死んだあと誰を操作するか。後継者の指名と、継承法ごとに事前に整えること）は必ず入れる。傀儡を入れるかは一次情報を見て決め、入れなかった場合は理由を報告に書く
- [ ] **Step 5: 7〜9章へ追記する**
- [ ] **Step 6: 合格基準を確かめる**（3章3,400字・4章3,000字以内、1〜4章の合計が70項目以内であることも書く）
- [ ] **Step 7: コミット**（メッセージ `ck3: 聖職者チェックリストの位を上げる・教会を動かす章を執筆`）

---

### Task 5: 5章「定期ルーチン」と6章「困ったとき」

**Files:**
- Modify: `ck3/ck3-clergy-play-checklist.md`（5・6章。必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: 1〜4章の内容（1回だけやることは5章に書かない）
- Produces: 5章（`###` で3〜4グループ、合計25項目以内、かつ1〜5章の合計が100以内）。グループ名と id 接頭辞は書き手が決めるが、設計書の目安「毎年／教皇選挙の前／公会議があるとき／戦争の前と後」から外すときは理由を報告に書く。6章は8症状以内

- [ ] **Step 1: 着手前の確認**（共通手順0）
- [ ] **Step 2: 一次情報を集める**（6章は `important_actions/` の助言の発火条件と、キリスト教会の状況の不安定・危機の段階を主な根拠にする）
- [ ] **Step 3: 5章を書く**
- [ ] **Step 4: 6章を書く**。1症状は次の形にする（チェックボックスは使わない）

```markdown
**〈症状〉**
- 見る場所: 〈画面・指標〉
- 打ち手: 〈行動〉（根拠 `[src: …]` または（コミュニティ知見））
```

- [ ] **Step 5: 7〜9章へ追記する**
- [ ] **Step 6: 合格基準を確かめる**（5章1,900字・6章2,100字以内。1〜5章全体の神権制の比重も書く）
- [ ] **Step 7: コミット**（メッセージ `ck3: 聖職者チェックリストの定期ルーチン・困ったときの章を執筆`）

---

### Task 6: 7〜9章の仕上げ・全体の整合・用語表・ブラウザ確認

**Files:**
- Modify: `ck3/ck3-clergy-play-checklist.md`
- Modify: `ck3/localization-reference.md`（チェックリストで使う語のうち、1.20.1 で訳が変わっていた・載っていない語だけ）

Step 1〜4・6 は implementer、Step 5 はコントローラーが行う。

- [ ] **Step 1: 数値を突き合わせる**。`grep -nE '[0-9]' ck3/ck3-clergy-play-checklist.md` で1〜6章の数値を抜き出し、判断に使う数値が7章に同じ値であること、7章の全行に `[src:]` か（コミュニティ知見）があることを確かめる
- [ ] **Step 2: 用語を突き合わせる**。本文の用語がすべて8章にあり、8章の語がすべて本文で使われていること。8章の訳語が 1.20.1 の `game_concept_*` キーと一致すること。ずれている・無い語は `ck3/localization-reference.md` も直す（それ以外の行は触らない）
- [ ] **Step 3: 出典を突き合わせる**。本文の `[src:]` のファイルがすべて9章「一次情報」にあること。加えて、`[src:]` のファイル名ごとに `find "$G" -name <名前> | wc -l` を数え、2以上なのにパスなしで書いているものが0件であること（数えた一覧を報告に書く）
- [ ] **Step 4: 上限と検証**。`python scripts/check_checklist.py ck3/ck3-clergy-play-checklist.md` が `OK: 項目数 ≤100 / 文字数 ≤20000` を返すこと。章ごとの字数（Global Constraints のコマンド）を報告に書く
- [ ] **Step 5: ブラウザで確かめる（コントローラー）**。repo 直下で `python -m http.server 8765` を起動し、Playwright で `http://localhost:8765/checklist.html?file=ck3/ck3-clergy-play-checklist.md&nocache=<時刻>` を開いて次を確かめる。結果とスクリーンショット1枚を残す
  - (a) チェックして再読込しても残る
  - (b) 全リセットとルーチンのリセットが、それぞれ対象だけを消す
  - (c) 出典トグルが効く
  - (d) 幅375pxで横スクロールが出ない。ダークモードで読める
  - (e) 先に EU5 と VIC3 のページで1項目ずつチェックしておき、CK3 側で全リセットしたあとも両方のチェックが残っている
  - (f) 1〜5章の流れに矛盾や重複がなく、1項目が2行を超えていない（通読）
- [ ] **Step 6: コミット**（メッセージ `ck3: 聖職者チェックリストの数値表・用語・出典を整備`。用語表を直したら `ck3/localization-reference.md` も add する）

---

### Task 7: 3名レビュー

**Files:**
- Modify: `ck3/ck3-clergy-play-checklist.md`（指摘の反映）

- [ ] **Step 1: レビューを依頼する**。`reviewer` エージェントを3並列で起動する（読み取り専用。報告は返信の全文で受け、コントローラーが `_staging/2026-10-xx-ck3-clergy-review-<観点>.md` に保存する）。観点は repo の `CLAUDE.md`「レビュー」節のとおり
  - 熟練者: 行動の正しさ・段階の妥当性・抜け漏れ（特に後を託す準備と、神権制の入口）・By God Alone の仕様
  - プレイヤー（一通り遊んだが聖職者プレイは新しい人）: 項目だけ見て操作できるか、画面名・用語がゲーム内表記と一致するか
  - テクニカルライター: 書式・表記揺れ・1項目2行以内・7章の数値の再掲の一致

  3名に共通する依頼:
  - 冒頭で buildid を確かめる（共通手順0）
  - `[src:]` を最低10件、実際にファイルを開いて値と識別子を照合する
  - 「（聖界のみ）」「（神権制のみ）」とラベルなしの項目を、設計書2章の基準と根拠の条件で照合する（最低10件）
  - 神権制の比重が3割程度か、特定の人物・地域の筋道が混ざっていないか、By God Alone 以外の DLC が要る項目に印が付いているかを見る
  - 指摘には重大度（critical / important / suggestion）と行番号を付ける
- [ ] **Step 2: 反映する**。critical と important はすべて反映する。suggestion は採否と理由を一覧にする。レビュアーの「直し方」を反映リストへ写す前に、根拠のスクリプト・助言の原文を1回開き、前提条件が落ちていないかを確かめる。訂正した語句・数値ごとに `grep -n` でファイル全体を見て、旧値が残っていないことを確かめる
- [ ] **Step 3: 合格基準を確かめてコミット**（メッセージ `ck3: 聖職者チェックリストに3名レビューの指摘を反映`）

---

### Task 8: 旧ファイルの削除・付随更新・マージ

**Files:**
- Delete（git 管理）: `ck3/ck3-england-1066-guide.md` `ck3/ck3-systems-guide.md` `ck3/ck3-recommended-mods.md` `docs/superpowers/specs/2026-04-09-ck3-systems-guide-design.md` `docs/superpowers/plans/2026-04-09-ck3-systems-guide.md`
- Delete（git 管理外）: Task 7 のレビュー結果 `_staging/2026-10-xx-ck3-clergy-review-*.md`（`_staging/ck3-1.19-factcheck.md` は残す）
- Modify: `index.html`、`README.md`、`CHANGELOG.md`、`CLAUDE.md`、`docs/templates/guide-section-template.md`、`docs/procedures/new-country-guide.md`、`docs/templates/country-guide-plan-template.md`

- [ ] **Step 1: ビルドを確かめ直す**（共通手順0のコマンド）。26046173 から変わっていたら、`python scripts/check_checklist.py ck3/ck3-clergy-play-checklist.md` を再実行し、変わった旨と結果をユーザーに報告してから進む
- [ ] **Step 2: 削除直前のコミットを控える**。`git log -1 --format=%h -- ck3/ck3-england-1066-guide.md` の値を Step 6・7 の「削除コミットの1つ前」の表記に使う
- [ ] **Step 3: git 管理下のファイルを `git rm` で削除する**。git 管理外のレビュー結果は、`ls _staging` の出力を報告に残してから `ck3-clergy-review-*` だけを `rm` する
- [ ] **Step 4: `index.html` を直す**
  - CK3 セクション（`<section class="game-section" data-game="ck3">` の `card-list`、現在 228〜257行付近の `<li>` 3枚）を2枚に置き換える。書き方は VIC3 セクションの2枚と同じで、変える値は次のとおり
    - 1枚目: `href="checklist.html?file=ck3/ck3-clergy-play-checklist.md"`、タイトル「聖職者（聖界・神権制）チェックリスト」、説明「1.20.1 — 聖職者として遊ぶときの「いつ・何をするか」」、タグ `tag--guide`「攻略」
    - 2枚目: `href="viewer.html?file=ck3/localization-reference.md"`、タイトル「用語対照表」、説明「ゲーム内日本語訳と英語名の対照」、タグ `tag--guide`「用語」
  - 7行目の meta description と186行目の副題から「おすすめMOD」を外す（MOD 記事が3タイトルとも無くなるため）。文言は「EU5・CK3・Vic3 のプレイ中チェックリスト」とする
- [ ] **Step 5: `README.md` を直す**
  - 「### Crusader Kings III」節の表と「おすすめMOD」の行を、VIC3 節と同じ形の2行の表（聖職者（聖界・神権制）チェックリスト `1.20.1`／用語対照表 `—`）に置き換える
  - 42行目の構成図の `ck3/` の説明を「Crusader Kings III 攻略（政体ごとのプレイ中チェックリスト＋用語対照表）」にする
  - 58行目の命名例を `ck3/ck3-clergy-play-checklist.md` にする
- [ ] **Step 6: `CLAUDE.md`（repo）を直す**
  - 4行目の模範例を「git 履歴の `ck3/ck3-england-1066-guide.md`（`<Step 2 の値>` 時点）」にする
  - 24行目の命名例を `ck3/ck3-clergy-play-checklist.md` にする
  - 32行目の「CK3 のファイル名は勢力名＋開始年」の段落を、「CK3 も国別ガイドを置かず、政体ごとのチェックリスト `ck3/ck3-<政体の英語名>-play-checklist.md` を正本とする（1本目 `ck3/ck3-clergy-play-checklist.md`）。書式は EU5 と同じ。コミット前に `python scripts/check_checklist.py ck3/<file>` を通す。政体の追加順と残りは設計書 `docs/superpowers/specs/2026-10-24-ck3-clergy-checklist-design.md` の8章」という趣旨の段落に置き換える
  - 「### CK3」の参照先リストに、By God Alone の主なファイル（`common/decisions/dlc_decisions/pam/`、`common/character_interactions/pam_interactions.txt`、`common/scripted_triggers/pam_scripted_triggers.txt`、`common/game_concepts/pam_game_concepts.txt`）、`common/governments/02_theocratic_government_types.txt`、ローカライズ `localization/japanese/dlc/pam/`、バージョン確認の `titus_branch.txt` を足す
  - 265行目付近の `index.html` のカードの例外の記述に、CK3 のチェックリストも `checklist.html?file=ck3/ck3-clergy-play-checklist.md` 形式であることを足す
- [ ] **Step 7: テンプレート・手順書を直す**
  - `docs/templates/guide-section-template.md` 4行目と `docs/procedures/new-country-guide.md` 50行目の模範例を、Step 6 の4行目と同じ書き方にする
  - `docs/procedures/new-country-guide.md` 3行目と `docs/templates/country-guide-plan-template.md` 3行目の注意書きに、CK3 も国別ガイドを置かない（政体ごとのチェックリストが正本）ことを足す
- [ ] **Step 8: 参照切れがないことを確かめる**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && grep -rnE 'ck3-(england-1066-guide|systems-guide|recommended-mods)' --include=*.md --include=*.html --include=*.py . | grep -vE '^\./CHANGELOG\.md:|^\./docs/superpowers/(specs|plans)/2026-03-31-recommended-mods|^\./docs/superpowers/(specs|plans)/2026-10-(19-vic3|24-ck3-clergy)-checklist|^\./_staging/'
```
Expected: 出力は `CLAUDE.md`・`docs/templates/guide-section-template.md`・`docs/procedures/new-country-guide.md` の模範例の行（「git 履歴の」を含む行）だけ

- [ ] **Step 9: `CHANGELOG.md` の先頭に追記する**

```markdown
## 2026-10-xx CK3 攻略を政体ごとのプレイ中チェックリストへ作り直し（1本目: 聖職者）

### Added
- `ck3/ck3-clergy-play-checklist.md`: 聖職者（聖界・神権制）として遊ぶときの「いつ・何をするか」をまとめたチェックリスト（1.20.1・ビルド 26046173 基準）。`checklist.html?file=ck3/ck3-clergy-play-checklist.md` で表示する

### Changed
- `scripts/check_checklist.py`: `ck3/` のパスで CK3 のゲームフォルダを選ぶようにした
- テンプレートの模範例を git 履歴の参照に差し替えた

### Removed
- イングランド1066ガイド・汎用システムガイド・MOD 記事（git 履歴から復元可）
```

- [ ] **Step 10: 最終確認**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest discover -s tests && python scripts/check_checklist.py ck3/ck3-clergy-play-checklist.md && python scripts/check_checklist.py vic3/vic3-play-checklist.md && python scripts/check_checklist.py eu5/eu5-play-checklist.md && git status --short`
Expected: テスト全件 OK、3つのチェックリストが `OK`、未コミットの変更なし（Step 11 のコミット後）

- [ ] **Step 11: コミット**（`git add -A` の前に `git status --short` で対象を確かめる → `git diff --cached --stat` → メッセージ `ck3: 旧ガイドを削除し、政体ごとのチェックリストの構成へ切り替え`）
- [ ] **Step 12: マージと push（ユーザーの了承後）**。`git diff --stat main...ck3-clergy-checklist` を示して了承を得てから、main へ `--no-ff` でマージして push する（push で GitHub Pages に即時公開される）。push 後、`https://ramdamain-commits.github.io/paradox-game-guides/checklist.html?file=ck3/ck3-clergy-play-checklist.md` が表示されることをコントローラーが Playwright で確かめる。あわせて root repo のサブモジュール参照をコミットする
