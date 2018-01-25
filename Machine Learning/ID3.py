import math
import operator

def calEnt(dataset):
	entries = len(dataset)
	numLabel = {}
	for data in dataset:
		currLabel = data[-1]
		if currLabel not in numLabel.keys():
			numLabel[currLabel] = 0
		numLabel[currLabel] += 1
	ent = 0.0
	for key in numLabel:
		prob = float(numLabel[key])/entries
		ent -= prob*math.log(prob,2)
	return ent

def createDataset():
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
	labels = ['age','spectacle-presc','astigmatism','tar-dorp-ract']
	return dataset,labels

def splitData(dataset,split,value):
	tempData =[]
	for data in dataset:
		if data[split] == value:
			reducedData = data[:split]
			reducedData.extend(data[split+1:])
			tempData.append(reducedData)
	return tempData

def chooseRoot(dataset):
	num = len(dataset[0])-1
	iniEnt = calEnt(dataset)
	iniGain = 0.0
	feature = -1
	for i in range(num):
		feaList = [data[i] for data in dataset]
		valList = set(feaList)
		newEnt = 0.0
		for val in valList:
			subSet = splitData(dataset,i,val)
			prob = len(subSet)/float(len(dataset))
			newEnt += prob*calEnt(subSet)
		gain = iniEnt-newEnt
		if(gain>iniGain):
			iniGain = gain
			feature = i
	return feature

def countRes(resList):
	resCount = {}
	for res in resList:
		if res not in resCount.keys():
			resCount[res] = 0
		resCount[res] = 1
	sortedCount = sorted(resCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedCount[0][0]

def createTree(dataset,labels):
	resList = [data[-1] for data in dataset]
	if resList.count(resList[0])==len(resList):
		return resList[0]
	if len(dataset[0])==1:
		return countRes(resList)
	feature = chooseRoot(dataset)
	feaLabel = labels[feature]
	tree = {feaLabel:{}}
	del(labels[feature])
	feaValue = [data[feature] for data in dataset]
	values = set(feaValue)
	for v in values:
		label = labels[:]
		tree[feaLabel][v] = createTree(splitData(dataset,feature,v),label)
	return tree

data,labels = createDataset()
tree =  createTree(data,labels)
print tree['tar-dorp-ract']['reduced']#['astigmatism']['yes']['spectacle-presc']['hypermetrope']['age']['young']
print tree['tar-dorp-ract']['normal']['astigmatism']['no']['age']['pre-presbyopic']#['spectacle-presc']['hypermetrope']
print tree['tar-dorp-ract']['reduced']#['astigmatism']['no']['age']['pre-presbyopic']['spectacle-presc']['hypermetrope']
print tree['tar-dorp-ract']['reduced']#['astigmatism']['yes']['age']['pre-presbyopic']['spectacle-presc']['myope']
print tree['tar-dorp-ract']['normal']['astigmatism']['no']['age']['pre-presbyopic']#['spectacle-presc']['hypermetrope']