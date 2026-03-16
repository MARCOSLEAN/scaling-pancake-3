from app import soma, subtracao

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(5, 2) == 3