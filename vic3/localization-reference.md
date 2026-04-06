# VIC3 ローカライズ対照表

> ゲーム内日本語表示の正本。攻略ガイドの用語はこのファイルを参照して統一する。
> 出典: `C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game\localization\japanese\` 配下の各 `.yml` ファイル
> 確認パッチ: **1.12.4**（2026-03-31 確認）

---

## 基本概念

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Prestige | 威信 | 国家の格 |
| Infamy | 悪名 | 外交的な悪評。高いと包囲網を招く |
| Authority | 権力 | 政府の統治力 |
| Legitimacy | 正当性 | 政府の正当性 |
| Bureaucracy | 行政力 | 制度運営に必要なリソース |
| GDP | 国内総生産 | 経済規模の指標 |
| Standard of Living | 生活水準 | Pop の生活の質 |
| Literacy | 識字率 | 技術伝播速度に影響 |
| Innovation | 革新 | 技術進歩の速度 |

## 利益団体（Interest Group）

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Interest Group | 利益団体 | 略称 IG |
| Landowners | 地主 | 保守的。農業利益を代表 |
| Industrialists | 実業家 | 工業化推進派 |
| Armed Forces | 軍部 | 軍事重視 |
| Devout | 信者 | 宗教勢力 |
| Intelligentsia | 知識人 | 進歩的。教育・自由主義 |
| Petite Bourgeoisie | 小ブルジョワ | 中産階級 |
| Trade Unions | 労働組合 | 労働者の利益を代表 |
| Rural Folk | 農村民 | 農村部の庶民 |

> **補足**: ゲーム内のキーは `ig_rural_folk`、`ig_devout` 等の形式。`interest_groups_l_japanese.yml` で確認済み。

## Pop Types

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Aristocrats | 貴族 | 上流階級 |
| Capitalists | 資本家 | 工場所有者 |
| Officers | 士官 | 軍の指揮官層 |
| Clergy | 聖職者 | 宗教関係者 |
| Academics | 学者 | 研究・教育 |
| Engineers | 技師 | 技術者 |
| Bureaucrats | 公務員 | 行政担当 |
| Shopkeepers | 商店主 | 小規模商業 |
| Clerks | 事務員 | 事務労働者 |
| Laborers | 労働者 | 工場労働者 |
| Peasants | 百姓 | 自給自足の農業従事者 |
| Machinists | 機械工 | 熟練工 |
| Farmers | 農家 | 商業農業従事者 |
| Slaves | 奴隷 | 奴隷制下の労働者 |
| Soldiers | 兵士 | 常備軍の兵 |

> **注意**: VIC3 の「Peasants」は「**百姓**」。EU5 の「庶民」、CK3 の訳語とも異なる。タイトルごとに正式訳を確認すること。

## 軍事

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Army | 陸軍 | 地上軍 |
| Fleet / Navy | 海軍 | ゲーム内キーは `concept_fleet` |
| Conscription | 徴兵 | 動員法による兵力確保 |
| General | 将軍 | 陸軍指揮官 |
| Admiral | 提督 | 海軍指揮官 |
| Barracks | 兵舎 | 陸軍施設 |
| Naval Base | 海軍基地 | 海軍施設 |
| War Goal | 戦争目標 | 戦争で達成すべき目標 |
| Diplomatic Play | 外交戦 | 戦争前の外交的駆け引き |
| Battalion | 大隊 | 軍事ユニットの基本単位 |
| Military Formation | 軍事ユニットグループ | 大隊をまとめた編隊 |
| Front | 戦線 | 戦闘が行われる前線 |
| Battle | 戦闘 | 前線上の個別の戦闘 |
| Mobilization | 動員 | 大隊を戦線に配備すること |
| Occupation | 占領 | 敵州の掌握 |
| War Exhaustion | 厭戦 | 長期戦で上昇する国民の疲弊度 |
| War Support | 戦争支持率 | 国民の戦争への支持度 |
| Power Projection | 戦力投射 | 威信・外交力に影響する軍事力指標 |
| Morale | 士気 | 戦闘中の大隊の意気 |
| Combat Width | 戦場の幅 | 一度に戦線に参加できる大隊数 |
| Supply | 供給 | 大隊の維持に必要な補給 |
| Blockade | 封鎖 | 港の封鎖。貿易・収入に影響 |
| Command Limit | 指揮限界 | 将軍1人が指揮できる大隊の上限 |
| Standing Army | 常備軍 | 常設の職業軍人部隊（技術） |
| Mandatory Service | 国民皆兵 | 大規模徴兵制の技術 |

### 陸軍兵種

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Irregular Infantry | 非正規軍 | 初期の歩兵。コスト低だが戦力も低 |
| Line Infantry | 戦列歩兵 | 標準的な歩兵。Era 1-2 の主力 |
| Skirmish Infantry | 散兵 | 軽歩兵。機動力重視 |
| Trench Infantry | 塹壕歩兵 | 後期の防御型歩兵 |
| Squad Infantry | 分隊 | 近代歩兵。Era 4-5 |
| Mechanized Infantry | 機械化歩兵 | 最後期の歩兵。車両化 |
| Hussars | 軽騎兵 | 軽装騎兵。序盤の騎馬ユニット |
| Dragoons | 竜騎兵 | 乗馬歩兵。汎用騎兵 |
| Cuirassiers | 胸甲騎兵 | 重装騎兵。攻撃力高 |
| Lancers | 槍騎兵 | 突撃型騎兵 |
| Light Tanks | 軽戦車 | Era 4 の装甲ユニット |
| Heavy Tank | 重戦車 | Era 5 の最強装甲ユニット |
| Cannon Artillery | カノン砲 | 初期砲兵ユニット |
| Mobile Artillery | 自走砲 | 機動力のある砲兵 |
| Shrapnel Artillery | 榴散弾砲 | 対人効果の高い砲兵 |
| Siege Artillery | 攻城砲 | 要塞攻略・上陸支援用 |

### 海軍兵種

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Man-o'-War | 軍艦 | 帆船時代の主力艦 |
| Frigate | フリゲート艦 | 汎用軍艦。封鎖に使用 |
| Monitor | モニター艦 | 沿岸防衛用装甲艦 |
| Ironclad | 装甲船 | 蒸気装甲艦。Era 2-3 |
| Torpedo Boat | 魚雷ボート | 小型高速艦 |
| Destroyer | 駆逐艦 | 対潜・魚雷ボート対策 |
| Scout Cruiser | 偵察艦 | 哨戒・シーレーン保護 |
| Dreadnought | ドレッドノート | Era 4 の弩級戦艦 |
| Battleship | 戦艦 | Era 5 の超弩級戦艦 |
| Submarine | 潜水艦 | 通商破壊・封鎖に強力 |
| Carrier | 母艦 | 航空母艦。Era 5 |

### 将官階級

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Brigadier General / Rear Admiral | 陸軍准将 / 海軍准将 | 階級1 |
| Major General / Vice Admiral | 陸軍少将 / 海軍少将 | 階級2 |
| Lieutenant General / Vice Admiral | 陸軍中将 / 海軍中将 | 階級3 |
| General / Admiral | 陸軍大将 / 海軍大将 | 階級4 |
| Field Marshal / Fleet Admiral | 陸軍元帥 / 海軍元帥 | 階級5（最高位） |
| Supreme Commander | 最高司令官 | 国家元首が兼任 |

## 経済

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Building | 施設 | 経済・軍事の建造物 |
| Construction | 資材 | 建設に必要な物資 |
| Construction Sector | 建設局 | 建設を担う施設 |
| Goods | 商品 | 生産・消費される物品 |
| Market | 市場 | 経済圏 |
| Trade Center | 取引所 | 交易施設 |
| Tax | 税金 | 国家収入 |
| Incorporated State | 編入州 | 完全に国内に統合された州 |
| Unincorporated State | 未編入州 | 植民地等。補正あり |
| Open Market | 市場開放 | 外国との自由貿易 |
| Migration | 移住 | Pop の移動 |
| Mass Migration | 集団移住 | 大規模な人口移動 |

### 主要商品（Goods）

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Iron | 鉄 | 基礎資源。工業化の基盤 |
| Coal | 石炭 | 工業・発電の主要燃料 |
| Steel | 鋼鉄 | 鉄から生産。Er 2 以降必須 |
| Wood / Timber | 軟材 / 硬材 | 建設材料 |
| Grain | 穀物 | 基本食料 |
| Fish | 魚 | 沿岸地域の食料 |
| Meat | 食肉 | 高級食料 |
| Fruit | 果実 | 農業産品 |
| Tools | 工具 | 建設に必要。工具工房で生産 |
| Fabric | 生地 | 衣類の原料 |
| Clothes | 衣類 | Pop の基本消費品 |
| Furniture | 家具 | 生活必需品 |
| Groceries | 食料品 | 加工食品 |
| Paper | 紙 | 行政・出版に使用 |
| Oil | 燃油 | Era 3 以降の重要燃料 |
| Rubber | ゴム | 後期工業化に必要 |
| Dye | 染料 | 繊維産業の原料 |
| Wool | 羊毛 | 繊維原料 |
| Silk | 絹 | 高級繊維原料 |
| Sugar | 砂糖 | 農園産品 |
| Cotton | （綿花農園で生産。Fabric の原料） | 商品キーなし。建物で対応 |
| Explosives | 爆薬 | 採掘・軍事に使用 |
| Ammunition | 弾薬 | 軍事消費品 |
| Small Arms | 小火器 | 軍事装備 |
| Artillery | 大砲 | 重火器。砲兵ユニット装備 |
| Clippers | 快速帆船 | 帆船時代の輸送船 |
| Steamers | 汽船 | 蒸気時代の輸送船 |
| Electricity | 電力 | Era 4-5 の基盤インフラ |
| Engines | 発動機 | 機械産業の中核品 |
| Manowars | 戦列艦 | 帆船艦隊向け建造品 |
| Ironclads | 装甲艦 | 蒸気艦隊向け建造品 |
| Luxury Clothes | 高級衣類 | 富裕層向け消費品 |
| Luxury Furniture | 高級家具 | 富裕層向け消費品 |
| Services | サービス | 知識人・商業 Pop の需要 |

### 主要建造物（Buildings）

#### 工業施設

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Steel Mill | 製鉄所 | 鉄→鋼鉄。工業化の要 |
| Textile Mill | 織物工場 | 生地→衣類 |
| Tooling Workshop | 工具工房 | 工具生産 |
| Paper Mill | 製紙工場 | 紙生産 |
| Shipyard | 造船所 | 輸送船生産 |
| Military Shipyard | 軍用造船所 | 軍艦生産 |
| Chemical Plant | 肥料工場 | 肥料・化学品 |
| Explosives Factory | 爆薬工場 | 爆薬生産 |
| Arms Industry | 武器工場 | 小火器・弾薬生産 |
| Artillery Foundry | 大砲工場 | 大砲生産 |
| Munition Plant | 弾薬工場 | 弾薬大量生産 |
| Food Industry | 食品産業 | 食料品生産 |
| Furniture Manufactory | 家具工場 | 家具生産 |
| Power Plant | 発電所 | 電力生産。Era 3 以降 |
| Motor Industry | 発動機産業 | 発動機生産 |
| Automotive Industry | 自動車産業 | 自動車生産 |
| Electrics Industry | 電気産業 | 電力機器生産 |
| Glassworks | ガラス工房 | ガラス生産 |
| Synthetics Plant | 合成繊維プラント | 合成素材生産 |

#### 採掘・農業

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Iron Mine | 鉄鉱山 | 鉄生産 |
| Coal Mine | 石炭鉱山 | 石炭生産 |
| Gold Mine | 金鉱山 | 金生産 |
| Lead Mine | 鉛鉱山 | 鉛生産 |
| Oil Rig | 石油リグ | 燃油生産。Era 3 以降 |
| Sulfur Mine | 硫黄鉱山 | 火薬・肥料の原料 |
| Logging Camp | 伐採所 | 軟材生産 |
| Wheat Farm | 小麦畑 | 穀物生産 |
| Rye Farm | ライ麦畑 | 穀物生産 |
| Rice Farm | 稲田 | 穀物生産（アジア地域） |
| Livestock Ranch | 家畜牧場 | 食肉生産 |
| Fishing Wharf | 漁港 | 魚生産 |
| Coffee Plantation | コーヒー農園 | コーヒー生産 |
| Cotton Plantation | 綿花農園 | 綿花→生地の原料 |
| Silk Plantation | 養蚕農園 | 絹生産 |
| Dye Plantation | 染料農園 | 染料生産 |
| Opium Plantation | アヘン農園 | アヘン生産 |
| Rubber Plantation | ゴム農園 | ゴム生産。Era 3 以降重要 |
| Tea Plantation | 茶園 | 茶葉生産 |
| Tobacco Plantation | タバコ農園 | タバコ生産 |
| Sugar Plantation | 砂糖農園 | 砂糖生産 |
| Vineyard | ブドウ園 | ワイン生産 |
| Banana Plantation | バナナ農園 | 果実生産 |

#### インフラ・行政

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Urban Center | 市街地 | 都市の基盤施設 |
| Construction Sector | 建設局 | 建設キューを担う |
| Subsistence Farm | 自給農家 | 後進地域の基礎施設 |

## 法律・制度

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Law | 法律 | 国家の法制度 |
| Institution | 制度 | 法律で設置する組織 |
| Government Type | 政府のタイプ | 政体 |
| Monarchy | 君主制 | |
| Presidential Republic | 大統領共和制 | |
| Parliamentary Republic | 議会共和制 | |
| Theocracy | 神権制 | |
| Council Republic | 評議会共和制 | |

### 主要制度

| 英語 | ゲーム内日本語 |
|------|---------------|
| Colonial Affairs | 植民地関係 |
| Schools | 教育 |
| Social Security | 社会保障 |
| Workplace Safety | 労働基準局 |
| Police | 法執行機関 |
| Health System | 医療制度 |
| Home Affairs | 治安維持 |

### 主要法律（攻略頻出）

#### 政治体制

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Autocracy | 専制政治 | 初期の権力集中型政体 |
| Oligarchy | 寡頭制 | 少数支配 |
| Landed Voting | 土地所有者投票 | 地主階級のみが投票権 |
| Wealth Voting | 富裕者投票 | 資産制限付き選挙権 |
| Census Voting | 制限選挙 | 識字・資産等の制限あり |
| Universal Suffrage | 普通選挙 | 全成人に投票権 |
| Single Party State | 一党独裁国家 | 独裁政党体制 |
| Proportional Representation | 比例代表制 | 比例票配分選挙 |
| First Past the Post | 単純小選挙区制 | 小選挙区制 |

#### 権利・自由

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Outlawed Dissent | 異議の禁止 | 最も抑圧的 |
| Censorship | 検閲 | 出版・集会制限 |
| Right of Assembly | 集会の権利 | 集会・結社を認める |
| Protected Speech | 言論の保護 | 最も自由 |
| Slavery Banned | 奴隷禁止 | 奴隷制の廃止 |
| Debt Slavery | 債務奴隷 | 債務による強制労働 |
| Slave Trade | 奴隷貿易 | 奴隷の売買を容認 |

#### 徴兵・軍制

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Peasant Levies | 農民召集兵 | 最も初歩的な軍制 |
| National Militia | 国民民兵 | 民兵制度 |
| Mass Conscription | 大規模徴兵 | 大量徴兵。戦時に有効 |
| Professional Army | 職業軍人 | 常備軍制度。質重視 |

#### 経済体制

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Traditionalism | 伝統主義 | 工業化に反対。初期状態 |
| Agrarianism | 農本主義 | 農業優先経済 |
| Laissez-Faire | レッセフェール | 自由市場。資本家が活性化 |
| Interventionism | 干渉主義 | 政府が積極介入 |
| Cooperative Ownership | 共同所有 | 協同組合経済 |
| Command Economy | 指令経済 | 計画経済 |

#### 貿易政策

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Free Trade | 自由貿易 | 関税なし。輸入を促進 |
| Protectionism | 保護主義 | 関税で国内産業を保護 |
| Mercantilism | 重商主義 | 輸出重視の貿易政策 |
| Isolationism | 孤立主義 | 外部との交流を最小化 |
| Canton System | 広東システム | 非承認国家の特殊貿易体制 |

#### 課税

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Consumption-Based Taxation | 消費ベース課税 | 消費税型 |
| Land-Based Taxation | 土地ベース課税 | 地租型。地主に負担 |
| Per Capita Taxation | 人頭課税 | 一律人頭税 |
| Proportional Taxation | 比例課税 | 比例税率 |
| Graduated Taxation | 累進課税 | 高所得者により重い税 |

#### 農業制度

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Serfdom | 農奴制 | 農民が土地に縛られる |
| Tenant Farmers | 小作農 | 地主の土地を賃借 |
| Homesteading | 入植 | 自作農。開拓地向け |
| Commercialized Agriculture | 商業化農業 | 市場向け農業 |
| Collectivized Agriculture | 集団農業 | 共同農業 |
| Latifundias | ラティフンディア | 大土地所有制 |

#### 労働・組合

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| No Workers Rights | 労働基本権の無保障 | 最も抑圧的 |
| Regulatory Bodies | 規制機関 | 基本的な労働規制 |
| Worker Protections | 労働者の保護 | 労働条件改善 |
| Guild System | ギルド制度 | 伝統的職人組合 |
| Combination Acts | 団結禁止法 | 組合結成禁止 |
| Anti-Strike Laws | 反ストライキ法 | ストライキ禁止 |
| Right to Associate | 結社の権利 | 組合結成を認める |
| Factory Councils | 工場評議会 | 労働者自治参加 |

#### 植民地

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| No Colonial Affairs | 植民地なし | 植民地を持たない |
| Colonial Resettlement | 植民地再定住 | 本国民を移住させる |
| Colonial Exploitation | 植民地搾取 | 現地から資源収奪 |
| Colonial Slavery | 植民地奴隷制 | 植民地での奴隷使用 |

#### 宗教・文化政策

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| State Religion | 国教 | 国家公認宗教制度 |
| Freedom of Conscience | 良心の自由 | 宗教の自由を認める |
| Total Separation | 完全分離 | 政教完全分離 |
| Atheist State | 無神論国家 | 宗教を否定 |
| Ethnostate | 民族国家 | 支配民族による単一国家 |
| National Supremacy | 国民至上 | 自国民優先 |
| Racial Segregation | 人種隔離 | 人種による隔離 |
| Multiculturalism | 多文化主義 | 全文化を平等に認める |

#### 行政・官僚制

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Appointed Bureaucrats | 任命制の官僚 | 任命制官僚システム |
| Meritocratic Bureaucracy | 実力制の官僚 | 実力主義的官僚制 |
| Elected Bureaucrats | 選挙制の官僚 | 選挙による官僚選出 |

## 技術

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Technology | 技術 | 研究対象 |
| Era | 時代 | 技術の時代区分（5段階） |
| Innovation | 革新 | 技術進歩の速度 |

### 攻略頻出技術（Era別）

#### Era 1（1836 年代〜）

| 英語 | ゲーム内日本語 | 分類 |
|------|---------------|------|
| Atmospheric Engine | 大気圧機関 | 経済 |
| Canals | 運河 | 経済 |
| Blast Furnaces | 溶鉱炉 | 経済 |
| Bessemer Process | ベッセマー法 | 経済 |
| Four-Field Crop Rotation | 四圃式輪作 | 農業 |
| Line Infantry | 戦列歩兵 | 軍事 |
| Gunsmithing | 銃工 | 軍事 |
| Gunpowder | 火薬 | 軍事 |
| Logistics | 兵站 | 軍事 |
| Enlightenment Thought | 啓蒙思想 | 文化 |
| Rule of Law | 法の支配 | 政治 |

#### Era 2（1850-60 年代〜）

| 英語 | ゲーム内日本語 | 分類 |
|------|---------------|------|
| Bessemer Steel | ベッセマー鋼 | 経済 |
| Railway (Electric Railway) | 電気鉄道 | 経済 |
| Breech-Loading Artillery | 後装砲 | 軍事 |
| Bolt-Action Rifles | ボルトアクションライフル | 軍事 |
| Ironclad Tech | 装甲艦 | 軍事 |
| Screw Frigate | スクリューフリゲート艦 | 軍事 |
| General Staff | 幕僚 | 軍事 |
| Army Reserves | 陸軍予備役 | 軍事 |
| Germ Theory | 胚種説 | 医療 |
| Antiseptics | 消毒薬 | 医療 |
| Empiricism | 経験論 | 文化 |
| Separation of Powers | 権力分立 | 政治 |
| Democracy | 民主主義 | 政治 |

#### Era 3（1870-80 年代〜）

| 英語 | ゲーム内日本語 | 分類 |
|------|---------------|------|
| Bessemer Steel / Crucible Steel | 坩堝鋼 | 経済 |
| Electrical Generation | 発電 | 経済 |
| Combustion Engine | 内燃機関 | 経済 |
| Dynamite | ダイナマイト | 経済 |
| Telegraph | 電報 | 経済 |
| Dreadnought Tech | 弩級戦艦 | 軍事 |
| Defense in Defense | 縦深防御 | 軍事 |
| Battlefleet Tactics | 近代戦艦戦術 | 軍事 |
| Mandatory Service | 国民皆兵 | 軍事 |
| Socialism | 社会主義 | 政治 |
| Labor Movement | 労働運動 | 政治 |

#### Era 4-5（1900 年代〜）

| 英語 | ゲーム内日本語 | 分類 |
|------|---------------|------|
| Battleship Tech | 超弩級戦艦 | 軍事 |
| Carrier Tech | 航空母艦 | 軍事 |
| Chemical Warfare | 化学兵器戦争 | 軍事 |
| Stormtroopers | 突撃歩兵 | 軍事 |
| Assembly Line | 組立ライン | 経済 |
| Central Planning | 中央指令型経済 | 経済 |
| Fascism | ファシズム | 政治 |

## 外交

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Alliance | 同盟 | 軍事同盟 |
| Customs Union | 関税同盟 | 経済統合 |
| Defensive Pact | 防衛協定 | 防衛のみの同盟 |
| Subject | 従属国 | 従属国の総称 |
| Overlord | 宗主国 | 従属国を支配する国 |
| Dominion | 自治領 | 高い自治権を持つ従属国 |
| Puppet | 傀儡国 | 外交を制限された従属国 |
| Protectorate | 保護国 | 保護下の従属国 |
| Vassal | 属国 | 代表的な従属形態 |
| Tributary | 属国（朝貢国） | 朝貢型の従属関係 |
| Personal Union | 同君連合 | 同じ君主を戴く連合 |
| Crown Land | 王領地 | 直轄植民地 |
| Colony | 植民地 | 植民地型従属国 |
| Guarantee of Independence | 独立保証 | 他国の独立を保証 |
| Rivalry | ライバル | 外交的競争関係 |
| Maneuver | 戦略 | 外交戦での行動ポイント |
| Liberty Desire | 自由への願望 | 従属国の独立志向度 |
| Tension | 緊張度 | 外交的な緊張レベル |
| Sway | 懐柔 | 他国を外交戦に引き込む行動 |
| Obligation | 義務 | 外交支援等で生じた義理 |
| Great Power | 列強 | 最上位の国家ランク |
| Major Power | 大国 | 二番目の国家ランク |
| Minor Power | （概念のみ） | 中小国家 |
| Recognized / Unrecognized | 承認国 / 非承認国家 | 国際社会での承認状態 |
| Power Bloc | 勢力ブロック | 複数国が形成する政治ブロック |

### 戦争目標（War Goal Types）

| 英語 | ゲーム内日本語 | 補足 |
|------|---------------|------|
| Conquer State | 州の征服 | 州を奪取する最基本戦争目標 |
| Return State | 州の返還 | 奪われた州を取り戻す |
| Annex Country | 国の併合 | 相手国を完全に吸収 |
| Humiliation | 屈辱 | 威信・悪名ペナルティを与える |
| Open Market | 市場開放 | 相手の市場を自由化させる |
| Regime Change | 体制変更 | 相手国の政体を変える |
| Ban Slavery | 奴隷制禁止 | 奴隷制廃止を強制 |
| Independence | 独立 | 従属国の独立を支援 |
| Liberate Subject | 従属国の解放 | 従属国を解放する |
| Make Dominion | 自治領を作る | 相手を自治領にする |
| Make Protectorate | 保護領の作成 | 相手を保護国にする |
| Make Tributary | 属国の作成 | 相手を属国にする |
| Reduce Autonomy | 自治権の縮小 | 従属国の自治度を下げる |
| Increase Autonomy | 自治権の拡大 | 従属国の自治度を上げる |
| Transfer Subject | 従属国の移譲 | 従属国を他国に移す |
| Take Treaty Port | 条約港取得 | 条約港を設置する |
| Force Recognition | 認識の強要 | 承認を強制する |
| Contain Threat | 分相応 | 脅威の国を弱体化させる |
| War Reparations | 戦争賠償金 | 賠償金支払いを要求 |
| Secession | 分離 | 特定地域の独立 |
| Foreign Investment Rights | 投資権 | 外国投資の権利取得 |
| Force Nationalization | 国有化の強制 | 外国資産の国有化阻止 |
| Join Power Bloc | 勢力ブロックに参加 | 勢力ブロック加入を強制 |
| Leave Power Bloc | 勢力ブロックを離脱 | 勢力ブロック脱退を強制 |
| Unification | 統合 | 統一国家の形成 |
| Primary Demand | 一次要求 | 外交戦の主要な要求 |
| Secondary Demand | 二次要求 | 外交戦での追加要求 |

---

## 運用ルール

- 攻略ガイドの用語はこのファイルを**正本**とする
- ゲーム内日本語が変更された場合、このファイルを更新し、各ガイドの用語対照表も合わせる
- 各ガイドの用語対照表にはそのガイドで使う用語のみ抜粋し、完全版はここを参照する
- 新しい用語を追加する場合は、必ずゲーム内ローカライズファイルで確認してから追加する
