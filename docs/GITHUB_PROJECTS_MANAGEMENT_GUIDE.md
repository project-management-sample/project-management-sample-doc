# GitHub Projects を使った WBS（Work Breakdown Structure）管理ガイド

このドキュメントでは、Organization-level の GitHub Projects を使用して、複数リポジトリにまたがるプロジェクトを WBS 的に管理する方法を説明します。

## 概要

GitHub Projects を使用することで、以下を実現します：

- **統一的な管理**: 複数リポジトリのタスクを一つのプロジェクトボードで管理
- **進捗追跡**: タスクのステータス、期日、担当者を一目で把握
- **優先度管理**: タスクの優先度を明確にし、効率的に管理
- **工数管理**: 見積もりと実績を追跡

## 対象リポジトリ

このプロジェクトでは、以下 3 つのリポジトリを統合管理します：

- **project-management-sample-backend** - バックエンド開発
- **project-management-sample-front** - フロントエンド開発
- **project-management-sample-doc** - ドキュメント作成

## Project のテンプレート

### 必須フィールド（カスタムフィールド）

GitHub Projects では、以下のフィールドを設定してください：

#### 1. タイトル（自動）
- Issue / PR のタイトル
- **必須**: はい

#### 2. ステータス（自動）
- New（未開始）
- In Progress（進行中）
- In Review（レビュー中）
- Done（完了）
- **必須**: はい

#### 3. 优先度（Priority） - カスタムフィールド/ 単一選択
```
- P0 - 最優先（ブロッカー）
- P1 - 高優先
- P2 - 中優先
- P3 - 低優先
```
- **必須**: はい
- **型**: 単一選択
- **目的**: タスクの重要度を明確化

#### 4. 担当者（Assignee） - GitHub ユーザー
- タスクの担当者を指定
- **必須**: はい
- **型**: ユーザーフィールド
- **目的**: 責任を明確にする

#### 5. 期日（Due Date） - 日付
- タスク完了の予定日
- **必須**: はい
- **型**: 日付
- **形式**: YYYY-MM-DD
- **目的**: スケジュール管理

#### 6. 見積もり（Estimation） - テキスト / 数値
```
単位：時間
例：8h, 16h, 40h
```
- **必須**: 推奨
- **型**: テキストまたは数値
- **目的**: スプリント計画と進捗管理

#### 7. 実績（Actual Hours） - テキスト / 数値（オプション）
```
実際に費やされた時間
単位：時間
```
- **必須**: オプション
- **型**: テキストまたは数値
- **目的**: 工数の検証と改善

#### 8. マイルストーン（Milestone） - テキスト / 単一選択
```
例：
- Phase 1 - 基本機能
- Phase 2 - 拡張機能
- Phase 3 - 最適化
```
- **必須**: 推奨
- **型**: テキストまたは単一選択
- **目的**: 大きな段階分けとしての WBS

#### 9. リポジトリ（Repository） - 自動
- Issue が属するリポジトリ
- **必須**: はい
- **型**: 自動生成
- **目的**: リポジトリ別の追跡

## Issue/PR テンプレートとの連携

各リポジトリの Issue / PR テンプレートには、以下の項目が必須として含まれています：

### Issue テンプレート（bug.yml, feature.yml, task.yml）に含まれる項目

1. **担当者（Assignee）**
   ```
   label: "担当者 (GitHub ユーザー名)"
   required: true
   ```
   
2. **期日（Due Date）**
   ```
   label: "期日" または "完了予定日"
   format: YYYY-MM-DD
   required: true
   ```

3. **重要度（Priority/Severity）**
   ```
   label: "重要度" または "優先度"
   options: ["P0", "P1", "P2", "P3"] または ["緊急", "高", "中", "低"]
   required: true
   ```

### Pull Request テンプレートに含まれる項目

1. **WBS 管理情報セクション**
   ```markdown
   ## WBS 管理情報
   
   ### 担当者
   @username
   
   ### 実施期間
   - 開始日: YYYY-MM-DD
   - 完了日: YYYY-MM-DD
   - 実施時間: XX時間（見積り）/ 実績XX時間
   
   ### 優先度
   - [ ] P0 - 最優先
   - [ ] P1 - 高優先
   - [ ] P2 - 中優先
   - [ ] P3 - 低優先
   ```

## Project での管理方法

### 1. Issue 作成時

1. リポジトリで Issue を作成
2. テンプレートを選択（bug.yml / feature.yml / task.yml）
3. **必須項目を入力**：
   - タスク内容
   - 担当者
   - 期日
   - 重要度

4. Issue を作成

### 2. Project への追加

1. Organization の Project を開く
2. Issue を Project に追加（ドラッグ&ドロップ、または Add item）
3. **カスタムフィールドを設定**：
   - Status: "New" から開始
   - Priority: Issue の重要度フィールドから転記
   - Assignee: Issue の担当者から自動取得
   - Due Date: Issue の期日から自動取得（または手動入力）
   - Estimation: 見積もり時間を入力

### 3. 進捗管理

タスク開始時：
- Status を "In Progress" に変更
- Assignee が自分であることを確認

タスク完了前：
- Status を "In Review" に変更（必要な場合）
- 実績時間を更新

タスク完了時：
- Status を "Done" に変更
- 実績時間を最終記録

