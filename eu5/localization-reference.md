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
| Emperor | 皇帝 | HRE の首長。選帝侯の投票で選出される |
| Elector | 選帝侯 | 皇帝選挙の投票権者。最大 7 名 |
| Imperial Authority | 帝国の権威 | 略称 IA。皇帝権力の強さを示す 0〜100 の指標 |
| Imperial Reform | 帝国改革 | IA を消費して HRE の制度を強化するアクション |
| Landfriede | ラント平和令 | HRE 内の諸侯間戦争を禁じる帝国法 |
| Golden Bull | 金印勅書 | 神聖ローマ帝国の基本法。選帝侯の権限を規定 |
| Imperial Diet | 帝国議会 | HRE の立法機関。帝国改革の審議の場 |
| Imperial Succession | 帝位継承 | 皇帝死亡時の選帝侯投票による後継者選出 |
| Demand Unlawful Territory | 不法領土の返還要求 | 非 HRE 国が保有する帝国領を取り返す外交アクション |

## カスティーリャ / スペイン固有

### 固有進歩

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| cas_repoblaciones | 移民の誘致 | 伝統の時代。繁栄+0.001、移住速度+10% |
| cas_the_reconquista | レコンキスタ | 伝統の時代。陸軍士気+15% |
| cas_castilian_navy | カスティーリャ海軍 | ルネサンスの時代。海上プレゼンス+10%、重船+15% |
| cas_cronicas_reales | 王国年代記 | ルネサンスの時代。文化伝統+10%、月間威信+0.1 |
| cas_masters_of_the_orders | 修道会の主 | 大航海の時代。月間陸軍伝統+0.05 |
| cas_new_world | 新大陸 | 大航海の時代。植民移住+25%、植民範囲+25% |
| cas_reform_of_millones | ミジョネスの改革 | 宗教改革の時代。税収効率大ボーナス |
| cas_marine_infantry | カスティーリャ海軍歩兵 | 宗教改革の時代。上陸速度+25%、海軍士気+10% |
| cas_pasos | カスティーリャのパソス | 絶対主義の時代。正統信仰寛容+1 |
| cas_real_academia_espanola | スペイン王立アカデミー | 絶対主義の時代。月間識字率+0.02 |
| cas_canal_de_castilla | カスティーリャ運河 | 革命の時代。月間食料+20% |
| cas_royal_factories | 王立工場 | 革命の時代。生産効率大ボーナス |

### 政府改革・政策

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Casa de Contratación | 通商院 | 植民地貿易の統括機関 |
| Royal Council of Castile | カスティーリャ王立評議会 | 内政改革 |
| Nueva Planta | ヌエバ・プランタ | アラゴン・カタルーニャの法制度改革 |
| Spanish Tolerance | イベリアの寛容 | 異端審問を拒否した場合の政府改革 |
| Royal Fifth / Quinto Real | 王室五分税 | 植民地産出への課税 |
| Mesta Council | メスタ会議 | 羊毛組合の法的特権 |
| Right of Possession | 占有権 | メスタの拡大政策 |
| Laws of Burgos | ブルゴス法 | エンコミエンダ制の法的基盤 |
| New Laws of the Indies | インディアス新法 | エンコミエンダ廃止法 |
| Nueva Recopilación | 新法令集 | 法典集成 |
| Leyes de Toro | トロ法 | 法制度改革 |

### 固有メカニクス・制度

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Reconquista | レコンキスタ | イベリア半島のキリスト教再征服 |
| Encomienda | エンコミエンダ | 植民地の先住民統治制度 |
| Mesta | メスタ | カスティーリャの羊毛組合 |
| Mita | ミタ制 | アンデスの強制労働制度 |
| Spanish Inquisition | 異端審問所 | 宗教政策の中核機関 |
| Comuneros | コムネロス | 都市共同体の反乱運動 |
| Intendancy | 総督制度 | ブルボン改革の行政機構 |

### 固有建造物

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Archive of the Indies | インド諸島の記録保管所 | 植民地文書館 |
| Royal Audience and Chancery | 王室大法官裁判所 | 行政・司法機関 |
| Sevilla Bullfighting School | セビリア闘牛学校 | 文化施設 |
| El Escorial Palace | エル・エスコリアル宮殿 | 威信ボーナス |
| School of Salamanca | サラマンカ学派 | 学術施設 |
| Segovia Artillery Academy | セゴビアの砲兵アカデミー | 軍事施設 |

### 主要イベント名

| 英語キー / ID | ゲーム内日本語 | 補足 |
|---------------|---------------|------|
| flavor_cas.2200 | イベリアの結婚 | ARA or POR との婚姻連鎖 |
| flavor_cas.85 | イベリア連合 | スペイン形成イベント |
| flavor_cas.22 | カトリック王の称号 | 教皇庁との関係で発火 |
| flavor_cas.1000 | トルケマダとスペイン語の異端審問 | 異端審問所設立の分岐点 |
| flavor_cas.1001 | アルハンブラ勅令 | ユダヤ人追放令 |
| flavor_cas.1002 | アンダルシア人の民の改宗 | モリスコ強制改宗 |
| flavor_cas.1502 | 太陽の沈まぬ国 | 4大陸制覇ボーナス |
| flavor_cas.1500 | 通商院 | 植民地貿易政府改革 |
| flavor_cas_rio_salado.1 | モロッコの脅威 | リオ・サラドの戦い連鎖開始 |
| flavor_cas.1800 | コムネロスの組織 | 都市反乱連鎖 |
| flavor_cas.102 | ヌエバ・プランタ法令 | アラゴン法制度改革 |

## イベリア文化共通ユニット

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| Tercio | テルシオ | 宗教改革の時代。イベリア文化共通の歩兵ユニット |
| Catalan Galley | カタルーニャ・ガレー船 | 伝統の時代。初期海軍 |
| Early Iberian Caravel | 初期イベリア・カラベル船 | 伝統の時代 |
| Iberian Caravel | イベリア・カラベル船 | ルネサンスの時代 |
| Early Iberian Galleon | 初期イベリア・ガレオン船 | 大航海の時代 |
| Square-rigged Caravel | 横帆カラベル船 | 大航海の時代 |
| Iberian Galleon | イベリア・ガレオン船 | 宗教改革の時代。重船の頂点 |
| Lanzas de Castilla | カスティーリャ騎槍兵 | 大航海の時代。CAS 専用 |

## スペイン形成

| 英語キー | ゲーム内日本語 | 補足 |
|----------|---------------|------|
| SPA / Spain | スペイン | CAS からの国家形成 |

---

## 運用ルール

- 攻略ガイドの用語はこのファイルを**正本**とする
- ゲーム内日本語が変更された場合、このファイルを更新し、各ガイドの用語対照表も合わせる
- 各ガイドの用語対照表にはそのガイドで使う用語のみ抜粋し、完全版はここを参照する
- 新しい用語を追加する場合は、必ずゲーム内ローカライズファイルで確認してから追加する
