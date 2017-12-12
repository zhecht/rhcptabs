from flask import *
main = Blueprint('main', __name__, template_folder='views')

@main.route('/',methods=["GET"])
def main_route():

  return render_template("main.html")