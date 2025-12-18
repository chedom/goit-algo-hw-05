def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(main_string, pattern):
    """Алгоритм Боєра-Мура для пошуку підрядка в рядку."""
    # Створюємо таблицю зсувів для патерну
    shift_table = build_shift_table(pattern)
    i = 0  # Початковий індекс у головному тексті

    # Проходимо по головному тексту, порівнюючи з підрядком
    while i <= len(main_string) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до початку
        while j >= 0 and main_string[i + j] == pattern[j]:
            j -= 1

        # Якщо весь підрядок збігається, повертаємо позицію
        if j < 0:
            return i

        # Зсуваємо індекс i на основі таблиці зсувів
        # Беремо зсув для символу з тексту, що не збігся
        i += shift_table.get(main_string[i + len(pattern) - 1], len(pattern))

    # Якщо підрядок не знайдено
    return -1