### 4. Project ビューの設定推奨例

#### ビュー 1: ステータスボード
```
グループ化: Status
ソート: Priority（昇順）、Due Date（昇順）
フィルタ: Assignee（自分）
```
→ 自分のタスク状況を一目で把握

#### ビュー 2: 優先度ビュー
```
グループ化: Priority
ソート: Due Date（昇順）
表示列: 
  - タイトル
  - Assignee
  - Due Date
  - Estimation
  - Status
```
→ 優先度別のタスク管理

#### ビュー 3: タイムラインビュー
```
開始日フィールド: 開始予定日（Issue/PR に記載）
終了日フィールド: 期日
グループ化: リポジトリ
```
→ ガント図的な進捗確認

#### ビュー 4: テーブルビュー
```
表示列:
  - タイトル
  - Status
  - Assignee
  - Priority
  - Due Date
  - Estimation
  - Repository
ソート: Priority（昇順）、Due Date（昇順）
```
→ 詳細情報の確認と編集

## ワークフロー例

### スプリント開始時

1. **バックログから課題を選択**
   - Priority と Due Date でソート
   - そのスプリント期間内の課題を特定

2. **見積もり実施**
   - 各 Issue に Estimation を設定
   - チーム全体の容量を確認

3. **Project に追加**
   - 選択した課題を Project に追加
   - Milestone を設定（例：Sprint X）

### スプリント進行中

1. **毎日**
   - Project のステータスボードで進捗確認
   - 担当者は自分のタスクを更新

2. **週単位**
   - 優先度ビューで優先業務を確認
   - ブロッカーの早期対応

3. **必要に応じて**
   - Priority や Due Date を調整
   - 完了した課題を "Done" に移動

### スプリント終了時

1. **完了確認**
   - すべての完了課題が "Done" に設定されていることを確認

2. **工数の検証**
   - 実績時間と見積もり時間を比較
   - 今後の見積もり精度向上に活用

3. **レトロスペクティブ**
   - 何がうまくいったか、何が課題か整理
   - 来次スプリント計画に反映

## Project オートメーション（推奨）

GitHub Projects では、自動化が可能です。以下の設定を推奨します：

### 自動ステータス更新

- **PR がマージされた時**: Issue を "Done" に自動更新
- **Issue がクローズされた時**: Project アイテムを "Done" に自動更新
- **Issue が再度開かれた時**: Project アイテムのステータスをリセット

### ドラフト Issue の自動作成

- Template からの Issue 作成時、自動的に Project に追加

## ベストプラクティス

### DO（すべき事）

✅ **Issue 作成時に必須項目をすべて入力**
- 担当者、期日、重要度は絶対に設定

✅ **定期的にステータスを更新**
- 最低でも週 1 回は進捗を反映

✅ **見積もりと実績を記録**
- 工数管理の精度向上のため

✅ **優先度の見直し**
- 状況変化に応じて Priority を調整

✅ **ドキュメント（Docリポジトリ）も同じテンプレートで管理**
- 一貫した管理プロセスの実現

### DON'T（してはいけない事）

❌ **Issue 作成後に必須項目を未設定のまま放置**
- Project が正確な情報を失う

❌ **ステータスを更新しないまま進める**
- 進捗追跡が不正確に

❌ **優先度と期日のバランスを無視**
- スケジュール遅延の原因に

❌ **個別リポジトリで独自のテンプレートやプロセスを使用**
- 統合管理が困難に

❌ **見積もりと実績の大きな落差を放置**
- 次のスプリントの計画精度が低下

## FAQ

### Q: Issue と Project アイテムの関係は？

A: 
- **Issue**: 各リポジトリに作成される個別の課題
- **Project アイテム**: 複数リポジトリの Issue/PR を統合管理するもの
- Project に Issue を追加することで、Organization レベルの一元管理が可能

### Q: どの Project に追加すべき？

A:
- Backend リポジトリの Issue → 「Backend」Project
- Frontend リポジトリの Issue → 「Frontend」Project
- Doc リポジトリの Issue → 「Documentation」Project
- 複数リポジトリにまたがる大型企画 → 「Overall」Project（全体管理用）

### Q: 期日が過ぎてしまった場合は？

A:
1. Due Date を新しい日付に更新
2. Priority を上げる検討
3. スコープの縮小を検討（必要な場合）
4. 詳細コメントで進捗状況を記載

### Q: リモートチームでの使い方は？

A:
- 毎日の Project チェック（非同期コミュニケーション）
- 週 1 回の同期ミーティングで優先度調整
- コメント機能で進捗報告・質問対応
- Notification を活用した情報共有

## 関連リソース

- [GitHub Projects ドキュメント](https://docs.github.com/ja/issues/planning-and-tracking-with-projects)
- [GitHub Issue テンプレート](各リポジトリの `.github/ISSUE_TEMPLATE/`)
- [GitHub Pull Request テンプレート](各リポジトリの `.github/PULL_REQUEST_TEMPLATE.md`)

## サポート

このテンプレートやプロセスについて質問がある場合は:

1. Issue でこのドキュメントへのフィードバックを作成
2. Project ボード上でコメント
3. チームメンバーに相談

---

**最終更新**: 2026-03-19
**管理者**: Project Management Team
