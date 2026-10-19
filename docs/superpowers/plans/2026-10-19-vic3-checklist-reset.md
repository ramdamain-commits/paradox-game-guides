# VIC3 プレイ中チェックリスト 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 既存の VIC3 攻略（日本・プロイセン・MOD）を廃止し、どの国でも使える「プレイ中に横に置くチェックリスト」を 1.14 オープンベータ基準でゼロから作る。

**Architecture:** 中身は `vic3/vic3-play-checklist.md` に EU5 と同じ書式で書き、既存の `checklist.html` で表示する（HTML は変更しない）。`scripts/check_checklist.py` は Markdown のパスからゲームを選べるように改修し、書式と `[src:]` の実在を機械的に検証する。

**Tech Stack:** Markdown、既存の `checklist.html`（marked 15.0.12）、Python 3.13 標準ライブラリ（argparse / re / unittest）、GitHub Pages（main への push で公開）

**Spec:** `docs/superpowers/specs/2026-10-19-vic3-checklist-reset-design.md`（実装前に必ず通読する）。書式の詳細は先行事例 `docs/superpowers/specs/2026-10-13-eu5-checklist-reset-design.md` の3章

**執筆タスク（Task 3〜6）の共通手順:** `docs/superpowers/plans/2026-10-19-vic3-checklist-writing-rules.md`。**Task 3〜6 の指示書には必ずこのファイルを添える**

## Global Constraints

- 作業は repo `C:\Users\ramda\projects\paradox-game-guides` の作業ブランチ `vic3-checklist-reset` で行う。main へのマージと push は Task 8 の最後に、ユーザーの了承を得てから行う（main への push で即公開されるため）
- 対象パッチ: 1.14 オープンベータ（ベータキー `1.14-openbeta`、`caligula_branch.txt` = `release/1.14.5`、`appmanifest_529340.acf` の `buildid` = `25629520`）。冒頭の表記は「1.14 オープンベータ（release/1.14.5・ビルド 25629520）・変動注意」
- ゲームスクリプトの場所: `C:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game`
- DLC は dlc001〜dlc018（EP2 まで）がすべてある前提。DLC が要る項目は行末に「（DLC名 が必要）」
- チェック項目は1〜5章の合計で100以内。本文は `[src:]` マーカーを除いて20,000字以内
- 1項目は「行動1行（`- [ ] … {#id}`）＋任意の『なぜ』1行（`  - なぜ: …`）」まで。id は `^[a-z0-9]+(-[a-z0-9]+)*$`、ファイル内で一意、一度付けたら変えない
- 国・文化・政体に固有の行動は書かない。過去パッチとの差分も書かない
- 旧 VIC3 ガイドの数値・`[src:]`・訳語は写さない（1.14 の現物で取り直す）
- ドキュメント・コミットメッセージは日本語。コミット末尾に `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`
- `git add` と `git commit` は別コマンドにし、間で `git diff --cached --stat` を確認する
- 実装担当は、引数なしの `python`/`cat` を起動しない。プロセスを名前一括（`taskkill /IM`）で止めない。変異確認は scratchpad の複製で行い、`git checkout <file>` で戻さない
- `checklist.html` のブラウザ確認と wiki の閲覧はコントローラー（メインセッション）が Playwright で行う（implementer / reviewer にはブラウザが無い）

## Review Focus

1. **ベータの自動更新**: 作業の途中で Steam がビルドを更新すると、`[src:]` の行番号や数値が黙ってずれる → 共通手順0（毎タスクの冒頭で buildid を確認）と Task 8 Step 1
2. **同名ファイル**: VIC3 では同じファイル名が複数のフォルダにあり、ファイル名だけの実在確認は別ファイルを指していても通る → 共通手順2-4（重複名は相対パスで書く）と Task 6 Step 3 の重複名チェック
3. **保存状態の混線**: VIC3 のチェック操作やリセットで、EU5 のチェック状態が消えたり混ざったりしないこと → Task 6 Step 5 の (e)
4. **実行場所**: 検証スクリプトを repo 直下以外から、または絶対パスで実行しても、同じゲームフォルダが選ばれること → Task 1 のテスト `test_select_absolute_and_relative_agree`
5. **DLC の印漏れ**: DLC が無いと出ない操作に印が無いと、DLC なしの環境では「画面に無い」行動になる → 共通手順2-7と Task 7 のレビュー観点

