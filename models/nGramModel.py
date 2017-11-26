import random
import sys
import json
from musicInfo import *

class NGramModel(object):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable. It is called from the
                  constructors of the NGramModel child classes. This
                  function is done for you.
        """
        self.nGramCounts = {}

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  Returns the string to print when you call print on an
                  NGramModel object. This string will be formatted in JSON
                  and display the currently trained dataset.
                  This function is done for you.
        """
        return self.__class__.__name__ + ':\n' +\
            json.dumps(
                       self.nGramCounts,
                       sort_keys=True,
                       indent=4,
                       separators=(',', ': ')
            )

    def prepData(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: nothing
        Effects:  returns a copy of text where each inner list starts with
                  the symbols '^::^' and '^:::^', and ends with the symbol
                  '$:::$'. For example, if an inner list in text were
                  ['hello', 'goodbye'], that list would become
                  ['^::^', '^:::^', 'hello', 'goodbye', '$:::$'] in the
                  returned copy.
        """
        textCopy = []
        for line in text:
            textCopy.append(['^::^', '^:::^'] + line + ['$:::$'])
        return textCopy

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts
        Effects:  this function populates the self.nGramCounts dictionary.
                  It does not need to be modified here because you will
                  override it in the NGramModel child classes according
                  to the spec.
        """
        pass

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns a bool indicating whether or not this n-gram model
                  can be used to choose the next token for the current
                  sentence. This function does not need to be modified because
                  you will override it in NGramModel child classes according
                  to the spec.
        """
        pass

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. This function does not need to be
                  modified because you will override it in the NGramModel child
                  classes according to the spec.
        """
        pass

    def weightedChoice(self, candidates):
        """
        Requires: candidates is a dictionary; the keys of candidates are items
                  you want to choose from and the values are integers
        Modifies: nothing
        Effects:  returns a candidate item (a key in the candidates dictionary)
                  based on the algorithm described in the spec.
        """
        keys = candidates.keys()
        value = candidates.values()
        cumCount = []
        
        cumValue = 0
        for i in value:
            cumValue += i
            cumCount.append(cumValue)

        num = random.randrange(0, cumCount[-1])
        print num

        for i in range(0, len(cumCount)):
            if cumCount[i] > num:
                return keys[i]
        
        pass

    def getNextToken(self, sentence):
        """
        Requires: sentence is a list of strings, and this model can be used to
                  choose the next token for the current sentence
        Modifies: nothing
        Effects:  returns the next token to be added to sentence by calling
                  the getCandidateDictionary and weightedChoice functions.
                  For more information on how to put all these functions
                  together, see the spec.
        """
        candidates = self.getCandidateDictionary(sentence)
        return self.weightedChoice(candidates)
        pass

    def getNextNote(self, musicalSentence, possiblePitches):
        """
        Requires: musicalSentence is a list of PySynth tuples,
                  possiblePitches is a list of possible pitches for this
                  line of music (in other words, a key signature), and this
                  model can be used to choose the next note for the current
                  musical sentence
        Modifies: nothing
        Effects:  returns the next note to be added to the "musical sentence".
                  For details on how to do this and how this will differ
                  from getNextToken, see the spec.
        """
        allCand = self.getCandidateDictionary(musicalSentence)
        constrainedCand = {}
        pitch = ''
        
        for i in allCand:
            pitch = i[0][0 : -1]
            if pitch in possiblePitches:
                constrainedCand[i] = allCand[i]
            elif i == '$:::$':
                constrainedCand[i] = allCand[i]
        
        # returs True if is not empty
        if self.constrainedCand:
            return self.weightChoice(constrainedCand)
        else:
            pitch = random.choice(possiblePitches) + '4'
            duration = random.choice(NOTE_DURATIONS)
            note = (pitch, duration)
            return note
        pass

        

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    nGramModel = NGramModel()
    
    # weightedChoice
    dic = {'north': 4, 'south': 1, 'east': 3, 'west': 2}
    print dic
    print nGramModel.weightedChoice(dic)

    dic = {('e5', 3): 4, ('f#2', 1): 1}
    print dic
    print nGramModel.weightedChoice(dic)

    # getNextToken
    # getNextNote
    # Since the function getCandidateDictionary is not define in
    # this file, these two functions are tested in the other files
    
    
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    choices = { 'the': 2, 'quick': 1, 'brown': 1 }
    nGramModel = NGramModel()
    print(nGramModel)
