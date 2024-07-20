'''
Написати декоратор, який буде виводити кількість часу, скільки працювала функція
'''


import time

# def time_function(function):
#     def internal(arg):
#         print('Timing')
#         result = function(arg)
#         print('After timing')
#         # return function(arg)
#         return result
#     return internal


def time_function(function):
    def internal(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f'Function time: {end_time - start_time}')
        # return function(arg)
        return result
    return internal

@time_function
def two_arguments(arg_one, arg_two):
    pass

def three_arguments(arg_one, arg_two, arg_three):
    pass

def three_arguments(arg_one, arg_two, arg_three, name='John'):
    pass

@time_function
def one_argument(arg):
    pass

def zero_args():
    pass

def universal(*args, **kwargs):
    print(args)
    print(kwargs)

def create_a_list(*args):
    # return list(args)
    result_list = []
    for element in args:
        result_list.append(element)
    return result_list

# one_argument('1')
# two_arguments(1, 2)

# three_arguments(1, 2, 3, name='Igor')
# universal(1, 2, 3, name='Igor')

# value_one, *values = (1, 2, 3)
# print(value_one)
# print(values)

print(create_a_list(1, 'hello', 3, 4, 5))

