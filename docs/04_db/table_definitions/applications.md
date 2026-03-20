# applications

| column | type | required | description |
|---|---|---|---|
| id | BIGSERIAL | yes | 申請ID |
| application_no | VARCHAR(20) | yes | 申請番号 |
| applicant_id | BIGINT | yes | 申請者ID |
| title | VARCHAR(100) | yes | 件名 |
| body | TEXT | yes | 内容 |
| status | VARCHAR(20) | yes | 状態 |
