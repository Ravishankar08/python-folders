tup=("Hello","World")
[print(x) for x in tup] 
dept=("CSE","Mech","ECE","EEE")
w,x,y,z=dept
print(w,x,y,z)
# *--> all the remaining will be allocated
# --> unpacking using ashtreik method

x,*y,z=dept
print(x,y,z)

*a,=dept   #--> to convert into a list  (shortcut)
print(a)

i=0
while i in range(len(dept)):
    print(dept[i])
    i+=1
    
# concatenation
print(tup+dept)

#multiplication
print(dept*2)

print((dept*2).count("Mech"))
print(dept.index("Mech"))


