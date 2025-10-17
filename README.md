# Brand Rating Analysis Tool

Скрипт для анализа рейтинга брендов из CSV файлов.

## Установка

```bash
  pip install -r requirements.txt
```

## Использование

```bash
  python main.py --files products.csv --report average-rating
```

### Пример
```bash
  python main.py --files csv/products1.csv csv/products2.csv --report average-rating
```

## Формат CSV файлов

Файлы должны содержать колонки:
```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
```

## Пример вывода

```
+-----+---------+----------+
|   # | brand   |   rating |
+=====+=========+==========+
|   1 | apple   |     4.55 |
|   2 | samsung |     4.53 |
|   3 | xiaomi  |     4.37 |
+-----+---------+----------+
```

## Тестирование

```bash
  pytest tests/ -v
```

## Структура проекта

- `main.py` - основной скрипт
- `reports.py` - генерация отчетов
- `file_reader.py` - чтение CSV файлов
- `tests/` - тесты
- `requirements.txt` - зависимости
