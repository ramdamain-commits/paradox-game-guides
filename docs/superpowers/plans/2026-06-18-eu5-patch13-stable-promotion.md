# EU5 1.3 安定版 昇格計画（全メニュー 1.3 化）

> **For agentic workers:** REQUIRED SUB-SKILL: 実装時は superpowers:executing-plans または superpowers:subagent-driven-development を使い、タスク単位で進める。Steps はチェックボックス（`- [ ]`）で追跡する。
> **着手トリガー（重要）:** 本計画は **EU5 1.3 が安定版（live / デフォルトブランチ）としてリリースされてから**着手する。それまでは現状（1.2 baseline 無傷 ＋ 各ガイドに「1.3 オープンベータ差分」純追記）で凍結。beta のまま昇格してはいけない。

**Goal:** 1.3 が正式版になった時点で、現在「1.3 オープンベータ差分」セクションとして各ガイドに**純追記**してある内容を本文へ統合し、ガイド群（＝index.html メニューの全 EU5 カード）の基準パッチを 1.2 → 1.3 に正式昇格する。beta マーカー（`（1.3 beta）` / `（コミュニティ知見：1.3 beta…）`）を安定版マーカーへ格上げし、差分セクションを解体する。

**Architecture:** 既存の純追記方式（案A）を逆回しする「昇格フロー」。差分セクション内で隔離してきた 1.3 情報を、各ガイドの該当本体章へ溶かし込み、暫定マーカーを正式マーカーに置換し、差分セクション・仮登録用語表・beta バッジを削除する。最後に汎用用語を中央 `localization-reference.md` に昇格。**beta→安定版で数値が変わりうるため、本文統合の前に全数値を安定版スクリプト/ノートで再検証する「プリフライト」を必須前段に置く。**

**Tech Stack:** Markdown、Bash/PowerShell（grep 検証）、subagent（researcher / implementer / reviewer、model: sonnet 固定）、EU5 安定版スクリプト（`C:/Program Files (x86)/Steam/steamapps/common/Europa Universalis V/game/in_game/`）。

**Reference:**
- 設計書（案A・確定表）: `docs/superpowers/specs/2026-06-16-eu5-patch13-update-design.md`
- spec の「昇格フロー」: 同 spec section 0「昇格フロー（1.3安定版リリース後）」
- 詳細レビュー成果物: `_staging/review-{accuracy,coverage,strategy}.md`（gitignore・残っていれば）
- プロジェクトルール: `CLAUDE.md`, `C:/Users/ramda/projects/CLAUDE.md`, `.claude/docs/tool-constraints.md`

---

## 昇格対象インベントリ（着手時点の現状）

「1.3 オープンベータ差分」セクションを持つ **11 ガイド = index.html の全 EU5 カード**:

| ガイド | 1.3 beta マーカー数(目安) | 主な 1.3 内容（差分セクション） |
|--------|------|------|
| universal | 9 | 経済(建物維持費逓増/利益率/mills半減/交易範囲scale)・海軍/軍事(船コスト4x金10x goods/陸軍goods2倍/正規vs徴募ダメボ撤廃/個別ユニット兵科再分類)・諜報網fog(政府への潜入=1.2既存の注意付)・自動化・宮廷芸術家12種 |
| government | 18 | 身分の文化宗教・官僚制10種・低Devotion/低Republican Tradition ペナルティ・Prikazi/Collegium 0.10・Voivode・退位コスト・宮廷芸術家廷臣管理 |
| religion | 6 | 身分の宗教・枢機卿+1%聖職者満足・低Devotion・バーガー同化hard-block撤廃→超低速・Papacy→Lutheran議会バグ修正（Patriarch/Rite Power は1.2変更=対象外） |
| byzantium | 12 | 反ジェノヴァ盟約・Born in the Purple・1337国境修正・ジェノヴァ弩兵軽歩兵化・船コスト/海戦致死性・Twilight of the Tsardom |
| regional | 20 | 百年戦争リバランス・薔薇戦争・ゲルフ/ギベリン改修・Taula de Canvi・Twilight/Voivode・RGO再分配・植民移民拡大・新文化(6種・種別保留)・天然痘亜熱帯化(0.05/0.15/subtropical)・Korea集賢殿ナーフ |
| ottoman | 3 | 船コスト/維持費/陸軍goods/海戦致死性・Twilight流動化（＋更新優先度Tier2メモ） |
| hungary | 5 | 陸軍goods2倍=黒軍直撃・Union of Crowns女性継承・no_female_heirs_for_poland例外 |
| austria | 3 | 従属国への宗教統一強制不可・HRE加入reluctance・土地剥奪集権・Twilight |
| brandenburg | 5 | HRE皇帝メカ・Voivode・Berenberg=HAM固有(非該当注記) |
| castile | 3 | 船コスト(植民艦隊)・経済・植民/新文化・Taula=アラゴン固有(非該当注記) |
| recommended-mods | — | MOD互換注記（※本文統合ではなく「対応パッチ列を1.3に更新」が昇格） |

