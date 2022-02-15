# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 04:36:25 2022

@author: Samuel Liechty
"""
def trimDictionary(dictionary):
    #initialize list of five letter words
    words_five = []

    #find and store all five letter words from master dictionary
    for i in range(len(dictionary)):
        if len(dictionary[i]) == 6 or (len(dictionary[i]) == 5 and i == len(dictionary) - 1): #check if 6 because of newline character
            words_five.append(dictionary[i][0:5]) #append word without newline character (first 5 chars)
    
    return words_five #returns properly formatted list of all five letter words

def letterDataCollection(dictionary):
    returnThis = []
    
    #initialize data of keys and values
    data = {}
    data['key'] = 'value'
    data['key2'] = 'value2'
    
    for i in range(len(dictionary)): #visit every five letter word
        current_word = dictionary[i] #hold current word
        
        for j in range(len(current_word)): #visit every letter of current word
            letter = current_word[j] #hold current letter of current word
            
            #if a letter is uppercase, make it lowercase
            if letter.isupper():
                letter = letter.lower()
                
            #if a letter is not yet stored, initialize it
            if (letter in data) == False:
                data[letter] = 1
            
            #if letter is already stored, update counter
            else:
                data[letter] += 1
    if "s" in data:            
        data["s"] -= round(348/(6665/data["s"]))
    returnThis.append(data)
    
    #initalize data for char_occurance
    data1 = {}
    data1['key'] = 'value'
    data1['key2'] = 'value2'
    data2 = {}
    data2['key'] = 'value'
    data2['key2'] = 'value2'
    data3 = {}
    data3['key'] = 'value'
    data3['key2'] = 'value2'
    data4 = {}
    data4['key'] = 'value'
    data4['key2'] = 'value2'
    data5 = {}
    data5['key'] = 'value'
    data5['key2'] = 'value2'
    char_occurance = [data1, data2, data3, data4, data5]
    most_common = ["x", "x", "x", "x", "x"]
    most_common_values = [0, 0, 0, 0, 0]

    for i in range(len(char_occurance)):
        for j in range(len(dictionary)):
            current_letter = dictionary[j][i]
            if current_letter not in char_occurance[i]:
                char_occurance[i][current_letter] = 1
            else:
                char_occurance[i][current_letter] += 1
        for j in range(len(dictionary)):
            current_letter = dictionary[j][i]
            if char_occurance[i][current_letter] > most_common_values[i]:
                if not (i == 4 and current_letter == "s"):
                    most_common[i] = current_letter
                    most_common_values[i] = char_occurance[i][current_letter]
    returnThis.append(char_occurance)
    
    return returnThis #returns a list with overall letter data in index 0 and character occurance data in index 1

def baseGrading(dictionary, data):
    #initalize variables
    scored_words_five = {}
    scored_words_five["xxxxx"] = -1

    for i in range(len(dictionary)):
        current_word = dictionary[i]
        word_value = 0
        
        used_letters = []
        for j in range(len(current_word)):
            current_letter = current_word[j]
            if current_letter not in used_letters:
                word_value += data[current_letter]
            
            used_letters.append(current_letter)
            
            if j == len(current_word) - 1 and current_letter == "s":
                word_value -= round(5*data[current_letter]/6)
        
        scored_words_five[current_word] = word_value
    scored_words_five.pop("xxxxx")
    return scored_words_five #returns dictionary of scored words

def extraGrading(dictionary, data, char_occurance):
    #initialize variables
    scored_extra_words_five = {}
    scored_extra_words_five["xxxxx"] = -1

    for i in range(len(dictionary)):
        current_word = dictionary[i]
        word_extra_value = 0
        
        #used_letters = [] #do we penalize for duplicates here?
        for j in range(len(current_word)):
            current_letter = current_word[j]
            word_extra_value += char_occurance[j][current_letter]
            
            if j == 4 and current_letter == "s":
                word_extra_value -= round(5*char_occurance[j][current_letter]/6)
        
        scored_extra_words_five[current_word] = word_extra_value
    scored_extra_words_five.pop("xxxxx")
    return scored_extra_words_five #returns dictionary of scored words by "extra" rubric

def mixedGrading(dictionary, scored_words_five, scored_extra_words_five):
    #initialize variables
    scored_mixed_words_five = {}
    scored_mixed_words_five["xxxxx"] = -1

    for i in range(len(dictionary)):
        current_word = dictionary[i]
        scored_mixed_words_five[current_word] = scored_words_five[current_word] + scored_extra_words_five[current_word]
    
    scored_mixed_words_five.pop("xxxxx")
    return scored_mixed_words_five

def instantWordle(words, scored_base, sol, grade_type):
    wordsCopy = words.copy()
    holdData = letterDataCollection(words)[0]
    
    if sol not in scored_base:
        print("Uh oh, you've inputted a word that does not exist.\nPlease try again and input a valid five-letter word.")
        print(sol)
        return 0
    while True:
        if len(sol) != 5:
            print("Solution must be five letters long")
            sol = input("Input today's five-letter Wordle solution: ")
        else:
            break
    
    guesses = []
    guessesColors = []
    solved = False
    clues = {}
    clues["yellowBlocked"] = []
    clues["yellow"] = {}
    clues["green"] = ["-1", "-1", "-1", "-1", "-1"]
    clues["yellowGuesses"] = {}
    clues["black"] = []
    clues["eliminatedIndices"] = {}
    
    for i in range(6):
        guess = max(scored_base, key=scored_base.get)
        guesses.append(guess)
        scored_base.pop(guess)
        guessColor = ["x", "x", "x", "x", "x"]
        if guess == sol:
            solved = True
            guessesColors.append("GGGGG")
            break
        letters_in = {}
        
        
        guessesColors.append("".join(colorEvaluator(guess, clues, letters_in, sol)[0]))
        
        #filter possibilities out of word list
        j = 0
        for j in range(len(words)):
            word_check = words[j].lower()
            wordQuality = True
            
            for k in range(len(word_check)):
                if clues["green"][k] != "-1" and clues["green"][k] != word_check[k]:
                    wordQuality = False
                    break
                
                if word_check[k] in clues["black"]:
                    wordQuality = False
                    break
                
                if word_check[k] in letters_in:
                    if word_check.count(word_check[k]) < letters_in[word_check[k]]:
                        wordQuality = False
                        break
                
                    
                if word_check[k] in letters_in:
                    breakAgain = False
                    for l in range(i + 1):
                        if guessesColors[l][k].lower() == "y" and guesses[l][k].lower() == word_check[k]:
                            wordQuality = False
                            breakAgain = True
                            break
                    
                    if breakAgain:
                        break
            
            for k in letters_in:
                if k not in word_check:
                    wordQuality = False
                    break
            
            
            if not wordQuality:
                if word_check in scored_base:
                    scored_base.pop(word_check)
                if word_check in wordsCopy:
                    wordsCopy.remove(word_check)
        
                    
                    
                    
        #regrade words
        if grade_type.lower() == "b":
            reGrade = []
            for key_ in scored_base.keys():
                reGrade.append(key_)
            letterData_ = holdData
            charOccurance_ = letterDataCollection(reGrade)[1]
            scored_base = baseGrading(reGrade, letterData_)
        elif grade_type.lower() == "e":
            reGrade = []
            for key_ in scored_base.keys():
                reGrade.append(key_)
            letterData_ = holdData
            charOccurance_ = letterDataCollection(reGrade)[1]
            scored_base = extraGrading(reGrade, letterData_, charOccurance_)
        elif grade_type.lower() == "m":
            reGrade = []
            for key_ in scored_base.keys():
                reGrade.append(key_)
            letterData_ = holdData
            #letterData_ = letterDataCollection(reGrade)[0]
            charOccurance_ = letterDataCollection(reGrade)[1]
            temp_base = baseGrading(reGrade, letterData_)
            temp_extra = extraGrading(reGrade, letterData_, charOccurance_)
            scored_base = mixedGrading(reGrade, temp_base, temp_extra)
            
                
    if solved:
        print("Puzzle solved in "+str(len(guesses)) + " guesses!")
        print("Here is the line:")
        for q in range(len(guesses)):
            print(guesses[q].upper() + " - " + guessesColors[q])
            
    else:
        print("Failed to solve puzzle.")
        print("This was the line:")
        for q in range(len(guesses)):
            print(guesses[q].upper() + " - " + guessesColors[q])
    
    if solved:
        return len(guesses)
    else:
        return 0

def colorEvaluator(guess, clues, letters_in, sol):
    guessColor = ["x", "x", "x", "x", "x"]
    #First for-loop responsible for evaluating a guess
    for j in range(len(guess)):
        #is this letter in the word and in the right spot?
        if guess[j] == sol[j]:
            clues["green"][j] = sol[j]
            guessColor[j] = "G"
            if guess[j] not in letters_in:
                letters_in[guess[j]] = 1
            else:
                letters_in[guess[j]] += 1
    
    #Second for-loop responsible for evaluating a guess
    j = 0
    for j in range(len(guess)):
        #is this letter not in the guess? add it to the blacklist
        if guess[j] not in sol and guess[j] not in clues["black"]:
            clues["black"].append(guess[j])
            guessColor[j] = "B"
        elif guess[j] not in sol:
            guessColor[j] = "B"
        
        if guess[j] in sol and guess[j] != sol[j]:
            
            if guess[j] not in clues["eliminatedIndices"]:
                clues["eliminatedIndices"] = []
                clues["eliminatedIndices"].append(j)
                guessColor[j] = "Y"
            else:
                clues["eliminatedIndices"].append(j)
            
            if guess[j] not in letters_in:
                letters_in[guess[j]] = 1
                guessColor[j] = "Y"
            elif letters_in[guess[j]] < sol.count(guess[j]):
                letters_in[guess[j]] += 1
                guessColor[j] = "Y"
            else:
                guessColor[j] = "B"
                
    return ["".join(guessColor), clues, letters_in]
    #Guess should be fully evaluated by now

def collectStats(_dictionary_, _letterData_, _charOccurance_, gradeWhat):
    baseGraded = baseGrading(_dictionary_, _letterData_)
    extraGraded = extraGrading(_dictionary_, _letterData_, _charOccurance_)
    mixedGraded = mixedGrading(_dictionary_, baseGraded, extraGraded)
    
    
    algorithmGuessDistribution = [{},{},{}]
    algorithmGuessesPerWord = [{},{},{}]
    if gradeWhat =="b":
        for n in range(7):
            algorithmGuessDistribution[0][n] = 0
        for j in range(len(_dictionary_)):
            baseGraded = baseGrading(_dictionary_, _letterData_)
            solvedIn = instantWordle(_dictionary_, baseGraded, _dictionary_[j], "b")
            algorithmGuessDistribution[0][solvedIn] += 1
            algorithmGuessesPerWord[0][_dictionary_[j]] = solvedIn
    elif gradeWhat =="e":
        for n in range(7):
            algorithmGuessDistribution[0][n] = 0
        for j in range(len(_dictionary_)):
            extraGraded = extraGrading(_dictionary_, _letterData_, _charOccurance_)
            solvedIn = instantWordle(_dictionary_, extraGraded, _dictionary_[j], "e")
            algorithmGuessDistribution[0][solvedIn] += 1
            algorithmGuessesPerWord[0][_dictionary_[j]] = solvedIn
    elif gradeWhat =="m":
        for n in range(7):
            algorithmGuessDistribution[0][n] = 0
        for j in range(len(_dictionary_)):
            baseGraded = baseGrading(_dictionary_, _letterData_)
            extraGraded = extraGrading(_dictionary_, _letterData_, _charOccurance_)
            mixedGraded = mixedGrading(_dictionary_, baseGraded, extraGraded)
            solvedIn = instantWordle(_dictionary_, mixedGraded, _dictionary_[j], "m")
            algorithmGuessDistribution[0][solvedIn] += 1
            algorithmGuessesPerWord[0][_dictionary_[j]] = solvedIn
    elif gradeWhat == "a":
        for i in range(3):
            for n in range(7):
                algorithmGuessDistribution[i][n] = 0
            for j in range(len(_dictionary_)):
                if i == 0:
                    baseGraded = baseGrading(_dictionary_, _letterData_)
                    solvedIn = instantWordle(_dictionary_, baseGraded, _dictionary_[j], "b")
                    algorithmGuessDistribution[0][solvedIn] += 1
                    algorithmGuessesPerWord[0][_dictionary_[j]] = solvedIn
                elif i == 1:
                    extraGraded = extraGrading(_dictionary_, _letterData_, _charOccurance_)
                    solvedIn = instantWordle(_dictionary_, extraGraded, _dictionary_[j], "e")
                    algorithmGuessDistribution[1][solvedIn] += 1
                    algorithmGuessesPerWord[1][_dictionary_[j]] = solvedIn
                elif i == 2:
                    baseGraded = baseGrading(_dictionary_, _letterData_)
                    extraGraded = extraGrading(_dictionary_, _letterData_, _charOccurance_)
                    mixedGraded = mixedGrading(_dictionary_, baseGraded, extraGraded)
                    solvedIn = instantWordle(_dictionary_, mixedGraded, _dictionary_[j], "m")
                    algorithmGuessDistribution[2][solvedIn] += 1
                    algorithmGuessesPerWord[2][_dictionary_[j]] = solvedIn
    return [algorithmGuessDistribution, algorithmGuessesPerWord]
    
if __name__ == "__main__":
    words = []
    with open('master_dictionary.txt') as file:
        words = file.readlines()
        
    tailored_dictionary = []
    with open('tailored_dictionary.txt') as file2:
        tailored_dictionary = file2.readlines()
        
    better_tailored_dictionary = []
    with open('better_tailored_dictionary.txt') as file2:
        better_tailored_dictionary = file2.readlines()
        
    thisDictionary = trimDictionary(better_tailored_dictionary)
    letterData = letterDataCollection(thisDictionary)[0]
    charOccurance = letterDataCollection(thisDictionary)[1]
    
    doneAnalysis = False
    statsCollected = []
    
    while True:
        ans = input("Play Wordle? (Y for Yes, N for No): ")
        if ans.lower() == "y" or ans.lower() == "yes":
            baseGraded = baseGrading(thisDictionary, letterData)
            extraGraded = extraGrading(thisDictionary, letterData, charOccurance)
            mixedGraded = mixedGrading(thisDictionary, baseGraded, extraGraded)
            score_type = ""
            play_type = ""
            
            score_type = input("Select score type (input B for Base, E for Extra, M for Mixed): ")
            play_type = input("Select play type (input I for Instant, W to play With bot): ")
            
            if not doneAnalysis:
                doAnalysis = input("Do analysis (this will take a while), Y for Yes, N for No: ")
                if doAnalysis != "" and doAnalysis[0].lower() == "y":
                    analysisType = input("Which grading types? B for Base, E for Extra, M for Mixed, A for All: ")
                    if analysisType != "" and analysisType[0].lower() == "b":
                        statsCollected = collectStats(thisDictionary, letterData, charOccurance, "b")
                    elif analysisType != "" and analysisType[0].lower() == "e":
                        statsCollected = collectStats(thisDictionary, letterData, charOccurance, "e")
                    elif analysisType != "" and analysisType[0].lower() == "m":
                        statsCollected = collectStats(thisDictionary, letterData, charOccurance, "m")
                    elif analysisType != "" and analysisType[0].lower() == "a":
                        statsCollected = collectStats(thisDictionary, letterData, charOccurance, "a")
                #statsCollected = collectStats(thisDictionary, letterData, charOccurance)
                doneAnalysis = True
                
            if score_type != "":
                if play_type[0].lower() == "i":
                    puzzle_solution = input("Input today's five-letter Wordle solution: ")
                    if score_type[0].lower() == "b":
                        print(instantWordle(thisDictionary, baseGraded, puzzle_solution, score_type))
                    if score_type[0].lower() == "e":
                        instantWordle(thisDictionary, extraGraded, puzzle_solution, score_type)
                    if score_type[0].lower() == "m":
                        print(instantWordle(thisDictionary, mixedGraded, puzzle_solution, score_type))
            #playWordle(thisDictionary, baseGraded, extraGraded, mixedGraded)
        else:
            break