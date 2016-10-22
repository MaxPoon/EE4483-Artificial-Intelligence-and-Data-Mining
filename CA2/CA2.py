from copy import deepcopy
class State:
    def __init__(self,currentState, zero, parrent=None,pathLength=0):
        self.parrent = parrent
        self.zero = zero
        self.pathLength = pathLength
        self.currentState = currentState
        self.heuristic = pathLength
        for row in range(3):
            for col in range(3):
                self.heuristic += abs(row-goalCoordinate[currentState[row][col]][0])+abs(col-goalCoordinate[currentState[row][col]][1])
goal = [[1,2,3],[8,0,4],[7,6,5]]
goalCoordinate = [[1,1],[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]]
startState = [[],[],[]]
open=[]
print("""
Enter each row of the start state. Use integer 1-8 to represent the eight tiles and space for the empty grid. For example:
First row:  321
Second row: 4 8
Third row:  567

Our goal state is:
123
8 4
765
""")

firstRow = input("Enter the first row:  ")
secondRow = input("Enter the second row: ")
thirdRow = input("Enter the third row:  ")
for c in firstRow:
    startState[0].append(int(c) if c!=" " else 0)
for c in secondRow:
    startState[1].append(int(c) if c!=" " else 0)
for c in thirdRow:
    startState[2].append(int(c) if c!=" " else 0)
if startState == goal:
    print()
    print("Solution: ")
    print(firstRow)
    print(secondRow)
    print(thirdRow)
    quit()
for r in range(3):
    for c in range(3):
        if startState[r][c]==0:
            zero=[r,c]
open.append(State(startState,zero))
while True:
    state = open[0]
    open = open[1:]
    currentState = state.currentState
    zeroR = state.zero[0]
    zeroC = state.zero[1]
    pathLength = state.pathLength + 1
    if zeroR>0:
        newState = deepcopy(currentState)
        newState[zeroR][zeroC] = newState[zeroR-1][zeroC]
        newState[zeroR-1][zeroC] = 0
        newState = State(newState,[zeroR-1,zeroC], state, pathLength)
        if newState.heuristic-pathLength==0:
            lastState = newState
            break
        open.append(newState)
    if zeroR < 2:
        newState = deepcopy(currentState)
        newState[zeroR][zeroC] = newState[zeroR + 1][zeroC]
        newState[zeroR + 1][zeroC] = 0
        newState = State(newState, [zeroR + 1, zeroC], state, pathLength)
        if newState.heuristic - pathLength == 0:
            lastState = newState
            break
        open.append(newState)
    if zeroC > 0:
        newState = deepcopy(currentState)
        newState[zeroR][zeroC] = newState[zeroR][zeroC-1]
        newState[zeroR][zeroC-1] = 0
        newState = State(newState, [zeroR , zeroC -1], state, pathLength)
        if newState.heuristic - pathLength == 0:
            lastState = newState
            break
        open.append(newState)
    if zeroC < 2:
        newState = deepcopy(currentState)
        newState[zeroR][zeroC] = newState[zeroR][zeroC+1]
        newState[zeroR][zeroC+1] = 0
        newState = State(newState, [zeroR , zeroC +1], state, pathLength)
        if newState.heuristic - pathLength == 0:
            lastState = newState
            break
        open.append(newState)
    open = sorted(open, key = lambda state: state.heuristic)

state = lastState
solution = [state.currentState]
while state.parrent:
    state = state.parrent
    solution.append(state.currentState)
print("\nSolution:\n")
for i in range(len(solution)-1,-1,-1):
    state = solution[i]
    for r in range(3):
        string=""
        for c in range(3):
            string+= str(state[r][c]) if state[r][c]!=0 else " "
        print(string)
    print()