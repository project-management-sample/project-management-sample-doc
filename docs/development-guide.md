# 開発ガイド

## スクラム運用

### ロール

| ロール | 責任 |
|---|---|
| プロダクトオーナー (PO) | バックログの優先順位付け、受け入れ基準の定義 |
| スクラムマスター (SM) | プロセスの促進、障害の除去 |
| 開発チーム | スプリント内のタスク実行 |

### セレモニー（2週間スプリント）

| セレモニー | タイミング | 時間 |
|---|---|---|
| スプリントプランニング | 初日（月曜） | 2h |
| デイリースクラム | 毎日 | 15min |
| バックログリファインメント | 中盤（水 or 木） | 1h |
| スプリントレビュー | 最終日（金曜） | 1h |
| レトロスペクティブ | 最終日（金曜） | 1h |

### Milestone の命名

```
Sprint <番号> (<開始日> 〜 <終了日>)
例: Sprint 1 (2026-03-17 〜 2026-03-31)
```

各リポジトリでも同名の Milestone を作成し、GitHub Projects で横断集計します。

### ストーリーポイント目安

| SP | 目安 |
|---|---|
| 1 | 数時間。明確で単純 |
| 2 | 半日〜1日 |
| 3 | 1〜2日。複数ステップあり |
| 5 | 2〜3日。複雑さあり |
| 8 | 3〜5日。分割を検討 |
| 13 | 1週間以上。必ず分割 |

---

## トランクベース開発（TBD）

### 基本ルール

- `main` が唯一の長寿命ブランチ。**常にデプロイ可能**
- 短命ブランチのみ許可。寿命は**最大1〜2日**
- `develop`, `release`, `hotfix` ブランチは作らない

### ブランチ命名

```
<author>/<issue番号>-<簡潔な説明>
例: tanaka/42-add-login-api
```

### ワークフロー

```bash
# 1. main から最新を取得
git checkout main && git pull

# 2. 短命ブランチを作成
git checkout -b tanaka/42-add-login-api

# 3. 小さな単位で作業（差分200行以内を目安）

# 4. PR を作成 → CI通過 & レビュー後 → Squash Merge
```

### 大きな機能 → Feature Flag

数日以上かかる機能は Feature Flag で制御:

```typescript
if (featureFlags.isEnabled('new-payment')) {
  return <NewPayment />;
}
return <LegacyPayment />;
```

- フラグはデフォルト OFF
- 完成後にフラグを有効化 → リリース
- 安定したら 1スプリント以内にフラグコードを削除

### リリースとロールバック

- **通常**: `main` マージ → 自動デプロイ
- **ロールバック**: `git revert` → PR → 即マージ
- **タグ**: デプロイ時に `v1.2.3` を付与

### ブランチ保護ルール（各リポジトリで設定）

- `main` への直プッシュ禁止
- PR レビュー 1人以上必須
- CI ステータスチェック必須
- マージ後にブランチ自動削除

---

## Done の定義

Issue を「Done」とするための条件:

- [ ] 受け入れ基準をすべて満たしている
- [ ] コードレビュー済み（1名以上）
- [ ] CI（テスト・lint）がすべて通過
- [ ] `main` に Squash Merge 済み
- [ ] テストが追加/更新されている
- [ ] Feature Flag が適切に管理されている（該当する場合）
- [ ] 必要なドキュメントが更新されている

---

## GitHub Projects の設定

### 推奨ビュー

| ビュー名 | タイプ | 用途 |
|---|---|---|
| Sprint Board | Board | 現スプリントのタスク管理 |
| Product Backlog | Table | 全バックログの優先度管理 |
| Roadmap | Timeline | エピック単位の進捗可視化 |

### カスタムフィールド（推奨）

| フィールド名 | 型 | 用途 |
|---|---|---|
| Start date | Date | タスク開始日 |
| End date | Date | タスク終了日 |
| Sprint | Iteration（2週間） | スプリント管理 |
| Priority | Single select | 優先度 |

### タイムラインビュー（ガントチャート）設定

1. **New view** → **Roadmap** を選択
2. **Date fields** で Start date / End date を選択
3. ロードマップ用: **Group by** → Epic、Zoom → Month
4. スプリント用: **Group by** → Assignee、Zoom → Week、Filter → 現スプリント

### 各リポジトリの Issue 自動追加（任意）

```yaml
# 各リポジトリの .github/workflows/add-to-project.yml
name: Add to Project
on:
  issues:
    types: [opened]
jobs:
  add:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v1.0.2
        with:
          project-url: https://github.com/users/akinami3/projects/1
          github-token: ${{ secrets.PROJECT_TOKEN }}
```
