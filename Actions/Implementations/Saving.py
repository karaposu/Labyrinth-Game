
from Actions.Implementations import Serialization
from Actions.Services.Action import AbstractAction
import jsonpickle # pip install jsonpickle
import json
import yaml # pip install pyyaml

# max_depth is optional


class  Save(AbstractAction):

    def do(self, params, GameHandler) :

        import traceback
        try:

            serialized = jsonpickle.encode(GameHandler.gamelogic, max_depth=7)


            # with open("save.json", "w") as text_file:
            # params="fileee"
            filename=str(params)+".json"

            with open(filename, "w") as text_file:
                K=print(serialized, file=text_file)

            # file = open("save.json", "r")
            # loaded_objects = jsonpickle.decode(file.read())

        except: TypeError
        traceback.print_exc()


        # print("DDDD:",b)
        F=0
        MESSAGE="SAVED"

        GameHandler.GameOutput(MESSAGE)
        return F, MESSAGE