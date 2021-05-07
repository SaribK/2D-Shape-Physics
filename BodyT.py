## @file BodyT.py
#  @author Sarib Kashif (kashis2)
#  @brief Contains the BodyT type which represents a
#  set of points that make up the body of a shape
#  @date Feb 12 2021

from Shape import Shape


## @brief BodyT is a class that implements an ADT for the
#  body of a shape
#  @details the ADT contains a set of central coordinates
#  for the body as well as a set of masses.
#  It is assumed that the arguments provided to the access
#  programs will be of the correct type.

class BodyT(Shape):

    ## @brief constructor method for BodyT
    #  @param x a set of real numbers for the x components of the centre of mass
    #  @param y a set of real numbers for the y components of the centre of mass
    #  @param m a set of real numbers for the masses
    #  @throws ValueError if the length of all parameters are not equal
    #  @throws ValueError if all masses in the set m are not greater than 0
    def __init__(self, x, y, m):
        if not (len(x) == len(y) == len(m)):
            raise ValueError
        for i in m:
            if not i > 0:
                raise ValueError
        self.cmx = self.__cm__(x, m)
        self.cmy = self.__cm__(y, m)
        self.m = sum(m)
        self.moment = self.__mmom__(x, y, m) - sum(m) * \
            (self.__cm__(x, m) ** 2 + self.__cm__(y, m) ** 2)

    ## @brief get the x component of the centre of mass
    #  @return a real number for the x component of the centre of mass
    def cm_x(self):
        return self.cmx

    ## @brief get the y component of the centre of mass
    #  @return a real number for the y component of the centre of mass
    def cm_y(self):
        return self.cmy

    ## @brief get the mass of the body
    #  @return a real number for the total mass of the body
    def mass(self):
        return self.m

    ## @brief get the moment of inertia of the body
    #  @return a real number representing the moment of inertia of the body
    def m_inert(self):
        return self.moment

    def __cm__(self, z, m):
        temp = 0
        for i in range(len(m)):
            temp += (z[i] * m[i])
        return temp / sum(m)

    def __mmom__(self, x, y, m):
        temp = 0
        for i in range(len(m)):
            temp += (m[i] * (x[i] ** 2 + y[i] ** 2))
        return temp
