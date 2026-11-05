import pandas as pd
import os
import openpyxl
from common.config import AppConfig
FILE=AppConfig.FILENAME
def save_to_excel(dataset):
    try:
        new_df = pd.DataFrame(dataset)

        if os.path.exists(FILE):

            old_df = pd.read_excel(FILE)

            df = pd.concat([old_df, new_df])
        else:
            df = new_df


        df.to_excel(FILE, index = False)

        print("Dane zostały zapisane w pliku")
    except Exception as e:
        print(e)


def read_excel():
    try:
        df = pd.read_excel(FILE)
        print(f"Odczytano plik "
              f"{df}")
        return df
    except Exception as e:
        print("Nie udało się odczytać pliku")
        return




