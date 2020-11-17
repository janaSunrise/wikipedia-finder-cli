#!/usr/bin/env python3

from click import command, echo, group

from scraper import _get_json

@command()
def hello():
    echo('Hello World!')

@group()
def cli():
    pass

@cli.command()
def random():
    pass


if __name__ == '__main__':
    hello()
