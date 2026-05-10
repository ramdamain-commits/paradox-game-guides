# Changelog

## 2026-05-10

### Changed
- EU5 全 9 ガイド（`eu5/eu5-*.md`）に Patch 1.2「Echinades」のスクリプト一次検証結果を反映、レビュー指摘を一括修正
  - スクリプト実検証で確認できた 10 項目のマーカーを `[src: Patch_1.2 wiki + script verified]` に昇格（全71箇所）
    - 皇帝 Great Power Score 貢献 50（`international_organizations/hre.txt`）
    - 要塞駐屯は Heavy Infantry のみ（`unit_categories/01_army_heavy_infantry.txt` の `is_garrison = yes`）
    - 列聖コスト Religious Influence 75（`prices/00_hardcoded.txt`）
    - 外交破門コスト Religious Influence 50（`prices/03_diplomacy.txt`）
    - Papal Authority 0-100 範囲（`international_organizations/catholic_church.txt`）
    - Claim Throne CB 制限（請求者が target.ruler の場合発行不可、`casus_belli/claim_throne.txt`）
    - Diet 4段階存在（Court Assembly / Early Diet / Bicamerial / Tricamerial、`parliament_types/01_international_organization.txt`）
    - Restore Roman Borders CB 存在（`casus_belli/D008_restore_roman_borders.txt`）
    - Light/Heavy 兵科カテゴリ存在（`unit_categories/`）
  - 数値誤りを修正
    - Light Cavalry 移動速度「7.00」→「3.0」（実値：`unit_categories/02_army_light_cavalry.txt`）
    - Light Cavalry フランキング「200%」→「210%」
    - Heavy Cavalry「Morale 被ダメ -10%」→「標準モラル耐性（Light Cavalry が被モラルダメ +10%）」に書き換え
  - レビュー指摘の重大度高 9 件修正
    - Papal Authority 75/25 閾値の「verified と未確認の同一行併記」を「0-100 範囲のみ verified」に分離（austria/castile/universal）
    - ottoman 用語対照表「支配度 = Dominance」誤訳を「Control（州支配度）」と「Dominance（大国指標）」に分離
    - regional/government 間の「官僚制」記述矛盾を統一
    - religion 末尾免責文を「スクリプト確認状況」4行構造に書き直し（individual verified と一括免責の整合）
    - universal 傭兵コストの時系列矛盾を整理（1.0→1.1 で値下げ、1.1→1.2 で再度 +25%）
    - government 出典セクションに `hre.txt` / `claim_throne.txt` / `parliament_types/` / `D008_restore_roman_borders.txt` 追記
    - religion の列聖・破門コスト本文側に `prices/00_hardcoded.txt` / `prices/03_diplomacy.txt` 出典追記
  - 断定過多の弱化（4 件：religion「全廃」/ austria「必ず参戦」/ castile「必ず発火」/ universal「ポップが直接死亡」）
  - brandenburg 王朝力上限 200→300 に「scripts に明示的な cap 値は未発見。dynastic_power は計算値」注記追加
  - hungary ハイドゥク兵科分類を「推定・スクリプト未確認」と明示

## 2026-05-09

### Changed
- EU5 オスマン帝国攻略ガイド（`eu5/eu5-ottoman-guide.md`）を Patch 1.2「Echinades」ベースに更新（DLC Fate of the Phoenix 直撃）
  - ヘッダ・確認日を 1.2 に更新
  - パッチ差分セクションを 1.2 確定情報に書き換え（バルカン・ビザンツ / 戦争外交 / 軍事 / 宗教 / 貿易の5カテゴリ）。「オスマンプレイヤーが特に注意すべき変更（破壊的）」サブ節を新設（ビザンツ復興・Restore Roman Borders CB・Greek Fire/Cataphracts/Legionaries・要塞駐屯 Heavy Infantry 限定・補給線管理・Coalition Superiority 化）
  - 序盤・中盤・終盤戦略に「1.2 重要」「1.2 最重要」blockquote 注記追加（バルカン DHE 動的化・コンスタンティノープル攻略タイミング加速・要塞数超過 Belligerent）
  - 軍事ドクトリンに「### 1.2 兵科分類とオスマン軍編成」節追加（イェニチェリ Heavy Infantry 推測・アクンジュ Light Cavalry・シパーヒー/カピクル騎兵 Heavy Cavalry・補給線管理）
  - 外交に「### 1.2 外交変更とオスマン」節追加（Claim Throne CB 制限・Coalition Superiority・Enforce Peace 双方合意・Belligerent 要塞超過判定）
  - 内政・経済に「### 1.2 貿易・宗教変更とオスマン内政」節追加（海上 1/10・正教オーバーホール）
  - 固有イベント時系列に「### 1.2 ビザンツ復興と DLC コンテンツ（脅威）」節追加（Pronoia・Katepanata・Restore Roman Borders CB・ギリシャ火・新ユニット・Latin Culture Movement）
  - よくあるミスに 1.2 関連 4 項目追加
  - 用語対照表に 7 項目追加（ローマ国境回復 CB・プロノイア・カテパナタ・軽装/重装歩兵・軽装/重装騎兵・優位性戦争・総主教）
  - 出典に Patch 1.2・Fate of the Phoenix・Byzantine content の各 Wiki URL を追加
