import re

def is_valid_date(date_str):
    # Регулярное выражение для проверки формата даты
    pattern = r"^\d{2}\s(Янв|Фев|Мар|Апр|Май|Июн|Июл|Авг|Сен|Окт|Ноя|Дек),\s\d{4}$"
    return re.match(pattern, date_str) is not None

# Тестирование
dates = [
    "21 Янв, 1978",   # корректная дата
    "32 Янв, 1978",   # некорректный день
    "21 Jan, 1978",   # некорректный месяц
    "21 Янв 1978",    # отсутствует запятая
    "21 Янв, 78",     # некорректный год
]

for date in dates:
    print(f"'{date}' is valid: {is_valid_date(date)}")
