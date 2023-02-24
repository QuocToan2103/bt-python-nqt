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

first = 1
mu = 1
second = 2 * (first * (mu + 2 ) * x**mu / mu)
while (math.fabs(first - second) > eps):
    mu += 2
    first = second
    second = 2 * (first * (mu + 2 ) * x**mu / mu)
print(first)