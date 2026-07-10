# EU5 1.3 オープンベータ ガイド更新案（確定版 v2 / マルチエージェントレビュー反映済）

対象: `paradox-game-guides/eu5/` 全12ファイル。現行は全て **1.2「Echinades」基準**。
検証ソース: ローカル1.3 open beta（buildid 23683141, BetaKey `1.3-open-beta`）スクリプト + 公式1.3.0/1.3.2パッチノート + **1.2/1.3パッチノート突き合わせ**（diff確定）。
**2026-07-10 安定版プリフライト後の基準更新**: 安定版 buildid 24075414（= 1.3.10、2026-07-09に正式stable昇格。UserConfig.BetaKey=`public`）に基準変更。再検証結果は `_staging/2026-07-10-eu5-13-stable-reverify.md` 参照。
レビュー: 正確性/網羅性/戦略構成の3エージェント（`review-accuracy.md` / `review-coverage.md` / `review-strategy.md`）反映済。

---

## 0. 方針 = 案A（純追記・差分セクション）【確定】

1.2を検証済みベースラインとして維持し、各ガイドに「1.3 オープンベータ差分」セクションを**純追記**する。理由: ①CLAUDE.md「インストール版固定・ベータ追従禁止」は"本体章の書き換え禁止"を意図したものであり、純追記の新規セクションはスコープ外、②読者多数派の live版(1.2)の足場を残す、③ローカル1.3 betaスクリプトで検証した差分を早期提供できる。

### 案A の実施制約（レビューA-1/A-2 critical 反映・必須）
1. **1.2本体章を一切変更しない純追記**。差分は専用セクション内に封じ込める。
2. **beta起源の数値を本文に昇格させない**（安定版まで差分セクション内に留める）。
3. 差分セクション冒頭に「本セクションは1.3 betaスクリプト/パッチノートを独立検証基準とし、上位の1.2 baselineとは独立」と明記。

### 昇格フロー（1.3安定版リリース後・レビューA-2反映）
①差分ブロックを本文該当章に統合 → ②マーカー昇格（後述）→ ③差分セクション削除 → ④パッチ差分テーブルに「Patch 1.3」行追記 → ⑤用語を正式登録 → ⑥CHANGELOG更新。

### 信頼性マーカー（レビューB-1 critical 反映）
新マーカーは**単体使用禁止**。既存3種体系に重ねる:
- beta検証済（script実値あり）: `[src: ファイル名:識別子]（1.3 beta・変動注意）`
- changelog由来（script実値なし）: `（コミュニティ知見：1.3 beta、公式パッチノート由来・スクリプト未確認）`
- 各変更は**1行1マーカーで分割**（総括ブロック禁止・レビューB-3反映）。

---

## 1. 数値検証の最終ステータス（実装時の出典確定表）

| 主張 | 検証結果 | 実装時マーカー |
|------|---------|--------------|
| ジェノヴァ弩兵→軽歩兵 | ✅script一致 `unit_types/1_uniques_for_age_2_renaissance.txt:69` ＋1.3新規(ノート差分) | `[src:...]（1.3 beta）` |
| Hobelar/Hakkapeliitta→軽騎兵 | ✅script一致（copy_from軽騎兵テンプレ）＋1.3新規 | `[src:...]（1.3 beta）` |
| Mamluk Horsemen 重騎兵 | ✅script一致（age1/2の2段）＋1.3追加(ノート) | `[src:...]（1.3 beta）` |
| 低devotionペナルティ 月次宗教影響 -0.1 | ✅script一致 `auto_modifiers/country.txt:611`（scales_with devotion） | `[src:...]（1.3 beta）` |
| バーガー交易範囲 600→1100 | ✅script一致 `age/00_default.txt`（age1=600, age2〜6で各+100, age6=1100） | `[src:...]（1.3 beta）` |
| Prikazi/Collegium 0.15/0.20→0.10 | ✅**1.3真正変更**（1.2ノート未記載／1.3ノート明記）。現値0.10は`country_specific.txt:2407/2932`で確認 | `[src:...]（1.3 beta）`＋旧値はノート出典 |
| 船コスト4x金/10x goods/維持下限10% | ⚠script実値なし・**1.3真正変更**(ノート差分確定) | changelog由来マーカー |
| 利益率 ギルド10/WS15/マニュ20/ミル25%・mills_employment半減 | ⚠script実値なし(エンジン内部)・1.3真正変更(ノート) | changelog由来マーカー |
| 建物維持費 1世紀で+50% | ⚠script実値なし・1.3真正変更(ノート。1.2はinflation影響化のみ) | changelog由来マーカー |
| 陸軍goods需要2倍 | ⚠script diff不可・1.3真正変更(ノート) | changelog由来マーカー |
| 正規兵vs徴募兵ダメボ撤廃 | ⚠script痕跡なし・1.3変更(ノート) | changelog由来マーカー |
| スパイ網fog解除 | ⚠1.3新規だが**Infiltrate Administrationは1.2既存**→文言注意 | changelog由来＋誤記回避 |
| Korea研究ナーフ(Hall of Worthies) | ⚠`country_KOR.txt`に研究値なし→**Hall of Worthiesの所在を実装前に特定**（別advance/building/reform） | 特定後に判定。不可なら言及保留 |

---

## 2. 1.3変更 → 影響ガイドのマッピング（レビュー反映後）

