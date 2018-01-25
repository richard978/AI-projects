#size of the board
size=0

#[sum, [segments]]
#huge one
problemR4 =[
        [15,[1,3],[1,4],[1,5]],
        [12,[1,7],[1,8]],
        [9,[1,10],[1,11]],
        [18,[2,3],[2,4],[2,5]],
        [26,[2,7],[2,8],[2,9],[2,10],[2,11]],
        [9,[3,2],[3,3]],
        [10,[3,5],[3,6]],
        [4,[3,8],[3,9]],
        [4,[3,11],[3,12]],
        [12,[4,2],[4,3]],
        [12,[4,6],[4,7]],
        [5,[4,9],[4,10]],
        [9,[4,12],[4,13]],
        [12,[5,3],[5,4]],
        [19,[5,7],[5,8],[5,9],[5,10]],
        [5,[5,13],[5,14]],
        [10,[6,1],[6,2]],
        [17,[6,4],[6,5]],
        [10,[6,8],[6,9]],
        [18,[6,12],[6,13],[6,14]],
        [4,[7,1],[7,2]],
        [9,[7,5],[7,6]],
        [7,[7,9],[7,10]],
        [14,[7,12],[7,13]],
        [13,[8,2],[8,3]],
        [17,[8,5],[8,6]],
        [14,[8,9],[8,10]],
        [16,[8,13],[8,14]],
        [13,[9,1],[9,2],[9,3]],
        [5,[9,6],[9,7]],
        [9,[9,10],[9,11]],
        [15,[9,13],[9,14]],
        [3,[10,1],[10,2]],
        [25,[10,5],[10,6],[10,7],[10,8]],
        [6,[10,11],[10,12]],
        [11,[11,2],[11,3]],
        [15,[11,5],[11,6]],
        [11,[11,8],[11,9]],
        [10,[11,12],[11,13]],
        [16,[12,3],[12,4]],
        [9,[12,6],[12,7]],
        [3,[12,9],[12,10]],
        [11,[12,12],[12,13]],
        [27,[13,4],[13,5],[13,6],[13,7],[13,8]],
        [13,[13,10],[13,11],[13,12]],
        [12,[14,4],[14,5]],
        [10,[14,7],[14,8]],
        [14,[14,10],[14,11],[14,12]]]

problemC4 =[
        [4,[6,1],[7,1]],
        [4,[9,1],[10,1]],
        [4,[3,2],[4,2]],
        [22,[6,2],[7,2],[8,2],[9,2],[10,2],[11,2]],
        [35,[1,3],[2,3],[3,3],[4,3],[5,3]],
        [17,[8,3],[9,3]],
        [16,[11,3],[12,3]],
        [17,[1,4],[2,4]],
        [16,[5,4],[6,4]],
        [24,[12,4],[13,4],[14,4]],
        [6,[1,5],[2,5],[3,5]],
        [24,[6,5],[7,5],[8,5]],
        [17,[10,5],[11,5]],
        [4,[13,5],[14,5]],
        [16,[3,6],[4,6]],
        [41,[7,6],[8,6],[9,6],[10,6],[11,6],[12,6],[13,6]],
        [17,[1,7],[2,7]],
        [4,[4,7],[5,7]],
        [4,[9,7],[10,7]],
        [7,[12,7],[13,7],[14,7]],
        [6,[1,8],[2,8],[3,8]],
        [17,[5,8],[6,8]],
        [16,[10,8],[11,8]],
        [16,[13,8],[14,8]],
        [28,[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9]],
        [3,[11,9],[12,9]],
        [16,[1,10],[2,10]],
        [3,[4,10],[5,10]],
        [23,[7,10],[8,10],[9,10]],
        [6,[12,10],[13,10],[14,10]],
        [6,[1,11],[2,11],[3,11]],
        [3,[9,11],[10,11]],
        [16,[13,11],[14,11]],
        [4,[3,12],[4,12]],
        [16,[6,12],[7,12]],
        [16,[10,12],[11,12],[12,12],[13,12],[14,12]],
        [39,[4,13],[5,13],[6,13],[7,13],[8,13],[9,13]],
        [16,[11,13],[12,13]],
        [3,[5,14],[6,14]],
        [16,[8,14],[9,14]]] 

