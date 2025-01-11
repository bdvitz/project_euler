from functools import wraps

def cache(fn: callable):
    """ Cached results wrapper """
    results = {}
    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs))
        if key not in results:
            results[key] = fn(*args, **kwargs)
        return results[args]
    return wrapper()
