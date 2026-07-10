# Changelog

## 2026-07-11 EU5 1.3 安定版昇格 フェーズ1 Task1-4（recommended-mods昇格）

### Changed
- `eu5-recommended-mods.md` の「1.3 オープンベータでのMOD互換性（純追記）」節を「1.3 でのMOD互換性」に格上げ
- MOD表の「対応パッチ」列（旧1.1.x基準）を、researcher（sonnet）によるSteam Workshop実地調査（8 MOD全件）に基づき更新。1.3対応が明確なのはImperial Papermapのみ（作者が1.3.10リリース当日に明言）、残り7件は「1.3未確認」としてコミュニティ知見マーカーで記載
- reviewer検出のWarning2件を反映: 4 MOD（Community Flavor Pack/Nice Wide Mapmode UI/Way of the Dodo/Beyond the Cape）の最終更新日がPatch1.2リリース日（2026-05-06）より前だったため対応パッチ表記を「1.2.x」→「1.1.x」に修正、Community Flavor Packのセーブクラッシュ報告を注意点欄へ反映

### Notes
- **これでフェーズ1（Task1-1〜1-4、全11ガイドの本文統合）が完遂**。次はフェーズ2（中央localization-reference昇格+index.html betaバッジ除去）→フェーズ2.5（小型3ガイド拡充、opus推奨）→フェーズ3（整合スイープ+検証）

## 2026-07-11 EU5 1.3 安定版昇格 フェーズ1 Task1-3（byzantium + 国別5 本文統合）

### Changed
- `eu5-byzantium-guide.md` / `eu5-ottoman-guide.md` / `eu5-hungary-guide.md` / `eu5-austria-guide.md` / `eu5-brandenburg-guide.md` / `eu5-castile-guide.md` の6ガイドについて「1.3 オープンベータ差分」セクションを本体章へ統合し、beta語をstable語へ昇格
- byzantium: ジェノヴァ弩兵の行番号誤記を修正（69→68）。船コスト増の記述を序盤・後半の両章に配置（差分原文が序盤文脈だったため）
- ottoman: 「更新優先度Tier2メモ」（運用メモ）を本文統合せず完全削除
- hungary: `no_female_heirs_for_poland`例外注記を維持しつつ、Union of Crownsの一般記述と例外を別節に分離配置
- austria: 「宗教改革への備え」という独立節を新設せず、既存の「中盤戦略」章「手順」節内へ統合（存在しない見出しの誤創出を回避）
- brandenburg: Berenberg（ハンブルク固有）の誤帰属回避注記を維持
- castile: Taula de Canvi（アラゴン固有）の誤帰属回避注記を維持
- 各ガイド間の相互参照リンクを、前セッション（Task1-1/1-2）およびWave1（byzantium/austria）で解体・再配置済みの新セクション名へ張り替え

### Notes
- 相互参照の依存関係を避けるため、他ガイド未参照の自己完結組（byzantium/austria/hungary＝Wave1）を先行させ、Wave1の結果を参照する組（ottoman/brandenburg/castile＝Wave2）を後続させる2波構成で実施
- reviewer（sonnet）3並列×2波でCritical指摘なし。Warning/Suggestion計6件は反映済み
- これでフェーズ1 Task1-3（byzantium+国別5）完遂。次はTask1-4（recommended-mods）→フェーズ2（中央用語昇格+index.html）→フェーズ2.5（小型3ガイド拡充）→フェーズ3（検証）

## 2026-07-10 EU5 1.3 安定版昇格 フェーズ1 Task1-2（regional単独 本文統合）

### Changed
- `eu5-regional-guide.md` の「1.3 オープンベータ差分」セクション（西欧/イタリア/イベリア/東欧バルカン/各地域共通/概要・東アジアの6ブロック）を本体の各地域章へ統合。beta語をstable語へ全面昇格
- 天然痘（Smallpox）の月次発生率の誤記を修正: パッチノート記載値0.05ではなく、インストール版の実機スクリプト値0.08を採用（中間hotfixでの再調整が疑われる旨を注記）
- Voivode改革のgovernment-guideへの相互参照リンクを、前セッション（Task1-1）で解体済みの旧セクション名から新セクション（「君主制（Monarchy）」章「主要政府改革」表）へ張り替え。byzantium-guideへの相互参照はbyzantium未着手のため意図的に維持

