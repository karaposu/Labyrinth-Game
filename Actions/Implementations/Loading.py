
from Actions.Implementations import Serialization
from Actions.Services.Action import AbstractAction
import jsonpickle # pip install jsonpickle
import json
import yaml # pip install pyyaml

# max_depth is optional


class  Load(AbstractAction):

    def do(self, params, GameHandler) :

        import traceback

        # print("b4 load:",GameHandler)
        # file = open(params+".json", "r")
        filename = str(params) + ".json"
        file = open(filename, "r")
        # print("file:",file)
        loaded_objects = jsonpickle.decode(file.read())

        print(type(loaded_objects))
        # data = pickle.load(file)
        GameHandler.gamelogic=loaded_objects
        print("after load:", GameHandler)
        print("after load loaded_objects:", loaded_objects)

        # loaded_objects.gamelogic.lab_obj.printMaze()
        loaded_objects.lab_obj.printMaze()



        # print("DDDD:",b)
        F=0
        MESSAGE="LOADED"

        GameHandler.GameOutput(MESSAGE)
        return F, MESSAGE