SyncYoutube
============

SyncYoutube is a python script used to sync a youtube channel to your local i.e it downloads videos from all playlist of that channel to your local directory. YouTube's api has been used to fetch the required data.

SyncYoutube will create separate folders for separate playlists so you don't have all the videos mixed up. Be it your favourite music channel, game tutorials or movie reviews, you can have everything offline. 

### Install Instructions
Run the following commands in your terminal

`git clone https://github.com/CodeMaxx/SyncYoutube.git`

Copy the `SyncYoutube.py` file to the directory you want to sync to the youtube channel.

Create a Youtube API key using your google account. The method is fairly simple. See the instructions given [here](http://help.dimsemenov.com/kb/wordpress-royalslider-tutorials/wp-how-to-get-youtube-api-key).

Now copy this key in the `SyncYoutube.py` file in the appropriate place(You can see it commented in the code) and save it. You're ready to rock!

##### Dependencies
* **youtube-dl** - a script to download youtube videos

Install instructions for **youtube-dl** -> [Install youtube-dl](https://github.com/rg3/youtube-dl#user-content-installation)

### Usage
`python SyncYoutube.py <link to the youtube channel>`

For e.g.:<br>
`python SyncYoutube.py https://www.youtube.com/channel/UCyp1gCHZJU_fGWFf2rtMkCg`

## Credits
[Akash Trehan](https://github.com/CodeMaxx)

[Deepesh Singh](https://github.com/deepesh00)

[Kumar Ayush](https://github.com/cheekujodhpur) - *For the idea and mentoring*
