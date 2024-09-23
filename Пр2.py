hello = "Hello Word"
first_name = "Vika"
last_name = "Tykhonchuk"
age = 16

print(hello, "-", type(hello))
print(first_name, "-", type(first_name))
print(last_name, "-", type(last_name))
print(age, "-", type(age))

types = [type(hello), type(first_name), type(last_name), type(age)]

print("Список типів змінних:", types)

if all(t == types[3] for t in types):
    print("good")
else:
    first_type = types[3]
    types = [t for t in types if t == first_type]
    print("Типи після видалення відмінних:", types)