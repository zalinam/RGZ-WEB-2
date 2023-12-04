from flask import Blueprint, redirect, url_for, render_template
main_page = Blueprint('main_page', __name__)

@main_page.route("/")
@main_page.route("/index")
def start():
     return redirect("/RGZ/main_page")

@main_page.route('/RGZ/main_page')
def mainpage():
    return render_template('main_page.html')