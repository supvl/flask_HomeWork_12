import logging
from json import JSONDecodeError

from flask import render_template, Blueprint, request

# Импортируем созданные функции
from main.utils import search_posts

# Задаем имя блюпринту и путь к шаблонам
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# Добавляем вьюшку на главную страницу
@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


# Добавляем вьюшку на страницу поиска
@main_blueprint.route('/search/')
def search_page():
    # Записываем в переменную слово, получаемое из формы поиска
    word_search = request.args.get('s', '')
    # Эаписываем в файл лога сообщение о поиске
    logging.info('Выполняется поиск')

    # Если ошибок нет, то ищем и записываем в переменную список всех постов с заданным словом
    try:
        found_posts = search_posts(word_search)
    # Если нет такого JSON-файла, то то сообщение об этом записываем в лог и выдаем на экран
    except FileNotFoundError:
        logging.error('Файл с данными для поиска не найден')
        return 'Файл с данными для поиска не найден'
    # Если JSON-файл не читается, то то сообщение об этом записываем в лог и выдаем на экран
    except JSONDecodeError:
        logging.error('Невозможно прочитать файл с данными для поиска по нему')
        return 'Невозможно прочитать файл с данными для поиска по нему'

    # Возвращаем страницу по шаблону, с заданным словом для поиска и списком найденных постов
    return render_template("post_list.html", word_search=word_search, found_posts=found_posts)