#big one
problemR3 = [
        [9,[1,1],[1,2]],
        [10,[1,4],[1,5]],
        [9,[1,8],[1,9]],
        [10,[2,1],[2,2]],
        [12,[2,4],[2,5],[2,6]],
        [10,[2,8],[2,9]],
        [17,[3,2],[3,3],[3,4]],
        [6,[3,6],[3,7],[3,8]],
        [12,[4,3],[4,4]],
        [14,[4,7],[4,8],[4,9]],
        [13,[5,4],[5,5],[5,6]],
        [10,[5,9],[5,10]],
        [4,[6,2],[6,3]],
        [14,[6,5],[6,6],[6,7]],
        [10,[6,10],[6,11]],
        [3,[7,2],[7,3]],
        [12,[7,6],[7,7],[7,8]],
        [9,[7,10],[7,11]],
        [9,[8,3],[8,4]],
        [19,[8,7],[8,8],[8,9]],
        [21,[9,4],[9,5],[9,6]],
        [14,[9,9],[9,10]],
        [17,[10,5],[10,6],[10,7]],
        [24,[10,9],[10,10],[10,11]],
        [10,[11,4],[11,5]],
        [19,[11,7],[11,8],[11,9]],
        [11,[11,11],[11,12]],
        [11,[12,4],[12,5]],
        [7,[12,8],[12,9]],
        [8,[12,11],[12,12]]]
problemC3 = [
        [16,[1,1],[2,1]],
        [7,[1,2],[2,2],[3,2]],
        [16,[1,4],[2,4],[3,4],[4,4],[5,4]],
        [17,[1,5],[2,5]],
        [10,[1,8],[2,8],[3,8],[4,8]],
        [16,[1,9],[2,9]],
        [3,[2,6],[3,6]],
        [16,[3,3],[4,3]],
        [3,[3,7],[4,7]],
        [16,[4,9],[5,9]],
        [17,[5,5],[6,5]],
        [6,[5,6],[6,6],[7,6]],
        [6,[5,10],[6,10],[7,10]],
        [3,[6,2],[7,2]],
        [6,[6,3],[7,3],[8,3]],
        [7,[6,7],[7,7],[8,7]],
        [16,[6,11],[7,11]],
        [16,[7,8],[8,8]],
        [16,[8,4],[9,4]],
        [35,[8,9],[9,9],[10,9],[11,9],[12,9]],
        [10,[9,5],[10,5],[11,5],[12,5]],
        [17,[9,6],[10,6]],
        [16,[9,10],[10,10]],
        [16,[10,7],[11,7]],
        [24,[10,11],[11,11],[12,11]],
        [16,[11,4],[12,4]],
        [4,[11,8],[12,8]],
        [3,[11,12],[12,12]],]

#middle one
problemR2 = [
        [13,[1,2],[1,3]],
        [13,[1,6],[1,7]],
        [28,[2,2],[2,3],[2,4],[2,5],[2,6],[2,7]],
        [15,[3,4],[3,5]],
        [3,[3,7],[3,8]],
        [8,[4,3],[4,4]],
        [14,[4,7],[4,8]],
        [14,[5,2],[5,3]],
        [17,[5,6],[5,7]],
        [13,[6,2],[6,3]],
        [10,[6,5],[6,6]],
        [32,[7,3],[7,4],[7,5],[7,6],[7,7],[7,8]],
        [11,[8,3],[8,4]],
        [12,[8,7],[8,8]]
        ]
