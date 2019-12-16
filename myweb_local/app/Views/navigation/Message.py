from flask import Blueprint
import os

CURRENT_PATH = os.getcwd()
message = Blueprint('message',__name__)

@message.route('/')
def show_message_interface():
    return None
