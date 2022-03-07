list1=["samosa","biscuits","pufs","ice creams","friuty","smoothy","pufs"]
print(type(list1))
print("==================================")
# list is ordered so has index.
print(list1[2])
print("==================================")
for i in range(0,len(list1)):
    print(list1[i])
print("==================================")
for i in list1:
    print(i)
print("==================================")
print("to print all the values sepearted by commas ',' :\n ")
inp=""
for i in range(0,len(list1)-1):
    inp+=list1[i]+","
print(inp+list1[i+1])
print("==================================")
list1[len(list1)-1]="tea"
print(list1)
print("==================================")
# list allows duplucates , and editble
n=int(input("Hoe many items do you need"))
items=[]
for i in range(n):
    items.append(input("Enter the value"))
print(items)
print("==================================")
m=int(input("How many items do you need : "))
element=[]
str=""
for i in range(m):
    str+=input("the value: ")+" "
element=str.strip().split(" ")
print(element)
print("==================================")
