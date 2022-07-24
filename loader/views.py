# Добавляем импорт шаблонизатора
from flask import render_template, Blueprint, request

# Импортируем функции
from loader.utils import save_picture, adding_post


# Задаем имя блюпринту и путь к шаблонам
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


# Добавляем вьюшку на страницу добавления поста
@loader_blueprint.route('/post/', methods=['GET'])
def add_post_page():
    return render_template("post_form.html")


# Добавляем вьюшку для добавления поста
@loader_blueprint.route('/post/', methods=['POST'])
def adding_get_post():
    # Получаем со страницы картинку для добавления и записываем ее в переменную
    add_picture = request.files.get('picture')
    # Получаем со страницы текст для добавления и записываем его в переменную
    add_text = request.form.get('content')

    # Если нет картинки или текста, то выдаем сообщение об этом
    if not add_picture or not add_text:
        return 'Для добавления поста не хватает картинки или текста'

    # Сохраняем картинку и записываем в переменную путь к ней
    path_picture = '/' + save_picture(add_picture)
    # Передаем в функцию добавления поста путь к картинке и текст поста и результат
    # этой функции(сам добавляемый пост) записываем в переменную
    post = adding_post({'pic': path_picture, 'content': add_text})
    return render_template("post_uploaded.html", post=post)
