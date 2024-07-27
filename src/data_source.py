"""Ссылка на источник данных"""

import pandas as pd


def receiving_data():
    """Функция получения данных для программы"""
    data_frame = pd.read_excel("../data/operations.xlsx")
    return print(data_frame)
