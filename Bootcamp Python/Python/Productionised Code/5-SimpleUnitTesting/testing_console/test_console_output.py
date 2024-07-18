def add_two(x):
    print(f'the value of add plus 2 is {x+2}')

# def test_add_two():
#     #Arrange
#     input_val = 5
#     expected_val =  'the value of add plus 2 is 7'

#     #Act
#     result = add_two(input_val)

#     assert result == expected_val

def test_add_two(capsys):
    # print('Hello World')

    # captured = capsys.readouterr()

    # assert captured.out == 'Hello World'
    # assert captured.err == ''

    # # Arrange
    # input_val = 5
    # expected_val = 'the value of add plus 2 is 7\n'

    # # Act
    # add_two(input_val)
    # captured = capsys.readouterr()

    # #Assert
    # assert captured.out == expected_val
    # assert captured.err == ''

    import sys
    def test_add_two(capsys):
        print('hello', file=sys.stderr)