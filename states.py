import csv

STATES = []
UNION_TERRITORIES = []
STATES_AND_TERRITORIES = []

state_file = './data/states.csv'


class State(object):

    def __init__(self, abbr: str, name: str):
        self.name = name
        self.abbr = abbr

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

    with open(state_file) as statesfile:
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
    with open(ut_file) as utsfile:
        uts = csv.reader(utsfile, delimiter= ',')
        for row in uts:
            ut = State(row[1], row[0])

            # creates a list of uts
            UNION_TERRITORIES.append(ut)

            # appends to the master list of all states and territories
            STATES_AND_TERRITORIES.append(ut)

            #provides package-level abbrevation
            globals()[ut.abbr] = ut


# initialising states and territories
if __name__ == '__main__':
    load_states()
    load_ut()
