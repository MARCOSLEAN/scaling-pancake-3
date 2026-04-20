from app import soma, subtracao, multiplicacao

def test_soma():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-1, -1) == -2

def test_subtracao():
    assert subtracao(5, 3) == 2

def test_multiplicacao():
    assert multiplicacao(4, 2) == 8

def test_multiplicacao_zero():
    assert multiplicacao(5, 0) == 0