from flask import Blueprint,render_template,url_for,request,redirect, Response
from flask_login import current_user
import os

audio = Blueprint('audio',__name__)

total_music_interface = "audio/total_music_interface.html"
music_player_interface = "audio/music_player_interface.html"
music_collection_interface = "audio/music_collection_interface.html"


@audio.route('/')
def show_music_interface():
    return render_template(total_music_interface)


@audio.route('collection/<path:collection_name>')
def show_music_collection_interface(collection_name):
    print(collection_name)
    if collection_name == "test_detail":
        return render_template(music_player_interface)
    return collection_name
