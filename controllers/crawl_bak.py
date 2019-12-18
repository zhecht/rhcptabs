import argparse
import json
import urllib.request
from bs4 import BeautifulSoup as BS

def scrape_html(args):
	html = ""
	instrument = args.url.split("-")[-2]
	with urllib.request.urlopen(args.url) as fh:
		html = fh.read().decode("utf-8")
	#with open("out.txt") as fh:
	#	html = fh.read()
		
		
	#with open("out.txt", "w") as fh:
	#	fh.write(html)
	#	exit()
	soup = BS(html, "lxml")	
	j = json.loads(soup.find("div", class_="js-store").get("data-content"))
	#with open("out.json", "w") as fh:
	#	json.dump(j, fh, indent=4)
	#	exit()
	tab = j["store"]["page"]["data"]["tab_view"]["wiki_tab"]["content"]
	tab = tab.replace("[tab]", "").replace("[/tab]", "")
	
	comments = j["store"]["page"]["data"]["tab_view"]["last_comments"]
	if comments:
		tab += "\n\n\nLAST {} COMMENTS\n\n".format(len(comments))
		for comment in comments:
			tab += "{}: {}\n\n".format(comment["username"], comment["text"])

	url = "static/tabs/{}/{}/{}.txt".format(args.album, args.track, instrument)
	with open(url, "w") as fh:
		fh.write(tab)

# python controllers/crawl.py -a redhotchilipeppers -t 1 -u "https://tabs.ultimate-guitar.com/tab/red-hot-chili-peppers/true-men-dont-kill-coyotes-tabs-32459"
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-a", "--album", help="Album", required=True)
	parser.add_argument("-u", "--url", help="URL of ultimate-guitar", required=True)
	parser.add_argument("-t", "--track", help="Track number", type=int, required=True)
	#parser.add_argument("-i", "--instrument", help="Tab/Solo/Bass/Drums", required=True)
	
	args = parser.parse_args()
	scrape_html(args)