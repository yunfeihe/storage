import requests, json
from pprint import pprint

def get_playlist_from_url(url):
    playlist = []
    #playlist_of_json = requests.get(url).text

    with open('test_json', 'r') as f:
        playlist_of_json = f.read()
        f.close()
    #test method

    loads_json = json.loads(playlist_of_json)
    print(playlist_of_json)
    for song in loads_json['song']:
        s = Song()
        s.title = song['title']
        s.artist = song['artist']
        s.song_url = song['url']
        playlist.append(s)
    return playlist

def get_channels_list():
    channels_list = []
    with open("风格数据_json") as f:
        channels_of_json = f.read()
        f.close()
    loads_json = json.loads(channels_of_json)

    return channels_list
#重构代码
# def playlist_item(a_list, ):
#     for song in loads_json['song']:
#         s = Song()
#         s.title = song['title']
#         s.artist = song['artist']
#         s.song_url = song['url']
#         a_list.append(s)
#
# def get_list_from_json_data_by_item(json_data, item):
#     item_list = []
#     json_data = json.loads(json_data)
#     item()
#     return item_list



class Song(object):
    def __init__(self):
        self.title = None
        self.artist = None
        self.song_url = None
        #self.album_url = albun_url
        #self.album_picture_url = album_picture_url
        # self.region = region
    def __repr__(self):
        return 'music:{0}'.format(self.title)


url = "https://douban.fm/j/v2/playlist?channel=11445&kbps=128&client=s%3Amainsite%7Cy%3A3.0&app_name=radio_website&version=100&type=s&sid=1930084&pt=&pb=128&apikey="
p = get_playlist_from_url(url)
print(p)
