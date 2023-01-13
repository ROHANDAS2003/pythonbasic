num = []
for i in range(0,5):
    print("Enter number", i+1)
    num.append(int(input()))

sum = 0
for i in range(0,5):
    if num[i]>9:
        sum = sum + num[i]

if sum == 0:
    print("The the numbers were less than 9")
else:
    print("The sum of numbers greater than 9 is: ", sum)