#######################################
# MusicMethods 音乐类的增删改查操作    #
#######################################
import os
import json
import uuid

CURRENT_PATH = os.getcwd()

#######################################
# 音乐保存方式
# index.json 和 audio 文件夹
# --------------- audio文件夹 ---------------
# audio 文件夹 包括 多个文件夹
# 其中包括 audio 文件夹 和 若干 小说文件夹
# music文件夹  通过 uuid.文件类型 的形式保存
# --------------- index.json 文件格式 ---------------
# {
# }
#######################################

# web 页面位置
INDEX_FILE = 'app/static/source/audio/index.json'
SOURCE_FILE = 'app/static/source/audio/'
# 测试时文件位置
# INDEX_FILE = '../static/source/audio/index.json'
# SOURCE_FILE = '../static/source/audio'


class Video:
    def __init__(self, uuid=None, seq=-1):
        """
        :param uuid: 判断seq是不是 0， 当 seq=-1 时，表示 uuid 为 audio 中的某个歌曲
                                     当 seq>=9 时， 表示 uuid 为 某个小说，seq为 audio_list 中的序列
                                     当 uuid = None，表示 新建audio对象
        :param seq: 序列 当seq=0时，表示 seq 没有赋值， 当 seq > 0 时，表示有特殊集数，说明uuid为一个小说
        :type seq: int
        """
        if uuid is None:
            self.audio = {'id': Video.create_uuid()}
        elif seq == -1:
            self.audio = self.get_music_by_uuid(uuid)
        else:
            self.audio = self.get_novel_by_seq(uuid, seq)

    @staticmethod
    def create_uuid():
        # noinspection PyBroadException
        try:
            with open(INDEX_FILE) as f:
                index_profile = json.load(f)
            id_set = [ i for i in index_profile['audio']]
            id_set.extend([i for i in index_profile['sets']])
        except BaseException as e:
            id_set = {}
        while True:
            # 如果生成的uuid存在就重新生成，直到不相同为止
            new_id = str(uuid.uuid4())
            if new_id not in id_set:
                return new_id

    @staticmethod
    def get_all_music():
        # noinspection PyBroadException
        try:
            with open(INDEX_FILE) as f:
                index_profile = json.load(f)
            id_set = [ i for i in index_profile['audio']]
        except:
            id_set = {}
        finally:
            return id_set

    @staticmethod
    def get_all_collection():
        # noinspection PyBroadException
        try:
            with open(INDEX_FILE) as f:
                index_profile = json.load(f)
                uuid_set = [ i for i in index_profile['novel']]
        except:
            uuid_set = []
        finally:
            return uuid_set

    def get_collection_by_name(self, collection_name):
        return

    def save_music(self):
        return

    def delete_music(self):
        return

    def get_music_by_uuid(self, uuid):
        try:
            with open(INDEX_FILE) as f:
                index_profile = json.load(f)
            uuid_set = [i for i in index_profile['audio']]
        except:
            return False
        return

    def get_novel_bu_seq(self, uuid, seq):
        return
