

ps = [{
        "firstname": input('Имя: '),
        "lastname": input('Фамилия: '),
        "middlename": input('Отчество: '),
        "birthdate": input('Год рождения: '),
        "diseases": input('Заболевания: '),
    } for _ in range(2)]

header = ['firstname', 'lastname', 'middlename', 'birthdate', 'diseases']

for col in header:
    print(f'\t{col} \t|', end='')

print('\n', '-'*130)



for person in ps:
    for k, v in person.items():
        print(f'\t\t{v} \t|', end='')
    print('\n', '-'*130)
