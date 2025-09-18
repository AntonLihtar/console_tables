from terminal_table.table import has_nested_lists

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

if __name__ == "__main__":
    test_with_nested_lists()
    test_with_mixed_elements()
    test_with_flat_list()
    test_with_empty_list()
    test_with_list_of_strings()
    print("Все тесты Line пройдены ✅")

