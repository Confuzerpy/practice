import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(42, 42)


def test_wrong_format_len():
    with pytest.raises(ValueError):
        is_under_queen_attack('abc', 'a1')


def test_wrong_format_upper():
    with pytest.raises(ValueError):
        is_under_queen_attack('A1', 'a1')


def test_wrong_format_values():
    with pytest.raises(ValueError):
        is_under_queen_attack('aa', 'a1')


def test_checking_order():
    with pytest.raises(ValueError):
        is_under_queen_attack('a9', 1)


def test_under_attack_vertical():
    assert is_under_queen_attack('a1', 'a8') is True


def test_under_attack_horizontal():
    assert is_under_queen_attack('a1', 'h1') is True


def test_under_attack_diagonal():
    assert is_under_queen_attack('a1', 'c3') is True


def test_not_under_attack():
    assert is_under_queen_attack('a1', 'c2') is False


def test_equal_positions():
    assert is_under_queen_attack('a1', 'a1') is True


def test_very_accurate_test():
    assert open('yandex_testing_lesson.py').read() == '''columns = list('abcdefgh')
rows = list('12345678')

def is_under_queen_attack(position, queen_position):
    for p in (position, queen_position):
        if type(p) != str:
            raise TypeError('Wrong type of position {}'.format(p))

        if ((len(p) != 2) 
            or (p[1] not in rows) 
            or (p[0] not in columns)):
            raise ValueError('Wrong value of position {}'.format(p))

    p_column = position[0]
    qp_column = queen_position[0]
    p_row = position[1]
    qp_row = queen_position[1]

    if (p_row == qp_row 
        or p_column == qp_column
        or position in _diagonal_cells(queen_position)):
        return True

    return False


def _diagonal_cells(position):
    col, row = list(position)
    col_i = columns.index(col)
    row_i = rows.index(row)

    cells = []

    for board_row in rows:
        for board_col in columns:
            board_col_i = columns.index(board_col)
            board_row_i = rows.index(board_row)
            if abs(board_row_i - row_i) == abs(board_col_i - col_i):
                cells.append(board_col+board_row)

    return cells'''
