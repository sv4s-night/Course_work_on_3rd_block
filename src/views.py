""" Веб-страница """



""" Страница «Главная»          -> answer.json
#json #requests #API #datetime #logging #pytest #pandas

Реализуйте набор функций и главную функцию, принимающую на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS 
и возвращающую JSON-ответ со следующими данными:

1. Приветствие в формате "???", где ??? — «Доброе утро» / «Добрый день» / «Добрый вечер» / «Доброй ночи» в зависимости от текущего времени.

2. По каждой карте:
последние 4 цифры карты;
общая сумма расходов;
кешбэк (1 рубль на каждые 100 рублей).

3. Топ-5 транзакций по сумме платежа.
4. Курс валют.
5. Стоимость акций из S&P500.

"""

import datetime as dt
from src.utils import mask_account_card


# +
def get_greeting():
    """1. Функция - приветствие в зависимости от времени суток"""
    hour = dt.datetime.now().hour
    if 4 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 17 <= hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"
# ========================================================================


def bank_card_information(dframe):
    """2. Информация по каждой карте:"""
    """2. По каждой карте:                      bank_card_information
                            последние 4 цифры карты;
                            общая сумма расходов;
                            кешбэк (1 рубль на каждые 100 рублей)."""

    info_cards = mask_account_card()

    pass



def mask_card_number(dframe):
    """2.1 последние 4 цифры карты"""
    pass


def total_expenses():
    """2.2 общая сумма расходов"""
    pass



def cashback():
    """2.3 Ф кешбэк (1 рубль на каждые 100 рублей)."""
    pass



# ======================================================================================================



def top_transactions(number=5):
    """3. Функция Топ-5 транзакции по сумме платежа."""
    pass
# ======================================================================================================


def exchange_rate():
    """4. Функция Курса валют."""
    pass
# ======================================================================================================


def stock_price(default="S&P 500"):
    """ 5. Функция Стоимость акций из S&P 500."""
    pass
