import re
import operator


class MonomException(Exception):
    pass


class Monom:
    """docstring for Monom"""
    def __init__(self, param=0, var='x', deg=0):
        self.param = param
        self.var = var
        self.deg = deg

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __add__(self, polynom):
        if polynom.deg == self.deg:
            self.param += polynom.param
        return MonomException('Not the same degree')
        pass

    def __sub__(self, polynom):
        if polynom.deg == self.deg:
            self.param -= polynom.param
        return MonomException('Not the same degree')

    def __eq__(self, other):
        return self.__hash__ == other.__hash__

    def __hash__(self):
        return hash("{}^{}".format(self.var, self.deg))

    def trivial(self):
        return 1 if self.deg == 0 else False

    def derivative(self):
        # f'(x) = n * c * x^(n - 1)
        if self.trivial():
            return self.param
        result = "{}{}^{}".format(self.deg * self.param, self.var, self.deg-1)
        return result


class Derivative:
    """docstring for Derivative"""
    def __init__(self, polynom):
        self.polynom = polynom
        self.operator = {"+": operator.add,
                         "-": operator.sub,
                         "*": operator.mul,
                         "/": operator.div}
        self.result = []

    def __make_monom(self):
        monoms = re.split('\+|\-|\*|\/', self.polynom)
        op = re.findall('\+|\-|\*|\/', self.polynom)
        for monom in monoms:
            self.result = Monom(list(monom)). derivative()

    def derivative(self, monom):
        for monom in self.polynom:
            if monom == monom:
                if monom.is_trivial():
                    self.derivative = monom.param
                self.derivative = monom + monom

