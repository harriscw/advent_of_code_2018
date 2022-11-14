import datetime

#Read data 
text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()]

lines.sort()

def get_minutes_list(start,end):  #This is a function to create a list of each minute between two times
    outlist=[]
    delta = datetime.timedelta(minutes=1)
    start = datetime.datetime.strptime( start, '%H:%M' )
    end = datetime.datetime.strptime( end, '%H:%M' )
    t = start
    while t < end :
        outlist.append(datetime.datetime.strftime( t, '%H:%M'))
        t += delta
    return(outlist)

## This approach here is to create a dictionary of dictionaries
## The outer dictionary will have a key per guard
## Each subdictionary per guard will have an entry for 1. total minutes slept and 2. a dictionary of most frequent asleep minutes
## Just realized i didn't need to keep a running tally of muntes slept, I could have summed values at the end.
## Oh well

guards_dict=dict()
for i,line in enumerate(lines):

    if("begins shift" in line): #add a key to the dictionary if the guard isn't in it already
        theguard = line.replace(" begins shift","").split("#")[1]
        if(theguard not in guards_dict.keys()):
            guards_dict[theguard]={"minutes_dict":dict(),"total":0}

    if("falls asleep" in line): 
        the_start = line.split("]")[0].split(" ")[1][:5] # parse the instructions a bit to get start and end times
        the_end = lines[i+1].split("]")[0].split(" ")[1][:5]
        the_minutes=get_minutes_list(the_start,the_end) #use my function above to get a list of times asleep
        guards_dict[theguard]["total"]+=len(the_minutes) #running tally of minutes slept per guard
        for j,this_min in enumerate(the_minutes): #increase dict entry for each minute slept
            if(this_min in guards_dict[theguard]["minutes_dict"].keys()):
                guards_dict[theguard]["minutes_dict"][this_min]+=1
            else:
                guards_dict[theguard]["minutes_dict"][this_min]=1

the_max=0 #OK now for part 1 find the guard who slept the most minutes
for this_guard in guards_dict.keys():
    if guards_dict[this_guard]["total"]>the_max:
        final_guard=this_guard
        the_max=guards_dict[this_guard]["total"]

the_time=max(guards_dict[final_guard]["minutes_dict"], key=guards_dict[final_guard]["minutes_dict"].get) #get the timepoint
print("Part 1:","\nGuard:",final_guard,"\nTotal Min:",the_max,"\nTime Most Often Asleep:",the_time,
"\nDays Asleep at that Time:",guards_dict[final_guard]["minutes_dict"][the_time],"\nFinal Answer (Didn't Want to Parse):",797*18)

the_max=0
for this_guard in guards_dict.keys():
    if(guards_dict[this_guard]["minutes_dict"]):
        max_time=max(guards_dict[this_guard]["minutes_dict"], key=guards_dict[this_guard]["minutes_dict"].get)
        max_val=guards_dict[this_guard]["minutes_dict"][max_time]
        if(max_val>the_max):
            final_guard=this_guard
            the_time=max_time
            the_max=max_val

print("\nPart 2:",
"\nGuard:",final_guard,
"\nTime Most Often Asleep:",the_time,
"\nDays Asleep at that Time:",the_max,
"\nFinal Answer (Didn't Want to Parse):",163*35)