---

### Task 1: 検証スクリプトをパスからゲームを選ぶよう改修

**Files:**
- Modify: `scripts/check_checklist.py`（冒頭 docstring、`DEFAULT_GAME_DIR`、`main`）
- Test: `tests/test_check_checklist.py`

**Interfaces:**
- Produces:
  - `REPO_ROOT: Path` = `Path(__file__).resolve().parents[1]`
  - `GAME_DIRS: dict[str, Path]` = `{"eu5": Path("C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis V/game"), "vic3": Path("C:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game")}`
  - `select_game_dir(markdown: Path, override: Path | None) -> Path | None`: `override` があればそれを返す。なければ `markdown.resolve()` を `REPO_ROOT` からの相対にして、最初のフォルダ名で `GAME_DIRS` を引く。repo の外、または未知のフォルダなら `None`
  - CLI: `--game-dir` の既定値は `None`。`--skip-src` が無く、`select_game_dir` が `None` なら、標準エラーに「ゲームディレクトリを決められない: <path>（--game-dir で指定するか --skip-src で省略）」と出して終了コード2。ディレクトリが存在しないときの既存のメッセージと終了コード2は変えない
  - `DEFAULT_GAME_DIR` は削除する（`GAME_DIRS["eu5"]` に置き換わる）

- [ ] **Step 1: 失敗するテストを書く**（`tests/test_check_checklist.py` に `SelectGameDirTests` クラスを追加）

```python
class SelectGameDirTests(unittest.TestCase):
    def test_select_eu5(self):
        self.assertEqual(cc.select_game_dir(cc.REPO_ROOT / "eu5" / "x.md", None), cc.GAME_DIRS["eu5"])

    def test_select_vic3(self):
        self.assertEqual(cc.select_game_dir(cc.REPO_ROOT / "vic3" / "x.md", None), cc.GAME_DIRS["vic3"])

    def test_select_unknown_folder(self):
        self.assertIsNone(cc.select_game_dir(cc.REPO_ROOT / "ck3" / "x.md", None))

    def test_select_outside_repo(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(cc.select_game_dir(Path(d) / "vic3" / "x.md", None))

    def test_select_override_wins(self):
        self.assertEqual(cc.select_game_dir(cc.REPO_ROOT / "vic3" / "x.md", Path("D:/g")), Path("D:/g"))

    def test_select_absolute_and_relative_agree(self):
        old = os.getcwd()
        try:
            os.chdir(cc.REPO_ROOT / "scripts")
            rel = cc.select_game_dir(Path("../vic3/x.md"), None)
        finally:
            os.chdir(old)
        self.assertEqual(rel, cc.GAME_DIRS["vic3"])

    def test_main_returns_2_when_game_unknown(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "c.md"
            f.write_text(doc(""), encoding="utf-8")
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                code = cc.main([str(f)])
        self.assertEqual(code, 2)
        self.assertIn("--game-dir", err.getvalue())
```

（`import os` を先頭に足す）

- [ ] **Step 2: 失敗を確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest tests.test_check_checklist -v`
Expected: `SelectGameDirTests` の7件が `AttributeError`（`select_game_dir` / `REPO_ROOT` 未定義）で FAIL/ERROR。既存のテストは PASS のまま

- [ ] **Step 3: `select_game_dir` と CLI の変更を実装する**（Interfaces のとおり。`main` は `select_game_dir(args.markdown, args.game_dir)` の結果を使う。docstring の使い方に `python scripts/check_checklist.py vic3/vic3-play-checklist.md` の例を足す）

- [ ] **Step 4: 全テストが通ることを確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest discover -s tests -v`
Expected: 全件 PASS（既存の `test_main_returns_2_without_game_dir` を含む）

