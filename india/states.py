""" This enables easy access to indian states and union territories """
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra1002@gmail.com

# python imports
import csv
from typing import List, AnyStr

# module imports
from . import utils

STATES = []
UNION_TERRITORIES = []
STATES_AND_TERRITORIES = []

_lookup_cache = {}


class State:
    """ defines a state"""
    def __init__(self, abbr: str, name: str, capital: str, population: int, area: int, lang: str):
        self.name = name
        self.abbr = abbr
        self.capital = capital
        self.population = self.stats_validation(population)
        self.area = self.stats_validation(area)
        self.density = self.calc_population_density(
            self.population,
            self.area
        )
        self.language = lang

    def __repr__(self):
        return "<State: {}>".format(self.name)

    def __str__(self):
        return self.name

    @staticmethod
    def stats_validation(stats: (str, int, None)=None) -> (int, None):
        """Validating Statistics entered and converting them to string"""

        if not isinstance(stats, (str, int, type(None))):
            raise TypeError(
                "Stats should either be a string of integers, integer or None. Provided type {}"
                .format(type(stats)))

        stats_is_not_none = stats is not None
        if stats_is_not_none:
            stats = int(stats)
        else:
            stats = None
        return stats

    @staticmethod
    def calc_population_density(population: int, area: int) -> (int, None):
        """ Calculating the Population Density given the Population and Area """
        if population is not None and area is not None:
            return population // area


#  the class functions of the package ends here #
def load_states():
    """
    Load state data from a csv file in the package

    Creates list of states.
    Also adds state abbrevation attribute access to the package.
    # in.states.AR
    """

    with open(utils.FILE_NAME['states']) as statesfile:
        states = csv.reader(statesfile, delimiter=',')
        for row in states:
            state = State(abbr=row[0],
                          name=row[1],
                          capital=row[2],
                          population=row[3],
                          area=row[4],
                          lang=row[5]
                          )

            # creates list of states
            STATES.append(state)

            # creates a master list of all states and territories
            STATES_AND_TERRITORIES.append(state)

            # provide package-level abbrevation
            globals()[state.abbr] = state


def load_ut():
    """
    Load union territories from a csv file provided with the package.

    Creates a list of Union Teriitories.
    Also add abbrevation attribute access to the package
    # in.states.PY

    """
    with open(utils.FILE_NAME['ut']) as utsfile:
        uts = csv.reader(utsfile, delimiter=',')
        for row in uts:
            ut = State(abbr=row[0],
                       name=row[1],
                       capital=row[2],
                       population=row[3],
                       area=row[4],
                       lang=row[5]
                       )

            # creates a list of uts
            UNION_TERRITORIES.append(ut)

            # appends to the master list of all states and territories
            STATES_AND_TERRITORIES.append(ut)

            # provides package-level abbrevation
            globals()[ut.abbr] = ut


def lookup(val: str, field: str=None, use_cache: bool=True) -> str:
    """ This provides functionality to find state based on the
    lookup value provided.

    :param str val: if val has 2 alphas it will look for abbrevation
                    anything else will try to match the state names

    :param str field: can take values, 'None', 'abbr', 'name' to bypass fuzzy matching.

    :param bool use_cache: Caching of the Loaded States
    This method caches non-None results, but cache can be bypassed with the
    `use_cache=False` argument.
    TODO: add another attribute to this for lookup of metaphones
        """
    # jellyfish for fuzzy matching
    # capitalizing the value to standardize formatting

    if field is None:
        if utils.ABBR_RE.match(val):
            val = val.upper()
            field = 'abbr'
        else:
            val = val.capitalize()
            field = 'name'
    elif field == 'name':
        val = val.capitalize()

    # see if result is in cache
    cache_key = "%s:%s" % (field, val)
    if use_cache and cache_key in _lookup_cache:
        return _lookup_cache[cache_key]

    for state in STATES_AND_TERRITORIES:
        if val == getattr(state, field):
            _lookup_cache[cache_key] = state
            return state

    raise ValueError('{}. matching state not found. Please try entering something else.'.format(val))


def get_states(entity: str = 'all') -> List[AnyStr]:
    """ This returns a list of strings of entities sorted in ascending order if entity param is not passed
    :param entity: enum with allowed values ('state', 'ut', 'all')
           default: 'all'
    Example:
    >>> from india import states
    >>> print(states.get_states())
    """
    allowed_entities = ('state', 'ut', 'all')
    # validation
    if entity not in allowed_entities:
        raise ValueError(f'Wrong entity type passed: {entity}. Allowed values {allowed_entities}')

    state_names = []

    # appending state names
    if entity in ('all', 'state'):
        for state in STATES:
            state_names.append(state.name)

    # appending ut names
    if entity in ('all', 'ut'):
        for ut in UNION_TERRITORIES:
            state_names.append(ut.name)

    return sorted(state_names)


# initialising states and territories
load_states()
load_ut()
