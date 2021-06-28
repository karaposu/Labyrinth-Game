from abc import ABCMeta, abstractmethod

from typing import List



class AbstractAction(metaclass=ABCMeta):
    @abstractmethod
    # def do(self, params: List[str], game: Game) -> ActionResult: pass
    def do(self, params, GameHandler) :
        pass