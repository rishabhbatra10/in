

STATES = []
UNION_TERRITORIES = []


class State(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        return "<State:%s>" % self.name

    def load_states():
        """
        Load state data from a txt file in the package

        creates list of states, union territories.
        Also adds state abbrevation attribute access to the package.
        in.states.MD
        """