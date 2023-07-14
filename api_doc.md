# API 文檔

## 實現一 API,提供打卡功能

用於創建新的出勤記錄。

- 請求路徑: `/api/attendance/`
- 請求方法: `POST`

#### 請求參數

| 參數名稱     | 類型      | 必填    | 描述                               |
| ------------ | --------- | ------- | ---------------------------------- |
| employee_number  | 整數      | 是      | 員工的唯一識別碼                   |
| clock_in     | 字符串    | 是      | 上班打卡時間 (格式: 'YYYY-MM-DD HH:MM') |
| clock_out    | 字符串    | 是      | 下班打卡時間 (格式: 'YYYY-MM-DD HH:MM') |

#### 請求範例

```text
POST /api/attendance/
Content-Type: application/json

{
"employee_number": 12345,
"clock_in": "2023-07-13 09:00",
"clock_out": "2023-07-13 18:00"
}
```

## 實現一 API,提供補打卡功能,使漏打上班或下班員工可以進行補打卡

#### 請求範例
```text
PATCH /api/attendance/<attendance_id>/
PATCH /api/attendance/101/
Content-Type: application/json

{
"employee_number": 12345,
"clock_in": "2023-07-13 09:00",
"clock_out": "2023-07-13 18:00"
}
```

## 實現一 API,列出所有員工當日資訊

#### 請求範例

```text
GET /api/attendance/
Content-Type: application/json
```

## 實現一API,可以列出指定日期當天所有員工資訊

#### 請求範例

沒有指定日期, 預設為當天資訊

```text
GET /api/attendance/?date=2022-01-05
Content-Type: application/json
```

## 實現一 API,可以列出指定日期區間未打下班卡的員工清單

#### 請求範例

```text
GET /api/attendance/no_check_out_employees/?start_date=2022-01-03&end_date=2022-01-06
Content-Type: application/json
```

## 實現一 API,可以列出指定日期,當天前五名最早打卡上班的員工

#### 請求範例

```text
GET /api/attendance/earliest_clock_in_employees/?date=2022-01-05
Content-Type: application/json
```
