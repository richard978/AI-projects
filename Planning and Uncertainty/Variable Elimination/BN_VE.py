import copy, itertools

class BN:
	def _init_(self):
		self.permBuf = {}
		self.net = {}
		self._data()

	#initialize data
	def _data(self):
		#alarm example
		self.net['PatientAge'] = {
			'parents': [],
			'children': ['Disability'],
			'pr': {},
			'conPr': {}
		}
		self.net['PatientAge']['pr'][('0-30',)] = 0.1
		self.net['PatientAge']['pr'][('31-65',)] = 0.3
		self.net['PatientAge']['pr'][('65+',)] = 0.6

		self.net['CTScanResult'] = {
			'parents': [],
			'children': ['StrokeType'],
			'pr': {},
			'conPr': {}
		}
		self.net['CTScanResult']['pr'][('IS',)] = 0.7
		self.net['CTScanResult']['pr'][('HS',)] = 0.3

		self.net['MRIScanResult'] = {
			'parents': [],
			'children': ['StrokeType'],
			'pr': {},
			'conPr': {}
		}
		self.net['MRIScanResult']['pr'][('IS',)] = 0.7
		self.net['MRIScanResult']['pr'][('HS',)] = 0.3

		self.net['Anticoagulants'] = {
			'parents': [],
			'children': ['Mortality'],
			'pr': {},
			'conPr': {}
		}
		self.net['Anticoagulants']['pr'][('Used',)] = 0.5
		self.net['Anticoagulants']['pr'][('Not used',)] = 0.5

		self.net['StrokeType'] = {
			'parents': ['CTScanResult','MRIScanResult'],
			'children': ['Mortality','Disability'],
			'pr': -1,
			'conPr': {}
		}
		self.net['StrokeType']['conPr'][('IS','IS','IS')] = 0.8
		self.net['StrokeType']['conPr'][('IS','HS','IS')] = 0.5
		self.net['StrokeType']['conPr'][('HS','IS','IS')] = 0.5
		self.net['StrokeType']['conPr'][('HS','HS','IS')] = 0
		self.net['StrokeType']['conPr'][('IS','IS','HS')] = 0
		self.net['StrokeType']['conPr'][('IS','HS','HS')] = 0.4
		self.net['StrokeType']['conPr'][('HS','IS','HS')] = 0.4
		self.net['StrokeType']['conPr'][('HS','HS','HS')] = 0.9
		self.net['StrokeType']['conPr'][('IS','IS','SM')] = 0.2
		self.net['StrokeType']['conPr'][('IS','HS','SM')] = 0.1
		self.net['StrokeType']['conPr'][('HS','IS','SM')] = 0.1
		self.net['StrokeType']['conPr'][('HS','HS','SM')] = 0.1


		self.net['Mortality'] = {
			'parents': ['StrokeType','Anticoagulants'],
			'children': [],
			'pr': -1,
			'conPr': {}
		}
		self.net['Mortality']['conPr'][('IS','Used','False')] = 0.28
		self.net['Mortality']['conPr'][('HS','Used','False')] = 0.99
		self.net['Mortality']['conPr'][('SM','Used','False')] = 0.1
		self.net['Mortality']['conPr'][('IS','Not used','False')] = 0.56
		self.net['Mortality']['conPr'][('HS','Not used','False')] = 0.58
		self.net['Mortality']['conPr'][('SM','Not used','False')] = 0.05
		self.net['Mortality']['conPr'][('IS','Used','True')] = 0.72
		self.net['Mortality']['conPr'][('HS','Used','True')] = 0.01
		self.net['Mortality']['conPr'][('SM','Used','True')] = 0.9
		self.net['Mortality']['conPr'][('IS','Not used','True')] = 0.44
		self.net['Mortality']['conPr'][('HS','Not used','True')] = 0.42
		self.net['Mortality']['conPr'][('SM','Not used','True')] = 0.95

		self.net['Disability'] = {
			'parents': ['StrokeType','PatientAge'],
			'children': [],
			'pr': -1,
			'conPr': {}
		}
		self.net['Disability']['conPr'][('IS','0-30','Negligible')] = 0.8
		self.net['Disability']['conPr'][('HS','0-30','Negligible')] = 0.7
		self.net['Disability']['conPr'][('SM','0-30','Negligible')] = 0.9
		self.net['Disability']['conPr'][('IS','31-65','Negligible')] = 0.6
		self.net['Disability']['conPr'][('HS','31-65','Negligible')] = 0.5
		self.net['Disability']['conPr'][('SM','31-65','Negligible')] = 0.4
		self.net['Disability']['conPr'][('IS','65+','Negligible')] = 0.3
		self.net['Disability']['conPr'][('HS','65+','Negligible')] = 0.2
		self.net['Disability']['conPr'][('SM','65+','Negligible')] = 0.1
		self.net['Disability']['conPr'][('IS','0-30','Moderate')] = 0.1
		self.net['Disability']['conPr'][('HS','0-30','Moderate')] = 0.2
		self.net['Disability']['conPr'][('SM','0-30','Moderate')] = 0.05
		self.net['Disability']['conPr'][('IS','31-65','Moderate')] = 0.3
		self.net['Disability']['conPr'][('HS','31-65','Moderate')] = 0.4
		self.net['Disability']['conPr'][('SM','31-65','Moderate')] = 0.3
		self.net['Disability']['conPr'][('IS','65+','Moderate')] = 0.4
		self.net['Disability']['conPr'][('HS','65+','Moderate')] = 0.2
		self.net['Disability']['conPr'][('SM','65+','Moderate')] = 0.1
		self.net['Disability']['conPr'][('IS','0-30','Severe')] = 0.1
		self.net['Disability']['conPr'][('HS','0-30','Severe')] = 0.1
		self.net['Disability']['conPr'][('SM','0-30','Severe')] = 0.05
		self.net['Disability']['conPr'][('IS','31-65','Severe')] = 0.1
		self.net['Disability']['conPr'][('HS','31-65','Severe')] = 0.1
		self.net['Disability']['conPr'][('SM','31-65','Severe')] = 0.3
		self.net['Disability']['conPr'][('IS','65+','Severe')] = 0.3
		self.net['Disability']['conPr'][('HS','65+','Severe')] = 0.6
		self.net['Disability']['conPr'][('SM','65+','Severe')] = 0.8

	def normalize(self, prob):
		return tuple(pr*1/(sum(prob)) for pr in prob)

	#get probability of P(v|e)
	def getProb(self,v,e):
		if self.net[v]['pr'] != -1:
			tup = (e[v],)
			pr = self.net[v]['pr'][tup]
		else:
			parents = tuple(e[p] for p in self.net[v]['parents'])
			tup = (e[v],)
			pr = self.net[v]['conPr'][parents+tup]
		return pr

	def getSeq(self,v):
		if v in self.permBuf:
			return self.permBuf[v]
		else:
			if self.net[v]['pr']==-1:
				perm = list(self.net[v]['conPr'])
			else:
				perm = list(self.net[v]['pr'])
			self.permBuf[v] = perm
			return perm

	def getFactor(self,v,factor,e):
		var = factor[v]
		var.sort()
		allVar = copy.deepcopy(self.net[v]['parents'])
		allVar.append(v)
		perm = self.getSeq(v)
		temp = {}
		evi = {}
		for p in perm:
			flag = False
			for pair in zip(allVar,p):
				if pair[0] in e and e[pair[0]]!=pair[1]:
					flag = True
					break
				evi[pair[0]] = pair[1]
			if flag:
				continue
			i = tuple(evi[j] for j in var)
			pr = self.getProb(v,evi)
			temp[i] = pr
		return (var,temp)

	def product1(self,v,f1,f2):
		var = []
		var.extend(f1[0])
		var.extend(f2[0])
		var = list(set(var))
		var.sort()

		perm = []
		for i in range(len(var)):
			t = []
			for p in self.getSeq(var[i]):
				if p[-1] not in t:
					t.append(p[-1])
			perm.append(t)
		perm = list(itertools.product(*perm))

		temp = {}
		evi = {}
		for p in perm:
			for pair in zip(var,p):
				evi[pair[0]] = pair[1]
			i = tuple(evi[a] for a in var)
			j = tuple(evi[a] for a in f1[0])
			k = tuple(evi[a] for a in f2[0])
			pr = f1[1][j]*f2[1][k]
			temp[i] = pr
		return (var,temp)

	def sumOut(self,v,factors):
		varFac = []
		index = []
		for i,factor in enumerate(factors):
			if v in factor[0]:
				varFac.append(factor)
				index.append(i)
		if len(varFac)>1:
			for i in reversed(index):
				del factors[i]
			res = varFac[0]
			for factor in varFac[1:]:
				res = self.product1(v,res,factor)
			factors.append(res)

		cond = []
		if self.net[v]['pr']==-1:
			for i in range(len(list(self.net[v]['conPr']))):
				if list(self.net[v]['conPr'])[i][-1] not in cond:
					cond.append(list(self.net[v]['conPr'])[i][-1])
		else:
			for i in range(len(list(self.net[v]['pr']))):
				if list(self.net[v]['pr'])[i][-1] not in cond:
					cond.append(list(self.net[v]['pr'])[i][-1])
		#sum out step
		for i,factor in enumerate(factors):
			for j,v1 in enumerate(factor[0]):
				if v1==v:
					var = factor[0][:j] + factor[0][j+1:]
					temp = {}
					for en in factor[1]:
						en = list(en)
						key = tuple(en[:j]+en[j+1:])
						pr = 0
						for con in cond:
							en[j] = con
							pr += factor[1][tuple(en)]
						temp[key] = pr

					factors[i] = (var,temp)
					if len(var)==0:
						del factors[i]
		return factors

	def elimination(self,v,e):
		factors = []
		elimed = set()
		while len(elimed)<len(self.net):
			variable = filter(lambda a:a not in elimed,list(self.net.keys()))
			variable = filter(lambda a:all(c in elimed for c in self.net[a]['children']),variable)
			varFac = {}
			for a in variable:
				varFac[a] = [p for p in self.net[a]['parents'] if p not in e]
				if a not in e:
					varFac[a].append(a)
			var = sorted(varFac.keys(),key=(lambda x:(len(varFac[x]),x)))[0]
			if len(varFac[var])>0:
				factors.append(self.getFactor(var,varFac,e))
			if var != v and var not in e:
				factors = self.sumOut(var,factors)
			elimed.add(var)

		if len(factors)>=2:
			res = factors[0]
			for f in factors[1:]:
				res = self.product1(var,res,f)
		else:
			res = factors[0]

		tempVar = []
		if self.net[res[0][0]]['pr'] != -1:
			for j in self.net[res[0][0]]['pr']:
				if j not in tempVar:
					tempVar.append(j[-1])
		else:
			for j in list(self.net[res[0][0]]['conPr']):
				if j[-1] not in tempVar:
					tempVar.append(j[-1])

		cond = []
		for i in res[1]:
			if i[0] in tempVar:
				cond.append(res[1][i])

		cond = self.normalize(cond)
		ans = {}
		count = 0
		for i in res[1]:
			ans[i[0]]=cond[count]
			count=count+1
		return ans

