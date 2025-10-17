from file_reader import read_csv_files
import tempfile
import pytest
import csv
import os


class TestFileReader:

    def test_read_csv_files_valid(self):
        """Тест чтения корректных CSV файлов"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f1:
            writer = csv.writer(f1)
            writer.writerow(['name', 'brand', 'price', 'rating'])
            writer.writerow(['iphone 15', 'apple', '999', '4.9'])
            file1 = f1.name

        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f2:
            writer = csv.writer(f2)
            writer.writerow(['name', 'brand', 'price', 'rating'])
            writer.writerow(['galaxy s23', 'samsung', '1199', '4.8'])
            file2 = f2.name

        try:
            data = read_csv_files([file1, file2])

            assert len(data) == 2
            assert data[0]['brand'] == 'apple'
            assert data[0]['price'] == 999.0
            assert data[0]['rating'] == 4.9
            assert data[1]['brand'] == 'samsung'

        finally:
            os.unlink(file1)
            os.unlink(file2)

    def test_read_csv_files_missing_file(self):
        """Тест чтения несуществующего файла"""
        with pytest.raises(FileNotFoundError):
            read_csv_files(['nonexistent_file.csv'])

    def test_read_csv_files_invalid_format(self):
        """Тест чтения файла с неверным форматом"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'brand', 'price'])  # Отсутствует rating
            file_path = f.name

        try:
            with pytest.raises(ValueError, match="не содержит все обязательные поля"):
                read_csv_files([file_path])
        finally:
            os.unlink(file_path)

    def test_read_csv_files_invalid_numeric_data(self):
        """Тест чтения файла с неверными числовыми данными"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'brand', 'price', 'rating'])
            writer.writerow(['iphone 15', 'apple', 'invalid_price', '4.9'])
            file_path = f.name

        try:
            with pytest.raises(ValueError, match="Неверный формат числовых данных"):
                read_csv_files([file_path])
        finally:
            os.unlink(file_path)
