#-*- coding: utf-8 -*-
import json
import os
import glob
from subprocess import call

url = "/home/zhecht/rhcptabs/"
url = ""

def read_data():
	with open("{}static/data.json".format(url)) as fh:
		data = json.loads(fh.read())
	for concert in data["live_concerts"]:
		data["all_songs"][concert["id"]] = concert["songs"]
	return data

if __name__ == '__main__':
	data = read_data()
	albums = os.listdir("static/tabs")
	for album in albums:
		if album.startswith(".DS"):
			continue
		path = "static/tabs/{}".format(album)
		venues = [""]
		if album == "live":
			venues = os.listdir(path)
		
		for venue in venues:
			if venue.startswith(".DS"):
				continue
			if venue:
				path = "static/tabs/{}/{}".format(album, venue)
			song_list = os.listdir(path)
			for song in song_list:
				if song.startswith(".DS"):
					continue
				txt_files = glob.glob("{}/{}/*.txt".format(path, song))
				for txt in txt_files:
					if txt.endswith("tabs.txt"):
						os.remove(txt)
						continue

					# EM dash -> regular hyphen-minus
					call(["gsed", "-i", "s/—/-/g", txt])
					call(["gsed", "-i", "s/–/-/g", txt])
					# weird '
					call(["gsed", "-i", "s/’/'/g", txt])
					
					if 0 and txt.endswith("chords.txt"):
						call(["gsed", "-i", "s/\[ch\]//g", txt])
						call(["gsed", "-i", "s/\[\/ch\]//g", txt])

					if album == "live":
						print(venue, song)
						song_name = data["all_songs"][venue][int(song) - 1]
					else:
						song_name = data["all_songs"][album][int(song) - 1]
					call(["enscript", "-B", "-t", song_name, "-f", "Courier7", "-p", "file.ps", txt])
					call(["ps2pdf", "file.ps", "{}.pdf".format(txt[:-4])])
					#os.remove("{}".format(txt))
					#exit()