- EU5 ブランデンブルク攻略ガイド（`eu5/eu5-brandenburg-guide.md`）を Patch 1.2「Echinades」ベースに更新
  - ヘッダ・確認日を 1.2 に更新
  - パッチ差分セクションを 1.2 確定情報に書き換え（HRE オーバーホール・戦争外交・軍事の3カテゴリ）。「ブランデンブルクプレイヤーが特に注意すべき変更」サブ節を新設
  - 序盤・中盤戦略に 1.2 注記追加（Free Cities 自動参戦廃止メリット・Coalition Superiority 化・王朝力上限 300）
  - 軍事ドクトリンに「### 1.2 兵科分類とプロイセン軍編成」節追加（擲弾兵 Heavy Infantry 推測・要塞守備見直し・補給線管理）
  - 外交に「### 1.2 外交変更とブランデンブルク」節追加（Claim Throne CB 制限・Coalition Superiority・Enforce Peace）
  - よくあるミスに 1.2 関連 4 項目追加
  - 用語対照表に 6 項目追加（Imperial Diet・Imperial Armories・王朝力・軽装/重装歩兵・軽装/重装騎兵・優位性戦争）
- EU5 カスティーリャ攻略ガイド（`eu5/eu5-castile-guide.md`）を Patch 1.2「Echinades」ベースに更新
  - ヘッダ・確認日を 1.2 に更新
  - パッチ差分セクションを 1.2 確定情報に書き換え（貿易/都市・宗教・戦争外交の3カテゴリ）。「カスティーリャプレイヤーが特に注意すべき変更」サブ節を新設
  - 序盤・中盤・終盤戦略に 1.2 注記追加（海上ルートコスト 1/10・Maritime Presence 反映・Megalopolis）
  - 軍事ドクトリンに「### 1.2 兵科分類とテルシオ編成」節追加（テルシオ Heavy Infantry 推測・北アフリカ/イタリア戦線補給線）
  - 内政・経済に「### 1.2 貿易改修と Urban Rights」節追加（海上 1/10・Town Rights スロット制・Megalopolis）
  - 「### 1.2 Papal Authority とカトリック超大国戦略」節追加（コスト半減・北アフリカ十字軍 CB フォールバック）
  - よくあるミスに 1.2 関連 4 項目追加
  - 用語対照表に 7 項目追加
- EU5 ハンガリー攻略ガイド（`eu5/eu5-hungary-guide.md`）を Patch 1.2「Echinades」ベースに更新
  - ヘッダ・確認日を 1.2 に更新
  - パッチ差分セクションを 1.2 確定情報に書き換え（バルカン新規・HRE関連・戦争外交・軍事の4カテゴリ）。「ハンガリープレイヤーが特に注意すべき変更」サブ節を新設（Restore Roman Borders CB がバルカン領土を標的化する最大脅威を強調）
  - 序盤・中盤・終盤戦略に 1.2 注記追加（バルカン DHE 動的化・ビザンツ復興警戒・ハプスブルク同君連合時の HRE オーバーホール影響）
  - 軍事ドクトリンに「### 1.2 兵科分類とハンガリー軍編成」節追加（ハイドゥク Light Infantry 推測・フッサル前身軽騎兵・対オスマン補給線）
  - 外交に「### 1.2 外交変更とハンガリー」節追加
  - 固有イベント時系列に「### 1.2 バルカン新規コンテンツ」節追加（Restore Roman Borders CB・Latin Culture Movement・新3Dモニュメント）
  - よくあるミスに 1.2 関連 4 項目追加
  - 用語対照表に 7 項目追加
