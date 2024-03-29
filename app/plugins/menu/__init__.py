"""Command to show menu"""
import logging
from app.commands import Command
from app import App


class MenuCommand(Command):
    """Command to show menu of commands"""
    def get_commands(self):
        """Gets list of commands"""
        app = App()
        return app.commandList
    def execute(self):
        """Executes command"""
        commands = self.get_commands()
        string = "\n"
        string += '-----------------\n'
        string += 'List of Commands: \n'
        for command in commands:
            string += " > " + command + "\n"
        string += '-----------------'
        print(string)
        logging.info("Displayed List of Commands")
        logging.info(string)
