# from  model import *
from view import *

def app():
    command_number = 10
    while command_number != 0:
        print_menu()
        command_number = int(input())
        match command_number:
            case 1:
                print(1)
            case 2:
                print(2)
            case 3:
                print(3)
            case 4:
                print(4)
            case 5:
                print(5)
            case 0:
                break
            case _:
                print_comand_not_exist()