import random
#inetlizing the variables

def die_roll(num_d_sides, num_rolls):
    
    result_array = []
    for i in range(num_rolls):
        roll_result = random.randint(1,num_d_sides)
        result_array.append(roll_result)
        print(result_array)
    return result_array
def get_avr_roll(result_array):
    '''
    getting the avrage
    '''
    print(result_array)
    all_rolls = 0
    for r in result_array:
        all_rolls += r
    avr_roll = int(all_rolls/len(result_array))
    print(avr_roll)
def get_precent(result_array):

def get_sides():
    num_d_sides = int(input("Choose number of sides for your die\n"))
    while(type(num_d_sides) != int):
       num_d_sides = input("Please insert your answer in a natrual number")
    return num_d_sides
def get_rolls():
    num_rolls = int(input("Chooose the number of times your die will be rolled\n"))
    while(type(num_rolls) != int):
        num_rolls = input("Please insert your answer in a natrual number")
    return num_rolls
def main():
    '''
    going to get_input
    '''
    num_d_sides = get_sides()
    num_rolls = get_rolls()
    result = die_roll(num_d_sides, num_rolls)
    get_avr_roll(result)
    print (result)
main()
