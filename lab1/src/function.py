from abc import ABC, abstractmethod
import math


class Function(ABC):
    """A function solved by gradient descent"""

    def __init__(self, input_size) -> None:
        super().__init__()
        self.input_size = input_size

    @abstractmethod
    def calculateValueFor(self, input):
        assert(len(input) == self.input_size)
    
    @abstractmethod
    def calculateDerivativesFor(self, input):
        assert(len(input) == self.input_size)

class FunctionF(Function):
    """A function solved by gradient descent"""

    def __init__(self) -> None:
        super().__init__(1)

    def calculateValueFor(self, input):
        super().calculateValueFor(input)
        x = input[0]
        return (x ** 4) / 4
        
    def calculateDerivativesFor(self, input):
        super().calculateDerivativesFor(input)
        x = input[0]
        return (x ** 3,)


class FunctionG(Function):
    """A function solved by gradient descent"""

    def __init__(self) -> None:
        super().__init__(2)

    def calculateValueFor(self, input):
        super().calculateValueFor(input)
        x1, x2 = input
        return 2 - math.exp(-x1 ** 2 - x2 ** 2) - 0.5 * math.exp(-(x1 + 1.5) ** 2 - (x2 - 2) ** 2)
        
    def calculateDerivativesFor(self, input):
        super().calculateDerivativesFor(input)
        x1, x2 = input
        return (
            2 * x1 * math.exp(-x1 ** 2 - x2 ** 2) + (x1 + 1.5) * math.exp(-(x1 + 1.5) ** 2 - (x2 - 2) ** 2),
            2 * x2 * math.exp(-x1 ** 2 - x2 ** 2) + (x2 - 2) * math.exp(-(x1 + 1.5) ** 2 - (x2 - 2) ** 2)
        )