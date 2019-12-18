from flask import *
from controllers.functions import *

album = Blueprint('album', __name__, template_folder='views')

def get_href_html(album, song_idx, tab):
	return "<a href=\"javascript:openTabsWindow('/static/tabs/{}/{}/{}')\">{}</a>".format(album, song_idx, tab, tab)

def get_tab_html(album, idx, tabs):
	html = ""
	for which in ["tab", "chords", "solo", "lyrics", "bass", "drums"]:
		tab = "{}.pdf".format(which)
		if which not in ["chords", "solo"]:
			html += "<td>"
		if tab in tabs:
			html += get_href_html(album, idx, tab)
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
			idx = 1
			for song in concert['songs']:
				tabs = get_tab_names(name, concert['id'], idx)
				if len(tabs) == 0:
					tabs = "None"
				
				all_songs.append({'id': concert['id'], 'where': concert['where'], 'when': concert['when'], 'title': song, 'tabs': tabs, 'idx': idx})
				idx += 1
	else:
		for idx, song in enumerate(song_list):
			tabs = get_tab_names(name, name, idx + 1)
			tab_html = get_tab_html(name, idx + 1, tabs)
			all_songs.append({'title':song, 'tabs':tabs, "tab_html": tab_html})

	if not album_instruments:
		return render_template("album.html", all_songs=all_songs, url=name, pic_url=album_data['url'], album_name=album_data['name'], instrument=instrument)  
	return render_template("album.html",all_songs=all_songs,url=name,pic_url=album_data['url'],album_name=album_data['name'], acoustic=album_instruments['acoustic'],electric=album_instruments['electric'],bass=album_instruments['bass'],drums=album_instruments['drums'])


@album.route('/album/<name>/<num>',methods=["GET"])
def song_route(name,num):
	all_songs,album_data = get_songs(name)
	song = all_songs[num-1]
	instrument = request.args.get('instrument')
	all_tabs = []

	return render_template("song.html",song=song,url=name,pic_url=album_data['url'],album_name=album_data['name'],instrument=instrument)