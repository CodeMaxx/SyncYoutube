import mechanize as mech
import subprocess
import os
from bs4 import BeautifulSoup

playlist = [];
def download():
	br = mech.Browser()
	br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

	br.open("https://www.youtube.com/channel/UCAgL0A1YpVwVwxQkSaWToUQ")
	soup = BeautifulSoup(br.response().read())
	i = 1
	for link in br.links():
		url_title = ""
		if (link.url).startswith ("/playlist?list"):
			url_title = soup.find_all("a")[i].getText()
			i=i+1
			if not os.path.exists(url_title):
				os.makedirs(url_title)
			os.chdir("./"+url_title)
			url_down = "youtube-dl " + "https://www.youtube.com" + link.url
			subprocess.call(url_down, shell=True)
			os.chdir("..")

download()