problemC2 = [
        [16,[1,2],[2,2]],
        [16,[5,2],[6,2]],
        [6,[1,3],[2,3]],
        [30,[4,3],[5,3],[6,3],[7,3],[8,3]],
        [15,[2,4],[3,4],[4,4]],
        [5,[7,4],[8,4]],
        [16,[2,5],[3,5]],
        [9,[6,5],[7,5]],
        [8,[1,6],[2,6]],
        [22,[5,6],[6,6],[7,6]],
        [29,[1,7],[2,7],[3,7],[4,7],[5,7]],
        [12,[7,7],[8,7]],
        [11,[3,8],[4,8]],
        [8,[7,8],[8,8]]
        ]

#small one
problemR1 = [
        [9,[1,1],[1,2]],
        [20,[2,1],[2,2],[2,3]],
        [12,[3,2],[3,3],[3,4]],
        [10,[4,3],[4,4]]]

problemC1 = [
        [16,[1,1],[2,1]],
        [7,[1,2],[2,2],[3,2]],
        [24,[2,3],[3,3],[4,3]],
        [4,[3,4],[4,4]]]

#tiny one
problemR0 = [
        [20,[1,1],[1,2],[1,3]],
        [19,[2,1],[2,2],[2,3]],
        [12,[3,1],[3,2],[3,3]]
        ]

problemC0 = [
        [23,[1,1],[2,1],[3,1]],
        [21,[1,2],[2,2],[3,2]],
        [7,[1,3],[2,3],[3,3]]
        ]

#blanks
#huge one
blank4  =[
    [1,1],[1,2],[1,6],[1,9],[1,12],[1,13],[1,14],
    [2,1],[2,2],[2,6],[2,12],[2,13],[2,14],
    [3,1],[3,4],[3,7],[3,10],[3,13],[3,14],
    [4,1],[4,4],[4,5],[4,8],[4,11],[4,14],
    [5,1],[5,2],[5,5],[5,6],[5,11],[5,12],
    [6,3],[6,6],[6,7],[6,10],[6,11],
    [7,3],[7,4],[7,7],[7,8],[7,11],[7,14],
    [8,1],[8,4],[8,7],[8,8],[8,11],[8,12],
    [9,4],[9,5],[9,8],[9,9],[9,12],
    [10,3],[10,4],[10,9],[10,10],[10,13],[10,14],
    [11,1],[11,4],[11,7],[11,10],[11,11],[11,14],
    [12,1],[12,2],[12,5],[12,8],[12,11],[12,14],
    [13,1],[13,2],[13,3],[13,9],[13,13],[13,14],
    [14,1],[14,2],[14,3],[14,6],[14,9],[14,13],[14,14]]
#big one
blank3 = [
    [1,3],[1,6],[1,7],[1,10],[1,11],[1,12],
    [2,3],[2,7],[2,10],[2,11],[2,12],
    [3,1],[3,5],[3,9],[3,10],[3,11],[3,12],
    [4,1],[4,2],[4,5],[4,6],[4,10],[4,11],[4,12],
    [5,1],[5,2],[5,3],[5,7],[5,8],[5,11],[5,12],
    [6,1],[6,4],[6,8],[6,9],[6,12],
    [7,1],[7,4],[7,5],[7,9],[7,12],
    [8,1],[8,2],[8,5],[8,6],[8,10],[8,11],[8,12],
    [9,1],[9,2],[9,3],[9,7],[9,8],[9,11],[9,12],
    [10,1],[10,2],[10,3],[10,4],[10,8],[10,12],
    [11,1],[11,2],[11,3],[11,6],[11,10],
    [12,1],[12,2],[12,3],[12,6],[12,7],[12,10]]
#middle one
blank2 = [
    [1,1],[1,4],[1,5],[1,8],
    [2,1],[2,8],
    [3,1],[3,2],[3,3],[3,6],
    [4,1],[4,2],[4,5],[4,6],
    [5,1],[5,4],[5,5],[5,8],
    [6,1],[6,4],[6,7],[6,8],
    [7,1],[7,2],
    [8,1],[8,2],[8,5],[8,6]
    ]
