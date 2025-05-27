from datetime import datetime

class Vika:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return "Рік народження не вказано"
        current_year = datetime.now().year
        age = current_year - self.birth_year
        course = age - 15  # Вступ до коледжу з 15 років
        if course < 1:
            return "Ще не студентка"
        elif course > 4:
            return "Можливо вже випускниця"
        else:
            return f"{course} курс"

    def get_fullname_list(self):
        return [self.name, self.surname]

# Приклад використання:
student = Vika("Vika", "Tykhonchuk", 2008)
print(student.calculate_course())         # Наприклад: "2 курс", якщо зараз 2025 рік
print(student.get_fullname_list())        # ["Vika", "Tykhonchuk"]

# Приклад з дефолтними значеннями:
default_student = Vika()
print(default_student.calculate_course())  # "Рік народження не вказано"
print(default_student.get_fullname_list()) # [None, None]

#Лябук Тарас КРАСАВЧИК P.S. Артем Пуцак 27.05.2025 15:15
