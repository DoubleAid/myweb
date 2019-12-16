from flask import Blueprint,render_template,url_for,request,redirect, Response
from flask_login import current_user
import os

music = Blueprint('music',__name__)

total_music_interface = "music/total_music_interface.html"
music_player_interface = "music/music_player_interface.html"
music_collection_interface = "music/music_collection_interface.html"

@music.route('/')
def show_music_interface():
    return render_template(total_music_interface)
