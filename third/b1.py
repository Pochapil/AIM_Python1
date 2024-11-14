import functools


def check_arguments(*arg_types):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args):
            if len(arg_types) > len(args):
                raise TypeError
            else:
                for i, arg_type in enumerate(arg_types):
                    if not isinstance(args[i], arg_type):
                        raise TypeError
            return func(*args)

        return wrapper

    return decorate


@check_arguments(int, str)
def f(a, b):
    print(a, b)


try:
    f(1, 'a')
except Exception as e:
    print('not good')
