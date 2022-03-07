while(True):
    try:
        a=int(input("Input First no.: "))
        b=int(input("Input Second no.: "))
        if(a<0 or b<0):
            raise Exception("Negative numbers are not allowed  ")
        c=a/b
        print("\tDivision is ",c)
        break
    except ValueError:
        print("Enter only Integer value " )
    except ZeroDivisionError:
        print("Dont use zero as a value ")
    
