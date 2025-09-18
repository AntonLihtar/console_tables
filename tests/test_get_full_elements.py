from terminal_table.table import get_full_elements

def test_left_alignment():
    elements = ["cat", "dog"]
    column_widths = [5, 6]
    result = get_full_elements(elements, column_widths, align="left")
    assert result == ["cat  ", "dog   "]


def test_right_alignment():
    elements = ["cat", "dog"]
    column_widths = [5, 6]
    result = get_full_elements(elements, column_widths, align="right")
    assert result == ["  cat", "   dog"]


def test_center_alignment():
    elements = ["cat", "dog"]
    column_widths = [5, 6]
    result = get_full_elements(elements, column_widths, align="center")
    assert result == [" cat ", " dog  "]


def test_int_elements():
    elements = [1, 123]
    column_widths = [4, 5]
    result = get_full_elements(elements, column_widths)
    assert result == ["1   ", "123  "]


def test_empty_string():
    elements = [""]
    column_widths = [3]
    result = get_full_elements(elements, column_widths)
    assert result == ["   "]

if __name__ == "__main__":
    test_left_alignment()
    test_right_alignment()
    test_center_alignment()
    test_int_elements()
    test_empty_string()
    print("Все тесты Line пройдены ✅")
