array = [642, 954, 936, 968]



# 1. number of characters which were not the same as the same index in the other word [length of string is the same]
# 2. making the letters all backwards 
# 3. string capitalise each word 
# 4. string number of consonants 

def isTriangular(num):

    # Base case
    if (num < 0):
        return False

    # A Triangular number must be 
    # sum of first n natural numbers
    sum, n = 0, 1

    while(sum <= num): 
    
        sum = sum + n
        if (sum == num):
            return True
        n += 1

    return False

# Driver code
n = 55
if (isTriangular(n)):
    print("The number is a triangular number")
else:
    print("The number is NOT a triangular number")


print(isTriangular(642))
print(isTriangular(654))
print(isTriangular(978))
print(isTriangular(936))

# Aman runs towards North for 10 m, turns left and runs another 20 m.He turns right and walks slowly for 10 m. Then he again turns right, walks another 50 m and stops.



# In which direction is he with respect to his initial position?

N: 10
