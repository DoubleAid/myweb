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

class Music:
    def __init__(self, uuid):
        if uuid is None:
            self.music = {id:self.create_uuid()}
        return

    @staticmethod
    def create_uuid(self):
        return

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

    def get_music_by_uuid(self):
        return
