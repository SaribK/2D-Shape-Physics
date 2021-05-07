## @file Plot.py
#  @author Sarib Kashif (kashis2)
#  @brief Contains the plot function to plot
#  the behaviour of a shape over time
#  @date Feb 12 2021
#  @details using an environment variable, win,
#  to manipulate the screen to show graphs

import matplotlib.pyplot as plt


## @brief plots the accelaration, velocity and distance
#  of a shape
#  @param w a sequence of sequences
#  @param t a sequence of the time stamps
#  @throws ValueError if the length of w and t are not equal
def plot(w, t):
    if len(w) != len(t):
        raise ValueError
    x = []
    y = []
    for i in range(len(w)):
        x += [w[i][0]]
        y += [w[i][1]]
    fig, axs = plt.subplots(3)
    fig.suptitle('Motion Simulation')
    axs[0].plot(t, x)
    axs[1].plot(t, y)
    axs[2].plot(x, y)

    axs.flat[0].set(xlabel='t (m)', ylabel='x (m)')
    axs.flat[1].set(xlabel='t (m)', ylabel='y (m)')
    axs.flat[2].set(xlabel='x (m)', ylabel='y (m)')

    plt.subplots_adjust(hspace=0.5)

    plt.show()
