import random

ran_num = random.randint(1,10)
print(ran_num)
num = 37
guess = False
while(guess != True):
    num = input("Choose a number between 1-10\n")
    if(num == ran_num): guess = True
print("good job yuo did it!")    
    
