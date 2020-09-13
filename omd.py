def question():
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]
        
def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️' ) 
    if question():
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print('Если будет дождь, может, останемся дома?')
    if question():
        return print('Ну и отлично! Посмотрим дома фильм!')
    return step2_no_umbrella()
    
def step2_no_umbrella():
    print('Может лучше побегаем?')
    if question():
        return run()
    return print('Нууу если утка не бежит, то игра закончена')

def run():
    print('Сколько км пробежишь?')
    km = int(input())
    if km >= 5:
        print('В самый раз! Как раз успеем в бар забежать по пути')
    else:
        print('Слишком мало...Даже до бара не добежим')

if __name__ == '__main__':
    step1()



