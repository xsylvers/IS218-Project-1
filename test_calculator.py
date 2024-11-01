import pytest # type: ignore
from calculator import Calculator

@pytest.fixture
def clear_history():
    """This line of code is a fixture to clear history before each test."""
    Calculator.history = []

def test_add(clear_history):
    assert Calculator.add(4, 3) == 7
    assert Calculator.get_last_calculation() == "Add: 4 + 3 = 7"

def test_subtract(clear_history):
    assert Calculator.subtract(8, 6) == 2
    assert Calculator.get_last_calculation() == "Subtract: 8 - 6 = 2"

def test_multiply(clear_history):
    assert Calculator.multiply(2, 5) == 10
    assert Calculator.get_last_calculation() == "Multiply: 2 * 5 = 10"

def test_divide(clear_history):
    assert Calculator.divide(10, 2) == 5.0
    assert Calculator.get_last_calculation() == "Divide: 10 / 2 = 5.0"

def test_divide_by_zero(clear_history):
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)

def test_calculation_history(clear_history):
    Calculator.add(4, 3)
    Calculator.subtract(8, 6)
    assert len(Calculator.history) == 2
    assert Calculator.get_last_calculation() == "Subtract: 8 - 6 = 2"