### Notes
- reviewer（sonnet）によるレビューでCritical/Warning/Suggestionすべてなし
- 計画書のセッション分割ガイド（regional単独・byzantiumと同居させない）に従い、`docs/superpowers/plans/2026-06-18-eu5-patch13-stable-promotion.md` のTask番号を実運用に合わせて整理（Task1-2=regional単独、Task1-3=byzantium+国別5に統合）
- 次はTask1-3（byzantium+国別5ガイド）

## 2026-07-10 EU5 1.3 安定版昇格 フェーズ1 Task1-1（universal/government/religion 本文統合）

### Changed
- EU5 1.3が安定版（buildid 24075414 / v1.3.10）としてリリースされたことに伴い、`docs/superpowers/plans/2026-06-18-eu5-patch13-stable-promotion.md` の昇格フローに着手。`eu5-universal-guide.md` / `eu5-government-guide.md` / `eu5-religion-guide.md` の3ガイドについて「1.3 オープンベータ差分」純追記セクションを解体し、該当する本体章へ統合。beta語（`（1.3 beta）` 等）をstable語へ全面昇格
- universal: 経済・海軍/軍事・諜報外交・自動化/宮廷芸術家の1.3項目を本体4章へ統合。プリフライト再検証で判明した誤記（「海軍維持費の下限が艦隊規模の10%」→正しくは「維持費も概ね2倍」）を修正した上で統合
- government: 政体別1.3項目を各政体章へ統合。低Devotionペナルティは、ファイル内の権力リソース定義（Devotion=神権制）に基づき神権制章へ配置（当初計画の「君主制」から実装時に訂正）。宮廷芸術家12種の詳細はこのガイドを正本として保持し、universal側は簡略＋参照のみに整理
- religion: 宗教関連1.3項目を「宗教改宗の仕組み（共通）」章・キリスト教グループ章へ統合。Patriarch/Rite Power廃止（1.2の変更であり1.3ではない）の誤帰属回避注記は削除せず正教会セクション冒頭に維持。マーカー表記の不整合（一括免責文と本文インライン表記の齟齬）・特殊文字（全角マイナス記号）を修正

### Notes
- reviewer 3並列によるレビューでCritical指摘なし（Warning 1件・Suggestion 2件は反映済み）
- `eu5-regional-guide.md` に government の旧セクション名（「1.3 オープンベータ差分」）への参照が残存。regional-guide自体の昇格作業（フェーズ1 Task1-2、次セッション予定）で解消する
- 残る作業: regional単独→国別6ガイド（ottoman/hungary/austria/brandenburg/castile/byzantium）→Tier4（用語対照表中央昇格）→検証（フェーズ2〜3）

## 2026-07-03 CLAUDE.md ダイエット（章テンプレ・定型手順の分離）

### Changed
- CLAUDE.md（35.2KB）から「ゲーム横断テンプレート」（全13セクションの章構成）を `docs/templates/guide-section-template.md` へ、「新規国別ガイド追加の手順」を `docs/procedures/new-country-guide.md` へ verbatim 分離（26.2KB へ削減・内容の削除なし）。CLAUDE.md にはルール・制約・スクリプト参照先とポインタのみを残す

## 2026-06-18 EU5 1.3 オープンベータ差分 純追記（Tier4 先行: recommended-mods 1.3 beta互換注記）

### Added
- `eu5/eu5-recommended-mods.md`: 「1.3 オープンベータでのMOD互換性（純追記）」を追加。ベータブランチ切替時の incompatible 挙動・バニラ上書き型MODの破損リスク・壊れにくい追加/ビジュアル系・セーブ非互換・実績仕様を整理（全て コミュニティ知見：1.3 beta 扱い）。MOD表の対応パッチ列(1.1.x基準)は安定版で更新する旨を明記
- 出典に Patch 1.3 wiki を追記、`index.html` の おすすめMOD カードに「1.3 beta差分」バッジを追加（計11）

### Notes
- Tier4 のうち beta 時点で意味を持つ「recommended-mods 互換注記」のみ先行。localization-reference 中央昇格・差分の本文統合（昇格フロー）は 1.3 安定版リリース後に実施

## 2026-06-18 EU5 1.3 オープンベータ差分 純追記（次セッションバッチ2: 国別 ottoman/hungary/austria/brandenburg/castile）

