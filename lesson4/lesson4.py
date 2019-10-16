#4.1.  Сгенерировать случайное число с помощью randint и вывести его на экран
import random
run_numb = random.randint(1,100)
print(run_numb)

# 4.2. Дан список чисел [1,2,3,4,5,6]. 
# Перемешать список с помощью функции random.shuffle и вывести случайное число с помощью random.choice

# shuffle() рандомизирует элементы из списка.

ran_str = [1,2,3,4,5,6]
random.shuffle(ran_str)
print(ran_str)
print(random.choice(ran_str))



# 4.3.Сгенерировать случайное число с плавающей точкой с помощью random.random() и вывести его на экран
# Функция random() возвращает псевдослучайное число с плавающей точкой в диапазоне от 0.0 до 1.0.

rand_num = random.random()
print(rand_num)

# 4.4. Сгенерировать случайное число с плавающей точкой 
# в диапазоне от 0 до 25 с помощью random.uniform и вывести его на экран
unif_run = random.uniform(0, 25)
print(unif_run)

# 4.5. Есть список со словам “rock”, “scissors”, “paper”. Создайте прототип игры камень-ножницы-бумага 
# с компьютером, в основе которой будет находится функции random.choice и input()

user_result = input("Enter 'rock', 'scissors' or 'paper' \n")
forUser = user_result;
print(forUser)

import random

my_list = ["rock", "scissors", "paper"]
a = random.choice(my_list)
print(a)

def play(forUser, a):
	
	if forUser == a :
		print("Paly again")
	elif forUser == "rock" and a == "scissors":
		print("You are win")
	elif forUser == "scissors" and a == "paper":
		print("You are win")
	elif forUser == "paper" and a == "rock":
		print("You are win")
	else:
		print("Your loose")



play(forUser, a)