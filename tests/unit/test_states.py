""" Testing indian states class """
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra10@gmail.com
# TODO: Write tests for each an every function
# TODO: Add test failure messages

# external imports
import unittest

# module imports
from india import states


class TestStates(unittest.TestCase):
    """ Test suite for States module """

    def test_state_initialization(self):
        """ Testing state initialization """
        abbrevation = 'KA'
        name = 'Karnataka'
        capital = 'Bangalore'
        population = '61095297' # in numbers
        area = '191791' # km^2 
        language = 'Kannada'

        state = states.State(abbr=abbrevation, 
                             name=name, 
                             capital=capital, 
                             population=population, 
                             area=area, 
                             lang=language)
        
        self.assertEqual(
            str(state), 
            name, 
            "State str not matching with the name"
            )
        self.assertEqual(
            type(state), 
            '<State: %s>'.format(name), 
            "Object representation doesn't match with the provided repr"
            )
        self.assertEqual(
            state.name, 
            name, 
            "Provided name not matches with object's name"
            )
        self.assertEqual(
            state.abbr, 
            abbrevation, 
            "Provided abbrevation not matching with objectss abbrevation"
            )
        self.assertEqual(
            state.capital, 
            capital, 
            "Provided capital not matching with object's capital"
            )
        self.assertEqual(
            state.population, 
            int(population), 
            "Provided population not matching with object's population"
            )
        self.assertEqual(
            state.area, 
            int(area), 
            "Provided area not matching with object's area"
            )
        self.assertEqual(
            state.density, 
            int(population) // int(area), 
            "Provided pop density not matching with object's density"
            )
        self.assertEqual(
            state.language, 
            language, 
            "Provided language not matching with object's language"
            )
