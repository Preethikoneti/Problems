# This checks for Anagram without using dictionary approach.
# First convert to lower case(lower(), then remove spaces(replace(" ","") and then punctuations(translate(None, string.punctuations).

import string

def anagram(s1,s2):
    s1 = s1.lower().replace(" ","").translate(None, string.punctuation)
    s2 = s2.lower().replace(" ","").translate(None, string.punctuation)
    
    return sorted(s1) == sorted(s2)
