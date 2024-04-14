'''
You are going to be given a word. Your job will be to make sure that each character in that word has the exact same number of occurrences. You will return true if it is valid, or false 
if it is not.

For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"

The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.

Examples
"abcabc" is a valid word because "a" appears twice, "b" appears twice, and"c" appears twice.
"abcabcd" is NOT a valid word because "a" appears twice, "b" appears twice, "c" appears twice, but "d" only appears once!
"123abc!" is a valid word because all of the characters only appear once in the word.

'''

def count_char(word):
    #initialise the list to store the keys
    #initialise an empty dictionary to store the count of the letters 
    #iterate through the string (ensuring all are .lower) and increase the count if it exists in the dictionary
    #otherwise will create a new dictionary key value pair
    #at the end of the loop through the dictionary and put into the list to store the keys
    #use set to output a unique value
    #if len = 1 then it means all the characters have the same value

    # refactored no need to store_values
    # store_values = []
    char_count = {}
    for char in word.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return len(set(char_count.values())) == 1

    # refactored from 
    # for key in char_count:
    #     store_values.append(char_count[key])
    # return len(set(store_values)) == 1


#refactored with the list comprehension and using .count

def count_char_2(word):
    word  = word.lower()
    return len(set(word.count(char) for char in word)) == 1

print(count_char("abcabc"))

print(count_char("abcabcd"))

print(count_char("123abc!"))



    
# learnings:
    # length of set class  
    # create a list from the dict_values class using list() or [x for x in char_count]
    # this can be applied to the map and filter function as it produces map object and filter object respectively
    # using .count and list comprehension to achieve the same as storing in a dictionary.
