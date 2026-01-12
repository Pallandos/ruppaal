from abc import ABC, abstractmethod

class LanguageSemantics(ABC):

    @abstractmethod
    def initials(self):
        pass

    @abstractmethod
    def actions(self, state):
        pass    

    @abstractmethod
    def execute(self, state, action):
        pass

