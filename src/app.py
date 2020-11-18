#!/usr/bin/env python3

from textwrap import dedent

from click import echo, group, option

from parser import (
    wiki_random,
    wiki_random_summary,
    wiki_summary,
    wiki_languages,
    wiki_search,
    wiki_suggest,
    pdf_download,
)

@group()
def wiki():
    pass

@wiki.command(help="Shows a random article title, and even the summary if the summary flag is specified.")
@option('--summary', is_flag=True, help="Get the summary of the random article along with title")
def random(summary):
    if summary:
        title, summary = wiki_random_summary()
        echo(
            dedent(f"""
            Here's a Random interesting topic: {title}\n
            {summary}
            """)
        )
    else:
        echo(f"A random interesting topic is {wiki_random().replace('_', ' ')}")

@wiki.command(help="Shows all the languages that wikipedia supports.")
def languages():
    echo(wiki_languages())

@wiki.command(help="Perform a search to find for various articles.")
@option('--query', prompt="The query to search in wikipedia", help="The query to search in wikipedia")
@option('--results', default=5, help="The number of results to display")
def search(query, results):
    res = wiki_search(query, results)
    echo(
        "The results for the search are:\n\n" + '\n'.join(res)
    )

@wiki.command(help="Get the summary of an article, by searching for it.")
@option('--query', prompt="The query to search in wikipedia", help="The query to search in wikipedia")
def summary(query):
    res = wiki_summary(query)
    if isinstance(res, str):
        echo(f"ERROR OCCURED! {res}")
    else:
        title, summary, link = res
        echo(
            dedent(f"""
            {title}\n
            {summary}\n
            Read more here: {link}
            """)
        )

@wiki.command(help="Get suggestion for more articles by adding the name of an article you're interested in.")
@option('--query', prompt="The query to search in wikipedia", help="The query to search in wikipedia")
def suggestion(query):
    res = wiki_suggest(query)
    if isinstance(res, str):
        echo(f"ERROR OCCURED! {res}")
    else:
        title, summary, link = res
        echo(
            dedent(f"""
            {title}\n
            {summary}\n
            Read more here: {link}
            """)
        )

@wiki.command(help="Download a PDF for an article by searching it.")
@option('--query', prompt="The query to search in wikipedia", help="The query to search in wikipedia")
def pdf(query):
    res = pdf_download(query)

    if isinstance(res, str):
        echo(f"ERROR OCCURED! {res}")
    else:
        with open(f"{query.replace(' ', '_')}.pdf", "wb") as file:
            file.write(res)

        echo(f"File saved as {query.replace(' ', '_')}.pdf")


if __name__ == '__main__':
    wiki()