### Added
- 5 国別ガイドに「1.3 オープンベータ差分（…直接影響・純追記）」を案A方式で追加。1.2 本体章は無変更:
  - `eu5/eu5-ottoman-guide.md`: 船コスト 4x/10x・海戦致死性・建物維持費逓増+50%・陸軍 goods 2 倍（いずれも changelog 由来）＋ Twilight of the Tsardom によるバルカン流動化 `[src: disasters/twilight_of_the_tsardom.txt]`。更新優先度 Tier2 メモを明記（B-1）
  - `eu5/eu5-hungary-guide.md`: 陸軍 goods 2 倍＝黒軍(a_the_black_army)コスト直撃（B-2、changelog 由来）＋ Union of Crowns の女性継承整理 `[src: scripted_relations/union_of_crowns_pact.txt, heir_selections/monarchy.txt]`、**⚠ 対ポーランド PU の女性継承除外例外 `no_female_heirs_for_poland` `[src: heir_selections/monarchy.txt:1206]`**（A-7）
  - `eu5/eu5-austria-guide.md`: **従属国への宗教統一強制が不可**（B-3）・HRE 加入 reluctance・土地剥奪の皇帝集権（いずれも changelog 由来）＋経済リバランス・Twilight 相互参照 `[src: disasters/twilight_of_the_tsardom.txt]`
  - `eu5/eu5-brandenburg-guide.md`: HRE 皇帝メカニクス調整・Voivode（東隣ポーランド）`[src: government_reforms/country_specific.txt]`・経済リバランス＋**⚠ Berenberg 家族銀行は HAM 固有 `[src: events/DHE/flavor_HAM.txt]` でブランデンブルク非該当（A-5・誤帰属回避）**
  - `eu5/eu5-castile-guide.md`: 船コスト増（植民艦隊直撃）・海戦致死性・経済リバランス・植民/移民拡大・新文化（種別断定保留）＋**ℹ Taula de Canvi はアラゴン固有 `[src: events/DHE/flavor_ARA.txt:flavor_ara.220]` で regional 移管済（誤帰属回避）**
- 各ガイドの用語対照表に「1.3 オープンベータ用語（仮登録）」を追加、出典に 1.3 スクリプトファイル・Patch 1.3 wiki を追記
- `index.html`: ottoman/hungary/austria/brandenburg/castile カードに「1.3 beta差分」バッジを追加

### Notes
- script-checkable 項目は実機 grep で再確認: `no_female_heirs_for_poland`(monarchy.txt:1206) / `union_of_crowns_pact`(scripted_relations) / Berenberg=flavor_HAM.txt（HAM 固有確定）/ Taula=flavor_ara.220 / Voivode=country_specific.txt
- 経済目玉値（船コスト 4x/10x・建物維持費+50%・陸軍 goods 2 倍・海戦致死性）はエンジン内部値で全て changelog 由来マーカー（spec section 1 の確定表どおり）
- austria/brandenburg からの被リンク相互更新を実体化（regional Twilight/Voivode ノードと相互参照、universal/government/byzantium へのリンクを 1.3 節内に配置）
- Tier4（localization-reference 中央昇格・差分の本文統合）は 1.3 安定版リリース後の昇格フローで実施

## 2026-06-18 EU5 1.3 オープンベータ差分 純追記（次セッションバッチ1: regional-guide 単独）

### Added
- `eu5/eu5-regional-guide.md`: 「1.3 オープンベータ差分（地域別・純追記）」を追加。1.2 本体（各地域節）は一切変更せず、地域別に 1.3 差分を純追記:
  - 西欧=百年戦争リバランス `[src: situations/hundred_years_war.txt]`・薔薇戦争ディザスター `[src: disasters/war_of_the_roses.txt]`
  - イタリア=ゲルフ／ギベリン改修 `[src: situations/guelphs_and_ghibellines.txt]`（spec通り西欧章から移動）
  - イベリア(アラゴン)=Taula de Canvi 公営銀行 `[src: events/DHE/flavor_ARA.txt:flavor_ara.220]`（castile でなく regional に配置）
  - 東欧・バルカン=Twilight of the Tsardom `[src: disasters/twilight_of_the_tsardom.txt, events/DHE/flavor_BUL.txt]`・Voivode 改革 `[src: government_reforms/country_specific.txt]`
  - 各地域共通=RGO 再分配（Iron/Wool/Horses/Beeswax、changelog 由来）
  - 概要・東アジア=植民/移民拡大・新文化（公式ノート 6 種、種別断定保留）・天然痘亜熱帯化 `[src: diseases/smallpox.txt]`（1.3.2 で発生率 0.1→0.05・拡散閾値 0.15・subtropical 追加）・Korea 研究ナーフ＝集賢殿(Hall of Worthies) `[src: events/DHE/flavor_KOR.txt: kor_hall_of_worthies_modifier]`
