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
        dist_list=[]
        for k,coord in enumerate(lines): #compare this coordinate to all coordinate in dataset
            dist_list.append(manhattan_distance(a=[i,j],b=coord)) #For Part 2 append distance to coord from data to list
        region_dict[(i,j)]=sum(dist_list) #write sum of distances to dictionary for that point

print("Part 2:",sum(i < 10000 for i in region_dict.values())) #now count all the values in the dict <10000