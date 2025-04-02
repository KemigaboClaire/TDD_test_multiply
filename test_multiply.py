import sys
import os

# Authors Kemigabo Claire & Namayanja Patricia 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from multiply import multiply

def test_multiply_1x1():
    assert multiply(1, 1) == 1


def test_multiply_2x2():
    assert multiply(2, 2) == 4


def test_multiply_3x3():
    assert multiply(-3, -3) == 9


def test_multiply_4x4():
    assert multiply(4, -4) == -16


def test_multiply_23x45():
    assert multiply(23, 45) == 23 * 45


    
def test_multiply_0x5():
    assert multiply(0, 5) == 0



def test_multiply_1x5():
    assert multiply(1, 5) == 5