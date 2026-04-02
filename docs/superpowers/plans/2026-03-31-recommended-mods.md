# おすすめMOD記事 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** EU5 / VIC3 / CK3 の3タイトルについてキュレーション型おすすめMOD記事を作成する

**Architecture:** 各タイトル1ファイル（`{game}/{game}-recommended-mods.md`）。カテゴリ別テーブル形式。全MODに「コミュニティ知見」マーカーを冒頭で一括宣言。更新停滞MODには警告付き。

**Tech Stack:** Markdown（既存ガイドと同一形式）

**Spec:** `docs/superpowers/specs/2026-03-31-recommended-mods-design.md`

---

## ファイル構成

| 操作 | ファイルパス | 内容 |
|------|-------------|------|
| Create | `eu5/eu5-recommended-mods.md` | EU5 おすすめMODガイド（8 MOD / 4カテゴリ） |
| Create | `vic3/vic3-recommended-mods.md` | VIC3 おすすめMODガイド（7 MOD / 4カテゴリ） |
| Create | `ck3/ck3-recommended-mods.md` | CK3 おすすめMODガイド（10 MOD / 6カテゴリ） |

---

### Task 1: EU5 おすすめMODガイド作成

**Files:**
- Create: `eu5/eu5-recommended-mods.md`
- Reference: `eu5/localization-reference.md`（用語確認用）
- Reference: `eu5/eu5-hungary-guide.md`（トーン・形式の参考）

**重要コンテキスト（サブエージェント向け）:**

このタスクは Markdown 記事の新規作成。コードではなくコンテンツ。以下のMOD情報を使って記事を書く。追記のみ、既存ファイルの削除・変更は行わない。

EU5 MOD情報（8 MOD）:

1. **Imperial Papermap** — 作者: enqwery / 14,315購読 / 最終更新: 2026-03-16 / Imperator: Rome風ペーパーマップ。Lite版は実績互換。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3600623918
2. **Community Flavor Pack** — 作者: El Tyranos / 26,482購読 / 最終更新: 2025-11-06 / 各文化圏の歴史的衣装をポートレートに追加。ゲームプレイ変更なし。作者がParadoxのキャラクターアートチームに加入したため更新鈍化の可能性。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3599543453
3. **Nice Wide Mapmode UI** — 作者: DDRJake / 12,334購読 / 最終更新: 2025-11-14 / マップモードUIを常時表示に変更。1.1.5〜1.1.9動作確認。hud_bot.gui/ingame_topbar.guiを編集する他MODと競合の可能性。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3603821572
4. **Formable Nations: Reworked** — 作者: Noah (JihadiJackass) / 5,145購読 / 最終更新: 2026-03-30 / 140以上のカスタム建国オプション。建国グループ単位で有効/無効切替可能。実績非互換。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3599977147
5. **New World Improvement Project** — 作者: NullPointer, Apuskipay / 14,197購読 / 最終更新: 2026-03-07 / 新大陸のVanilla+強化。数百の動的地名、20以上の植民地建国オプション。バニラファイル上書きが多く他MODとの互換性注意。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3599544582
6. **Way of the Dodo** — 作者: Weyland/Tinholt, Uber / 7,680購読 / 最終更新: 2025-12-31 / 探検テーマのイベントパック。動植物発見イベント200件以上計画。追加型で壊れにくい。GameRant Top 5選出。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3600174902
7. **Beyond the Cape** — 作者: Stami / 2,832購読 / 最終更新: 2026-03-28 / 探検・海軍オーバーホール。新船種5タイプ、海峡通行料、地図窃盗メカニクス。新規ゲーム開始が必要。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3599889968
8. **Xorme - AI** — 作者: xorme / 6,278購読 / 最終更新: 2026-02-03 / EU4同名MOD後継。AIの請求権取得、議会利用、複数戦争管理等を改善。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3599552939

- [x] **Step 1: localization-reference.md を読み、EU5固有の用語（召集軍、支配度、進歩 等）を確認する**

Read: `eu5/localization-reference.md`
目的: 記事で使うゲーム内用語の正式日本語名を把握する

- [x] **Step 2: eu5-hungary-guide.md の冒頭30行を読み、メタデータ・トーンを確認する**

