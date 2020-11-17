#!/usr/bin/env python3

from scraper import _get_json

def wiki_random():
    params = {
        'list': 'random',
        'rnnamespace': 0,
        'rnlimit': 1,
    }

    request = _get_json(params)

    return request["query"]["random"][0]["title"]

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
