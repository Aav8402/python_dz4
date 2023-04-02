# print('hello world')

# типы данных и переменная
# int, float, boolean,str, list, None


# value = None
# a = 123
# b = 1.23
# print(a)               вывод значений переменных
# print(b)
# value = 1234
# print(value)     




# value = None
# a = 123
# b = 1.23
# print(type(a))          #вывод типа данных переменных
# print(type(b))
# value = 1234
# print(type(value))

# s = 'hello "world"'
# print(s)                  # вывод строки     



# list = [1, 2, 3, 4.5, 'hello', True]
# print(list)                                        #Списки

#  Ввод и вывод данных
#  print()    Input()

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+', b, '=', a+b)                     # ТИП данных Вещественные


# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())                     #Целые

# print(a, '+', b, '=', a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')



# Арифметические операции

# a = 123
# b = 321
# c = a+b
# print(c)

# a = 12
# b = 8
# c = a/b
# print(c)                    #Для вещественных


# a = 12
# b = 8
# c = a//b
# print(c)                     #Для целых чисел


# a = 12
# b = 8
# c = a%b
# print(c)                    #Остаток от деления


# a = 2
# b = 8
# c = a**b
# print(c)                    #Возведение в степень


# a = 1.2
# b = 3
# c = round(a**b, 3)
# print(c)                      #Округление до 3го числа


# a = 3
# a+=5
# print(a)                        #Присваивание


# Логические операции


# a = 1<4 and 5>2
# print(a)


# a = 1<3<5<10
# print(a)


# func = 1
# T = 4
# x = 123
# print(func<T>(x))



# f = [1,2,3,4]
# print(f)
# print(not 2 in f)


# is_odd = not f[0] % 2 
# print(is_odd)


# Управляющие конструкции: if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)    


# username = input ('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Аня':
#     print('Привет, Аня!')
# else:
#     print('Привет, ', username,'!')              #Оператор elif


# original = 48
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)                                   #Оператор while




# for i in 1,2,3,4,5:
#     print(i**2)                                     #Оператор for



# list = [1, 2, 3, 10, 5]
# for i in list:
#     print(i)


# r = range(10)
# for i in r:
#     print(i)                                       #Перечисление от 0 до 9


# for i in range(5):
#     print(i)                                       #Перечисление 

# for i in range(1, 10):
#     print(i)                                         #Перечисление 

# for i in range(1, 10 , 2):
#     print(i)                                       #Перечисление от 1 до 9 с шагом 2


# for i in 'qwerty':
#     print(i)                                       #Перечисление        


# for i in 'qwe - rty':
#     print(i)                                       #Перечисление 


# Строка

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                                    #c
# print(text[1])                                    #ъ
# # print(text[len(text)])
# print(text[len(text)-1])                          #k
# print(text[-5])                                   #б
# print(text[:])                                    #print(text)
# print(text[:])                                    #съ
# print(text[len(text)-2])                          #ок
# print(text[2:9])                                  #ешь ещё
# print(text[6:-18])                                #ещё этих мягких
# print(text[0:len(text):6])                        #сеикакл    
# print(text[::6])                                  #сеикакл
# text = text[2:9] + text[-5] + text[:2]            # ...


#Списки list


# numbers = [1, 2, 3, 4, 5]
# # print(numbers)
# # ran = range(1, 6)
# # numbers = list(ran)
# # print(numbers)
# # numbers[0] = 10
# # print(numbers)
# for i in numbers:
#     i*=2
#     print(i)
#     # print(numbers)


#######################################


# Списки

# list1 = []
# list1 = list()
# list1 = [1, 2, 3, 4, 5]
# print(list1(1))


# list1 = [1, 5]
# print(list1)
# list1.append(8)
# print(list1)



# list1 = []
# print(list1)
# for i in range(5):
#     list1.append(i)
#     print(list1)

# Кортеж

# t = ()
# print(type(t))

# t = (1, 8, 9)
# print(t)

# a, b, c = t
# print(t)



# Словари

d ={}
d = dict()

d['q'] = 'qwert'
d['w'] = 'werty'
print(d)
print(d['q'])








