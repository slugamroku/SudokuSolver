# problem = ('000|000|000\n' +
#            '000|000|000\n' +
#            '000|000|000\n' +
#            '---|---|---\n' +
#            '000|000|000\n' +
#            '000|000|000\n' +
#            '000|000|000\n' +
#            '---|---|---\n' +
#            '000|000|000\n' +
#            '000|000|000\n' +
#            '000|000|000\n'
#            )

# problem = ('000|300|060\n' +
#            '901|008|000\n' +
#            '007|000|000\n' +
#            '---|---|---\n' +
#            '090|640|000\n' +
#            '005|000|000\n' +
#            '070|500|603\n' +
#            '---|---|---\n' +
#            '000|000|130\n' +
#            '800|002|009\n' +
#            '000|050|400\n'
#            )

problem = ('409|800|170\n' +
           '001|040|308\n' +
           '035|006|000\n' +
           '---|---|---\n' +
           '000|003|090\n' +
           '690|057|003\n' +
           '000|004|627\n' +
           '---|---|---\n' +
           '926|008|451\n' +
           '150|020|030\n' +
           '000|001|902\n'
           )


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
        self.solved = False if self.solution == 0 else True
        self.row = row
        self.column = column
        self.zone = (-(self.row // -3) * 10) + -(self.column // -3)
        self.possible_values = set() if self.solved is True else set(range(1, 10))

    def __str__(self):
        return 'Value at row ' + str(self.row) + ' column ' + str(self.column) + ' zone ' + str(
            self.zone) + ' is ' + str(self.solution) + ' and is solved: ' + str(
            self.solved) + '. Possible values: ' + str(self.possible_values)

    def check_if_solved(self):
        if len(self.possible_values) == 1:
            self.solution == self.possible_values.pop()
            self.solved = True


def sudoku_string_to_sudoku_logic(sudoku_string):
    sudoku_string = retrieve_digits_from_string(sudoku_string)
    if len(sudoku_string) != 81:
        raise Exception('Unexpected number of elements in problem - should be 81')
    sudoku_logic = list()
    for index, element in enumerate(sudoku_string):
        row = (index // 9) + 1
        column = (index % 9) + 1
        sudoku_logic.append(SudokuElement(int(element), row, column))
        # print(sudoku_logic[index])
    return sudoku_logic


def sudoku_logic_to_sudoku_string(sudoku_logic):
    sudoku_string = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    for item in sudoku_logic:
        item_position_in_string = ((item.row - 1) * 9) + item.column - 1
        sudoku_string = (sudoku_string[:item_position_in_string]
                         + str(item.solution)
                         + sudoku_string[item_position_in_string + 1:]
                         )

    sudoku_string = (sudoku_string[0:3] + '|' + sudoku_string[3:6] + '|' + sudoku_string[6:9] + '\n' +
                     sudoku_string[9:12] + '|' + sudoku_string[12:15] + '|' + sudoku_string[15:18] + '\n' +
                     sudoku_string[18:21] + '|' + sudoku_string[21:24] + '|' + sudoku_string[24:27] + '\n' +
                     '---|---|---\n' +
                     sudoku_string[27:30] + '|' + sudoku_string[30:33] + '|' + sudoku_string[33:36] + '\n' +
                     sudoku_string[36:39] + '|' + sudoku_string[39:42] + '|' + sudoku_string[42:45] + '\n' +
                     sudoku_string[45:48] + '|' + sudoku_string[48:51] + '|' + sudoku_string[51:54] + '\n' +
                     '---|---|---\n' +
                     sudoku_string[54:57] + '|' + sudoku_string[57:60] + '|' + sudoku_string[60:63] + '\n' +
                     sudoku_string[63:66] + '|' + sudoku_string[66:69] + '|' + sudoku_string[69:72] + '\n' +
                     sudoku_string[72:75] + '|' + sudoku_string[75:78] + '|' + sudoku_string[78:81]
                     )
    return sudoku_string


def retrieve_digits_from_string(string):
    result = ''

    for symbol in string:
        if symbol.isdigit():
            result += symbol

    return result


def update_possible_values(list_of_elements):
    solved = [item for item in list_of_elements if item.solved]
    unsolved = [item for item in list_of_elements if not item.solved]

    for unsolved_item in unsolved:
        for solved_item in solved:
            if (
                    solved_item.row == unsolved_item.row
                    or solved_item.column == unsolved_item.column
                    or solved_item.zone == unsolved_item.zone
            ):
                # print(unsolved_item)
                # print(solved_item)
                unsolved_item.possible_values.discard(solved_item.solution)

        unsolved_item.check_if_solved()

        if unsolved_item.solved:
            solved.append(unsolved_item)


if __name__ == '__main__':
    print(problem)
    # example = SudokuElement(0, 1, 1)
    # print(example)
    sudoku_list = sudoku_string_to_sudoku_logic(problem)

    i = 1

    while i <= 5:
        # for item in sudoku_list:
        #     print(item)

        update_possible_values(sudoku_list)

        print(sudoku_logic_to_sudoku_string(sudoku_list))

        print('---------------------------------------------------------------')

        i += 1

# write some tests
'''
items = [1,2,3,4,5,6,7,8]

odd = lambda x: x % 2 > 0

for x in filter(odd, items):
    print(x)
'''
