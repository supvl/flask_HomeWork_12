import json


def reading_file() -> list[dict]:
    """
    Загружаем из заданного JSON-файла все данные
    :return: Список всех постов
    """
    # Задаем JSON-файл
    json_file = 'posts.json'
    # Открываем заданный файл на чтение
    with open(json_file, 'r', encoding='utf-8') as file:
        # Загружаем в переменную список словарей из открытого файла
        post_list = json.load(file)
    return post_list


def search_posts(word: str) -> list[dict]:
    """
    В общем списке постов ищем посты с заданным словом
    :param word: заданное слово
    :return: список найденных постов
    """
    # Задаем переменную для найденногосписка постов
    found_posts = []
    # Запускаем цикл по всему списку постов
    for post in reading_file():
        # Если заданное слово есть в очередном посте, то...
        if word.lower() in post['content'].lower():
            # ...добавляем этот пост в список найденных
            found_posts.append(post)
    return found_posts
