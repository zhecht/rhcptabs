from flask import *
add = Blueprint('add', __name__, template_folder='views')

@add.route('/add',methods=["GET"])
def add_route():

  return render_template("add.html")