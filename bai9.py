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

mu = 2
dau = -1
first = 1
second = first + dau * x**mu / factorial(mu+1)
while (math.fabs(first - second) > eps):
    mu += 2
    first = second
    dau = -dau
    second = first + dau * x**mu / factorial(mu+1)
print(first)