- 用語対照表に「1.3 オープンベータ用語（仮登録）」表（7 語）を追加、出典セクションに 1.3 スクリプトファイル一覧・Patch 1.3 wiki を追記
- `index.html`: regional カードに「1.3 beta差分」バッジを追加
- byzantium 既存 1.3 節の「regional 東欧・バルカン節の Twilight 記述と相互参照」を実体化（regional 側 Twilight ノードから byzantium へ相互リンク）

### Notes
- load-bearing な値は実機 grep で再確認: smallpox 実値（spawn 0.05 / threshold 0.15 / subtropical）・Taula(flavor_ara.220)・Hall of Worthies(flavor_KOR.txt:1893)・Guelph/Ghibelline・War of the Roses・Hundred Years War の各シチュエーション/ディザスターの実体を確認
- 「新文化 6 種」は spec のカウントを鵜呑みにせず、どの文化が 1.3 新規かはノート差分依存のため種別断定を保留（changelog 由来マーカー）。前バッチの宮廷芸術家 14→12 種の誤り捕捉に倣う
- austria/brandenburg からの被リンク相互更新は、両ガイドの 1.3 節を作成する次バッチ（国別）で実施
- 国別（ottoman/hungary 格上げ・austria・brandenburg・castile）・Tier4 は後続持越し

## 2026-06-17 EU5 1.3 オープンベータ差分 純追記（バッチ2: religion + byzantium）

### Added
- `eu5/eu5-religion-guide.md`: 「1.3 オープンベータ差分（宗教関連・純追記）」を追加（身分の宗教属性 `[src: estates/00_default.txt]`、低Devotionペナルティ `[src: auto_modifiers/country.txt]`、枢機卿+1%聖職者満足、市場言語話者バーガー同化のhard-block撤廃→超低速、Papacy→Lutheran議会バグ修正）。**Patriarch/Rite Power廃止は1.2変更のため1.3差分に再掲しない**旨を明記（B-5反映）
- `eu5/eu5-byzantium-guide.md`: 「1.3 オープンベータ差分（ビザンツ直接影響・純追記）」を追加（反ジェノヴァ盟約 `[src: events/DHE/flavor_byz_ven.txt]`、Born in the Purple `[src: heir_selections/monarchy.txt]`、1337国境修正、ジェノヴァ弩兵軽歩兵化 `[src: unit_types/1_uniques_for_age_2_renaissance.txt:69]`、船コスト増・海戦致死性のエーゲ海/ボスポラス影響、Twilight of the Tsardom=ブルガリア崩壊→再征服機会 `[src: disasters/twilight_of_the_tsardom.txt, events/DHE/flavor_BUL.txt]`）
- 両ガイドの用語対照表に「1.3 beta 仮登録」用語を追加、出典セクションに 1.3 スクリプトファイル・Patch 1.3 wiki を追記
- `index.html`: religion/byzantium カードに「1.3 beta差分」バッジを追加

### Notes
- byzantium 1.3項目は全て実機script実体確認済（反ジェノヴァ=flavor_byz_ven.txt / Born in the Purple=heir_selections/monarchy.txt+culture_greek.txt / Twilight=disasters/twilight_of_the_tsardom.txt+flavor_BUL.txt）。「1.3新規か否か」最終判定はノート差分による
- regional-guide・国別（ottoman/hungary格上げ・austria・brandenburg・castile）・Tier4 は次々セッション持越し

## 2026-06-17 EU5 1.3 オープンベータ差分 純追記（バッチ1: universal + government）

