import json
filename = 'numbers.json'
numbers = [5,7,5,8,9,3,2,1]
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
with open(filename) as f_obj:
    number = json.load(f_obj)
print(number)

filename = 'favorite_numbers.json'
try:
    with open(filename) as f_obj1:
        favorite_number = json.load(f_obj1)
except FileNotFoundError:
    favorite_number = input('Enter your favorite number: ')
    with open(filename,'w') as f_obj2:
        json.dump(favorite_number,f_obj2)
else:
    print('Your favorite number is : '+favorite_number )