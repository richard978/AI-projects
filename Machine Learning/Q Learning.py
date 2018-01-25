from numpy import *
Gamma = 0.8
count = 1000
ROOM_SIZE = 6
Q = zeros((ROOM_SIZE,ROOM_SIZE))
R = array([[-1,-1,-1,-1,0,-1],
	[-1,-1,-1,0,-1,100],
	[-1,-1,-1,0,-1,-1],
	[-1,0,0,-1,0,-1],
	[0,-1,-1,0,-1,100],
	[-1,0,-1,-1,0,100]])

def Q_Learning(state):
	curr = 0
	for action in range(ROOM_SIZE):
		if(R[state][action] == -1):
			Q[state][action] = 0
		else:
			curr = action;
			Q[state][action] = R[state][action] + Gamma*max(Q[curr,:])

c = 0
while(c<count):
	for i in range(ROOM_SIZE):
		Q_Learning(i)
	c+=1
def getRoute(start,end):
	curr = start
	route = []
	while True:
		next = argmax(Q[curr,:])
		if next not in route:
			Q[curr][next] = 0
			route.append(curr)
			curr = next
		if curr == end:
			route.append(curr)
			break
	print route

start = int(input("Enter start node: "))
end = int(input("Enter goal node: "))
print "Q matrix:"
print Q/Q.max()*100
getRoute(start,end)

