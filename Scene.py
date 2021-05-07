## @file Scene.py
#  @author Sarib Kashif (kashis2)
#  @brief Contains the Scene class to create
#  a simulation of a shape moving
#  @date Feb 12 2021
#  @details Uses provided functions that decide
#  how the shape will behave

from scipy import integrate


## @brief Scene is a class that implements an ADT to display
#  how a shape behaves
#  @details the ADT contains functions Fx and Fy
#  which determine how a shape would behave

class Scene:

    ## @brief constructor method for Scene
    #  @param s a shape object for which a simulation is made
    #  @param Fx a function for the force in the x direction
    #  @param Fy a function for the force in the y direction
    #  @param vx a real number that represents the initial velocity in the x direction
    #  @param vy a real number that represents the initial velocity in the y direction
    def __init__(self, s, Fx, Fy, vx, vy):
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.vx = vx
        self.vy = vy

    ## @brief get the shape that the Scene is using
    #  @return a shape object
    def get_shape(self):
        return self.s

    ## @brief get the forces of both directions
    #  @return a tuple containing the forces in the x and y directions
    def get_unbal_forces(self):
        return self.Fx, self.Fy

    ## @brief get the initial velocity
    #  @return a tuple containing the velocities in the x and y directions
    def get_init_velo(self):
        return self.vx, self.vy

    ## @brief set the shape that scene is using to the provided shape
    #  @param s a shape object
    def set_shape(self, s):
        self.s = s

    ## @brief set the forces to the provided ones
    #  @param Fx a function for the force in the x direction
    #  @param Fy a function for the force in the y direction
    def set_unbal_forces(self, Fx, Fy):
        self.Fx, self.Fy = Fx, Fy

    ## @brief set the initial velocities to the provided ones
    #  @param vx a real number that represents the initial velocity in the x direction
    #  @param vy a real number that represents the initial velocity in the y direction
    def set_init_velo(self, vx, vy):
        self.vx, self.vy = vx, vy

    ## @brief set the initial velocities to the provided ones
    #  @param t_final a real number that represents the final time
    #  @param nsteps a real number for the number of steps in the simulation
    #  @return a tuple containing the time and position data for chosen object's scene
    def sim(self, t_final, nsteps):
        t = []
        for i in range(nsteps):
            temp = (i * t_final) / (nsteps - 1)
            t += [temp]
        x = integrate.odeint(self.__ode__,
                             [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t)
        return t, x

    def __ode__(self, w, t):
        x = self.Fx(t) / self.s.mass()
        y = self.Fy(t) / self.s.mass()
        return [w[2], w[3], x, y]