Read: `eu5/eu5-hungary-guide.md` (lines 1-30)
目的: 既存ガイドのメタデータ形式・文体に揃える

- [x] **Step 3: eu5-recommended-mods.md を作成する**

Write: `eu5/eu5-recommended-mods.md`

記事構成（この順序で書く）:

```markdown
# EU5 おすすめMODガイド（Patch 1.1.10 時点）

> 信頼性マーカー: 本記事のMOD情報はコミュニティ知見ベース（コミュニティ知見）。
> 2026-03-31 確認時点。パッチ更新でMOD互換性が変わる場合あり。
> 日本語は原則としてゲーム内ローカライズ準拠。

## MOD導入の基本

- Steam Workshop で「サブスクライブ」→ ゲームランチャーの「MOD」タブで有効化
- ロード順: 基盤系MOD（フレームワーク）→ ゲームプレイ変更 → ビジュアル・UIの順が安全
- 実績: MODを有効にするとほとんどの場合実績が解除されなくなる（例外は各MODの注意点を参照）
- Steam Workshop で「incompatible」と表示されるMODがあるが、これはParadoxのバージョンチェック機構によるもので実際には動作する場合が多い。各MODのコメント欄で動作状況を確認すること

## ビジュアル変更

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Imperial Papermap | enqwery | Imperator: Rome風のペーパーマップに変更。水面を暗く、陸地を明るく表示 | 14,000以上の購読者を持つ定番ビジュアルMOD。Lite版なら実績互換 | 通常版は実績非互換。Lite版を別途サブスクライブ可能 | 1.1.10 |
| Community Flavor Pack | El Tyranos | 各文化圏の歴史的衣装をキャラクターポートレートに追加 | EU5 MOD中最多の26,000購読。CK3版の公式移植。ゲームプレイ変更なし | 更新停滞の可能性あり（最終更新: 2025-11-06）。作者がParadox入社のため。ビジュアル系のため動作継続の可能性は高い | 1.1.x |

## UI・便利系

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Nice Wide Mapmode UI | DDRJake | マップモードUIを常時表示に変更 | ホバー時のポップアップ表示が煩わしい人向け。12,000購読 | 更新停滞の可能性あり（最終更新: 2025-11-14）。hud_bot.gui/ingame_topbar.guiを変更する他MODと競合の可能性 | 1.1.5〜1.1.9確認 |

## ゲームプレイ変更

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Formable Nations: Reworked | Noah | 140以上のカスタム建国オプション追加。バニラ建国もリワーク | 超アクティブ（2日前更新）。建国グループ単位で有効/無効の切替が可能 | 実績非互換 | 1.1.10 |
| New World Improvement Project | NullPointer, Apuskipay | 新大陸のVanilla+強化。動的地名、植民地建国オプション20以上 | 14,000購読。新大陸プレイを大幅に充実させる | バニラファイルを丸ごと上書きするため他MODとの互換性に注意。Bailiff上限0バグの報告あり | 1.1.x |
| Way of the Dodo | Weyland/Tinholt, Uber | 探検テーマのイベントパック。動植物発見イベント200件以上を計画 | GameRant Top 5選出。追加型MODのためパッチで壊れにくい | イベント追加のみでバランス変更なし | 1.1.x |
| Beyond the Cape | Stami | 探検・海軍オーバーホール。新船種5タイプ、海峡通行料、地図窃盗メカニクス | 探検メカニクスを根本から拡張。アクティブに更新中 | 新規ゲーム開始が必要。大型MODのため他MODとの競合に注意 | 1.1.10 |

## AI強化

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Xorme - AI | xorme | AIの請求権取得、議会利用、複数戦争管理、エステート管理等を改善 | EU4同名MODの後継。EU5で唯一の本格的AI改善MOD | 経済・征服者・探検システムは開発中（WiP） | 1.1.x |

## 出典

- **コミュニティ:**
  - [GameRant: Best Mods for EU5](https://gamerant.com/europa-universalis-5-eu5-best-mods/)
  - [Deltia's Gaming: EU5 5 Best Mods](https://deltiasgaming.com/europa-universalis-5-eu5-5-best-mods/)
  - [Steam Workshop Essential Mods コレクション](https://steamcommunity.com/sharedfiles/filedetails/?id=3606622874)
  - [Steam Workshop: EU5](https://steamcommunity.com/app/3450310/workshop/)
```

