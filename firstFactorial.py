def FirstFactorial(value):
    #print("ciao")
    if value == 0:
        return 1 
    else:
        return value*FirstFactorial(value-1)
        
    
a = FirstFactorial(4)
print (a)
for i in range(19):
    print(str(i)+" "+str(FirstFactorial(i)))
    
