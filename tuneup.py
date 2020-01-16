#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Joey Brown with help from Coaches"

import cProfile
import pstats
import functools
import timeit
from collections import Counter


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    @functools.wraps(func)
    def inner(*args, **kwargs):
        c = cProfile.Profile()
        c.enable()
        result = func(*args, **kwargs)
        c.disable()
        sort_by = 'cumulative'
        cs = pstats.Stats(c).strip_dirs().sort_stats(sort_by)
        cs.print_stats(5)
        return result
    return inner


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movie_counter = Counter(movies)
    duplicates = [movie for movie, count in movie_counter.items() if count > 1]
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='pass', setup='pass')
    res = t.repeat(repeat=7, number=5)
    average = min(res)/float(5)
    print('Best time across 7 repeats of 5 runs per repeat: {} sec'.format(average))



                     


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    timeit_helper()


if __name__ == '__main__':
    main()
