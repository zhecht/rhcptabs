from flask import *
from controllers.functions import *

album = Blueprint('album', __name__, template_folder='views')

def get_href_html(album, venue, song_idx, tab):
	#return "<a href=\"javascript:openTabsWindow('/static/tabs/{}/{}/{}')\">{}</a>".format(album, song_idx, tab, tab)
	if album == "live":
		return "<a href='/static/tabs/{}/{}/{}/{}' target='_blank'>{}</a>".format(album, venue, song_idx, tab, tab)
	return "<a href='/static/tabs/{}/{}/{}' target='_blank'>{}</a>".format(album, song_idx, tab, tab)

def get_tab_html(album, venue, idx, tabs):
	html = ""
	for which in ["tab", "chords", "solo", "lyrics", "bass", "drums"]:
		tab = "{}.pdf".format(which)
		if which not in ["chords", "solo"]:
			html += "<td>"
		if tab in tabs:
			html += get_href_html(album, venue, idx, tab)
		elif which not in ["tab", "chords", "solo"]:
			html += "-"
		if which not in ["chords", "tab"]:
			html += "</td>"
	return html

@album.route('/album/<name>',methods=["GET"])
def album_route(name):
	song_list,album_data,album_instruments = get_songs(name)
	all_songs = []

	if name == "live":
		for concert in song_list:
			for idx, data in enumerate(concert["songs"]):
				all_songs.append({
					"title": data["title"],
					"tabs": data,
					"trackNo": idx+1,
					"type": concert['where']+" ("+concert['when']+")",
					"video": data["video"]
				})
	else:
		trackType = "Album"
		for idx, data in enumerate(song_list):
			if data["title"] == "B-Sides":
				trackType = "B-Side"
			else:
				all_songs.append({
					"trackNo": idx+1,
					"title": data["title"],
					"tabs": data,
					"type": trackType,
					"video": data["video"]
				})

	if not album_instruments:
		return render_template("album.html", all_songs=all_songs, url=name, pic_url=album_data['url'], album_name=album_data['name'])

	return render_template(
		"album.html",
		all_songs=all_songs,
		album_name=album_data['name'],
		url=name,pic_url=album_data['url'], acoustic=album_instruments['acoustic'],electric=album_instruments['electric'],bass=album_instruments['bass'],drums=album_instruments['drums']
	)


@album.route('/album/<name>/<num>',methods=["GET"])
def song_route(name,num):
	all_songs,album_data = get_songs(name)
	song = all_songs[num-1]
	all_tabs = []

	return render_template("song.html",song=song,url=name,pic_url=album_data['url'],album_name=album_data['name'])