- index.html の `tag--beta">1.3 beta差分` バッジ = **11 個**（着手時に再カウントすること）。
- `localization-reference.md` には現状 1.3 用語の登録なし（中央昇格は純増）。

---

## フェーズ 0（前段・必須）: プリフライト = 安定版での全数値再検証

> beta→安定版でリバランス値が変わるのが常。**本文統合の前に必ず**、差分セクションの全クレームを安定版スクリプト/パッチノートで再確認する。spec section 1 の「数値検証の最終ステータス」表を安定版で再走査する。

### Task 0-1: 安定版ブランチ確認とバージョン固定
- [ ] Steam で 1.3 が beta でなく live になったことを確認（`eu5.paradoxwikis.com/Patches`／ゲーム内バージョン表示／buildid）。1.3.x の最終 hotfix 版を基準に固定する。
- [ ] spec の検証基準行（buildid 23683141 / `1.3-open-beta`）を、確定した安定版 buildid に差し替える。

### Task 0-2: script 実値クレームの再 grep（researcher 委任可）
- [ ] `[src:…]（1.3 beta）` 付きの全クレームを安定版スクリプトで再確認。特に load-bearing:
  - `diseases/smallpox.txt`（spawn 0.05 / threshold 0.15 / subtropical）
  - `government_reforms/country_specific.txt`（Prikazi/Collegium 0.10・Voivode）
  - `artist_types/00_default.txt`（宮廷芸術家=beta では12種。安定版で再カウント）
  - `bureaucracies/`（官僚制 generic 10種を再カウント）
  - `unit_types/1_uniques_for_age_2_renaissance.txt`（ジェノヴァ弩兵軽歩兵化の行番号）
  - `heir_selections/monarchy.txt`（`no_female_heirs_for_poland`・行番号）
  - `events/DHE/flavor_ARA.txt`（Taula `flavor_ara.220`）・`flavor_KOR.txt`（Hall of Worthies）・`flavor_HAM.txt`（Berenberg）
  - `disasters/twilight_of_the_tsardom.txt` / `disasters/war_of_the_roses.txt` / `situations/{hundred_years_war,guelphs_and_ghibellines}.txt`
- [ ] 行番号がズレていたら識別子優先で更新。**実体が消えた/改名された項目は記録**（昇格せず削除 or 文言修正）。

### Task 0-3: changelog 由来値（エンジン内部）の安定版ノート突き合わせ
- [ ] 船コスト4x金/10x goods・建物維持費+50%・陸軍goods2倍・利益率/mills半減・正規vs徴募ダメボ撤廃・海戦致死性 を **1.3 安定版パッチノート**で再確認。beta から数値変更があれば反映。1.3.x hotfix での再調整に注意。
- [ ] 結果を `_staging/2026-XX-XX-eu5-13-stable-reverify.md` に「クレーム / beta値 / 安定版値 / 差異 / 対応」で一覧化（後続 implementer の入力にする）。

**プリフライト完了をコミット境界とする**（本文はまだ無変更）。

---

## フェーズ 1: 各ガイドの本文統合 + マーカー昇格 + 差分セクション解体

