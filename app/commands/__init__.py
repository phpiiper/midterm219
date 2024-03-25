from abc import ABC, abstractmethod
import multiprocessing
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
    def execute_command(self, command_name: str,args=[]):
        try:
            if (len(args) == 0):
                process = multiprocessing.Process(target=self.commands[command_name].execute())
            else:
                process = multiprocessing.Process(target=self.commands[command_name].execute(args))
            process.start()
            process.join()
        except KeyError:
            print(f"No such command: {command_name}")
