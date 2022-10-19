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
    21|22|23
    --|--|--
    31|32|33
    """

    def __init__(self, solution, row, column):
        self.solution = solution
        if self.solution < 0 or self.solution > 9:
            raise ValueError('Sudoku elements must take value between 1 and 9 or 0 for unknown value')
        self.solved = False
        self.check_if_solved()
        self.row = row
        self.column = column
        self.zone = (-(self.row // -3) * 10) + -(self.column // -3)
        self.possible_values = set() if self.solved is True else set(range(1, 10))

    def __str__(self):
        return 'Value at row ' + str(self.row) + ' column ' + str(self.column) + ' zone ' + str(self.zone) + ' is ' + str(self.solution)

    def check_if_solved(self):
        self.solved = False if self.solution == 0 else True


def sudoku_string_to_sudoku_logic(sudoku_string):
    sudoku_string = retrieve_digits_from_string(sudoku_string)
    if len(sudoku_string) != 81:
        raise Exception('Unexpected number of elements in problem - should be 81')
    sudoku_logic = list()
    for index, element in enumerate(sudoku_string):
        row = (index // 9) + 1
        column = (index % 9) + 1
        sudoku_logic.append(SudokuElement(int(element), row, column))
        #print(sudoku_logic[index])
    return sudoku_logic


def retrieve_digits_from_string(string):
    result = ''

    for symbol in string:
        if symbol.isdigit():
            result += symbol

    return result


if __name__ == '__main__':
    print(problem)
    # example = SudokuElement(0, 1, 1)
    # print(example)
    sudoku_list = sudoku_string_to_sudoku_logic(problem)

# write some tests
