from src.math_operations import add, subtract, multiply, divide

def test_add():
    # Arrange
    input_value1 = 10
    input_value2 = 20
    expected_output = 30

    # Act
    result = add(input_value1, input_value2)

    # Assert
    assert result == expected_output