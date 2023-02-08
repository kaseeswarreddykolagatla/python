def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

n = int(input("Enter a positive integer: "))
result = is_happy(n)

if result:
    print("the number is a happy number.")
else:
    print("the number is not a happy number.")