#small one
blank1 = [
    [1,3],[1,4],
    [2,4],
    [3,1],
    [4,1],[4,2]]
#tiny one
blank0 = []


def init_CurDom(board,index):
    global CurDom
    global problemR
    global problemC
    able_num = []
    temp = []
    temp1 = []
    temp2 = []
    row = index//size
    col = index%size
    pos = [row+1,col+1]
    for i in range(10):
        able_num.append(1)

    #constraint for sum
    for i in range(len(problemR)):
        if pos in problemR[i]:
            tmpL = partition(problemR[i][0],len(problemR[i])-1)
            for l in tmpL:
                for j in range(10):
                    if j in l and j not in temp1:
                        temp1.append(j)
    for i in range(len(problemC)):
        if pos in problemC[i]:
            tmpL = partition(problemC[i][0],len(problemC[i])-1)
            for l in tmpL:
                for j in range(10):
                    if j in l and j not in temp2:
                        temp2.append(j)

    temp = [val for val in temp1 if val in temp2]
    CurDom.append(temp)

def init_Board(blank):
    global board
    board = [[0 for i in range(size)] for i in range(size)]
    for i in range(len(blank)):
        board[blank[i][0]-1][blank[i][1]-1] = -1

def init(board,R,C):
    global Assigned
    global num
    global CurDom
    global problemR
    global problemC
    problemR = R
    problemC = C
    for i in range(size*size):
        Assigned.append(0)
    for i in range(size*size):
        r = i//size
        c = i%size
        if(board[r][c]==0):
            num = num+1
            init_CurDom(board,i)
        else:
            Assigned[i] = 1
            CurDom.append([])

def partition(n, k):
    def _part(n, k, pre):
        if n <= 0:
            return []
        if k == 1:
            if n <= pre:
                return [[n]]
            return []
        ret = []
        for i in range(min(pre, n), 0, -1):
            ret += [[i] + sub for sub in _part(n-i, k-1, i)]
        return ret
    re =  _part(n, k, n)
    tmpL = []
    for v in re:
        if len(v)!=len(set(v)):
            tmpL.append(v)
        for i in range(len(v)):
            if v[i]>9 and v not in tmpL:
                tmpL.append(v)
    for d in tmpL:
        re.remove(d)
    return re

def PickAnUnassignedVariable():
    global CurDom
    global Assigned
    value = 10
    index = size*size+1
    for i in range(size*size):
        if(Assigned[i]==0):
            if(len(CurDom[i])<value):
                value = len(CurDom[i])
                index = i
            
    return index

def temp_Assigned(index,d):
    global CurDom
    global Assigned
    global queue
    global problemR
    global problemC
    row = index//size
    col = index%size
    temp = []
    pos = [row+1,col+1]

    #delete curdom in row problems
    for i in range(len(problemR)):
        if pos in problemR[i]:
            for j in range(len(problemR[i])-1):
                row_index = (problemR[i][j+1][0]-1)*size+problemR[i][j+1][1]-1
                if(Assigned[row_index]==0):
                    if d in CurDom[row_index]:
                        temp.append(row_index)
                        CurDom[row_index].remove(d)

    #delete curdom in column problems
    for i in range(len(problemC)):
        if pos in problemC[i]:
            for j in range(len(problemC[i])-1):
                col_index = (problemC[i][j+1][0]-1)*size+problemC[i][j+1][1]-1
                if(Assigned[col_index]==0):
                    if d in CurDom[col_index]:
                        temp.append(col_index)
                        CurDom[col_index].remove(d)

    return temp

def RestoreValues(restore,d):
    global CurDom
    for i in restore:
        CurDom[i].append(d)

