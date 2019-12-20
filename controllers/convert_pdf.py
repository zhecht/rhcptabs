import os
import glob
from subprocess import call

if __name__ == '__main__':
	albums = os.listdir("static/tabs")
	for album in albums:
		if album.startswith(".DS"):
			continue
		path = "static/tabs/{}".format(album)
		if album == "live":
			path = "static/tabs/live/{}".format(album)
		try:
			song_list = os.listdir(path)
		except:
			continue
		
		for song in song_list:
			if song.startswith(".DS"):
				continue
			txt_files = glob.glob("{}/{}/*.txt".format(path, song))
			for txt in txt_files:
				if txt.endswith("tabs.txt"):
					os.remove(txt)
					continue
				call(["enscript", "-B", "-f", "Courier7", "-p", "file.ps", txt])
				call(["ps2pdf", "file.ps", "{}.pdf".format(txt[:-4])])
				os.remove("{}".format(txt))