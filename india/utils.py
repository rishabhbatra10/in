# python imports
import subprocess

WORKING_DIRECTORY = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).communicate()[
                            0].rstrip().decode('utf-8') + '/'

FILE_NAME = {
    'states': WORKING_DIRECTORY + 'india/data/states.csv',
    'ut': WORKING_DIRECTORY + 'india/data/ut.csv'
}