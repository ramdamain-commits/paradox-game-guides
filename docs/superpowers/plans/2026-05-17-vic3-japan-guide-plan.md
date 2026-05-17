# VIC3 日本攻略ガイド 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** VIC3 1.13 + DLC 時点の日本フルスペック攻略ガイド（550-700行、プロイセン版同構成 + 海軍ドクトリン独立セクション）を新規作成する。

**Architecture:** ドキュメント生成プロジェクト。researcher で DLC スクリプトを網羅調査 → staging レポート確定 → implementer 並列でセクション分担執筆 → reviewer 並列で網羅性検証 → 修正してコミット。2セッション分割（B方式）で進行。

**Tech Stack:** Markdown ドキュメント、PowerShell/Bash、subagent (researcher / implementer / reviewer)、Paradox VIC3 スクリプト (`C:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game/`)。

**Reference:**
- 設計書: `docs/superpowers/specs/2026-05-17-vic3-japan-guide-design.md`
- 既存ガイド（同構成参考）: `vic3/vic3-prussia-guide.md`
- 用語表: `vic3/localization-reference.md`
- プロジェクトルール: `CLAUDE.md`, `C:/Users/ramda/projects/CLAUDE.md`

---

## セッション1（今セッション）: 調査レポート確定

### Task 1: researcher 投入 → DLC スクリプト網羅レポート作成

**Files:**
- Create: `vic3/_staging/japan-research.md` (gitignore済、ローカルのみ)

- [ ] **Step 1: researcher サブエージェントを起動**

プロンプト要件:
```
あなたは VIC3 1.13 + DLC の日本固有メカニクスを調査する researcher です。

対象パス: C:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game/

調査範囲:
- events/ 配下: japan, meiji, shogunate, restoration を Glob で全件列挙
- common/journal_entries/ : *japan*, *meiji*, *shogunate*, *restoration* を grep
- common/decisions/ : 同上
- common/character_templates/JAP_* と日本人物テンプレ
- common/country_definitions/ : JAP 定義、tag swap (JAP→EOJ 等)
- common/scripted_modifiers/, common/static_modifiers/ : 日本固有
- common/laws/ : unrecognized, isolationism
- common/diplomatic_plays/, common/diplomatic_actions/ : 開国圧力・不平等条約系
- common/buildings/ : 日本専用建造物
- 海軍改修: common/military_formations/, common/combat_unit_*/, common/flotilla_*, common/coastal_*
- localization/japanese/, localization/english/ : 用語の正式表記

最初に EU4 派生キーワード除外 grep を実行:
fabricate_claim, forge_claim, spy_network, 領有権主張捏造, 理念グループ,
交易ノード, Tariff, Liberty Desire, 関税

報告規約:
- 行番号付きで該当ファイルパスを明示
- 推測禁止、不在は「不在」と明記
- 出力先は paradox-game-guides/vic3/_staging/japan-research.md (Write ツールで直書き)
- 完了報告は要約 200 字のみ（ファイル全文転記禁止）

章立て (staging ファイル内):
1. 1.13/DLC 日本関連 changelog 要約
2. 明治維新 JE（前提条件・期限・報酬・分岐）
3. 開国・不平等条約フロー（イベント連鎖・modifier）
4. 日本固有 IG とプロミネンス挙動
5. 海軍改修の構造変更点（旧→新の差分。1.12以前のテンプレと比較できない場合は現状記述のみ）
6. 主要人物テンプレ（徳川慶喜・明治天皇・西郷ほか）
7. 開始 modifier・建造物・法律で日本固有のもの一覧
8. EU4 派生メカニクス除外 grep の結果（不在キーワード列挙）

想定文字数: 5000-8000 字
```

呼び出し: subagent_type=researcher で 1 並列 (情報統合性のため複数並列にしない)。

- [ ] **Step 2: staging ファイルの存在確認**

```bash
ls -la C:/Users/ramda/projects/paradox-game-guides/vic3/_staging/japan-research.md
wc -c C:/Users/ramda/projects/paradox-game-guides/vic3/_staging/japan-research.md
```

期待: ファイル存在、5000-15000 バイト程度。

- [ ] **Step 3: 章立て網羅チェック (grep)**