- [ ] **Step 5: 変異で落ちることを確かめる**。scratchpad に `scripts/` と `tests/` を複製し、複製の `select_game_dir` で次の2つの変異を1つずつ入れて、複製側のテストが落ちることを確かめる（本体は書き換えない）。報告に「変異 → 落ちたテスト名」を書く
  - `override` を無視する → `test_select_override_wins` が落ちる
  - `resolve()` を外す → `test_select_absolute_and_relative_agree` が落ちる

- [ ] **Step 6: EU5 で回帰がないことを確かめる**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python scripts/check_checklist.py eu5/eu5-play-checklist.md`
Expected: `OK: 項目数 81 / …`（`--game-dir` なしで EU5 のフォルダが選ばれる）

- [ ] **Step 7: コミット**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && git add scripts/check_checklist.py tests/test_check_checklist.py
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git diff --cached --stat
```
```bash
cd /c/Users/ramda/projects/paradox-game-guides && git commit -F - <<'EOF'
scripts: check_checklist.py が Markdown のパスから検証するゲームを選ぶようにする

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
EOF
```

---

### Task 2: 対象パッチの確定とチェックリストの骨組み

**Files:**
- Create: `vic3/vic3-play-checklist.md`

**Interfaces:**
- Consumes: Task 1 の CLI
- Produces: 冒頭と見出しだけの `vic3/vic3-play-checklist.md`。章見出しの文言は以下で固定（後続タスクはこの見出しの下に書く）

- [ ] **Step 1: ビルドを確かめる**（共通手順0のコマンド）。違っていたら作業を止めてユーザーに報告する
- [ ] **Step 2: 時代の年と日本語名を確かめる**

```bash
G="/c/Program Files (x86)/Steam/steamapps/common/Victoria 3/game"; sed 's/^\xEF\xBB\xBF//' "$G/common/technology/eras/00_eras.txt" | grep -nE '^era_[0-9]'; grep -rnE '^\s*era_[1-5]:' "$G/localization/japanese/"
```
Expected: era_2 `#1836-1861`、era_3 `#1862-1886`、era_4 `#1887-1911`、era_5 `#1911-1936`。年が違っていたら見出しの年を直し、ユーザーに報告する。時代の日本語名のキーが見つかれば見出しの括弧内に「・時代名」を添える。見つからなければ添えない（`JAP_era_*` は日本の元号なので使わない）

- [ ] **Step 3: 骨組みを書く**（`<日付>` は作業日）

```markdown
# VIC3 プレイ中チェックリスト
> 対象パッチ: 1.14 オープンベータ（release/1.14.5・ビルド 25629520）・変動注意 ／ 最終確認日: <日付>

どの国でも共通の「いつ・何をするか」をまとめたチェックリスト。チェック状態はこのブラウザに保存される。国ごとの事情は扱わない。DLC はすべてある前提で書き、DLC が要る項目には「（DLC名 が必要）」と付ける。「（公式の説明）」は、ゲーム内のヒント・チュートリアル・用語説明が根拠で、効果をスクリプトでは確かめていない記述。

## 1. 開始直後（ポーズ中にやること）

## 2. 序盤（1836〜1861）

## 3. 中盤（1862〜1886）

## 4. 終盤（1887〜）

## 5. 定期ルーチン {.routine}

## 6. 困ったとき

## 7. 判断の目安

| 指標 | 目安 | 出典 |
|---|---|---|
| 時代の区切り | 1836〜1861／1862〜1886／1887〜1911／1911〜1936 | [src: 00_eras.txt, era_2 〜 era_5] |

## 8. 用語

完全版は [用語対照表](localization-reference.md)。

## 9. 出典

### 一次情報

- `common/technology/eras/00_eras.txt`

### コミュニティ情報
```

