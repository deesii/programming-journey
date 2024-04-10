'''
6kyu

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. 
The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

'''

def two_sum(numbers,target):
    # when there is an array of two, the answer will be the target
    # it will return the index within a list/tuple for these two numbers that when added give the target number
    
    # instanciate the variable for storing the "sum remaining"
    # iterate across the length of the array
    # for each number :
        # and carry out the sum target-number[i] and store in a variable outside loop
        # iterate across the remainder of the array
        #   minus from the variable to see if it equal 0
                # if it does not then you iterate to the next number and repeat 
                # else it does find another number which it equals 0
                    # you need to store the index of the number which you have currently "on"
                    # you need to store the index of the number which you have minused to make it 0        

    # sum_remaining = 0
    # index_first = 0
    # index_second = 0
    
    for index, num in enumerate(numbers):
        sum_remaining = target - num
        for index2, num2 in enumerate(numbers[index+1:]): #changed this, because did not understand the start = 0 etc 
            if sum_remaining - num2 == 0:
                index_first = index
                #print(index_first)
                index_second = index2 + index + 1 # error here , was returning the index of the shortened array to start with
                #print(index_second)
                print(f"the index of the first number is {index_first}, and the index of the second number is {index_second}")
                return (index_first, index_second)

print(two_sum([5,4,9,8,2] , 10))
print(two_sum([1,2,3] , 4))
print(two_sum([1234,5678,9012], 14690,))
print(two_sum([2, 2, 3], 4))

#learnings: 
    # knowing how to use enumerate functions i,n in enumerate (array, start = what number)
    # indexing and iterating in a nest for loops requires a lot of care and attention
    # using print statements and also debugging has been key to understanding the above learnings
    # from other solutions:
        # use of range()
            # def two_sum(numbers, target):
            #     for i in range(len(numbers)):
            #         for j in range(i+1, len(numbers)):
            #             if (numbers[i] + numbers[j]) == target:
            #                 return [i, j]


            # class range(stop)
            # class range(start, stop, step=1)


        # use of dictionaries, with key value pairs:
            # def two_sum(nums, target):
                # d = {}
                # for i, num in enumerate(nums):
                #     diff = target - num
                #     if diff in d:
                #         return [d[diff], i]
                #     d[num] = i