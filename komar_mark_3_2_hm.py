a = int(input())
b = int(input())
c = int(input())

# 1
res = a and b and c and "Нет нулевых значений!!!"
print(res)
# 2
res_2 = a or b or c or "Введены все нули!"
print(res_2)
# 3, 4
if a > (b + c):
    print(a-b-c)
else:
    print(b + c - a)
# 5
if a > 50 and b > a or c > a:
    print('Vasya')
# 6
if a > 5 or b == 7 and c == 7:
    print('Petya')
