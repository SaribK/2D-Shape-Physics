## @file Shape.py
#  @author Sarib Kashif (kashis2)
#  @brief An interface for modules that implement shapes
#  @date Feb 12 2021

from abc import ABC, abstractmethod


## @brief Shape provides an interface for different shapes
## @details The methods in the interface are abstract and need to be
#  overridden by the modules that inherit this interface

class Shape(ABC):
    @abstractmethod
    ## @brief an abstract method for getting the centre mass x
    #  @return a real number representing the centre mass x coordinate
    def cm_x(self):
        pass

    @abstractmethod
    ## @brief an abstract method for getting the centre mass y
    #  @return a real number representing the centre mass y coordinate
    def cm_y(self):
        pass

    @abstractmethod
    ## @brief an abstract method for getting the mass
    #  @return a real number representing the mass
    def mass(self):
        pass

    @abstractmethod
    ## @brief an abstract method for getting the moment of inertia
    #  @return a real number representing the moment of inertia
    def m_inert(self):
        pass
