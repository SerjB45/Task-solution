import sys
import importlib
import time

PATH_TO_MODULE = 'src.TaskSolution.'
FILE_MODULE_CLS = 'src\TaskSolution\List Of Modules With Class.txt'
FILE_MODULE_FUNC = 'src\TaskSolution\List Of Modules With Functions.txt'

class Singltone(type):
    _instances = {}
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]     

class App(metaclass=Singltone):
    def __init__(self):
        self.__infomodules = [FILE_MODULE_CLS, FILE_MODULE_FUNC]
        self.__options = self.get_options()
        self.__modules = None
        print('Programm run')

    def exit_programm(self):
        print('Exit')
        sys.exit()

    def call_func(self, func_info):
        if func_info[0] == 'exit':
            self.exit_programm()

        print('Started: ', 'module -', func_info[0], 'Function - ', func_info[1])
        self.call_function(func_info[0], func_info[1])
        print('Stopped\n')

    def call_function(self, name_module, name_function):
        module = importlib.import_module(PATH_TO_MODULE + name_module)
        func = getattr(module, name_function)
        func()   
    
    def create_object(self, cls_info):
        print('Started: ', 'module -', cls_info[0], 'Class - ', cls_info[1])
        self.execute(cls_info[0], cls_info[1])
        print('Stopped\n')     

    def execute(self, name_module, name_class):
        module = importlib.import_module(PATH_TO_MODULE + name_module)
        cls = getattr(module, name_class)
        instance = cls()
        instance.execute()

    def get_options(self):
        options = { 'q' : ['exit', 'function'] }
        numb_options = 0
        self.__modules = []
        for file in self.__infomodules:
            with open(file, 'r') as file:
                self.__modules += file.readlines()
            
        for index, module in enumerate(self.__modules):
            numb_options += index
            options[str(numb_options)] = [ tech_info for tech_info in module.strip().split('/')]

        return options    

    def choise_option(self):
        while True:
            print('=' * 10, 'Options', '=' * 10)
            for option in self.__options:
                print(f'{option}  -  {self.__options[option]}')
            print('=' * 29, '\n')    
            try: 
                option = input('Choise function: ').lower()
            except EOFError:
                print('Incorrect input')
                continue
            
            try:
                choise_option = self.__options[option]
            except KeyError:
                print('Function/Class not found')
                continue
            
            match choise_option[len(choise_option) - 1]:
                case 'function':
                    self.call_func(choise_option)
                case 'class':
                    self.create_object(choise_option)
            time.sleep(1)        




    