# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 01:44:21 2022

@author: Samuel Liechty
"""

import re

rawText =""
textFile = open("reformat.txt", "r")
rawText = textFile.read()
textFile.close()
print(rawText)

words = re.findall(r'\"(.*?)\"',rawText)

sorted_words = sorted(words)

with open("reformatted.txt", "w") as writeTo:
    for word in sorted_words:
        writeTo.write(word)
        writeTo.write("\n")

print(sorted_words)