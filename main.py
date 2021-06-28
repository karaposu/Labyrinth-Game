import sys
import random
from abc import *
from enum import Enum

from services.command import *

from impl.commands import *
from impl.Game import *

# we need command interface which will turn commands and args to  fundtions
# we need  Game Hnadler interface , takes input for the game and prints output for the game and evaluate game actions
#

# we write a command start
#  start goes through command interface and triggers StartCommand function
# Startcommand function goes to gamehandler input
# gamehandler input checks the command and triggers the related action function gamebuilder
# gamebuilder builds the game.


# lets first  make our "input interface" ready. Job of this interface is this : no matter what it is we will need some inputs.
'''

'''


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

if __name__ == "__main__":
    print("Labyrinth Starts")
    print("supported_commands:",supported_commands.keys())
    finished = False
    state = ""
    message = ""
    args = []
    cmd = None
    try:
        while not(finished):
            user_input = input("$> ")

            cmd, args, message = parse_user_input(user_input)

            print( "cmd:",cmd,"args:",args, "message:", message )

            if cmd == None:
                print(message)
                continue

            if not args:
                args=args
            else:
                args=args[0]

            (finished, state, message) = eval_command(cmd, args,gamehandler, state)

            print("-------------------------finished:", finished, "state:", state, "message:", message)
            # print("New state: " + str(state))
            # if obj is not None:
            # if message != "": print(message)
    except:
        print("Unexpected error:", sys.exc_info()[0])





