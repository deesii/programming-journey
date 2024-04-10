'''
You will be given an array of strings. The words in the array should mesh together where one or more letters at the end of one word 
will have the same letters (in the same order) as the next word in the array. But, there are times when all the words won't mesh.

Examples of meshed words:

"apply" and "plywood"

"apple" and "each"

"behemoth" and "mother"

Examples of words that do not mesh:

"apply" and "playground"

"apple" and "peggy"

"behemoth" and "mathematics"

If all the words in the given array mesh together, then your code should return the meshed letters in a string. 
You should return the longest common substring. You won't know how many letters the meshed words have in common, but it will be at least one.

If any pair of consecutive words fails to mesh, your code should return "failed to mesh".

Input: An array of strings. There will always be at least two words in the input array.

Output: Either a string of letters that mesh the words together or the string "failed to mesh".

Examples
#1:

["allow", "lowering", "ringmaster", "terror"] --> "lowringter"
because:

the letters "low" in the first two words mesh together
the letters "ring" in the second and third word mesh together
the letters "ter" in the third and fourth words mesh together.
#2:

["kingdom", "dominator", "notorious", "usual", "allegory"] --> "failed to mesh"
Although the words "dominator" and "notorious" share letters in the same order, the last letters of the first word don't mesh with the first letters of the second word.

'''

def word_mesh(array):
    #iterate across the words one at a time
    # then iterate across splices of the first word and compare the equivalent of the splice reversed for the second word 
    # if it equals the same letter, store in a string variable
        # compare the next letter along with the equivalent index along 
        # splice?? compare first_word[n:] with second_word[:n]
        # if it is the same, then increase the value of n, and store the new splice to the variable
        # iterate until it is not the same, and loop across the next word doing the same
        # use any() ?? 

    final_string = []
    i = 0
    for index, word in enumerate(array):
        if index + 1 < len(array):
            # if word == array[index + 1]:
            #     print(f"the first word : {word[-i:]}, the second word: {array[index + 1]}")
            #     final_string.append(word)
            # else:
            word_store= []
            for i in range(1,len(word)+1):
                print(f"the first word : {word[-i:]}, the second word: {array[index + 1][:i]}")
                if (word[-i:]) == (array[index + 1][:i]):
                    word_store.append(word[-i:])
                    print(f"the first word :{word[-i:]}")
                    print(f"the second word: {array[index + 1][:i]}")
                        #tests show this fails... due to initial breaking when a match found , especially challenging when first letter matched, but for longer words, also there was a match
                    print(f"the same words in the word store are {word_store}") # therefore created a wordstore and sorted by longest word with tuples.

            if len(word_store) > 0:
                sorted_word_store = sorted([(word,len(word)) for word in word_store], key = lambda word : word[1], reverse= True) # not necessary, as I just need to reverse the word_store list.
                # i.e final_string.append(word_store[-1])
                final_string.append(sorted_word_store[0][0])

                    #issues here when you have the same letter 
    if len(final_string) != len(array)-1:
        return "failed to mesh"
    else:
        return "".join(final_string)


print(word_mesh (["allow", "lowring", "ringmaster", "terror"]))
print(word_mesh (["kingdom", "dominator", "notorious", "usual", "allegory"]))
print(word_mesh (["dominator","notorious"]))
print(word_mesh(['breakfastlunchdinner', 'dinnertimebell', 'ellipticalcirclesquare', 'ellipticalcirclesquare', 'squaredtripled', 'pledgedaliegience']))
print(word_mesh(['abbabbabba', 'abbacccdddeee', 'deeedledeedledum', 'dumdum', 'umbrellas', 'llasaapsopuppy', 'puppydogtails']))
print(word_mesh(['muchbetter', 'terngullkittiwake', 'keeperatthezoo', 'oolongtea']))

#learnings : 
    # the slices values for the start and end of strings
    # using debugging python 
    # importance of knowing when the slice begins and ends , including steping!
    # sorted with lambda function sorting by the 2nd index (by length)
    # sorted can be used with any iterable --> new list with elements sorted
    # careful for range(start, stop, step) : stop is one less than the value