import math
from sympy import *
# var 4
# f(x) = 1/2x^2 - sin(x) , [a, b] = [0, 1] , epsilon = 0.03

#method polovinnogo delenya
# Arguments of program
flag = False
x_1 = 0
x_2 = 0
x = 0
a = 0
b = 1
x_m = 0
y_m = 0
epsilon = 0.03


def main_function(arg):
    return 1/2 * arg ** 2 - math.sin(arg) 

while not flag:
    #1
    x_1 = (a+b-epsilon)/2
    x_2 = (a+b+epsilon)/2
    #2
    y1 = main_function(x_1) 
    y2 = main_function(x_2) 
    #3
    if y1 > y2:
        a = x_1
    else: 
        b = x_2
    #4
    if b - a <= 2 * epsilon:
        x_m = (a+b)/2 
        y_m = main_function(x_m) 
        flag = True

print("X_m=", x_m, " y_m=", y_m)


#method gold sechenyia
x_1 = 0
x_2 = 0
a = 0
b = 1
epsilon = 0.03
flag = False
i = 0
x = 0
while not flag:
    i = i + 1
    #1
    x_1 = b - (b-a)/1.618
    x_2 = a + (b-a)/1.618

    #2
    if main_function(x_1) >= main_function(x_2):
        a = x_1
    else:
        b = x_2
    
    if abs(b-a) < epsilon:
        x = (a+b)/2
        break

print("x1=", x_1, " x=", x)


#3 method hord       
flag = False
a = 0
b = 1
epsilon = 0.03

f_a = a-math.cos(a)
f_b = b - math.cos(b)

while not flag: 
    x_sh = a - (f_a/(f_a - f_b)) * (a-b)
    f_x_sh = x_sh-math.cos(x_sh)
    if abs(f_x_sh) <= epsilon:
        x_star = x_sh
        f_star = f_x_sh
        break
    if f_x_sh > 0:
        b = x_sh
        f_b = f_x_sh
        f_a = a-math.cos(a)
    else:
        a = x_sh
        f_a = f_x_sh
        f_b = b - math.cos(b)


print("x~ =", x_sh, " f* =", f_star)

#4 method nuitona
flag = False
i = 0
a = 0
b = 1
x_1 = 0

print("Метод Ньютона:")

while not flag:
    i = i + 1
    if i == 1:
        x_0 = 0.5
    else:
        x_0 = x_1
    x_1 = x_0 - (x_0 - cos(x_0))/(1+sin(x_0))

    if abs(x_1 - cos(x_1)) <= epsilon:
        x_star = x_1
        f_star = main_function(x_1)
        break

print("x*=", x_star, " y*=", f_star)