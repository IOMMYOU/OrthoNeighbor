# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:29:36 2022

@author: Alec
"""

#reads list of words
#outputs a word
##maybe runs random index 
#scans list for next word that satisfies being only
#	a single character away 
import random
import sys

with open('./5list.txt','r') as f:
	lines = f.readlines()

swaps = 0
consecSwaps = 0
swapStorage = 0
random.shuffle(lines)
word = "start"
word = lines[0]
madeDifferent=False
firstRun = True
out="" 
used = []
print("type 5 letter word to get started or press ENTER")
print("type x to exit")
temp = input()
print(temp)
if (temp == 'x' or temp=='exit'):
    sys.exit(0)
if(len(temp.strip())==5):
	word = temp.strip()
while(firstRun or input()!='x'):
	firstRun = False
	random.shuffle(lines)
	used.append(word)
	for line in lines:
		if (line.strip() in used):
			continue
		madeDifferent = False
		if (len(word) == len(line.strip())):
			for idx, letter in enumerate(line.strip()):
				if(letter == word[idx]):
					out  += letter
					continue
				else:
					if (not madeDifferent):
						out  += letter
						madeDifferent = True
						continue
					else:
						out=""
						break
		if(len(out) > 0):	
			swaps += 1
			consecSwaps += 1
			print(word, "->", line.strip(),"\t consecutive swaps:", consecSwaps, "\t total swaps:", swaps)
			word = line.strip()
			break
		out=""
	if(swaps == swapStorage):
		word=lines[0].strip()
		print(word, ": \t", "no swap", ": \t", line.strip())
		consecSwaps = 0
	swapStorage = swaps
f.close()