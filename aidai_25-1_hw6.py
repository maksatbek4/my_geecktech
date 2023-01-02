import re
data = open('MOCK_DATA.txt', 'r')
content = data.read()
data.close()

while True:
    print('1 - Считать имена и фамилии')
    print('2 - Считать все емайлы')
    print('3 - Считать названия файлов')
    print('4 - Считать цвета')
    print('5 - Выход')
    command = input('Введите команду: ')
    if command == '1':
        with open('name_surname.txt', 'w') as file:
            names_list = re.findall(r'[A-Z][a-z\-]+\s[A-Za-z\' ]+\b', content)
            for name in names_list:
                file.write(name + '\n')
    elif command == '2':
        with open('email.txt', 'w') as file:
            emails_list = re.findall(r'(\b[\w]+@[\w\-]+(\.[\w]+)+)', content)
            for email in emails_list:
                file.write(email[0] + '\n')
    elif command == '3':
        with open('files.txt', 'w') as file:
            files_list = re.findall(r'\t[\w]+\.[\w]+', content)
            for files in files_list:
                file.write(files[1:] + '\n')
    elif command == '4':
        with open('colors.txt', 'w') as file:
            colors_list = re.findall(r'#[\w]{6}', content)
            for color in colors_list:
                file.write(color + '\n')
    elif command == '5':
        break
    else:
        print('ННеизвастная команда')
