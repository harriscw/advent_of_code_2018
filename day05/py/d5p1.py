#Read data 
text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()][0]

loopcnt=0
while True:
    loopcnt+=1
    changed_one=False
    if(loopcnt % 1000==0):
        print(loopcnt,len(lines))
    for i,char in enumerate(lines): #iterate over each character in the string.  the next line compares two characters accounting for upper/lower case
        if(i>0 and lines[i].lower()==lines[i-1].lower() and ((lines[i].isupper() and lines[i-1].islower()) or (lines[i].islower() and lines[i-1].isupper()))):
            lines=lines[:i-1]+lines[i+1:] #if they match then remove them
            changed_one=True #if there was a splice then restart the outer loop
            break 
    if not changed_one: #If there wasn't a change you can't react anymore so stop
        print("Didn't change one this time")
        print("Part 1:",len(lines))
        break
