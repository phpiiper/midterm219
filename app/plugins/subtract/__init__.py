import logging
from app.commands import Command


class SubtractCommand(Command):
    def execute(self):
        print("SUBTRACT!")