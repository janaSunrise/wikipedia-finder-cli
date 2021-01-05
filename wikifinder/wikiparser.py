#!/usr/bin/env python3
import html2text
import requests

from scraper import _get_json, base_url
from utils import remove_italics

import typing as t
from random import choice

handler = html2text.HTML2Text()
handler.ignore_images = True
handler.ignore_links = True
handler.bypass_tables = True
handler.ignore_emphasis = True
handler.escape_snob = True
handler.escape_html = True


def wiki_random() -> str:
    """
    Fetches a random interesting article from wikipedia to read from.

    Returns
    -------
    str
        The random article's title.
    """
    request = _get_json("/page/random/title")

    return remove_italics(request["items"][0]["title"])


def wiki_random_summary() -> t.Tuple[str, str]:
    """
    Fetches a random article with it's summary.

    Returns
    -------
    t.Tuple[str, str]
        The title and summary of the random article.
    """
    request = _get_json("/page/random/summary")

    return remove_italics(request["displaytitle"]), handler.handle(request["extract"]).replace("\n", " ")


def wiki_summary(query: str) -> t.Union[str, t.Tuple[str, str, str]]:
    """
    Gets the summary of the specified article.

    Parameters
    ----------
    query: str
        The article to be searched for.

    Returns
    -------
    t.Union[str, t.Tuple[str, str, str]]
        Returns Title, extract and URL for article, else `"Article not found"` if the article couldn't be found.
    """
    request = _get_json(f"/page/summary/{query}?redirect=true")

    if "detail" in request:
        return "Article Not found!"

    return remove_italics(request["displaytitle"]), request["extract"], request["content_urls"]["desktop"]["page"]


def wiki_suggest(query: str) -> t.Union[str, t.Tuple[str, str, str]]:
    """
    Gets the suggestion on basis of the specified article.

    Parameters
    ----------
    query: str
        The article to be used for suggestion.

    Returns
    -------
    t.Union[str, t.Tuple[str, str, str]]
        Returns Title, extract and URL for article, else `"Article not found"` if the article couldn't be found.
    """
    request = _get_json(f"/page/related/{query}")

    if "detail" in request:
        return "No suggestion found!"

    page = choice(request["pages"])
    return remove_italics(page["displaytitle"]), page["extract"], page["content_urls"]["desktop"]["page"]


def pdf_download(query: str) -> t.Union[str, bytes]:
    """
    Get the PDF content of the whole article and save it for reading it anytime.

    Parameters
    ----------
    query: str
        The query / article to search for.

    Returns
    -------
    bytes
        The Byte format of the PDF which is going to be saved.
    """
    request = requests.get(f"{base_url}/page/pdf/{query}")

    if "detail" in request:
        return "No such page found!"

    return request.content


def html_download(query: str, redirect: bool, stash: bool, accept_language: str) -> t.Union[str, bytes]:
    def bool_to_str(expression: bool) -> str:
        return str(expression).lower()

    headers = {
        "Accept-Language": accept_language
    }

    request = requests.get(
        f"{base_url}/page/html/{query}?redirect={bool_to_str(redirect)}&stash={bool_to_str(stash)}",
        headers=headers
    )

    if "detail" in request:
        return "No such page found!"

    return request.content


def on_this_day(year: int, month: int, day: int) -> t.Union[str, t.Tuple[str, str, str]]:
    """
    Get the incidents that happened on the specified date.
    Parameters
    ----------
    year: int
        The year for the incident.
    month: int
        The month for the incident.
    day: int
        The day for the incident.

    Returns
    -------
    t.Union[str, t.Tuple[str, str, str]]
       Returns Title, extract and URL for article, else `"Article not found"` if the article couldn't be found.
    """
    request = _get_json(f"/feed/featured/{year}/{month}/{day}")

    if "detail" in request:
        return request["detail"]

    page = choice(request["onthisday"][0]["pages"])

    return remove_italics(page["displaytitle"]), page["extract"], page["content_urls"]["desktop"]["page"]
