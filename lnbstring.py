para = input("Enter a sentence or paragraph: ")
lst = para.split(" ")

newlst=[]
for element in lst:
    if len(element)>4:
        newlst.append(element)

print(newlst)