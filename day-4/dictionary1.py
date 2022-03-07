data={'name':"ravi","age":20,"occupation":"business","gender":"male"}
print(data)
print(data["age"])
data["name"]="trijun"
print(data)

[print(x+ ":" ,data[x]) for x in data]
data.update({"age":21})
print(data)
data.pop("occupation")
print(data)

#data.popitem()  # --> removes the last key values from the dictionary
#print(data)

#del data  --> deletes the entire dictionary 
temp=data.values()
keys=data.keys()

temp_dict=data

print(temp,keys)

temp_dict=data
print(temp_dict)

data["name"]=("Ravi","Deva","Skandan")
print(data)
