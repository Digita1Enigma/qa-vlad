# QA Portfolio — Владислав Горбачёв (Pro)

Расширенный набор артефактов для начинающего QA (ручное тестирование + базовая автоматизация API).
Готов для публикации на GitHub/Google Drive/Notion и вставки ссылок в резюме HH.

## Состав папок
- `bug_reports/` — шаблон + 5 оформленных примеров (UI).
- `test_cases/` — авторизация, поиск/фильтры, корзина/чекаут, API кейсы.
- `checklists/` — смоук, регресс и чеклист доступности.
- `api_tests/` — мини-проект `pytest + requests + jsonschema` (+ html-отчёт).
- `postman/` — расширенная коллекция и окружение (base_url).
- `hh_blocks/` — готовые блоки для резюме HH («О себе», «Навыки», «Проекты»).
- `docs/` — сертификаты, сопроводительное, место для ссылок.

## Быстрый старт (локальный запуск API-тестов)
```bash
cd api_tests
python -m pip install -r requirements.txt
pytest -s            # обычный запуск
pytest --html=report.html --self-contained-html  # красивый отчёт
```
Отчёт появится в `api_tests/report.html` — его удобно прикреплять к откликам.

## Как опубликовать на GitHub (кратко)
```bash
git init
git add .
git commit -m "Add QA portfolio (initial)"
git branch -M main
git remote add origin https://github.com/<user>/qa-portfolio-vlad.git
git push -u origin main
```

## Что кастомизировать в первую очередь
1) Заменить примеры багов/кейсов на свои реальные находки (любой сайт).  
2) В `docs/certificates.md` добавить сканы сертификатов MIMO (Python/SQL).  
3) В `00_PORTFOLIO_INDEX.md` и `docs/portfolio_links.md` вставить реальные ссылки (GitHub/Notion/Drive).
