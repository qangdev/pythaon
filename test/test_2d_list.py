from typing import List

list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_in_list = [list_1, list_2]



def get_values_at_column(col_index: int, data: List[list]):
    # This function should return all values at the given column index
    result = []
    for i in range(len(data)):
        a = data[i][col_index]
        result.append(a)
    return result


def get_cell_value_at(x: int, y: int, data: List[list]):
    # This function should return a values at the given row index (x), and column index (y)
    return data[x][y]


def test_get_values_at_column_returns_a_list_of_value():
    assert get_values_at_column(0, list_in_list) == [1, 6]
    assert get_values_at_column(2, list_in_list) == [3, 8]
    # assert get_values_at_column(13, list_in_list) is None  list index out of range (make unittest fail)


def test_get_cell_value_at_returns_a_single_value():
    assert get_cell_value_at(0, 1, list_in_list) == 2
    assert get_cell_value_at(1, 0, list_in_list) == 6
#     assert get_cell_value_at(100, 100, list_in_list) is None   list index out of range (make unit-test fail)
