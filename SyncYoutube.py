import subprocess
import os
import urllib.request as urlreq
import urllib.parse as urlparse
import simplejson as json
import sys

playlistIds = []
titles = []

def getPlaylistId():
	data = {}
	data['maxResults'] = '50'
	data['channelId'] = sys.argv[1].split('/')[-1]
	data['part'] = 'snippet'
	data['key'] = 	'AIzaSyAngcF6oKnyEbhk3KyL9Wz1OhSi28JjbzE'
	requestValues = urlparse.urlencode(data)
	request = "https://www.googleapis.com/youtube/v3/playlists?" + requestValues
	string = urlreq.urlopen(request).read().decode('utf-8')
	items = json.loads(string)['items']

	for item in items:
		playlistIds.append(item['id'])
		titles.append(item['snippet']['title'])

def download():
	for ids,title in zip(playlistIds,titles):
			url = "https://www.youtube.com/playlist?list=" + ids
			if not os.path.exists(title):
				os.makedirs(title)
			os.chdir("./" + title)
			url_down = "youtube-dl --no-check-certificate -o '%(title)s' " + url
			subprocess.call(url_down, shell=True)
			os.chdir("..")

getPlaylistId()
download()
