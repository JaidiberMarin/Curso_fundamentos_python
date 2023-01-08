'''
for element in range(1, 21):
  print(element)

'''

my_list = [23, 45, 67, 89 ,43]
for element in my_list:
  print(element)

my_tuple = ('brayan', 'yonathan', 'german')
for element in my_tuple:
  print(element)


product = {
  'name': 'shirt',
  'price': 100,
  'stock': 89
}

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'brayan',
    'age': 34
  },
  {
    'name': 'yonathan',
    'age': 45
  },
  {
    'name': 'german',
    'age': 4
  }
]

for person in people:
  print('name =>', person['name'])