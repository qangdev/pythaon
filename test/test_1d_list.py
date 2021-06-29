from typing import List

my_list = [1, 2, 3, 4, 5]

# This function should return all values at the given index
# https://stackoverflow.com/questions/54981448/how-to-avoid-indexerror-list-index-out-of-range-error
def get_values_at_index(index: int, data: list):
    try:
        return data[index]
    except IndexError:
        return None



def test_get_values_at_index_returns_a_value():
    assert get_values_at_index(0, my_list) == 1
    assert get_values_at_index(2, my_list) == 3
    assert get_values_at_index(6, my_list) is None