### Added
- 案A（純追記・差分セクション方式）で 1.3 open beta（buildid 23683141 / `1.3-open-beta`）の差分を**専用セクションとして純追記**。1.2「Echinades」本体章は一切変更せず、beta 起源の数値は本文に昇格させない方針
- `eu5/eu5-universal-guide.md`: 「1.3 オープンベータ差分（全国家影響・純追記）」を追加（経済=建物維持費逓増/利益率/mills 半減/バーガー交易範囲スケール `[src: age/00_default.txt]`、海軍・軍事=船コスト4x金/10x goods・陸軍goods2倍・正規vs徴募ダメボ撤廃・個別ユニット兵科再分類 `[src: unit_types/1_uniques_for_age_2_renaissance.txt:69]`、諜報=諜報網fog段階解除（**政府への潜入=1.2既存**の誤帰属注意付き）、自動化・宮廷芸術家12種 `[src: artist_types/00_default.txt]`）
- `eu5/eu5-government-guide.md`: 「1.3 オープンベータ差分（政府タイプ別・純追記）」を追加（身分の文化宗教 `[src: estates/00_default.txt]`、官僚制実装 `[src: bureaucracies/]`、低Devotion/低Republican Tradition ペナルティ `[src: auto_modifiers/country.txt]`、Prikazi/Collegium country_cabinet_efficiency=0.10 `[src: government_reforms/country_specific.txt:2407/2932]`、Voivode改革、退位コスト prestige50+legitimacy40 `[src: prices/03_diplomacy.txt:115]`、宮廷芸術家の廷臣管理）
- 両ガイドの用語対照表に「1.3 beta 仮登録」用語を追加（安定版で中央 localization-reference.md へ昇格予定）、出典セクションに 1.3 スクリプトファイル・Patch 1.3 wiki を追記
- `index.html`: universal/government カードに「1.3 beta差分」バッジ（`.tag--beta`）を追加

### Notes
- 残検証2件を実機で確定: ①Hall of Worthies = 集賢殿（country modifier `kor_hall_of_worthies_modifier`、イベント flavor_kor.28 経由）、②スパイ網fog = 「諜報網」構築による段階解除が1.3新規／「政府への潜入」は1.2既存と切り分け
- spec の誤りを実機検証で2点是正: 宮廷芸術家は **12種**（spec の14種は誤り）、官僚制の汎用は10種（generic.txt）
- regional-guide・国別（ottoman/hungary格上げ・austria・brandenburg・castile）・Tier4 は次々セッション持越し（CLAUDE.md「2バッチ上限」遵守）

## 2026-06-01 VIC3 プロイセン攻略ガイド ゼロベース書き直し（1.13.8 統一メカニクス再検証）

### Changed
- `vic3/vic3-prussia-guide.md` を全面書き直し（361 → 363 行、内容を日本ガイド水準に深化）。基準パッチをインストール版 **1.13.8 + EP2** に正確化し、ドイツ統一メカニクス・開始状態を explorer 2並列で再検証
- **核心の統一 JE チェーンを完全データ表化**（旧版は完了条件の記載なし）: je_schleswig_holstein_question → je_german_unification_idea → je_north/south_german_unification → je_german_unification の前提・完了条件・効果・技術ゲートを明記
- ツォルフェラインを「関税同盟」曖昧記述 → **パワーブロック（identity_trade_league、リーダー交易容量+25%、初期原則 principle_internal_trade_1）** として正確化
- **プロイセン教育修正（amendment_prussian_education、開始時付与・同化+10%/徴兵率+10%/軍部政治力+10%）** を新規記載（旧版は言及なし）
- 投機的な「UI導線（一般知識ベース）」節を削除し、検証済みメカニクスに置換

### Fixed
- 「裏取り予定」だったクーデター扇動・砲撃外交の実在を確認し昇格（`57_orchestrate_coup.txt` / `can_threaten_naval_hostilities` ルール `:226`）
- 技術ゲートを明確化: NGF/SGF JE = **nationalism**（era_2）、je_german_unification = **pan-nationalism**（era_3、ID ハイフン表記）
- GER 形成要件を明記: greater_germany 地域の **73%**（required_states_fraction=0.73）+ pan-nationalism または統一理念変数
- イベント ID `—` だった2件を**スクリプト上に不在と確定**: ツォルフェライン拡大イベント・ビスマルク社会立法イベントは未実装（拡大は外交、社会立法は法律改正で行う）
- ビスマルク（PRU_otto_von_bismarck）の所属 IG を ig_landowners、登用前提を pan-nationalism 研究済みと明記
- 開始状態を実測値に: 首都 STATE_BRANDENBURG、文化 north_german、国教 protestant、与党 IG（地主・軍部）
- `vic3/localization-reference.md`: 岩倉使節団 JE の説明を「外交承認の代替ルート」（JE スクリプトに根拠なし）→「生産・社会技術の研究加速 JE（外交承認フェーズと並行）」に訂正

