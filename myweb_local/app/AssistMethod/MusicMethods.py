#######################################
# MusicMethods 音乐类的增删改查操作    #
#######################################
import os
import json
import uuid

CURRENT_PATH = os.getcwd()

#######################################
# 音乐保存方式
# index.json 和 music 文件夹
# music文件夹 通过 uuid.文件类型 的形式保存
# index.json 文件格式
# {
#   ’music‘:{ # music 中不应该包括 有声小说 
#       uuid:{
#           'file_type': mp3，等，
#           'name': 歌名
#           ’author‘: 作者
#           ’words‘: 歌词
#       }
#   }
#   ’collections‘:{
#       歌集名:{
#           assort: 有声小说 or 歌曲
#           song_list: [ uuid ]
#       }
#   }
# }
#######################################

INDEX_FILE = 'app/static/source/music/index.json'

class Music:
    def __init__(self, uuid=None):
        if uuid is None:
            self.music = {'id': Music.create_uuid()}
        else:
            self.music = self.get_music_by_uuid(uuid)

    @staticmethod
    def create_uuid():
        try:
            with open(INDEX_FILE) as f:
                index_profiles = json.load(f)
                id_set = index_profiles['time']
        except:
            id_set = {}
        while True:
            # 如果生成的uuid存在就重新生成，直到不相同为止
            id = str(uuid.uuid4())
            if id not in id_set:
                return id

    def get_all_music(self):
        return

    def get_all_collection(self):
        return

    def get_collection_by_name(self, collection_name):
        return

    def save_music(self):
        return

    def delete_music(self):
        return

    def get_music_by_uuid(self, uuid):
        return
