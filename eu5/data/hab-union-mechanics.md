# 婚姻・連合メカニクス調査データ

調査日: 2026-04-11  
対象: EU5 (Europa Universalis V)  
一次ソース: ゲームスクリプト（読み取り専用）

---

## 婚姻連合（Marriage Union / 結婚連合）

| 項目 | 内容 | src |
|------|------|-----|
| 種別 | International Organization (`marriage_union`) | marriage_union.txt:2 |
| 日本語名 | 結婚連合 | international_organizations_l_japanese.yml:812 |
| 成立条件 | **コード管理（hardcoded）** — 少なくとも2ヵ国が同じ後継者（heir）を共有していること | international_organizations_l_japanese.yml:819, marriage_union.txt:1 |
| 成立方式 | 確率式ではなく**確定**（条件成立時に自動生成）。手動で参加・離脱はできない | marriage_union.txt:49–57 |
| リーダー | 全メンバーの君主または摂政下の後継者をリーダーとして列挙（最大2ヵ国のcharacter） | marriage_union.txt:8–16 |
| リーダー更新タイミング | 君主交代時（`rulerchange`） | marriage_union.txt:8 |
| 防衛参加 | 外敵に対して常時共同防衛（`join_defensive_wars_always = yes`） | marriage_union.txt:19–21 |
| 宣戦布告 | メンバー同士への宣戦は原則不可。相手がメンバーでなければ自由に宣戦可 | marriage_union.txt:23–31 |
| 外交マップ表示 | あり（`show_on_diplomatic_map = yes`） | marriage_union.txt:45 |
| 霧の戦争解除 | あり（`fog_of_war_lifted = yes`） | marriage_union.txt:44 |
| 中央集権化 | **不可**。Personal Union (union) と異なり integration level なし | international_organizations_l_japanese.yml:813 |
| 性質 | 防衛同盟（defensive_league）に近い分権的連合 | international_organizations_l_japanese.yml:819 |
| 解消条件 | 以下のいずれかで自動解散: メンバーが2未満 / どちらかのleaderが存在しない / 2つのleaderが同一 / leader[0]の配偶者がleader[1]でない（= 王室婚姻が解消された） | marriage_union.txt:64–78 |
| 解消理由の日本語表示 | 「王室間の婚姻連合が破棄された」 | international_organizations_l_japanese.yml:814 |

---

## 同君連合（Personal Union / ユニオン）

### 成立条件

| 条件 | 内容 | src |
|------|------|-----|
| 基本 | **コード管理（hardcoded）** — 確率式なし。以下の経路のいずれかで**確定成立** | union.txt:1, _hardcoded.txt |
| 経路①: 継承 | 君主交代時に複数国が同一のキャラクターを君主として共有するとき自動成立。union の月次処理でメンバーが共通ruler/heirを持つかチェックし、持たない国は自動除外される | union.txt:270–295 |
| 経路②: 継承法「王位連合」 | `union_of_crowns_succession` — 相互に `union_of_crowns_pact` scripted_relation を持つ他国の候補者を継承対象に含める特別継承法 | heir_selections/monarchy.txt:union_of_crowns_succession |
| 経路③: 戦争（cb_union_war_for_seniority / cb_union_independence） | 同君連合戦争の勝者が `create_union = scope:loser`（または scope:winner）を確定実行 | _hardcoded.txt:1484–1528 |
| 経路④: 平和条約 | フランス王位継承 CB など特定平和条約に `create_union` が直書き（確定） | peace_treaties/claim_french_throne.txt:63–67 |
| 経路⑤: スクリプト効果 | `create_union_of_integration_level` / `create_union_of_level` — 各種イベント・決定から呼ばれる | scripted_effects/country_effects.txt:2261, IO_effects.txt:907 |
| 関係値の要件 | スクリプトには明示的な関係値閾値なし（コード側 hardcoded の可能性あり） | — |
| 王朝の要件 | 継承経路でのみ発動。`union_of_crowns_succession` は pact（外交関係）が必要 | heir_selections/monarchy.txt |

### 維持条件

