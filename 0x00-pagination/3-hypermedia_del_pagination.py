#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]
            return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
                    }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''This function returns a dictionary with the following
        key-value pairs: index, next index, page_size, data'''
        indexed_dataset = self.indexed_dataset()

        '''Start by handling index == None'''
        if index is None:
            index = 0
        '''Use the assert method to assert whether the index is valid'''
        assert 0 <= index < len(indexed_dataset), "Index out of range"
        '''This code fetches the current page data to handle
        any potential deletions'''
        data = []
        next_index = index
        for i in range(page_size):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1
        '''return the th dictionary with the required info'''
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data}
