print("\nEnter the input in comma seperated form")
print("Eg: 1,2,3")
x = input('Enter the tuple : ')
tup = tuple(int(a) for a in x.split(","))

print("\nEnter the string:")
str = input()

lst = list(tup)
for i in range(1,len(lst)+1):
    lst.insert(i+(i-1),str)

newTup = tuple(lst)
print(newTup)