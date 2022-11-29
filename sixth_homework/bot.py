from random import choice
import json

films = list()


def save():
    with open('films.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(films, ensure_ascii=False))
    print('Фильмотека выгружена в файл films.json')


def load():
    global films
    with open('films.json', 'r', encoding='utf-8') as f:
        films = json.load(f)
    print('Фильмотека загружена из файла films.json')


try:
    load()
except:
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властилин колец")
    films.append("Гордость и предубеждение")
    films.append("Санта Барбара")


while True:
    command = input("Введите команду ")
    if command == '/start':
        print('Бот-фильмотека начал свою работу')
    elif command == '/stop':
        save()
        print('Бот остановил свою работу. Заходите ещё, будем рады!')
        break
    elif command == '/all':
        print('Вот текущий список фильмов')
        print(films)
    elif command == '/add':
        f = input('Введите название фильма: ')
        films.append(f)
        print('Фильм был успешно добавлен в коллекцию!')
    elif command == '/remove':
        f = input('Введите название фильма, который необходимо удалить: ')
        try:
            films.remove(f)
            print('Фильм был успешно удален из коллекции!')
        except ValueError:
            print("This value does not exist")
    elif command == '/random':
        # index = randint(0, len(films) - 1)
        # print(f'Случайный фильм для вас {films[index]}')
        print(f'Случайный фильм для вас {choice(films)}')
    elif command == '/save':
        save()
    elif command == '/load':
        load()
    elif command == '/help':
        print('Здесь какой-то мануал.')
    else:
        print('Неопознанная команда. Просьба изучить мануал через /help')