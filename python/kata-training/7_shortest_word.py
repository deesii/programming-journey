'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''

# split into an array
# len(element) in the array
# use min function

def find_short(string):
    string_list = string.split()
    print(string_list)
    list_tuples = [(index, string, len(string)) for index , string in enumerate(string_list)]
    print(list_tuples)
    list_tuples_sorted = sorted(list_tuples, key = lambda word: word[2])
    return list_tuples_sorted[0][2]

print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("turns out random test cases are easier than writing out basic ones"))
print(find_short("i want to travel the world writing code one day"))

def find_short_2(string):
    string_list=string.split()
    return min([len(word) for word in string_list])

print(find_short_2("bitcoin take over the world maybe who knows perhaps"))
print(find_short_2("turns out random test cases are easier than writing out basic ones"))
print(find_short_2("i want to travel the world writing code one day"))

# revision of the min 
# list comprehension
    # return min(len(x) for x in s.split()) -- > threfore do not need []