# HAB 固有進歩（Advances）一覧

- ソース: `game/in_game/common/advances/country_HAB.txt`
- ローカライズ: `game/main_menu/localization/japanese/advances_l_japanese.yml`（行 2501–2532）
- 抽出日: 2026-04-11

## 凡例

- **適用対象**: HAB=オーストリア, STY=シュタイアーマルク, TIR=チロル（potential 条件）
- **requires**: 前提となる汎用進歩または固有進歩の識別子
- 数値変数: `diplomatic_reputation_mild_bonus = 2`、`large_production_efficiency_bonus = 0.1`（default_values.txt 行 217, 747）

## 進歩テーブル

| 進歩名（英語） | 日本語名 | 時代 | 適用対象 | 前提（requires） | 効果 | src 行 |
|---------------|---------|------|---------|-----------------|------|--------|
| `austrian_tradition` | 栄光の一族 | age_1_traditions | HAB, STY | `feudalism_advance` | 外交官/月 +0.1、威信/月 +0.05 | 1 |
| `austrian_heritage` | ルドルフ1世の遺産 | age_1_traditions | HAB, STY | `austrian_tradition` | 陸軍士気 +10% | 14 |
| `hab_expert_mountaineers` | 山と川の国 | age_2_renaissance | HAB, STY, TIR | `renaissance_urbanisation` | 山岳地形近接影響 -50%、丘陵地形近接影響 -50%、高原地形近接影響 -50% | 26 |
| `austrian_marriage_policy` | 幸いなるオーストリアよ、結婚せよ | age_2_renaissance | HAB, STY | `renaissance_thought` | 外交評判 +2 | 42 |
| `habsburg_dominance` | オーストリアの外交手腕 | age_3_discovery | HAB, STY, TIR | `diplomatic_training` | 関係改善効果 +33% | 54 |
| `austrian_military_flexibility` | ランツクネヒトの戦術 | age_3_discovery | HAB, STY, TIR | `pike_square` | 軍事戦術 +10%、傭兵雇用コスト -10% | 67 |
| `edict_of_restitution` | 復旧令 | age_4_reformation | HAB のみ | `crown_power_advance_reformation` | 全国人口改宗速度 +10% | 81 |
| `austrian_court` | オーストリアの宮廷 | age_4_reformation | HAB のみ | `leader_recruit_cost_advance` | 外交容量 +2 | 90 |
| `geheimrat` | 枢密顧問院 | age_5_absolutism | HAB のみ | `the_constitution` | 政府規模 +1 | 99 |
| `hofkriegsrat` | 宮廷軍事局 | age_5_absolutism | HAB のみ | `artillery_vs_fort_age_5_absolutism` | 軍補充コスト -10%、連隊補充速度 +10% | 109 |
| `military_border` | 軍事的国境 | age_5_absolutism | HAB のみ | `army_movement_speed_absolutism` | 全国移住速度 +10%、規律 +3% | 119 |
| `austrian_ambition` | 教育による啓発 | age_6_revolutions | HAB のみ | `enlightened_court` | 子供教育 +40%、新規芸術家スキル +0.2 | 130 |
| `austrian_state_industrialization` | 国の産業化 | age_6_revolutions | HAB のみ | `joint_stock_companies` | 全国生産効率 +10% | 140 |
| `wiener_klassik` | ウィーン古典主義 | age_6_revolutions | HAB のみ | `artists_advance_revolutions` | 文化的伝統 +10%、文化的影響力 +10% | 149 |
| `multicultural_empire` | 多文化帝国 | age_6_revolutions | HAB のみ | `rights_of_man` | 文化容量 +3 | 159 |
| `imperial_artillery` | 帝国砲兵隊 | age_6_revolutions | HAB のみ | `the_gold_standard` | 砲兵戦闘力 +10%、砲兵建設コスト -10% | 168 |

## 時代別サマリー

| 時代 | 進歩数 | HAB 専用 | STY/TIR 共有 |
|------|--------|---------|-------------|
| age_1_traditions（伝統時代） | 2 | 0 | 2（STY） |
| age_2_renaissance（ルネサンス） | 2 | 0 | 2（STY/TIR） |
| age_3_discovery（大航海時代） | 2 | 0 | 2（STY/TIR） |
| age_4_reformation（宗教改革） | 2 | 2 | 0 |
| age_5_absolutism（絶対主義） | 3 | 3 | 0 |
| age_6_revolutions（革命） | 5 | 5 | 0 |
| **合計** | **16** | **10** | **6** |

## 注記

- age_1〜3 は STY（シュタイアーマルク）やTIR（チロル）との共有進歩。オーストリアが統合または継承するまでは他国が取れる
- `edict_of_restitution`（復旧令）は史実の1629年復旧令を参照。「紛争を引き起こすことはないだろう」というflavorテキストは皮肉
- `military_border`（軍事的国境）はオスマン国境に設置された軍事植民地制度（クライナ）が元ネタ
- `austrian_marriage_policy` の説明文はマクシミリアン1世の格言 "Bella gerant alii, tu felix Austria nube" の引用
