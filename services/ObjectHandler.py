import sys
import random
from abc import *
from enum import Enum

# from services.knowledge_base.knowledge_base import IKnowledgeBase

class ObjectHandler():
    @abstractmethod
    def place(self): pass

    @abstractmethod
    def activate(self): pass

    def deactivate(self): pass


