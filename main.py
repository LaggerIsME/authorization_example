from User import *
from Auth import *
def main():
    auth = Auth()
    s = 'Print your '
    username = input(s + 'username: ')
    name = input(s + 'name: ')
    surname = input(s + 'surname: ')
    age = input(s + 'age: ')
    password = input(s + 'password: ')
    man = User(username, name, surname, age, password)
    #print(auth.register(man, password))
    #print(auth.login(man, password))
    print(auth.change_password(man, password))
main()