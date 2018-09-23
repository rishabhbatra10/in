import csv

STATES = []
UNION_TERRITORIES = []
STATES_AND_TERRITORIES = []

state_file = './data/states.csv'


class State(object):

    def __init__(self, abbr, name):
        self.name = name
        self.abbr = abbr

    def __repr__(self):
        return "<State: %s>" % self.name

    def __str__(self):
        return self.name


def load_states():
    """
    Load state data from a txt file in the package

    creates list of states, union territories.
    Also adds state abbrevation attribute access to the package.
    in.states.MD
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


# initialising states and territories
if __name__ == '__main__':
    load_states()
