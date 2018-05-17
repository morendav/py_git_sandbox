#######################################
# HangMan Game
# Date: 05.16.2018
#
#   This project will be a hangman game that can be played by a human user (or robot ai who has accumulated sufficient english proficiency)
#######################################

#######################################
###     CodeBlock: Initialize Variables
###           & import modules
#######################################
#   Import modules
import os
import random
from setuptools import setup
#   Init Var
#curDir = os.path.abspath(os.path.dirname(__file__))                            ###EnvSpecific: Uncomment for Production
curDir = "/Users/z001mc0/IAE/Dev/Python/StudyProjects"                          ###EnvSpecific: Uncomment for AtomDebugging
f = open(curDir + "/library/RandWordList.txt",'r')
randWorkList=[]
guessHist=[]

#######################################
###     CodeBlock: Project Functs
#######################################
#   Function: Read from fileObj, remove the 'characters & the trailling /n regex
def readFilenoHeaders (fileObj,outputArray):
    for line in fileObj:
        if not line.startswith("#"):
            #print line,                                                        ###DebugPoint: Prints current read line from file
            #print tempvar                                                      ###DebugPoint: Prints current read line from file
            tempvar = line.replace('"', '').strip()     #line read brings in '' & /n characters for each line, this will strip the /n and remove the ' characters
            outputArray.extend([tempvar])
    return outputArray

#   Establish Game Parameters: Number of tries and Secret word
randWordList = readFilenoHeaders (f,randWorkList) #read from the file, remove headers etc from the file
mysteryWord = randWordList[random.randint(0, len(randWorkList)-1)] #establish the secret word based
mysteryWord = mysteryWord.lower() # standard all text will be lower case
mystLength = len(mysteryWord)
discLetters = 0 #tracks number of correct characters discovered in the word, will count multiples individually
maxTries = 10
# print("Mystery word is %s characters long..." % (mystLength))
guessWord = "_" * mystLength
print("Your Mystery Word length is %s characters: \n%s" % (len(guessWord),guessWord))

#######################################
###     CodeBlock: Begin Rounds
#######################################
for it in range(maxTries):
    guess = raw_input("What is your Guess? ")
    guess = guess.lower() # standard all text will be lower case
    ### Conditionals for invalid scenarios
    if guess in guessHist:
        print("%s has already been guessed!\n" % (guess))
        continue
    if len(guess) != 1:
        print("%s is an invalid guess!\n" % (guess))
        continue
    guessHist.extend([guess])   #Add current guess to guess history list
    ### Conditionals for match vs no match
    if guess in mysteryWord:
        matchInd = [pos for pos, char in enumerate(mysteryWord) if char == guess]   ##Return array of indecies where match occurred
        ### Replace missing letters with correct guesses
        #       for each match for current guess, in the mysteryword,
        #       replace that guess word value "_" to be the current guess
        for ind in matchInd:
            guessWord = guessWord[:ind] + guess + guessWord[ind+1:]
        discLetters+=len(matchInd)
        print("Your guesses so far are: %s\nYour word is: %s\n" % (guessHist,guessWord))
        #print("%s Was Found %s Times" % (guess,len(matchInd))) #ebugPoint: prints out match & count of match per round
    else:
        print("%s Was not found" % (guess))
    if discLetters == mystLength:
        print("winner winner chicken dinner! You guessed the correct word!\nThe word is: %s" % (mysteryWord))
        break
else:
    print("You did not guess the word, sorry dude.\nThe Correct word was: %s" % (mysteryWord))
