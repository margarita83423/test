# # 3.1.Написать функцию, которая будет считать и возвращать сумму двух чисел. Если сумма больше 10 - вывести
# #  на экран “This sum is greater than 10. It’s {sum}”, если меньше - “This sum is less than 10. It’s {sum}”

# # x = 1
# # y = 2 
# # c = x+y
# # # print(c)

# # if c>10:
# # 	print("This sum is greater than 10." + "It’s" + str(c))
# # else:
# # 	print("This sum is less than 10." + "It’s" + str(c))

x = 1
y = 2
def res_sum(x,y):
	return x + y
	
result = res_sum(x, y)
if result > 10:
	print("This sum is greater than 10." + "It’s" + str(result))
else:
	print("This sum is less than 10." + "It’s" + str(result))	


# # 3.2.Написать функцию, которая будет принимать пароль. Если его длина не менее 
# # 10 символов вывести: “Your password is strong.” в противном случае “Your password is not strong enough.”

# s = "1234"
# if len(s) > 10:
# 	print("Your password is strong")
# else:
# 	print("Your password is not strong enough")

s = "1234"
def strong_pass(s):
	return(s)

new_result = len(s)
if len(s) < 10:
	print("Your password is not strong enough.")
else:
	print("Your password is strong.")

# 3.Белки проводят большую часть дня, играя. В частности, они играют, если температура 
# составляет от 60 до 90 (включительно). Если лето, то верхний предел температуры 
# равен 100 вместо 90. Напишите функцию, которая принимает температуру int и 
# логическое значение is_summer, верните True, если белки играют, и False в противном случае.

int1 = 80
is_summer = False


def squirrel(int, is_summer):
    if is_summer and int1 >=60 and int1 <= 100:
      print("True")
    elif not is_summer and int1 >=60 and int1 <=90:
      print("True")
    else:
      print("False")

squirrel(int1, is_summer)



