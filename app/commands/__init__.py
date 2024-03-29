"""Handles commands"""
from abc import ABC, abstractmethod
import multiprocessing
class Command(ABC):
    """A class used to execute code"""
    @abstractmethod
    def execute(self):
        """Placeholder for executing function"""
        pass # pylint: disable=unncessary-pass

class CommandHandler:
    """Handles commands from plugins"""
    def __init__(self):
        self.commands = {}
    def register_command(self, command_name: str, command: Command):
        """Registers a command"""
        self.commands[command_name] = command
    def execute_command(self, command_name: str,args=[]): # pylint: disable=dangerous-default-value
        """Executes command"""
        try:
            if len(args) == 0:
                process = multiprocessing.Process(target=self.commands[command_name].execute())
            else:
                process = multiprocessing.Process(target=self.commands[command_name].execute(args))
            process.start()
            process.join()
        except KeyError:
            print(f"No such command: {command_name}")
