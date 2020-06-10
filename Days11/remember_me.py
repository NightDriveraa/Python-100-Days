import json
def get_stored_username():
    file_name = 'user_name.txt'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input('Enter your name: ')
    file_name = 'user_name.txt'
    with open(file_name,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print('are you ' + username + ' ?')
        flag = input('yes or no: ')
        if str(flag) == 'yes':
            print('Welcome back,' + username + ' !')
        else:
            get_new_username()
            print('We\'ll remember you when you come back,' + username + ' !')

    else:
        username = get_new_username()
        print('We\'ll remember you when you come back,' + username + ' !')

greet_user()