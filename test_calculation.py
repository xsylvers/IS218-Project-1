import pytest

def perform_calculation(a, b, operation):
    """This line of code demonstrates a simple function to perform basic calculations."""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is undefined")

@pytest.mark.parametrize("a, b, operation, expected_result", [])
def test_dynamic_calculation(generate_test_data, a, b, operation, expected_result):
    """This line of code test calculations using dynamically generated data."""
    assert perform_calculation(a, b, operation) == expected_result
