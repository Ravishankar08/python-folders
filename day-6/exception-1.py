##a=int(input("Enter a :"))
##b=int(input("Enter b :"))
##try:
##    print(a/b)
##except:
##    print("Divisible by zero ERROR {} / {} ".format(a,b))
##else:
##    print("This is else block - No ERROR is found")  #--> if no error
##finally:
##    print("Always execute ")
print("===================================")

try:
    file=open("hi.txt","w")
    file.write("hai this is new text")
    print("the text 'hai this new text' has been written")
except:
    print("NO file found")
finally:
    file.close()
    print("File implementation closed")