- [x] **Step 4: 作成したファイルを読み返し、テーブルの整合性（列数の一致、Markdown構文）を確認する**

Read: `eu5/eu5-recommended-mods.md`
確認項目: テーブル列数が全行で一致、リンク構文、パッチ番号の整合性

- [x] **Step 5: コミットする**

```bash
git add eu5/eu5-recommended-mods.md
git commit -m "追加: EU5 おすすめMODガイド（8 MOD / 4カテゴリ）"
```

---

### Task 2: VIC3 おすすめMODガイド作成

**Files:**
- Create: `vic3/vic3-recommended-mods.md`
- Reference: `vic3/localization-reference.md`（用語確認用）

**重要コンテキスト（サブエージェント向け）:**

このタスクは Markdown 記事の新規作成。コードではなくコンテンツ。追記のみ、既存ファイルの削除・変更は行わない。

VIC3 MOD情報（7 MOD）:

1. **Kuromi's AI** — 作者: KuromiAK / 約64,954購読 / 最終更新: 2025-12-13 / AI経済管理改善（非ヨーロッパ国家含む）、建設判断、技術優先度、政治改革の改善。ゲームプレイ変更やチートなし。Anbeeld (ARoAI作者) が後継として推奨。ロード順は他MODの前（バグ修正MODの後）。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3227982912
2. **Victorian Flavor Mod (VFM)** — 作者: stjern他 / 約44,191購読 / 最終更新: 2026-03-26 / 総合オーバーホール。中央集権法、AI改善、地域特性、新生産方式/技術、植民地リワーク。ペルシア、プロイセン/ドイツ、スウェーデン、フランス、オスマン等の拡張コンテンツ。200MB。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2880089689
3. **Better Politics Mod (BPM)** — 作者: Irbynx他 / 約53,091購読 / 3.0 Beta が 1.12対応 / 基本7利益団体を13以上に拡張。IG分裂、法律メカニクスオーバーホール、新ジャーナルエントリ・イベント。新法律/イデオロギー/制度を追加するMODとは非互換。VFM, VTM用互換パッチあり。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2932134122
4. **Morgenrote - Dawn of Flavor** — 作者: Marco Dandolo / Patreonコミュニティ / 最終更新: 約2026-03-25 (v2.7.1) / 科学遠征、文化プレステージ、芸術家・科学者育成システム。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2889925770
5. **Kikko's Formable and Releasable Nations** — 作者: Kikko / 約32,114購読 / 最終更新: 2025-12-11 / 100以上の建国/解放可能国家。カスタムフラグ、動的命名、11言語対応。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2901488792
6. **Advanced Cheat Menu ++** — 作者: Craveirusko / 約26,195購読 / 最終更新: 2025-12-11 / 国家・キャラクター・利益団体の修正GUI。カスタムキャラクタースポーン、ゴールド増減、権威修正。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3032469528
7. **Community Mod Framework (CMF)** — 作者: Victoria 3 Modding Co-op / 1.12確認 / MOD間の互換性向上ユーティリティ。GUI、政治運動フレームワーク、政党システム、MOD検出機能。複数フレーバーMODの前提依存。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=3385002128

- [x] **Step 1: localization-reference.md を読み、VIC3固有の用語（利益団体、法律、生産方式 等）を確認する**

Read: `vic3/localization-reference.md`

- [x] **Step 2: vic3-recommended-mods.md を作成する**

Write: `vic3/vic3-recommended-mods.md`

記事構成:

