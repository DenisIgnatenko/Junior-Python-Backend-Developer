# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Укажите значение для переменной beaufort и запустите код.

# for current_hour in range(0, 24):
#     print("На часах " + str(current_hour) + ":00.")
#     # Вместо многоточий напишите код
#     if current_hour < 6:
#         print('Доброй ночи!')
#     elif current_hour < 12:
#         print('Доброе утро!')
#     elif current_hour < 18:
#         print('Добрый день!')
#     elif current_hour < 23:
#         print('Добрый вечер!')
#     else:
#         print('Доброй ночи!')
#
#     # Допишите программу

# # Код функции say_hello()
# def say_hello(current_hour):
#     if current_hour <= 5 or current_hour >= 23:
#         print('Доброй ночи!')
#     elif current_hour >= 6 and current_hour <= 11:
#         print('Доброе утро!')
#     elif current_hour >= 12 and current_hour <= 17:
#         print('Добрый день!')
#     elif current_hour >= 18 and current_hour <= 22:
#         print('Добрый вечер!')
#
#
# def say_about():
# # Код, написанный ниже, переместите в тело объявленной функции
#     print('Привет, я Анфиса!')
#     print('Я персональный помощник.')
#     print('Я ещё маленькая,')
#     print('но постоянно расту и умнею:')
#     print('ведь мой код каждый день дописывают!')
#
# # Ниже вызовите объявленную вами функцию say_about()
# say_about()
# Объявите функцию здесь
# def print_friends_count(friends_count):
#     if friends_count == 0:
#         print('У тебя нет друзей')
#     elif friends_count == 1:
#         print('У тебя', friends_count, 'друг')
#     elif friends_count >= 2 and friends_count <= 4:
#         print('У тебя', friends_count, 'друга')
#     elif friends_count >= 5 and friends_count < 20:
#         print('У тебя', friends_count, 'друзей')
#     else:
#         print('Ого, сколько у тебя друзей! Целых', friends_count)
#
# print_friends_count(10)
# print_friends_count(2)
# print_friends_count(25)

#
# def print_friends_count(friends_count):
#     if friends_count == 0:
#         print('У тебя нет друзей')
#     elif friends_count == 1:
#         print('У тебя', friends_count, 'друг')
#     elif friends_count >= 2 and friends_count <= 4:
#         print('У тебя', friends_count, 'друга')
#     elif friends_count >= 5 and friends_count < 20:
#         print('У тебя', friends_count, 'друзей')
#     else:
#         print('Ого, сколько у тебя друзей! Целых', friends_count)
#
# for i in range(21):
#     print_friends_count(i)
#
# def print_home(name = 'По умолчанию', planet = 'По умолчанию'):
#     print(name, 'привет на планете', planet)
#
# print_home('Иван', 'Земля')

# flat = [
#     5.55, 22.19, 7.78, 26.86, 5.55,
# #     29.84, 22.19, 5.55, 16.85, 4.52
# # ]
# #
# # room_size = 22.19
# # count = 0
# # sum_area = 0
# #
# # for room in flat:
# #         sum_area += room
# #         count += 1
# #
# # print('Комнат в квартире:', str(count))
# # print('Общая площадь квартиры:', str(sum_area))
#
# # Объявите функцию rooms_equal() с параметрами room_size и room_list
# # Перенесите следующий код в тело функции, которую вы объявили
# def rooms_equal(room_size, room_list):
#     count = 0
#
#     for room in room_list:
#         if room == room_size:
#             count = count + 1
#
#     print('Комнат площадью', room_size, 'кв.м:', count)
#
#
# # Следующий код не изменяйте и не переносите в тело функции
# flat = [
#     5.55, 22.19, 7.78, 26.86, 5.55,
#     29.84, 22.19, 5.55, 16.85, 4.52
# ]
#
# hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]
#
# rooms_equal(5.55, flat)
# rooms_equal(9.2, hut)
# # Добавьте ещё один вызов функции rooms_equal()
# # Передайте в функцию искомую площадь - 9.2 кв.м и список hut
# # def number_of_occurrences(char, string):
# #     # Здесь объявите переменную count, равную нулю.
# #     # Она будет хранить количество вхождений
# #     count = 0
# #     for letter in string:
# #         # Напишите условие: сравните переменные letter и char
# #         # И если letter равна char - увеличивайте счётчик count на 1
# #         if letter == char:
# #             count += 1
# #
# #     # Печатаем исходную строку:
# #     print('Исходная строка:', string)
# #     # Печатаем результат подсчётов:
# #     print('Количество вхождений символа', char, 'составляет:', count)
# #
# #
# # # Код ниже не изменяйте
# # phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'
# #
# # # Вызываем функцию number_of_occurrences(), чтобы она посчитала,
# # # сколько раз во фразе phrase встречается буква 'е'
# # number_of_occurrences('е', phrase)
#
# # may_2017 = [24, 26, 15, 10, 15, 19, 10,
# #             1, 4, 7, 7, 7, 12, 14, 17,
# #             8, 9, 19, 21, 22, 11, 15,
# #             19, 23, 15, 21, 16, 13, 25,
# #             17, 19
# #             ]
# #
# # may_2018 = [20, 27, 23, 18, 24, 16, 20,
# #             24, 18, 15, 19, 25, 24, 26,
# #             19, 24, 25, 21, 17, 11, 20,
# #             21, 22, 23, 18, 20, 23,
# #             18, 22, 23, 11
# #             ]
# #
# # def comfort_count(temperatures):
# #     temp_count = 0
# #
# #     for temp in temperatures:
# #         if 22 <= temp <= 26:
# #             temp_count += 1
# #
# #     print('Количество тёплых месяцев:', str(temp_count))
# #
# #
# # # Дальше код не меняйте
# # comfort_count(may_2017)  # Узнаем, что было в мае 2017 г.
# # comfort_count(may_2018)  # Узнаем, что было в мае 2018 г.
#
# # may_2017 = [24, 26, 15, 10, 15, 19, 10, 1,
# #             4, 7, 7, 7, 12, 14, 17, 8, 9,
# #             19, 21, 22, 11, 15, 19, 23, 15,
# #             21, 16, 13, 25, 17, 19
# #             ]
# #
# # # Допишите эту функцию
# # def comfort_count(temperatures):
# #     count = 0
# #     for temp in temperatures:
# #         if 22 <= temp <= 26:
# #             count += 1
# #     return count
# #
# # # Код ниже не изменяйте:
# # # вызовем функцию comfort_count(), передадим в неё список may_2017,
# # # результат работы сохраним в переменную nice_days
# # nice_days = comfort_count(may_2017)
# #
# # # Напечатаем значение, сохранённое в nice_days
# # print('Количество тёплых дней в этом месяце:', nice_days)
#
# # Функция для вычисления периметра куба.
# def calc_cube_perimeter(side):
#     return side * 12
#
# # Присвойте переменной one_cube_perimeter значение,
# # которое вернёт функция calc_cube_perimeter() с аргументом 3:
# # 3 метра - это длина ребра куба.
#
# one_cube_perimeter = 3
#
# # Вычислите общую длину палок, необходимых
# # для строительства 8 кубов,
# # и сохраните это значение в переменную full_length
# full_length = calc_cube_perimeter(one_cube_perimeter)
#
# # А теперь напечатаем результат (в этой строке ничего изменять не нужно)
# print('Необходимый метраж палок для 8 кубов:', full_length)
#
# # Функция для вычисления площади куба.
# def calc_cube_area(side):
#     # Формулу для вычисления площади одной грани куба Афанасий написал:
#     one_face = side * side
#
#     # Вычислите полную площадь куба: у него шесть одинаковых граней.
#     cube_area = one_face * 6
#
#     return cube_area
#
# # Присвойте переменной one_cube_area значение,
# # которое вернёт функция calc_cube_area() с аргументом 3:
# # 3 метра - это длина ребра куба.
# one_cube_area = calc_cube_area(3)
#
# # Вычислите общую площадь стекла, необходимого
# # для строительства 8 кубов,
# # и сохраните это значение в переменную full_area
# full_area = one_cube_area * 8
#
# print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)
#
# # Функция для вычисления периметра куба.
# def calc_cube_perimeter(side):
#     return side * 12
#
# # Вызов функции calc_cube_perimeter() с аргументом 3
# one_cube_perimeter = calc_cube_perimeter(3)
# full_length = one_cube_perimeter * 8
# print('Необходимый метраж палок для 8 кубов:', full_length)
#
# # Функция для вычисления площади куба.
# def calc_cube_area(side):
#     one_face = side * side
#     cube_area = one_face * 6
#     return cube_area
#
# # Вызов функции calc_cube_area() с аргументом 3
# one_cube_area = calc_cube_area(3)
# full_area = one_cube_area * 8
# print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)
#
#
#
# # Функция для вычисления периметра куба.
# def calc_cube_perimeter(side):
#     return side * 12
#
# # Функция для вычисления площади куба.
# def calc_cube_area(side):
#     one_face = side * side
#     cube_area = one_face * 6
#     return cube_area
#
# # Основная функция, которая принимает длину ребра куба
# def calc_cube(side):
#     # Вызываем функцию, рассчитывающую периметр
#     # и передаём в неё размер куба
#     one_cube_perimeter = calc_cube_perimeter(side)
#     full_length = one_cube_perimeter * 8
#
#     # Вызываем функцию, рассчитывающую площадь стекла
#     # и передаём в неё размер куба
#     one_cube_area = calc_cube_area(side)
#     full_area = one_cube_area * 8
#
#     print('Для 8 кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)
#
# # В результате остался лишь один вызов "основной" функции,
# # а она уже вызовет две вспомогательные
# calc_cube(3)
#
#
# # Функция для вычисления периметра кубов.
# def calc_cube_perimeter(side):
#     return side * 12
#
# # Функция для вычисления площади кубов.
# def calc_cube_area(side):
#     one_face = side * side
#     cube_area = one_face * 6
#     return cube_area
#
# # Дополните объявление функции:
# # теперь должна принимать два параметра -
# # длину ребра куба и количество кубов.
# def calc_cube(side, amount):
#     # Вызываем функцию, рассчитывающую периметр
#     # и передаём в неё размер куба
#     one_cube_perimeter = calc_cube_perimeter(side)
#
#     # Здесь вместо многоточия должна стоять переменная,
#     # хранящая количество кубов, переданное во втором аргументе.
#     full_length = one_cube_perimeter * amount
#
#     # Вызываем функцию, рассчитывающую площадь стекла
#     # и передаём в неё размер куба
#     one_cube_area = calc_cube_area(side)
#
#     # Здесь вместо многоточия должна стоять переменная,
#     # хранящая количество кубов, переданное во втором аргументе.
#     full_area = one_cube_area * amount
#
#     # В этой строке замените многоточие на переменную, хранящую количество кубов
#     print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)
#
#
# # Для проверки работы кода вызываем функцию с двумя аргументами:
# # 3 - это размер ребра куба,
# # 2 - это необходимое количество кубов
# calc_cube(3, 2)
#
#
# def calc_cube_perimeter(side):
#     return side * 12
#
# def calc_cube_area(side):
#     one_face = side * side
#     cube_area = one_face * 6
#     return cube_area
#
# def calc_cube(side, amount):
#     one_cube_perimeter = calc_cube_perimeter(side)
#     full_length = one_cube_perimeter * amount
#     one_cube_area = calc_cube_area(side)
#     full_area = one_cube_area * amount
#     print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)
#
#
# # Ниже напишите три вызова функции calc_cube().
# # Каждый вызов должен быть на отдельной строке.
# calc_cube(2, 4)
# calc_cube(0.5, 26)
# calc_cube(0.61, 6)
#
#
# concert_songs = {
#     'Ничего на свете лучше нету',
#     'Мы к вам заехали на час',
#     'Рок-колыбельная',
#     'Луч Солнца Золотого',
#     'Ничего на свете лучше нету',
#     'Куда ты, тропинка, меня завела',
#     'А как известно, мы народ горячий'
# }
# # Выясним, к какому типу данных принадлежит переменная concert_songs
# # для этого есть встроенная в Python функция type()
# print(type(concert_songs))
#
# # Напечатаем содержимое переменной concert_songs
# print(concert_songs)
#
# songs_list = [
#     'Мы к вам заехали на час',
#     'А как известно, мы народ горячий',
#     'Куда ты, тропинка, меня завела',
#     'Луч Солнца Золотого',
#     'Рок-колыбельная',
#     'Рок-колыбельная',
#     'Куда ты, тропинка, меня завела',
#     'А как известно, мы народ горячий',
#     'Луч Солнца Золотого',
#     'Ничего на свете лучше нету',
#     'А как известно, мы народ горячий',
#     'Луч Солнца Золотого',
#     'Мы к вам заехали на час',
#     'Ничего на свете лучше нету',
#     'Куда ты, тропинка, меня завела',
#     'Луч Солнца Золотого'
# ]
#
# # Преобразуем список songs_list в сет
# # и запишем этот сет в переменную unique_songs:
# unique_songs = set(songs_list)
#
# # Сначала напечатаем заголовок афиши
# print('Только один концерт! Проездом из Бремена в Рио-де-Жанейро!')
# print('БРЕМЕНСКИЕ МУЗЫКАНТЫ!')
#
# # Объявляем цикл
# for song in unique_songs:
#     print(song)
#
# # А эта строка выполнится после того,
# # как цикл закончит работу
# print('Не опаздывайте, начало в 19:00')
#
# cities = [
#     'Вологда',
#     'Чебоксары',
#     'Тольятти',
#     'Москва',
#     'Бремен',
#     'Санкт-Петербург',
#     'Новороссийск',
#     'Челябинск',
#     'Вологда',
#     'Новосибирск',
#     'Челябинск',
#     'Санкт-Петербург',
#     'Москва',
#     'Новосибирск'
# ]
#
# unique_cities = set(cities)
#
# for city in unique_cities:
#     print('У меня есть друг в городе', city)

