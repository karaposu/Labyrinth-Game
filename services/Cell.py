import sys
import random
from abc import *
from enum import Enum


class cell(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self, id ,coordinates,designator):
        pass

    def CoordinateUpdate(self,c):
        pass