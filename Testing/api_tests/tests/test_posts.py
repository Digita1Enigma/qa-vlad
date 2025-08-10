import json, pytest, requests, os
from jsonschema import validate

def load_schema(name):
    p = os.path.join(os.path.dirname(__file__), "..", "schemas", name)
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

POST_SCHEMA = load_schema("post_schema.json")

@pytest.mark.parametrize("post_id", [1,2,3])
def test_get_post(base_url, post_id):
    r = requests.get(f"{base_url}/posts/{post_id}", timeout=20)
    assert r.status_code == 200
    data = r.json()
    validate(instance=data, schema=POST_SCHEMA)
    assert data["id"] == post_id
