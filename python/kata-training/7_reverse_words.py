'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

'''

def reverse_words(string):
    # split 
    # iterate across the length of the string and slice each iterator
    # join again 
    string_list = string.split(" ")
    print(string_list)
    return " ".join([word[::-1] for word in string_list])



print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))

# learnings: 
    # practice with the reverse string slice
    # using the split with the deliminator of " " to ensure capturing of whitespace more than single whitespace!  