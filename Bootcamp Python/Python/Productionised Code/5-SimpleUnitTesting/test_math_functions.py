def add_two(x:int) -> int:
    """Add two to the input integer"""
    return x + 2

def test_add_two():
    output_add_two_with_four = add_two(4)
    assert output_add_two_with_four == 6

def test_add_two_extended():
    # Arrange
    input_1 = 3
    input_2 = -200
    expected_result1 = 5
    expected_result2 = -198

    # Act
    result1 = add_two(input_1)
    result2 = add_two(input_2)

    # Assert
    assert result1 == expected_result1
    assert result2 == expected_result2

