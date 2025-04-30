import pytest
from fa import factorial

def t0():
    assert factorial(0) == 1

def t1():
    assert factorial(1) == 1

def t2():
    assert factorial(2) == 2

def t6():
    with pytest.raises(ValueError, match="для отрицательных не определеных"):
        factorial(-1)

def t3():
    assert factorial(3) == 6

def t4():
    assert factorial(4) == 24

def t5():
    assert factorial(5) == 120

def t7():
    assert factorial(8) == 40320