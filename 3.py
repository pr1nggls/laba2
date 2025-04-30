
import pytest
from us import orig

def test1():
    assert orig([10, 20, 20, 30, 40, 40, 50]) == [10, 20, 30, 40, 50]

def test2():
    assert orig(['x', 'y', 'y', 'z']) == ['x', 'y', 'z']

def test3():
    assert orig([7, 7, 7, 7, 7]) == [7]

def test4():
    assert orig([]) == []

def test5():
    assert orig([5, 6, 7, 8, 9]) == [5, 6, 7, 8, 9]

def test6():
    assert orig([4, 5, 5]) == [4, 5]

def test7():
    assert orig([4.4, 4.4, 5.5, 6.6, 6.6]) == [4.4, 5.5, 6.6]

def test8():
    assert orig([-3, -3, 5, -5, 5]) == [-5, -3, 5]

def test9():
    large_input = [2] * 5000 + [4] * 5000 + [6] * 5000
    assert orig(large_input) == [2, 4, 6]

def test10():
    assert orig(['grape', 'kiwi', 'grape', 'pear']) == ['grape', 'kiwi', 'pear']

if __name__ == "__start__":
    pytest.run()

