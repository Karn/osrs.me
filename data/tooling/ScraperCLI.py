#!/usr/bin/python

"""
A command-line tool that allows for data scraping for various datasets.

Usage:
    Scraper.py item <id> [--wiki|--ge]

Arguments:
    item
    object
    npc
"""
from docopt import docopt

class ScraperCLI(object):

    def __init__(self):
        pass

    def parse_args(self, argv):

        # Start by filtering for item specific operations.
        if 'item' in argv and argv['item']:

            print 'Scraping data for item with id', argv['<id>']


    def fetch_from_ge(self, item_id):
        pass

    def fetch_from_wiki(self):
        pass

if __name__ == '__main__':
    # Leverage the docopt module to get commands for the arguments.
    argv = docopt(__doc__)

    print argv

    # Create an instance of the Scraper object.
    _Scraper = ScraperCLI()

    # Start the scraper.
    _Scraper.parse_args(argv)