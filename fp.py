"""functional programming helpers"""
# https://toolz.readthedocs.io/en/latest/api.html
from toolz.curried import curry

@curry
def pick(keys, dic):
    """
    filter dict keys:
    >>> dic = pick(['foo', 'baz'])({ 'foo': 1, 'bar': 2, 'baz': 3 })
    """
    return {key: dic[key] for key in keys}

@curry
def destruct(keys, dic):
    """
    destructure variables from a dict:
    >>> foo, baz = destruct(['foo', 'baz'])({ 'foo': 1, 'bar': 2, 'baz': 3 })
    """
    return (dic[key] for key in keys)

@curry
def evolve(transformations, dic):
    """
    change part of a dict:
    >>> doubled = evolve({ 'age': lambda x: 2*x })({ 'name': 'me', 'age': 10 })
    """
    result = {}
    for key in dic:
        tform = transformations.get(key, None)
        result[key] = tform(dic[key]) if callable(tform) else \
              evolve(tform, dic[key]) if isinstance(tform, dict) else dic[key]
    return result