# def print_valid_cities(all_cities, used_cities):
#
#     valid_cities = all_cities.difference(used_cities)
#
#     for i in valid_cities:
#         print(i)
#     # Вместо этого многоточия напишите код функции, она должна
#     # принимать и обрабатывать аргументы all_cities и used_cities,
#     # а затем печатать результат в нужном формате
#
# all_cities = {
#     'Абакан',
#     'Астрахань',
#     'Бобруйск',
#     'Калуга',
#     'Караганда',
#     'Кострома',
#     'Липецк',
#     'Новосибирск'
# }
#
# used_cities = {'Калуга', 'Абакан', 'Новосибирск'}
#
# print_valid_cities(all_cities, used_cities)
#
# def print_valid_cities(all_cities, used_cities):
#     diff = all_cities.difference(used_cities)
#     for city in diff:
#         print(city)
#
#
# def add_cities(all_cities, new_cities):
#     for city in new_cities:
#         all_cities.add(city)
#
#
# # Анфиса нашла названия нескольких новых городов,
# # эти города нужно добавить в множество all_cities
# new_cities = [
#     'Екатеринбург',
#     'Выборг' ,
#     'Владивосток',
#     'Казань',
#     'Why',
#     'Йезд'
# ]
#
# all_cities = {
#     'Абакан',
#     'Астрахань',
#     'Бобруйск',
#     'Калуга',
#     'Караганда',
#     'Кострома',
#     'Липецк',
#     'Новосибирск'
# }
#
# used_cities = {
#     'Калуга',
#     'Абакан' ,
#     'Новосибирск'
# }
#
# add_cities(all_cities, new_cities)
# print_valid_cities(all_cities, used_cities)
#
# def get_together_games(game_array1, game_array2):
#     game_array_match = set(game_array1).intersection(set(game_array2))
#
#     return game_array_match
#     # Напишите здесь код функции для поиска пересечений
#
# anfisa_games = [
#     'Online-chess',
#     'Города',
#     'DOOM',
#     'Крестики-нолики'
# ]
# alisa_games = [
#     'DOOM',
#     'Online-chess',
#     'Города',
#     'GTA',
#     'World of tanks'
# ]
#
# # Вызовите функцию со списками игр в качестве параметров
# together_games = get_together_games(anfisa_games, alisa_games)
# # Напечатайте итоговый перечень игр в цикле
#
# for game in together_games:
#     print('👾',game)

# english = {
#     'рука': 'hand',
#     'нога': 'leg',
#     'хвост': 'tail',
#     'питон': 'python',
#     'бэкенд-разработчик': 'back-end developer'
# }
#
# # Доступ по ключу: как по-английски рука?
# print(english['рука'])
#
# dump = {
#     1: 'единица',               # Ключ - число, значение - строка.
#     'земляника': 'ягода',       # И ключ, и значение - строки.
#     'помидор': 'ягода',         # Значение 'ягода' - не уникально. Так можно.
#     False: 0,                   # Ключ - булево значение, значение - число.
#     'лук': ['овощ', 'оружие'],  # Ключ - строка, значение - список.
#                                 # Ключ - строка, а значение - словарь. Так тоже можно!
#     'англо-русский словарь': {'рука': 'hand',
#                               'нога': 'leg',
#                               'бэкенд-разработчик': 'back-end developer'
#                                },
# }
#
# print(dump[False])
# # Будет напечатано ['овощ', 'оружие']
#
# friends =  {
#     'Серёга': 'Оренбург',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
# friends_cities = set(friends.values())
#
# for city in friends_cities:
#     print(city)
#
# friends =  {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск'
# }
#
# new_friends = {
#     'Денис': 'Москва',
#     'Онотолей': 'Йошкар-Ола'
# }
#
# friends.update(new_friends)
#
# print(friends)
#
# friends = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Айгуль': 'Казань',
#     'Алёна': 'Белгород'
# }
#
# friends['Даниил'] = 'Санкт-Петербург'
#
# print(friends)
#
# # Через доступ по ключу добавьте новый элемент словаря
# # с ключом 'Даниил' и значением 'Санкт-Петербург'
#
# # Напечатайте словарь friends

