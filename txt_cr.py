def imp_txt(pers):
    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(str(pers)+'\n')


def exp_txt():
    with open('data.txt', 'r', encoding='utf-8') as f:
        result = f.read().splitlines()
        for pers in result:
            print(pers)
