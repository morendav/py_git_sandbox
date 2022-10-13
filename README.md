# Python

## Description
Projects developed to solve simple problems in an educational sandbox


## ./StudyProjects/
Brief description of complete projects

### numberGuesser.py
* Description: script that generates a random number, begins with an initial guess, and iterates until the correct number is guessed by the program.
* Optimizations: introduce a degree of magnitude of the guess-number difference to adjust itself per iteration && removed redundant if conditions to improve run time
* Dependencies: random, math

### hangMan.py
* Description: hangman game written in python
* Optimizations: nest loops aren't 'pythonic'. Doesn't draw a fun little hangman, just counts down guesses
* Dependencies: os, random, setuptools
  * pulls random words from ./library/RandWordList.txt

### graphMachine.py
* Description: Live plot for newtonian body in motion under second order (acceleration) and first order (velocity) terms. Fun plot! 
* Optimizations: make it interactive
* Dependencies: numpy, scipy, matplotlib
    * pulls random words from ./library/RandWordList.txt
