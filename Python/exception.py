import sys
x = int(input("Input 1 "))
y = int(input("Input 2 "))

try:
    result = x/y
except ZeroDivisionError:
    print("Error: zero se divide nahi kar sakte!")
    sys.exit(1)

print(f"{x}/{y} = {result}")