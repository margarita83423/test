# 1.Посчитать количество 9 в списке.
# list1 = [1,9,9,9,1,8]
# count = 0
# for element in list1:
# 	if element == 9:
# 		# print(element)
# 		count += 1

# print(count)

# 2.Вывести количество четный и нечетных елементов в рандомной последовательности.

# import random

# list2 = [60, 8, 3, 7]
# countEven = 0
# countOdd = 0
# for element in list2:
# 	if element % 2 == 0:
# 		# print(element)
# 		countEven = countEven + 1
# 	else:
# 		# print(element)
# 		countOdd = countOdd +1

# print(countEven)
# print(countOdd)


# # 3.Пользователь должен ввести последовательность чисел через пробел.Для каждого числа выведите 
# # слово YES (в отдельной строке), 
# # если это число ранее встречалось в последовательности или NO, если не встречалось.
# # l = input().split(',')

# # print(l)


# l = input().split(',')
# s = set(l)
# print(s)

# # for element in l:
# # 	if element in s:
# # 		print("No")
	

# 8) Вывести последовательность Фибоначчи где количество элементов последовательности задается пользователем
# https://younglinux.info/algorithm/fibonacci

fib1 = 1
fib2 = 2

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
 
print(fib2)



# 6.С помощью random сгенерировать 2 целых числа и спросить у пользователя ответ суммы этих чисел.
#  Если пользователь посчитал верно то засчитать ему одно очко. Повторять пока пользователь не введет ‘q’.
import random
n1 = (random.randint(0,2))
n2 = (random.randint(0,2))
sum = n1 + n2
print("my sum is " + str(sum))

i = 0

while i < 5:
  n3 = input("enter result for sum " + str(n1) + " and " + str(n2) + "\n")
  user = n3
  q = "q"
  if user == "q":
    print("by")
    break
  elif int(user) == sum:
    print("you win")
    continue
  elif int(user) != sum:
    i = i + 1
    print("not win, your score id " + str(i))
	

# 5) Посчитать факториал для введенного пользователем числа.
# number = int(input("Введите число: "))
# factorial = 1
# for i in range(1, number+1):
#     factorial *= i
# print("Факториал числа", number, "равен", factorial)



upper = False
number = 0
longg = False
passwordWrong = True

password = input("pls enter a password" + "\n")
password = str(password)

if len(password) >= 5:
  longg = True

for letter in password:
  if letter.isupper():
    upper = True
    break

for letter2 in password:
  if letter2.isdigit():
    number = number + 1

if upper and number >= 5 and longg:
  print("Your password is strong")
else: 
  print('Your password is not strong enough.')