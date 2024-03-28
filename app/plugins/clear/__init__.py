import logging
import os
from app.commands import Command
import pandas as pd
from app import App
import json


class ClearCommand(Command):
    def execute(self):
        app = App()
        data_dir = './data'
        csv_file_path = os.path.join(data_dir, 'calc_history.csv')
        try:
            app = App()
            cols = json.loads(app.get_environment_variable("DATACOLUMNS")) if app.get_environment_variable("DATACOLUMNS") else ["Oper.","Vars."]
            df_data = pd.DataFrame(columns=cols)
            df_data.to_csv(csv_file_path, index=False)
            logging.info("Cleared ")
        except Exception as e:
            logging.error(f"File cannot be cleared: {e}")
        