def GAC_Enforce():
    global Assigned
    global CurDom
    global problemR
    global problemC

    for i in range(size*size):
        if(Assigned[i]==0):
            if(len(CurDom[i])==0):
                return False
    
    for i in range(len(problemC)):
        sum = 0
        count = 0
        for j in range(1,len(problemC[i])):
            pos = (problemC[i][j][0]-1)*size+problemC[i][j][1]-1
            sum += Assigned[pos]
            if Assigned[pos]==0:
                count += 1
        if count==0:
            if sum==problemC[i][0]:
                continue
            return False

    for i in range(len(problemR)):
        sum = 0
        count = 0
        for j in range(1,len(problemR[i])):
            pos = (problemR[i][j][0]-1)*size+problemR[i][j][1]-1
            sum += Assigned[pos]
            if Assigned[pos]==0:
                count += 1
        if count==0:
            if sum==problemR[i][0]:
                continue
            return False

    return True

def GAC(level,R,C):
    global CurDom
    global Assigned
    global queue
    global problemR
    global problemC
    problemR = R
    problemC = C
    if level is num:
        return True
    V = PickAnUnassignedVariable()
    row = V//size
    col = V%size
    for d in sorted(CurDom[V]):
        queue.append([row,col,d])
        Assigned[V] = d
        temp_list = temp_Assigned(V,d)
        if(GAC_Enforce()):
            if(GAC(level+1,problemR,problemC)):
                return True
        RestoreValues(temp_list,d)
        Assigned[V] = 0
        queue.remove([row,col,d])
    return False

if __name__ == '__main__':
    global board
    global CurDom
    global Assigned
    global num
    global queue

    num = 0
    CurDom = []
    Assigned = []
    queue = []
    size = 3
    init_Board(blank0)
    init(board,problemR0,problemC0)
    GAC(0,problemR0,problemC0)
    for value in queue:
        board[value[0]][value[1]] = value[2]
    print "Test Case 1"
    for i in range(size):
        for j in range(size):
            print ("%2s"%(board[i][j])),
        print
    print

    num = 0
    CurDom = []
    Assigned = []
    queue = []
    size = 4
    init_Board(blank1)
    init(board,problemR1,problemC1)
    GAC(0,problemR1,problemC1)
    for value in queue:
        board[value[0]][value[1]] = value[2]
    for i in range(size):
        for j in range(size):
            if (board[i][j]==-1):
                board[i][j] = '*'
    print "Test Case 2"
    for i in range(size):
        for j in range(size):
            print ("%2s"%(board[i][j])),
        print
    print

    num = 0
    CurDom = []
    Assigned = []
    queue = []
    size = 8
    init_Board(blank2)
    init(board,problemR2,problemC2)
    GAC(0,problemR2,problemC2)
    for value in queue:
        board[value[0]][value[1]] = value[2]
    for i in range(size):
        for j in range(size):
            if (board[i][j]==-1):
                board[i][j] = '*'
    print "Test Case 3"
    for i in range(size):
        for j in range(size):
            print ("%2s"%(board[i][j])),
        print
    print

    num = 0
    CurDom = []
    Assigned = []
    queue = []
    size = 12
    init_Board(blank3)
    init(board,problemR3,problemC3)
    GAC(0,problemR3,problemC3)
    for value in queue:
        board[value[0]][value[1]] = value[2]
    for i in range(size):
        for j in range(size):
            if (board[i][j]==-1):
                board[i][j] = '*'
    print "Test Case 4"
    for i in range(size):
        for j in range(size):
            print ("%2s"%(board[i][j])),
        print
    print

    num = 0
    CurDom = []
    Assigned = []
    queue = []
    size = 14
    init_Board(blank4)
    init(board,problemR4,problemC4)
    GAC(0,problemR4,problemC4)
    for value in queue:
        board[value[0]][value[1]] = value[2]
    for i in range(size):
        for j in range(size):
            if (board[i][j]==-1):
                board[i][j] = '*'
    print "Test Case 5"
    for i in range(size):
        for j in range(size):
            print ("%2s"%(board[i][j])),
        print
    print