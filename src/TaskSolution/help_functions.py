import tracemalloc
from time import perf_counter
from functools import wraps

def time_memory_used(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start = perf_counter()
        result = function(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        stop = perf_counter()
        print(f'Название функции: {function.__name__}')
        # print(f'Использованный метод: {function.__doc__}')
        print(f'Текущее потребление памяти: {current / 10**6:.6f} мб \n'
              f'Пик использования памяти: {peak / 10**6:.6f} мб ')
        print(f'Операция заняла: {stop - start:.6f} секунд')
        tracemalloc.stop()
        return result
    return wrapper