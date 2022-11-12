import itertools
import sys

#Read data 
text_file = open("../input.txt", "r")
lines = [v.strip("\n").split(": ") for v in text_file.readlines()]

#parse into two lists: one for starting points and one for areas
start_pt=[]
area=[]
for line in lines:
    start_pt.append([int(x) for x in line[0].split(" @ ")[1].split(",")])
    area.append([int(x) for x in line[1].split("x")])

outdict=dict()
for i,this_start in enumerate(start_pt): #iterate over each instruction

    start_x=this_start[0]+1
    end_x=start_x+area[i][0]

    start_y=this_start[1]+1
    end_y=start_y+area[i][1]

    x_list=list(range(start_x,end_x)) #all x coordinates
    y_list=list(range(start_y,end_y)) #all y coordinates

    res = list(itertools.product(x_list, y_list)) #cross them to get all coordinates

    for coord in res: #iterate over each coordinate adding 1 to that spot in the dictionary
        if coord in outdict.keys():
            outdict[coord]+=1
        else:
            outdict[coord]=1


###
# Use objects from part 1 as a starting point 
# But now check if all coordinates from instruction are "1" in the dictionary we previously created
###

for i,this_start in enumerate(start_pt): #iterate over each instruction

    start_x=this_start[0]+1
    end_x=start_x+area[i][0]

    start_y=this_start[1]+1
    end_y=start_y+area[i][1]

    x_list=list(range(start_x,end_x)) #all x coordinates
    y_list=list(range(start_y,end_y)) #all y coordinates

    res = list(itertools.product(x_list, y_list)) #cross them to get all coordinates

    ###
    # Code below changed in p2
    ###

    outlist=[]
    for coord in res: #iterate over each coordinate
        if outdict[coord]>1: #flag if >1
            outlist.append(1)
        else:
            outlist.append(0) #else append 0

    if(sum(outlist)==0): #if all are 0 return the instruction
        sys.exit(lines[i])