- EU5 汎用攻略ガイド（`eu5/eu5-universal-guide.md`）を Patch 1.2「Echinades」（2026-05-06 リリース）ベースに全面更新
  - ヘッダ・確認日を 1.2「Echinades」（2026-05-06 リリース）に更新
  - パッチ差分セクションを 1.2 主要変更 12 項目（HRE 大幅オーバーホール・Papal Authority・Heavy/Light 兵科分類・兵站厳格化・Coalition→Superiority War・Enforce Peace 双方合意・Claim Throne CB 制限・貿易改修・Urban Rights/Megalopolis・正教オーバーホール・ギリシャバルカン新規）に書き換え
  - 「⚠ 1.2 更新候補」マーカー 6 箇所を確定情報に置換（官僚制関連は「1.2 では実装されなかった」明記）
  - 軍事セクションに「兵科の Heavy/Light 分類（1.2）」節追加（要塞駐屯 Heavy Infantry 限定・独立アップグレードツリー）
  - 外交セクションに「1.2 の外交変更」節追加（Coalition War / Enforce Peace / Claim Throne / Belligerent）
  - 新セクション「貿易・都市システム（1.2 改修）」追加
  - よくあるミスに 1.2 関連 4 項目追加
  - 用語対照表に 12 項目追加（帝国議会・帝国兵器庫・教皇権威・軽装/重装歩兵・軽装/重装騎兵・優位性戦争・都市特権・メガロポリス・プロノイア・ローマ国境回復 CB）
- EU5 オーストリア攻略ガイド（`eu5/eu5-austria-guide.md`）を Patch 1.2「Echinades」（2026-05-06 リリース）ベースに更新
  - ヘッダ・確認日を 1.2 に更新
  - パッチ差分セクションを 1.2 確定情報に書き換え。「オーストリアプレイヤーが特に注意すべき破壊的変更」サブ節を新設（GP Score 250→50・Free Cities 自動参戦廃止・Claim Throne CB 制限・Golden Bull 1400 離脱条件）
  - HRE 運営セクション: 皇帝アクション表に「Imperial Armories 建造（1.2 新規）」追加。帝国法ロードマップ前に Imperial Diet 投票システム刷新の注記。選帝侯管理に Diet UI タブ化・同一王朝再選 +5 IA。帝国防衛フローに「1.2 重要な変更」節（Free Cities 自動参戦廃止・指揮権自動取得廃止）
  - ハプスブルク婚姻外交: Claim Throne CB 制限注記・王朝力上限 200→300 注記を追加
  - 軍事ドクトリン: 「### 1.2 兵科分類とオーストリアの編成」節を新設（4 兵科特性表）。帝国防衛軍の補給線管理注記
  - 宗教改革: 「### Papal Authority（1.2 新システム）の活用」節を新設
  - よくあるミスに 1.2 関連 5 項目追加
  - 用語対照表に 13 項目追加
- EU5 宗教グループ別攻略ガイド（`eu5/eu5-religion-guide.md`）を Patch 1.2「Echinades」（2026-05-06 リリース）ベースに更新
  - ヘッダ・確認日を 1.2 に更新
  - 「⚠ 1.2 更新候補」マーカー 2 箇所を確定情報に置換
  - カトリック節に 2 小節追加（Papal Authority 新システム・十字軍 CB 変更）
  - 正教節を 3 部構成に再編（1.2 オーバーホール破壊的変更・1.1 系旧メカニクス参考情報・上位概要）
  - 用語対照表に 5 項目追加（教皇権威・外交破門・総主教・儀式力（廃止）・列聖コスト更新）
  - 出典に Patch 1.2 wiki マーカー対照表を追加
- EU5 政府タイプ別攻略ガイド（`eu5/eu5-government-guide.md`）を Patch 1.2「Echinades」（2026-05-06 リリース）ベースに更新
  - ヘッダ・確認日を 1.2「Echinades」（2026-05-06 リリース）に更新
  - 君主制: 「⚠ 1.2 更新候補」（官僚制）を HRE オーバーホール確定情報に置換。「### 1.2 君主制への影響」節を新設（Imperial Diet・Armories・GP Score 250→50・王朝力上限 200→300・Free Cities 自動参戦廃止・Claim Throne CB 制限等）
  - 共和国: 「⚠ 1.2 更新候補」を確定情報に置換。「### 1.2 共和国への影響」節を新設（貿易改修・Urban Rights・Megalopolis・Heavy/Light 兵科分類）
  - 神権制: 「⚠ 1.2 更新候補」を正教オーバーホール確定情報（破壊的）に置換。「### 1.2 神権制への影響」節を新設（Papal Authority コスト半減・Papal States 制限・Patriarch キャラクター実装・Rite Power 廃止）
  - ステップ遊牧民・部族: 「⚠ 1.2 更新候補」を確定情報に置換。「### 1.2 ホード/部族への影響」節を新設（ロジスティクス距離 50→30・食料消費 10 倍・Light Cavalry 分類）
  - 「1.2 更新候補まとめ」セクションを「Patch 1.2 政府タイプ別変更まとめ」に更新。官僚制を「1.2 では実装されなかった」と明記
  - 「## 1.2 新規用語（政府タイプ別ガイド範囲）」節を新設（9 用語追加：Imperial Diet・Imperial Armories・Papal Authority・Dynastic Power・Restore Roman Borders CB・Urban Rights・Megalopolis・Pronoia・Katepanata）
  - 出典セクションに Patch 1.2・Holy Roman Empire・Fate of the Phoenix の各 Wiki URL を追加
