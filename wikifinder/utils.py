#!/usr/bin/env python3
__all__ = (
    "remove_italics",
    "get_color",
    "get_bright_color"
)

import colorama

colorama.init(autoreset=True)


def get_color(color: str) -> str:
    return getattr(colorama.Fore, color.upper())


def get_bright_color(color: str) -> str:
    return getattr(colorama.Style, "BRIGHT") + get_color(color)  # noqa: B009


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
