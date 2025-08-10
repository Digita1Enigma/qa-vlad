import requests

def test_create_post(base_url):
    payload = {"title":"ping","body":"test","userId":1}
    r = requests.post(f"{base_url}/posts", json=payload, timeout=20)
    assert r.status_code in (201, 200)
    data = r.json()
    for k,v in payload.items():
        assert data.get(k) == v
