import logging
from json import JSONDecodeError

from flask import render_template, Blueprint, request

# Импортируем созданные функции
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
    # Если у добавляемого файла неверное расширение, то:
    if add_picture.filename.split('.')[-1] not in ['ipg', 'png']:
        # Записываем сообщение об этом в файл лога
        logging.info('Добавляется не картинка')
        # И выдаем сообщение на экран
        return 'Добавлять можно ТОЛЬКО файлы .jpg или .png'

    # Сохраняем картинку, путь к ней записываем в переменную для добавления в JSON-файл
    path_picture = '/' + save_picture(add_picture)

    # Если нет ошибок, то:
    try:
        # Передаем в функцию добавления поста путь к картинке и текст поста и результат
        # этой функции(сам добавляемый пост) записываем в переменную
        post = adding_post({'pic': path_picture, 'content': add_text})
    # Если нет JSON-файла для добавления, то сообщение об этом записываем в лог и выдаем на экран
    except FileNotFoundError:
        logging.error('Файл, для добавления в него данных, не найден')
        return 'Файл, для добавления в него данных, не найден'
    # Если JSON-файл не читается, то сообщение об этом записываем в лог и выдаем на экран
    except JSONDecodeError:
        logging.error('Невозможно прочитать файл с данными, для добавления в него')
        return 'Невозможно прочитать файл с данными, для добавления в него'

    # Возвращаем страницу по шаблону, с добавляемым постом
    return render_template("post_uploaded.html", post=post)
