__author__ = 'Dmitry Pechatnikov'

from configparser import ConfigParser


class Config():
    def __init__(self):
        config = ConfigParser()
        config.read('config.ini')

        sections = config.sections()

        for section in sections:
            params = config.options(section)
            for param in params:
                __setattr__= param = config.get(section, param)