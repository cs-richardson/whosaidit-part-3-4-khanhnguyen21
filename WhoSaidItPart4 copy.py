# WhoSaidIt, part 3 & 4
# A program that will predict a piece of text's author, either Austen or Shakespeare.
# By Khanh Nguyen
# -----
# Dictionary: https://www.w3schools.com/python/python_dictionaries.asp
# Punctuation removal code: https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate/34294022

import math
import string

translator=str.maketrans('','',string.punctuation)

# get_score
# -----
# This function takes a word and a dictionary of
# word counts, and it generates a score that
# approximates the relevance of the word
# in the document from which the word counts
# were generated. The higher the score, the more
# relevant the word.
#
# In many cases, the score returned will be
# negative. Note that the "higher" of two
# negative scores is the one that is less
# negative, or the one that is closer to zero.
def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase

def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.

def get_counts(filename):
    words = []
    resultDict = {"_total":0}
    file = open(filename,"r")
    for line in file:
        line = line.translate(translator)
        words = line.split()
        for word in words:
            if word.isalpha():
                word = normalize(word)
                if word in resultDict:
                    resultDict[word] = resultDict[word] + 1
                else:
                    resultDict[word] = 1
                resultDict["_total"] = resultDict["_total"] + 1
      
    file.close()
    return resultDict

# getCountP
# -----
# Calculate the total score of the text respective to the one person

def getScorePerson(text, dictionary):
    total = 0
    words = []
    text = text.translate(translator)
    words = text.split()
    for word in words:
        word = normalize(word)
        total = total + get_score(word, dictionary)
    return total

# Get the word count for each literature piece /
# establishing a dictionary for each author

shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride_and_prejudice.txt")

print('Enter some text and I will predict whose its author is: Austen or Shakespeare.')
textInput = input('Your text here: ')
scoreAusten = getScorePerson(textInput, austen_counts)
scoreSp = getScorePerson(textInput, shakespeare_counts)

if scoreAusten > scoreSp:
    print('I think it was written by Jane Austen')
elif scoreSp > scoreAusten:
    print('I think it was written by Shakespeare')
else:
    print('IDK :<')






























