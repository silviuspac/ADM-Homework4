import numpy as np
from tqdm import tqdm


class BloomFilter():
    
    def __init__(self, n, m, k):
        self.n = n
        self.m = m
        self.k = k
        
        self.bloom_filter = np.zeros(self.m)
        
        self.n_elements = 0

        self.n_duplicates = 0
    
    # hash function 1, simply multiply ASCII 
    def hash_1(self, string):
        ord_list = [ord(c) for c in string]
        res = 1
        for elem in ord_list:
            res *= elem
        return res
    
    # hash function 2, radix = 37
    def hash_2(self, string):
        radix = 37
        e = 1
        ord_list = [ord(c) for c in string]
        res = 0
        for elem in ord_list:
            res += elem*e
            e = e*radix
        return res
    
    # Calculates k number of hashes using theorem in:
    # Less Hashing, Same Performance: Building a Better Bloom Filter
    def my_hash(self, string):
        
        hash_array = []
        hash1 = self.hash_1(string)
        hash2 = self.hash_1(string)
        
        for i in range(self.k):
            hash_array.append(abs((hash1 + i * hash2 + i**2) % self.m))

        return hash_array
    
    # Add a password to the bloom filter
    def add_to_bloom(self, string):
        
        hash_array = self.my_hash(string)
        
        for idx in hash_array:
            if not self.bloom_filter[idx]:
                self.bloom_filter[idx] = 1
            
        self.n_elements += 1
        
    
    # Check if a password may be in the filter or not
    def check_pass(self, string):
        
        hash_array = self.my_hash(string)
        
        for idx in hash_array:
            if not self.bloom_filter[idx]:
                #print("The password is NOT in the filter")
                return
            
        #print("The password may be in the filter")
        self.n_duplicates += 1
