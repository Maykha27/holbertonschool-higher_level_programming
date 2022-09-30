#!/usr/bin/python3
import json
"""function that returns an object represented by a JSON string:"""


def from_json_string(my_str):
    """fonction"""
    return json.loads(my_str)

