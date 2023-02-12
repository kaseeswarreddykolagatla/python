def delchar(s,c):

    if(len(c)==1):
        for i in range(len(s)):
            if (c is not s[i]):
                print(s[i])
            else:
                continue
a=input("Enter A phase")
b=input("Enter the letter to be Deleted")
delchar(a,b)
