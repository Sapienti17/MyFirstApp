# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = input("Введите операцию: ")

# if ((c == "/") or (c == "mod") or (c == "div")) and (b == 0):
#     print("Деление на 0!")
# elif c == "*":
#     print(a * b)
# elif c == "+":
#     print(a+b)
# elif c == "-":
#     print(a-b)
# elif c == "/":
#     print(a/b)
# elif c == "mod" or "%":
#     print(a%b)
# elif c == "pow" or "**":
#     print(a**b)
# elif c == "div":
#     print(a//b)
##########################################################
# age = 32
# name = 'Артур'
# print('Возраст {0} -- {1} лет.'.format(name, age))
# print('Почему {0} забавляется с этим Python?'.format(name))
###########################################################
# length = 5
# breadth = 2
# area = length * breadth
# print('Площадь равна', area)
# print('Периметр равен', 2 * (length + breadth))

# genome = input()
# cnt = 0
# for nucl in genome:
#     if nucl == 'K':
#         cnt +=1
#     print(nucl)
# print(cnt)



# stroka = input()
# d = 0
# e = 0
# f = 0
# for i in stroka:
#     if i == "a":
#         d += 1
#     if i == "b":
# 	    e += 1
#     if i == "c":
# 	    f += 1
# print("a" + str(d)+ "b" + str(e) + "c" + str(f))


message = str(input())
cnt = 1
x = 1
j = message[x:x+1]
for i in message:
    if i in j:
        cnt += 1
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1
    x += 1
    j = message[x:x+1]
