# Добавляем импорт шаблонизатора
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

    try:
        # Если ошибок нет, то ищем и записываем в переменную список всех постов с заданным словом
        found_posts = search_posts(word_search)
    # Если нет такого JSON-файла, то выдаем сообщение
    except FileNotFoundError:
        return 'Файл с данными для поиска не найден'

    # Возвращаем страницу по шаблону, с заданным словом для поиска и списком найденных постов
    return render_template("post_list.html", word_search=word_search, found_posts=found_posts)
