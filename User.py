class User:

    #Конструктор User-a
    def __init__(self, username, name, surname, age, password):
        #Все свойства класса
        #self. альтернатива this. из Java
        self.__username = username
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__hashed_password = hash(password)

    #Методы для получения значений защищенных полей
    def get_name(self): 
        return self.__name
    def get_username(self):
        return self.__username 
    def get_surname(self):
        return self.__surname
    def get_age(self):
        return self.__age
    def get_hashed_password(self):
        return self.__hashed_password
        
    #Методы для изменения значений защищенных полей
    def set_name(self, name):
        self.__name = name
    def set_username(self, username):
        self.__username = username
    def set_surname(self, surname):
        self.__surname = surname
    def set_age(self, age):
        self.__age = age
    def set_hashed_password(self, hashed_password):
        self.__hashed_password = hashed_password
