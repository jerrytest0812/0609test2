# import requests

# def test_home():
#     r = requests.get("http://127.0.0.1:5001?a=2&b=1")
#     assert r.status_code == 200

import pytest
def add(x, y):
    return x + y

def test_add():
    assert add(1, 1) == 2
def test_add1():
    with pytest.raises(TypeError):
        assert add(2) == 4
def test_add2():
    assert(2,2) == 3
    