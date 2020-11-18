#!/usr/bin/env python3

import html2text

from scraper import _get_json

handler = html2text.HTML2Text()
handler.ignore_images = True
handler.ignore_links = True
handler.bypass_tables = True

def wiki_random():
    request = _get_json("/page/random/title")

    return request["items"][0]["title"]


def wiki_random_summary():
    request = _get_json("/page/random/summary")

    return request["titles"]["display"], handler.handle(request["extract"])


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
    params = {
        'list': 'search',
        'srinfo': 'suggestion',
        'srprop': '',
    }
    params['srsearch'] = query

    raw_result = _get_json(params)

    titles = []
    if raw_result["query"]["search"]:
        for search in raw_result["query"]["search"]:
            titles.append(search["title"])

        return titles

    return None
