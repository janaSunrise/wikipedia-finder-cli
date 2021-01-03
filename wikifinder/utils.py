#!/usr/bin/env python3

def remove_italics(to_parse: str) -> str:
    """
    A utility function for removing the italic HTML tags.

    Parameters
    ----------
    to_parse: str
        The string to be cleaned.

    Returns
    -------
    str
        The cleaned string.
    """
    return to_parse.replace("<i>", "").replace("</i>", "")
