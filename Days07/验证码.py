import random
def generate_code(code_len=4):
    all_chars = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    last_pos = len(all_chars) - 1  #randint左右两侧都为闭区间
    code = ''
    for _ in range(code_len):
            index = random.randint(0,last_pos)
            code += all_chars[index]
    return code

print(generate_code())