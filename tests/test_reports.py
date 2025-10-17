from reports import ReportGenerator
import pytest


class TestReportGenerator:

    def setup_method(self):
        self.report_generator = ReportGenerator()

    def test_generate_average_rating_report(self):
        """Тест генерации отчета среднего рейтинга"""
        test_data = [
            {'name': 'iphone 15 pro', 'brand': 'apple', 'price': 999, 'rating': 4.9},
            {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': 1199, 'rating': 4.8},
            {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': 199, 'rating': 4.6},
            {'name': 'iphone 14', 'brand': 'apple', 'price': 799, 'rating': 4.7},
        ]

        result = self.report_generator.generate_report('average-rating', test_data)

        assert 'headers' in result
        assert 'rows' in result
        assert result['headers'] == ['#', 'brand', 'rating']

        assert result['rows'][0][1] == 'apple'
        assert result['rows'][0][2] == 4.8

        assert len(result['rows']) == 3

    def test_generate_average_rating_report_empty_data(self):
        """Тест генерации отчета с пустыми данными"""
        result = self.report_generator.generate_report('average-rating', [])

        assert result['headers'] == ['#', 'brand', 'rating']
        assert result['rows'] == []

    def test_generate_unknown_report(self):
        """Тест генерации неизвестного отчета"""
        with pytest.raises(ValueError, match="Неизвестный тип отчета"):
            self.report_generator.generate_report('unknown-report', [])

    def test_get_available_reports(self):
        """Тест получения списка доступных отчетов"""
        reports = self.report_generator.get_available_reports()
        assert 'average-rating' in reports
