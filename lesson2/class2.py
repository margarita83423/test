# Выполнить вычисления, записать в переменную и вывести 
# в результате целую часть и дробную часть от деления:
# (a^c - b + d) / f
# 1. (15^2 - 20 + 5.5) / 6
# 2. (63/2 + 45 - 8) / 2^5
# 3. 7^3 + 20 * (10/3 + 6)
# 4. 83/8 * (43/20 + 5^7)
# 5. 72 + 36 / 7 * (72-6^5)




# full_part1 = ((15**2)-20+5.5)//6
# fraction_part1 = ((15**2)-20+5.5)%6
# print(full_part1, fraction_part1)


# full_part2 = ((63/2 + 45 - 8) // 2**5)/1
# fraction_part2 = (63/2 + 45 - 8) % 2**5
# print(result2, full_part2, fraction_part2)


# full_part3 = (7**3+20*(10/3+6))//1
# fraction_part3 = (7**3+20*(10/3+6))%1
# print(full_part3, fraction_part3)

# result5 = 72 + 36 / 7 * (72-6**5)
# full_part5 = (72 + 36 / 7 * (72-6**5))//1
# fraction_part5 = (72 + 36 / 7 * (72-6**5))%1
# print(result5, full_part5, fraction_part5)

# 2) Записать процесс вычисления в функцию, вызвать эту функцию с параметрами
a=2
c=3
b=7
d=9
f=6
def result(a,c,b,d,f):
	return (a**c - b + d) / f

one_res = result(a,c,b,d,f)
print(one_res)
# в принтах прописать деление по модулю и остаток

# h=1
# def result2(h):
# 	result 
# 	return(h)

# second_res = (result)/h
# print = second_res






# 3) Написать функцию, которая будет принимать номер телефона
#  и выводить его в формате +38 (099) 123 - 12 - 12
code1 = "+38"
code2 = "(099)"
code3 = "123"
code4 = "- 12"
code5 = "- 12"
def ph_number(code1, code2,code3, code4, code5):
	return(code1 + code2 + code3 + code4 +code5)

function_res = ph_number(code1, code2, code3, code4, code5)
print(function_res)

# 4) Написать функцию, которая будет принимать параметры: ФИО, дата рождения 
# и выводит информацию о возрасте в следующем формате: “Age for Фамилия Имя Отчество: 30 years”

name="dddd"
last="ggggg"
pat="hhhh"
age="1988"
	
def person(name, last, pat, age):
	
	return(name + last + pat + age)

func_result = person(name, last, pat, age)
print(func_result)