- [ ] **Step 4: 検証する**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python scripts/check_checklist.py vic3/vic3-play-checklist.md`
Expected: `OK: 項目数 0 / …`

- [ ] **Step 5: コミット**（`git add vic3/vic3-play-checklist.md` → `git diff --cached --stat` → メッセージ `vic3: プレイ中チェックリストの骨組みを追加（1.14 オープンベータ基準）`）

---

### Task 3: 1章「開始直後」と2章「序盤」

**Files:**
- Modify: `vic3/vic3-play-checklist.md`（1・2章。必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: Task 2 の見出し、共通手順ファイル
- Produces: 1章（10項目以内、id 接頭辞 `start-`）、2章（25項目以内、id 接頭辞 `early-`、`###` で2〜4グループ。グループの軸は書き手が決める。設計書の目安は「財政の安定 → 建設の回し方 → 最初の法改正」）

- [ ] **Step 1: 着手前の確認**（共通手順0）
- [ ] **Step 2: 一次情報を集める**。特に `tutorial_lessons/` の `budget_balance`・`buildings`・`capacities`・`production_methods`・`grow_gdp`・`reform_government`・`promote_ig`・`intro`、`tutorial_lesson_chains/00_tutorial_lesson_chains.txt` の順序、`alert_types/`。候補一覧を scratchpad に書く
- [ ] **Step 3: 1章を書く**（ポーズ中に済む設定・確認だけ。時間を進めないとできないことは2章へ回す）
- [ ] **Step 4: 2章を書く**（各グループの冒頭に、そのグループの到達目標を1行の通常文で書いてよい）
- [ ] **Step 5: 7〜9章へ追記する**（共通手順2-5・2-6・2-9）
- [ ] **Step 6: 合格基準を確かめる**（共通手順3）
- [ ] **Step 7: コミット**（メッセージ `vic3: チェックリストの開始直後・序盤の章を執筆`。手順は Task 2 Step 5 と同じ）

---

### Task 4: 3章「中盤」と4章「終盤」

**Files:**
- Modify: `vic3/vic3-play-checklist.md`（3・4章。必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: Task 3 で使った id（重複させない）と8章の用語
- Produces: 3章（20項目以内、`mid-`）、4章（15項目以内、`late-`）。1〜4章の合計は70項目以内（5章の枠を残すため）

- [ ] **Step 1: 着手前の確認**（共通手順0）
- [ ] **Step 2: 一次情報を集める**。特に `tutorial_lessons/` の `market_access`・`foreign_investment`・`company`・`form_power_bloc`・`declare_interest`・`start_diplomatic_play`・`subject_interactions`・`lobbies`・`institution_by_law`・`increase_immigration`、`country_ranks/00_country_ranks.txt`（列強の扱い）、`political_movements/`、1.14 で更新された `war_goal_types/`・`treaty_articles/`
- [ ] **Step 3: 3章を書く**（産業化・市場と貿易・政治改革・勢力拡大）
- [ ] **Step 4: 4章を書く**（列強の地位の維持、急進派・財政・戦争の崩れの予防）
- [ ] **Step 5: 7〜9章へ追記する**
- [ ] **Step 6: 合格基準を確かめる**（1〜4章の合計が70以内であることも書く）
- [ ] **Step 7: コミット**（メッセージ `vic3: チェックリストの中盤・終盤の章を執筆`）

---

### Task 5: 5章「定期ルーチン」と6章「困ったとき」

**Files:**
- Modify: `vic3/vic3-play-checklist.md`（5・6章。必要に応じて7〜9章へ追記）

**Interfaces:**
- Consumes: 1〜4章の内容（1回だけやることは5章に書かない）
- Produces: 5章（`###` で3〜4グループ、合計25項目以内、かつ1〜5章の合計が100以内）。グループ名と id 接頭辞は書き手が決めるが、設計書の目安「毎年／法律が成立したとき／新しい技術の時代に入ったとき／外交プレイ（戦争）の前と後」から外すときは理由を報告に書く。6章は8症状以内

