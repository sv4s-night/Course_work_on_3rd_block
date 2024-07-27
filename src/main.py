from src.utils import receiving_data


def main():
    """Главная функция"""
    dframe = receiving_data()
    return dframe


if __name__ == "__main__":
    main()
