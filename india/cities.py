""" This enables easy access to indian districts in the respective states """
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra1002@gmail.com
# Get weather for every city using weather API

# python imports
import csv
from typing import List, AnyStr

# module imports
from . import config, states, utils

CITIES = []

_lookup_cache = {}


class City:
    """
    Defines a city
    """
    def __init__(self,
                 abbr: str,
                 name: str,
                 state: str,
                 population: int=None,
                 area: int=None,
                 url: str=None):
        self.name = name
        self.state = states.lookup(state)
        self.abbr = abbr
        self.state_abbr = '%s_%s' % (self.state.abbr, abbr)
        self.population = states.State.stats_validation(population)
        self.area = states.State.stats_validation(area)
        self.density = states.State.calc_population_density(
            self.population, self.area
        )
        self.url = url

    def __repr__(self):
        return "<City: %s>" % self.name

    def __str__(self):
        return self.name

    def is_capital(self):
        """
        :return: boolean whether the city is capital or not
        """
        return bool(self.name == self.state.capital)

    @staticmethod
    def weather():
        """
        :return:
        """
        config.Config().get('Machine')


def load_city():
    """
    Loads districs of india data from csv file.

    Also adds city level abbreviation to the package
    # in.cities.DL_CD
    :return:
    """
    with open(utils.FILE_NAME['cities'], encoding="utf-8") as citiesfile:
        cities = csv.reader(citiesfile, delimiter=',')
        next(cities)
        for row in cities:
            # reassigning empty strings of population area or url
            if len(row[4]) == 0:
                row[4] = None
            if len(row[5]) == 0:
                row[5] = None
            if len(row[7]) == 0:
                row[7] = None

            city = City(state=row[0],
                        abbr=row[1],
                        name=row[2],
                        population=row[4],
                        area=row[5],
                        url=row[7]
                        )
            # list of cities
            CITIES.append(city)

            globals()[city.state_abbr] = city

    return 0


def lookup(val: str, field: str=None, use_cache: bool=True):
    """ This provides functionality to find city based on the
       lookup value provided.

       :param str val: if val has 2 alphas it will look for abbrevation
                       anything else will try to match the state names

       :param str field: can take values, 'None', 'abbr', 'name' to bypass fuzzy matching.

       :param bool use_cache:
       This method caches non-None results, but cache can be bypassed with the
       `use_cache=False` argument.

       TODO: Add fuzzy matching
    """
    if field is None:
        if utils.ABBR_RE.match(val):
            val = val.upper()
            field = 'abbr'
        else:
            val = val.capitalize()
            field = 'name'

    # check if result in cahe
    cache_key = "%s:%s" %(field, val)
    if use_cache and cache_key in _lookup_cache:
        return _lookup_cache[cache_key]

    for city in CITIES:
        if val == getattr(city, field):
            _lookup_cache[cache_key] = city
            return city


def get_cities() -> List[AnyStr]:
    """ This returns a list of strings of cities sorted in ascending order
    Example:
    >>> from india import cities
    >>> print(cities.get_cities())
    """

    city_names = []
    for city in CITIES:
        city_names.append(city.name)
    return sorted(city_names)


# initialising cities
load_city()
