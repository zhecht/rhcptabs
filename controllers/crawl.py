import argparse
import os
import json
import urllib.request
from bs4 import BeautifulSoup as BS
from time import sleep

def scrape_html(downloads):

	for idx, tab_data in enumerate(downloads["links"]):
		html = ""
		instrument = tab_data["url"].split("-")[-2]
		if "solo" in tab_data:
			instrument = "solo"
		elif instrument == "tabs":
			instrument = "tab"
		try:
			with urllib.request.urlopen(tab_data["url"]) as fh:
				html = fh.read().decode("utf-8")
		except:
			print("ERROR", tab_data)
			continue

		soup = BS(html, "lxml")	
		j = json.loads(soup.find("div", class_="js-store").get("data-content"))
		tab = j["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]
		tab = tab.replace("[tab]", "").replace("[/tab]", "")
		
		comments = j["store"]["page"]["data"]["tab_view"]["last_comments"]
		if comments:
			tab += "\n\n\nLAST {} COMMENTS\n\n".format(len(comments))
			for comment in comments:
				tab += "{}: {}\n\n".format(comment["username"], comment["text"])

		dir_ = "static/tabs/{}/{}".format(tab_data["album"], tab_data["track"])
		if "live" in tab_data:
			dir_ = "static/tabs/live/{}/{}".format(tab_data["where"], tab_data["track"])
		if not os.path.exists(dir_):
			os.mkdir(dir_)
		url = "{}/{}.txt".format(dir_, instrument)
		with open(url, "w") as fh:
			fh.write(tab)

		if idx > 20 and idx % 20 == 0:
			sleep(1)
		else:
			sleep(0.05)

if __name__ == '__main__':
	with open("downloads.json") as fh:
		downloads = json.loads(fh.read())
	scrape_html(downloads)