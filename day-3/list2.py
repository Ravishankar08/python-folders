##s=input("Enter the word with spaces : ")
s="The geat Khali"
print(s.split(" "))
list1=s.split(" ")
print("==================================")

list2=["super","Ragul","boy"]
list3=list1+list2
print(list3)
print (list2[:4])
if("geat" in list3):
    print("present")
list1[0:2]=list2[-2:]
print(list1)
# insert in between -> any space in between
actor=["vijay","ajith","dhanush","suriya"]
actor.insert(1,"jayam Ravi")
print(actor)

print("==================================")
print(list1)
print(list2)
list1.extend(list2)
print(list1)
# extend can be used to extend any list,tuple as cross
list1.remove("Khali")   #--> values
print(list1)
list1.pop(3)            #--> indexes
print(list1)
del list1[0]
print(list1)

# if del list1 is run then the entire list is deleted
# no list is present anymore

list1.clear()   # --> removes all the element in the list
print(list1)