# friends = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Айгуль': 'Казань',
#     'Алёна': 'Белгород',
#     'Даниил': 'Санкт-Петербург'
# }
#
# new_friends = {
#     'Лев': 'Тула',
#     'Валера': 'Сыктывкар',
#     'Антон': 'Ялта',
#     'Карен': 'Краснодар'
# }
# # Добавьте элементы словаря new_friends в словарь friends
# friends.update(new_friends)
#
# print(friends)
#
# # Напечатайте словарь friends
#
# favorite_songs = {
#     'Тополиный пух': 'Иванушки international',
#     'Город золотой': 'Аквариум',
#     'Звезда по имени Солнце': 'Кино',
#     'Space Oddity': 'David Bowie',
#     'Рыба': 'Аквариум',
#     'Серенада Трубадура': 'Муслим Магомаев',
# }
# print(favorite_songs['Тополиный пух'])  # Здесь напечатайте значение для ключа 'Тополиный пух'
# print(favorite_songs['Space Oddity'])  # А здесь - значение для ключа 'Space Oddity'
#
# for song, performer in favorite_songs.items():
#     print('Песню', song, 'исполняет', performer)
#
# for artist in favorite_songs.values():
#     print(artist)
#
# for song in favorite_songs:
# #     print(song)
#
# friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
# friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
#
# # Объявлен пустой словарь, его нужно будет наполнить элементами,
# # каждый из которых составлен по схеме "имя: город"
# friends =  {}
#
# # Допишите ваш код сюда
# for i in range(0, len(friends_names)):
#     friends[friends_names[i]] = friends_cities[i]
#
# print('Лена живет в городе', friends['Лена'])
#
# friends =  {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Айгуль': 'Казань',
#     'Алёна': 'Белгород',
#     'Даниил': 'Санкт-Петербург',
#     'Лев': 'Тула',
#     'Валера': 'Сыктывкар',
#     'Антон': 'Ялта',
#     'Карен': 'Краснодар'
# }
#
# for friend, city in friends.items():
#     print(friend, 'живёт в городе', city)

#
# favorite_songs = {
#     'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'],
#     'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'],
#     'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
# }
# # Ниже напишите код, который напечатает на экран, сколько у Димы любимых песен
# print(len(favorite_songs['Дима']))
#
# # Ниже напишите код, который построчно напечатает
# # все любимые песни Сони.
#
# for friend, songs in favorite_songs.items():
#     if friend == 'Соня':
#         for i in songs:
#             print(i)
#
#
#
# # Список (list): в квадратных скобках:
# sleep_list = [
#     'спать',
#     'дрыхнуть',
#     'кемарить',
#     'спать'
# ]
#
# # Множество (set): в фигурных скобках, элементы выглядят как в списке,
# # но не могут повторяться:
# sleep_set = {
#     'дрыхнуть',
#     'спать',
#     'кемарить'
# }
# # Словарь (dict): в фигурных скобках, элементы выглядят как ключ:значение;
# # ключи не могут повторяться:
# sleep_dict = {
#     'спать': 'дрыхнуть',
#     'почивать': 'кемарить'
# }
#
# # Есть ли элемент 'дрыхнуть' в списке sleep_list?
# if 'дрыхнуть' in sleep_list:
#     print('В списке: нашлось!')
# else:
#     print('В списке: не нашлось :(')
#
# # Есть ли элемент 'дрыхнуть' в сете sleep_set?
# if 'дрыхнуть' in sleep_set:
#     print('В сете: нашлось!')
# else:
#     print('В сете: не нашлось :(')
#
# # Есть ли элемент 'дрыхнуть' в словаре sleep_dict?
# if 'дрыхнуть' in sleep_dict:
#     print('В словаре: нашлось!')
# else:
#     print('В словаре: не нашлось :(')
#
# playlist = {
#     'Venus',
#     'Yesterday',
#     'Fireball',
#     'Time',
#     'Poison',
#     'Thunderstruck'
# }
#
# new_music = [
#     'Kashmir',
#     'Smoke on the Water',
#     'Bohemian Rhapsody',
#     'Zombie',
#     'Let It Be',
#     'Its My Life',
# ]ќ
#
# for song in new_music:
#     playlist.add(song)
#
# print(playlist)
# #
# #
# friends = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Хабаровск',
#     'Егор': 'Пермь'
# }
#
# def is_anyone_in(collection, city):
#     for friend in collection:
#         if collection[friend] == city:
#             print('В городе ' + collection[friend] + ' живет ' + friend + '. Обязательно зайду в гости')
#         else:
#             print('В городе ' + collection[friend] + ' у меня есть друг, но мне туда не надо')
#
# is_anyone_in(friends, 'Хабаровск')

# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
# def process_anfisa(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(DATABASE)
#         return 'У тебя ' + str(count) + ' друзей.'
#     # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
#     elif query == 'Кто все мои друзья?':
#         friends_string = ''
#         # Чтобы получить перечень друзей -
#         # переберите словарь DATABASE в цикле
#         for friend in DATABASE:
#             friends_string += friend + ' '
#                  # Добавляйте к переменной friends_string имя друга и пробел
#         # Верните строку, составленную из 'Твои друзья: ' и friends_string
#         return('Твои друзья: ' + friends_string)
#     elif query == 'Где все мои друзья?':
#         friends_cities = ''
#         for city in set(DATABASE.values()):
#             friends_cities += city + ' '
#         return('Твои друзья в городах: ' + friends_cities)
#     else:
#         return '<неизвестный запрос>'
#
# # Не изменяйте следующий код
# print('Привет, я Анфиса!')
# print(process_anfisa('Сколько у меня друзей?'))
# print(process_anfisa('Кто все мои друзья?'))
# print(process_anfisa('Где все мои друзья?'))

# string = 'По Борнео и Ямайке ходит слон в трусах и майке'
# new_list = list(string)
# new_set = set(string)
#
# print('Список из строки: ', new_list)
# print('Сет из строки: ', new_set)
#
# monument_string = 'Я памятник себе воздвиг нерукотворный'
#
# index_list = [0, 1, 2, 8, 6, 17, 24]
#
# for i in index_list:
#     print(monument_string[i])
#
# friends = ['Сергей', 'Соня', 'Миша', 'Дима', 'Алина']
# print(friends[-1])
# print(friends[1])
# print(monument_string[-10])
# print(monument_string[-37])
#
# milk_str = 'Молоковоз в навозной куче'
#
# new_list = milk_str.split(' ')
# print(new_list)
#
# counter_str = 'Раз-два-три-четыре-пять, вышел зайчик погулять'
#
# counter_list = counter_str.split('-')
#
# counter_list_double = ''
#
# for word in counter_list:
#     counter_list_double += word + ' '
#
# counter_list_double_str = counter_list_double
#
#
# print(counter_list_double)
# print(counter_list_double_str)
#
# words_list = ['раз', 'два', 'три', 'четыре', 'пять', 'вышел', 'зайчик', 'погулять']
#
# new_string = ' '.join(words_list)
#
# print(new_string)
# #
# quote_1 = 'Работает? Не трогай'
# quote_2 = 'Если твой код работает, значит это хороший код'
# quote_3 = 'Лень - главное достоинство программиста'
#
# def penult_word(message):
#     word_list = message.split()
#     return word_list[-3]
#
# # Вызовы функции готовы к работе, не изменяйте их!
#
# # Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
# print(penult_word(quote_1))
#
# # То же, но с аргументом quote_2.
# print(penult_word(quote_2))
#
# # То же с аргументом quote_3.
# print(penult_word(quote_3))


