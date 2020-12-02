#!/usr/bin/env python3

def remove_italics(to_parse):
    return to_parse.replace("<i>", "").replace("</i>", "")
