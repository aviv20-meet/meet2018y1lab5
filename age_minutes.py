name = input("Please type your first and last name\n")
lastname = name.split()
lastname = lastname[1]
age = int(input("What's your age?\n"))
age = age * 365.25 *24 *60
name = name[0].capitalize()+" . " +lastname.upper()
print(name,"\nYour age in minutes",age)
