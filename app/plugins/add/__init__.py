import logging
from app.commands import Command


class AddCommand(Command):
    def execute(self):
        print("ADD!")