- [ ] **Step 1: 着手前の確認**（共通手順0）
- [ ] **Step 2: 一次情報を集める**（6章は `alert_types/` の警告条件を主な根拠にする）
- [ ] **Step 3: 5章を書く**
- [ ] **Step 4: 6章を書く**。1症状は次の形にする（チェックボックスは使わない）

```markdown
**〈症状〉**
- 見る場所: 〈画面・指標〉
- 打ち手: 〈行動〉（根拠 `[src: …]` または（コミュニティ知見））
```

- [ ] **Step 5: 7〜9章へ追記する**
- [ ] **Step 6: 合格基準を確かめる**
- [ ] **Step 7: コミット**（メッセージ `vic3: チェックリストの定期ルーチン・困ったときの章を執筆`）

---

### Task 6: 7〜9章の仕上げ・全体の整合・用語表・ブラウザ確認

**Files:**
- Modify: `vic3/vic3-play-checklist.md`
- Modify: `vic3/localization-reference.md`（チェックリストで使う語のうち、1.14 で訳が変わっていた・載っていない語だけ）

Step 1〜4・6 は implementer、Step 5 はコントローラーが行う。

- [ ] **Step 1: 数値を突き合わせる**。`grep -nE '[0-9]' vic3/vic3-play-checklist.md` で1〜6章の数値を抜き出し、判断に使う数値が7章に同じ値であること、7章の全行に `[src:]` か（コミュニティ知見）があることを確かめる
- [ ] **Step 2: 用語を突き合わせる**。本文の用語がすべて8章にあり、8章の語がすべて本文で使われていること。8章の訳語が 1.14 の `concept_*` キーと一致すること。ずれている・無い語は `vic3/localization-reference.md` も直す（それ以外の行は触らない）
- [ ] **Step 3: 出典を突き合わせる**。本文の `[src:]` のファイルがすべて9章「一次情報」にあること。加えて、`[src:]` のファイル名ごとに `find "$G" -name <名前> | wc -l` を数え、2以上なのにパスなしで書いているものが0件であること（数えた一覧を報告に書く）
- [ ] **Step 4: 上限と検証**。`python scripts/check_checklist.py vic3/vic3-play-checklist.md` が `OK: 項目数 ≤100 / 文字数 ≤20000` を返すこと
- [ ] **Step 5: ブラウザで確かめる（コントローラー）**。repo 直下で `python -m http.server 8765` を起動し、Playwright で `http://localhost:8765/checklist.html?file=vic3/vic3-play-checklist.md&nocache=<時刻>` を開いて次を確かめる。結果とスクリーンショット1枚を残す
  - (a) チェックして再読込しても残る
  - (b) 全リセットとルーチンのリセットが、それぞれ対象だけを消す
  - (c) 出典トグルが効く
  - (d) 幅375pxで横スクロールが出ない。ダークモードで読める
  - (e) 先に EU5 のページで1項目チェックしておき、VIC3 側で全リセットしたあとも EU5 のチェックが残っている
  - (f) 1〜5章の流れに矛盾や重複がなく、1項目が2行を超えていない（通読）
- [ ] **Step 6: コミット**（メッセージ `vic3: チェックリストの数値表・用語・出典を整備`。用語表を直したら `vic3/localization-reference.md` も add する）

---

### Task 7: 3名レビュー

**Files:**
- Modify: `vic3/vic3-play-checklist.md`（指摘の反映）

- [ ] **Step 1: レビューを依頼する**。`reviewer` エージェントを3並列で起動する（読み取り専用。報告は返信の全文で受け、コントローラーが `_staging/2026-10-xx-vic3-checklist-review-<観点>.md` に保存する）。観点は repo の `CLAUDE.md`「レビュー」節のとおり
  - 熟練者: 行動の正しさ・時期の妥当性・抜け漏れ・1.14 ベータでの仕様（特に戦争目標・条約・利益団体）
  - プレイヤー（一通り遊んだが間が空くと忘れる人）: 項目だけ見て操作できるか、画面名・用語がゲーム内表記と一致するか
  - テクニカルライター: 書式・表記揺れ・1項目2行以内・7章の数値の再掲の一致

  3名に共通する依頼:
  - 冒頭で buildid を確かめる（共通手順0）
  - `[src:]` を最低10件、実際にファイルを開いて値と識別子を照合する
  - 国・文化・政体に固有の行動が混ざっていないか、DLC が要る項目に印が付いているかを見る
  - 指摘には重大度（critical / important / suggestion）と行番号を付ける
