from pycourse_test import algos

def test_add_one():
    out = algos.add_one(1)
    assert out == 2, f'output should be 2 but is {out}'

def test_add_two():
    out = algos.add_two(1)
    assert out == 3

def test_something():
    pass
