# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite
# correct).
# -----------

from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    #######################
    ### ENTER CODE HERE ###
    #######################
    delta_x=1
    delta_y=1
    while delta_x>tolerance or delta_y>tolerance:
        delta_x=0
        delta_y=0
        for i in range(len(newpath)-2):
            old_x=newpath[i+1][0]
            old_y=newpath[i+1][1]
            newpath[i+1][0]=newpath[i+1][0]+weight_data*(path[i+1][0]-newpath[i+1][0]) +weight_smooth*(newpath[i+2][0]+newpath[i][0]-2*newpath[i+1][0])

            newpath[i+1][1]=newpath[i+1][1]+weight_data*(path[i+1][1]-newpath[i+1][1]) +weight_smooth*(newpath[i+2][1]+newpath[i][1]-2*newpath[i+1][1])


            delta_x=delta_x+abs(newpath[i+1][0]-old_x)
            delta_y=delta_y+abs(newpath[i+1][1]-old_y)


    return newpath # Leave this line for the grader!

printpaths(path,smooth(path))
