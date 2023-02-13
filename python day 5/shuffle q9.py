def shuffle(11,12):
    output= []
    for i in range(len(11)):
        output.append(11[i])
        if i<len(12):
            output.append(12[i])
        if len(11)<len(12):
            output=output+12[len(11):]
        print("shuffled list =",output)

n = int(input("Enetr the number of elements of 11: "))
11=[]
for i in range(n):
    element = int(input("Enter the elements: "))
    11.append(element)

m=int(input("Enter the number of elements of 12: "))
12=[]
for i in range(m):
    element = int(input("Enter the element: "))
    12.append(element)
    shuffle(11,12)
