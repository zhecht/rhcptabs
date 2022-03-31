import os
import json

url = "/home/zhecht/rhcptabs/"
url = ""

def read_data():
	with open("{}static/data.json".format(url)) as fh:
		data = json.loads(fh.read())
	return data

def get_songs(album_name):
	data = read_data()
	if album_name == "live":
		return data["live_concerts"], data["all_urls"]["live"], None
	return data["all_songs"][album_name], data["all_urls"][album_name], data["all_album_instruments"][album_name]

def get_tab_names(path,album_name,num):
	try:
		if path == "live":
			return os.listdir("{}static/tabs/live/{}/{}".format(url, album_name,num))
		return os.listdir(f"{url}static/tabs/{album_name}/{num}")
	except:
		return []
	


