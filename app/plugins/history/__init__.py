import logging
import os
from app.commands import Command
import pandas as pd


class HistoryCommand(Command):
    def execute(self):
        data_dir = './data'
        csv_file_path = os.path.join(data_dir, 'calc_history.csv')
        try:
            df_read_states = pd.read_csv(csv_file_path)
            print("Calc History:")
            for item in df_read_states.iterrows():
                print(f"{item[1][0]}, {item[1][1]}")
        except:
            print("Unavailable")
        