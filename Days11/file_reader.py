with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

filename = 'pi_digits.txt'
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[0:5])
print(len(pi_string))

pi_string2 = ''
with open('pi_million_digits.txt') as file_object:
    lines2 = file_object.readlines()
for line in lines2:
    pi_string2 += line.strip()
birthday = input('Enter your birthday,in the form mmddyy:')
if birthday in birthday:
    print('Your birthday appears in the first millon digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi')