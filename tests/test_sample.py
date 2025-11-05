import pytest
from src.testing import add,sub

def test_add():
    assert add(2,3)==5

def test_sub():
    assert sub(4,3)==1


