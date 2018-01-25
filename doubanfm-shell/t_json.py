import json
from pprint import pprint
with open("风格数据_json") as f:
    json_data = json.loads(f.read())

pprint(json_data)

class Channels(object):
    def __init__(self):
        self.artists = None    #艺术家
        self.brand = None      #品牌频道
        self.genre = None      #风格
        self.language = None   #语言
        self.scenario = None   #场景

class Channel(object):
    def __init__(self):
        self.title = None
        self.id = None
        self.related_channel = None

    def __repr__(self):
        return self.title

def channels_item(json_data):
    test_list = []
    json_data = json_data['data']['channels']
    print(json_data)
    artists = json_data['artist']
    brand = json_data['brand']
    genre = json_data['genre']
    language = json_data['language']
    scenario = json_data['scenario']
    for c in json_data:
        print(c)
        for channel in json_data[c]:
            print(channel)
            c = Channel()
            c.title = channel['name']
            c.id = channel['id']
            test_list.append(c)
    return test_list
a_list = channels_item(json_data)
print(a_list)
    # for a in artists:
    #     channel = Channel()
    #     channel.title = a['name']
    #     channel.id = a['id']
