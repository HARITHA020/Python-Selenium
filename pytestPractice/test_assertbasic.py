import pytest
import sys
@pytest.mark.smoke
def test_simple_sample_assertion():
    assert 1+1==2
@pytest.mark.regression
def test_camparison():
    x=5
    y=5
    assert x==y
@pytest.mark.skip(reason="this is unwanted test")
def test_not_equal_sample_assertion():
    x=5
    y=10
    assert x!=y

def test_in_sample_assertion():
    numbers=[1,2,3,4,5]
    assert 3 in numbers

def test_equalsString_sample_assertion():
    a="haritha"
    b="haritha"
    assert a.__eq__(b)
@pytest.mark.skipif(sys.version_info<(3,8),reason="requires crt version")   
def test_example_skipif():
    assert 3 * 3==9
    
@pytest.mark.xfail(reason="expected to fail")
def test_example_xfail():
    assert 2*3==7
@pytest.mark.parametrize("test_input,expected",[(1,3),(4,6),(5,7)])
def test_addition(test_input,expected):
    assert test_input+2== expected