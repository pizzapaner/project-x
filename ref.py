import random

#printing
print('Hello World!')

#Baisc variable set and operations
a = 3
b = 5
c = a + b #3 + 5 = 8

print(c)

#Dictionary
dictionary = {
    'key': 'value',
    3: 'string',
    'value': 4
}

card_dict = {
    1: 'A',
    2: '2',
    10: '10',
    'K': 10
}

print(dictionary['key']) #'value'
print(dictionary[3]) #'string'

#Functions
def random_gen():
    return random.randint(1, 13)

def random_number_count(value):
    return value + random.randint(1, 13)

#for loops through a string - range, len, for
list_of_num = range(5)
tin = 'Tin Ngyuen'

for i in range(len(tin)):
    print(i)

#Boolean syntax and operations

a = True
b = False
c = a and b or a

print(c)

print(input('type your input here:'))