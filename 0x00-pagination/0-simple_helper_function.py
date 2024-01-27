#!/usr/bin/env python3
"""
0-simple_helper_function
"""


def index_range(page, page_size):
    '''This function takes two integer arguments page and page_size
    and returns a tuple of size two containing a start
    index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters'''
    if page < 1 or page_size < 1:
        raise ValueError("Page size and page must be greater than one.")
    starting_index = (page - 1) * page_size
    ending_index = page * page_size
    return (starting_index, ending_index)