```markdown
# VIC3 おすすめMODガイド（Patch 1.12.4 時点）

> 信頼性マーカー: 本記事のMOD情報はコミュニティ知見ベース（コミュニティ知見）。
> 2026-03-31 確認時点。パッチ更新でMOD互換性が変わる場合あり。
> 日本語は原則としてゲーム内ローカライズ準拠。

## MOD導入の基本

- Steam Workshop で「サブスクライブ」→ ゲームランチャーの「MOD」タブで有効化
- ロード順: フレームワーク（CMF）→ AI改善 → ゲームプレイ変更 → チートの順が安全
- 実績: MODを有効にするとほとんどの場合実績が解除されなくなる
- 大型MOD（VFM, BPM等）は互いに競合する場合がある。互換パッチの有無を確認すること

## AI強化

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Kuromi's AI | KuromiAK | AI経済管理・建設判断・技術優先度・政治改革を改善。非ヨーロッパ国家のAIも強化 | 65,000購読のVIC3最人気AI MOD。ARoAI作者が後継として推奨。ゲームプレイ変更なし | ロード順は他MODの前（バグ修正MODの後）に配置 | 1.12 |

## ゲームプレイ変更

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Victorian Flavor Mod (VFM) | stjern他 | 総合オーバーホール。中央集権法、地域特性、新生産方式、植民地リワーク | 44,000購読。最もアクティブな大型MOD。ペルシア、プロイセン等の地域コンテンツ充実 | 200MB。他の大型MODとの併用時は互換パッチを確認 | 1.12.4 |
| Better Politics Mod (BPM) | Irbynx他 | 利益団体を7→13以上に拡張。IG分裂、法律メカニクスオーバーホール | 53,000購読。政治システムの深化に特化。3.0 Betaが1.12対応 | 新法律/イデオロギー追加MODと非互換。VFM用互換パッチあり | 1.12 (3.0 Beta) |
| Morgenrote - Dawn of Flavor | Marco Dandolo | 科学遠征、文化プレステージ、芸術家・科学者育成システム | 文化・ライフスタイル面を充実させるユニークなMOD。アクティブに更新中 | — | 1.12 |
| Kikko's Formable Nations | Kikko | 100以上の建国/解放可能国家。カスタムフラグ、動的命名 | 32,000購読。11言語対応。建国プレイの幅が大きく広がる | — | 1.12 |

## チート・デバッグ

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Advanced Cheat Menu ++ | Craveirusko | 国家・キャラクター・利益団体をGUIから修正。ゴールド増減、権威調整等 | 26,000購読。コンソールコマンド不要で手軽にテスト・実験が可能 | — | 1.12 |

## フレームワーク

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Community Mod Framework (CMF) | Victoria 3 Modding Co-op | MOD間の互換性向上ユーティリティ。政治運動フレームワーク、政党システム | 複数のフレーバーMOD（Hail, Columbia!等）が前提依存。MODを複数使うなら導入推奨 | 単体では目に見える変化なし | 1.12 |

## 出典

- **コミュニティ:**
  - [GameRant: 18 Best Victoria 3 Mods](https://gamerant.com/best-victoria-3-mods/)
  - [GameWatcher: Best Victoria 3 Mods](https://www.gamewatcher.com/news/the-best-victoria-3-mods)
  - [Steam Workshop Must Have コレクション](https://steamcommunity.com/sharedfiles/filedetails/?id=3258909663)
  - [Steam Workshop: Victoria 3](https://steamcommunity.com/app/529340/workshop/)
```

- [x] **Step 3: 作成したファイルを読み返し、テーブルの整合性を確認する**

Read: `vic3/vic3-recommended-mods.md`

- [x] **Step 4: コミットする**

```bash
git add vic3/vic3-recommended-mods.md
git commit -m "追加: VIC3 おすすめMODガイド（7 MOD / 4カテゴリ）"
```

---

### Task 3: CK3 おすすめMODガイド作成

**Files:**
- Create: `ck3/ck3-recommended-mods.md`
- Reference: `ck3/localization-reference.md`（用語確認用）

**重要コンテキスト（サブエージェント向け）:**

このタスクは Markdown 記事の新規作成。コードではなくコンテンツ。追記のみ、既存ファイルの削除・変更は行わない。

CK3 MOD情報（10 MOD）:

