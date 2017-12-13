from flask import *
from controllers.functions import *

album = Blueprint('album', __name__, template_folder='views')

@album.route('/album/<name>',methods=["GET"])
def album_route(name):
  song_list,album_data = get_songs(name)
  instrument = request.args.get('instrument')
  all_songs = []

  if name == "live":
    for concert in song_list:
      idx = 1
      for song in concert['songs']:
        tabs = get_tab_names(name,concert['id'],idx)
        if len(tabs) == 0:
          tabs = "None"
        #print(song,tabs,concert['id'],idx)
        all_songs.append({'id': concert['id'], 'where': concert['where'], 'when': concert['when'], 'title': song, 'tabs': tabs, 'idx': idx})
        idx += 1
  else:
    idx = 1
    for song in song_list:
      tabs = get_tab_names(name,name,idx)

      if len(tabs) == 0:
        tabs = "None"
      idx += 1
      all_songs.append({'title':song,'tabs':tabs})
  print(all_songs)
  return render_template("album.html",all_songs=all_songs,url=name,pic_url=album_data['url'],album_name=album_data['name'],instrument=instrument)


@album.route('/album/<name>/<num>',methods=["GET"])
def song_route(name,num):
  all_songs,album_data = get_songs(name)
  song = all_songs[num-1]
  instrument = request.args.get('instrument')
  all_tabs = []

  return render_template("song.html",song=song,url=name,pic_url=album_data['url'],album_name=album_data['name'],instrument=instrument)