# def check_query(query):
# # Допишите код тела функции
#     elements = query.split(', ')
#     return elements[1]
#
# # Дальше следует код, вызывающий вашу функцию; не изменяйте его:
# queries = [
#     'Анфиса, сколько у меня друзей?',
#     'Андрей, ну где ты был?',
#     'Андрей, ну обними меня скорей!',
#     'Анфиса, кто все мои друзья?'
# ]
#
# # Напечатаем результат.
# # Переберём список вопросов в цикле
# for q in queries:
#     # Каждый из вопросов передадим аргументом
#     # в функцию check_query()
#     result = check_query(q)
#     # И для каждого вызова напечатаем вопрос и, через дефис - вердикт программы
#     print(q, '-', result)
#
# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
#
# def process_anfisa(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(DATABASE)
#         return 'У тебя ' + str(count) + ' друзей.'
#
#     elif query == 'Кто все мои друзья?':
#         # Из словаря DATABASE создайте строку с помощью join();
#         # имена друзей разделите запятой и пробелом.
#         # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
#         friends_string = ', '.join(DATABASE)
#
#         return 'Твои друзья: ' + friends_string
#     elif query == 'Где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         # Из сета unique_cities создайте строку с помощью join();
#         # названия городов разделите запятой и пробелом.
#         # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
#         cities_string = ', '.join(unique_cities)
#
#         return 'Твои друзья в городах: ' + cities_string
#     else:
#         return '<неизвестный запрос>'
#
#
# print('Привет, я Анфиса!')
# print(process_anfisa('Сколько у меня друзей?'))
# print(process_anfisa('Кто все мои друзья?'))
# print(process_anfisa('Где все мои друзья?'))
#
# weather = 'cloudy'
# print('There is ' + weather + '.')
#
# print(f'There is {weather}.')
#
# one_hundred_100 = 100
# five_hundred = 500
# rubles = 'рублей'
# friends = 'друзей'r
# print(f'Не имей {one_hundred_100} {rubles}, а имей {one_hundred_100} {friends}!')
# print(f'{one_hundred_100} + {five_hundred} = {one_hundred_100 + five_hundred}')
#
#
# def show_meteo(temperature, weather):
#     print(f'Сейчас {weather}, на градуснике {temperature}.')
#
# show_meteo(24, 'облачно')
#
# russian_alphabet = ['а','б','в','г','д','е','ё','ж','з','и',
#                     'й','к','л','м','н','о','п','р','с','т',
#                     'у','ф','х','ц','ч','ш','щ','ъ','ы','ь',
#                     'э','ю','я']
#
# print(f'«{russian_alphabet[0]}» - первая буква в алфавите.')
#
# favorite_songs = {
#     'Тополиный пух': 'Иванушки international',
#     'Город золотой': 'Аквариум',
#     'Звезда по имени Солнце': 'Кино'
# }
#
# song = 'Город золотой'
#
# print(f'"{song}" – одна из самых известных песен группы "{favorite_songs[song]}".')
#
# def print_time(hour, minute, second):
#     print(f'На часах {hour}:{minute}:{second}')
#
# print_time(19,28,16)
#
# def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
#     return(f'Вы прослушали {len(listened)} песен общей продолжительностью {sum(listened) // 60} минут.')
#
# print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))
#
#
# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
# # Функция, распределяющая входящие запросы по первому слову в запросе.
# # Если запрос к Анфисе - запускаем функцию для Анфисы. Если нет, то для других.
# def process_query(query):
#     query_split = query.split(', ')
#     if query_split[0] == 'Анфиса':
#         return process_anfisa(query_split[1])
#     else:
#         return process_friend(query_split[0], query_split[1])
#
# # Функция, обрабатывающая запросы к друзьям.
# def process_friend(name, query):
#     if name in DATABASE:
#         if query == 'ты где?':
#             return f'{name} в городе {DATABASE[name]}'
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
# # Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# # в зависимости от того, какое число передано в аргументе friends_count
# def format_friends_count(friends_count):
#     if friends_count == 1:
#         return '1 друг'
#     elif 2 <= friends_count <= 4:
#         return f'{friends_count} друга'
#     else:
#         return f'{friends_count} друзей'
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         # Вызовите функцию format_friends_count() и передайте в неё count.
#         # Отредактируйте строку ниже: в ней должно использоваться выражение,
#         # которое вернёт функция format_friends_count()
#         return f'У тебя {format_friends_count(count)}.'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
# print('Привет, я Анфиса!')
# print(process_query('Анфиса, сколько у меня друзей?'))
# print(process_query('Анфиса, кто все мои друзья?'))
# print(process_query('Анфиса, где все мои друзья?'))
# print(process_query('Анфиса, кто виноват?'))
# print(process_query('Соня, ты где?'))
# print(process_query('Коля, что делать?'))
# print(process_query('Антон, ты где?'))

# from random import choice
#
# def find_a_present(prizes):
#     return choice(prizes)
#
# print(find_a_present(['кукла', 'жвачка', 'игрушечный питон']))
# print(find_a_present(['мяч', 'чебурашка', 'лосяш']))
#
# import random
#
# answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']
#
# def how_are_you():
#     return random.choice(answers)
#
# print(how_are_you())

# import datetime as dt
#
# start_time = dt.datetime(1961, 4, 12, 9, 7, 0)
# landing_time = dt.datetime(1961, 4, 12, 10, 55, 0)
#
# print(f'Время в полете составило {landing_time - start_time}. Класс!')
#
# import datetime as dt
#
# # Дата выхода первой серии.
# start_time = dt.datetime(2011, 4, 17)
# # Укажите дату выхода последней серии.
# final_time = dt.datetime(2019, 4, 15)
# # Вычислите, сколько времени шёл сериал.
# duration = final_time - start_time
#
# print(duration)
#
# import datetime as dt
#
# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь'
# }
#
# UTC_OFFSET = {
#     'Санкт-Петербург': 3,
#     'Москва': 3,
#     'Самара': 4,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Пермь': 5,
#     'Воронеж': 3,
#     'Волгоград': 3,
#     'Краснодар': 3,
#     'Калининград': 2
# }
#
# # def what_time(city):
# #     return dt.datetime.utcnow() + dt.timedelta(hours=UTC_OFFSET[city])
#
# def what_time(friend):
#     friendCity = DATABASE[friend]
#     return dt.datetime.utcnow() + dt.timedelta(hours=UTC_OFFSET[friendCity])
#
# start_moment = dt.datetime(2022, 6, 7, 19, 40)
# current_moment = dt.datetime(2022, 6, 19, 15, 35)
#
# utc_time = dt.datetime.utcnow()
#
# period = dt.timedelta(hours=3)
# moscow_time = utc_time + period
#
# time_bottas = dt.timedelta(minutes=1, seconds=25, microseconds=273250)
# time_hamilton = time_bottas + dt.timedelta(microseconds=208860)
#
# print(moscow_time)
# print(time_hamilton)
#
# print(what_time('Соня'))
#
# import datetime as dt
#
# first_snow = dt.datetime(2018, 9, 9)
# last_snow = dt.datetime(2018, 5, 19)
#
# print(last_snow.strftime('Последний снег выпал в %U-ю неделю года'))
# print(first_snow.strftime('А первый снег пошел в %U-ю неделю.'))

# import datetime as dt
#
#
# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь'
# }
#
# UTC_OFFSET = {
#     'Санкт-Петербург': 3,
#     'Москва': 3,
#     'Самара': 4,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Пермь': 5,
#     'Воронеж': 3,
#     'Волгоград': 4,
#     'Краснодар': 3,
#     'Калининград': 2
# }
#
#
# def what_time(friend):
#     utc_time = dt.datetime.utcnow()
#     city = DATABASE[friend]
#     time_in_city = utc_time + dt.timedelta(hours=UTC_OFFSET[city])
#     return time_in_city.strftime('%H:%M')
#
#
# print(what_time('Егор'))
#
# import datetime as dt
#
# DATABASE = {
#     'Сергей': 'Омск',
#     'Соня': 'Москва',
#     'Алексей': 'Калининград',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск',
#     'Артём': 'Владивосток',
#     'Петя': 'Михайловка'
# }
#
# UTC_OFFSET = {
#     'Москва': 3,
#     'Санкт-Петербург': 3,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Самара': 4,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Воронеж': 3,
#     'Пермь': 5,
#     'Волгоград': 3,
#     'Краснодар': 3,
#     'Калининград': 2,
#     'Владивосток': 10
# }
#
#
# def format_count_friends(count_friends):
#     if count_friends == 1:
#         return '1 друг'
#     elif 2 <= count_friends <= 4:
#         return f'{count_friends} друга'
#     else:
#         return f'{count_friends} друзей'
#
#
# def what_time(city):
#     if city in UTC_OFFSET:
#         offset = UTC_OFFSET[city]
#         city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
#         f_time = city_time.strftime("%H:%M")
#         return f'Там сейчас {f_time}'
#     else:
#         return f'<не могу определить время в городе {city}>'
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         return f'У тебя {format_count_friends(count)}.'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         city = DATABASE[name]
#         if query == 'ты где?':
#             return f'{name} в городе {city}'
#         if query == 'который час?':
#             return what_time(city)
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# def process_query(query):
#     elements = query.split(', ')
#     if elements[0] == 'Анфиса':
#         return process_anfisa(elements[1])
#     else:
#         return process_friend(elements[0], elements[1])
#
#
# def runner():
#     queries = [
#         'Анфиса, сколько у меня друзей?',
#         'Анфиса, кто все мои друзья?',
#         'Анфиса, где все мои друзья?',
#         'Анфиса, кто виноват?',
#         'Коля, ты где?',
#         'Соня, что делать?',
#         'Антон, ты где?',
#         'Алексей, который час?',
#         'Артём, который час?',
#         'Антон, который час?',
#         'Петя, который час?'
#     ]
#     for query in queries:
#         print(query, '-', process_query(query))
#
#
# runner()

# user_query = 'как стать бэкенд-разработчиком'
# query_list = user_query.split(' ')
# user_query_url = '%20'.join(query_list)
#
# url = 'https://yandex.ru/search/?text=' +  'как%20стать%20бэкенд-разработчиком'
#
# print(url)
#
# import urllib.parse
#
# url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'
#
# # чтобы вычленить текст вопроса
# # разбейте строку по знаку = и возьмите
# # второй элемент получившегося списка
# question =  url.split('=')
#
# print(urllib.parse.unquote(question[1]))

# напечатайте на экран запрос в расшифрованном виде
#
# import requests
#
# url = 'https://wttr.in/?0O'
#
# response = requests.get(url)
#
# print(response.text)

