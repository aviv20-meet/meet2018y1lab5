def binary(decimal_num):
    """
    Converts number to binary
    """
    binary_array = []
    temp = 0
    while(decimal_num>0):
        temp = decimal_num
        decimal_num = int(temp/2)
        if(temp%2 == 0):
            binary_array += '0'
        else:
            binary_array += '1'
    print(binary_array)
    reset()
        
def hex_num(decimal_num):
    """
    converts decimal number inputed by user to hex 
    """
    hex_num = hex(decimal_num)
    hex_num = hex_num[2:]
    print(str(decimal_num)+" in hexdecimal is "+hex_num)
    reset()

def main():
    """
    asks user input and calls appropriate function
    """
    decimal_num = int(input("Please type a ddecimal number\n"))
    type_num = input("choose number type(hex/bin)\n")
    if(type(type_num) != str or type(decimal_num) != int):
        print("try agian")
        main()
    if(type_num == 'hex'):
        hex_num(decimal_num)
    else:
        binary(decimal_num)
def reset():
    """
    aks user tor try agian and call main
    """
    answer = input("would you like to try again?(y/n)\n")
    answer = answer.lower()
    if(answer == 'y' or answer == 'yes' or answer == 'yeah'):
        main()
    else:
        exit
main()
