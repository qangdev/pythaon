from typing import List

my_list = [1, 2, 3, 4, 5]


def get_values_at_index(col_index: int, data: List[list]):
    # This function should return all values at the given column index
    pass


def test_get_values_at_index_returns_a_value():
    assert get_values_at_column(0, list_in_list) == [1, 6]
    assert get_values_at_column(2, list_in_list) == [3, 8]
    assert get_values_at_column(13, list_in_list) is None
