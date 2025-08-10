# API Tests (pytest + requests + jsonschema)

## Установка и запуск
```
python -m pip install -r requirements.txt
pytest -s
# html-отчет:
pytest --html=report.html --self-contained-html
```
Можно переопределить базовый URL:
```
pytest -s --base-url=https://jsonplaceholder.typicode.com
```
