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


def save_picture(add_picture) -> str:
    """
    Сохраняет добавляемую картинку в указанный каталог
    :param add_picture: картинка для добавления в пост
    :return: путь сохранения добавляемой картинки
    """
    # Получаем имя файла картинки
    filename = add_picture.filename
    # Записываем в переменную путь для добавления картинки
    save_path = f'uploads/images/{filename}'
    # Сохраняем картинку по указанному пути
    add_picture.save(save_path)
    return save_path


def adding_post(add_post: dict) -> dict:
    """
    Добавляет полученный пост в JSON-файл
    :param add_post: получаемый пост в виде словаря
    :return: полученный пост
    """
    # Загружаем в переменную(в словарь) все данные из заданного JSON-файла
    all_posts = reading_file()
    # Добавляем полученный пост в загруженный ранее словарь с постами
    all_posts.append(add_post)
    # Открываем заданный JSON-файл на перезапись
    json_file = 'posts.json'
    with open(json_file, 'w', encoding='utf-8') as file:
        # Записываем в JSON-файл весь полученный словарь с постами
        json.dump(all_posts, file, ensure_ascii=False)
    return add_post