## 2026-06-01 VIC3 日本攻略ガイド ゼロベース書き直し（1.13.8 全数値再検証）

### Changed
- `vic3/vic3-japan-guide.md` を全面書き直し（911 行 → 499 行）。基準パッチをインストール版 **1.13.8 + EP2** に正確化し、全数値を再検証
- 構成の整理（重複排除）:
  - 3 セクション（A/B/C）結合の痕跡を除去（文書途中の 2 つ目 H1 `# Section A`、`<!-- Section C -->` HTML コメント）
  - 重複していた鎖国法効果表（4 回 → 1 回）、維新発動条件（3 回 → 1 回）、大名 IG トレイト表（3 回 → 1 回）、法律改正ロードマップ（2 章 → 「技術・法律」に一本化）、出典セクション（2 つ → 末尾 1 つ）を統合
  - 海軍ドクトリンを独立セクション＋独立出典から「軍事ドクトリン（陸軍・海軍）」に統合
  - 「開国の軛」独立章を「外交・同盟」に吸収

### Fixed（再検証で判明した誤りの訂正）
- `law_free_ports` は**存在しない法律 ID**。鎖国の移行先を `law_mercantilism` に訂正（旧ガイドは「未検証」のまま放置）
- `force_recognition` 外交プレイ/CB は**スクリプト上に存在しない**。承認は `je_meiji_diplomacy` 完了で得る旨に訂正（慣用表現と明記）
- `law_bakufu` の所在を `00_social_hierarchy.txt`（誤）→ `00_distribution_of_power.txt:114`（正）に訂正、行番号未検証を解消
- 「プロミネンス +5 補正」は誤解釈。実際は `magnate_leader_weight +5`（大名リーダー選出重みの加算）に訂正 `[src: common/interest_groups/00_landowners.txt:751-762]`
- 岩倉使節団の社会技術ボーナスを +0.25%/stack（誤）→ +1%/stack（正）に訂正
- 維新 possible 条件を「law_sakoku/law_closed_borders でない」→「law_isolationism でない」に厳密化、je_meiji_army に `pm_no_organization` 兵舎条件を追加、je_meiji_economy を「70% 超（>0.7）」に厳密化
- 鎖国は前提に `law_traditionalism` が必要・九州外交易禁止（`country_disallow_trade_outside_kyushu_bool`）を追記
- キャラクターパスを `common/characters/`（誤）→ `common/character_templates/country_jap.txt`（正）に訂正
- 現行の朝鮮植民地化 JE は `07_korea_colonization.txt`（`03_korea.txt` は内乱系で別物）と明記
- 残存していた `（未検証）` マーカーをすべて解消（スクリプト確認または慣用表現への格下げ）
- 検証範囲: インストール版 1.13.8 のゲームスクリプト全数値を 3 トピック並列で再検証（明治維新/鎖国 JE・法律/IG/PM/人物・外交/技術/modifier/海軍/宗教/朝鮮）

## 2026-05-17 VIC3 日本攻略ガイド 新規追加（EP2 + 1.13 海軍改修対応）

### Added
- `vic3/vic3-japan-guide.md` 新規作成（911 行、EP2 The Great Wave + Patch 1.13 Matcha 対応）
  - パッチ 1.13 / DLC での日本関連変更点（砲撃外交・プロミネンス・単一指揮官制・戦略的関心度・海軍改修）
  - 開始状況（1836年）: 周辺国関係 / 強み・弱み / IG 構造特殊性（幕府/大名/学者）
  - 開国の軛（Unrecognized 脱却・不平等条約・関税）を序盤独立セクションとして配置
  - 時系列戦略 序盤（1836-1860）/ 中盤（1860-1880）/ 終盤（1880-1936）
  - 内政・経済（建設優先 / IG 管理（維新前後の遷移）/ プロミネンス活用 / 法律改正ロードマップ）
  - 外交・同盟（必須外交 / Unrecognized→Recognized 昇格ルート / 1.13 新外交手段）
  - 軍事ドクトリン（陸軍）+ 海軍ドクトリン（1.13 海軍改修反映、独立セクション）
  - 固有イベント時系列（明治維新JE 攻略チャート: kobu_gattai / kogi_yoron 2 分岐の表形式）
  - 技術・法律 / よくあるミス / 用語対照表 / 出典
