import math

def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))
    
print("Nhập x: ")
x = float(input())
print("Nhập eps: ")
eps = float(input())

mu = 1
dau = 1
first = 0
second = first + dau * x**mu / mu
while (math.fabs(first - second) > eps):   
    mu += 2
    dau = -dau
    first = second
    second = first + dau * x**mu / mu
print(first)