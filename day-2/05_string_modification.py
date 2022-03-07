txt="    PubG is banned   "
txt2="    Ff is banned     "
txt.upper()
print(txt)
print(txt.upper())
print(txt.lower())
print(txt.strip()+" ,"+txt2.strip()) #rstrip,lstrip
print(txt.rstrip()+" hello")
print(txt.replace("PubG","FF").strip())
print(txt.strip().split(" "))
list1=txt.strip().split(" ")
print("----------------------------------------")
for i in list1:
    print(i)

print("----------------------------------------")

date=input("Enter a date in (DD/MM/YYYY): ")
list2=date.split("/")
print("Date : ",list2[0])
print("Month: ",list2[1])
print("Year : ",list2[2])
