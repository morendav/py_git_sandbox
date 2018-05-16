#######################################
# Project: Random number guessing
# Date: 05.16.2018
#
#   This project will assign a random number to a varaible, then in a loop iterate until the random number is guessed
#######################################

###     CodeBlock: Initialize Variables & import modules      ###
import random
randomNo = random.randint(0, 100)
guess = 50
i = 0
guessHist=[guess]

###     CodeBlock: Calculate Difference      ###
while (randomNo - guess) != 0 and i < 10:
    #Adjust the guess to a new value based on polarity and magnitude of difference
    if (randomNo - guess)<0 and abs(randomNo - guess)>10:
        guess-=10
        i+=1
    elif (randomNo - guess)<0 and abs(randomNo - guess)<10:
        guess-=1
        i+=1
    elif (randomNo - guess)>0 and abs(randomNo - guess)>10:
        guess+=10
        i+=1
    elif (randomNo - guess)>0 and abs(randomNo - guess)<10:
        guess+=1
        i+=1
    #Append the new guess to our guess history array
    guessHist.extend([guess])


print ('The random number was: ' + repr(guess) + '\nNumber of guesses: ' + repr(i))
print (repr(randomNo))
print (repr(guessHist))
