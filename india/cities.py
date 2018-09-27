""" This enables easy access to indian districts in the respective states """
# @coding: utf-8
# @author: Rishabh Batra
# @email: ribhu.1996@gmail.com
# TODO:
# Write the function for loading states

# python imports

# module imports
import states

CITIES = []


class City(object):
    """
    Defines a city
    """
    def __init__(self, name: str, state: str):
        self.name = name
        self.state = states.lookup(state)

    def __repr__(self):
        return "<City: %s>" % self.name

    def __str__(self):
        return self.name

    def is_capital(self):
        """
        :return: boolean whether the city is capital or not
        """
        if self.name == self.state.capital:
            return True
        else:
            return False



