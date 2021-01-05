#!/usr/bin/env python3
from textwrap import dedent

from click import echo, group, option

from wikiparser import (
    wiki_random,
    wiki_random_summary,
    wiki_summary,
    wiki_suggest,
    pdf_download,
    html_download,
    on_this_day,
)


@group()
def wiki() -> None:
    pass


@wiki.command(help="Shows a random article title, and even the summary if the summary flag is specified.")
@option('--summary', is_flag=True, help="Get the summary of the random article along with title")
def random(summary: str) -> None:
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


@wiki.command(help="Get the summary of an article, by searching for it.")
@option('--query', prompt="The query to search in wikipedia", help="The query to search in wikipedia")
def summary(query: str) -> None:
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
def suggestion(query: str) -> None:
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
def pdf(query: str) -> None:
    res = pdf_download(query)

    if isinstance(res, str):
        echo(f"ERROR OCCURRED! {res}")
    else:
        with open(f"{query.replace(' ', '_')}.pdf", "wb") as file:
            file.write(res)

        echo(f"File saved as {query.replace(' ', '_')}.pdf")


@wiki.command(help="Download the HTML for an article by searching it.")
@option('--query', prompt="The query to search in wikipedia", help="The query to search in wikipedia")
@option('--language', prompt="The language for the HTML to get.", help="""
The desired language variant code for wikis where LanguageConverter is enabled. Example: sr-el for Latin
transcription of the Serbian language.
""")
def html(query: str, accept_language: str) -> None:
    res = html_download(query, redirect=False, stash=False, accept_language=accept_language)

    if isinstance(res, str):
        echo(f"ERROR OCCURRED! {res}")
    else:
        with open(f"{query.replace(' ', '_')}.html", "wb") as file:
            file.write(res)

        echo(f"File saved as {query.replace(' ', '_')}.html")


@wiki.command(help="Get an incident on the specified date using the flags.")
@option('--year', type=int, prompt="The year of the incident", help="The year of the incident to be searched")
@option('--month', type=int, prompt="The month of the incident", help="The month of the incident to be searched")
@option('--day', type=int, prompt="The day of the incident", help="The day of the incident to be searched")
def onthisday(year: int, month: int, day: int) -> None:
    res = on_this_day(year, month, day)

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
