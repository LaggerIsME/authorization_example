from User import *
import json
class Auth():

    #Метод регистрации
    def register(self):
        #Ввод данных в объект пользователя
        s = 'Print your '
        username = input(s + 'username: ')
        name = input(s + 'name: ')
        surname = input(s + 'surname: ')
        age = input(s + 'age: ')
        password = input(s + 'password: ')

        #Создание словаря для записи его в json-файл
        new_dict = { username:{
                'name' : name, 
                'surname' : surname, 
                'age' : age, 
                'password' : password}
        }

        #Запись в файл
        with open('Users.json', 'r') as file:
            #Извлекаю изначальный словарь
            data = json.load(file)
            #Модифицирую его
            data.update(new_dict)
        with open('Users.json', 'w') as file:
            #Загружаю измененный словарь
            json.dump(data, file, indent = 4)
        return 'User was registered!'

    #Метод входа в аккаунт    
    def login(self):
        #Желает ли человек войти
        answer = input('Do you want login?[Y/N]').upper()
        if(answer == 'Y' ):

            #Запрос информации
            s = 'Print your '
            username = input(s + 'username: ')
            name = input(s + 'name: ')
            surname = input(s + 'surname: ')
            age = input(s + 'age: ')
            password = input(s + 'password: ')
            
            #Значения входящего
            new_dict = {username:{
                'name' : name, 
                'surname' : surname, 
                'age' : age, 
                'password' : password
            }}
            
            with open('Users.json', 'r') as file:
                #Извлечение изначального словаря
                data = json.load(file)
            #Счетчик
            count = 0
            
            #Итерация словарей внутри словаря
            for i in data:
                #Получение основного ключа из словаря
                if(i == next(iter(new_dict))):
                #Итерация значения внутренних словарей
                    for key, value in data[i].items():
                        #dict[наружний ключ][внутренний ключ]
                        if(value == new_dict[next(iter(new_dict))][key]):
                            print(value)
                            print(new_dict[next(iter(new_dict))][key])
                            count =+ 1

            if(count == len(new_dict.keys())):
                return 'You are in account!'
                
            else:
                return 'Fail!'

        elif(answer == 'N'):
            return 'OK!'
            
        else:
            return 'Fail!'
    

        