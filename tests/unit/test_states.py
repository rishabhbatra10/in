""" Testing indian states class """
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra1002@gmail.com
# TODO: Write tests for each an every function
# TODO: Add test failure messages

# external imports
import unittest

# module imports
from india import states


class TestStates(unittest.TestCase):
    """ Test suite for States module """
    def __init__(self):
        super().__init__(self)
        self.abbrevation = 'KA'
        self.name = 'Karnataka'
        self.capital = 'Bangalore'
        self.population = '61095297' # in numbers
        self.area = '191791' # km^2 
        self.language = 'Kannada'

        self.state = states.State(abbr=abbrevation, 
                             name=name, 
                             capital=capital, 
                             population=population, 
                             area=area, 
                             lang=language)


    def test_state_initialization(self):
        """ Testing state initialization """
        self.assertEqual(
            str(self.state), 
            self.name, 
            "State str not matching with the name"
            )
        self.assertEqual(
            type(self.state), 
            '<State: %s>'.format(name), 
            "Object representation doesn't match with the provided repr"
            )
        self.assertEqual(
            self.state.name, 
            self.name, 
            "Provided name not matches with object's name"
            )
        self.assertEqual(
            self.state.abbr, 
            self.abbrevation, 
            "Provided abbrevation not matching with objectss abbrevation"
            )
        self.assertEqual(
            self.state.capital, 
            self.capital, 
            "Provided capital not matching with object's capital"
            )
        self.assertEqual(
            self.state.population, 
            int(self.population), 
            "Provided population not matching with object's population"
            )
        self.assertEqual(
            self.state.area, 
            int(self.area), 
            "Provided area not matching with object's area"
            )
        self.assertEqual(
            self.state.density, 
            int(self.population) // int(self.area), 
            "Provided pop density not matching with object's density"
            )
        self.assertEqual(
            self.state.language, 
            self.language, 
            "Provided language not matching with object's language"
            )

    def test_states_stats_validation(self):
        """ Testing the stats validation for states class"""
        # TEST 1: Function returning None on giving None as Input
        stats = None
        self.assertEqual(self.state.stats_validation(stats), None, 
            "Function should return none when stats are none."
        )

        # TEST 2: Function returns an integer on passing str.
        stats = '10939485'
        self.assertEqual(self.state.stats_validation(stats), int(stats), 
        "Function should return {}".format(int(stats)))
        
        self.assertEqual(str(state), name)
        self.assertEqual(type(state), '<State: %s>'.format(name))
        self.assertEqual(state.name, name)
        self.assertEqual(state.abbr, abbrevation)
        self.assertEqual(state.capital, capital)
        self.assertEqual(state.population, int(population))
        self.assertEqual(state.area, int(area))
        self.assertEqual(state.density, int(population)/ int(area))
        self.assertEqual(state.language, language)

        # TEST 4: Funcion raises type error on passing a list
        stats = 1029482384
        with self.assertRaises(TypeError):
            self.state.stats_validation([stats])
        
        # TEST 5: Function raises ValueError on passing a illegal value as integer.
        stats = "fsdibvs130923"
        with self.assertRaises(ValueError):
            self.state.stats_validation(stats)
