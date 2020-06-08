# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:51:44 2018

@author: *
"""
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    lettersNeeded = []
    lettersLeft = int(len(secretWord))
    for i in secretWord:
        lettersNeeded += i
    for i in lettersNeeded:
        if i not in lettersGuessed[::]:
            return False
        else:
            lettersLeft -= 1
            if lettersLeft == 0:
                return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    displayString = ""
    for i in secretWord:
        if i in lettersGuessed:
            displayString += i
        else:
            displayString += "_ "
    return displayString

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'
    ,'p','q','r','s','t','u','v','w','x','y','z']
    availLets = ""
    for l in lettersGuessed:
        if l in abc:
            abc.remove(l)
    for l in abc:
        availLets += l
            
    return availLets


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    numTries = 8
    lettersGuessed = []
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    while numTries > 0:
        print('-----------')
        print('You have ' + str(numTries) + ' guesses left.')
        print('Available Letters: ' + str(getAvailableLetters(lettersGuessed)))
        guess = input('Please guess a letter: ')[0]
        if guess in secretWord:
            if guess not in str(getAvailableLetters(lettersGuessed)):
                print("Oops! Not a letter or you've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                lettersGuessed += guess
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print('-----------')
                    return(print('Congratulations, you won!'))
                else:
                    continue
        else:
            if guess not in str(getAvailableLetters(lettersGuessed)):
                print("Oops! Not a letter or you've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                lettersGuessed += guess
                numTries -= 1
                print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
    print('-----------')
    return(print('Sorry, you ran out of guesses. The word was: ' + str(secretWord) + '.'))

if __name__ == '__main__':
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)