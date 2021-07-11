import random as rand

LETTERS_CAN_BE_USED = 'йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm'
LETTERS_CAN_BE_USED += LETTERS_CAN_BE_USED.upper() + ''',.1234567890-=`~!@#$%^&*()_+[]{};: '"\\|<>/?\n'''

LETTERS_TO_CODE = LETTERS_CAN_BE_USED

# print(LETTERS_TO_CODE)


def key_to_seed(key: str) -> int:
    seed = 2

    for i in key:
        seed += ord(i)
        seed *= ord(i)

    return seed


def text_to_code(key: str, text: str) -> str:
    seed = key_to_seed(key)
    rand.seed(seed)

    code = ''.join([LETTERS_TO_CODE[rand.randint(0, len(LETTERS_TO_CODE) - 1)] for i in range(rand.randint(0, 10))])
    for i in text:
        if i not in LETTERS_CAN_BE_USED:
            continue

        n = [(rand.randint(0, len(LETTERS_TO_CODE) - 1)) for _ in range(rand.randint(1, 10))]
        n = [j + LETTERS_TO_CODE.index(i) for j in n]
        n = [j % len(LETTERS_TO_CODE) for j in n]
        n = [LETTERS_TO_CODE[j] for j in n]

        code += ''.join(n)

    return code


def code_to_text(key: str, code: str) -> str:
    seed = key_to_seed(key)
    rand.seed(seed)

    text = ''.join([LETTERS_TO_CODE[rand.randint(0, len(LETTERS_TO_CODE) - 1)] for i in range(rand.randint(0, 10))])
    code = code[len(text):]

    while code:
        n = rand.randint(1, 10)

        letter = LETTERS_TO_CODE.index(code[0])
        code = code[n:]

        rand_letter = [(rand.randint(0, len(LETTERS_TO_CODE) - 1)) for _ in range(n)][0]

        if rand_letter > letter:
            letter += len(LETTERS_TO_CODE)

        target_letter = LETTERS_TO_CODE[letter - rand_letter]

        text += target_letter

    return text


def my_input(fun) -> tuple:
    print('Введите ключ\n')
    key = input()
    print('Введите имя файла\n')
    file_name = input()
    text = open(file_name, encoding='UTF-8').read()

    return file_name, fun(key, text)


if __name__ == '__main__':
    print('Закодировать - 0\n'
          'Разкодировать - 1\n')

    num = 2

    try:
        num = int(input())
    except Exception as x:
        input(f'ERROR: {x}\n')
        exit(0)

    if num == 0:
        func = text_to_code
    elif num == 1:
        func = code_to_text
    else:
        input('ERROR\n')
        exit(0)

    ret = my_input(func)

    f = open(ret[0][:-4] + '_' + ('de' if num else '') + 'code.txt', 'w', encoding='UTF-8')
    f.write(ret[1])
    f.close()