```bash
grep -c "^## " C:/Users/ramda/projects/paradox-game-guides/vic3/_staging/japan-research.md
grep "^## " C:/Users/ramda/projects/paradox-game-guides/vic3/_staging/japan-research.md
```

期待: 8章すべて存在 (changelog / 明治維新JE / 開国 / IG / 海軍 / 人物 / modifier等 / EU4除外grep)。欠落あれば researcher に追加投入。

- [ ] **Step 4: 行番号付き出典チェック**

```bash
grep -cE ":[0-9]+" C:/Users/ramda/projects/paradox-game-guides/vic3/_staging/japan-research.md
```

期待: 20件以上 (主要メカニクスに最低1件ずつ)。少なすぎる場合は researcher に「行番号必須」で再投入。

### Task 2: spec + plan をコミット & push

**Files:**
- Modify: `paradox-game-guides/docs/superpowers/specs/2026-05-17-vic3-japan-guide-design.md` (作成済)
- Modify: `paradox-game-guides/docs/superpowers/plans/2026-05-17-vic3-japan-guide-plan.md` (本ファイル)

- [ ] **Step 1: git status 確認**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && git status
```

期待: spec + plan 2ファイルが untracked、_staging/japan-research.md は .gitignore で表示されない。

- [ ] **Step 2: _staging が gitignore でカバーされているか確認**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && git check-ignore -v vic3/_staging/japan-research.md
```

期待: `.gitignore` の `_staging/` 行が出力される。出ない場合は `.gitignore` に `vic3/_staging/` を追記して別コミット。

- [ ] **Step 3: コミット**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
git add docs/superpowers/specs/2026-05-17-vic3-japan-guide-design.md \
        docs/superpowers/plans/2026-05-17-vic3-japan-guide-plan.md && \
git commit -m "docs: VIC3 日本攻略ガイド 設計書+実装計画 (B方式 セッション1)"
```

- [ ] **Step 4: push**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && git push
```

- [ ] **Step 5: root repo でサブモジュール参照を更新**

```bash
cd C:/Users/ramda/projects && git status
cd C:/Users/ramda/projects && git add paradox-game-guides && \
git commit -m "chore: paradox-game-guides サブモジュール参照更新 (VIC3 日本ガイド設計)"
cd C:/Users/ramda/projects && git push
```

---

## セッション2（次セッション）: 本体執筆

### Task 3: ガイド本体スケルトン作成（海軍以外）

**Files:**
- Create: `vic3/vic3-japan-guide.md`
- Reference (read-only): `vic3/_staging/japan-research.md`, `vic3/vic3-prussia-guide.md`

- [ ] **Step 1: implementer サブエージェント (1並列) でスケルトン作成**

プロンプト要件:
```
あなたは VIC3 日本攻略ガイドのスケルトンを書く implementer です。

参考:
- vic3/vic3-prussia-guide.md (既存、同構成)
- vic3/_staging/japan-research.md (DLC 調査レポート)

作成: vic3/vic3-japan-guide.md

含めるセクション (この時点では見出しと1-2文の概要のみ。本文は後続タスク):
- # VIC3 日本攻略ガイド（Patch 1.13 + DLC 時点）
- ## パッチ 1.13 / DLC での日本関連変更点
- ## 開始状況（1836年）
  - ### 周辺国との関係
  - ### 初期の強み・弱み
  - ### IG構造の特殊性（幕府/藩/学者）
- ## 開国の肋（Unrecognized脱却・不平等条約・関税）
- ## Day 1（ポーズ解除直後）
- ## 時系列戦略
  - ### 序盤（1836〜1860）
  - ### 中盤（1860〜1880）
  - ### 終盤（1880〜1936）
- ## 内政・経済
  - ### 建設の優先順位
  - ### 利益団体（IG）管理
    - #### プロミネンスの活用（1.13）
  - ### 法律改正ロードマップ
- ## 外交・同盟
  - ### 必須外交
  - ### Unrecognized → Recognized 昇格ルート
  - ### 1.13 で増えた外交手段
- ## 軍事ドクトリン（陸軍）
  - ### 将軍の選び方（1.13 単一指揮官制）
- ## 海軍ドクトリン（1.13 海軍改修） ← 別タスクで埋めるため <!-- TBD: Task 4 --> プレースホルダ可
- ## 固有イベント時系列
  - ### 明治維新JE 攻略チャート
- ## 技術・法律
- ## よくあるミス
- ## 用語対照表
- ## 出典

完了報告は要約 200 字のみ。
```

