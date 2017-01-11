# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]



init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    #first print initial value, expand and insert to pool, choose one with least optimal path, if equal to goal return, if cannot expand fail.
    pool=[]
    pool.append([])
    pool[0].append([0, init[0], init[1]])
    visit = grid
    visit[init[0]][init[1]]=1
    index=1


    while(len(pool)!=0):
        current=[]
        path=[]
        current=pool.pop(0)
        index-=1

        if (current[0][1]==goal[0] and current[0][2]==goal[1]):
            path=current[0]
            break
        new=[]
        for i in range(len(delta)):
            new=[current[0][0]+cost, current[0][1]+delta[i][0], current[0][2]+delta[i][1]]
            if new[1]<0 or new[1]>len(grid)-1 or new[2]<0 or new[2]>len(grid[0])-1:
                continue

            if visit[new[1]][new[2]]==0 and grid[new[1]][new[2]]!=1:
                pool.append([])
                pool[index].append(new)
                index+=1
                visit[new[1]][new[2]]=1
    if path==[]:
        return 'fail'

    return path


print(search(grid, init, goal, cost))
