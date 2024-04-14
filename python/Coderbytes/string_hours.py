import math

def StringChallenge(num):

  # num input is the number of minutes
  # divide num by 60 and floor to make the number of minutes, any remainder is minutes
    hours = math.floor(num/60)
    minutes = num - (hours * 60)

    return f"{hours}: {minutes}"


print(StringChallenge(126))

import math
def StringChallenge(num):

  # num input is the number of minutes
  # divide num by 60 and floor to make the number of minutes, any remainder is minutes
  hours = math.floor(num/60)
  minutes = num - (hours * 60)

  return str(hours) + ":" + str(minutes)
  

# keep this function call here 
print(StringChallenge(input()))