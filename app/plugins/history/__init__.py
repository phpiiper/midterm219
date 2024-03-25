import logging
from app.commands import Command


class HistoryCommand(Command):
    def execute(self):
        print("HISTORY!")