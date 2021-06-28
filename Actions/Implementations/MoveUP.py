from Actions.Services.Action import AbstractAction


from game_classes import*
#
# class  SetUpTheGame(AbstractAction):
class  MoveUp(AbstractAction):

    def do(self, params, GameHandler) :



        F,MESSAGE=GameHandler.gamelogic.MoveTheObject(0,1)
        GameHandler.gamelogic.BearMoveTheObject(2, 15)
        GameHandler.GameOutput(MESSAGE)
        return F, MESSAGE



class MoveDown(AbstractAction):

    def do(self, params, GameHandler):

        F,MESSAGE=GameHandler.gamelogic.MoveTheObject(2, 1)
        GameHandler.gamelogic.BearMoveTheObject(2, 15)
        GameHandler.GameOutput(MESSAGE)
        return F, MESSAGE


class MoveLeft(AbstractAction):

    def do(self, params, GameHandler):

        F,MESSAGE=GameHandler.gamelogic.MoveTheObject(3, 1)
        GameHandler.gamelogic.BearMoveTheObject(2, 15)
        GameHandler.GameOutput(MESSAGE)
        return F, MESSAGE


class MoveRight(AbstractAction):

    def do(self, params, GameHandler):
        F,MESSAGE=GameHandler.gamelogic.MoveTheObject(1, 1)
        GameHandler.gamelogic.BearMoveTheObject(2, 15)
        GameHandler.GameOutput(MESSAGE)
        return  F,MESSAGE

class Skip(AbstractAction):

    def do(self, params, GameHandler):
        F,MESSAGE=GameHandler.gamelogic.MoveTheObject(9, 1)
        GameHandler.gamelogic.BearMoveTheObject(2, 15)
        GameHandler.GameOutput(MESSAGE)
        return F, MESSAGE

class Map(AbstractAction):

    def do(self, params, GameHandler):
        F,MESSAGE=GameHandler.gamelogic.MoveTheObject(9, 1)
        GameHandler.gamelogic.BearMoveTheObject(2, 15)
        lab=GameHandler.gamelogic.lab_obj.maze

        GameHandler.GameOutput(MESSAGE)
        return F, lab


class Quit(AbstractAction):

    def do(self, params, GameHandler):
        F,MESSAGE=1,"Quitted game"
        GameHandler.GameOutput(MESSAGE)
        return F, MESSAGE


