import numpy as np

text_file = open("../input.txt", "r")
lines = [[int(x) for x in v.strip("\n").split(", ")] for v in text_file.readlines()]

def manhattan_distance(a, b): #function for manhattan distance, I googled this
    a=np.array(a)
    b=np.array(b)
    return(np.abs(a - b).sum())

# find all points in the area contained by the dataset
min_x = min([x[0] for x in lines])
max_x = max([x[0] for x in lines])+1
min_y = min([x[1] for x in lines])
max_y = max([x[1] for x in lines])+1

# iterate over each point, find the point in the dataset that has the minimum manhattan distance
# store each occordinate in a dictionary indexed by dataset points

region_dict=dict()
for i in range(min_x,max_x): #iterate over each x
    print("x:",str(i)+"/"+str(max_x))
    for j in range(min_y,max_y): #iterate over each y
        mindist=float("inf")
        for k,coord in enumerate(lines): #compare this coordinate to all coordinate in dataset
            this_dist=manhattan_distance(a=[i,j],b=coord)
            if(this_dist<mindist):
                mindist=this_dist
                mincoord=[coord]
            elif(this_dist==mindist):
                mincoord.append(coord)
        dict_entry=(mincoord[0][0],mincoord[0][1]) 
        if(len(mincoord)==1):
            if(dict_entry in region_dict.keys()):
                region_dict[dict_entry].append([i,j])
            else:
                region_dict[dict_entry]=[[i,j]]

# if a region in the dictionary has a coordinate that touches the border it is infinite.
# So find the largest region that doesn't touch the border

def is_not_on_the_border(coord): 
    if((coord[0] in [min_x,max_x-1]) or (coord[1] in [min_y,max_y-1])): ###Ugh its so annoying how range() works, had to adjust 1 here
        return(False)
    else:
        return(True)

outlist=[]
for key in region_dict.keys():
    if(all([is_not_on_the_border(x) for x in region_dict[key]])):
        outlist.append(len(region_dict[key]))

print("Part 1:",max(outlist))