from typing import List, Dict, Any
import csv


def read_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Читает данные из нескольких CSV файлов и возвращает объединенный список

    Args:
        file_paths: Список путей к CSV файлам

    Returns:
        List[Dict]: Объединенные данные из всех файлов

    Raises:
        FileNotFoundError: Если файл не существует
        ValueError: Если файл имеет неверный формат
    """
    all_data = []

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                required_fields = ['name', 'brand', 'price', 'rating']
                if not all(field in reader.fieldnames for field in required_fields):
                    raise ValueError(f"Файл {file_path} не содержит все обязательные поля: {required_fields}")

                for row in reader:
                    try:
                        row['price'] = float(row['price'])
                        row['rating'] = float(row['rating'])
                    except ValueError:
                        raise ValueError(f"Неверный формат числовых данных в файле {file_path}")

                    all_data.append(row)

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {file_path} не найден")
        except Exception as e:
            raise ValueError(f"Ошибка при чтении файла {file_path}: {e}")

    return all_data
