#!/usr/bin/env python3

from click import echo, group, option

from parser import (
    wiki_random,
    wiki_languages,
    wiki_search,
    wiki_suggest,
)

@group()
def wiki():
    pass

@wiki.command()
def random():
    echo(f"A random interesting topic is {wiki_random()}")

@wiki.command()
def languages():
    echo(wiki_languages())

@wiki.command()
@option('--query', prompt="The query to search in wikipedia", help="The query to search in wikipedia")
@option('--results', default=5, help="The number of results to display")
def search(query, results):
    res = wiki_search(query, results)
    echo(
        "The results for the search are:\n\n" + '\n'.join(res)
    )

@wiki.command()
@option('--query', prompt="The query to search in wikipedia", help="The query to search in wikipedia")
def suggestion(query):
    res = wiki_suggest(query)
    if res:
        echo(f"The suggestion found for {query} are:\n\n" + '\n'.join(res))
    else:
        echo(f"Wupsy, The suggestion for {query} could not be found.")


if __name__ == '__main__':
    wiki()
