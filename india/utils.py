# python imports
import subprocess

WORKING_DIRECTORY = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).communicate()[
                            0].rstrip().decode('utf-8') + '/'

FILE_NAME = {
    'states': 'data/states.csv',
    'ut': 'data/ut.csv'
}