#
# import requests
#
# url = 'https://wttr.in'
#
# weather_parameters = {
#     '0': '',
#     'T': '',
#     'M': '',
#     'lang': 'ru'
# }
#
# response = requests.get(url, params=weather_parameters)
#
# print(response.text)
#
# import requests
#
# request_headers = {
#     'Accept-Language': 'ru'
# }
#
# # response = requests.get('https://ya.ru/white')
# #
# # code = response.status_code
# # print(f'Код ответа = {code}')
# #
# # headers = response.headers
# #
# # print(headers)
# # print(f'Тип содержимого = {headers["content-type"]}')
# # print(f'Время ответа = {headers["date"]}')
# #
# # response = requests.get('https://prakticum.yandex.ru/notfound')
# #
# # print(f'Код ответа {response.status_code}')
#
# response = requests.get('https://habr.com', headers=request_headers)
#
# print(response.text)

# import requests
#
# url = 'https://wttr.in'
#
# weather_parameters = {
#     '0': '',
#     'T': '',
#     'M': ''
# }
#
# request_headers = {
#     'Accept-Language': 'ru'
# }
#
# response = requests.get(url, headers=request_headers, params=weather_parameters)
#
# print(response.text)

# import random
# import math
#
# def calc_share(apples, friends):
#     friends_number = int(friends.split()[0])
#     return apples / friends_number
#
# apples = 17
#
# for friends in ['7 друзей', '2 друга', '0 друзей', 'один враг']:
#     try:
#         print(f'Каждому достанется по {calc_share(apples, friends)} яблока')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#     except ValueError:
#         print(f'Из строки {friends} не получилось достать число')
#
#
# import requests
#
# cities = [
#     'Омск',
#     'Калининград',
#     'Челябинск',
#     'Владивосток',
#     'Красноярск',
#     'Москва',
#     'Екатеринбург',
# ]
#
# def make_url(city):
#     return f'https://wttr.in/{city}'
#
#
# def make_parameters():
#     params = {
#         'format': 2,
#         'M': ''
#     }
#     return params
#
#
# def what_weather(city):
#     try:
#         response = requests.get(make_url(city), params=make_parameters())
#         if response.status_code == 200:
#             return response.text
#     except requests.ConnectionError:
#         return '<сетевая ошибка>'
#
#
# print('Погода в городах:')
# for city in cities:
#     print(city, what_weather(city))

#
# import datetime as dt
# import requests
#
# DATABASE = {
#     'Сергей': 'Омск',
#     'Соня': 'Москва',
#     'Алексей': 'Калининград',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск',
#     'Артём': 'Владивосток',
#     'Петя': 'Михайловка'
# }
#
# UTC_OFFSET = {
#     'Москва': 3,
#     'Санкт-Петербург': 3,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Самара': 4,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Воронеж': 3,
#     'Пермь': 5,
#     'Волгоград': 3,
#     'Краснодар': 3,
#     'Калининград': 2,
#     'Владивосток': 10
# }
#
#
# def format_count_friends(count_friends):
#     if count_friends == 1:
#         return '1 друг'
#     elif 2 <= count_friends <= 4:
#         return f'{count_friends} друга'
#     else:
#         return f'{count_friends} друзей'
#
#
# def what_time(city):
#     offset = UTC_OFFSET[city]
#     city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
#     f_time = city_time.strftime("%H:%M")
#     return f_time
#
#
# def what_weather(city):
#     url = f'http://wttr.in/{city}'
#     weather_parameters = {
#         'format': 2,
#         'M': ''
#     }
#     try:
#         response = requests.get(url, params=weather_parameters)
#     except requests.ConnectionError:
#         return '<сетевая ошибка>'
#     if response.status_code == 200:
#         return response.text
#     else:
#         return '<ошибка на сервере погоды>'
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         return f'У тебя {format_count_friends(count)}.'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         city = DATABASE[name]
#         if query == 'ты где?':
#             return f'{name} в городе {city}'
#         elif query == 'который час?':
#             if city not in UTC_OFFSET:
#                 return f'<не могу определить время в городе {city}>'
#             time = what_time(city)
#             return f'Там сейчас {time}'
#         elif query == 'как погода?':
#             if city not in UTC_OFFSET:
#                 return f'<не могу определить погоду в городе {city}>'
#             weather = what_weather(city)
#             return weather
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# def process_query(query):
#     elements = query.split(', ')
#     if elements[0] == 'Анфиса':
#         return process_anfisa(elements[1])
#     else:
#         return process_friend(elements[0], elements[1])
#
#
# def runner():
#     queries = [
#         'Анфиса, сколько у меня друзей?',
#         'Анфиса, кто все мои друзья?',
#         'Анфиса, где все мои друзья?',
#         'Анфиса, кто виноват?',
#         'Коля, ты где?',
#         'Соня, что делать?',
#         'Антон, ты где?',
#         'Алексей, который час?',
#         'Артём, который час?',
#         'Антон, который час?',
#         'Петя, как погода?',
#         'Коля, как погода?',
#         'Соня, как погода?',
#         'Антон, как погода?'
#     ]
#     for query in queries:
#         print(query, '-', process_query(query))
#
# runner()
#
# def practicum():
#     args = {
#         0: 'Практикум',
#         1: 'Яндекс',
#     }
#     args[0] = 'Яндекс'
#     args[1] = 'Практикум'
#     return [b for b in args.keys()]
#
#
# from decimal import Decimal
#
# steps_per_day = {
#     'day_1': 1.434,
#     'day_2': 2.12,
#     'day_3': 1.632,
#     'day_4': 5.59,
#     'day_5': 2.542,
#     'day_6': 1.1,
#     'day_7': 1.324
# }
#
# week_dist = 0
#
# for i in steps_per_day:
#     steps_per_day[i] = str(steps_per_day[i])
#     week_dist += Decimal(steps_per_day[i])
#
# print(week_dist)
#
# result = 3 ** 4 ** (0 + 5)
# print(result)

# # Получаем данные в секундах
# response = 424562
# # Переведите полученное значение в необходимые единицы измерения
# days = int(response / 3600 / 24)
#
# response -= days * 3600 * 24
# hours = int(response / 3600)
#
# response -= hours * 3600
# minutes = int(response / 60)
#
# response -= minutes * 60
# seconds = int(response)
#
# print(days, hours, minutes, seconds)
# #
#
# weight = 75
# height = 175
# dist = 9.75
# hours = 2
#
# spent_calories = (weight * 0.035 + (((dist/hours) ** 2 / height) * (weight * 0.029))) * (hours * 60)
#
# print(spent_calories)
#
# rating = 4.9
#
# result = 'Отличный фильм' if rating > 4.7 else 'Так себе кино'
# print(result)
#
# print('Отличный фильм' if rating > 4.7 else 'Так себе кино')
#
#
# x = -2
# y = 5
# if x < 0 > y:
#     print('Первая четверть')
# elif x > 0 > y:
#     print('Четвертая четверть')
# elif x < 0 < y:
#     print('Вторая четверть')
# else:
#     print('Третья четверть')
#
# movies = ['Аватар', 'Матрица', 9, 4.2]
#
# for i in movies:
#     print(type(i), i)
#
# name_movie = 'Джонни Мнемоник'
# print(name_movie[0])
# print(name_movie[2])
# print(name_movie[-5])
# print(name_movie[-2])
# print(ord(name_movie[-1]))
#
# print([10, 'one'] > [10, 'one'])
#
# print(ord('1'), ord('0'))
#
# first = [15, 2, '11', 10]
# second = [15, 2, '101', 17]
#
# print(first[2] < second[2])
#
# a = 'Роботы стали важны'
# b = 'в период'
# c = 'эмиграции с Терры'
#
# print(a[4:6], b[2] + b[4] + b[6] + c[3:6] + c[1] + c[1:3] + a[7:9])
#
#
# recommended_movies = ['Хатико', '23', 'Достучаться до небес',
#                       'Хакеры', 'Трон', '1408']
#
# hackers_movies = ['Трон', 'Военные игры', 'Тихушники',
#                   'Джонни Мнемоник', 'Хакеры', 'Нирвана',
#                   '23', 'Враг государства', 'Взлом',
#                   'Пароль рыба-меч', 'Сеть', 'Кто я']
#
# for top_film in recommended_movies:
#     if top_film in hackers_movies:
#         print(f'Рекомендуем программистам посмотреть фильм "{top_film}"')
#
# rng = range(2, 12, 2)
# print(type(rng))
# print(rng[2])
#
# for i in rng:
#     print(i)
#
# for num in rng:
#     print(f'Это строка # {num}')
#
# movies = ['Martix', 'Hackers', 'Throne', 'Silencers', 'Web']
# movie_ratings = [4.7, 5.0, 4.3, 4.9, 3.4]
#
# print('Рейтинг пользователей')
# for index in range(len(movies)):
#     print(f'{movies[index]}: {movie_ratings[index]}')

