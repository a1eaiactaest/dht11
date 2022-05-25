from functools import lru_cache


def cache(user_function, /):
    return lru_cache(maxsize=None)(user_function)
