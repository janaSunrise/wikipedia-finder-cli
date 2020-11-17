#!/usr/bin/env python3

import requests

lang = "en"

base_url = f"https://{lang}.wikipedia.org/w/api.php"


def _get_json(params):

    params["action"] = "query"
    params["format"] = "json"
    params["formatversion"] = "2"  # Cleaner json results
    params["prop"] = "extracts"  # Include extract in returned results
    params["exintro"] = "1"  # Only return summary paragraph(s) before main content
    params["redirects"] = "1"  # Follow redirects
    params["explaintext"] = "1"  # Make sure it's plaintext (not HTML)

    return requests.get(base_url, params=params).json()
