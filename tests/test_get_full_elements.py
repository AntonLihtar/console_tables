from table import get_full_elements

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
