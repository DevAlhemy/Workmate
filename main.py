"""
Скрипт для анализа рейтинга брендов из CSV файлов
"""

from file_reader import read_csv_files
from reports import ReportGenerator
from tabulate import tabulate
import argparse


def main():
    parser = argparse.ArgumentParser(description='Анализ рейтинга брендов')
    parser.add_argument('--files', nargs='+', required=True,
                        help='Пути к CSV файлам с данными')
    parser.add_argument('--report', required=True,
                        choices=['average-rating'],
                        help='Тип отчета для генерации')

    args = parser.parse_args()

    try:
        data = read_csv_files(args.files)

        report_generator = ReportGenerator()
        report_data = report_generator.generate_report(args.report, data)

        headers = report_data['headers']
        rows = report_data['rows']
        print(tabulate(rows, headers=headers, tablefmt='outline'))

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
    except Exception as e:
        print(f"Ошибка при выполнении скрипта: {e}")


if __name__ == '__main__':
    main()