# alert_string = ('Потребление калорий превысило расход на 300%! '
#                  'Уберите бургер в холодильник!')
# print(alert_string)
#
# output_string = '''Количество шагов в день: 18500
# пройденная дистанция 12 км
# Отличный результат!'''
#
# print(output_string)
#
# alert_string = alert_string.upper()
# print(alert_string)
#
# cat_motto = 'Котики важны. Котики улучшают здоровье.'
#
# fitness_motto = cat_motto.replace('Котики', 'Тренировки', 3)
#
# print(fitness_motto)
#
# error_message = 'ER03:"!Ошибка подключения устройства! Доступ блокирован!!E"'
# text = error_message.strip('!!"E3!0R:')
# print(text)
#
# steps = 10550
#
# print('Сегодня вы прошли {} шагов.'.format(steps))
#
# zero_txt = 'чувствую'
# first_txt = 'в тебе'
# second_txt = 'силу'
#
# print('{2} {1} {0}'.format(zero_txt, first_txt, second_txt))
#
# dist_km = 0.56098
#
# print(f'За день Вы прошли {dist_km:.2f} км')
#
# achievement_part = 0.2
# #
# print('Прогресс достижения цели: {:.0%}'.format(achievement_part))
#
# steps = 8465    # Количество пройденных шагов
# len_step_m = 0.65   # Длина одного шага пользователя в метрах
# transfer_coef = 1000   # Метров в километре
#
# print(f'За день вы прошли {steps * len_step_m:.0f} м')

#
# weight = 75 # Вес
# height = 175 # Рост
# steps = 8462 # Количество пройденных за день шагов
# hours = 2 # Время движения в часах
# len_step_m = 0.65 # Длина одного шага в метрах
# transfer_coeff = 1000 # Коэффициент перевода значения расстояния из метров в километры
#
# dist = steps * len_step_m / transfer_coeff # Напишите формулу расчёта
#
# mean_speed = dist / hours
# minutes = hours * 60
#
# spent_calories = (0.035 * weight + (mean_speed ** 2 / height) * 0.029 * weight) * minutes
#
# if dist >= 6.5:
#     achievement = 'Отличный результат! Цель достигнута.'
# elif dist >= 3.9:
#     achievement = 'Неплохо! День был продуктивным.'
# elif dist >= 2:
#     achievement = 'Маловато, но завтра наверстаем!'
# else:
#     achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'
#
# output = f'''
# Сегодня вы прошли {steps} шагов.
# Пройденная дистанция {dist:.2f} км.
# Вы сожгли {spent_calories:.2f} ккал.
# {achievement}'''
#
# print(output)

# brand_name = 'Unicorn'
# print(id(brand_name))
#
# brand_name[1] = '1'
#
# print(brand_name[1])
#
# movie_ratings = [4.7, 5.0, 4.9, 3.8]
#
# new_movie_ratings = [
#     rating + 0.2 if rating < 4.9 else rating for rating in movie_ratings
# ]
#
# print(new_movie_ratings)

# # Объявляем новый список, в него будем складывать измененные оценки
# new_movie_ratings = [rating + 0.2 for rating in movie_ratings]
#
# print(new_movie_ratings)
#

#
# # Перебор списка в цикле:
# for rating in movie_ratings:
#     rating += 0.2
#     print(rating)
#
#
# whole_num_list = [whole_num ** 2 for whole_num in range(1, 11)]
#
# print(whole_num_list)

# week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
#
# print(week)
#
# week.append('Пердельник')
#
# print(week)
#
# movie_ratings = [4.7, 5.0, 4.3, 3.8]
# movies = ['Матрица', 'Хакеры', 'Трон']
# only_text_movies = [2.2, 2.3, 'Место встречи', 'Старики-разобойники', 'Берегись автомобиля']
# print(movies, id(movies))
#
# movies.extend(movie_ratings)
# print(movies, id(movies))
#
# movies.insert(0, 'Джей и молчаливый Боб наносят ответный удар')
# print(movies, id(movies))
#
# movies.remove('Хакеры')
# print(movies, id(movies))
#
# for movie in only_text_movies:
#     print(movie)
#
# for movie in only_text_movies:
#     pop = only_text_movies.pop()
#     print('Popped:', pop)
#
# print(only_text_movies)
#
# movie_ratings = [4.7, 5.0, 4.3, 3.8, 4.7, 4.1]
# print(movie_ratings)
# movie_ratings.sort()
# print(movie_ratings)
# movie_ratings.reverse()
# print(movie_ratings)
# movie_ratings = movie_ratings[::-1]
# print(movie_ratings)
#
# force_words = ['сила', 'пребудет', 'с', 'тобой', 'Да']
#
# package = tuple()
#
# for word in force_words:
#     package.
#
# print(package)
# #
# print(id(force_words))
#
# force_words.insert(0, force_words.pop(force_words.index('Да')))
# force_words.append(force_words.pop(force_words.index('сила')))
#
# print(force_words)
# # Убедимся, что это тот же объект, что и в начале программы
# print(id(force_words))
#

# tpl = tuple('2:00:01')
# print(tpl)
#
# not_sorted_tpl = (5**5, 5**2, 5**1, 5**4, 5**0, 5**3)
# print(type(not_sorted_tpl))
# print(not_sorted_tpl)
#
# sorted_tpl = sorted(not_sorted_tpl)
# print(type(sorted_tpl))
# print(sorted_tpl)


# not_srtd_tpl = (5**5, 5**2, 5**1, 5**4, 5**0, 5**3)
#
# # Измените это выражение, чтобы результатом был кортеж
# srtd_tpl = tuple(sorted(not_srtd_tpl))
# print(type(srtd_tpl))

# days = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
# steps = [1500, 3445, 13222, 10000, 12555, 1300, 6000]

# result = [(days[0], steps[0]), (days[1], steps[1]), (days[2], steps[2]),
#           (days[3], steps[3]), (days[4], steps[4]), (days[5], steps[5]),
#           (days[6], steps[6])]
#
# print(result)

# result = []
#
# for i in range(len(days)):
#     result += [(days[i], steps[i])]
#
# print(result)
#
# toys = {'куклы', 'кубики', 'странная штука', 'самолетики', 'мелки'}
#
# for toy in toys:
#     print(toy)
#
# movie_ratings = [5.0, 4.1, 4.3, 4.7, 4.7, 3.8]
# print(movie_ratings)
# movie_ratings = set(movie_ratings)
# print(movie_ratings)
#
# for rating in movie_ratings:
#     print(rating)
#
# movies = ['Матрица', 'Сеть', 'Хакеры', 'Трон', 'Тихушники', 'Сеть', 'Трон']
# uniq_movies = set(movies)
# uniq_movies_list = list(uniq_movies)
# print(uniq_movies_list)
#
# not_uniq_str = 'съешь же ещё этих мягких французских булок да выпей чаю'
# not_uniq_str_nospace = not_uniq_str.replace(' ', '')
#
# count_char = len(set(not_uniq_str_nospace))
# print(count_char)
#
# movies = ['Матрица', 'Сеть', 'Хакеры', 'Трон',]
# movie_ratings = [4.7, 5.0, 4.3, 3.8]
# movie_stars = {'***', '****', '*', '**', '*****'}
# print(type(movie_stars))
# movies_set = {movie_stars}
# print(movies)
#
# movie_info = {'Матрица': 4.5, 'Трон': 4.8}
#
# movie_names = set(movie_info)
# print(movie_names)
#
# movie_ratings = [5.0, 4.1, 4.3, 4.7, 4.7, 3.8]
# movie_ratings_set = set(movie_ratings)
# print(movie_ratings_set)
#
# maxim_toys = {'машинка', 'скакалка', 'кубики', 'пистолетик'}
# lera_toys = {'скакалка', 'кукла', 'кубики', 'юла'}
#
# import time
#
# num_set = set()
#
# for num in range(10**6):
#     num_set.add(num)
#
# print(time.time())
# start_time = time.time()
# if 954365 in num_set:
#     print(True)
#
# print(time.time() - start_time)
#
# num_list = []
# for num in range(10**6):
#     num_list.append(num)
#
# start_time = time.time()
# if 954365 in num_list:
#     print(True)
#
# print(time.time() - start_time)


# num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'
# num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'
#
# num_string_1_set = set(num_string_1.split(' '))
# num_string_2_set = set(num_string_2.split(' '))
#
# overlap_set = num_string_1_set.intersection(num_string_2_set)
# print(len(overlap_set))

# id_string = '32 48 2 6 14 58 2 88 9 14 123 48 3 17 42 42 7'
#
# id_list = id_string.split(' ')
# id_list = [int(x) for x in id_list]
# # id_list.sort()
#
# unique_ids = []
# duplicate_ids = []
#
# for id in id_list:
#     if id in unique_ids:
#         duplicate_ids.append(id)
#         print('Найден дубликат id', id)
#     else:
#         unique_ids.append(id)
#
# unique_ids.sort()
# print(unique_ids)

# no_duplicates_id_list = []
#
# for id in range(len(id_list)-1):
#     # print('Текущий', id_list[id])
#     # print('Следующий', id_list[id+1])
#     if id_list[id] in id_list:
#         print('Найден дубликат', id_list[id])
#     if id_list[id] not in no_duplicates_id_list:
#         no_duplicates_id_list.append(id_list[id])
#
# print(no_duplicates_id_list)
# print(id_list)
#
# movies = [('Матрица', 4.7), ('Трон', 3.8), ('Хакеры', 4.3), ('Матрица', 4.0)]
#
# movies_dict = dict(movies)
# print(movies_dict)
#
# movies_dict = dict(Матрица=4.7, Трон=3.8, ФЫв=4.3)
# print(movies_dict)

