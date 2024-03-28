from app.commands import Command
from app import App
import logging


class MenuCommand(Command):
    def getList(self):
        app = App()
        return app.commandList
    def execute(self):
        commands = self.getList()
        string = "\n"

        string += '-----------------\n'
        string += 'List of Commands: \n'
        for command in commands:
            string += " > " + command + "\n"
        string += f'-----------------'
        print(string)
        logging.info("Displayed List of Commands")
        logging.info(string)