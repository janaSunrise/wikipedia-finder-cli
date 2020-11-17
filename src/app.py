#!/usr/bin/env python3

from click import command, echo, group

from parser import wiki_random

@group()
def cli():
    pass

@cli.command()
def random():
    echo(f"A random interesting topic is {wiki_random()}")


if __name__ == '__main__':
    cli()
