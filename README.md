# attendance_project

架構 Django REST framework + nginx + uwsgi + postgres

# deploy

```cmd
docker-compose build
docker-compose up -d
```

瀏覽 [http://0.0.0.0/api/attendance/?date=2022-01-05](http://0.0.0.0/api/attendance/?date=2022-01-05)

# api 文檔

[api_doc.md](api_doc.md)

可以搭配 postman, 範例可自行匯入 [attendance.postman_collection.json](attendance.postman_collection.json)


# 其他問題
- 原始資料 [member.json](https://github.com/blue-rubiks/attendance_project/blob/main/api/member.json), 裡面的 clockIn 有 "clockIn" 以及 "clockIn "(多一個空白) 不確定是測試的還是筆誤？
- 休息時間不太理解, 最後是直接回傳1.5小時


# 未實做
- test case
- deploy
