array_three_five = []
for i in range(1000):
    if(i%3 == 0 or i%5==0):
        array_three_five.append(i)
sum_array = sum(array_three_five)
print(sum_array)
