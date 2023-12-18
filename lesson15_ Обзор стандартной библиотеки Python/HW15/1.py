from random import randint
import logging
from argparse import ArgumentParser

logging.basicConfig(filename='guess_num.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )


def guess_num(low_=0, up_=10, count=3):
    start = "Игра началась"
    logging.info(start)
    num = randint(low_, up_)

    while count > 0:
        logging.info(f"Попыток осталось: {count}")
        print('Попытка', count)
        count -= 1
        try:
            choice = int(input('Введите ваше число: '))
            logging.info(f"Выбор пользователя: {choice}")
            if choice > num:
                print('Не угадали - меньше')
                logging.info('Пользователь указал число больше, чем загаданное.')
            elif choice < num:
                print('Не угадали - больше')
                logging.info('Пользователь указал число больше, чем загаданное.')
            else:
                print('Вы угадали')
                win = "Пользователь указал верное число. Игра закончилась."
                logging.info(win)
                quit()

        except ValueError as e:
            logging.error(f"Неправильный ввод: {e}. Пожалуйста введите число.")
            print("Неправильный ввод. Пожалуйста введите число.")

    print(f'Попытки закончились')
    out_of_attempts = "Попытки закончились. Игра закончилась."
    logging.info(out_of_attempts)
    quit()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--low", type=int, help="Нижняя граница для загадываемого числа", default=0)
    parser.add_argument("--up", type=int, help="Верхняя граница для загадываемого числа", default=10)
    parser.add_argument("--count", type=int, help="Количество попыток", default=3)
    args = parser.parse_args()

    print(guess_num(args.low, args.up, args.count))