### 全国家影響（universal-guide.md）
建物維持費逓増/船コスト/陸軍goods2倍/利益率・mills/市場吸引力/交易範囲scaling/海戦致死性↑/兵科再分類/正規vs徴募ダメボ撤廃/要塞兵士雇用↓/補助連隊食料+50%/自動化(Members・Actions分割+外交+建物/RGO自動拡張)/スパイ網fog解除(文言注意)/連合スノーボール抑制(Dissolve Coalition 75→20)。
**＋宮廷芸術家刷新（レビューA-1 critical・欠落補填）**: `artist_types/00_default.txt`の14種、`invite_artist.txt`の制約 → 廷臣/内政章に追記。

### government-guide.md
身分の文化・宗教(全政体)/新政府改革17種/bureaucracy10種/低devotionペナルティ(devotion型)/共和制低republican traditionペナルティ/Prikazi・Collegium 0.10/Voivode改革/退位コスト/内閣2長封鎖/内閣自動化Members・Actions分割。**＋宮廷芸術家の廷臣管理（A-1）**。

### religion-guide.md
身分の宗教/枢機卿+1%聖職者満足/低devotionペナルティ/市場言語話者バーガー同化(hard-block撤廃→超低速)/Papacy→Lutheran議会バグ修正。**Patriarch/Rite Power廃止は1.2変更のため既存記述か要確認（レビューB-5）**。

### regional-guide.md
- **西欧章**: 百年戦争リバランス(仏初期国力・Appanage弱体・Influence French Subject再スケール・騎士的貴族徴募減)、薔薇戦争(ブリテン)。
- **イタリア章**: **ゲルフ/ギベリン改修（レビューA-2 critical・西欧章から移動）**。
- **イベリア章(アラゴン)**: **Taula de Canvi銀行（レビューA-5・castileから移動）**。
- **東欧・バルカン章**: **Twilight of the Tsardom（レビューA-3 critical）**、Voivode(ポーランド/カルパチア)。
- **各地域章**: RGO再分配(Iron/Wool/Horses/Beeswax)。
- **概要/東アジア**: 植民移民拡大、新文化6種、ギリシャ語地名、天然痘亜熱帯化(1.3.2で0.1→0.05+閾値15%)、Korea研究ナーフ(所在特定後)。

### byzantium-guide.md
反ジェノヴァ盟約(ヴェネツィア)/Born in the Purple/1337国境修正/ジェノヴァ弩兵軽歩兵化。**＋船コスト・海戦致死性のエーゲ海/ボスポラス影響（レビューB-4）**。**＋Twilight of the Tsardom=ブルガリア崩壊の機会（A-3）**。

### 国別（次セッション）
- **ottoman**: **Tier2格上げ（レビューB-1 critical）**。船コスト4x/10x・建物維持費+50%を海軍/貿易/内政章に数値明記。
- **hungary**: **陸軍goods2倍=黒軍コスト直撃を軍事章に（B-2 critical）**。Union of Crowns女性継承＋**`no_female_heirs_for_poland`例外注記（A-7・対ポーランドPU）**。
- **austria**: HRE加入reluctance・**宗教統一強制を従属国に不可（B-3でTier2相当）**・土地剥奪が皇帝の手に。
- **brandenburg**: HRE変更・Voivode。**Berenberg銀行のBrandenburg影響はscript未確認→ハンブルク固有なので無理に紐付けない（A-5）**。
- **castile**: 船コスト・海軍・経済全般（Taula de Canvi はregionalへ移管済）。

### Tier4
recommended-mods（1.3 beta互換注記）/localization-reference（家族銀行・Voivode・身分の文化宗教・Twilight of the Tsardom・Mamluk Horsemen・宮廷芸術家 等の中央昇格）。

---

## 3. 実施シーケンス（レビューD-1反映・2バッチ上限厳守）

- **検証残務（先行・軽量）**: ①Korea「Hall of Worthies」の所在特定 ②スパイ網fogの文言確定（Infiltrate Administration=1.2既存を踏まえる）。※経済数値の出典は本v2で確定済。
- **バッチ1**: Tier1 = universal + government（宮廷芸術家含む）。各変更1行1マーカー。
- **バッチ2**: religion + byzantium。
- **次セッション バッチ1**: regional-guide単独（検証ポイント最多のため分離・レビューD-1）。
- **次セッション バッチ2**: 国別(ottoman/hungary格上げ・austria・brandenburg・castile)。
- **次セッション 仕上げ**: Tier4(localization中央昇格・index.htmlバッジ・CHANGELOG)。

### 章追加4点セット（各バッチで同コミット・レビューC反映）
新語→当該ガイド末尾用語表に**仮登録(beta扱い)** / 出典セクション追記 / パッチ差分テーブルに1.3根拠 / CHANGELOG。中央`localization-reference.md`への昇格はTier4。**index.htmlは「既存カードに1.3 betaバッジ追加」スコープ → バッジを付けるバッチと同コミット（レビューC-1）**。regional更新時はbyzantium/austria/brandenburgからの被リンク相互更新（レビューC-2）。

---

## 4. 残ユーザー確認
1. 実装着手のタイミング（本セッション バッチ1 / 次セッション）。CLAUDE.md「レビュー+実装はセッション分割」推奨に従うなら次セッション。
2. 北イタリア都市国家(ピサ/シエナ/ルッカ/モンフェラート)の新規国別ガイド作成は別タスク（本案外）。
