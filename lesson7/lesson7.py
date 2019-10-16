#1. Подсчитать количество каждого элемента в списке. Результат в виде словаря

# l = input().split(',')
# d ={}
# for elem in l:
# 	if elem in d:
# 		d[elem]=d[elem]+1
# 	else:
# 		d[elem]=1
# print(d)

# # 2.Вывести количество четный и нечетных елементов в рандомной последовательности.Результат в виде словаря
# import random

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(-10, 10))

# print(numbers)

# even = 0
# odd = 0

# for number in numbers:
#     if number % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
        
# print("Even: %d, odd: %d" % (even, odd))


# # 10) необходимо объединить два прайс-листа (задаются в виде словарей) с тем условием, что если наименование товара присутствует в обоих прайсах,
# #  то в итоговый прайс помещается тот, чья цена выше. (с помощью списковых включений)

# dict1 = {'яблоки':100, 'груши':13, 'арбузы':20, 'картофель':15, 'алыча':22}
# dict2 = {'яблоки':150,'груши':18,'ананасы':45, 'апельсины':30, 'киви':35}
# dict_itog = {}
# for i in dict1.keys():
#     if i in dict2.keys():
#         dict_itog[i]=max(dict1[i],dict2[i])
#         dict2.pop(i)
#     else:
#         dict_itog[i] = dict1[i]
# print(dict(dict2.items() | dict_itog.items()))

# # 8. Написать функцию, которая генерирует матрицу размером n*n с рандомными числами. Размер указывает пользователь
# # import random  
# import random
# ma1 = 2
# ma2 = 5

# matrix = [[random.randrange(0,10) for y in range(ma2)] for x in range(ma1)]

# print(matrix)


# # 4.Вам дан словарь, состоящий из пар слов. {“Hello”: “Hi”, “Bye”: “Goodbye”, “List”: “Array”} Каждое слово 
# # является синонимом к 
# # парному ему слову. Все слова в словаре различны. Определить синоним для слова введенного пользователем.

# d = {"Hello":"Hi", "Bye":"Goodbye"}
# n = input("Enter")

# for word in d.keys():
# 	if word == n:
# 		w = word[d]:
# 		print(w)


# 10) необходимо объединить два прайс-листа (задаются в виде словарей) с тем условием, что если наименование товара присутствует 
# в обоих прайсах, то в итоговый прайс помещается тот, чья цена выше. (с помощью списковых включений)

# pr1 = {'apple':100, 'tea':13, 'coffee':20, 'dog': 12}
# pr2 = {'apple':80, 'tea':10, 'coffee':20, 'cat':30}

# res_dict = {}
# for i in pr1.keys():
# 	if i in pr2.keys():
# 		res_dict[i] = max(pr1[i], pr2[i])
	

# print(res_dict)


# 5) Пользователь вводит список чисел через пробел, вывести новый список
#  в котором элементы из введенного пользователем списка будут умножены на 2 с помощью списковых включений.
a1 = input("enter numbers").split(',')

newList = []
for i in a1:
  newList.append(int(i)) 

res1 = [x*2 for x in newList]
print(res1)


# 6) Пользователь вводит список чисел через пробел, вывести новый список содержащий 
# только четные элементы (с помощью списковых включений)

a = input("Enter the number").split()
b_list = []
c_list = []
i = 0
for i in a:
  b_list.append(int(i))

c_list = [x for x in b_list if x % 2 == 0]
# for x in b_list:
#   if x % 2 == 0:
#     c_list.append(int(x))

print(c_list)

# 7) Дан список чисел от 1 до 31, обозначающий дни в месяце. Вывести список только рабочих дней месяца без выходных.(с помощью списковых включений)

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
# days_a1 = []
# days_a2 = []


c_list = [x for x in days if x <= 5 or (x >= 8 and x <= 12) or (x >= 15 and x <= 19)]

# for x in days:
#   if x < 6:
#     days_a1.append(int(x))
#   if x >7 and x<13:
#     days_a2.append(int(x))


print(str(c_list))
# print("Second week" + str(days_a2))