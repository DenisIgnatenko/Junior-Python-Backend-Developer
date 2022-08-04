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

# import math
#
#
# class Planet:
#     def __init__(self, name, radius, temp_celsius):
#         self.name = name
#         self.surface_area = 4 * math.pi * radius**2
#         self.average_temp_celsius = temp_celsius
#         self.average_temp_fahrenheit = (temp_celsius * 9 / 5) + 32
#
#     def show_info(self):
#         print(f'Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.')
#         print(f'Средняя температура поверхности планеты: {self.average_temp_fahrenheit} по Фаренгейту.')
#
#
# pluto = Planet('Плутон', 1187, -233.15)
# uranus = Planet('Уран', 25362, -224.2)
# neptune = Planet('Нептун', 24662, -220)
# earth = Planet('Земля', 6371, 14)
#
# pluto.show_info()
# uranus.show_info()
# neptune.show_info()
# earth.show_info()

# class User:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def show(self):
#         print(f'{self.name} ({self.phone})')
#
# class Friend(User):
#     def __init__(self, name, phone, address):
#         super().__init__(name, phone)
#         self.address = address
#
#     def show(self):
#         print(f'Имя: {self.name} || '
#               f'Телефон: {self.phone} || '
#               f'Адрес: {self.address}')
#
#
# father = User('Дюма-отец', '+33 3 23 96 23 30')
# son = Friend('Дюма-сын', '+33 2 23 44 11 34', 'Тверская-ямская')
#
# father.show()
# son.show()
#
# class User:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def show(self):
#         print(f'{self.name} ({self.phone})')
#
#
# class Friend(User):
#     def show(self):
#         print(f'Имя: {self.name} || Телефон: {self.phone}')
#
#
# user = User("Виктор Гюго", "+33 1 42 72 10 16")
# # у класса friend нет конструктора, но он есть
# # у родительского класса User, поэтому код сработает
# friend = Friend("Виктор Гюго", "+33 1 42 72 10 16")
#
# user.show()
# friend.show()
#
# from math import radians, sin, cos, acos
#
# class Point:
#     def __init__(self, latitude, longitude):
#         self.latitude = radians(latitude)
#         self.longitude = radians(longitude)
#
#     def distance(self, other):
#         cos_d = sin(self.latitude) * sin(other.latitude) +\
#                 cos(self.latitude) * cos(other.latitude) * \
#                 cos(self.longitude - other.longitude)
#
#         return 6371 * acos(cos_d)
#
#
# class City(Point):
#     def __init__(self, latitude, longitude, name, population):
#         super().__init__(latitude, longitude)
#         self.name = name
#         self.population = population
#
#     def show(self):
#         print(f'Город {self.name}, население {self.population} чел.')
#
#
# class Mountain(Point):
#     def __init__(self, latitude, longitude, name, height):
#         super().__init__(latitude, longitude)
#         self.name = name
#         self.height = height
#
#     def show(self):
#         print(f'Высота горы {self.name} - {self.height} м.')
#
#
# def print_how_far(geo_object_1, geo_object_2):
#     print(f'От точки «{geo_object_1.name}» до точки «{geo_object_2.name}» — '
#           f'{geo_object_1.distance(geo_object_2)} км.')
#
#
# moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
# everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
# chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)
#
# moscow.show()
# everest.show()
# print_how_far(moscow, everest)
# print_how_far(moscow, chelyabinsk)


class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print(f'Очень интересный вопрос! Не знаю.')


class Student(Human):
    def ask_question(self, someone, question):
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print()


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print(f'Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)


class CodeReviewer(Human):
    def answer_question(self, question):
        if question != 'что не так с моим проектом?':
            super().answer_question(question)
        else:
            print('О, вопрос про проект, это я люблю.')


class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
