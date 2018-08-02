array = []
num = 0
num1 = 1
temp = 0
while(num <= 4000000):
    print(num , num1)
    temp = num1
    print(num , num1)
    num1 = num1 + num
    print(num , num1)
    num = temp
    print(num , num1)
    
    #num,num1 = num1, num + num1
    
    if(num%2==0):
        array.append(num)
print(sum(array))        
