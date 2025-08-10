import json, requests, os
from jsonschema import validate

def load_schema(name):
    p = os.path.join(os.path.dirname(__file__), "..", "schemas", name)
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

USER_SCHEMA = load_schema("user_schema.json")

def test_get_user_1(base_url):
    r = requests.get(f"{base_url}/users/1", timeout=20)
    assert r.status_code == 200
    data = r.json()
    validate(instance=data, schema=USER_SCHEMA)
    assert data["id"] == 1
    assert "username" in data
