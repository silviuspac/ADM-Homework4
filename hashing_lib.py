import BitVector


class BloomFilter():

	# Implementation of a simple bloom filter
	# Precalculated p, m, n and k needed
    
	def __init__(self, m, k):

		# Define global variables
		# m = size of the bloom filter
		# k = # of hashing functions

		self.m = m
		self.k = k

		# bit vector of 0 and 1
		self.bloom_filter = BitVector.BitVector(size = m)

		# number of elements added in the filter
		self.n_elements = 0

		# numberof probably duplicates found
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
	    
	    # hash_array is the array of the k hash dunctions
	    hash_array = []

	    hash1 = self.hash_1(string)
	    hash2 = self.hash_2(string)
	    
	    for i in range(self.k):
	        hash_array.append((hash1 + i * hash2 + i**2) % self.m)

	    return hash_array

	# Add a password to the bloom filter
	def add_to_bloom(self, string):
	    
	    # calculatate the k hash of the string
	    hash_array = self.my_hash(string)
	    
	    # iterate on the hash functions and set the bit to 1
	    for idx in hash_array:
	        if not self.bloom_filter[idx]:
	            self.bloom_filter[idx] = 1

	    self.n_elements += 1

	    

	# Check if a password may be in the filter or not
	def check_in_bloom(self, string):
	    
	    # calculatate the k hash of the string
	    hash_array = self.my_hash(string)
	    
	    # iterate and controll the state of the bit. If 0 the pass is NOT in the filter
	    for idx in hash_array:
	        if not self.bloom_filter[idx]:
	            #print("The password is NOT in the filter")
	            return
	        
	    #print("The password may be in the filter")
	    self.n_duplicates += 1


	# Print some stats of the filter
	def print_stats(self):
		print('Number of elements: ', self.n_elements)
		print('Number of probably duplicates: ', self.n_duplicates)
		print('Size of the filter: ', self.m)
		print('Number of hashing functions: ', self.k)



