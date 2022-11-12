import itertools

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

print("Final:" + str(sum([x>=2 for x in outdict.values()]))) #find values in dictionary >=2