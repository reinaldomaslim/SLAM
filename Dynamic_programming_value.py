# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value=[[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    iteration=0
    x=goal[0]
    y=goal[1]
    isnotFull=True
    value[x][y]=0
    open = [[iteration, x, y]]

    while(isnotFull):
        if len(open)==0:
            isnotFull=False
        else:
            open.sort()
            open.reverse()
            next=open.pop()
            x = next[1]
            y = next[2]
            g = next[0]

            for i in range(len(delta)):
                x2=x+ delta[i][0]
                y2=y+ delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                    if grid[x2][y2]==0:

                        if value[x2][y2]>g+1:

                            value[x2][y2]=g+1
                            open.append([g+1, x2, y2])


    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value

result=compute_value(grid,goal,cost)
for i in range(len(grid)):
    print(result[i])
