#getting the info
hieght = float(input("Hey whats you hieght?\n"))
age = int(input('Whats your age in years\n'))
eye_color= str(input('Whats your eye color\n'))
#getting question
def q_loop():
    q = str(input("Lets see if I remmember\nAsk me about you "))
    #making it into an array
    q_list = q.split(" ")
    #finding the answer
    for i in q_list:
        if(i == 'hieght'):
            print('Your hieght is ', hieght)
            reset()
        if(i == 'age'):
            print('Your age is ', age)
            reset()
        if(i == 'color' or i =='colour'):
            print('Your eye color is ', eye_color)
            reset()
        else:
            continue
def reset():
    reset = input('Would you like to know more? Y/N\n')
    if(reset == 'Y'or reset =='y' or reset == 'yes'):
        q_loop()
    else:
        exit()            
q_loop()