- [ ] **Step 2: 反映する**。critical と important はすべて反映する。suggestion は採否と理由を一覧にする。レビュアーの「直し方」を反映リストへ写す前に、根拠のスクリプト・ヒント原文を1回開き、前提条件が落ちていないかを確かめる。訂正した語句・数値ごとに `grep -n` でファイル全体を見て、旧値が残っていないことを確かめる
- [ ] **Step 3: 合格基準を確かめてコミット**（メッセージ `vic3: チェックリストに3名レビューの指摘を反映`）

---

### Task 8: 旧ファイルの削除・付随更新・マージ

**Files:**
- Delete（git 管理）: `vic3/vic3-japan-guide.md` `vic3/vic3-prussia-guide.md` `vic3/vic3-recommended-mods.md` `docs/superpowers/specs/2026-05-17-vic3-japan-guide-design.md` `docs/superpowers/plans/2026-05-17-vic3-japan-guide-plan.md`
- Delete（git 管理外・復元不可）: `vic3/_staging/`（8本）、Task 7 のレビュー結果 `_staging/2026-10-xx-vic3-checklist-review-*.md`
- Modify: `index.html`、`README.md`、`CHANGELOG.md`、`CLAUDE.md`、`docs/templates/guide-section-template.md`、`docs/procedures/new-country-guide.md`、`docs/templates/country-guide-plan-template.md`

- [ ] **Step 1: ビルドを確かめ直す**（共通手順0のコマンド）。25629520 から変わっていたら、`python scripts/check_checklist.py vic3/vic3-play-checklist.md` を再実行し、変わった旨と結果をユーザーに報告してから進む
- [ ] **Step 2: git 管理下のファイルを `git rm` で削除する**
- [ ] **Step 3: git 管理外のファイルを削除する**。消す前に `ls vic3/_staging _staging` の出力を報告に残し、`vic3/_staging/` が8本であることを確かめてから `rm` する
- [ ] **Step 4: `index.html` を直す**。VIC3 セクション（`<section class="game-section" data-game="vic3">` の `card-list`、現在 266〜295行の `<li>` 3枚）を2枚に置き換える。書き方は EU5 セクションの2枚と同じで、変える値は次のとおり
  - 1枚目: `href="checklist.html?file=vic3/vic3-play-checklist.md"`、タイトル「プレイ中チェックリスト」、説明「1.14 オープンベータ — どの国でも共通の「いつ・何をするか」」、タグ `tag--guide` 「攻略」
  - 2枚目: `href="viewer.html?file=vic3/localization-reference.md"`、タイトル「用語対照表」、説明「ゲーム内日本語訳と英語名の対照」、タグ `tag--guide` 「用語」
- [ ] **Step 5: `README.md` を直す**
  - 「### Victoria 3」節の勢力表と「おすすめMOD」の行を、EU5 節と同じ形の2行の表（プレイ中チェックリスト `1.14 オープンベータ`／用語対照表 `—`）に置き換える
  - 構成図の `vic3/` の説明を「Victoria 3 攻略（プレイ中チェックリスト＋用語対照表）」にする
  - 命名例 `vic3/vic3-prussia-guide.md` を外し、`ck3/ck3-england-1066-guide.md` だけにする
