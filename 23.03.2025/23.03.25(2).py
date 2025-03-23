a = 5
b = 2
c = 1
if (b > a and b < c) or (b < a and b > c):
    print(b)
elif (a < c and a > b) or (a > c and a < b):
    print(a)
elif (c < a and c < b) or (c > a and c < b):
    print(c)