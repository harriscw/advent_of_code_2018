#get just combinations of letters
lines = [v.strip("\n").replace("Step ","").replace(" can begin.","").split(" must be finished before step ") for v in open("../input.txt", "r").readlines()]

# dictionary where keys are parents and values are children
out_dict=dict()
for line in lines:
    if(line[0] not in out_dict.keys()):
        out_dict[line[0]]=[line[1]]
    else:
        out_dict[line[0]].append(line[1])

#starting point is key that isn't in values
#ending point is value not in key
allvals=[inner for outer in out_dict.values() for inner in outer] #get all the children
allkeys=list(out_dict.keys()) #get all the parents
start=list(set(allkeys).difference(allvals)) #if you don't have a parent youre a starting point
end=list(set(allvals).difference(allkeys)) #if you don't have a kid you're the ending point

# dictionary that tells you all the parents for a given node
parent_dict=dict()
for val in allvals:
    parent_dict[val]=[k for k,v in out_dict.items() if val in v]

path=""
available=start.copy()
i=0
while True:
    i+=1
    print("Start of iteration",i,"Current path:",path,"\nAvailable:",available)
    available.sort()
    for char in available: #iterate over each available letter
        print(char,list(path),available) #criteria to meet: character isn't the end char and its either the start char (has no parents) or all its parents are already unlocked (in the path)
        if(char != end[0] and (char not in parent_dict.keys() or (char in parent_dict.keys() and all([x in list(path) for x in parent_dict[char]])))):
            path+=char #update path
            available.remove(char) #remove current character from list of available
            available+=out_dict[char] #add newly available characters
            available=list(set(available)) #get unique
            break #restart for loop
    if(len(available)==1 and available[0]==end[0]): #check for end condition: if there's only 1 left available and its the end char
        path+=available[0] #add it to the path
        break #end while loop

print("Part 1:",path)