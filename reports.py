from typing import List, Dict, Any
from collections import defaultdict


class ReportGenerator:
    """Генератор различных отчетов на основе данных о товарах"""

    def __init__(self):
        self.report_handlers = {
            'average-rating': self._generate_average_rating_report
        }

    def generate_report(self, report_type: str, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Генерирует отчет указанного типа

        Args:
            report_type: Тип отчета
            data: Данные для анализа

        Returns:
            Dict: Данные для отображения отчета

        Raises:
            ValueError: Если тип отчета не поддерживается
        """
        if report_type not in self.report_handlers:
            raise ValueError(f"Неизвестный тип отчета: {report_type}")

        return self.report_handlers[report_type](data)

    def _generate_average_rating_report(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Генерирует отчет со средним рейтингом по брендам

        Args:
            data: Список словарей с данными о товарах

        Returns:
            Dict: Заголовки и строки для таблицы отчета
        """
        if not data:
            return {
                'headers': ['#', 'brand', 'rating'],
                'rows': []
            }

        brand_ratings = defaultdict(list)
        for item in data:
            brand = item['brand'].strip().lower()
            brand_ratings[brand].append(item['rating'])

        brand_avg_ratings = []
        for brand, ratings in brand_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            brand_avg_ratings.append({
                'brand': brand,
                'avg_rating': round(avg_rating, 2)
            })

        brand_avg_ratings.sort(key=lambda x: x['avg_rating'], reverse=True)

        rows = []
        for i, brand_data in enumerate(brand_avg_ratings, 1):
            rows.append([i, brand_data['brand'], brand_data['avg_rating']])

        return {
            'headers': ['#', 'brand', 'rating'],
            'rows': rows
        }

    def get_available_reports(self) -> List[str]:
        """Возвращает список доступных типов отчетов"""
        return list(self.report_handlers.keys())
