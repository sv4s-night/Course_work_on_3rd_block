from src.views import get_greeting
from src.data_source import receiving_data


# def main():
#     """Главная функция"""
#     dframe = receiving_data()
#     return dframe



def main():
    """ Главная функция возвращающую JSON-ответ"""

    welcome = get_greeting()    # переменная приветствия с учетом времени суток

    data_frame = receiving_data()    # dataframe с данными


    info_cards = bank_card_information(data_frame)
    """2. По каждой карте:                      bank_card_information
                        последние 4 цифры карты;
                        общая сумма расходов;
                        кешбэк (1 рубль на каждые 100 рублей)."""



    """3. Топ-5 транзакций по сумме платежа.    top_transactions"""

    """4. Курс валют.                           exchange_rate"""

    """5. Стоимость акций из S&P500.            stock_price"""

    return welcome  # возврат Json-файл с {welcom},
                    # {bank_card_information},{top_transactions},{exchange_rate},{stock_price}




if __name__ == "__main__":
    print(main())
