""" This enables easy access to indian states and union territories """
# @coding: utf-8
# @author: Rishabh Batra
# @email: ribhu.1996@gmail.com
# TODO:
# Add state lookup function for finding states

# python imports
import csv
import re

# module imports
from . import utils

ABBR_RE = re.compile(r'^[a-zA-Z]{2}$')

STATES = []
UNION_TERRITORIES = []
STATES_AND_TERRITORIES = []

_lookup_cache = {}


class State(object):
    """ defines a state"""
    def __init__(self, abbr: str, name: str, capital: str=None):
        self.name = name
        self.abbr = abbr
        self.capital = None

    def __repr__(self):
        return "<State: %s>" % self.name

    def __str__(self):
        return self.name


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
            state = State(row[1], row[0])

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
        uts = csv.reader(utsfile, delimiter= ',')
        for row in uts:
            ut = State(row[1], row[0])

            # creates a list of uts
            UNION_TERRITORIES.append(ut)

            # appends to the master list of all states and territories
            STATES_AND_TERRITORIES.append(ut)

            #provides package-level abbrevation
            globals()[ut.abbr] = ut


def lookup(val: str, field: str=None, use_cache: bool=True) -> str:
    """ This provides functionality to find state based on the
    lookup value provided.

    :param str val: if val has 2 alphas it will look for abbrevation
                    anything else will try to match the state names

    :param str field: can take values, 'None', 'abbr', 'name' to bypass fuzzy matching.


    This method caches non-None results, but cache can be bypassed with the
    `use_cache=False` argument.
    TODO: add another attribute to this for lookup of metaphones
        """
    # jellyfish for fuzzy matching

    if field is None:
        if ABBR_RE.match(val):
            val = val.upper()
            field = 'abbr'
        else:
            val = val.capitalize()
            field = 'name'

    # see if result is in cache
    cache_key = "%s:%s" % (field, val)
    if use_cache and cache_key in _lookup_cache:
        return _lookup_cache[cache_key]

    for state in STATES_AND_TERRITORIES:
        if val == getattr(state, field):
            _lookup_cache[cache_key] = state
            return state


# initialising states and territories
load_states()
load_ut()
