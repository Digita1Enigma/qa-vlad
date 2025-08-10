# Тест‑кейсы: API

## TC-API-GET-001: GET /posts/{id}
Ожидаемо: 200, JSON со свойством id == {id}.

## TC-API-NEG-001: GET /posts/0 (невалидный id)
Ожидаемо: 404/empty, без падения сервера.

## TC-API-POST-001: POST /posts
Ожидаемо: 201, тело с теми же полями (title, body, userId).

## TC-API-PUT-001: PUT /posts/{id}
Ожидаемо: 200/204, изменения применены.

## TC-API-DEL-001: DELETE /posts/{id}
Ожидаемо: 200/204, удаление без ошибок.
