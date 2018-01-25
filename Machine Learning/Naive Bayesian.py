# -*- coding: utf-8 -*-
dataset = [['young','myope','no','reduced','none'],
			   ['young','myope','no','normal','soft'],
			   ['young','myope','yes','reduced','none'],
			   ['young','myope','yes','normal','hard'],
			   ['young','hypermetrope','no','reduced','none'],
			   ['young','hypermetrope','no','normal','soft'],
			   ['young','hypermetrope','yes','reduced','none'],
			   ['young','hypermetrope','yes','normal','hard'],
			   ['pre-presbyopic','myope','no','reduced','none'],
			   ['pre-presbyopic','myope','no','normal','soft'],
			   ['pre-presbyopic','myope','yes','reduced','none'],
			   ['pre-presbyopic','myope','yes','normal','hard'],
			   ['pre-presbyopic','hypermetrope','no','reduced','none'],
			   ['pre-presbyopic','hypermetrope','no','normal','soft'],
			   ['pre-presbyopic','hypermetrope','yes','reduced','none'],
			   ['pre-presbyopic','hypermetrope','yes','normal','none'],
			   ['presbyopic','myope','no','reduced','none'],
			   ['presbyopic','myope','no','normal','none'],
			   ['presbyopic','myope','yes','reduced','none'],
			   ['presbyopic','myope','yes','normal','hard'],
			   ['presbyopic','hypermetrope','no','reduced','none'],
			   ['presbyopic','hypermetrope','no','normal','soft'],
			   ['presbyopic','hypermetrope','yes','reduced','none'],
			   ['presbyopic','hypermetrope','yes','normal','none']]

def calProb(pos, evi, res):
	numE = 0.0
	numR = 0.0
	for data in dataset:
		if data[-1] == res:
			numR = numR+1
			if data[pos] == evi:
				numE = numE+1
	return numE/numR

def product(eviList):
	resList = []
	for data in dataset:
		resList.append(data[-1])
	resList = list(set(resList))
	pList = []
	for res in resList:
		prob = 1.0
		j = 0
		for evi in eviList:
			prob = prob*calProb(j,evi,res)
			j = j+1
		pList.append(prob)
	return resList[pList.index(max(pList))]
		

print product(['young','hypermetrope','yes','reduced'])
print product(['pre-presbyopic','hypermetrope','no','normal'])
print product(['pre−presbyopic','hypermetrope','no','reduced'])
print product(['presbyopic','myope','yes','reduced'])
print product(['presbyopic','hypermetrope','no','normal'])