- [ ] **Step 6: `CLAUDE.md`（repo）を直す**
  - 4行目の模範例を `ck3/ck3-england-1066-guide.md` にする
  - 24行目の命名例から `vic3/vic3-prussia-guide.md` を外す
  - 26行目の直後に、VIC3 も国別ガイドを置かず `vic3/vic3-play-checklist.md` を正本とすること、書式は EU5 と同じであること、コミット前に `python scripts/check_checklist.py vic3/vic3-play-checklist.md` を通すこと（ゲームのフォルダはパスから自動で選ばれる）を書く
  - 129行目の直後に、VIC3 チェックリストもユーザーの指示で 1.14 オープンベータを基準にしており差分セクション方式の例外であること、再開のたびに `steamapps/appmanifest_529340.acf` の `buildid` を冒頭の表記と照合すること、安定版が出たら再検証することを書く
  - 259行目の例外の説明に、VIC3 のチェックリストも `checklist.html?file=vic3/vic3-play-checklist.md` 形式であることを足す
  - VIC3 の「ゲームスクリプト参照先」節は残す（日本固有ファイルの例もスクリプトの場所の説明として残す）
- [ ] **Step 7: テンプレート・手順書を直す**
  - `docs/templates/guide-section-template.md` 4行目と `docs/procedures/new-country-guide.md` 50行目の模範例を `ck3/ck3-england-1066-guide.md` にする
  - `docs/procedures/new-country-guide.md` 3行目と `docs/templates/country-guide-plan-template.md` 3行目の注意書きに、VIC3 も国別ガイドを置かない（`vic3/vic3-play-checklist.md` が正本）ことを足し、「CK3 / VIC3 の国別ガイド追加用」の言い方を CK3 用に直す
- [ ] **Step 8: 参照切れがないことを確かめる**

```bash
cd /c/Users/ramda/projects/paradox-game-guides && grep -rnE 'vic3-(japan-guide|prussia-guide|recommended-mods)' --include=*.md --include=*.html --include=*.py . | grep -vE '^\./CHANGELOG\.md:|^\./docs/superpowers/(specs|plans)/2026-03-31-recommended-mods|^\./docs/superpowers/(specs|plans)/2026-10-19-vic3-checklist'
```
Expected: 出力なし

- [ ] **Step 9: `CHANGELOG.md` の先頭に追記する**

```markdown
## 2026-10-xx VIC3 攻略をプレイ中チェックリストへ作り直し

### Added
- `vic3/vic3-play-checklist.md`: どの国でも共通の「いつ・何をするか」をまとめたチェックリスト（1.14 オープンベータ・ビルド 25629520 基準）。`checklist.html?file=vic3/vic3-play-checklist.md` で表示する

### Changed
- `scripts/check_checklist.py`: Markdown のパス（`eu5/`・`vic3/`）から検証するゲームのフォルダを自動で選ぶようにした
- テンプレートの模範例を `ck3/ck3-england-1066-guide.md` に差し替えた

### Removed
- 日本・プロイセンの国別ガイドと MOD 記事（git 履歴から復元可）
```

- [ ] **Step 10: 最終確認**

Run: `cd /c/Users/ramda/projects/paradox-game-guides && python -m unittest discover -s tests && python scripts/check_checklist.py vic3/vic3-play-checklist.md && python scripts/check_checklist.py eu5/eu5-play-checklist.md && git status --short`
Expected: テスト全件 OK、2つのチェックリストが `OK`、未コミットの変更なし（Step 11 のコミット後）

- [ ] **Step 11: コミット**（`git add -A` の前に `git status --short` で対象を確かめる → `git diff --cached --stat` → メッセージ `vic3: 旧ガイドを削除し、チェックリスト中心の構成へ切り替え`）
- [ ] **Step 12: マージと push（ユーザーの了承後）**。`git diff --stat main...vic3-checklist-reset` を示して了承を得てから、main へ `--no-ff` でマージして push する（push で GitHub Pages に即時公開される）。push 後、`https://ramdamain-commits.github.io/paradox-game-guides/checklist.html?file=vic3/vic3-play-checklist.md` が表示されることをコントローラーが Playwright で確かめる。あわせて root repo のサブモジュール参照をコミットする