# 5) Найти в тексте https://ru.lipsum.com/feed/html подстроку “Sed”

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sollicitudin massa in sapien eleifend tempus. Cras ac nibh accumsan, porttitor erat vitae, commodo quam. Vestibulum quis sem tortor. Duis ac quam dui. Suspendisse eu ultrices velit. Suspendisse tempor odio ipsum, vel pretium ipsum suscipit et. Vivamus at aliquet augue. Vestibulum efficitur, tortor vel tempus imperdiet, diam ligula iaculis augue, id blandit diam tortor ac massa. Phasellus imperdiet eros ut porta rhoncus. Aliquam eget nibh purus. In eget tincidunt mi.Ut eleifend, enim vel porttitor lobortis, nisi tortor vestibulum augue, non porttitor dui nisi ut orci. Phasellus elementum varius libero id blandit. Mauris quis sodales ante, a tempus dui. Integer augue augue, volutpat ac elit quis, mollis fringilla enim. Etiam est diam, convallis ac orci sit amet, vehicula elementum neque. Pellentesque tempus lorem est, at ornare arcu sollicitudin vel. Duis sollicitudin venenatis metus ac egestas. Nulla lacinia ut elit sit amet scelerisque. Duis a turpis at purus posuere posuere nec sit amet neque. Suspendisse non pellentesque risus.Vestibulum auctor convallis gravida. Morbi risus nisi, maximus sed fringilla in, finibus vitae nibh. Nulla pulvinar et arcu id egestas. Ut porta ultricies lacinia. Quisque vel felis vulputate, commodo dui id, posuere arcu. Phasellus ac condimentum felis. Nulla ut felis euismod, lobortis est at, euismod justo. Vestibulum nec gravida eros. Phasellus quis pharetra urna, a cursus arcu. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;Proin tincidunt gravida nisl non hendrerit. Ut viverra egestas sapien. Phasellus rutrum nec diam gravida pulvinar. Donec porta, arcu nec ultrices pretium, sem eros tempus purus, rhoncus suscipit metus tortor non dolor. Curabitur consequat purus a mi aliquam, eget vehicula nulla sodales. Curabitur imperdiet blandit est et accumsan. Curabitur suscipit neque sit amet risus auctor ullamcorper. Morbi id iaculis felis. Donec sapien magna, hendrerit in enim vel, malesuada pretium arcu. Proin gravida scelerisque congue. Praesent a ultrices sapien, non laoreet sem. Pellentesque non aliquam massa. Aliquam ut risus non orci vehicula fringilla quis ut urna. Quisque vestibulum tortor blandit, porttitor mi id, rhoncus dui. Interdum et malesuada fames ac ante ipsum primis in faucibus. Ut vestibulum sit amet sem a sagittis.Donec sed nisi et mi tristique rutrum. Donec convallis pretium metus, vitae molestie elit blandit ac. Sed metus diam, hendrerit auctor facilisis eu, maximus eu eros. Duis consequat scelerisque sollicitudin. Donec tincidunt lorem sit amet volutpat maximus. Quisque risus est, dictum ut risus quis, malesuada sagittis risus. Ut at aliquam urna. Mauris lacus massa, viverra vel vulputate ut, dignissim nec libero. Praesent placerat, leo non ultrices finibus, mauris mi fringilla mauris, nec posuere eros lorem sollicitudin massa. Quisque blandit neque a purus dapibus euismod. Donec sed aliquet sapien. Nulla non ipsum venenatis nunc imperdiet ultrices. Sed consequat congue neque, id congue lorem dapibus ut. Nullam euismod dui dolor, ut convallis lectus maximus ac. Duis hendrerit diam in velit auctor, ac ullamcorper tortor commodo."
print(lorem.find("Sed"))
# //2595
# Возвращает наименьший индекс, по которому обнаруживается начало указанной подстроки в исходной.

# 6) Вывести первые 10 символов в строке

text = "a1b2c3h4k3n2m4"
print(text[:10])

# # 7) Вывести последние 25 символов в строке

text2 = "qwertyuiopasdfghjklzxcvbnm123456789dgdfgdfg"
print(text2[-25:])

# # 8)Вывести строку “HELLO WORLD” в нижнем регистре

lowerCase = "HELLO WORLD"
print(lowerCase.swapcase())

# 9) Вставить слова: ”I like {fruit} and {vegetables}” 
fruit = 'I like {}'.format('fruit')
vegetables = ' and {}'.format('vegetables')
print(fruit + vegetables)

# 10) "length - {}, width - {}, height - {}"
length1 = "length - {}".format('10')
width2 = " width - {}".format('20')
height3 = " height - {}".format('30')
print(length1 + width2 + height3)

# 11) Заменить слова Yes на No в строке: “Do you like summer? - Yes”
yesNo = "Do you like summer? -Yes"
no = yesNo.replace('Yes', 'No')
print(no)

# 12) "This is a {subj}. It's {prop}."
string1 = "This is a {}.".format('day')
string2 = "It's {}".format('good')
print(string1 + string2)

# 13) Убрать пробелы в строке “    Hello world!    ”
spaceString = "   Hello world!    "
lastSpace = spaceString.rstrip(" ")
firstSpace = lastSpace.strip(" ")
print(firstSpace)

# 14) Заменить в строке строчные буквы прописными, а прописные – строчными: “gOOD nIghT EVEryoNE!”
str = "gOOD nIghT EVEryoNE!"
newStr = str.swapcase()
print(newStr)

# 15) Есть две строки “Yes” и “No” преобразовать их в одну: “NoNoYesYesYes”
yes = "Yes"
not2 = "No"

yes, not2 = not2, yes
all = yes*2 + not2*3
print(all)




