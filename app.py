from flask import Flask, redirect, url_for, render_template
from main_page import main_page

app = Flask(__name__) # создание объекта приложения
app.register_blueprint(main_page)
# redirect - перенаправление
# url_for - для ссылок (см. в 1 лабе как фото вставлять)
# render_template - отвечает за рендеринг шаблонов (создание html-текста для браузера)

