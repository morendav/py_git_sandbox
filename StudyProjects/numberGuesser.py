#######################################
# Random number guessing
# Date: 05.16.2018
#
#   This project will assign a random number to a varaible, then in a loop iterate until the random number is guessed
#######################################

#######################################
###     CodeBlock: Initialize Variables
###           & import modules
#######################################
import random
import math

randomNo = random.randint(0, 500)
#guess = input('What is your first guess? ')                                    ###         comment this section if you prefer to use a hardcoded first guess
guess = 1                                                                       ###         comment this section if you prefer to use user defined first guess
i = 1
maxTries = 10
guessHist=[guess]


#######################################
###     CodeBlock: Calculate Difference
#######################################
### Old Block to adjust guess, was optimized in the while loop that follows...
# while (randomNo - guess) != 0 and i < 50:
#     #Adjust the guess to a new value based on polarity and magnitude of difference
#     if (randomNo - guess)<0 and abs(randomNo - guess)>10:
#         guess-=10
#         i+=1
#     elif (randomNo - guess)<0 and abs(randomNo - guess)<10:
#         guess-=1
#         i+=1
#     elif (randomNo - guess)>0 and abs(randomNo - guess)>10:
#         guess+=10
#         i+=1
#     elif (randomNo - guess)>0 and abs(randomNo - guess)<10:
#         guess+=1
#         i+=1
#     #Append the new guess to our guess history array
#     guessHist.extend([guess])

### New Block to adjust guess, optimized and faster!
while (randomNo - guess) != 0 and i < maxTries:
    #Adjust the guess to a new value based on polarity and magnitude of difference
    diffMag = math.floor(math.log10(randomNo - guess))  # calculates the magnitude of the difference between last guess and mystery number
    if (randomNo - guess)<0:
        guess = guess - math.pow(10,diffMag)
        i+=1
    else:
        guess = guess + math.pow(10,diffMag)
        i+=1
    #Append the new guess to our guess history array
    guessHist.extend([guess])


if (randomNo - guess) == 0:
    print("The random number was: %s and it was guessed after %s attempts"%(randomNo,i))
elif (randomNo - guess) != 0:
    print ("The random number was not guessed in %s tries, correct answer was %s" % (i, randomNo))
print (repr(guessHist))
