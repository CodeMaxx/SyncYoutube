import mechanize as mech
import subprocess

playlist = [];
def download():
	br = mech.Browser()
	br.open("https://www.youtube.com/channel/UCAgL0A1YpVwVwxQkSaWToUQ")

	for link in br.links():
		if link.url.startswith ("/playlist?list"):
			subprocess.call("youtube-dl " + "https://www.youtube.com" + link.url, shell=True)

download()