# movies = dict.fromkeys(['Матрица', 'Хакеры', 'Трон', 'Кибер'], [2.2, 2.4])
# print(movies)
#
# movie_ratings = [4.7, 5.0, 4.3, 4.0]
# movies = ['Матрица', 'Хакеры', 'Трон', 'Кибер']
# review = ['Фильм крут', 'Фильм крут', 'Смотреть можно', 'Смотреть можно']
#
#
# movies_info = dict(zip(movies, movie_ratings))
#
# print(movies_info)
#
#
# print(dict(movies_info))
#
# for element in movies_info:
#     print(element)
#
# movies_info_dict = dict(movies_info)
# print(type(movies_info_dict))
#
# print(movies_info_dict)

#
# movie_ratings = [4.7, 5.0, 4.3, 4.0]
# movies = ['Матрица', 'Хакеры', 'Трон', 'Кибер', 'Сеть']
#
# zipped_movies = zip(movies, movie_ratings)
#
# dict_movies = dict(zipped_movies)
# print(dict_movies)
# # print('Dict:', dict_movies)
#
# new_dict = {
#     num: num for num in range(3)
# }
# print(new_dict)
#
# movies = ['Матрица', 'Хакеры', 'Трон']
# category = 'Фантастика в IT'
#
# movies_info = {
#     movie: category for movie in movies
# }
#
# print(movies_info)
#
# movies = {
#     'Матрица': 4.7,
#     'Хакеры': 4.3,
#     'Трон': 3.8,
#     'Кибер': 2.5,
#     'Пятая власть': 4.1
# }
#
# print(movies['Матрица'])
#
# for movie in movies:
#     print(movies[movie])

# movies = {
#     'Матрица': {'rating': '4.7', 'review': 'Фильм крут'},
#     'Хакеры':  {'rating': '4.5', 'review': 'Смотреть можно'},
#     'Трон':  {'rating': '3.8', 'review': 'Смотреть можно'},
#     'Кибер':  {'rating': '2.5', 'review': 'Так себе киношечка'},
#     'Пятая власть':  {'rating': '4.1', 'review': 'Смотреть можно'},
# }
#
# hackers = movies['Хакеры']
#
# print(hackers['rating'], hackers['review'])

#
# movies = {
#     'Матрица': {'rating': 4.7, 'review': 'Фильм крут'},
#     'Хакеры':  {'rating': 4.5, 'review': 'Смотреть можно'},
#     'Трон':  {'rating': 3.8, 'review': 'Смотреть можно'},
#     'Кибер':  {'rating': 2.5, 'review': 'Так себе киношечка'},
#     'Пятая власть':  {'rating': 4.1, 'review': 'Смотреть можно'},
# }
# # Вызов метода get() с одним обязательным параметром
# print(movies.get('Хоббит'))
# # Вывод в терминал: None
#
# print(movies.get('Матриц', 'Такого фильма нет'))
#
# print(movies)
#
# movies['Место встречи изменить нельзя'] = 2
#
# print(movies)

# movies = {
#     'Матрица': 4.7,
#     'Хакеры': 4.3,
#     'Трон': 3.8,
#     'Кибер': 2.5
# }
# #
# # movies['Хакеры'] = 5.0
# #
# # del movies['Хакеры']
# #
# # popped = movies.pop('Трон')
# #
# # print(popped)
# # print(movies)
#
# for movie, rating in movies.items():
#     print(movie, rating)


# favorite_movies = {}
# garbage = {}
#
# recommended_movies = {
#     'Хенкок': {'rating': 4.5, 'review': 'Смотреть можно'},
#     'Матрица': {'rating': 4.7, 'review': 'Фильм крут'},
#     'Кибер': {'rating': 2.5, 'review': 'Так себе киношечка'},
#     'Трон': {'rating': 3.8, 'review': 'Так себе киношечка'},
#     'Мстители': {'rating': 4.7, 'review': 'Фильм крут'},
#     'Хакеры':  {'rating': 4.5, 'review': 'Смотреть можно'}
# }
#
# for movie, details in recommended_movies.items():
#     if details['rating'] > 4.0:
#         print(f'У фильма "{movie}" хороший отзыв: "{details["review"]}". Фильм добавлен в избранное.')
#         favorite_movies[movie] = details
#     else:
#         print(f'Фильм "{movie}" не интересен: "{details["review"]}". Фильм удалён из рекомендаций.')
#         garbage[movie] = details
#
# for movie in garbage:
#     del recommended_movies[movie]
#
# print(favorite_movies)

# print('Мусор:', garbage)
# print('ОТСОРТИРОВАННЫЕ:', favorite_movies)
# print('ОСТАВШИЕСЯ В РЕКОМЕНДОВАННЫХ', recommended_movies)
#
# a = 1
# b = '2'
# c = ['Анатолий', 3.15, '3 поросёнка']
#
# res = a + int(b) + len(c)
#
# print(len(c[0]) - int(b))
#
# result = f'Суммой чисел {a}, {int(b)} и {len(c)} будет {res}'
# print(result)
#
# def get_mod_diff(a, b=1):
#     """Фукнция возвращает разницу в переданных значениях по модулю"""
#     diff = abs(a - b)
#     return diff
#
#
#
# x = 3
# y = 4
# # Именованные аргументы можно передавать в любом порядке, функция всё поймёт и примет.
# print(get_mod_diff(b=y, a=x))
#
# x = [10, 22, 334]
# y = [*x,4, 5, 6]
# print(y)
#
#
# def get_boost(coeff, *ratings):
#     for rating in ratings:
#         print(coeff + rating)
#
#
# x = 0.2
# y = {4.3, 4.5, 3.0, 2.5, 4.7}
#
# get_boost(x, 4.3, 4.5, 3.0, 2.5, 4.7)

#
# def print_profile(character, **info):
#     '''Распаковка названия персонажа и способностей'''
#     print(f'Персонаж: {character}')
#     for key, value in info.items():
#         print(f'{key}: {value}')
#
#
# print_profile('Spider_man',
#               name='Питер Паркер',
#               talent=['Суперсила', 'Паучье чутьё', 'Огромный член'],
#               city='Нью Йорк'
#               )
#
#
# def empty():
#     ...
#
# print(empty())

# def get_mean(values):
#     values_sum = 0
#     for value in values:
#         values_sum += value
#     return values_sum / len(values)
#
#
# # Список значений для теста
# num_lst = [3, 6, 5, 7, 9, 1]
#
# result = f'{get_mean(num_lst):.2f}'
#
# print(result)  # Напечатайте результат вызова функции.


# print('{2} {1} {0}'.format(zero_txt, first_txt, second_txt))
#
# dist_km = 0.56098
#
# print(f'За день Вы прошли {dist_km:.2f} км')
#
# achievement_part = 0.2
# #
# print('Прогресс достижения цели: {:.0%}'.format(achievement_part))
#
# def test_range(start, end, *range):  # Укажите параметры
#     valid_range = []
#     for value in range:
#         if start < value < end:
#             valid_range += [value]
#         else:
#             print(f'Число за границами диапазона')
#     # print('range', valid_range)
#     return valid_range
#
# start = 4
# end = 12
# print(test_range(start, end, 5, 16, 32, 6, 7, 1))
# import datetime as dt
# import time
#
# lera_birthday = dt.date(2015, 5, 16)
# maxim_birthday = dt.date(2011, 12, 16)
#
# today = dt.date.today()
#
# today_year = today.year
#
# lera_birthday = lera_birthday.replace(year=today_year)
# maxim_birthday = maxim_birthday.replace(year=today_year)
#
# lera_birthday_left = (lera_birthday - today).days
# maxim_birthday_left = (maxim_birthday - today).days
#
# print(lera_birthday_left)
# print(maxim_birthday_left)
#
# import datetime as dt
#
# lera_birthday = dt.date(2015, 5, 16)
# maxim_birthday = dt.date(2011, 12, 16)
#
#
# def get_days_to_birthday(date_birthday):
#     today = dt.date.today()
#     today_year = today.year
#
#     birthday_year_replace = date_birthday.replace(year=today_year)
#
#     if birthday_year_replace < today:
#         return ((birthday_year_replace.replace(year=today.year+1)) - today).days
#     return (birthday_year_replace - today).days
#
#
# print(get_days_to_birthday(lera_birthday))
# print(get_days_to_birthday(maxim_birthday))
#
#
# import datetime as dt
# # В эту переменную запишите формат для
# # преобразования даты
# FORMAT = '%d.%m.%Y'
# # Добавьте в объявление функции ещё один параметр - имя
# def get_days_to_birthday(name, date_birthday):
#     # Преобразуйте полученную строку с датой в объект нужного типа
#     #date_birthday =
#
#     date_birthday = dt.datetime.strptime(date_birthday, FORMAT).date()
#
#     today = dt.date.today()
#     date_birthday = date_birthday.replace(year=today.year)
#
#     if date_birthday < today:
#         date_birthday = date_birthday.replace(year=today.year + 1)
#
#     days_to_birthday = date_birthday - dt.date.today()
#     return f'{name}, до твоего дня рождения осталось дней: {days_to_birthday.days}'
#
#
# birthdays = [
#     ('Лера', '16.05.2015'),
#     ('Максим', '16.12.2011'),
#     ('Толя', '12.06.2016')
# ]
#
# # Напечатайте результат вызова функции get_days_to_birthday()
# # для каждой пары из списка birthdays
#
# for friend in birthdays:
#     print(get_days_to_birthday(friend[0], friend[1]))

