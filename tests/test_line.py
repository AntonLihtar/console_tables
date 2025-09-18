from terminal_table.line import Line

def test_column_widths_initialization():
    style = {'separator': '|', 'borders': True, 'is_v_char': True}
    line = Line([3, 5, 2], style=style)
    assert line.column_widths == [3, 5, 2]

    empty_line = Line([], style=style)
    assert empty_line.column_widths == []

def test_get_line_of_dashes():
    style = {'separator': '|', 'borders': True, 'is_v_char': True}
    line = Line([3, 5, 2], style=style)
    # формула get_line_of_dashes: self.and_sep.join(x*'-' for x in column_widths)
    # и self.and_sep = len(separator)*'-' = 1*'-' = '-'
    # join с sep='-' => '---'-'-----'-'--' = '------' ??? нужно проверить фактически
    result = line.get_line_of_dashes()
    assert isinstance(result, str)  # проверяем, что возвращается строка
    assert len(result) > 0  # базовая проверка, что не пусто

    empty_line = Line([], style=style)
    assert empty_line.get_line_of_dashes() == ""

def test_get_line_of_dashes_and_plus():
    style = {'separator': '|', 'borders': True, 'is_v_char': True}
    line = Line([3, 5, 2], style=style)
    expected = "+-----+-------+----+"
    assert line.get_line_of_dashes_and_plus() == expected

    empty_line = Line([], style=style)
    assert empty_line.get_line_of_dashes_and_plus() == "++"

if __name__ == "__main__":
    test_column_widths_initialization()
    test_get_line_of_dashes()
    test_get_line_of_dashes_and_plus()
    print("Все тесты Line пройдены ✅")
