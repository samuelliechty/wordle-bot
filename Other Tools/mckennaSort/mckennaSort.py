# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 01:15:43 2022

@author: Samuel Liechty
"""
def CollectWordsFromTxt(readFile):
    dictionary = open(readFile+".txt", "r")
    words = dictionary.readlines()
    
    for i in range(len(words)):
        words[i] = words[i][0:5]
        
    return words

def WriteTxt(writeFile, lines):
    with open(writeFile+".txt", "w") as f:
        f.writelines(lines)

if __name__ == "__main__":
    unsortted_words = CollectWordsFromTxt("mckenna_unsortted_dictionary")
    denied_words = CollectWordsFromTxt("mckenna_denied_words")
    approved_words = CollectWordsFromTxt("mckenna_approved_words")
    print("\n")
    for word in unsortted_words:
        if word not in denied_words and word not in approved_words:
            decision = ""
            while True:
                decision = input("Do you like " +word.upper()+ "?"+"\n"+"Input Y for Yes, N for No, or Q to Quit the program: ")
                if len(decision) > 0:
                    if decision[0].lower() == "y" or decision[0].lower() == "n" or decision[0].lower() == "q":
                        break
                    else:
                        print("\n"+"HEY! Input valid response! >:(")
                else:
                    print("\n"+"HEY! Input valid response! >:(")
            
            if decision[0].lower() == "y":
                approved_words.append(word)
            elif decision[0].lower() == "n":
                denied_words.append(word)
            elif decision[0].lower() == "q":
                break
    
    for i in range(len(denied_words)):
        denied_words[i] = denied_words[i]+"\n"
        
    for i in range(len(approved_words)):
        approved_words[i] = approved_words[i]+"\n"
    
    WriteTxt("mckenna_denied_words", denied_words)
    WriteTxt("mckenna_approved_words", approved_words)