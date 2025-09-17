from table import has_nested_lists

def test_with_nested_lists():
    lst = [[1, 2], [3, 4]]
    assert has_nested_lists(lst) is True

def test_with_mixed_elements():
    lst = [1, [2, 3], 4]
    assert has_nested_lists(lst) is True

def test_with_flat_list():
    lst = [1, 2, 3, 4]
    assert has_nested_lists(lst) is False

def test_with_empty_list():
    lst = []
    assert has_nested_lists(lst) is False

def test_with_list_of_strings():
    lst = ["a", "b", "c"]
    assert has_nested_lists(lst) is False
