import re


def validate_login(login: str) -> bool:
    pattern = r'^[A-Za-z][A-Za-z0-9_]{3,18}[A-Za-z0-9]$'
    return bool(re.fullmatch(pattern, login))


def find_dates(text: str):
    pattern = r'\b\d{1,2}[./-]\d{1,2}[./-](?:\d{2}|\d{4})\b'
    return re.findall(pattern, text)


def parse_log(log: str):
    pattern = (
        r'(?P<date>\d{4}-\d{2}-\d{2})\s+'
        r'(?P<time>\d{2}:\d{2}:\d{2}).*?'
        r'user=(?P<user>\w+)\s+'
        r'action=(?P<action>\w+)\s+'
        r'ip=(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
    )
    match = re.search(pattern, log)
    return match.groupdict() if match else None


def validate_password(password: str) -> bool:
    pattern = (
        r'^(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'(?=.*\d)'
        r'(?=.*[!@#$%^&*])'
        r'.{8,}$'
    )
    return bool(re.fullmatch(pattern, password))


def validate_email(email: str, domains: list) -> bool:
    domain_pattern = "|".join(map(re.escape, domains))
    pattern = rf'^[A-Za-z0-9._%+-]+@(?:{domain_pattern})$'
    return bool(re.fullmatch(pattern, email))


def normalize_phone(phone: str) -> str:
    digits = re.sub(r'\D', '', phone)

    if len(digits) == 10:
        digits = '7' + digits
    elif digits.startswith('8'):
        digits = '7' + digits[1:]
    
    if len(digits) != 11:
        return "Не коректный номер"

    return '+' + digits


# ===== ПРИМЕРЫ ЗАПУСКА =====

if __name__ == "__main__":

    print("Валидация логина")
    print("user_123 ->", validate_login("user_123"))
    print("1badlogin ->", validate_login("1badlogin"))
    print()

    print("Поиск дат")
    text = "Встречи: 1.02.2024, 12-03-24 и 7/7/2025"
    print("Найденные даты:", find_dates(text))
    print()

    print("Парсинг лога")
    log = "2024-02-10 14:23:01 INFO user=ada action=login ip=192.168.1.15"
    print(parse_log(log))
    print()

    print("Проверка пароля")
    print("Password1! ->", validate_password("Password1!"))
    print("weakpass ->", validate_password("weakpass"))
    print()

    print("Проверка email")
    domains = ['gmail.com', 'yandex.ru', 'edu.ru']
    print("test@gmail.com ->", validate_email("test@gmail.com", domains))
    print("test@mail.com ->", validate_email("test@mail.com", domains))
    print()

    print("Нормализация телефона")
    print("8(999)123-45-67 ->", normalize_phone("8(999)123-45-67"))
    print("+7 999 123 45 67 ->", normalize_phone("999 123 45 67"))
    print("+7 999 123 45 67 ->", normalize_phone("863 123 45 67"))