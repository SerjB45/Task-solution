from src.TaskSolution.abstract_class import RunningFunctions
# from src.TaskSolution.help_functions import time_memory_used

class TestModule(RunningFunctions):
    def __init__(self):
        super().__init__()
        self.message = ''

    def execute(self):
        print('----Test create object----')
        self.select_input()
        self.print_new_message(self.message)

    def handle_input(self):
        self.message = input('Enter the message: ')
        pass

    def auto_input(self):
        self.message = 'Auto message'
        
    def print_new_message(self, mess):
        print('Your message >>', mess)
           

# @time_memory_used
def test_func():
    print('----Test call function----')
        