- `index.html` の Victoria 3 セクションに日本カード追加
- スクリプト検証範囲: `common/journal_entries/00_meiji_restoration.txt`, `07_sakoku.txt`, `07_iwakura_mission.txt`, `07_japanese_religion.txt`, `07_korea_colonization.txt`, `common/laws/00_trade_policy.txt`, `common/interest_groups/00_landowners.txt`, `common/static_modifiers/00_ep2_04_modifiers.txt` 他（src マーカー 128 件、未検証マーカー 6 件、コミュニティ知見マーカー 40 件）
- EU4 派生メカニクス混入チェック完了（fabricate_claim / forge_claim / spy_network / 領有権主張捏造 / 理念グループ / 交易ノードはすべて不在確認、VIC3 固有の関税は注意書きで区別）

## 2026-05-17 ハンガリーガイド 序盤〜中盤 1.2 再整合

### Fixed
- 序盤〜中盤セクション（行 150〜394）の 1.0〜1.1 残存記述を一掃
  - `flavor_hun.2`（議会と摂政問題）トリガーに `has_parliament` 等 6 条件を明示。option A の貴族満足度を `mild_penalty` → `weak_penalty` に訂正
  - ドラゴン騎士団（`flavor_hun.410`）に `order_of_chivalry_law` 必須条件を明記
  - ヴィシェグラード会議（`flavor_hun.330`）にカローイ・ロベルト＋カジミェシュ 3 世のキャラクター存命条件を追記、成立時の `union_of_crowns_succession` 継承法変更も追加
  - マティアス・コルヴィヌス（`flavor_hun.110`）が `dynasty:hunyadi_dynasty` 判定で固有キャラ ID 不在であることを注記
- 市場中心ロケーション誤記を修正: ブダ（首都・wine 産地）に市場を建てる記述 → ペスト（wheat 穀倉地、`is_market_center`）の市場ツリー強化に修正（Day 1 とフェーズ 1 の 2 箇所）
- EU4 派生メカニクスの除去:
  - 「諜報→請求権捏造（fabricate_claim）」前提の戦略記述を削除（EU5 1.2 に `spy_actions/` 自体が存在せず、`scripted_relations/` のスパイ網にも Claim 付与効果なし）
  - ボスニアを「ライバル設定」対象から除外。`flavor_BOS.txt:28` の `is_subject_of = c:HUN` で開始時 HUN 属国を間接確認、`disloyal_subject` CB 経路に統一
  - CB 取得ルートを `cb_conquer_enemy`（ライバル相手・コア不要）/ `cb_conquer_province`（コア要、Claims on Province）に分離

### Added
- `eu5/localization-reference.md` の CB セクションに 4 項目追加: Claims on Province / Dubious Claims / Conquer Enemy / Disloyal Subject。「EU4 のスパイ請求権捏造は EU5 に存在しない」を Dubious Claims の補足として明記
- ハンガリーガイド本文の用語対照表に同 4 項目を追記（`flavor_BOS.txt:28` 出典も付与）
- `.gitignore` に `_staging/` を追加（subagent の script-check / review メモは local のみ保持）

### Changed
- `CLAUDE.md` に学び 5 件追記: EU4 派生メカニクス横断スキャン・市場の location 依存・属国スタートの間接確認・ユーザー指摘起点の researcher 即委任パターン・追加検証フロー

## 2026-05-16 ハンガリーガイド ビザンツ並み粒度に拡張

