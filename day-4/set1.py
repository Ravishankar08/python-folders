web={"google","FB","IBM","Yahoo","orkut","g+","youtube","FB"}
print(web)
games=('PubG','COD','roadrash','rummy','gta')
web.update(games)
# cannot sort
# cannot append
for i in web:
    print(i)


web.add("hello")
print(web)

web.remove("orkut")
print(web)
print( "orkut" in web)
#web.remove("ravi")
web.discard("ravi")

web.pop()   # -> removes any random element from the set
print(web)
print()

#web.clear()
#print(web)
names={"ravi","deva"}
tem=web.union(names)
print(tem)

names={"ravi","deva","google","Yahoo","PubG"}
tem=web.intersection(names)
print(tem)


names={"ravi","deva","google","Yahoo","PubG"}
web.intersection_update(names)
print(web)

print("---------------------------------")
names={"ravi","deva","google","Yahoo","PubG"} #--> returns the set
print(web)
web.symmetric_difference_update(names)
print(web)
