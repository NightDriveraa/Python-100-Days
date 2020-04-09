import os
import time
def main():
    message = '123456'
    while True:
        os.system('clear')
        print(message)
        time.sleep(0.2)
        message = message[1:] + message[0]

if __name__ == '__main__':
    main()