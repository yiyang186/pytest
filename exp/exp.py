import math
import sys

if len(sys.argv) < 3:
    print('usage:', sys.argv[0], '<iteration>  <value>')
    sys.exit(0)

def arctanh(x):
    return 0.5*math.log((1+x)/(1-x))

def single_iter(i, x_cur, y_cur, angle_i): 
    angle_iter = arctanh(2**(-i))

    if angle_i > 0:
        d = 0
        angle_i = angle_i - angle_iter
    else:
        d = 1
        angle_i = angle_i + angle_iter
    #print(angle_i)

    x_next = x_cur + (-1)**d * y_cur * 2**(-i)
    y_next = y_cur + (-1)**d * x_cur * 2**(-i)
    x_cur = x_next
    y_cur = y_next

    return x_cur, y_cur, angle_i

ITER = int(sys.argv[1])
input_value = float(sys.argv[2])
sinh1 = math.sinh(input_value)
cosh1 = math.cosh(input_value)
exp1 = math.exp(input_value)

k = []
j = 1
for i in range(1, 10):
     j = 3*j + 1
     k.append(j)
print(k)

def cr_exp(input_value, iter=30):
    q = input_value // math.log(2)
    input_value = input_value % math.log(2)
    for i in range(1, ITER):
        if i == 1:
            x_cur = 1.20749706
            y_cur = 0
            angle_i = float(input_value)
        if i in k :
            # print(i)
            x_cur, y_cur, angle_i = single_iter(i, x_cur, y_cur, angle_i)
        x_cur, y_cur, angle_i = single_iter(i, x_cur, y_cur, angle_i)
        # print(angle_i)
        result = (x_cur + y_cur)*2**q
    return result

result = cr_exp(input_value, iter=ITER)
print('real value is %.20f' % exp1)
print('calculate by codic %.20f' % result)
print('exp absolute error is %.20e' % abs(result - exp1))
print('exp relative error is %.20e' % (abs(result - exp1)/exp1))

print('=========================')

res = 1 / (1 + cr_exp(-input_value, ITER))
res1 = 1 / (1 + math.exp(-input_value))
print('sigmoid cr_exp', res)
print('sigmoid exp', res1)
print('sigmoid absolute error is %.20e' % abs(res - res1))
print('sigmoid relative error is %.20e' % (abs(res - res1)/res1))
