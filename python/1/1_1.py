print(10) # 10

print(5 + 3 + 4) # 12

print(9 - 1) # 8

print(6 / 2) # 3.0

print((2 * 4) + (4 - 6)) # 6

a = 3
b = a + 1
print(a + b + a * b) # 19

print(a == b) # False

if b > a and b < a * b: # 4
    print(b)
else:
    print(a)
    
if a == 4: # 16
    print(6)
elif b == 4:
    print(6 + 7 + a)
else:
    print(25)
    
if b > a: # 6
    print(b + 2)
else:
    print(a + 2)

if a > b: # 16
    print(a * (a + 1))
elif a < b:
    print(b * (a + 1))
else:
    print(-1 * (a + 1))
