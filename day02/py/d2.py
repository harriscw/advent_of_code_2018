#Read data 
text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

## Part 1

two_cnt = 0
three_cnt = 0
for line in lines: #iterate over each line
    counts = dict() #initialize dict to count each character
    for i in line: #count each character
        counts[i] = counts.get(i, 0) + 1
    if(2 in counts.values()): #if there's a 2...
        two_cnt+=1
    if(3 in counts.values()): #if there's a 3...
        three_cnt+=1

print("Final:" + str(two_cnt) + "*" + str(three_cnt) + "=" + str(two_cnt*three_cnt))


## Part 2

# lines = [
# 'abcde',
# 'fghij',
# 'klmno',
# 'pqrst',
# 'fguij',
# 'axcye',
# 'wvxyz']

print(lines)
res = dict()
currentmax=0
for i,line1 in enumerate(lines): #Iterate over each line
    this_line=list(line1) #convert string to list
    for j,line2 in enumerate(lines): #Compare to all other lines
        that_line=list(line2)
        if(i !=j): #Dont self compare
            z=sum([ x==y for (x,y) in zip(this_line, that_line)]) #elementwise comparison of to lists, results in list of booleans, then sum
            if(z>currentmax):#compare this sum to the current leader, if this one is more it becomes the new leader
                currentmax=z
                the_strings=[line1,line2]

print(currentmax,the_strings)
print("".join(list(set(the_strings[0]) & set(the_strings[1])))) #This didn't work, I guess I need to preserve order...

# ...So I manually inspected these
# pbykrmjmizwhxlqnmasfgtycdv
# pbykrmjmizwhxlqnwasfgtycdv
# ................*.........