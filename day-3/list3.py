actor=["vijay","A","a","ajith","Kumar","vs","ps","suriya"]
# compresensive
[print(x) for x in actor]
##new_list=[]
##for x in actor:
##    if "a" in x:
##        new_list.append(x)
##print(new_list)
new_list=[]
new_list=[ x if "suriya" in x else "ak" for x in actor]
print(new_list)

actor.sort(reverse=True)    #--> for descending 
print(actor)

actor.sort(key=str.lower)
print(actor)

actor.sort(key=str.upper)
print(actor)

newactor=[]
newactor=actor.copy()
print(newactor)

print(actor.count("a"))

print(actor.index("vijay"))
