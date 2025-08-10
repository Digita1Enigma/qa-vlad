import os, json, pytest, requests
from jsonschema import validate

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com"))

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url")

@pytest.fixture
def logger():
    def _log(method, url, resp):
        print(f"\n[LOG] {method.upper()} {url} -> {resp.status_code}")
        try:
            print(json.dumps(resp.json(), ensure_ascii=False, indent=2)[:800])
        except Exception:
            print(resp.text[:500])
    return _log
