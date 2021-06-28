from abc import ABCMeta, abstractmethod

from typing import List
#
# here you should provide ILabyrinthSerializer interface with 2 methods serialize and deserialize.
# The serialize method should convert your game object into JSON format and save it to a file, and the
# deserialize method reads the file and converts JSON to your game object Labyrinth

class ILabyrinthSerializer(metaclass=ABCMeta):
    @abstractmethod
    # def do(self, params: List[str], game: Game) -> ActionResult: pass
    def Serialize(self, params) :
        pass
    def Deserialize(self, params) :
        pass