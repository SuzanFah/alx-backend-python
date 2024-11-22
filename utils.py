#!/usr/bin/env python3
"""Utility functions for nested map access"""

def access_nested_map(nested_map, path):
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    """
    for key in path:
        if not isinstance(nested_map, dict):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map
