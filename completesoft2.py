data={"food":[],"cost":[],"having":[]}
            
def add_item(*new_food):
    data['food'].append(new_food[0])
    data['cost'].append(new_food[1])
    data['having'].append(new_food[2])
    print("\n******************New element added successfully*************\n")

def display(c):
    if(len(data['food'])==0):
        print("\n******************no Results Found**********************")
    for j in range(len(food)):
        if(data['having'][j]!=0):
            print("-------------------------------------------------------------------")
            c=1
            print(order.format(j+1,data['food'][j],data['cost'][j],data['having'][j]))
    if(c==0):
        print("******************All stocks are out******************")
        
print("\t\t\t WELCOME to our shop\n ")
n=int(input("Enter the number of items : "))
txt="Enter the {0} of food {1} : "
order="{0}.\t{1}\t\t\t{2}\t{3}"
food=data['food']
for i in range(n):
    data["food"].append(input(txt.format("name",i+1)))
    data["cost"].append(int(input(txt.format("cost",i+1))))
    data["having"].append(int(input(txt.format("availability",i+1))))
while(True):
    print("\n0.EXIT\n1.Update\n2.Remove\n3.Display\n4.Add\n5.Only Available Stock\n6.Today's Expenditure")
    ch=int(input("Enter your choice : "))
    if(ch==0):
        print("\nThank you so much .......\n")
        print(data)
        break
    elif(ch==3):
        display(1)
    elif(ch==4):
           food_name=input("Enter the new food to be added : ")
           food_cost=int(input("Enter the cost of new food : "))
           food_hav=int(input("Enter the current Stock : "))
           add_item(food_name,food_cost,food_hav)
    elif(ch==2):
        food_remove=input("Enter the food to be removed : ").strip()
        if(food_remove in data['food']):
            index=food.index(food_remove)
            data['food'].pop(index)
            data['cost'].pop(index)
            data['having'].pop(index)
            print("\n************** ITEM REMOVED SUCCESSFULLY***********************\n")
        else:
            print("\nItem not Found \n")
    elif(ch==1):
        change=input("Enter the name of the food to be changed : ")
        if(change not in data['food']):
            print("\nSorry data Not found\n")
        else:
            print("what you need to update :\n1.Cost\n2.Availability")
            ch2=int(input("Enter our choice : "))
            index=data['food'].index(change)
            form="Enter the {}  to be modified : "
            if(ch2==1):
                cost_change=int(input(form.format("COST")))
                data['cost'][index]=cost_change
                print("\n********* Modified Successfully***************\n")
            elif(ch2==2):
                hav_change=int(input(form.format("Availability")))
                data['having'][index]=hav_change
                print("\n********* Modified Successfully***************\n")
            else :
                print("\n*****Incorrect Choice*****\n")
    elif(ch==5):
        display(0)
        print("\n")
    elif(ch==6):
        ex=0
        display(0)
        for i in range(len(data['food'])):
            ex+=int(data['cost'][i])*int(data['having'][i])
        print("\n\t\tTodays Expenditure is  : ",ex)
            
        
    
    else:
        print("\n******* Incorrect Choice ******\n")
        

