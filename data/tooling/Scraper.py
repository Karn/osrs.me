#!/usr/bin/python

"""
A command-line tool that allows for data scraping for various datasets.

Usage:
    Scraper.py item <id> [ge|wiki|both]

Arguments:
    item
    object
    npc
"""
from docopt import docopt

class Scraper(object):

    def __init__(self):
        pass

    def parse_args(self, argv):

        if 'item' in argv and argv['item']:
            print 'Scraping data for item with id', argv['<id>']

            source = 'both' if argv['both'] else ('ge' if argv['ge'] else 'wiki')


    def fetch_from_ge(self):
        pass

    def fetch_from_wiki(self):
        pass

if __name__ == '__main__':
    # Leverage the docopt module to get commands for the arguments.
    argv = docopt(__doc__)

    print argv

    # Create an instance of the Scraper object.
    _Scraper = Scraper()

    # Start the scraper.
    _Scraper.parse_args(argv)