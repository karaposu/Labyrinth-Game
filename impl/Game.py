
import json
from random import randrange
from typing import List
from game_classes import GameLogic

import colorama
from colorama import Fore, Back, Style
colorama.init()




from Actions.Implementations.gamebuilder import SetUpTheGame
from Actions.Implementations.MoveUP import MoveUp,MoveLeft,MoveRight,MoveDown,Skip,Map
from Actions.Implementations.Saving import Save
from Actions.Implementations.Loading import Load


# game class responsibilites  start the game  evaluate the actions
# gameinut ties command line and game
# start game  ties command line with game actions
# EvaluateAction interfaeres with object handler
# object handler deals with game objects.



class GameHandler(object):
    def __init__(self):

        self.is_finished = False
        self.is_started = False
        self.gamelogic = 0
        self.si=0
        self.si_to_load = 0
        # self.gamelogic = GameLogic()


    def Input(self, Command,Arg):

        self.Command=Command
        self.Arg=Arg

        # print("Command:",Command)
        # print("Arg:",Arg)

        # if isinstance(Command,StartCommand):
        if Command.id==10:
            gb=SetUpTheGame()
            self.Current_Action = gb


        elif Command.id==0:
            gb = MoveUp()
            self.Current_Action = gb

        elif Command.id == 1:
            gb = MoveRight()
            self.Current_Action = gb
        elif Command.id == 2:
            gb = MoveDown()
            self.Current_Action = gb

        elif Command.id == 3:
            gb = MoveLeft()
            self.Current_Action = gb

        elif Command.id == 9:
            gb = Skip()
            self.Current_Action = gb
        elif Command.id == 950:
            gb = Skip()
            self.Current_Action = gb

        elif Command.id == 8:
            gb = Map()
            self.Current_Action = gb
        elif Command.id == 100:
            gb = Save()
            self.Current_Action = gb
        elif Command.id == 200:
            gb = Load()
            self.Current_Action = gb

            # print("z1:", self.Current_Action.__dict__)

        else:
            print("error:")


        X= self.EvaluateAction(gb,Arg,Command.id)

        return X

    def EvaluateAction(self, Current_Action,Arg,id):
        print("------------------------------Inisde EvaluateAction :")


        a=self
        if self.is_finished == 0:
            F,X=self.Current_Action.do(Arg,a)
            self.current_message=X

            self.is_finished = F

            # if id==950:
            #     self.GameOutput("hello")

        else:
            self.GameOutput("Game Already Finished")


        return X



    def GameOutput(self, Message):



        print(Fore.RED)

        print("           ")
        print(Message)
        print("           ")

        print(Style.RESET_ALL)







