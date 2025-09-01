import time
from sympy import isprime
from functools import wraps


def benchmark_squares(iters=10):
    def act_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()

                if i == iters - 1:
                    ret_res = func(*args, **kwargs)
                else:
                    func(*args, **kwargs)

                time_spent = time.time() - start
                total += time_spent
            print(f'time benchmark of counting the squares is {total} sec.')
            return ret_res
        return wrapper
    return act_dec


def benchmark_filter(iters = 10):
    def act_dec(func):
        @wraps(func)
        def wrapper(opt, *args):
            total = 0
            for i in range(iters):
                start = time.time()

                if i == iters - 1:
                    ret_res = func(opt, *args)
                else:
                    func(opt, *args)

                time_spent = time.time() - start
                total += time_spent
            print(f'time benchmark of filtering function (mode {opt}) is {total} sec.')
            return ret_res
        return wrapper
    return act_dec


def show_nested_enters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) == 0:
            curr_depth = 0
        else:
            curr_depth = args[0]
        i = list(kwargs.values())[0]

        print(curr_depth * '__' + f'-->fib({i})')
        res = func(curr_depth, sequence_number=i)
        print(curr_depth * '__' + f'<--fib({i})')
        return res
    return wrapper


@benchmark_squares(iters=10000)
def count_squares(*args, **kwargs):
    """
    принимает N целых чисел и возвращает список значений этих чисел в заданной степени
    :param args: список чисел
    :param kwargs: степень, в которую они будут возводиться
    :return: кортеж с результатом возведения в степень
    """
    deg = list(kwargs.values())[0]
    return tuple(pow(num, deg) for num in args)


@benchmark_filter(iters=20000)
def filter_numbers(option, *args):
    """
    принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа
    :param option: определяет критерий фильтрации (0,1,2)
    :param args: писок чисел
    :return: кортеж отфильтрованных значений
    """
    if option == 0:
        return tuple(filter(lambda x: x % 2 == 0, args))
    elif option == 1:
        return tuple(filter(lambda x: x % 2 != 0, args))
    return tuple(filter(lambda x: isprime(x), args))


@show_nested_enters
def count_fib_numbers(curr_depth=1, sequence_number=5):
    """
    вычисляет значение N-го числа Фибоначчи
    :param sequence_number: номер искомого значения числовой последовательности
    :param curr_depth: текущая глубина рекурсии (используется для форматирования вывода в декораторе)
    :return: значение искомой величины в последовательности
    """

    if sequence_number > 2:
        curr_depth += 1
        fib = (count_fib_numbers(curr_depth, sequence_number=sequence_number - 2) +
               count_fib_numbers(curr_depth, sequence_number=sequence_number - 1))
    else: fib = 1
    return fib


if __name__ == '__main__':
    numbers = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,)
    degree = 2
    res = count_squares(*numbers, index=degree)
    print(f'the result of raising the following numbers:\n{numbers}\n'
          f'into the power {degree}:\n'
          f'{res}\n')

    filt = filter_numbers(0,*numbers)
    print(f'even numbers: {filt}')
    filt = filter_numbers(1,*numbers)
    print(f'uneven numbers: {filt}')
    filt = filter_numbers(2,*numbers)
    print(f'prime numbers: {filt}\n')

    fib_num = 20
    res = count_fib_numbers(sequence_number=fib_num)
    print(f'the value of Fibonacci number {fib_num} is {res}\n')

    print(count_squares.__name__)
    print(count_squares.__doc__)
    print()

    print(filter_numbers.__name__)
    print(filter_numbers.__doc__)
    print()

    print(count_fib_numbers.__name__)
    print(count_fib_numbers.__doc__)

