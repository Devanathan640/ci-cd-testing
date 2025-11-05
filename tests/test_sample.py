import pytest
from src.testing import add,sub,mul

def test_add():
    assert add(2,4)==6

def test_sub():
    assert sub(4,2)==2

def test_mul():
    assert mul(2,3)==6


