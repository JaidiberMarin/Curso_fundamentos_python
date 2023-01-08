my_dictionary = {}
print(type(my_dict))

my_dict = {
  'avion': "b16",
  'name': 'brayan',
  'last_name': 'marin perez',
  'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))

print('avion' in my_dict)
print('another' in my_dict)