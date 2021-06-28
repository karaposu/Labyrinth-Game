from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import url_for
import jinja2



app = Flask(__name__)



# ---------------------------------------------------------------------------------------------------

import sys
import random
from abc import *
from enum import Enum

from services.command import *

from impl.commands import *
from impl.Game import *

def make_commands_dict(cmd_lst):
    cmd_dict = dict()
    for cmd in cmd_lst:
        cmd_dict[cmd.get_command_tag().lower().strip()] = cmd
    return cmd_dict

supported_commands = make_commands_dict(
    [ StartCommand()

    , GoUpCommand()
    , GoDownCommand()
    , GoLeftCommand()
    , GoRightCommand()
    , SkipCommand()
    , SaveCommand()
    , MapCommand()
    , LoadCommand()
    , TaskCommand()

    ])




def parse_user_input(user_input):
    # print("parse_user_input input",user_input)
    # print("////////////////:")
    tokens = user_input.strip().split(" ")
    print("tokens ", tokens)

    if len(tokens) == 0:
        return (None, None, "no token")


    norm_cmd = tokens[0].lower()

    if norm_cmd in supported_commands:
        cmd = supported_commands[norm_cmd]
        # print("tokens[1:10] ", tokens[1:10])
        # print("tokens[0:10] ", tokens[0:10])
        # print("cmd ", cmd)
        return (cmd, tokens[1:10], "")

    return (None, None, "Command not supported: ")



def eval_command(cmd : IUserCommand, args, handler,st):
    # if cmd.get_args_count() != len(args):
    #     return (False, st, "Invalid number of args. Expected: "
    #         + str(cmd.get_args_count()) + ", " + "got: " + str(len(args)))
    return cmd.evaluate(st, args,handler)

global gamehandler
gamehandler=GameHandler()


import uuid


global current_session_id
current_session_id=None


def make_clickable(url, name):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(url,name)



app.config["APPLICATION_ROOT"] = "/start"


class SessionID():
    def __init__(self):
        sessionid = uuid.uuid1()

        self.sessionid=  str(sessionid)



@app.route('/', methods=['GET'])
def initialize():
    return render_template('base.html' )


@app.route('/start', methods=['GET'])
def start():

    sessionid_object= SessionID()
    global current_session_id
    current_session_id=sessionid_object.sessionid
    sessionid=current_session_id
    # sessionid = uuid.uuid1()

    print("curren_session_id",current_session_id)



    BASE = " http://127.0.0.1:5000/"
    uplink= BASE+"up/"+str(sessionid)
    downlink= BASE+"down/"+str(sessionid)
    rightlink= BASE+"right/"+str(sessionid)
    leftlink= BASE+"left/"+str(sessionid)
    skiplink= BASE+"skip/"+str(sessionid)
    maplink = BASE + "get_maze_state_json/" + str(sessionid)
    savelink= BASE+"save/"+str(sessionid)

    gamehandler.si=sessionid

    (finished, state, message) = eval_command(StartCommand(), "5", gamehandler, False)

    return render_template('init.html', t_sessionid= sessionid,  t_message= message ,t_up=uplink ,t_down=downlink, t_right=rightlink ,t_left=leftlink ,t_skip=skiplink ,t_map=maplink  ,t_save=savelink)




@app.route('/up/<string:sessionid>', methods=['GET'])
def up(sessionid):

    print("(inside up)current_session_id", current_session_id)
    print("session_id", sessionid)

    if sessionid==current_session_id:

        print("current_session_id", current_session_id)
        print("session_id", sessionid)
        # if current_session_id == sessionid:

        (finished, state, message) = eval_command(GoUpCommand(), None, gamehandler, False)

        BASE = " http://127.0.0.1:5000/"
        uplink = BASE + "up/" + str(sessionid)
        downlink = BASE + "down/" + str(sessionid)
        rightlink = BASE + "right/" + str(sessionid)
        leftlink = BASE + "left/" + str(sessionid)
        skiplink = BASE + "skip/" + str(sessionid)
        maplink = BASE + "get_maze_state_json/" + str(sessionid)
        savelink = BASE + "save/" + str(sessionid)
        return render_template('init.html', t_sessionid=sessionid, t_message=message, t_up=uplink, t_down=downlink,
                               t_right=rightlink, t_left=leftlink, t_skip=skiplink, t_map=maplink, t_save=savelink)
    else:
        return {" error messgae": "Wrong sessionid"}


@app.route('/down/<string:sessionid>', methods=['GET'])
def down(sessionid):
    if sessionid == current_session_id:


        (finished, state, message) = eval_command(GoDownCommand(), None, gamehandler, False)
        BASE = " http://127.0.0.1:5000/"
        uplink = BASE + "up/" + str(sessionid)
        downlink = BASE + "down/" + str(sessionid)
        rightlink = BASE + "right/" + str(sessionid)
        leftlink = BASE + "left/" + str(sessionid)
        skiplink = BASE + "skip/" + str(sessionid)
        maplink = BASE + "get_maze_state_json/" + str(sessionid)
        savelink = BASE + "save/" + str(sessionid)
        return render_template('init.html', t_sessionid=sessionid, t_message=message, t_up=uplink, t_down=downlink,
                               t_right=rightlink, t_left=leftlink, t_skip=skiplink, t_map=maplink, t_save=savelink)
    else:
        return {" error messgae": "Wrong sessionid"}

