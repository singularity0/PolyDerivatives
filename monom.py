class MonomException(Exception):
    pass


class Monom:
    """docstring for Monom"""
    def __init__(self, param, var, deg):
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

    def __eq__(self, other):5
        return self.deg == other.deg

    def __hash__(self):
        return hash(self.deg)

    def is_trivial(self):
        return 1 if self.deg == 0 else False

    def derivative(self):
        # f'(x) = n * c * x^(n - 1)
        result = "{}{}^{}".format(self.deg * self.param, self.var, self.deg-1)
        return result


class Derivative(Monom):
    """docstring for Derivative"""
    def __init__(self, polynom):
        self.polynom = polynom
        self.derivative

    def derivative(self):
        for monom in self.polynom:
            if monom == monom:
                if monom.is_trivial():
                    self.derivative = 0
                self.derivative = monom + monom

