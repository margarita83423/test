# # 1. Написать функцию, которая будет принимать температуру по цельсию и 
# # возвращать ее 
# # перевод в температуру по фаренгейту по формуле: (temp - 32) * (5/9)

# # tempStr = input("Enter the temp" + "\n")
# # temp = int(tempStr)

# # def newTemp(temp):
# # 	a = (temp - 32) * (5/9)
# # 	print(a)
# # 	return a

# # newTemp(temp)

# # 2.Написать функцию поиска минимума 
# # в произвольном количестве элементов переданных в функцию
# # b = [11,8,12,1] 
# # def minB(b):
# # 	sortB = sorted(b)
# # 	print(sortB[0])
# # 	return sortB

# # minB(b)


# # 3.Написать функцию которая принимает два аргумента: первый аргумент отвечает за выбор пользователя: минимум
#  # или максимум, второй 
# # аргумент - список элементов в котором нужно найти минимум или максимум
# # добавить в словарь две функции мин и макс 

# lst = [10, 3, 6, 5, 7]
 
# mins = lst[0]
# for i in lst:
#     if i < mins:
#         mins = i
        
# lst = [10, 3, 6, 5, 7]
 
# maxx = lst[0]
# for i in lst:
#     if i > maxx:
#         maxx = i
        
# choice = input("Enter mins or max" + "\n")

# def userCh(mins, maxx, choice):
# 	if choice == "mins":
# 		print(mins)
# 		return mins
# 	else:
# 		print(maxx)
# 		return(maxx)

# userCh(mins, maxx, choice)

# # 4.Написать функцию пересечения и функцию объединения неограниченного количества последовательностей
# aa = [1, 2, 3, 4, 5]
# bb = [3, 4, 5, 6, 7]
# cc = []
# dd = []

# def combine(aa, bb, cc):
#   for i in bb:
#     for j in aa:
#       if i == j:
#         cc.append(i)
#   print(cc)
  
# combine(aa, bb, cc)

# def remove(aa, bb, dd):
#   for i in aa:
#     if i not in bb:
#       dd.append(i)

#   for j in bb:
#     if j not in aa:
#       dd.append(j)
#   print(dd)

# remove(aa, bb, dd)


# 7. Написать функцию для подсчета периметра фигуры в зависимости от того какую фигуру укажет пользователь
figure = input("Enter square, triangle or rectangle" + "\n")

def summa_square():
  res1 = input("Please, enter square side" + "\n")
  res1 = int(res1)
  res1 = res1*4
  return(res1)

def summa_triangle():
  a = input("Please, enter triangle 1 side" + "\n")
  b = input("Please, enter triangle 2 side" + "\n")
  c = input("Please, enter triangle 3 side" + "\n")
  res1 = int(a) + int(b) + int(c)
  return(res1)


def summa_rectangle():
  a = input("Please, enter rectangle 1 side" + "\n")
  b = input("Please, enter rectangle 2 side" + "\n")
  res1 = 2(int(a) + int(b))
  return(res1)

perimetr = 0
if figure == "square":
  perimetr = summa_square()

if figure == "triangle":
  perimetr = summa_triangle()

if figure == "rectangle":
  perimetr = summa_rectangle()

print(perimetr)



# def figur(*long):
#     sum = 0
    
#     for n in long:
#         sum += n

#     print("Sum: ", sum)

# figur(3, 5, 6)