@app.route('/left/<string:sessionid>', methods=['GET'])
def left(sessionid):

    if sessionid == current_session_id:

        (finished, state, message) = eval_command(GoLeftCommand(), None, gamehandler, False)
        BASE = " http://127.0.0.1:5000/"
        uplink = BASE + "up/" + str(sessionid)
        downlink = BASE + "down/" + str(sessionid)
        rightlink = BASE + "right/" + str(sessionid)
        leftlink = BASE + "left/" + str(sessionid)
        skiplink = BASE + "skip/" + str(sessionid)
        maplink = BASE + "get_maze_state_json/" + str(sessionid)
        savelink = BASE + "save/" + str(sessionid)
        return render_template('init.html', t_sessionid=sessionid, t_message=message, t_up=uplink, t_down=downlink,
                               t_right=rightlink, t_left=leftlink, t_skip=skiplink, t_map=maplink, t_save=savelink)

    else:
        return {" error messgae": "Wrong sessionid"}

@app.route('/right/<string:sessionid>', methods=['GET'])
def right(sessionid):

    if sessionid == current_session_id:

        (finished, state, message) = eval_command(GoRightCommand(), None, gamehandler, False)
        BASE = " http://127.0.0.1:5000/"
        uplink = BASE + "up/" + str(sessionid)
        downlink = BASE + "down/" + str(sessionid)
        rightlink = BASE + "right/" + str(sessionid)
        leftlink = BASE + "left/" + str(sessionid)
        skiplink = BASE + "skip/" + str(sessionid)
        maplink = BASE + "get_maze_state_json/" + str(sessionid)
        savelink = BASE + "save/" + str(sessionid)
        return render_template('init.html', t_sessionid=sessionid, t_message=message, t_up=uplink, t_down=downlink,
                               t_right=rightlink, t_left=leftlink, t_skip=skiplink, t_map=maplink, t_save=savelink)
    else:
        return {" error messgae": "Wrong sessionid"}


@app.route('/skip/<string:sessionid>', methods=['GET'])
def skip(sessionid):

    if sessionid == current_session_id:

        (finished, state, message) = eval_command(SkipCommand(), None, gamehandler, False)
        BASE = " http://127.0.0.1:5000/"
        uplink = BASE + "up/" + str(sessionid)
        downlink = BASE + "down/" + str(sessionid)
        rightlink = BASE + "right/" + str(sessionid)
        leftlink = BASE + "left/" + str(sessionid)
        skiplink = BASE + "skip/" + str(sessionid)
        maplink = BASE + "get_maze_state_json/" + str(sessionid)
        savelink = BASE + "save/" + str(sessionid)
        return render_template('init.html', t_sessionid=sessionid, t_message=message, t_up=uplink, t_down=downlink,
                               t_right=rightlink, t_left=leftlink, t_skip=skiplink, t_map=maplink, t_save=savelink)
    else:
        return {" error messgae": "Wrong sessionid"}


@app.route('/save/<string:sessionid>', methods=['GET'])
def save(sessionid):

    if sessionid == current_session_id:

        (finished, state, message) = eval_command(SaveCommand(), sessionid, gamehandler, False)
        BASE = " http://127.0.0.1:5000/"
        uplink = BASE + "up/" + str(sessionid)
        downlink = BASE + "down/" + str(sessionid)
        rightlink = BASE + "right/" + str(sessionid)
        leftlink = BASE + "left/" + str(sessionid)
        skiplink = BASE + "skip/" + str(sessionid)
        maplink = BASE + "get_maze_state_json/" + str(sessionid)
        savelink = BASE + "save/" + str(sessionid)
        return render_template('init.html', t_sessionid=sessionid, t_message=message, t_up=uplink, t_down=downlink,
                               t_right=rightlink, t_left=leftlink, t_skip=skiplink, t_map=maplink, t_save=savelink)
    else:
        return {" error messgae": "Wrong sessionid"}

@app.route('/load/<string:sessionid>', methods=['GET'])
def load(sessionid):
    gamehandler.si_to_load = sessionid
    # print("current_session_id", current_session_id)
    print("session_id_to_load", sessionid)
    # if current_session_id == sessionid:

    (finished, state, message) = eval_command(LoadCommand(), sessionid, gamehandler, False)
    global current_session_id
    current_session_id=sessionid
    BASE = " http://127.0.0.1:5000/"
    uplink = BASE + "up/" + str(sessionid)
    downlink = BASE + "down/" + str(sessionid)
    rightlink = BASE + "right/" + str(sessionid)
    leftlink = BASE + "left/" + str(sessionid)
    skiplink = BASE + "skip/" + str(sessionid)
    maplink = BASE + "get_maze_state_json/" + str(sessionid)
    savelink = BASE + "save/" + str(sessionid)
    return render_template('init.html', t_sessionid=sessionid, t_message=message, t_up=uplink, t_down=downlink,
                           t_right=rightlink, t_left=leftlink, t_skip=skiplink, t_map=maplink, t_save=savelink)





@app.route('/get_maze_state_json/<string:sessionid>', methods=['GET'])
def get_maze_state_json(sessionid):

    if sessionid == current_session_id:

        (finished, state, message) = eval_command(MapCommand(), None, gamehandler, False)
        BASE = " http://127.0.0.1:5000/"
        uplink = BASE + "up/" + str(sessionid)
        downlink = BASE + "down/" + str(sessionid)
        rightlink = BASE + "right/" + str(sessionid)
        leftlink = BASE + "left/" + str(sessionid)
        skiplink = BASE + "skip/" + str(sessionid)
        maplink = BASE + "get_maze_state_json/" + str(sessionid)
        savelink = BASE + "save/" + str(sessionid)
        return render_template('init.html', t_sessionid=sessionid, t_message=message, t_up=uplink, t_down=downlink,
                               t_right=rightlink, t_left=leftlink, t_skip=skiplink, t_map=maplink, t_save=savelink)

    else:
        return {" error messgae": "Wrong sessionid"}







if __name__ == "__main__":
    app.run(debug=True)