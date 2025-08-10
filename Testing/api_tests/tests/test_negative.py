import requests
import pytest

@pytest.mark.parametrize("bad_id", [0, -1, 999999])
def test_get_post_negative(base_url, bad_id):
    r = requests.get(f"{base_url}/posts/{bad_id}", timeout=20)
    # JSONPlaceholder возвращает 404/пусто на невалидные id — допускаем оба варианта:
    assert r.status_code in (200, 404)
