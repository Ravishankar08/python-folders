
class lib:
    
    def __init__(self,a,b):
        self.auth=a
        self.name=b
        
    def show(self):
        print(self.auth)
        print(self.name)
    
b1=lib('harry potter','JK')
b1.show()
costl=[]
namel=[]
availl=[]



class canteen:    
    def create(self,name,price,hav):
        self.name=name
        self.price=price
        self.hav=hav
    def add_item(self):
        costl.append(self.price)
        namel.append(self.name)
        availl.append(self.hav)
    def display(self):
        txt="{0}.\t{1}\t\t{2}\t{3}"
        for i in range(len(namel)):
            print(txt.format(i+1,namel[i],costl[i],availl[i]))
    def calc(self):
        total=0
        for i in range(len(namel)):
            total+=costl[i]*availl[i]
        print("The Total Expenditure is  : ",total)
    def take(self, nm):
        if nm in namel:
            namel.remove(nm)
            print("Removed successfully")
        else:
            print("Not Found")
        
    
morn=canteen()
n=int(input("Enter the number of items"))
for i in range(n):
    morn.create(input("Enter the Name"),int(input("Enter the price")),int(input("Enter the Avail")))
    print()
    morn.add_item()
while(True):
    print("Actions:\n1.display\n2.calculate total\n3.Remove")
    ch=int(input("Enter the choice : "))
    if(ch==1):
        morn.display()
    if(ch==2):
        morn.calc()
    if(ch==0):
        break;
    if(ch==3):
        change=input("Enter the name of the food to be removed : ")
        morn.take(change)