### Added
- EU5 ハンガリー攻略ガイド（`eu5/eu5-hungary-guide.md`）: 524 行 → 約 1000 行に拡張
  - 軍事ドクトリン: 黒軍・ハンガリー・フサール・ハイドゥクをユニット別深掘り（script verified）
  - 後半戦略 1500-1700 章を新設（HRE/PU ルート、Mohács 局面、オーストリア＝ハンガリー逆転ルート、首都避難）
  - 序盤戦略を 3 フェーズに細分化（バルカン前準備・バルカン拡張・黒死病対策と中盤準備）
  - 固有イベント表を 59 イベントに拡張（B-1〜B-21 全網羅）
  - アドバンス取得ロードマップを追加
  - 用語対照表を 16 用語追加（黒軍・フサール・ハイドゥク・ヴェグヴァール体制・黒軍政策・フニャディ等）
  - wiki 由来から script verified に格上げ: 11 ファイル・29 項目

## 2026-05-16

### Fixed
- 「破壊的変更」マーカーの表記揺れを統一（`eu5-austria-guide.md` 行21・`eu5-universal-guide.md` 行19/32）
  - 表セル・箇条書きの行内マーカーを `（**破壊的変更**）`（括弧＋太字）に統一
  - 見出し内・地の文での使用は文脈上適切なため変更なし

- 汎用ガイド（`eu5/eu5-universal-guide.md`）: Complacency（慢心）テーブルの単位誤記を修正
  - 表ヘッダ「値（慢心 1 ポイントあたり）」→「慢心 100（最大）時の値」に修正
  - スクリプト `auto_modifiers/country.txt:419-422` の `scales_with multiply = 0.01` により効果は慢心値（0〜100）× 0.01 で線形スケールすることをスケール仕様として明記
  - 漏れていた正効果 `global_monthly_prosperity = +0.01`（最大時 +1%）を追加
  - 出典マーカーを `[src: コミュニティ知見・スクリプト未確認]` → `[src: country.txt:413-441 + script verified]` に昇格

### Changed
- ビザンツガイド（`eu5/eu5-byzantium-guide.md`）: レビュー指摘修正（矛盾解消・訳語修正・出典統一）
  - A: 「攻撃戦争は 1400 年まで厳禁」→「全面戦争は 1400 年まで厳禁（限定的奪還戦は例外）」に修正し、奪還検討目標リストに前提条件を追加（矛盾解消）
  - B: `strength_vs_overlord` の説明「抵抗減」→「宗主国への反乱強度 -50%」、`ticking_war_score` に単位「/月」追加、「ローカライゼーション条件」→「Hellenization 閾値条件」に修正
  - C: 統合軍備ボーナスに `[src: コミュニティ知見・スクリプト未確認]` マーカー追加、`christian.txt` 出典を「正教固有か共通かは未確認」付きに変更
  - D: `bureaucracies/byz.txt` を参照ファイル欄から一次情報欄へ格上げ、重複していた「スクリプト検証済み項目の一覧」セクションを削除して出典テーブル参照に置換
  - E: アドバンス表の「ビザンツ固有進歩（確認中）」空欄行を削除

### Added
- EU5 ビザンツ帝国攻略ガイド（`eu5/eu5-byzantium-guide.md`）新規作成、1015 行
  - Patch 1.2「Echinades」/ DLC Fate of the Phoenix の主役国家
  - 全12章構成（パッチ差分・1337開始状況・Day 1・序盤/中盤/後半戦略・軍事・外交・内政・固有イベント・固有Advance・よくあるミス・用語・出典）
  - DLC スクリプト一次検証済み: Restore Roman Borders CB / Pronoia サブジェクト / Katepanata 政体 / Cataphracts / Legionaries / Greek Fire Ships / Greek Fire Infantry / Varangians / Latinization vs Hellenization / 1337 開始状態（stability -45 / gold -300 / war_exhaustion 10）/ 正教 maximum_religious_influence 400
  - スクリプト出典マーカー 131 箇所、コミュニティ知見明示 48 箇所
- `eu5/localization-reference.md` にビザンツ固有用語 24 件追加（Pronoia / Katepanata / Cataphracts / Legionaries / Varangians / Greek Fire / Latinization vs Hellenization / Byzantine Succession Crisis 等）
- `index.html` にビザンツガイドカード追加（カスティーリャ枠の次）

### Changed
- `eu5/eu5-regional-guide.md` のビザンツ評価「⚠ 非推奨」→「★★★ 上級」に昇格、新ガイドへの相互リンク追加
  - DLC Fate of the Phoenix 実装により復興パスが確立されたため

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
