import logging

from flask import Flask, send_from_directory

# Импортируем блюпринты из пакетов
from main.views import main_blueprint
from loader.views import loader_blueprint

# Определяем пути для файлов
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Запускаем логирование в указанный файл и с указанным уровнем
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding='utf-8')


# Добавляем вьюшку, разрешающую загружать файлы в указанный каталог
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run()
