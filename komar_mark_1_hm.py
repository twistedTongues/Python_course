print("Не знаю, как там в Лондоне, я не была. Может, там собака — друг \
 человека. А у нас управдом — друг человека!")

# 1
string = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг \
 человека. А у нас управдом — друг человека!"
s1 = 'Количество символов - '
i = len(string)
print("1." + s1 + "" + str(i))
# 2
print("2." + "Перевернул строку - " + "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека.\
     А у нас управдом — друг человека!"[::-1])
# 3
print("3." + "Сделал каждое слово с большой буквы -" + " " + string.title())
# 4 Я не совсем понимаю, что такое прописными, если имеется ввиду все
# маленькими, тогда заменить на lower надо
print("4." + "Сделал весь текст прописными буквами -" + " " + string.upper())
# 5
num = "Число вхождений (нд, ам, o) в строку - "

nd = string.count("нд")
am = string.count("ам")
o = string.count("о")
print("5." + num + str(nd) + ", " + str(am) + ", " + str(o) + ".")

# 6
print("6." + "Вывести только некоторую часть текста - " + string[:38])
