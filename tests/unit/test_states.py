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
        
        self.assertEqual(str(state), name)
        self.assertEqual(type(state), '<State: %s>'.format(name))
        self.assertEqual(state.name, name)
        self.assertEqual(state.abbr, abbrevation)
        self.assertEqual(state.capital, capital)
        self.assertEqual(state.population, int(population))
        self.assertEqual(state.area, int(area))
        self.assertEqual(state.density, int(population)/ int(area))
        self.assertEqual(state.language, language)

