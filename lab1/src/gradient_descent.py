import numpy as np
from solver import Solver
from function import Function

class GradientDescentSolver(Solver):
    def __init__(self, step, iterations, minimal_delta) -> None:
        super().__init__()
        self.step = step
        self.iterations = iterations
        self.minimal_delta = minimal_delta

    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        return {"step" : self.step, "iterations" : self.iterations, "minimal_delta" : self.minimal_delta}

    def solve(self, problem: Function, x0):
        """
        A method that solves the given problem for given initial solution.
        It may accept or require additional parameters.
        Returns the solution and may return additional info.
        """
        X = [x0]
        for _ in range(self.iterations):
            input_to_derivative = zip(X[-1], problem.calculateDerivativesFor(X[-1]))
            new_x = (x_i - self.step * derivative_i for x_i, derivative_i in input_to_derivative)

            X.append(list(map(lambda x: np.round(x, 10), new_x)))
            if abs(sum(pair[1]**2 for pair in input_to_derivative))**1/2 < self.minimal_delta:
                break
        return X[-1], X
 