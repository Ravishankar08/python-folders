friends=("Ravi","Deva","Ragul","iniyan","Hema","Abhiram","Hema")
print(friends)
# no change , no delete , no sort
temp_list=list(friends)
print(type(temp_list))
print(temp_list)
temp_list.append("Skandhan")
friends=tuple(temp_list)
print(friends)
print(friends[-5:-3])

