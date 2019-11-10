""" This enables access to indian towns in respective cities """
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra1002@gmail.com
# Write class Town and creating a Town object for every town in database

# python imports

# module imports
from . import cities

TOWNS = []


class Town:
    """
    Defines a Town
    """
    def __init__(self,
                 pin_code: int,
                 name: str,
                 city: str,
                 latitude: float,
                 longitude: float,
                 accuracy: float):

        self.pin_code = pin_code
        self.name = name
        self.city = cities.lookup(city)
        self.state = self.city.state
        self.latitude = latitude
        self.longitude = longitude
        self.accuracy = accuracy

    def __repr__(self):
        return '<Town: %s>' % self.name

    def __str__(self):
        return self.name
