from abc import ABC, abstractmethod

class Figure(ABC):

    # @property
    # @abstractmethod
    # def number_of_sides(self):
    #     pass

    # @property
    # @abstractmethod
    # def number_of_angles(self):
    #     pass

    # @number_of_sides.setter
    # def number_of_sides(self, value):
    #     #self._number_of_sides = value
    #     pass

    # @number_of_angles.setter
    # def number_of_angles(self, value):
    #     #self._number_of_angles = value
    #     pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass
