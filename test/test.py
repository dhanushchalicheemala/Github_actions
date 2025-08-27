from src.app import add,sub


def test_add():
    assert add(1,20) == 21
    assert add(-1,20) == 19
    assert add(-1,-20) == -21
    assert add(0,0) == 0
    assert add(0,1) == 1
    assert add(0,-1) == -1
    assert add(0,0) == 0
    assert add(0,0) == 0

def test_sub():
    assert sub(1,20) == -19
    assert sub(-1,20) == -21
    assert sub(-1,-20) == 19
    assert sub(0,0) == 0
    assert sub(0,1) == -1
    assert sub(0,-1) == 1
    assert sub(0,0) == 0
    assert sub(0,0) == 0

