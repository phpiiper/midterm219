import logging
import os
import pandas as pd


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
        for item in df_read.iterrows():
            oper_list.append([item[1][0],item[1][1]])
    if (operation):
        oper_list.append([operation[0],operation[1]])

    df_data = pd.DataFrame(oper_list, columns=['Operation', 'Variables'])
    df_data.to_csv(csv_file_path, index=False)
        
    logging.info(f"States saved to CSV at '{csv_file_path}'.")
    csv_file_path = os.path.join(data_dir, 'calc_history.csv')
    logging.info(f'the relative path  to save my file is {csv_file_path}')
    absolute_path = os.path.abspath(csv_file_path)
    logging.info(f'the absolute path  to save my file is {absolute_path}')