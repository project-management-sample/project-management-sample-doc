# Project Management Hub

Webアプリ開発の**横断管理リポジトリ**です。  
スクラム（2週間スプリント）× トランクベース開発（TBD）で運用します。

## 関連リポジトリ

| リポジトリ | 説明 | 技術スタック |
|---|---|---|
| [project-management-sample-frontend](https://github.com/akinami3/project-management-sample-frontend) | フロントエンド | React, TypeScript |
| [project-management-sample-backend](https://github.com/akinami3/project-management-sample-backend) | バックエンド API | Node.js, TypeScript |

## クイックスタート

1. [開発ガイド](docs/development-guide.md) を読む（スクラム運用・TBD・Doneの定義）
2. [アーキテクチャ](docs/architecture.md) を確認する
3. 各リポジトリの README に従い開発環境をセットアップ
4. GitHub Projects の Sprint Board を確認し、タスクに着手

## ドキュメント

| ドキュメント | 内容 |
|---|---|
| [docs/development-guide.md](docs/development-guide.md) | スクラム運用 + TBD + Doneの定義 |
| [docs/architecture.md](docs/architecture.md) | システム構成図 + 技術スタック |
| [docs/roadmap.md](docs/roadmap.md) | ロードマップ（ガントチャート付き） |

## GitHub Projects ボード

| ボード | 用途 |
|---|---|
| Sprint Board | 現スプリントのタスク管理（Board ビュー） |
| Product Backlog | 全バックログの優先度管理（Table ビュー） |
| Roadmap | エピック単位の進捗可視化（Timeline ビュー） |

> ボード作成方法は [開発ガイド](docs/development-guide.md#github-projects-の設定) を参照

## ラベル体系

[labels.yml](.github/labels.yml) で一元管理。各リポジトリへの同期方法:

```bash
npx github-label-sync --access-token <TOKEN> --labels .github/labels.yml akinami3/project-management-sample-frontend
npx github-label-sync --access-token <TOKEN> --labels .github/labels.yml akinami3/project-management-sample-backend
```

| カテゴリ | 例 |
|---|---|
| `type:*` | `type:story`, `type:bug` |
| `priority:*` | `priority:high`, `priority:low` |
| `sp:*` | `sp:3`, `sp:8` |
| `repo:*` | `repo:frontend`, `repo:backend` |
| `status:*` | `status:blocked` |

## Issue の作り方

- **機能・タスク** → Story テンプレートを使用
- **バグ** → Bug テンプレートを使用

## セットアップ

```bash
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
```

リポジトリをクローン後、初回セットアップを実行してください：

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
```

これにより **Pre-commit hooks** が有効化され、ドキュメント変更時に `CHANGELOG.md` の更新が必須となります。

> ドキュメントファイル（`docs/` 配下、`.md` ファイルなど）を変更した場合、`CHANGELOG.md` も同時に更新していない commit はブロックされます。

## ライセンス

[MIT License](LICENSE)
