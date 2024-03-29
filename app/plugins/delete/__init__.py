"""Delete history CSV file"""
import logging
import os
import pandas as pd
from app.commands import Command


class DeleteCommand(Command):
    """Delete history CSV file"""
    def execute(self):
        """Executes command"""
        data_dir = './data'
        csv_file_path = os.path.join(data_dir, 'calc_history.csv')
        if os.path.exists(csv_file_path):
            logging.info("Deleted file: %s",csv_file_path)
            os.remove(csv_file_path)
