#!/usr/bin/env python3
'''3-lru_cache'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''This class inherits from BaseCaching
    and is a caching system'''
    def __init__(self):
        super().__init__()
        self.cache_order = []
        self.cache_data = {}

    def put(self, key, item):
        '''This function assign to the dictionary
        self.cache_data the item value for the key'''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            self.cache_data[key] = item
            self.cache_order.append(key)
            if len(self.cache_order) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_order.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        '''This function must return the
        value in self.cache_data linked to key'''
        if key is not None and key in self.cache_data:
            self.cache_order.remove(key)
            self.cache_order.append(key)
            return self.cache_data[key]
        return None
