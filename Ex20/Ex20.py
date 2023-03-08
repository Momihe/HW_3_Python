# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость 
# введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# *Пример:*

#    н   о   у   т   б   у   к
#    1   1   2   
#     12

word = (input('Введите свое слово: '))
a = word.upper()
price = 0
dictinary = {1 : 'АВЕИНОРСТ', 2 : 'ДКЛМПУ', 3 : 'БГЁЬЯ', 4 : 'ЙЫ', 5 : 'ЖЗХЦЧ', 8 : 'ШЭЮ', 10 : 'ФЩЪ'} 
for s in range(len(a)):
      for (k,v) in dictinary.items():
         for i in v:
             if a[s] == i:
                 price += k 
                 print(f'Буква {i} стоит {k}.')
print(f'Слово "{word}" стоит {price} очков.')
      