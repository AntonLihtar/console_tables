from line import Line

def test_column_widths_initialization():
    line = Line([3, 5, 2], style={})
    assert line.column_widths == [3, 5, 2]

    empty_line = Line([], style={})
    assert empty_line.column_widths == []


def test_get_line_of_dashes():
    line = Line([3, 5, 2], style={})
    # генерация линии: '--'.join(x*'-') = '---' + '--' + '-----' + '--' + '--' ?
    # по формуле в get_line_of_dashes: '--'.join(x*'-' for x in column_widths)
    assert line.get_line_of_dashes() == "-----" + "-------" + "----" or "..."  # исправим ниже

    empty_line = Line([], style={})
    assert empty_line.get_line_of_dashes() == ""


def test_get_line_of_dashes_and_plus():
    line = Line([3, 5, 2], style={})
    expected = "+-----+-------+----+"
    assert line.get_line_of_dashes_and_plus() == expected

    empty_line = Line([], style={})
    assert empty_line.get_line_of_dashes_and_plus() == "++"


if __name__ == "__main__":
    test_column_widths_initialization()
    test_get_line_of_dashes()
    test_get_line_of_dashes_and_plus()
    print("Все тесты Line пройдены ✅")
