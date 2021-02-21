from helper import *
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore')

def main(kod_path, label_path):
    data, questions_df, semi_open = load_frames(kod_path, label_path)
    tshuvot_df, questions_df = create_tshuvot(data, questions_df, semi_open)
    return tshuvot_df, questions_df

if __name__ == '__main__':
        tshuvot_df, questions_df = main(os.getcwd() + r'\seker\seker_kod.xlsx', os.getcwd() + r'\seker\seker_label.xlsx')
        print(tshuvot_df.head())
