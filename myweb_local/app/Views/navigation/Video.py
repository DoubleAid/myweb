from flask import Blueprint,render_template
import os

video = Blueprint('video',__name__)

total_video_interface = "video/total_video_interface.html"
video_player_interface = "video/video_player_interface.html"
video_collection_interface = "video/video_collection_interface"

@video.route('/')
def show_music_interface():
    return render_template(total_video_interface)
