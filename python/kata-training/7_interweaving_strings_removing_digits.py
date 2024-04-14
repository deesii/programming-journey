'''
Your friend Rick is trying to send you a message, but he is concerned that it would get intercepted by his partner. He came up with a solution:

Add digits in random places within the message.

Split the resulting message in two. He wrote down every second character on one page, and the remaining ones on another. He then dispatched the two messages separately.

Write a function interweave(s1, s2) that reverses this operation to decode his message!

Example 1: interweave("hlo", "el") -> "hello" Example 2: interweave("h3lo", "el4") -> "hello"

Rick's a bit peculiar about his formats. He would feel ashamed if he found out his message led to extra white spaces hanging around the edges of his message...

'''

# forward decryption:
    # added digits 
    # split the result message in two (assuming odd number of digits??)
    # every second character (i.e even indices)as part of one word
    # odd indces as part of the second word

# backward operation:
    # instanciate an empty string
    # remove all digits  : use the filter or list comprehension
    # original did a nested loop, but caused issues
    # loop across first set and assign numbers to the letters based on the indexing and create a list of tuples
    # loop across the second set and assign numbers to the letters based on the indexing and create a list of tuples
    # concat the two lists 
    # sort by the index values and do a third loop LOL 


def interweave(str_a, str_b):
    str_a_alphabet = [x for x in str_a if x.isalpha()]
    str_b_alphabet = [x for x in str_b if x.isalpha()]

    print(str_a_alphabet)
    print(str_b_alphabet)

    tuple_a = [(index*2, char) for index, char in enumerate(str_a_alphabet)]
    print(tuple_a)
    tuple_b = [(index*2+1, char) for index, char in enumerate(str_b_alphabet)]
    print(tuple_b)
    tuple_c = tuple_a + tuple_b
    tuple_sorted = sorted(tuple_c, key = lambda char: char[0])
    print(tuple_sorted)
    print("".join(list(char[1] for char in tuple_sorted)))
    return "".join(list(char[1] for char in tuple_sorted))

    # tried the following:
    # for i in range(len(str_a_alphabet)):
    #     result_string += str_a_alphabet[i]
    #     print(f"the result string with the first letter added: {str_a_alphabet[i]} the result is {result_string}")
    #     # for index_2, char_2 in enumerate(str_b_alphabet):
    #     #     if i == index_2:
    #     #         result_string += char_2[index_2]
    #     #         print(f"after adding 2nd letter : {char_2} , the result_string is {result_string}")
    #return result_string

print(interweave('rkjzlcboWF1L5e1mB8UsE5aqtqHjYMR19Ek5pJfohGXSq72cWB', 'lCNt4nA8MzOg8CouhGSQNc33PqAgK35ycYPHy0GQNStlvNRvK'))


#trying to use dictionaries:

def interweave_2(str_a, str_b):
  
    str_a_alphabet = [x for x in str_a if x.isalpha()]
    str_b_alphabet = [x for x in str_b if x.isalpha()]

    print(str_b_alphabet)
    dict_empty = {}
    
    for index, char in enumerate(str_a_alphabet):
        dict_empty[index*2] = char
    
    print(dict_empty)

    for index, char in enumerate(str_b_alphabet):
        dict_empty[index*2+1 ] = char

    print(dict_empty)

    dict_sorted = sorted((dict_empty.items()))
    
    print(dict_sorted)
    print("".join(list(char[1] for char in dict_sorted)))
    return "".join(list(char[1] for char in dict_sorted))

print(interweave_2("hlo", "el"))

print(interweave_2("h3lo", "el4"))