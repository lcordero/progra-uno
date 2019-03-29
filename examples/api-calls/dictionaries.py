# Dictionaries

# === Method KEYS ===
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())


# === Method fo adding ===
d = {'key':'value'}
print(d)
# {'key': 'value'}
d['mynewkey'] = 'mynewvalue'
print(d)
# {'mynewkey': 'mynewvalue', 'key': 'value'}


# === Method DELTE ===
d = {'key1':'value1', 'key2': 'value2'}
print(d)
# {'key': 'value'}

del d['key1']


# === Method GET ===
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))



# ==== EJERCICIO ====
# Crear un diccionario y llenarlo con productos de compras de supermercado
# El usuario debe proveer los productos
