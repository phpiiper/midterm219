import logging
import os
import pandas as pd
from app import App
import json


def SaveOperation(operation):
    data_dir = './data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        logging.info(f"The directory '{data_dir}' is created.")
    elif not os.access(data_dir, os.W_OK):
        logging.error(f"The directory '{data_dir}' is not writable.")
        return
    
    csv_file_path = os.path.join(data_dir, 'calc_history.csv')
    oper_list = []
    if os.path.exists(csv_file_path):
        df_read = pd.read_csv(csv_file_path)
        if not df_read.empty:
            oper_list = [list(item) for item in df_read.values] if not df_read.empty else []
    if operation:
        oper_list.append([operation[0],operation[1]])
    app = App()
    cols = json.loads(app.get_environment_variable("DATACOLUMNS",["Oper.","Vars."]))
    df_data = pd.DataFrame(oper_list, columns=cols)
    df_data.to_csv(csv_file_path, index=False)
    logging.info(f"Operation saved at '{csv_file_path}'.")
