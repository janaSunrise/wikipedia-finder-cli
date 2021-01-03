#!/usr/bin/env python3

import requests

lang = "en"

base_url = f"https://{lang}.wikipedia.org/api/rest_v1"


def _get_json(url: str) -> dict:
    """
    This function is used to fetch JSON from the specified path of Wikipedia.

    Parameters
    ----------
    url : str
        The URL path to be used to fetch JSON.

    Returns
    -------
    dict
        The JSON response from the endpoint.
    """
    return requests.get(base_url + url).json()
