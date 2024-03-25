import logging
from app.commands import Command


class MultiplyCommand(Command):
    def execute(self):
        print("MULTIPLY!")