import sys
#Read data 
text_file = open("../input.txt", "r")
lines = [int(v.strip("\n")) for v in text_file.readlines()]

# Part 1
print(sum(lines))

# Part 2

# lines=[+7, +7, -2, -7, -4]
seen = [] #list for keeping track of seen numbers
current=0 #current number
loopcnt=0
while True: #While loop is needed because we are restarting the list over and over
    loopcnt+=1
    print("Loop count: " + str(loopcnt))
    for i,line in enumerate(lines): #Iterate over each number
        seen.append(current) #add the prior number to the list
        current+=line #find current number
        if (current in seen): #stop everything if we've already seen it
            sys.exit("Found it: " + str(current))