1. **Community Flavor Pack (CFP)** — 作者: El Tyranos / 586,834購読 / 最終更新: 2025-01-27 / 867-1453年の歴史的ポートレートアクセサリー追加。ゲームプレイ変更なし。更新停滞警告付き。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2220098919
2. **Ethnicities & Portraits Expanded (EPE)** — 作者: Celticus他 / 330,547購読 / 最終更新: 2025-03-18 / カスタム民族・3Dアセット追加。アラブ・ペルシャ等の装飾品、時代別衣装。VRAM 4GB以上推奨。CFPとの併用にはCompatibility Patchが必要。更新停滞警告付き。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2507209632
3. **Nameplates** — 作者: FUN / 424,786購読 / 最終更新: 2025-11-12 / イベント画面でキャラクター名・関係・称号を表示。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2220762808
4. **RICE (Regional Immersion and Cultural Enrichment)** — 作者: cybrxkhan / 最終更新: 2026-02-11 (v1.18.1.b) / 43のフレーバーパック。各地域・文化・宗教に固有アクティビティ、決定、イベント、音楽を追加。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2273832430
5. **A Culling of the Weak** — 作者: Olympia / 2,936購読 / 最終更新: 2025-11-13 / 外交圏外の遠方ルーラーのCPU処理を制限。約30%のパフォーマンス向上。Steam: https://steamcommunity.com/workshop/filedetails/?id=3604013167
6. **Divine Intervention Cheat Menu** — 作者: Lithane / 106,319購読 / 最終更新: 2026-03-14 / キャラクターエディタ、軍隊スポナー、アーティファクト作成等の包括的チートメニュー。旧定番Daddy Pika's Cheat Menuの後継的存在。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2986538297
7. **A Game of Thrones (CK3AGOT)** — 作者: CK3AGOTチーム / 565,957購読 / 最終更新: Beta 0.4.30.1 (CK3 1.18.4対応) / ジョージ・R・R・マーティンの世界への完全変換。ドラゴン、キングスガード、ヴァリリアンスチール、40文化以上。DLC不要（Roads to Power & Royal Court推奨）。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2962333032
8. **Princes of Darkness** — 作者: Morkeoth他 / 192,900購読 / 最終更新: 2026-03-12 (Blood & Silk) / World of Darkness系。ヴァンパイア、ハンター、ウェアウルフとして1230年のプリンス戦争を体験。Steam: https://steamcommunity.com/sharedfiles/filedetails/?id=2216659254
9. **Elder Kings 2** — 作者: コミュニティチーム / 最終更新: v0.18.0.1 (CK3 1.18.3.1対応) / Elder Scrolls世界への変換。ファンタジー種族、魔法ライフスタイル、吸血鬼システム。Steam/Nexus Modsで配布。

- [x] **Step 1: localization-reference.md を読み、CK3固有の用語（封臣、直轄領、ライフスタイル 等）を確認する**

Read: `ck3/localization-reference.md`

- [x] **Step 2: ck3-recommended-mods.md を作成する**

Write: `ck3/ck3-recommended-mods.md`

記事構成:

