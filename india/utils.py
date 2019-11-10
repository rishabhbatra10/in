""" Utils File supporting the module"""
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra1002@gmail.com
# python imports
import os
import re

WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

FILE_NAME = {
    'states': WORKING_DIRECTORY + '/data/states.csv',
    'ut': WORKING_DIRECTORY + '/data/ut.csv',
    'cities': WORKING_DIRECTORY + '/data/cities.csv',
    'towns': WORKING_DIRECTORY + '/data/towns.csv',
    'config': WORKING_DIRECTORY + '/data/in.conf'
}

ABBR_RE = re.compile(r'^[a-zA-Z]{2,3}$')
