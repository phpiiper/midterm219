import logging
import os
from app.commands import Command
import pandas as pd
from app import App


class HistoryCommand(Command):
    def execute(self):
        app = App()
        data_dir = './data'
        csv_file_path = os.path.join(data_dir, app.get_environment_variable("HISTORYFILENAME","history.csv"))
        try:
            df_read = pd.read_csv(csv_file_path)
            print("Calc History:")
            logging.info(f"Printed History")
            print("Operation, Values")
            logging.info(f"Operation, Values")
            oper_list = [list(item) for item in df_read.values] if not df_read.empty else []
            for item in oper_list:
                print(f" > {item[0]}, {item[1]}")
                logging.info(f" > {item[0]}, {item[1]}")
        except:
            print("History is unavailable.")

        