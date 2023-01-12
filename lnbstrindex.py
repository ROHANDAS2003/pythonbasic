string = input("Enter the string:\n")
if len(string)>7:
    print(string[0::2])
else:
    print(string[1::2])