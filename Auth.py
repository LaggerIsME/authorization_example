from User import *
import json
class Auth():

    #Метод регистрации
    def register(self, user, password):
        #Создание словаря для записи его в json-файл
        new_dict = { user.get_username():{
                'name' : user.get_name(), 
                'surname' : user.get_surname(), 
                'age' : user.get_age(), 
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
    def login(self, user, password):
        #Желает ли человек войти
        answer = input('Do you want login?[Y/N] ').upper()
        if(answer == 'Y' ):

            #Значения входящего
            new_dict = {user.get_username():{
                'name' : user.get_name(), 
                'surname' : user.get_surname(), 
                'age' : user.get_age(), 
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
                            count += 1

            if(count == len(new_dict[next(iter(new_dict))].keys())):
                return 'You are in your account!'
                
            else:
                return 'Fail!'

        elif(answer == 'N'):
            return 'OK!'
            
        else:
            return 'Fail!'
    
    #Метод смены пароля
    def change_password(self, user, password):
        #Желает ли человек сменить пароль
        answer = input('Do you want change password?[Y/N] ').upper()
        if(answer == 'Y'):
            a = input('Write previous password: ')
            with open('Users.json', 'r') as file:
                #Извлечение изначального словаря
                data = json.load(file)
            checker = False
            for i in data:
                if(i == user.get_username()):
                    if(data[i]['password'] == password):
                        checker = True
            if(checker):
                new_password = input('Write new password: ')
                with open('Users.json', 'r') as file:
                #Извлечение изначального словаря
                    data = json.load(file)
                for i in data:
                    if(i == user.get_username()):
                        data[i]['password']  = new_password
                        with open('Users.json', 'w') as file:
                        #Загружаю измененный словарь
                            json.dump(data, file, indent = 4)
                        return 'The password was changed'
            else:
                return 'Fail!'
        elif(answer == 'N'):
            return 'OK!'
        else:
            return 'Fail!'


        