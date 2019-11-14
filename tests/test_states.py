""" Testing indian states class """
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra1002@gmail.com

# external imports
import unittest

# module imports
from india import states


class TestStates(unittest.TestCase):
    """ Test suite for States module """
    ABBREVIATION = 'KA'
    NAME = 'Karnataka'
    CAPITAL = 'Bangalore'
    POPULATION = '61095297'  # in numbers
    AREA = '191791'  # km^2
    LANGUAGE = 'Kannada'

    STATE = states.State(abbr=ABBREVIATION,
                         name=NAME,
                         capital=CAPITAL,
                         population=int(POPULATION),
                         area=int(AREA),
                         lang=LANGUAGE)

    def test_state_initialization(self):
        """ Testing state initialization """
        self.assertEqual(
            str(self.STATE),
            self.NAME,
            "State str not matching with the name"
        )

        self.assertEqual(
            repr(self.STATE),
            '<State: {}>'.format(self.NAME),
            "Object representation doesn't match with the provided repr"
        )

        self.assertEqual(
            self.STATE.name,
            self.NAME,
            "Provided name not matches with object's name"
        )

        self.assertEqual(
            self.STATE.abbr,
            self.ABBREVIATION,
            "Provided abbrevation not matching with objectss abbrevation"
        )

        self.assertEqual(
            self.STATE.capital,
            self.CAPITAL,
            "Provided capital not matching with object's capital"
            )
        self.assertEqual(
            self.STATE.population,
            int(self.POPULATION),
            "Provided population not matching with object's population"
            )
        self.assertEqual(
            self.STATE.area,
            int(self.AREA),
            "Provided area not matching with object's area"
            )
        self.assertEqual(
            self.STATE.density,
            int(self.POPULATION) // int(self.AREA),
            "Provided pop density not matching with object's density"
            )
        self.assertEqual(
            self.STATE.language,
            self.LANGUAGE,
            "Provided language not matching with object's language"
            )

    def test_states_stats_validation(self):
        """ Testing the stats validation for states class"""
        # TEST 1: Function returning None on giving None as Input
        stats = None
        self.assertEqual(self.STATE.stats_validation(stats), None,
                         "Function should return none when stats are none."
                         )

        # TEST 2: Function returns an integer on passing str.
        stats = '10939485'
        self.assertEqual(self.STATE.stats_validation(stats), int(stats),
                         "Function should return {}".format(int(stats))
                         )

        # TEST 4: Function raises type error on passing a list
        stats = 1029482384
        with self.assertRaises(TypeError):
            self.STATE.stats_validation([stats])

        # TEST 5: Function raises ValueError on passing a illegal value as integer.
        stats = "fsdibvs130923"
        with self.assertRaises(ValueError):
            self.STATE.stats_validation(stats)

    def test_lookup(self):
        """ Testing the lookup for getting states output """

        # TEST 1: test with abbrevation and use_cache True
        self.assertEqual(states.lookup(val='KA', field='abbr'), states.KA)

        # TEST 2: test with full name and use_cache = True
        self.assertEqual(states.lookup(val='manipur', field='name'), states.MN)

        # TEST 3: test with abbrevation without using cache
        self.assertEqual(states.lookup(val='HR', field='abbr', use_cache=False), states.HR)

        # TEST 4: test with name without using cache
        self.assertEqual(states.lookup(val='delhi', field='name', use_cache=False), states.DL)

        # TEST 5: test with faulty name so that matching fail
        with self.assertRaises(ValueError):
            states.lookup(val='XY', field='abbr')


if __name__ == '__main__':
    unittest.main()
