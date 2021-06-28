import sys
import random
from abc import *
from enum import Enum


from impl.Game import GameHandler

from services.command import IUserCommand



'''
Starting a new game with a predefined labyrinth size: "start <labyrinth_size>". Labyrinth size should be not less 4 and not bigger 10.
Quiting the current game: "quit" (without saving).
Quiting the current game with saving: "save <file_name>" (the game should be saved into a text file).

Moving: "go up", "go down", "go left", "go right".
Skipping a turn: "skip".

first we need a  command line interface 
after this we need to implement the game class


'''

class StartCommand(IUserCommand):
    def __init__(self):
        self.id=10
    def get_command_tag(self):
        return "start"

    def get_args_count(self):
        return 1

    def evaluate(self, state, args,handler):
        msg=handler.Input(self,args)
        return (False, state, msg)


class QuitCommand(IUserCommand):
    def __init__(self):
        self.id=1
    def get_command_tag(self):
        return "quit"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args,handler):
        # agame.quit()
        return (True, state, "Quited.")


class SkipCommand(IUserCommand):
    def __init__(self):
        self.id = 9
    def get_command_tag(self):
        return "skip"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args,handler):


        msg=handler.Input(self, args)

        F = 0


        return (False, state, msg)


class MapCommand(IUserCommand):
    def __init__(self):
        self.id = 8
    def get_command_tag(self):
        return "skip"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args,handler):


        msg=handler.Input(self, args)

        F = 0

        return (False, state, msg)

class GoUpCommand(IUserCommand):
    def __init__(self):
        self.id = 0
    def get_command_tag(self):
        return "goup"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args,handler):

        msg=handler.Input(self,args)

        F=0

        return (False, state, msg)

class GoDownCommand(IUserCommand):
    def __init__(self):
        self.id = 2
    def get_command_tag(self):
        return "godown"


    def get_args_count(self):
        return 0

    def evaluate(self, state, args,handler):

        msg=handler.Input(self, args)

        F = 0
        return (False, state, msg)

class GoLeftCommand(IUserCommand):
    def __init__(self):
        self.id = 3
    def get_command_tag(self):
        return "goleft"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args,handler):
        msg=handler.Input(self, args)


        F = 0
        return (False, state, msg)


class GoRightCommand(IUserCommand):
    def __init__(self):
        self.id = 1
    def get_command_tag(self):
        return "goright"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args,handler):
        msg=handler.Input(self, args)

        F = 0
        return (False, state, msg)


class SaveCommand(IUserCommand):
    def __init__(self):
        self.id = 100
    def get_command_tag(self):
        return "save"

    def get_args_count(self):
        return 1

    def evaluate(self, state, args,handler):
        # print("asdf:",args)
        msg=handler.Input(self, args)


        return (False, state, msg)

class LoadCommand(IUserCommand):
    def __init__(self):
        self.id = 200
    def get_command_tag(self):
        return "Load"

    def get_args_count(self):
        return 1

    def evaluate(self, state, args,handler):
        msg=handler.Input(self,  args)

        return (False, state, msg)


class TaskCommand(IUserCommand):
    def __init__(self):
        self.id = 950

    def get_command_tag(self):
        return "task"

    def get_args_count(self):
        return 0

    def evaluate(self, state, args,handler):


        handler.Input(self, args)

        F = 0


        return (False, state, "skip")

