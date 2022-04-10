from flask import *
main = Blueprint('main', __name__, template_folder='views')

@main.route('/',methods=["GET"])
def main_route():
	return render_template("main.html")


@main.route('/frusciante',methods=["GET"])
def jfmain_route():
	albums = [
		{"title": "Niandra Lades and Usually Just a T-Shirt", "year": 1994},
		{"title": "Smile From the Streets You Hold", "year": 1997},
		{"title": "From the Sounds Inside", "year": 2001},
		{"title": "To Record Only Water for Ten Days", "year": 2001},
		{"title": "Shadows Collide with People", "year": 2004},
		{"title": "The Will to Death", "year": 2004},
		{"title": "DC EP", "year": 2004},
		{"title": "Inside of Emptiness", "year": 2004},
		#{"title": "Automatic Writing", "year": 2004},
		{"title": "A Sphere in the Heart of Silence", "year": 2004},
		{"title": "Curtains", "year": 2005},
		#{"title": "AWII", "year": 2007},
		{"title": "The Empyrean", "year": 2009},
		{"title": "Omar Rodriguez Lopez & John Frusciante", "year": 2010},
		{"title": "Letur-Lefr", "year": 2012},
		{"title": "PBX Funicular Intaglio Zone", "year": 2012},
		{"title": "Outsides", "year": 2013},
		{"title": "Enclosure", "year": 2014},
		{"title": "Maya", "year": 2020},
	]
	return render_template("jfmain.html", albums=albums)