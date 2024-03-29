"""Clears operations from CSV file"""
import logging
import os
import json
import pandas as pd
from app import App
from app.commands import Command


class ClearCommand(Command):
    """Clears operations from CSV file"""
    def execute(self):
        """Executes function"""
        app = App()
        data_dir = './data'
        csv_file_path = os.path.join(data_dir, 'calc_history.csv')
        try:
            app = App()
            cols = json.loads(app.get_environment_variable("DATACOLUMNS")) if app.get_environment_variable("DATACOLUMNS") else ["Oper.","Vars."]
            df_data = pd.DataFrame(columns=cols)
            df_data.to_csv(csv_file_path, index=False)
            logging.info("Cleared ")
        except Exception as e: # pylint: disable=broad-exception-caught
            logging.error("File cannot be cleared: %s",e)
        