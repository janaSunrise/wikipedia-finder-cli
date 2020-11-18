#!/usr/bin/env python3

import html2text
import requests

from scraper import _get_json, base_url

from random import choice

handler = html2text.HTML2Text()
handler.ignore_images = True
handler.ignore_links = True
handler.bypass_tables = True
handler.ignore_emphasis = True
handler.escape_snob = True
handler.escape_html = True

def wiki_random():
    request = _get_json("/page/random/title")

    return request["items"][0]["title"]


def wiki_random_summary():
    request = _get_json("/page/random/summary")

    return request["displaytitle"], handler.handle(request["extract"]).replace("\n", " ")

def wiki_summary(query):
    request = _get_json(f"/page/summary/{query}?redirect=true")

    if "detail" in request:
        return "Article Not found!"

    return request["displaytitle"], request["extract"], request["content_urls"]["desktop"]["page"]


def wiki_search(query, results=5):
    params = {
        'list': 'search',
        'srprop': '',
        'srlimit': results,
        'limit': results,
        'srsearch': query
    }

    raw_results = _get_json(params)

    if 'error' in raw_results:
        if raw_results['error']['info'] in ('HTTP request timed out.', 'Pool queue is full'):
            raise Exception(query)
        else:
            raise Exception(raw_results['error']['info'])

    search_results = (result['title'] for result in raw_results['query']['search'])

    return list(search_results)


def wiki_languages():
    response = _get_json(
        {
            'meta': 'siteinfo',
            'siprop': 'languages'
        }
    )

    languages = response['query']['languages']

    lang_string = ""
    for lang in languages:
        lang_string += f"{lang['code']}: {lang['name']}\n"

    return lang_string


def wiki_suggest(query):
    request = _get_json(f"/page/related/{query}")

    if "detail" in request:
        return "No suggestion found!"

    page = choice(request["pages"])
    return page["displaytitle"], page["extract"], page["content_urls"]["desktop"]["page"]

def pdf_download(query):
    request = requests.get(f"{base_url}/page/pdf/{query}")

    if "detail" in request:
        return "No such page found!"

    return request.content