- [ ] **Step 2: スケルトン構造確認**

```bash
grep -c "^##\|^###\|^####" C:/Users/ramda/projects/paradox-game-guides/vic3/vic3-japan-guide.md
```

期待: 24見出し以上 (## 14 + ### 9 + #### 1)。

### Task 4: 本体セクション執筆 implementer 並列（海軍以外）

**Files:**
- Modify: `vic3/vic3-japan-guide.md`

実装サブエージェントを 3 並列で起動し、セクションを担当分割する。

- [ ] **Step 1: implementer A 起動 — 開始状況〜Day 1**

担当範囲:
- パッチ 1.13 / DLC での日本関連変更点
- 開始状況（1836年）全体（IG構造特殊性含む）
- 開国の肋
- Day 1

参考: `_staging/japan-research.md` の章 1, 3, 4, 7。出典は行番号付きで本文末尾の「出典」セクションに集約 (フォーマットはプロイセン版踏襲)。完了報告は200字。

- [ ] **Step 2: implementer B 起動 — 時系列戦略〜内政**

担当範囲:
- 時系列戦略 (序盤/中盤/終盤)
- 内政・経済 (建設/IG管理/プロミネンス/法律改正ロードマップ)

参考: `_staging/japan-research.md` の章 2 (明治維新JE), 4, 7。維新前/維新後の分岐を法律改正セクションで明示。

- [ ] **Step 3: implementer C 起動 — 外交〜よくあるミス（陸軍含む、海軍除く）**

担当範囲:
- 外交・同盟 (必須外交 / Unrecognized→Recognized / 1.13 増分)
- 軍事ドクトリン（陸軍）
- 固有イベント時系列 (明治維新JE 攻略チャート含む)
- 技術・法律
- よくあるミス

参考: `_staging/japan-research.md` の章 2, 3, 6, 8。明治維新JE 攻略チャートは表形式（前提条件 / 達成期限 / 分岐 / 報酬の4列）。

- [ ] **Step 4: 3並列完了後、本文差分確認**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && wc -l vic3/vic3-japan-guide.md
```

期待: 400-550 行 (海軍ドクトリン未執筆状態)。

- [ ] **Step 5: コミット境界 1（海軍以外の本体執筆）**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
git add vic3/vic3-japan-guide.md && \
git commit -m "docs: VIC3 日本攻略ガイド 本体執筆 (海軍除く)"
```

### Task 5: 海軍ドクトリン執筆

**Files:**
- Modify: `vic3/vic3-japan-guide.md` (## 海軍ドクトリン セクション)

- [ ] **Step 1: implementer 1並列で海軍ドクトリン執筆**

プロンプト要件:
```
あなたは VIC3 1.13 海軍改修を反映した日本ガイドの海軍ドクトリンセクションを書く implementer です。

参考: vic3/_staging/japan-research.md の章 5 (海軍改修の構造変更点)。

対象ファイル: vic3/vic3-japan-guide.md
位置: ## 海軍ドクトリン（1.13 海軍改修） セクション
想定行数: 200-300行
重要: 1.12 以前の構造を流用しない。research レポートで「現状不在」とされた要素は記述しない。

含める内容:
- 1.13 海軍改修の構造変更点 (旧 vs 新)
- 艦隊編成 (flotilla / formation の単位、ユニット種別)
- 製造拠点 (該当 building、location_potential 条件、日本のどの州が適合するか)
- 進出ルート (序盤の沿岸防衛 → 中盤の対清・対朝 → 終盤の太平洋進出)
- 1.13 の指揮官制との関係（提督の運用、単一指揮官制の海軍適用範囲）
- 日本固有の海軍 modifier / decision がある場合は明示

完了報告は 200 字。
```

- [ ] **Step 2: 海軍セクション行数確認**

```bash
sed -n '/^## 海軍ドクトリン/,/^## /p' C:/Users/ramda/projects/paradox-game-guides/vic3/vic3-japan-guide.md | wc -l
```

期待: 200-300 行。

- [ ] **Step 3: コミット境界 2（海軍ドクトリン）**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
git add vic3/vic3-japan-guide.md && \
git commit -m "docs: VIC3 日本ガイド 海軍ドクトリンセクション執筆 (1.13 改修反映)"
```

### Task 6: reviewer 並列で網羅性チェック

**Files:**
- Read-only: `vic3/vic3-japan-guide.md`
- Reference: `vic3/_staging/japan-research.md`

3 並列で章単位分割（行番号均等ではなく検証ポイント均等で分割）。

- [ ] **Step 1: ガイドの行範囲を確認し、章単位で 3 グループに分割**

```bash
grep -n "^## " C:/Users/ramda/projects/paradox-game-guides/vic3/vic3-japan-guide.md
```

検証密度を考慮した分割例:
- Reviewer A: パッチ変更点 + 開始状況 + 開国の肋 + Day 1
- Reviewer B: 時系列 + 内政・経済 + 外交・同盟
- Reviewer C: 軍事 + 海軍 + 固有イベント + 技術・法律 + よくあるミス + 用語表 + 出典

- [ ] **Step 2: reviewer 3並列起動**

各 reviewer の指示テンプレート:
```
あなたは VIC3 日本ガイドのレビュアーです。担当範囲: [行N1-N2]

検証項目:
1. EU4 派生メカニクス混入チェック (fabricate_claim, forge_claim, spy_network,
   領有権主張捏造, 理念グループ, 交易ノード, Tariff, Liberty Desire, 関税)
2. 1.12 以前の海軍構造混入チェック (research レポートの「現状不在」項目)
3. _staging/japan-research.md と本文の整合 (行番号出典の妥当性)
4. プロイセン版 (vic3/vic3-prussia-guide.md) との構成整合
5. 用語の揺れ (例: 「明治維新JE」と「明治維新ジャーナル」が混在していないか)
6. 数値・期限・前提条件の出典なし箇所

報告形式 (必須):
- 行番号: 一行要約 (1問題1行)
- 全文転記禁止
- critical / warning / suggestion を先頭マーカーで明示

例:
[critical] 行234: fabricate_claim が混入 (VIC3 不在)
[warning] 行456: 出典の行番号が貼られていない
[suggestion] 行678: 用語「藩」と「Daimyo」が同節で混在

完了報告は 200 字。
```

- [ ] **Step 3: 3並列のレビュー結果を `_staging/review-{a,b,c}.md` に保存** (各 reviewer に直書きさせる)

- [ ] **Step 4: critical / warning 件数確認**

```bash
grep -cE "^\[critical\]|^\[warning\]" \
  C:/Users/ramda/projects/paradox-game-guides/vic3/_staging/review-a.md \
  C:/Users/ramda/projects/paradox-game-guides/vic3/_staging/review-b.md \
  C:/Users/ramda/projects/paradox-game-guides/vic3/_staging/review-c.md
```

### Task 7: レビュー結果に基づく修正

**Files:**
- Modify: `vic3/vic3-japan-guide.md`

- [ ] **Step 1: implementer 1並列で修正**

プロンプト:
```
あなたは VIC3 日本ガイドの修正担当 implementer です。

修正対象: vic3/vic3-japan-guide.md
指示書: vic3/_staging/review-a.md, review-b.md, review-c.md を全件読み、
critical を最優先、warning を次に、suggestion は時間内で対応してください。

参考: vic3/_staging/japan-research.md (元の調査レポート)

完了報告は 200 字。修正箇所を「行番号: 修正サマリ」形式で列挙。
```

- [ ] **Step 2: 修正後の本文行数確認 + EU4 派生キーワード再 grep**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
  wc -l vic3/vic3-japan-guide.md && \
  grep -cE "fabricate_claim|forge_claim|spy_network|理念グループ|交易ノード|Liberty Desire" \
       vic3/vic3-japan-guide.md
```

期待: 行数 550-700、EU4 派生キーワード grep カウント 0。

- [ ] **Step 3: コミット境界 3（レビュー修正）**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
git add vic3/vic3-japan-guide.md && \
git commit -m "docs: VIC3 日本ガイド レビュー指摘反映 (critical/warning 対応)"
```

### Task 8: localization-reference.md 更新

**Files:**
- Modify: `vic3/localization-reference.md`

- [ ] **Step 1: 既存 localization-reference の構造確認**

```bash
head -30 C:/Users/ramda/projects/paradox-game-guides/vic3/localization-reference.md
grep "^## \|^### " C:/Users/ramda/projects/paradox-game-guides/vic3/localization-reference.md
```

- [ ] **Step 2: implementer 1並列で日本関連用語追記**

プロンプト:
```
vic3/localization-reference.md に日本関連用語セクションを追記。

参考:
- vic3/_staging/japan-research.md (loc 章)
- localization/japanese/, localization/english/ の日本関連 .yml

追加対象:
- 明治維新JE 名 (英/日)
- 海軍ユニット改名 (1.13 で変更されたもの)
- 不平等条約 modifier 名
- 日本固有 IG 名
- 日本固有 decision / law 名

既存セクションの記述スタイル踏襲。完了報告は 200 字。
```

- [ ] **Step 3: コミット境界 4（localization 更新）**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
git add vic3/localization-reference.md && \
git commit -m "docs: localization-reference に VIC3 日本関連用語追記"
```

### Task 9: CHANGELOG / README 更新

**Files:**
- Modify: `paradox-game-guides/CHANGELOG.md`
- Modify: `paradox-game-guides/README.md` (VIC3 ガイド一覧があれば)
- Modify: `paradox-game-guides/vic3/README.md` (存在する場合)

- [ ] **Step 1: README 構造確認**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
  head -50 README.md && \
  [ -f vic3/README.md ] && head -30 vic3/README.md
```

- [ ] **Step 2: CHANGELOG に新規エントリ追加 (日付セクション)**

```markdown
## 2026-05-XX (執筆完了日)

- 新規: vic3/vic3-japan-guide.md (VIC3 1.13 + DLC 日本攻略フルスペックガイド)
- 更新: vic3/localization-reference.md に日本関連用語追記
```

- [ ] **Step 3: README にガイド一覧があれば日本ガイドを追加**

- [ ] **Step 4: コミット境界 5（CHANGELOG/README）**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
git add CHANGELOG.md README.md vic3/README.md 2>/dev/null && \
git commit -m "docs: VIC3 日本ガイド 公開準備 (CHANGELOG / README 更新)"
```

- [ ] **Step 5: push & サブモジュール参照更新**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && git push
cd C:/Users/ramda/projects && \
  git add paradox-game-guides && \
  git commit -m "chore: paradox-game-guides サブモジュール参照更新 (VIC3 日本ガイド完成)" && \
  git push
```

### Task 10: 学びを CLAUDE.md に追記（必要なら）

**Files:**
- Modify: `paradox-game-guides/CLAUDE.md` (学びが出た場合のみ)

- [ ] **Step 1: セッション中に出た学びを列挙**

例:
- VIC3 と EU5 のスクリプト構文差分で詰まった点
- DLC 関連 grep の落とし穴
- 海軍改修の旧構造を見落とした事例

- [ ] **Step 2: 該当する学びを CLAUDE.md の既存セクションに追記**

- [ ] **Step 3: コミット**

```bash
cd C:/Users/ramda/projects/paradox-game-guides && \
git add CLAUDE.md && \
git commit -m "docs: CLAUDE.md に VIC3 ガイド執筆時の学び追記" && \
git push
cd C:/Users/ramda/projects && \
  git add paradox-game-guides && \
  git commit -m "chore: paradox-game-guides サブモジュール参照更新 (CLAUDE.md 更新)" && \
  git push
```

---

## トークン安全策（全タスク共通）

- サブエージェント並列は最大 3
- レビュアー指示は「行番号+一行要約のみ、ファイル全文転記禁止」必須
- staging ファイルはサブエージェントに直書きさせ、メイン側で中間整形しない
- 1セッション 2バッチ上限（CLAUDE.md ルール）。Task 3+4 が1バッチ、Task 5+6+7 が1バッチ、Task 8+9+10 は次バッチに繰り越し可
- API 上限到達時: git status で完了済み分を確認 → コミット & push で checkpoint → 別セッションで再投入

## 成功基準（spec から再掲）

- スクリプト由来の記述すべてに行番号付き出典が紐づく
- EU4 派生メカニクス grep が本文で 0 件
- 海軍ドクトリンが 1.13 改修後の構造で書かれている
- 明治維新JE の前提・期限・分岐・報酬が表で参照可能
- プロイセン版と同じセクション順
- 想定行数 550-700 行
