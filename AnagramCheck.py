# Anagram check using dictionary approach.

def anagram(string1,string2):
    
    # Convert the strings to lower case using lower() and remove the spaces using replace()
    # Note that if you want to remove punctuations you could use .translate(None, string.punctuations)
    string1 = string1.lower().replace(" ","")
    string2 = string2.lower().replace(" ","")
    
    # Check for the length of the strings, if unequal return False
    if len(string1) != len(string2):
        return False
    
    # Create an empty dictionary to hold character and corresponding occurence count from both dictionaries
    c = {}
    
    # Add all characters from string 1 as keys and store corresponding occurence counts.
    for letter in string1:
        if letter in c.keys():
            c[letter] += 1
        else:
            c[letter] = 1
    
    # Follow the same process for string 2
    # If the same letter occurs in string 1 then subtract count by one, else set it to one.
    for letter in string2:
        if letter in c.keys():
            c[letter] -= 1
        else:
            c[letter] = 1
                
    #If all the count values are zero then both the strings have same letters and occurences, so return True else False
    for key in c.keys():
        if c[key] != 0:
            return False
        return True
