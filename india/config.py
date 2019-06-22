""" Config parsing to create a singleton """
# @coding: utf-8
# @author: Rishabh Batra
# @email: rishabhbatra10@gmail.com

from configparser import ConfigParser


class Config(object):
    """
    Handles the singleton use
    of the application configuration
    """
    class __ActualConfig(object):
        def __init__(self, path):
            self.config = ConfigParser()
            with open(path) as infl:
                self.config.read_file(infl)
            self.validate()

        def validate(self):
            # Validating whether Required Configurations are available
            if not self.config.has_option('WEATHER_API', 'KEY'):
                raise ValueError('Authorisation Key not found in config file')
            if not self.config.has_option('WEATHER_API', 'BASE_URL'):
                raise ValueError('Base Url not found for Support API')

    config_instance = None

    def __init__(self, path=None):
        if not Config.config_instance and path:
            Config.config_instance = Config.__ActualConfig(path)

    def __getattr__(self, name):
        """Proxy to the singleton configuration object
        """
        return getattr(self.config_instance.config, name)

    def get_items(self, section):
        """
        Get all the items found in the section
        :param section:
        :return:
        """
        return dict(self.config_instance.config.items(section))

