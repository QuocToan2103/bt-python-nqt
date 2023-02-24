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
first = 0
second = - first - x**mu/ mu
while (math.fabs(first - second) > eps):
    mu = mu + 1
    first = second
    second = - first - x**mu / mu
print(first)