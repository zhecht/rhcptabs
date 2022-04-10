import os
import json
from sys import platform

url = "/home/zhecht/rhcptabs/"
#url = ""

albumTranslation = {
	"asphereintheheartofsilence": "A Sphere in the Heart of Silence",
	"awii": "AW II",
	"bloodsugarsexmagik": "Bloody Sugar Sex Magik",
	"bytheway": "By The Way",
	"californication": "Californication",
	"curtains": "Curtains",
	"dcep": "DC EP",
	"freakystyley": "Freaky Styley",
	"fromthesoundsinside": "From the Sounds Inside",
	"thegetaway": "The Getaway",
	"imbesideyou": "I'm Beside You",
	"imwithyou": "I'm With You",
	"insideofemptiness": "Inside of Emptiness",
	"leturlefr": "Letur-Lefr",
	"live": "All Live Shows",
	"mothersmilk": "Mother's Milk",
	"niandraladesandusuallyjustatshirt": "Niandra Lades and Usually Just a T-Shirt",
	"omarrodriguezlopez&johnfrusciante": "Omar Rodriguez Lopez & John Frusciante",
	"onehotminute": "One Hot Minute",
	"pbxfunicularintagliozone": "PBX Funicular Intaglio Zone",
	"redhotchilipeppers": "Red Hot Chili Peppers",
	"smilefromthestreetsyouhold": "Smile From the Streets You Hold",
	"shadowscollidewithpeople": "Shadows Collide With People",
	"stadiumarcadium": "Stadium Arcadium",
	"unlimitedlove": "Unlimited Love",
	"theempyrean": "The Empyrean",
	"theupliftmofopartyplan": "The Uplift Mofo Party Plan",
	"thewilltodeath": "The Will To Death",
	"torecordonlywaterfortendays": "To Record Only Water for Ten Days"
}

def stripPunctuation(s):
	return s.lower().replace(" ", "").replace("-", "").replace(".", "")

def read_data():
	with open("{}static/data.json".format(url)) as fh:
		data = json.loads(fh.read())
	return data

def get_songs(album_name):
	data = read_data()
	if album_name == "live":
		return data["live_concerts"], data["all_urls"]["live"], None
	urlData = {
		"url": f"{album_name}.jpg",
		"name": albumTranslation.get(album_name, "")
	}
	instr = data["all_album_instruments"].get(album_name, {
        "acoustic": "",
        "electric": "",
        "bass": "",
        "drums": ""
    })
	return data["all_songs"][album_name], urlData, instr

def get_tab_names(path,album_name,num):
	try:
		if path == "live":
			return os.listdir("{}static/tabs/live/{}/{}".format(url, album_name,num))
		return os.listdir("{}static/tabs/{}/{}".format(url, album_name,num))
	except:
		return []
	


