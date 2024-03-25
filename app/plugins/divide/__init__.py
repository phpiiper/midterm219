import logging
from app.commands import Command


class DivideCommand(Command):
    def execute(self):
        print("DIVIDE!")