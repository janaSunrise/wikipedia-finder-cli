#!/usr/bin/env python3

import requests

lang = "en"

base_url = f"https://{lang}.wikipedia.org/api/rest_v1"


def _get_json(url):
    return requests.get(base_url + url).json()
