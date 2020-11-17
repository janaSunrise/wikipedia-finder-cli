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
