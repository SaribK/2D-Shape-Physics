## @file TriangleT.py
#  @author Sarib Kashif (kashis2)
#  @brief Contains the TriangleT type which represents a
#  triangle by inheriting the Shape interface
#  @date Feb 12 2021

from Shape import Shape


## @brief TriangleT is a class that implements an ADT for the
#  shape of a triangle
#  @details the ADT contains the central coordinates
#  of the triangle as well as the mass and sides.
#  It is assumed that the arguments provided to the access
#  programs will be of the correct type.

class TriangleT(Shape):

    ## @brief constructor method for TriangleT
    #  @param x a real number for the x component of the centre of mass
    #  @param y a real number for the y component of the centre of mass
    #  @param s a real number for the sides of the triangle (equilateral triangle)
    #  @param m a real number for the mass
    #  @throws ValueError if both parameters s and m are not greater than 0
    def __init__(self, x, y, s, m):
        if not (s > 0 and m > 0):
            raise ValueError
        self.x = x
        self.y = y
        self.s = s
        self.m = m

    ## @brief get the x coordinate of the centre of mass
    #  @return a real number for the x component of the centre of mass
    def cm_x(self):
        return self.x

    ## @brief get the y coordinate of the centre of mass
    #  @return a real number for the y component of the centre of mass
    def cm_y(self):
        return self.y

    ## @brief get the mass of the triangle
    #  @return a real number for the mass of the triangle
    def mass(self):
        return self.m

    ## @brief get the moment of inertia of the triangle
    #  @return a real number representing the moment of inertia of the current triangle
    def m_inert(self):
        return (self.m * (self.s ** 2)) / 12
