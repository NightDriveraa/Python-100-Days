print('Enter two number')
while(True):
    try:
        num1 = input('first_number: ')
        number1 = int(num1)
        num2 = input('second_number: ')
        number2 = int(num2)
    except ValueError:
        print('请输入数字')
        continue
    else:
        answer = number1 + number2
        print(answer)