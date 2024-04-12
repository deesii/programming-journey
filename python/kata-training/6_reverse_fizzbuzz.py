'''
FizzBuzz is often one of the first programming puzzles people learn. Now undo it with reverse FizzBuzz!

Write a function that accepts a string, which will always be a valid section of FizzBuzz. Your function must return an array that
contains the numbers in order to generate the given section of FizzBuzz.

Notes:

If the sequence can appear multiple times within FizzBuzz, return the numbers that generate the first instance of that sequence.
All numbers in the sequence will be greater than zero.
You will never receive an empty sequence.
Examples
reverse_fizzbuzz("1 2 Fizz 4 Buzz")        -->  [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz")  -->  [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")              -->  [9, 10]

'''

# if there is a number
# find the index of this number
# I know length of the array
# return the number 


def reverse_fizzbuzz(fizzbuzz_string):
    # Fizz is a multiple of 3
    # Buzz is a multiple of 5
    # FizzBuzz is a multiple of 3 and 5
    
    # generate the first instance of that sequence --> incrementing sequentially from n = 1 upwards

    # turn your string into list with the whitespaces removed
    # then loop through your list, making any string numbers actual integers
    # tuple with index ??  / dictionary with index ??
    
    list_fizzbuzz = fizzbuzz_string.split()
    # return [(i, str) for i, str in enumerate(list_fizzbuzz) if int(str)]

    # numbers = "1234567890"
    # new_list = []
    # for str in list_fizzbuzz:
    #     if any(i for i in str if i in numbers): 
    #         new_list.append(int(str))
    #     else:
    #         new_list.append(str)
    
    # return new_list # new list now has made all numbers integers, whereas has kept the others as strings
    
    # tackle if you know the length of the array, and one of the numbers:

    
    new_list = []
    for i, str in enumerate(list_fizzbuzz):
        if str.isdigit():  # using isdigit as a string method / can refactor as the any() not needed here  # if any(i for i in str if i.isdigit()):
            tuple = (i,int(str))
            new_list.append(tuple)
            break
    
    if len(new_list) > 0:
        len_of_array = len(list_fizzbuzz)
        print(f"the length of the array is : {len_of_array}")
        print(f"the first instance of a number is at index: {new_list[0][0]}")
        print(f"the first instance of a number is: {new_list[0][1]}")
        
        #list of numbers including the number found :
        list_num_including_num_found = [i for i in range(new_list[0][1], new_list[0][1] + len(list_fizzbuzz) - new_list[0][0])] # had to adjust this (originally + 1)
        list_num_before_num_found = [i for i in range(new_list[0][1] - new_list[0][0]  , new_list[0][1])]
    
        return list_num_before_num_found + list_num_including_num_found
    
    elif fizzbuzz_string == "Fizz Buzz":
        return [9, 10]
    elif fizzbuzz_string == "Fizz":
        return [3]
    elif fizzbuzz_string == "Buzz":
        return [5]
    elif fizzbuzz_string == "FizzBuzz":
        return [15]
    elif fizzbuzz_string == "Buzz Fizz":
        return [5, 6]
        



print(reverse_fizzbuzz("1 2 Fizz 4 Buzz"))

print(reverse_fizzbuzz("Fizz 688 689 FizzBuzz"))


    # learnings :
        # hello = filter(lambda x: x == "Fizz", list_fizzbuzz) , practice with the filter function which I didnt use in the end. 
        # # hello is an iterable therefore can loop through it 
        # return [x for x in hello] : a very long approach which you can work with list comprehension (much more readable): [x for x in list_fizzbuzz if x == "Fizz"]
        # list concatination 
        # using the any function --> returns True for if any iterator returns True
        # .isdigit() string method as an alternative to the if x in num where num = "0123456789"
        # solutions : using a dictionary to cover a lot of elif statements. 

                # fizzbuzz = {
                #     'Fizz': [3], 
                #     'Buzz': [5], 
                #     'FizzBuzz': [15], 
                #     'Fizz Buzz': [9, 10], 
                #     'Buzz Fizz': [5, 6]
                #     }

                # return fizzbuzz[fizzbuzz_string]

                #simpler way for making the list with a numbers in it:
                    # for i in range(len(s)):
                        # if s[i].isdigit():
                        #     start = int(s[i]) - i
                        #     return list(range(start, start + len(s)))