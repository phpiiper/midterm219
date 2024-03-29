"""Saves operations to CSV file"""
import logging
import os
import json
import pandas as pd
from app import App


def SaveOperation(operation): # pylint: disable=invalid-name
    """Saves an operation, called by successfully inputting one and executing operation"""
    app = App()
    data_dir = app.get_environment_variable("DATADIRNAME",'./data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        logging.info("The directory '%s' is created.",data_dir)
    elif not os.access(data_dir, os.W_OK):
        logging.error("The directory '%s' is not writable.",data_dir)
        return
    fn = app.get_environment_variable("HISTORYFILENAME","history.csv")
    csv_file_path = os.path.join(data_dir, fn)
    oper_list = []
    if os.path.exists(csv_file_path):
        df_read = pd.read_csv(csv_file_path)
        if not df_read.empty:
            oper_list = [list(item) for item in df_read.values] if not df_read.empty else []
    if operation:
        oper_list.append([operation[0],operation[1]])
    cols = json.loads(app.get_environment_variable("DATACOLUMNS",["Oper.","Vars."]))
    df_data = pd.DataFrame(oper_list, columns=cols)
    df_data.to_csv(csv_file_path, index=False)
    logging.info("Operation saved at '%s'.",csv_file_path)
