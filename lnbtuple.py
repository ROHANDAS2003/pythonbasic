Intnum=[]
for i in range(0,10):
    print(f"Enter number {i+1}:")
    Intnum.append(int(input()))
print("\nInput in integers are:\n",Intnum)

Bintuple=[]
for element in Intnum:
    Binnum = str(bin(element)).replace("0b", "")
    Binlist=[]
    for char in Binnum:
        Binlist.append(int(char))
    Bintuple.append(tuple(Binlist))
print("Input converted into binary are:\n",Bintuple)

AndRes = tuple(map(lambda i, j: i & j, Bintuple[-1], Bintuple[-2]))
print("\nResult of AND operation between last two Binary tuple is: ",AndRes)

OrRes = tuple(map(lambda i, j: i | j, Bintuple[-1], Bintuple[-2]))
print("Result of OR operation between last two Binary tuple is: ",OrRes)

string = ''
for element in AndRes:
    string = string + str(element)
AndResInt = int(string,2)
print("\nThe AND operation result in integer is: ", AndResInt)

string = ''
for element in OrRes:
    string = string + str(element)
OrResInt = int(string,2)
print("The OR operation result in integer is: ", OrResInt, end="\n\n")