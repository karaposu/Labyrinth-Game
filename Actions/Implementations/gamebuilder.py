

from Actions.Services.Action import AbstractAction


from game_classes import*
#
# class  SetUpTheGame(AbstractAction):
class  SetUpTheGame(AbstractAction):

    def do(self, params, GameHandler) :
        # print("params: ",params)
        size = params
        GG= GameLogic(size=size)
        GameHandler.gamelogic=GG
        import traceback
        try:

            F, X =    GameHandler.gamelogic.gameBuilder()

        except TypeError:
            traceback.print_exc()

        GameHandler.GameOutput(X)

        return F, X









