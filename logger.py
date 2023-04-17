import datetime
from datetime import date

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



if __name__ == '__main__':
    pass