#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gitterpy.client import GitterClient
import json

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def regex_fix(msg):
    essence = ""
    if "I'd like to become a virtual intern" in msg:
        essence = "please follow the first steps found here:  https://treehouses.io/#!pages/vi/firststeps.md"
    if "review my pull request" in msg:
        essence = "Thank you for your contribution. Our team will review your pull request shortly. Cheers! :D"
    if "review my issue" in msg:
        essence = "Thank you for your input. We will take your issue into consideration as we sail the 7 seas! Ahoy!"
    if "I'm on step" in msg:
        essence = "Congratulations for completing a step! Good job! :)"
    if "I'd like to become a virtual intern" in msg:
        essence = "please follow the first steps found here: https://treehouses.io/#!pages/vi/firststeps.md"
    return essence

gitter_api_token='de7f501f5ff24069d7aa9ff36966e33b4875d596' # Gitter API token
gitter_room='treehouses/Lobby' # Gitter Room Name
gitter = GitterClient(gitter_api_token)
print("Entering main loop")
while True:
    try:
        response = gitter.stream.chat_messages(gitter_room)
        for stream_messages in response.iter_lines():
            stream_messages = stream_messages.decode('utf-8')
            if is_json(stream_messages):
                resp = json.loads(stream_messages)
                if 'msg' in globals():
                    if resp['text'] == msg:
                        continue
                if 'botresp' in globals():
                    if botresp == msg:
                        continue
                msg = resp['text']
                userid = resp['fromUser']['username']
                if userid == gitter.auth.get_my_id['name']:
                    continue
                botresp = regex_fix(msg)
                if botresp != "":
                    gitter.messages.send(gitter_room, "@" + userid + " " + botresp)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
