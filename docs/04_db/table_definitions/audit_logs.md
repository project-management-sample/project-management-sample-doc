# audit_logs

| column | type | required | description |
|---|---|---|---|
| id | BIGSERIAL | yes | 監査ログID |
| entity_type | VARCHAR(50) | yes | 対象種別 |
| entity_id | BIGINT | yes | 対象ID |
| action | VARCHAR(50) | yes | 操作種別 |
| operated_by | BIGINT | yes | 操作者 |
