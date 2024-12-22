my_dict = {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
print(my_dict)
print(my_dict["Johnny"])
print(my_dict.get('Anton'))
my_dict.update({'Anton':4.5, 'Olay':5.0})
print(my_dict.pop('Bilbo'))
print(my_dict)
# Множества
my_set = {1,2,3,4.5,6,3,True,'Foton',True,3,True,'Anton',4,False,4.5,6,3}
print(my_set)
my_set.add((1,2,6))
my_set.add('Olay')
my_set.discard('Anton')
print(my_set)