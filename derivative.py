import re

class Derivative:
    """docstring for Derivative"""
    def __init__(self, param):
        self.input = param

    def __validator(self):
        print("not sure what to do now")
        pass

    def __check_for_var(self, polynom):
        f = re.compile('[x]+')
        return 1 if not len(f.findall(polynom)) > 0 else True
    def __method(self):
        return 2