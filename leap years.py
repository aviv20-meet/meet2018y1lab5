def main():
    year = float(input("What year is it?\n"))
    leap_year = 4
    until_leap = year%4
    if(until_leap == 0):
        year = leap_year
        print("You are in a leap year")
    else:
        leap_year = year-until_leap
        print("The last leap year was: ",leap_year)
main()
reset = input("\nAgian? Y/N\n")
if (reset == 'Y','y'):
    main()
else:
    exist()
