import os
import datetime
from datetime import date



# Задание №1
def logger(old_function):

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        dt_now = datetime.datetime.now()
        d_now = date.today()
        time_now = dt_now.time()
        with open('main.log', 'a') as f:
            f.write(f'date: {d_now}\n'
                    f'time: {time_now}\n'
                    f'name: {old_function.__name__}\n'
                    f'arguments: {args}, {kwargs}\n'
                    f'result: {result}\n\n')
        return result
    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'




# Задание №2


def logger2(path):
    def __logger(old_function):

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            dt_now = datetime.datetime.now()
            d_now = date.today()
            time_now = dt_now.time()
            with open(path, 'a') as f:
                f.write(f'date: {d_now}\n'
                        f'time: {time_now}\n'
                        f'name: {old_function.__name__}\n'
                        f'arguments: {args}, {kwargs}\n'
                        f'result: {result}\n\n')
            return result
        return new_function
    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger2(path)
        def hello_world():
            return 'Hello World'

        @logger2(path)
        def summator(a, b=0):
            return a + b

        @logger2(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2(), test_1()


