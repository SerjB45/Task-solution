import abc 

class RunningFunctions(abc.ABC):
    @abc.abstractmethod
    def execute(self):pass