- EU5 地域別攻略ガイド（`eu5/eu5-regional-guide.md`）を Patch 1.2「Echinades」（2026-05-06 リリース）ベースに全面更新
  - ヘッダ・確認日を 1.2 に更新
  - 西欧セクション: 官僚制「1.2 更新候補」を削除し、貿易改修（海上ルートコスト 1/10・Maritime Presence 反映）に置換。「### 1.2 貿易改修と海洋国家」節を新設
  - HRE セクション: 「1.2 更新候補」を確定情報に格上げ（Imperial Diet・GP Score 250→50・Free Cities 自動参戦廃止等）。「### 1.2 HRE オーバーホール（地域影響）」節を新設
  - 東欧セクション: セルビア欄の「1.2 更新候補」を正教オーバーホール確定情報に置換。東欧サマリーを確定情報に格上げ。「### 1.2 ビザンツ復興とバルカン新コンテンツ」節を新設（Pronoia・Katepanata・Restore Roman Borders・Greek Fire 等 DLC Fate of the Phoenix 内容含む）
  - 東アジア・ステップ・アフリカの「⚠ 1.2 更新候補」を「1.2 確認: 変更なし」形式に更新（「オープンベータ」語を除去）
  - 用語対照表: 官僚制エントリを「1.2 で実装されず」に修正
  - 「## 1.2 新規用語（地域別ガイド範囲）」節を新設（13 用語追加）
  - 出典セクションに Patch 1.2・Fate of the Phoenix・Holy Roman Empire・Byzantine content の各 Wiki URL を追加

## 2026-05-08

### Fixed
- VIC3 プロイセンガイド 1.13 対応のレビュー指摘修正
  - ビスマルク Prominence 記述を「IG指導者として育てる手順は推奨しない（首相任命ルートを優先）」に修正
  - 用語対照表に Prominence・艦船デザイナー・旗艦・戦略的関心度・クーデター扇動・砲撃外交の6用語を追加
  - 砲撃外交・クーデター扇動の発動条件をスクリプト未確認である旨を明記
  - `[src: https://...Patch_1.13]` を `[src: Patch_1.13 wiki]` 形式に統一（テンプレート準拠）
  - 単一指揮官制・クーデター扇動・砲撃外交の UI 導線記述を追加（一般知識ベース、要プレイ検証）

### Changed
- VIC3 プロイセンガイド Patch 1.13（Matcha、2026-04-28 リリース）全面対応
  - 冒頭メタ情報・パッチ差分セクションを 1.13 に更新
  - 軍事ドクトリン「将軍の選び方」を単一指揮官制に書き換え（編成あたり指揮官1名・階級と特性の重要性）
  - 「統一戦争での注意」に複数前線時の編成分割・階級と距離による同時攻撃制限を追記
  - 外交セクションに 1.13 の新手段（戦略的関心度ティアド・クーデター扇動・砲撃外交・条約強化）を追加
  - 終盤の海軍記述を艦船デザイナー・旗艦仕様に更新
  - 利益団体管理にプロミネンス（Prominence）活用の節を追加
  - 出典に Patch 1.13 wiki を追加

## 2026-04-05

### Added
- EU5 ブランデンブルクガイド最新情報更新（2026-04-05確認）（001e209）
- EU5 カスティーリャ攻略ガイド + Patch 1.2差分（79b8970）

## 2026-04-04

### Added
- オーストリアガイド 骨格 + セクション1-4（9c18c58）
- オーストリアガイド セクション5-13（07869d5〜0e462bb）
- オーストリアガイド付随更新（index・用語・相互リンク）（a621094）

### Fixed
- オーストリアガイド レビュー指摘修正（表記揺れ・構造統一・用語追加）（c12e217）

### Changed
- オーストリアガイド中間データを削除（72ea3f8）

## 2026-04-03

### Changed
- README に EU5 共通システムガイド・GitHub Pages セクション追加（6401562）
