# CK3 おすすめMODガイド（Patch 1.19.0.6 時点）

> 信頼性マーカー: 本記事の互換性欄は配布元・更新ページ・ゲーム本体GUI定義を優先して確認。
> 2026-07-12確認時点。1.19系（Scribe、インストール版1.19.0.6）移行から約3ヶ月が経過し、主要MODの多くが正式対応済み。
> 日本語は原則としてゲーム内ローカライズ準拠。

## 1.19時点の結論

- 2026-07-12 時点で、本稿掲載の定番MODのうち5件（Community Flavor Pack・Ethnicities & Portraits Expanded・RICE・A Game of Thrones・Princes of Darkness）が配布元により「CK3 1.19 対応」を明記済み。1.19 移行から約3ヶ月が経過し、主要MODの追随が進んだ
- そのため 1.19 では「待つべきもの」より「対応済み＝すぐ入れるおすすめ一覧」として扱ってよい。ただし個々の注意点（実機確認推奨・直近リリースのため様子見が無難、等）は各行を確認する
- 例外として `CFP + EPE Compatibility Patch` のように、親MODは対応済みでも互換パッチ自体の状況が別（Steam非互換表示が継続中）というケースがあるため、併用MODは個別に確認する
- `Elder Kings II` のみ、配布元による1.19対応の明記が引き続き確認できず「待ち」区分のまま
- `Nameplates` は 1.19 バニラに `Event Nameplates` が入ったため、優先度が大きく下がった（変更なし）

## MOD導入の基本

- Steam Workshop で「サブスクライブ」し、ゲームランチャーの「MOD」タブで有効化する
- 1.19 移行直後は、既存セーブより新規セーブかバックアップを前提に試す
- ビジュアル系MOD同士は互換パッチを確認する。`CFP + EPE` はその代表例
- 大型変換MOD（Total Conversion）はバニラ向けMODと基本的に併用しない

## 自己責任で試す候補

1.19 対応の明記は見つからないが、更新継続や実装内容から見て追跡価値があるもの。

| MOD名 | 区分 | 現況 | 判断 | 注意点 |
|-------|------|------|------|--------|
| A Culling of the Weak: Performance Improvements | パフォーマンス | 配布説明では `For CK3 1.18+`。遠方AIの簡略化が中心 | 終盤の重さ対策として最初に試す候補 | 1.19 明記は未確認。挙動確認は新規セーブかバックアップ前提 |
| Divine Intervention Cheat Menu | チート・デバッグ | 2026-03-14 更新。Workshop 上では非互換表示だが更新自体は継続 | 検証用チートの第一候補 | 1.19 明記は未確認。右クリック interaction を変えるMODと競合しやすい |

## 対応済み

2026-07-12時点で、配布元が「CK3 1.19 対応」を明記しているもの。

| MOD名 | 区分 | 状況（出典・確認日） | 判断 | 注意点 |
|-------|------|----------------------|------|--------|
| Community Flavor Pack | ビジュアル | v3.3.6（2026-04-21）で「1.19.0 - Scribe」対応 `[出典: wiki.communityflavorpack.com/pages/releases, 2026-07-12確認]` | 導入可 | `EPE` と併用するなら互換パッチ（下記）の状況に注意 |
| Ethnicities & Portraits Expanded | ビジュアル | Steam説明文で「THE MOD IS 1.19.0.6 COMPATIBLE!」と明記 `[出典: Steam Workshop該当ページ, 2026-07-12確認]` | 導入可 | Steamの自動互換性バッジ自体は非互換表示のままの可能性があるため、実機（ゲーム内MODタブ）での最終確認を推奨 |
| RICE | ゲームプレイ変更 | Version 1.19.1「Pacific」（2026-07-10リリース、直近）が「for vanilla patch 1.19.x」と明記 `[出典: github.com/cybrxkhan/RICE-for-CK3, 2026-07-12確認]` | 導入可（直近リリース、要追跡・様子見も選択肢） | フレーバー量が多く、リリース直後の初期不具合が残っている可能性あり |
| A Game of Thrones | 大型変換 | Beta `0.4.38` がCK3 1.19.0.6向けとして公開済み（2026-07-03更新） `[出典: Steam Workshop該当ページ, 2026-07-12確認]` | 導入可 | 大型変換MODのためバニラ向けMODと基本的に併用しない |
| Princes of Darkness | 大型変換 | 「Descent of the Dragons」アップデート Version 1.19.0.6が2026-06-24リリース（未検証・要実機確認） `[出典: WebSearch経由確認, 2026-07-12。Nexusページ直接アクセスは403で失敗のため断定は避ける]` | 導入可（未検証・要実機確認） | 大型変換MODのためバニラ向けMODと基本的に併用しない。Nexus本体ページでの最終確認を推奨 |

### CFP + EPE Compatibility Patch

親MOD（CFP・EPE）は両方1.19.0.6対応済みだが、互換パッチ自体はSteamの互換性インジケーターが「incompatible」表示のまま（最終更新2026-06-07）。判断: 不明（要追加調査）。親MODは1.19対応済みだが、互換パッチ自体はSteam非互換表示が継続中。導入前に実機確認を推奨。

## 1.19対応待ち

| MOD名 | 区分 | 2026-07-12時点の状況 | 推奨判断 | 注意点 |
|-------|------|----------------------|----------|--------|
| Elder Kings II | 大型変換 | Nexus の最新公開は `0.18.0.2`。1.19 明記なし | 待ち | サブMODも親MOD追従待ちになりやすい |

## 1.19で優先度が下がったMOD

| MOD名 | 旧来の役割 | 1.19時点の判断 | 理由 |
|-------|------------|-----------------|------|
| Nameplates | イベント画面でキャラクター名・関係・特性を見やすくする | 外してよい | 1.19 バニラに `Event Nameplates` が追加され、Workshop 側も非互換表示になっている |

## 出典

- **一次・準一次情報:**
  - `C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game\gui\event_windows\character_event.gui`
  - [Crusader Kings III 1.19 "Scribe" Preliminary Changelog](https://store.steampowered.com/oldnews/?appgroupname=Crusader+Kings+III&appids=1158310&feed=steam_community_announcements)
  - [Community Flavor Pack Releases](https://wiki.communityflavorpack.com/pages/releases)
  - [Ethnicities & Portraits Expanded](https://steamcommunity.com/sharedfiles/filedetails/?id=2507209632)
  - [CFP + EPE Compatibility Patch](https://steamcommunity.com/sharedfiles/filedetails/?id=2996881191)
  - [RICE for CK3](https://github.com/cybrxkhan/RICE-for-CK3)
  - [Divine Intervention Cheat Menu](https://steamcommunity.com/sharedfiles/filedetails/?id=2986538297)
  - [A Game of Thrones](https://steamcommunity.com/workshop/filedetails/?id=2962333032)
  - [Princes of Darkness](https://www.nexusmods.com/crusaderkings3/mods/33?tab=files)
  - [Elder Kings II](https://www.nexusmods.com/crusaderkings3/mods/32)
- **コミュニティ/ミラー:**
  - [A Culling of the Weak: Performance Improvements](https://catalogue.smods.ru/archives/400869)
