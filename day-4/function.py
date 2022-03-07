#arbitary arguments
def sg(*msg):
    print("good morning "+msg[0])
    print(type(msg))
    return "code word accepted "+str(msg[1])
print(sg('girls',50))
print(sg("roshan",100))
print("===========================================")

#keyword arguments
def db(msg1,msg2):
    print("good morning "+str(msg1))
    return "code word accepted "+str(msg2)
print(db(msg2=50,msg1='mass'))
print(db("roshan",100))

print("===========================================")

# arbitary + keyword
def sg(**msg):
    print("good morning "+str(msg['a']))
    print(type(msg))
    return "code word accepted "+str(msg['b'])
print(sg(b=50,a='girls'))
print(sg(a="roshan",b=100))
print("===========================================")

#   default arguments
##  def name(temp="value")

#recursion
