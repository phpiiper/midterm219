import logging
import os
from app.commands import Command
import pandas as pd


class DeleteCommand(Command):
    def execute(self):
        data_dir = './data'
        csv_file_path = os.path.join(data_dir, 'calc_history.csv')
        if os.path.exists(csv_file_path):
            df_read_states = pd.read_csv(csv_file_path)
            logging.info("Deleted file: " + csv_file_path)
            os.remove(csv_file_path)
        else:
            print("File cannot be deleted.")
        