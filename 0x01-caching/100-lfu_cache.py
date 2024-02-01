#!/usr/bin/env python3
'''100-lfu_cache'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''This class inherits from BaseCaching
    and is a caching system'''
    def __init__(self):
        super().__init__()
        self.cache_order = []
        self.frequency = {}

    def put(self, key, item):
        '''This function assign to the dictionary
        self.cache_data the item value for the key'''
        if key is not None and item is not None:
            if key is not None and item is not None:
                self.cache_data[key] = item
                self.frequency[key] = self.frequency.get(key, 0) + 1
                self.cache_order.append(key)
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.remove_least_frequently_used()

    def get(self, key):
        '''This function must return the
        value in self.cache_data linked to key'''
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.cache_order.remove(key)
            '''You have to update the access order
            for LRU'''
            self.cache_order.append(key)
            return self.cache_data[key]
        return None

    def remove_least_frequently_used(self):
        '''This function removes the leased used
        and usues LRU as a tie breaker if
        2 items have the same frequency'''
        least_frequent_keys = [
                key for key, freq in self.frequency.items()
                if freq == min(self.frequency.values())
                ]
        least_recently_used_key = min(least_frequent_keys,
                                      key=self.cache_order.index)
        del self.cache_data[least_recently_used_key]
        del self.frequency[least_recently_used_key]
        self.cache_order.remove(least_recently_used_key)
        print(f"DISCARD: {least_recently_used_key}")
