
# 2.#Записать в файл слова, которые нужно будет угадать.
# #В коде открыть файл и выбрать рандомно одно слово, которое пользователь должен угадать. 
#Дальше просим пользователя ввести по одной букве в слове.
#Если такой буквы нет - рисуем человечка на виселице
from random import choice, randint
words = ('компьютер', 'тетрадь', 'монитор', 'чашка', 'часы', 'игла',
'ножницы', 'ручка', 'карандаш', 'линейка')
descriptions = ('Устройство, спсобное выполнять операцию или ряд операций','Тонкая брошюра для письма', 'Стеклянные сосуд для напитков', 'Устройство для определения времени', 'Острая швейная...', 'Металлические ножи для резки бумаги', 'Гелевое или масляное устройство для начертания знаков','Инструмент для начертания знаков с графитным стержнем внутри', 'Устройство для измерения длинны чётко отведеннного промежутка пространства')
  
def fine(i):
      print(process[i])
      return i+1
  
process = ('''
         -----------
         |         |
         |        ---
         |
         |
         |
         |
         |
         |
        ---
  
      ''',
      '''
         -----------
         |         |
         |        ---
         |         O
         |
         |
         |
         |
         |
        ---
  
      ''',
      '''
         -----------
         |         |
         |        ---
         |         O
         |         |
         |         |
         |
         |
         |
        ---
  
      ''',
      '''
         -----------
         |         |
         |        ---
         |         O
         |        /|
         |         |
         |
         |
         |
        ---
  
      ''',
      '''
         -----------
         |         |
         |        ---
         |         O
         |        /|\
         |         |
         |
         |
         |
        ---
  
      ''',
      '''
         -----------
         |         |
         |        ---
         |         O
         |        /|\
         |         |
         |        /
         |
         |
        ---
  
      ''',
      '''
         -----------
         |         |
         |        ---
         |         O
         |        /|\
         |         |
         |        / \
         |       -----
         |       |   |
        ---
  
      ''',
      '''
         -----------
         |         |
         |        ---
         |         O
         |        /|\
         |         |
         |        / \
         |
        ---
  
      ''')
  
  
print('1 - Играть')
print('2 - Выйти')
result = int(input('Введите 1/2.\n'))
if result == 2:
	exit()
	
if result == 1:
    k = randint(0, 8)
    print('Угадайте:')
    print(descriptions[k])
    word = words[k]
    word_inp = '_'*len(word)
for c in word_inp:
    print(c, end=' ')
print(word_inp)
i = 0
while word != word_inp and i < len(process):
    char = input('Ваша буква: ')
    if len(char) > 1:
        char = char[0:1]
    char = char.lower()
    if char in word:
        if not(char in word_inp):
            print('Yep!')
    else:
        i = fine(i)


# 1.Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало 
# являются простыми числами: 197, 719 и 971. Существует тринадцать таких простых чисел меньше 100: 2, 
# 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97. Сколько существует круговых простых чисел меньше миллиона?
# def isSimple(variable):
#   if variable % 2 == 0:
#     return False
#   if variable % 3 == 0:
#     return False

#   d = variable - 1 
#   while d > 3:
#     if variable % d:
#       d = d - 1
#     else: 
#       return False
#   return True; 

# def isListSimple(myList):
#   for j in myList:
#     if isSimple(j) == False:
#       return False
#   return True

# def shuffleInteger(integer):
#   my_digits = [str(i) for i in str(integer)]
#   result = [integer]
#   for i in range(len(my_digits) - 1):
#     a = len(my_digits) - 1
#     my_digits = [my_digits[a]] + my_digits[:a]
#     newString = ''.join(my_digits)
#     newInt = int(newString)
#     result.append(newInt)
  
#   return result

# def findSimpleIntegers(inRange = 100):
#   result = []
#   for i in range(2, inRange):
#     if isSimple(i):
#       result.append(i)

#   return result

# def filterRoundIntegers(listOfInts):
#   result = []
#   for i in listOfInts:
#     shuffled = shuffleInteger(i)
#     if isListSimple(shuffled):
#       result.append(i)

#   return result

# simpleIntergers = findSimpleIntegers(10000)

# filteredRound = filterRoundIntegers(simpleIntergers)
# print(filteredRound)