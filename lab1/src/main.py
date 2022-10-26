import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

from function import FunctionF, FunctionG
from gradient_descent import GradientDescentSolver
from random import random



def tune_hyperparameters(step_sizes, iterations, epochs, function, delta):
    for step_size in step_sizes:
        solver = GradientDescentSolver(step_size, iterations, delta)
        minimums = []
        for _ in range(epochs):
            x0 = [(random() - 1/2) * 10 for _ in range(function.input_size)]
            answer, _ = solver.solve(function, x0)
           

            y_solution = function.calculateValueFor(answer)
            minimums.append(y_solution)

        print("step size: ", step_size)
        print("avg: ", np.average(minimums))
        print("std: ", np.std(minimums))
        print("minimum: ", np.min(minimums))
        print('\n')



def plot_function(function, start, end):
    X = np.arange(start, end, 0.1)
    Y = np.array([function.calculateValueFor([x]) for x in X])

    plt.plot(X, Y)
    plt.show()

def plot_3d(function, start, end):
    X = np.arange(start, end, 0.1)
    Y = np.arange(start, end, 0.1)
    Z = []
    for x in X:
        Z.append([function.calculateValueFor((x, y)) for y in Y])
    Z = np.array(Z)
    X, Y = np.meshgrid(X, Y)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
                        cmap=cm.RdBu,linewidth=0, antialiased=False)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)
    show()


sizes_f = [10**-6, 10**-4, 10**-2, 5 * 10**-1, 10**-1]
sizes_g = [10**-6, 10**-4, 10**-2, 10**-1, 1, 10]
# print("G")
# plot_3d(FunctionG(), -5, 5)
# tune_hyperparameters(sizes_g, 10_000, 100, FunctionG(), 0.0001)
plot_function(FunctionF(), -5, 5)
print("F")
tune_hyperparameters(sizes_f, 1_000, 1000, FunctionF(), 0.0001)
