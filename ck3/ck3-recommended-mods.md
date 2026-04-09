# CK3 おすすめMODガイド（Patch 1.19.0.1 時点）

> 信頼性マーカー: 本記事の互換性欄は配布元・更新ページ・ゲーム本体GUI定義を優先して確認。
> 2026-04-09 確認時点。1.19 系は移行直後のため、Steam の「非互換」表示と説明文の対応表記が食い違う場合がある。
> 日本語は原則としてゲーム内ローカライズ準拠。

## 1.19時点の結論

- 2026-04-09 時点で、本稿掲載の定番MODに「CK3 1.19 対応」を配布元が明記しているものは確認できなかった
- そのため 1.19 では「すぐ入れるおすすめ一覧」より、「待つべきもの」と「自己責任で試す候補」を分けて考えるほうが安全
- `Nameplates` は 1.19 バニラに `Event Nameplates` が入ったため、優先度が大きく下がった

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

## 1.19対応待ち

| MOD名 | 区分 | 2026-04-09時点の状況 | 推奨判断 | 注意点 |
|-------|------|----------------------|----------|--------|
| Community Flavor Pack | ビジュアル | 公式リリース確認は CK3 1.18.3 系まで | 待ち | `EPE` と併用するなら互換パッチが必要 |
| Ethnicities & Portraits Expanded | ビジュアル | Workshop 説明欄は `1.18.4 COMPATIBLE` のまま。Workshop は非互換表示 | 待ち | `CFP + EPE Compatibility Patch` 自体は 2026-03-20 更新だが、親MOD側の 1.19 明記は未確認 |
| RICE | ゲームプレイ変更 | 作者 GitHub の最新表記は `Version 1.18.2`、`for vanilla patch 1.18.x` | 待ち | フレーバー量が多く、パッチ跨ぎ直後の様子見推奨 |
| A Game of Thrones | 大型変換 | Workshop 説明欄は Beta `0.4.31` で CK3 `1.18.4` 向け | 待ち | 1.19 本体ではなく AGOT 側の対応更新待ち |
| Princes of Darkness | 大型変換 | Nexus の最新公開は `1.18.3.1` まで確認 | 待ち | 1.19 明記なし |
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
