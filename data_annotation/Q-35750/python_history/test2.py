from pprint import pprint
from collections import defaultdict


def pseudo_raise(**kwargs):
    """
    Creates a nested dictionary from key-value pairs.

    Args:
        **kwargs: Arbitrary number of key-value pairs.

    Returns:
        Nested dictionary.
    """

    result = defaultdict(dict)  # Creates nested dictionaries automatically
    for key, value in kwargs.items():
        parts = key.split("__")

        if len(parts) == 2:
            # If the key has a "__", split it into nested_key and nested_value
            nested_key, nested_value = parts
            result[nested_key][nested_value] = value
        else:
            # If there's no "__" in the key, treat it as a top-level key
            result[key] = value

    return dict(result)  # Convert defaultdict back to a regular dictionary

# pprint(pseudo_raise(cipherOutput__logId="2", toplevel="banter"))

# Example usage:
pprint(pseudo_raise(toplevel__secondlevel="here", itworks="yes"))