def main():
	bn=BN()
	bn._init_()
	#p1
	X = 'Mortality'
	e = ['PatientAge','CTScanResult']
	edict = {'PatientAge':'31-65','CTScanResult':'IS'}
	Xvalue = 'True'
	res = bn.elimination(X,edict)
	print("P1 Result:")
	print Xvalue,":",res[Xvalue]
	#p2
	X = 'Disability'
	e = ['PatientAge','MRIScanResult']
	edict = {'PatientAge':'65+','MRIScanResult':'HS'}
	Xvalue = 'Moderate'
	res = bn.elimination(X,edict)
	print("P2 Result:")
	print Xvalue,":",res[Xvalue]
	#p3
	X = 'StrokeType'
	e = ['PatientAge','CTScanResult','MRIScanResult']
	edict = {'PatientAge':'65+','CTScanResult':'HS','MRIScanResult':'IS'}
	Xvalue = 'SM'
	res = bn.elimination(X,edict)
	print("P3 Result:")
	print Xvalue,":",res[Xvalue]
	#p4
	X = 'Anticoagulants'
	e = ['PatientAge']
	edict = {'PatientAge':'0-30'}
	Xvalue = 'Not used'
	res = bn.elimination(X,edict)
	print("P4 Result:")
	print Xvalue,":",res[Xvalue]

if __name__=='__main__':
	main()