```markdown
# CK3 おすすめMODガイド（Patch 1.18.4 時点）

> 信頼性マーカー: 本記事のMOD情報はコミュニティ知見ベース（コミュニティ知見）。
> 2026-03-31 確認時点。パッチ更新でMOD互換性が変わる場合あり。
> 日本語は原則としてゲーム内ローカライズ準拠。

## MOD導入の基本

- Steam Workshop で「サブスクライブ」→ ゲームランチャーの「MOD」タブで有効化
- ロード順: ビジュアル系MOD同士は互換パッチを確認（CFP + EPE等）
- 実績: MODを有効にするとほとんどの場合実績が解除されなくなる
- 大型変換MOD（AGOT等）はバニラMODと併用不可。単体で使用すること

## ビジュアル変更

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Community Flavor Pack | El Tyranos | 867-1453年の歴史的ポートレートアクセサリー追加 | 587,000購読のCK3最人気MOD。ゲームプレイ変更なし | 更新停滞の可能性あり（最終更新: 2025-01-27）。ビジュアル系のため動作継続の可能性は高い | 1.18 |
| Ethnicities & Portraits Expanded | Celticus他 | カスタム民族・3Dアセット追加。アラブ・ペルシャ等の装飾品、時代別衣装 | 331,000購読。文化的多様性を大幅に向上 | 更新停滞の可能性あり（最終更新: 2025-03-18）。VRAM 4GB以上推奨。CFPとの併用にはCompatibility Patchが必要 | 1.18.3 |

## UI・便利系

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Nameplates | FUN | イベント画面でキャラクター名・関係・称号を常時表示 | 425,000購読。イベント選択時に「この人誰だっけ？」がなくなる | — | 1.18 |

## ゲームプレイ変更

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| RICE | cybrxkhan | 43のフレーバーパック。各地域・文化・宗教に固有アクティビティ、決定、イベント、音楽を追加 | CK3フレーバーMODの定番。マイナー地域にも対応しプレイの幅が大幅に広がる | — | 1.18.X |

## パフォーマンス

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| A Culling of the Weak | Olympia | 外交圏外の遠方ルーラーのCPU処理を制限 | テストで約30%のパフォーマンス向上を報告。終盤の重さに悩む人向け | 遠方のキャラクター行動が簡略化されるため、世界全体の動きがやや単調になる可能性 | 1.18+ |

## チート・デバッグ

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| Divine Intervention Cheat Menu | Lithane | キャラクターエディタ、軍隊スポナー、アーティファクト作成等の包括的チートメニュー | 106,000購読。旧定番Daddy Pika's（更新停止）の後継。GUIから操作可能 | — | 1.18.4 |

## 大型変換MOD

大型変換（Total Conversion）MODはゲーム全体を別の世界観に置き換える。バニラ用MODとは併用できないため、単体で導入すること。

| MOD名 | 作者 | 概要 | おすすめ理由 | 注意点 | 対応パッチ |
|-------|------|------|-------------|--------|-----------|
| A Game of Thrones | CK3AGOTチーム | ジョージ・R・R・マーティンの世界への完全変換。ドラゴン、40文化以上 | 566,000購読。CK3最大規模のTC。DLC不要で遊べる | Beta版。Roads to Power & Royal Court推奨。サブMODは0.4.30.1未対応の場合あり | 1.18.4 |
| Princes of Darkness | Morkeoth他 | World of Darkness系。ヴァンパイア・ハンター・ウェアウルフとして1230年を体験 | 193,000購読。CK3の王朝メカニクスを吸血鬼の血統に転用した独創的設計 | — | 1.18.4 |
| Elder Kings 2 | コミュニティチーム | Elder Scrolls世界への変換。ファンタジー種族、魔法ライフスタイル | TES世界をCK3で体験できる唯一のMOD。活発に開発中 | — | 1.18.3 |

## 出典

- **コミュニティ:**
  - [Seven Swords: Best CK3 Mods 2026](https://sevenswords.uk/bets-mods-crusader-kings-3/)
  - [TheGamer: 16 Best Mods for CK3](https://www.thegamer.com/best-mods-crusader-kings-3-ranked/)
  - [PC Gamer: Best CK3 Mods](https://www.pcgamer.com/best-crusader-kings-3-ck3-mods/)
  - [Steam Workshop: CK3](https://steamcommunity.com/app/1158310/workshop/)
```

- [x] **Step 3: 作成したファイルを読み返し、テーブルの整合性を確認する**

Read: `ck3/ck3-recommended-mods.md`

- [x] **Step 4: コミットする**

```bash
git add ck3/ck3-recommended-mods.md
git commit -m "追加: CK3 おすすめMODガイド（10 MOD / 6カテゴリ）"
```

---

### Task 4: 最終確認・全体コミット

**Files:**
- Read: `eu5/eu5-recommended-mods.md`, `vic3/vic3-recommended-mods.md`, `ck3/ck3-recommended-mods.md`

- [x] **Step 1: 3ファイルの存在を確認する**

```bash
ls -la eu5/eu5-recommended-mods.md vic3/vic3-recommended-mods.md ck3/ck3-recommended-mods.md
```

- [x] **Step 2: 各ファイルの行数・構造を確認する**

```bash
wc -l eu5/eu5-recommended-mods.md vic3/vic3-recommended-mods.md ck3/ck3-recommended-mods.md
```

各ファイルの想定行数: 50-80行

- [x] **Step 3: テンプレート一貫性を確認する**

3ファイル全てに以下が含まれていることを確認:
- 冒頭の信頼性マーカー blockquote
- 「MOD導入の基本」セクション
- カテゴリ別テーブル（6列: MOD名 / 作者 / 概要 / おすすめ理由 / 注意点 / 対応パッチ）
- 出典セクション

- [x] **Step 4: git status で未コミットファイルがないことを確認する**

```bash
git status
```

Expected: nothing to commit, working tree clean