| 条件 | 内容 | src |
|------|------|-----|
| 共通の君主/後継者 | 毎月チェック。メンバーがルーラーを持たない、またはシニア側のルーラーと異なる場合、かつ選挙継承法でない場合は除外 | union.txt:275–295 |
| 後継者も共有必要 | union に heir_character が設定されている場合、heir を持つが senior partner の heir と異なるメンバーも除外される | union.txt:285–295 |
| 例外 | 選挙制継承法（`uses_elections = yes`）の国はルーラーが異なっても除外されない | union.txt:281–284 |
| シニアパートナー | 大国力スコア（great_power_score）最大のメンバーが毎月自動更新。`union_senior_partner` 変数で保持 | union.txt:213–222 |
| ジュニア昇格 | ジュニアの great_power_score がシニアの 125% 以上になったとき `take_over_seniority` アクションが解放 | international_organizations_l_japanese.yml:820 |
| 解散トリガー | メンバー数が2未満になったとき自動解散 | union.txt:170–172 |

### 解消条件

| 条件 | 内容 | src |
|------|------|-----|
| メンバー自動離脱 | 共通の君主を持たなくなった国（選挙制除く）が月次処理で自動除外 | union.txt:275–294 |
| 自動解散 | `total_members < 2` | union.txt:170–172 |
| 独立戦争 (`cb_union_independence`) | ジュニアが勝訴すると union 離脱。敗訴するとシニアが `create_union` で再吸収 | _hardcoded.txt:1484–1528 |
| 外交（予定） | スクリプト上に `can_leave_trigger = always = no` とあり、手動離脱はコード管理と明記 | union.txt:160–163 |

### 統合レベル（Integration Level）

| 法律 / 政策 | 統合レベル変化 | 前提条件 | src |
|-------------|--------------|----------|-----|
| `union_senior_succession_law`（継承法の成文化: 主権的→同一継承法） | +1 | 連合存続10年以上, `union_establish_seniority_policy` 施行済, 共通君主あり | laws/40_personal_unions.txt:~200 |
| `union_unified_treasury_policy`（統一財政） | +1 | 連合20年以上, `union_senior_succession_law` 施行済 | laws/40_personal_unions.txt |
| `union_unified_external_diplomacy_policy`（統一外交） | +1 | 連合30年以上, 統一財政済 | laws/40_personal_unions.txt |
| `union_aligned_legislature_policy`（議会統一） | +1 | 連合40年以上, 統一外交済 | laws/40_personal_unions.txt |
| `union_crown_unification_policy`（王冠統合） | +1 | 連合50年以上, 議会統一済 | laws/40_personal_unions.txt |
| `union_swift_crown_unification_policy` | +2 | 王冠統合または迅速統合済 | laws/40_personal_unions.txt |
| `union_rapid_crown_unification_policy`（迅速統合） | +3 | 迅速または俊速済 | laws/40_personal_unions.txt |
| 併合（annex） | — | シニアが非subject, `union_integration_level` 充足, 連合50年以上 | union.txt:23–48 |

### 宣戦布告制限

| 状況 | 制限内容 | src |
|------|----------|-----|
| `union_blocked_from_declaring_war` モディファイア持ちメンバー | シニアパートナーに対してのみ宣戦可（独立戦争CB要） | union.txt:83–98 |
| `union_establish_seniority_policy` 施行済 | ジュニアから外部へは原則宣戦不可（シニアのみ可能） | union.txt:100–116 |
| 外部国からの宣戦 | メンバーに同盟している外部国はメンバーへ宣戦不可 | union.txt:127–136 |
| `union_unified_external_diplomacy_policy` 施行済 | ジュニアへ「ジュニア外交封じ（rein_in_junior_diplomacy）」アクション解放 | laws/40_personal_unions.txt |

---

## 婚姻連合と同君連合の関係

```
王室婚姻（royal_marriage）
  → 共通後継者が生まれると自動で marriage_union 成立（確定）
  → その後継者が複数国を継承すると union（同君連合）に昇格（確定）

union（同君連合）
  → 統合法律を段階的に施行（最短50年 + 各要件）
  → union_integration_level が条件を満たせば併合（annexation）が解放
```

**確率式か確定か**: EU5 の婚姻連合・同君連合メカニクスはすべて**確定ロジック**。  
条件を満たすと自動成立・自動解消する。ランダムロールは確認されていない。  
（EU4 と異なり、継承時のランダム判定は存在しない）
