from abc import ABC, abstractmethod
class Color(ABC):

    @property
    @abstractmethod
    def color(self):
        pass

    @color.setter
    @abstractmethod
    def color(self, value):
        pass
