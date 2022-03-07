print("Hello! Canteen ")
print("Enter all the available items today ")
food=[]
cost=[]
n=int(input("Enter the number of snacks to be inputed : "))
for x in range(n):
    food.append(input("Enter the food "+str(x+1)+": "))
    cost.append(int(input("Enter the cost  : ")))

    
while(True):
    print("0.EXIT\n1.Modify\n2.Remove\n3.ADD\n4.Display")
    ch=int(input("Enter your choice : "))
    if(ch==0):
        print("Thank you for Using me............")
        break
    else :
        if (ch==1):
            food_name=input("Enter the  name of the food to be modified : ")
            change=food.index(food_name.strip())
            if(change >=0):
                cost_change=int(input("Enter the amount to be Modified : "))
                cost[change]=cost_change
                print("\n\t****************Modified Successfully1****************")
            else:
                print("item not found")
        if(ch==2):
            food_name=input("Enter the name of the food to be removed : ")
            if(food_name in food):
                index=food.index(food_name)
                food.pop(index)
                cost.pop(index)
                print("\n\t*************removed successfuly*********************")
            else:
                print("SORRY ! item not Found ")
        if(ch==4):
            if(len(food)==0):
                print("SORRY ! Your list is empty")
            print("\n====================================")
            for x in range(len(food)):
                txt="{0}. {1}   {2}"
                print(txt.format(x+1,food[x],cost[x]))
                print("----------------------------------")
            print("====================================\n")
        if(ch==3):
            food_new=input("Enter the new item to be added ").strip()
            cost_new=int(input("Enter the cost of new item "))
            food.append(food_new)
            cost.append(cost_new)
            print("\n\t****************Added successfully**********************")
        
                         
    
                 
          

    
