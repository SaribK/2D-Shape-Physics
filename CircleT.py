## @file CircleT.py
#  @author Sarib Kashif (kashis2)
#  @brief Contains the CircleT type which represents a circle
#  by inheriting the Shape interface
#  @date Feb 12 2021

from Shape import Shape


## @brief CircleT is a class that implements an ADT for the
#  shape of a circle
#  @details the ADT contains the central coordinates
#  of the circle as well as the mass and radius.
#  It is assumed that the arguments provided to the access
#  programs will be of the correct type.

class CircleT(Shape):

    ## @brief constructor method for CircleT
    #  @param x a real number for the x component of the centre of mass
    #  @param y a real number for the y component of the centre of mass
    #  @param r a real number for the radius
    #  @param m a real number for the mass
    #  @throws ValueError if both parameters r and m are not greater than 0
    def __init__(self, x, y, r, m):
        if not (r > 0 and m > 0):
            raise ValueError
        self.x = x
        self.y = y
        self.r = r
        self.m = m

    ## @brief get the x coordinate of the centre of mass
    #  @return a real number for the x component of the centre of mass
    def cm_x(self):
        return self.x

    ## @brief get the y coordinate of the centre of mass
    #  @return a real number for the y component of the centre of mass
    def cm_y(self):
        return self.y

    ## @brief get the mass of the circle
    #  @return a real number for the mass of the circle
    def mass(self):
        return self.m

    ## @brief get the moment of inertia of the circle
    #  @return a real number representing the moment of inertia of the current circle
    def m_inert(self):
        return (self.m * (self.r ** 2)) / 2
