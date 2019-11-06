""" This enables access to indian towns in respective cities """
# @coding: utf-8
# @author: Rishabh Batra
<<<<<<< HEAD
# @email: rishabhbatra10@gmail.com
# TODO: Write class town representing a town
=======
# @email: rishabhbatra1002@gmail.com
# TODO:
# Write class town representing a town
>>>>>>> 0e9a42e7dffe20d757a22c1b3e9c552232f2c12b

# python imports

# module imports
from . import cities

TOWNS = []


class TOWN(object):
    """
    Defines a Town
    """
    def __init__(self, pin_code: int, name: str, city: str, latitude: float, longitude: float, accuracy: float):
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
