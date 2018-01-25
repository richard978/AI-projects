from pomegranate import *

B = DiscreteDistribution({'T':0.001,'F':0.999})
E = DiscreteDistribution({'T':0.002,'F':0.998})

A = ConditionalProbabilityTable(
	[['T','T','T',0.95],
	 ['T','T','F',0.05],
	 ['T','F','T',0.94],
	 ['T','F','F',0.06],
	 ['F','T','T',0.29],
	 ['F','T','F',0.71],
	 ['F','F','T',0.001],
	 ['F','F','F',0.999]], [B,E])

J = ConditionalProbabilityTable(
	[['T','T',0.9],
	 ['T','F',0.1],
	 ['F','T',0.05],
	 ['F','F',0.95]], [A])

M = ConditionalProbabilityTable(
	[['T','T',0.7],
	 ['T','F',0.3],
	 ['F','T',0.01],
	 ['F','F',0.99]], [A])

s1 = State(B, name="Burglary")
s2 = State(E, name="Earthquake")
s3 = State(A, name="Alarm")
s4 = State(J, name="John")
s5 = State(M, name="Mary")

model = BayesianNetwork("Burglary Problem")

model.add_states(s1,s2,s3,s4,s5)

model.add_transition(s1,s3)
model.add_transition(s2,s3)
model.add_transition(s3,s4)
model.add_transition(s3,s5)
model.bake()

marginals = model.predict_proba({})
print marginals[2].parameters[0]['T']
marginals = model.predict_proba({'John':'T','Mary':'F'})
print marginals[0].parameters[0]['T']
