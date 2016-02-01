import mechanize as mech
import subprocess
import os

playlist = [];
def download():
	br = mech.Browser()
	br.open("Add the link here")  #Add the youtube link containing playlists you want to sync to local
	for link in br.links():
		url_title = ""
		if (link.url).startswith ("/playlist?list"):
			playlist.append(link)
	for link in playlist:
			br.open(link.url)
			url_title = br.title()[:-10]
			if not os.path.exists(url_title):
				os.makedirs(url_title)
			os.chdir("./"+url_title)
			url_down = "youtube-dl " + "https://www.youtube.com" + link.url
			subprocess.call(url_down, shell=True)
			os.chdir("..")

download()