> 各ガイドで spec の昇格フロー ①〜⑥ を実行する:
> ① 差分ブロックの各項目を該当本体章へ統合 → ② マーカー昇格（`（1.3 beta）`→`[src:…]`／`（コミュニティ知見：1.3 beta…）`→`（コミュニティ知見）` か script 化）→ ③「1.3 オープンベータ差分」セクション削除 → ④ パッチ差分テーブルに「Patch 1.3」行追記 → ⑤ 仮登録用語表を本体の用語対照表へ溶かす → ⑥ ヘッダのパッチ版・確認日を 1.3 に更新。
>
> **委任方針（CLAUDE.md 準拠）:** implementer に最大3並列で委任。各 implementer に「担当ガイドのみ編集／本体章の既存記述を壊さない／プリフライト staging の確定値を使う／用語表・出典は担当ガイド内で完結」を明示。レビューは reviewer 3並列で「行番号+一行要約のみ報告」。

### Task 1-1: 横断系3ガイド（universal / government / religion）
- [ ] **universal**: 経済・海軍/軍事・諜報・自動化・宮廷芸術家を本体の該当章（内政/経済・軍事ドクトリン・諜報・廷臣）へ統合。「政府への潜入=1.2既存」の切り分け注記は本文側にも残す。差分セクション削除・パッチ差分に Patch 1.3 行・ヘッダ更新。
- [ ] **government**: 身分の文化宗教・官僚制・各ペナルティ・Prikazi/Collegium 0.10・Voivode・退位コスト・宮廷芸術家廷臣を政体別章へ統合。
- [ ] **religion**: 身分の宗教・枢機卿・低Devotion・バーガー同化・Papacy→Lutheran修正を宗教章へ統合。**Patriarch/Rite Power は1.2変更なので触らない**。

### Task 1-2: regional + byzantium（相互参照あり・同時/隣接タスク）
- [ ] **regional**: 西欧/イタリア/イベリア/東欧バルカン/各地域/概要・東アジア の 1.3 ノードを、対応する各地域節の本文へ統合。Twilight/Voivode の被リンクを byzantium/austria/brandenburg と整合させたまま昇格。
- [ ] **byzantium**: 外交継承国境・海軍・Twilight を本体章へ統合。regional 側の Twilight 記述（昇格後の位置）への相互リンクを張り直す。

### Task 1-3: 国別4ガイド（ottoman / hungary / austria / brandenburg / castile）
- [ ] **ottoman**: 船コスト/維持費/陸軍goods/海戦/Twilight を海軍・貿易・内政・外交章へ統合。**「更新優先度Tier2メモ」は昇格時に削除**（運用メモであり本文ではない）。難易度評価（regional の ★★★）も 1.3 のコスト増を踏まえ再評価。
- [ ] **hungary**: 陸軍goods=黒軍直撃を軍事章へ、Union of Crowns 女性継承＋`no_female_heirs_for_poland` 例外を継承/外交章へ統合。例外注記は**必ず残す**（A-7）。
- [ ] **austria**: 宗教統一強制不可・HRE reluctance・土地剥奪を HRE 運営/宗教章へ統合。
- [ ] **brandenburg**: HRE皇帝メカ・Voivode(東隣ポーランド)を統合。**Berenberg=HAM固有の非該当注記は残す**（A-5・誤帰属再発防止）。
- [ ] **castile**: 船コスト/経済/植民/新文化を海軍・経済章へ統合。**Taula=アラゴン固有(regional)の非該当注記は残す**。

### Task 1-4: recommended-mods（昇格＝対応パッチ列更新）
- [ ] 「1.3 オープンベータでのMOD互換性」節を「1.3 でのMOD互換性」に格上げ。MOD表の「対応パッチ」列（現状 1.1.x 基準）を 1.3 動作確認ベースに更新（各 Workshop の 1.3 対応状況を確認）。ヘッダのパッチ版を更新。

**各ガイドの統合をコミット境界に揃える**（CLAUDE.md: staging 結合タイミング＝コミット境界）。1セッション2バッチ上限のため、横断3＋regional/byz で1〜2セッション、国別＋mods で1セッションが目安。

---

## フェーズ 2: 中央 localization-reference 昇格 + index.html 更新

