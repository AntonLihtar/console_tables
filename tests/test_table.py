import pytest
from table import Table  # предполагаем, что основной файл называется table.py


class TestTable:
    def test_list_of_lists_with_headers(self):
        """Тест 1: данные — список списков с заголовками"""
        table = Table(data=[
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ], headers=["City name", "Area", "Population", "Annual Rainfall"])

        assert table.headers == ["City name", "Area", "Population", "Annual Rainfall"]
        assert table.rows == [
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ]

    def test_dict_data(self):
        """Тест 2: данные — словарь"""
        table = Table(data={
            "City name2": ["Adelaide", "Brisbane"],
            "Area2": [1295, 5905],
            "Population2": [1158259, 1857594],
            "Annual Rainfall2": [600.5, 1146.4]
        })

        assert table.headers == ["City name2", "Area2", "Population2", "Annual Rainfall2"]
        assert table.rows == [
            ("Adelaide", 1295, 1158259, 600.5),
            ("Brisbane", 5905, 1857594, 1146.4)
        ]

    def test_single_list(self):
        """Тест 3: одна строка — просто список"""
        table = Table(data=["Alice", 30, "Engineer"])

        assert table.headers == ["column 1", "column 2", "column 3"]
        assert table.rows == [["Alice", 30, "Engineer"]]

    def test_list_of_lists_without_headers(self):
        """Тест 4: список списков без заголовков"""
        table = Table(data=[
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ])

        assert table.headers == ["column 1", "column 2", "column 3", "column 4"]
        assert table.rows == [
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4]
        ]

    def test_empty_data(self):
        """Тест 5: пустые данные"""
        table = Table(data=[])
        assert table.headers == []
        assert table.rows == []

        table2 = Table(data=None)
        assert table2.headers == []
        assert table2.rows == []

    def test_column_widths_calculation(self):
        """Тест 6: вычисление ширины колонок"""
        table = Table(data=[
            ["A", "LongHeader"],
            ["VeryLongValue", "B"]
        ], headers=["Short", "Header"])

        # Проверяем, что ширины вычисляются правильно
        # (точные значения зависят от реализации)
        assert len(table.column_widths) == 2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])