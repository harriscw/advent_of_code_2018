import time

start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()

#Read data 
text_file = open("../input.txt", "r")
lines = [v.strip("\n") for v in text_file.readlines()][0]

# Make a function out of part 1
def react(lines):
    loopcnt=0
    while True:
        loopcnt+=1
        changed_one=False
        if(loopcnt % 10000==0):
            print(loopcnt,len(lines))
        for i,char in enumerate(lines):
            if(i>0 and lines[i].lower()==lines[i-1].lower() and ((lines[i].isupper() and lines[i-1].islower()) or (lines[i].islower() and lines[i-1].isupper()))):
                lines=lines[:i-1]+lines[i+1:]
                changed_one=True
                break
        if not changed_one:
            print("Didn't change one this time")
            print("Length after reacting:",len(lines))
            return(len(lines))

outdict=dict()
for letter in map(chr, range(97, 123)): # Iterate over each letter
    print(letter)
    thisline = lines.replace(letter,'').replace(letter.upper(),'') #Remove all upper and lower case versions of the letter
    outdict[letter]=react(lines=thisline) #react it with part 1 function and store in a dictionary

the_min=min(outdict, key=outdict.get) #key with min
the_val=outdict[the_min] #min value

print("Start:",start)
print("End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print("Time Elapsed:",round(time.time()-startsec,5))
print("Part 2:",the_min,the_val)