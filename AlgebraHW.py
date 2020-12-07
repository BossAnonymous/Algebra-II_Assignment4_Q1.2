""" Finds elements <one> and <two> in Z[sqrt(-3)] which do not divide <test>
    (defaulted to the irreducible element we found, 1+sqrt(-3)) but for which
    <one>*<two> does divide <test>.
"""
import numpy as np


def TestDivisible(divisor: complex, quotient: complex, eps: float=1e-12) -> bool:
    """ [DEPRECATED] Is <quotient> divisible by <divisor> in Z[sqrt(-3)]? """
    division: complex = quotient/divisor
    realInt: bool = abs(division.real - division.real//1) < eps
    imagInt: bool = abs(division.imag/s3 - (division.imag/s3)//1) < eps
    return realInt and imagInt


def TestInGaussIntRoot3(number: complex, eps: float=1e-12) -> bool:
    """ Is <number> in Z[sqrt(-3)]? """
    realTest: bool = abs(number.real - number.real//1) < eps
    imagTest: bool = abs(number.imag/s3 - (number.imag/s3)//1) < eps
    return realTest and imagTest


class GaussIntRoot3:
    """ A class to represent numbers in the set Z[sqrt(-3)] """

    def __init__(self, a: int, b: int) -> None:
        """ Initialises the number in Z[sqrt(-3)] with value a+b*sqrt(-3) """
        self.a = a
        self.b = b

    def __mul__(self, other):
        """ Multiply two values in the set together """
        newReal = self.a*other.a - 3*self.b*other.b
        newImag = self.b*other.a + self.a*other.b
        # print(newReal, newImag)
        return GaussIntRoot3(newReal, newImag)

    def __rmul__(self, other):
        """ Multiply two values in the set together (in other direction) """
        return other.__mul__(self)

    def __add__(self, other):
        return GaussIntRoot3(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return GaussIntRoot3(self.a - other.a, self.b - other.b)

    def __str__(self) -> str:
        sign = "-" if self.b < 0 else "+"
        return f"{self.a}{sign}{abs(self.b)}isqrt(3)"

    def Complex(self) -> complex:
        """ Returns <self> as a complex number """
        return complex(self.a, self.b*s3)

    def __truediv__(self, other):
        return self.Complex()/other.Complex()

    def __rtruediv__(self, other):
        return other.Complex()/self.Complex()

    def TestDivisible(self, divisor, eps: float=1e-12) -> bool:
        """ Am I divisible by divisor (within Z[sqrt(-3)])? """
        return TestInGaussIntRoot3(self/divisor, eps=eps)


intRange: list = [-10, 10]
s3: float = np.sqrt(3)
test = GaussIntRoot3(1, 1) # The irreducible element we wish to test
epsilon: float = 1e-10

maxIterations: int = 100
for i in range(maxIterations):
    """ The 2*(...) here comes from the need for 'ab' to be divisible by 4
        (which you get from da maffs). 1*(...) and 4*(...) also seems to work
        to the same effectiveness (1*(...) and 1*(...) much less so).
    """
    oneCoeffs: list = 2*np.random.randint(*intRange, [2])
    twoCoeffs: list = 2*np.random.randint(*intRange, [2])
    one = GaussIntRoot3(*oneCoeffs)
    two = GaussIntRoot3(*twoCoeffs)
    if not(one.TestDivisible(test) or two.TestDivisible(test)):
        value = one*two
        if value.TestDivisible(test):
            division = value/test
            if TestInGaussIntRoot3(division, eps=epsilon):
                division = GaussIntRoot3(round(division.real), round(division.imag/s3))
            print(f"{i}: {one} {two}, {value}, {division}")

