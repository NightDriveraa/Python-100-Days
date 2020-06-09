def count_words(file_name):
    try:
        with open(file_name) as f_ojb:
            contens = f_ojb.read()
    except FileNotFoundError:
        print('File not found')
    else:
        words = contens.split()
        num_word = len(words)
        dog_num = contens.count('dog')
        print('have words: '+str(num_word)+' have dog: ' + str(dog_num))

count_words('dog.txt')