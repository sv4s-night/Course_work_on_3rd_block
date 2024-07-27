""" Код, который повторяется """

def mask_account_card(mask_info_card: str) -> str:
    """Функция маскировки карты и счета"""

    masquerade = mask_info_card.split(" ")

    for account_or_card in masquerade:
        if account_or_card.isdigit():

            if len(account_or_card) == 16:
                result = " ".join(masquerade[0:-1]) + get_mask_card_number(account_or_card)
            elif len(account_or_card) > 16:
                result = " ".join(masquerade[0:-1]) + get_mask_account(account_or_card)
            else:
                result = "Вы допустили ошибку при вводе данных счета или карты"

    return result



def get_mask_card_number(number_card: str) -> str:
    """Возвращает замаскированный номер карты"""
    # masks_logger.info("function get_mask_card_number")
    return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер счета"""
    # masks_logger.info("function get_mask_account")
    return f"XXXX{str(account_number)[-4:]}"
