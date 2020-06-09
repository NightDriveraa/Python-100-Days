import json
filename = 'numbers.json'
numbers = [5,7,5,8,9,3,2,1]
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
with open(filename) as f_obj:
    number = json.load(f_obj)
print(number)

filename = 'username.txt'
try:
    with open(filename) as f_obj1:
        username = json.load(f_obj1)
except FileNotFoundError:
    username = input('Enter your name: ')
    with open(filename,'w') as f_obj2:
        json.dump(username,f_obj2)
        print('We\'ll remeber you when you come back,' + username + ' !')
else:
    print(username + ' welcome back！')
