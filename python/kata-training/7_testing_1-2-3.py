'''
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

'''

def text_editor (string_list):
    # iterate across the length of the list
    # the number that prepends the string will be related to the index 
    # can be implemented with a range/or using the enumerate function
    # must also have a test case for empty list.
    result = []
    for index, string in enumerate(string_list):
        text = f"{index + 1}: {string}"
        result.append(text)
    return result

print(text_editor(["a", "b", "c"]))
print(text_editor([]))

#refactored

def text_editor_2(string_list):
    return [f"{index+1}: {string}" for index, string in enumerate(string_list)]

print(text_editor_2(["a", "b", "c"]))
print(text_editor_2([]))