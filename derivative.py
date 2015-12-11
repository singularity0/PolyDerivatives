import re

class Derivative:
    """docstring for Derivative"""
    def __init__(self, param):
        self.input = param

    def __validator(self):
        print("not sure what to do now")
        pass

    def __check_for_var(self, polynom):
        f = re.compile('[/d]+')
        f.findall(polynom)
        
