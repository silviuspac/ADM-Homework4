## Implementation of Counting Sort only for positive numbers.

import numpy as np
import re

def CountingSort_num(A):

    # defining an auxiliary array
    
    size = max(A)  
    aux = np.zeros(size+1, dtype=int) 
    
    # to see the occurrency of each element to the respective index
    
    for i in A:
        aux[i] += 1

    # defining the output
        
    sort = []   
    for j in range(size+1):
        sort.extend([j]*aux[j]) # showing all the sorted elements
        
    return sort



## Implementation of Counting Sort to get the ordered list of letters.

def CountingSort_let(letters):
    
    alphabet_l = string.ascii_lowercase
    alphabet_u = string.ascii_uppercase
    
    # Unicode value for each letter

    unicode_l = []
    unicode_u = []

    for i in alphabet_l:
        unicode_l.append(ord(i))
    for j in alphabet_u:
        unicode_u.append(ord(j))

    # creating map to get in order the Unicode values associated to upper and lower case (example: AaBbCc...).
    # initializing the alphabetical order

    unicode_map = []

    for p in zip(unicode_u, unicode_l):
        for code in p:
            unicode_map.append(code)

    # creating a dictionary to have an index for each unicode

    dict_alpha = {code:i for i, code in enumerate(unicode_map)}

    # creating the reverse of the dictionary

    dict_alpha_rev = {ind:code for code, ind in dict_alpha.items()}

    # we define an auxiliary array

    aux = np.zeros(len(dict_alpha), dtype=int)

    # taking the input, we have to convert it into Unicode values

    num = []
    for i in letters:
        num.append(ord(i))

    # Now, as we made for the CountingSort_num,
    # we check the occurrences of each character (from the input)
    # and we set values of aux

    for i in num:
        aux[dict_alpha[i]] += 1

    sorted_letters = []

    for i in range(len(aux)):
        sorted_letters.extend([chr(dict_alpha_rev[i])]*aux[i])

    return sorted_letters



## Implementation of Counting Sort to get the ordered list of words.


    
