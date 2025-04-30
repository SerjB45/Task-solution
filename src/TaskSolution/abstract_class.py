import abc 

class RunningFunctions(abc.ABC):
    @abc.abstractmethod
    def execute(self):pass

    
    def select_input(self):
        choise = input('Handle input or Auto(h/a): ')
        match choise.lower():
            case 'h':
                self.handle_input()
            case 'a':
                self.auto_input()
            case _:    
                self.auto_input()

    @abc.abstractmethod
    def handle_input():
        pass

    @abc.abstractmethod
    def auto_input():
        pass
