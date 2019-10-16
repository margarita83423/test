# # 5.1.Дан список чисел L. Написать функцию, которая вернет True если сумма 
# # первых 4 элементов списка равны 9. При этом функция должна вызываться только если длина списка больше 4.


# 2, 2, 3, 2
my_l = [2, 2, 3, 2, 6, 7]
s = sum(my_l[0:4])
i_lengh = len(my_l)

def sum1(s, i_lengh):
	if s == 9 and i_lengh > 4 :
		print("True")
	else:
		print("False")

sum1(s, i_lengh)


# # 5.6.Перевернуть список: [1,2,3,4] => [4,3,2,1]

turn_list1 = [1,2,3,4]
turn_list1.reverse()
print(turn_list1)

# # 5.3.Написать функцию, которая принимает список как 
# # аргумент и возвращает True если первый и последний элемент в списке равен 6

list2 = [6, 1, 3, 4, 1]

def list_func(list2):
	if list2[0] == 6 and list2[-1] == 6:
		print("True")
	else:
		print("False")

list_func(list2)

# # 5.4.Написать функцию, которая принимает 2 списка и возвращает True 
# # если первые или последние элементы списка равны

lis1 = [1,2,3,4]
lis2 = [1,3,2,4]

def equality(lis1, lis2):
	if (lis1[0] == lis2[0]) or (lis1[-1] == lis2[-1]):
		print("True")
	else:
		print("False")

equality(lis1, lis2)


# 5.5. Написать функцию, которая принимает 3 списка и возвращает их общую сумму элементов

listt1 = [1, 1]
listt2 = [1]
listt3 = [1]

def addlistts(listt1, listt2, listt3):
	joinedlistt = listt1 + listt2 + listt3
	print(joinedlistt)
	sumFromList = sum(joinedlistt)
	print(sumFromList)

addlistts(listt1, listt2, listt3)


# 7)	Определить самый большой элемент списка и заменить им все элементы. Длина списка не больше 5

a_list = [2, 1, 4, 3, 5]
b_list = sorted(a_list)


if(b_list[-1] > a_list[0]):
  a_list[0] = b_list[-1]
if(b_list[-1] > a_list[1]):
  a_list[1] = b_list[-1]
if(b_list[-1] > a_list[2]):
  a_list[2] = b_list[-1]
if(b_list[-1] > a_list[3]):
  a_list[3] = b_list[-1]
if(b_list[-1] > a_list[4]):
  a_list[4] = b_list[-1]

print(a_list)
print(b_list)

# 8)	Написать функцию, которая вернет сумму первых 2 элементов в списке. Если длина списка 
# меньше 2, просто суммируйте существующие элементы, возвращая 0, если массив имеет длину 0.

a_list1 = [1,2]


def lenSum(a_list1):
  lenForA = len(a_list1)

  if lenForA >= 2:
    print(a_list1[0]+a_list1[1])
  elif lenForA < 2 and lenForA > 0:
    print(a_list1[0]+0)
  else:
    print(0)


lenSum(a_list1)


# 5.9)	Дано 2 списка int, a и b, длина каждого равна 3.Написать функцию, 
# которая принимает оба списка и возвращает новый список длиной 2, содержащий их средние элементы.
int1 = [2,3,4]
int2 = [7,8,9]

def newInt3(int1, int2):
  joinInt = int1[1], int2[1]
  print(joinInt)


newInt3(int1, int2)

# 10)	 Написать функцию, которая принимает список как аргумент и 
# возвращает True если цифры 2 и 3 есть в этом списке


int_list1 = [4, 4, 88, 22]

def newIntList(int_list1):
  if 2 in int_list1:
    print("true")
  elif 3 in int_list1:
    print("true")
  else:
    print("false")

newIntList(int_list1)


# 11) Дан список чисел [1,2,3,2,1]. Определите, сколько в нем встречается различных чисел.
intCount = [1,2,3,2,1]
first = intCount.count(1)
second = intCount.count(2)
third = intCount.count(3)
print(first, second, third)

# 12) Даны два списка чисел: [1, 3, 2], [4, 3, 2] Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

li1 = [1, 3, 2]
li2 = [4, 3, 2]

li3 = li1 + li2
int_li1 = li3.count(1)
int_li2 = li3.count(2)
int_li3 = li3.count(3)
int_li4 = li3.count(4)
print(int_li1, int_li2, int_li3, int_li4)


# 13) Даны два списка чисел: [1, 2, 6, 4, 5, 7], [10, 2, 3, 4, 8] Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.

num1 = [1, 2, 6, 4, 5, 7, 8]
num2 = [10, 2, 3, 4, 8]
num3 = []

if 1 in num1 and 1 in num2:
  num3.append(1)
if 2 in num1 and 2 in num2:
  num3.append(2)
if 3 in num1 and 3 in num2:
  num3.append(3)
if 4 in num1 and 4 in num2:
  num3.append(4)
if 5 in num1 and 5 in num2:
  num3.append(5)
if 6 in num1 and 6 in num2:
  num3.append(6)
if 7 in num1 and 7 in num2:
  num3.append(7)
if 8 in num1 and 8 in num2:
  num3.append(8)
if 9 in num1 and 9 in num2:
  num3.append(9)
if 10 in num1 and 10 in num2:
  num3.append(10)
else:
  print("false")

print(sorted(num3))


# 14) Посчитать количество слов в первом абзаце текста: https://ru.lipsum.com/feed/html
loremString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam a lorem purus. In hac habitasse platea dictumst. Nunc ante elit, vulputate non volutpat sed, varius porta ligula. Duis varius faucibus nisl, a consequat mi. Ut lectus metus, lobortis a sem a, pulvinar ornare eros. Etiam non finibus sapien. Donec consectetur justo turpis, sed vehicula risus faucibus sed. Aenean lorem eros, tempus vel augue sagittis, malesuada volutpat nibh."

loremList = loremString.split()
words = len(loremList)
print(words)


# 2.Написать функцию, которая будет возвращать True если в списке,
#  который передается функции как аргумент присутствует последовательность чисел 1, 2, 3, 4
listWord = [1,2,3,4]
if (listWord[0] == 1) and (listWord[1] == 2) and (listWord[2]==3) and (listWord[3] == 4):
  print ("True")
else:
  print("False")