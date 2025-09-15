import pytest
from line import Line  # предполагаем, что класс Line находится в line.py


class TestLine:

    def test_column_widths_initialization(self):
        """Тест 1: правильная инициализация column_widths"""
        line = Line([3, 5, 2])
        assert line.column_widths == [3, 5, 2]

        # пустой список
        empty_line = Line([])
        assert empty_line.column_widths == []

    def test_get_line_of_dashes(self):
        """Тест 2: корректная генерация линии дефисов"""
        line = Line([3, 5, 2])
        assert line.get_line_of_dashes() == "------------"

        empty_line = Line([])
        assert empty_line.get_line_of_dashes() == ""

    def test_get_line_of_dashes_and_plus(self):
        """Тест 3: корректная генерация линии с +"""
        line = Line([3, 5, 2])
        expected = "+-----+-------+----+"
        assert line.get_line_of_dashes_and_plus() == expected

        empty_line = Line([])
        assert empty_line.get_line_of_dashes_and_plus() == "++"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
