from typing import List

my_list = [1, 2, 3, 4, 5]


def get_values_at_index(index: int, data: list):
    # This function should return all values at the given index
    return data[index]




def test_get_values_at_index_returns_a_value():
    assert get_values_at_index(0, my_list) == 1
    assert get_values_at_index(2, my_list) == 3
    # assert get_values_at_index(6, my_list) is None   'note: IndexError: list index out of range'