### Task 2-1: localization-reference.md 中央昇格
- [ ] spec Tier4 の中央昇格候補のうち **汎用語のみ**を `eu5/localization-reference.md` へ正式登録（CLAUDE.md: 汎用語＝HRE系/PU系/CB系/兵科系のみ中央、勢力固有は本体のみ）:
  - 中央へ: Voivode（政府改革・汎用）、身分の文化/宗教（汎用メカニクス）、宮廷芸術家（汎用）、Mamluk Horsemen（兵科・汎用）、Twilight of the Tsardom（地域跨ぎ）、家族銀行（Berenberg/Taula は「家族/公営銀行」概念として汎用見出し化、固有名は本体）。
  - 本体のみで完結: no_female_heirs_for_poland（hungary）、集賢殿（regional/Korea）、薔薇戦争・百年戦争・ゲルフ/ギベリン（地域固有寄り）。
- [ ] 各ガイドの「1.3 オープンベータ用語（仮登録）」表は、本体用語対照表に溶かしたうえで**仮登録という枠を削除**し、完全版（localization-reference）への参照に一本化。

### Task 2-2: index.html
- [ ] `tag--beta">1.3 beta差分` バッジを**全 11 個削除**（着手時に再カウント）。`.tag--beta` の CSS 定義は将来のため残してよい。
- [ ] 各 EU5 カードの `card__meta` のパッチ表記（現状 "Patch 1.1.10" / "Patch 1.2" 等）を **"Patch 1.3"** に統一更新。

---

## フェーズ 3: 検証 + 仕上げ

### Task 3-1: 整合スイープ（grep）
- [ ] `grep -rn "（1.3 beta）\|1.3 オープンベータ\|仮登録\|tag--beta" eu5/ index.html` が**0件**になることを確認（差分セクション・暫定マーカー・バッジの残存ゼロ）。
- [ ] 各ガイド冒頭のパッチ版・確認日が 1.3 になっているか確認。`grep -rn "Patch 1.2 時点\|1.2「Echinades」" eu5/` で旧版表記の取り残しを検出。
- [ ] 被リンク（regional⇔byzantium/austria/brandenburg、universal/government への参照）が昇格後の見出し位置を指しているか確認。

### Task 3-2: レビュー（reviewer 3並列・行番号+一行要約のみ）
- [ ] 正確性（安定版スクリプト整合）／網羅性（差分項目の取りこぼし無し）／構成（差分セクション解体後の章構成の自然さ）。

### Task 3-3: CHANGELOG + コミット + push + root submodule
- [ ] `CHANGELOG.md` に「EU5 1.3 安定版へ昇格（差分セクション統合・本文昇格・中央用語登録・betaバッジ除去）」エントリ。
- [ ] paradox-game-guides を push、root repo でサブモジュール参照を更新（CLAUDE.md）。
- [ ] MEMORY.md / projects.json 等のプロジェクト状態は `/session-end` の更新順序（projects.json 起点）で反映。

---

## リスク・注意点

- **数値変動リスク（最重要）**: beta の changelog 由来値（船コスト4x/10x 等）は安定版で再調整されることがある。フェーズ0を飛ばして本文統合すると、誤値が baseline に昇格して取り返しがつかない。**プリフライト必須**。
- **「1.3新規か否か」の再判定**: 一部項目は安定版で 1.2 へバックポートされたり撤回されたりしうる。spec section 1 の真正性判定（1.2/1.3 ノート差分）を安定版ノートで取り直す。
- **誤帰属注記は昇格後も残す**: Berenberg=HAM固有 / Taula=アラゴン固有 / 政府への潜入=1.2既存。これらは「やらない理由」の記録なので削除しない。
- **本体無変更ルールの終了**: 昇格フェーズでは初めて 1.2 本体章を改変する。`git diff --stat` で想定外の章への波及がないか各コミット前に確認。
- **トークン**: 84+マーカー×11ガイドの本文統合は重い。implementer 並列＋staging 直書き＋「行番号+要約のみ報告」で抑える。1セッション2バッチ上限を守り、3〜4セッションに分割する前提。