# *******************************************************
# *******************************************************
# СПРИНТ1: ФИНАЛЬНЫЙ ПРОЕКТ, ФИТНЕС ТРЕКЕР
# *******************************************************
# *******************************************************
#
# import datetime as dt
#
# FORMAT = '%H:%M:%S'
# WEIGHT = 75  # Вес.
# HEIGHT = 175  # Рост.
# K_1 = 0.035  # Коэффициент для подсчета калорий.
# K_2 = 0.029  # Коэффициент для подсчета калорий.
# STEP_M = 0.65  # Длина шага в метрах.
# transfer_coeff = 1000
#
# storage_data = {}  # Словарь для хранения полученных данных.
#
#
# def check_correct_data(data):
#     """Проверка корректности полученного пакета."""
#     # Если длина пакета отлична от 2
#     # или один из элементов пакета имеет пустое значение -
#     # функция вернет False, иначе - True.
#     if len(data) != 2 or data[0] is None:
#         return False
#     return True
#     # formatted_time = dt.datetime.strptime(data[0], FORMAT).time()
#     # print(formatted_time)
#     # try:
#     #     formatted_time = dt.datetime.strptime(data[0], FORMAT).time()
#     # except:
#     #     return False
#     # if formatted_time == FORMAT:
#     #     print('норм')
#
#
# def check_correct_time(time):
#     """Проверка корректности параметра времени."""
#     # Если словарь для хранения не пустой
#     # и значение времени, полученное в аргументе,
#     # меньше самого большого ключа в словаре,
#     # функция вернет False.
#     # Иначе - True
#     if storage_data and time <= max(storage_data.keys()):
#         return False
#     return True
#
# def get_step_day(steps):
#     """Получить количество пройденных шагов за этот день."""
#     # Посчитайте все шаги, записанные в словарь storage_data,
#     # прибавьте к ним значение из последнего пакета
#     # и верните эту сумму.
#     return sum(storage_data.values()) + steps
#
#
# def get_distance(steps):
#     """Получить дистанцию пройденного пути в км."""
#     # Посчитайте дистанцию в километрах,
#     # исходя из количества шагов и длины шага.
#     return get_step_day(steps) * STEP_M / transfer_coeff
#
# def get_seconds(time):
#     time_str = str(time)
#     hours, minutes, seconds = time_str.split(':')
#     return int(hours)*3600 + int(minutes)*60
#
# def get_spent_calories(dist, current_time):
#     """Получить значения потраченных калорий."""
#     # В уроке «Строки» вы написали формулу расчета калорий.
#     # Перенесите её сюда и верните результат расчётов.
#     # Для расчётов вам потребуется значение времени;
#     # получите его из объекта current_time;
#     # переведите часы и минуты в часы, в значение типа float.
#
#     seconds = get_seconds(current_time)
#     hours = seconds / 3600
#     minutes = hours * 60
#     mean_speed = dist / hours
#     return (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * minutes
#
#     # weight = 75 # Вес
#     # height = 175 # Рост
#     # steps = 8462 # Количество пройденных за день шагов
#     # hours = 2 # Время движения в часах
#     # len_step_m = 0.65 # Длина одного шага в метрах
#     # transfer_coeff = 1000 # Коэффициент перевода значения расстояния из метров в километры
#     #
#     # dist = steps * len_step_m / transfer_coeff # Напишите формулу расчёта
#     #
#     # mean_speed = dist / hours
#     # minutes = hours * 60
#     #
#     # spent_calories = (0.035 * weight + (mean_speed ** 2 / height) * 0.029 * weight) * minutes
#
#
# def get_achievement(dist):
#     """Получить поздравления за пройденную дистанцию."""
#     # В уроке «Строки» вы описали логику
#     # вывода сообщений о достижении в зависимости
#     # от пройденной дистанции.
#     # Перенесите этот код сюда и замените print() на return.
#     if dist >= 6.5:
#         return 'Отличный результат! Цель достигнута.'
#     elif dist >= 3.9:
#         return 'Неплохо! День был продуктивным.'
#     elif dist >= 2:
#         return 'Маловато, но завтра наверстаем!'
#     return 'Лежать тоже полезно. Главное — участие, а не победа!'
#
#
# def show_message(time, day_steps, distance, spent_calories, achievement):
#     print('')
#     print(f'Время: {time}.')
#     print(f'Количество шагов за сегодня: {day_steps}.')
#     print(f'Дистанция составила {distance:.2f} км.')
#     print(f'Вы сожгли {spent_calories:.2f} ккал.')
#     print(achievement)
#     print('')
#
#
# def accept_package(data):
#     # if  # Если функция проверки пакета вернет False
#     #     return 'Некорректный пакет'
#     if not check_correct_data(data):
#         # print('Некорректный пакет')
#         return 'Некорректный пакет'
#     # # Распакуйте полученные данные.
#     # pack_time =  # Преобразуйте строку с временем в объект типа time.
#     pack_time = dt.datetime.strptime(data[0], FORMAT).time()
#
#     # if  # Если функция проверки значения времени вернет False
#     #     return 'Некорректное значение времени'
#     if not check_correct_time(pack_time):
#         return 'Некорректный пакет'
#
#     # print('Прошедший пакет', pack_time, data[1])
#
#     # day_steps =  # Запишите результат подсчёта пройденных шагов.
#     day_steps = get_step_day(data[1])
#     # print('Day Steps', day_steps)
#
#     # dist =  # Запишите результат расчёта пройденной дистанции.
#     dist = get_distance(data[1])
#     # print('Day Dist', dist)
#
#     # spent_calories =  # Запишите результат расчёта сожжённых калорий.
#     spent_calories = get_spent_calories(dist, pack_time)
#     # print('Калории', spent_calories)
#
#     # achievement =  # Запишите выбранное мотивирующее сообщение.
#     achievement = get_achievement(dist)
#
#     # output = f'''
#     # Сегодня вы прошли {steps} шагов.
#     # Пройденная дистанция {dist:.2f} км.
#     # Вы сожгли {spent_calories:.2f} ккал.
#     # {achievement}'''
#
#     # # Вызовите функцию show_message().
#     show_message(pack_time, day_steps, dist, spent_calories, achievement)
#
#     # # Добавьте новый элемент в словарь storage_data.
#     storage_data[pack_time] = data[1]
#
#     return storage_data
#
#
# # Данные для самопроверки.Не удаляйте их.
# package_0 = ('2:00:01', 505)
# package_1 = (None, 3211)
# package_2 = ('9:36:02', 15000)
# package_3 = ('9:36:02', 9000)
# package_4 = ('8:01:02', 7600)
#
# accept_package(package_0)
# accept_package(package_1)
# accept_package(package_2)
# accept_package(package_3)
# accept_package(package_4)
# # print('Storage data', storage_data)

# class Contact:
#     def __init__(self, name, phone, birthday, address):
#         self.name = name
#         self.phone = phone
#         self.birthday = birthday
#         self.address = address
#         print(f'Создаём новый контакт {name}')
#
#     def show_contact(self):
#         print(f'{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}')
#
#     def show(self):
#         print(f'Имя: {self.name}, '
#               f'телефон: {self.phone}, '
#               f'день рождения: {self.birthday}')
#
#     def __str__(self):
#         return f'Контакт: {self.name}'
#
# mike = Contact('Михаил Булгаков',
#                '2-03-27',
#                '15.05.1891',
#                'Россия, Москва, Большая Пироговская, дом 35б, кв. 6')
#
# vlad = Contact('Владимир Маяковский',
#                '73-88',
#                '19.07.1893',
#                'Россия, Москва, Лубянский проезд, д. 3, кв. 12')
#

# def print_contact():
#     print(f'{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}')
#     print(f'{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}')
#
# mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
# mike.phone = 'К-058-67'
#
# vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
# vlad.phone = '2-35-71'

# print_contact()
#
# mike.show_contact()
# vlad.show_contact()
#

import math


class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = 4 * math.pi * radius**2
        self.average_temp_celsius = temp_celsius
        self.average_temp_fahrenheit = (temp_celsius * 9 / 5) + 32

    def show_info(self):
        print(f'Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.')
        print(f'Средняя температура поверхности планеты: {self.average_temp_fahrenheit} по Фаренгейту.')


jupiter = Planet('Юпитер', 69911, -108)
pluto = Planet('Плутон', 1187, -233.15)
uranus = Planet('Уран', 25362, -224.2)
neptune = Planet('Нептун', 24662, -220)
earth = Planet('Земля', 6371, 14)

jupiter.show_info()
pluto.show_info()
uranus.show_info()
neptune.show_info()
earth.show_info()

