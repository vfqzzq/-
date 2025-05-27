from datetime import datetime

# Базовий клас з ЛР1
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
        course = age - 15  # Вступ до коледжу у 15 років
        if course < 1:
            return "Ще не студентка"
        elif course > 4:
            return "Можливо вже випускниця"
        else:
            return f"{course} курс"

    def get_fullname_list(self):
        return [self.name, self.surname]

# Дочірній клас
class Student(Vika):
    def __init__(self, name=None, surname=None, birth_year=None, group=None, specialty=None, grade_average=None):
        super().__init__(name, surname, birth_year)
        self.group = group
        self.specialty = specialty
        self.__grade_average = grade_average  # Приватне поле

    def _is_scholarship_eligible(self):
        """Protected метод: перевіряє, чи студентка має стипендію"""
        if self.__grade_average is None:
            return "Оцінки не вказані"
        return self.__grade_average >= 9

    def student_info(self):
        """Метод, що повертає загальну інформацію про студентку"""
        info = f"Студентка {self.name} {self.surname}, спеціальність: {self.specialty}, група: {self.group}, середній бал: {self.__grade_average}"
        return info

# Приклад використання:
student2 = Student("Vika", "Tykhonchuk", 2008, "21-ІСT", "Інформаційні системи та технології", 10.5)

print(student2.calculate_course())            # 2 курс
print(student2.get_fullname_list())           # ['Vika', 'Tykhonchuk']
print(student2.student_info())                # Повна інформація про студентку
print(student2._is_scholarship_eligible())    # True (є стипендія)

# Перевірка об'єкта з дефолтними значеннями:
default_st = Student()
print(default_st.student_info())              # Інформація з None
print(default_st._is_scholarship_eligible())  # Оцінки не вказані
