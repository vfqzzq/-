hello = "Hello Word"
first_name = "Vika"
last_name = "Tykhonchuk"
age = 16

types_list = [type(hello), type(first_name), type(last_name), type(age)]

print("Типи змінних:", types_list)

#all() перевіряє, чи всі елементи у types_list однакові.
#types_list[0] використовується як базовий тип для порівняння, тобто всі інші елементи в types_list повинні відповідати першому типу (<class 'str'>).
#Якщо всі типи однакові, виводиться good.
if all(elem == types_list[0] for elem in types_list):
    print("good")

else:

    unique_type = types_list[0]
    types_list = [t for t in types_list if t == unique_type]
    print("Після видалення відмінного типу:", types_list)
