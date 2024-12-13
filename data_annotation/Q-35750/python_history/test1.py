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

    result = defaultdict(dict)
    for key, value in kwargs.items():
        parts = key.split("__")
        if len(parts) == 1:
          result[parts[0]] = value  # Handle single keys
        elif len(parts) > 1:
          r = result[parts[0]]
          for part in parts[1:-1]:
            r = r[part] = defaultdict(dict) if not isinstance(r.get(part, {}), dict) else r[part] # Create nested dicts as needed
          r[parts[-1]] = value


    return result

# Test cases
pprint(pseudo_raise(toplevel__secondlevel="here", itworks="yes"))
pprint(pseudo_raise(a__b__c__d=4, a__b__e=5, f=6))
pprint(pseudo_raise(a="apple"))
pprint(pseudo_raise(a__b=1, a__c=2, d=3))