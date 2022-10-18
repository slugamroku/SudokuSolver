problem = '000|300|060\n' \
          '901|008|000\n' \
          '007|000|000\n' \
          '---|---|---\n' \
          '090|640|000\n' \
          '005|000|000\n' \
          '070|500|603\n' \
          '---|---|---\n' \
          '000|000|130\n' \
          '800|002|009\n' \
          '000|050|400\n' \


class SudokuElement:
    """
    123|456|789
    200|000|000
    300|000|000
    ---|---|---
    400|000|000
    500|000|000
    600|000|000
    ---|---|---
    700|000|000
    800|000|000
    900|000|000

    11|12|13
    --|--|--
    12|22|23
    --|--|--
    13|23|33
    """

    def __init__(self, solution, row, column, zone):
        self.solution = solution
        if self.solution < 0 or self.solution > 9:
            raise ValueError('Sudoku elements must take value between 1 and 9 or 0 for uknnown value')
        self.solved = False if self.solution == 0 else True
        self.row = row
        self.column = column
        self.zone = zone
        self.possible_values = set() if self.solved is True else set(range(1, 10))

    def __str__(self):
        return 'Value at ' + ' is ' + str(self.solution)


def sudoku_string_to_sudoku_logic(sudoku_string):
    sudoku_string = retrieve_digits_from_string(sudoku_string)
    if len(sudoku_string) != 81:
        raise Exception('Unexpected number of elements in problem - should be 81')
    sudoku_logic = list()
    for element in sudoku_string:
        sudoku_logic.append(SudokuElement(int(element), 1, 1, 11))
    return sudoku_logic

def retrieve_digits_from_string(string):
    result = ''

    for symbol in string:
        if symbol.isdigit():
            result += symbol

    return result


if _name_ == '_main_':
    print(problem)
    dupa = SudokuElement(1, 1, 1, 11)
    print(dupa)
    sudoku_list = sudoku_string_to_sudoku_logic(problem)

# dopisać test