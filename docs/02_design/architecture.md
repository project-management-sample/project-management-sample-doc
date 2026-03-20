# アーキテクチャ設計

## 構成
- Browser
- Frontend (React)
- Backend API (Spring Boot)
- PostgreSQL

## 方針
- 画面は API を介してデータ取得する
- 認証後はセッションを維持する
- 監査ログを全更新系処理で記録する
