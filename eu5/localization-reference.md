# EU5 ローカライズ対照表

> ゲーム内日本語表示の正本。攻略ガイドの用語はこのファイルを参照して統一する。
> 出典: `C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis V\game\main_menu\localization\japanese\` 配下の各 `.yml` ファイル
> 確認パッチ: **1.1.10**（2026-03-30 確認）

---

## 基本概念

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Crown Power | 君主力 | 君主と階級の力関係 |
| Stability | 安定度 | 国家の安定性 |
| Prestige | 威信 | 国家威信 |
| Legitimacy | 正統性 | 君主の正統性 |
| Control | 支配度 | 州の実効支配度 |
| Antagonism | 敵対心 | 拡張に対する反発 |
| Opinion | 評価 | 国家間の関係値 |
| Trust | 信頼度 | 同盟の信頼蓄積 |
| Favor | 好感度 | 同盟国との蓄積関係値 |
| Manpower | 人的資源 | 兵士の補充プール |
| Inflation | インフレ | 通貨膨張 |
| Development | 開発度 | 州の発展度 |
| Population | 人口 | 州の人口 |
| Institution | 制度 | 技術伝播の仕組み |
| Advance | 進歩 | 技術・制度・国家固有ツリー |
| Age | 時代 | ゲーム内の時代区分 |
| Government | 政府 | 政体 |
| Government Reform | 政府改革 | 政体の改革オプション |
| Road | 街道 | 近接ペナルティ軽減 |
| Cabinet | 内閣 | 高官による統治機構 |
| Cabinet Action | 内閣アクション | 内閣が実行する行動 |
| Cabinet Efficiency | 内閣効率 | 内閣の効率値 |
| Spy Network | 諜報網 | スパイ活動の成果 |
| RGO / Resource Gathering Operations | RGO / 資源採取 | ゲーム内でも「RGO」とアルファベット表記 |

## 階級（Estate）

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Estate | 階級 | 貴族・聖職者・市民・庶民の総称 |
| Nobles | 貴族 | `nobles_estate` |
| Clergy | 聖職者 | `clergy_estate` |
| Burghers | 市民 | `burghers_estate` |
| Peasants | 庶民 | `peasants_estate`。Commoners も同じ階級を指す |
| Estate Power | 階級権力 | 各階級の権力値 |

> **注意**: EU5 では「Peasants」の日本語訳は「**庶民**」であり「農民」ではない。攻略ガイドでは必ず「庶民」を使用すること。

## 外交

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Alliance | 同盟 | 軍事同盟 |
| Royal Marriage | 王室間の婚姻 | 王族同士の婚姻外交 |
| Personal Union | 同君連合 | 同じ統治者を戴く連合 |
| Improve Relations | 関係改善 | 外交アクション |
| Guarantee | 独立保障 | 他国の独立を保障 |
| Truce | 停戦 | 戦争終了後の停戦期間 |
| Call to Arms | 参戦要請 | 同盟国への参戦要請 |
| Peace Treaty | 和平条約 | 戦争の終結条件 |
| War Score | 戦勝点 | 戦争の優劣を示す値 |
| War Participation | 戦争貢献度 | 同盟戦争での貢献度 |
| Diplomatic Range | 外交範囲 | 外交可能な距離 |
| Diplomatic Capacity | 外交許容量 | 維持可能な外交関係数 |
| Diplomatic Reputation | 外交評判 | 外交的な信用度 |

## 従属国

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Subject | 従属国 | 従属国の総称 |
| Overlord | 宗主国 | 従属国の主人 |
| Vassal | 属国 | 代表的な従属国形態 |
| March | 辺境伯領 | 軍事特化の従属国。分権化ペナルティが軽い |
| Fiefdom | 封土 | 主に君主制向けの従属形態 |
| Appanage | アパナージュ | 王族への領地分与 |
| Tributary | 朝貢国 | 貢物を納める従属国 |
| Colonial Nation | 植民地国家 | 植民地の自治国 |
| Dominion | 自治領 | 自治権を持つ従属国 |
| Trade Company | 交易会社 | 交易特化の従属組織 |
| Imperial Free City | 帝国自由都市 | HRE の自由都市 |
| Integrate | 統合 | 従属国を自国に吸収 |
| Annex | 併合 | 他国を完全に吸収 |
| Subject Loyalty | 従属国忠誠度 | 従属国の忠誠度 |
| Liberty Desire | 独立欲求 | 従属国の独立志向 |

## 開戦事由（Casus Belli）

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Casus Belli | 開戦事由 | 戦争の正当化根拠。略称 CB |
| War Goal | 戦争目標 | 戦争で達成すべき目標 |
| Claims on Province | 州の請求 | 領有権主張に基づく CB |
| Fabricated Claims | 州の請求（根拠なし） | 捏造した請求権 |
| Claim Throne | 王位の請求 | 王位を請求する CB |
| Crusade | 十字軍 | 宗教的大義の CB |
| Humiliate Rival | ライバルに屈辱を与える | ライバル国への CB |
| Imperialism | 帝国主義 | 後半の汎用 CB |
| Border Dispute | 国境紛争 | 隣接国との紛争 CB |
| Coalition | 包囲網 | 敵対心が高い国の連合 CB |
| Imperial Ban | 帝国の禁令 | HRE 内の CB |

## 軍事

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Battle | 戦闘 | 軍同士の戦い |
| Combat Power | 戦闘力 | 部隊の戦闘能力 |
| Morale | 士気 | 部隊の戦意 |
| Discipline | 規律 | 部隊の規律度 |
| Combined Arms | 統合軍備 | 多兵科混成ボーナス |
| Frontage | 戦闘幅 | 戦場に展開できる部隊幅 |
| Bombard Phase | 砲撃フェーズ | 戦闘の砲撃段階 |
| Combat Phase | 戦闘フェーズ | 戦闘の接近段階 |
| Attrition | 消耗 | 部隊の自然減少 |
| Reinforcement | 補充 | 部隊の兵員回復 |
| Siege | 包囲 | 要塞の包囲攻撃 |
| Assault | 突撃 | 要塞への直接攻撃 |
| Garrison | 守備隊 | 要塞の防衛部隊 |
| Zone of Control | 支配領域（ZoC） | 要塞の影響範囲 |
| General | 将軍 | 陸軍指揮官 |
| Admiral | 提督 | 海軍指揮官 |
| General Trait | 将軍特性 | 将軍の固有能力 |
| Army Tradition | 陸軍伝統 | 陸軍の伝統値 |
| Retreat | 撤退 | 戦闘からの撤退 |
| Levy | 召集軍 | 人口から直接動員する軍 |
| Regulars | 正規軍 | 常備軍 |

## 建造物

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Marketplace | 市場 | 交易収入を増やす |
| Grand Marketplace | 大市場 | 市場の上位 |
| Hospital | 病院 | 疫病対策 |
| Bridge | 橋 | 湖・河川の近接障壁を解消 |
| Lumber Mill | 製材所 | 建設資材を生産 |
| Workshop | 工房 | 生産効率を向上 |
| Temple | 寺院 | 宗教施設 |
| University | 大学 | 教育・制度伝播 |
| Granary | 穀物庫 | 食料貯蔵 |
| Barracks | 兵舎 | 軍事施設 |
| Fortification / Fortress | 要塞 | 防衛施設。ZoC を発生 |
| Star Fort | 星形要塞 | 要塞の上位 |
| Dock | ドック | 海軍施設 |
| Shipyard | 造船所 | 艦船建造 |

## 宗教

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Tolerance Own | 自国宗教寛容度 | 自国宗教への寛容さ |
| Tolerance Heretic | 異端寛容度 | 異端への寛容さ |
| Tolerance Heathen | 異教寛容度 | 異教への寛容さ |
| Religious Influence | 宗教的影響力 | 宗教の影響力値 |
| National Church Power Cost | 国教会権力コスト | 国教会の権力行使コスト |

## 神聖ローマ帝国（HRE）

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Holy Roman Empire | 神聖ローマ帝国 | 略称 HRE |
| Emperor | 皇帝 | HRE の首長 |
| Elector | 選帝侯 | 皇帝選挙の投票権者 |

---

## 運用ルール

- 攻略ガイドの用語はこのファイルを**正本**とする
- ゲーム内日本語が変更された場合、このファイルを更新し、各ガイドの用語対照表も合わせる
- 各ガイドの用語対照表にはそのガイドで使う用語のみ抜粋し、完全版はここを参照する
- 新しい用語を追加する場合は、必ずゲーム内ローカライズファイルで確認してから追加する
