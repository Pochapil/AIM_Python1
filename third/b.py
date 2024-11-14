import functools
import inspect


def check_arguments(*arg_types):
    # @functools.wraps(func)
    def decorate(func):
        # l = inspect.getargspec(func)
        sig = inspect.signature(func)
        # bound_types = sig.bind_partial(*arg_types).arguments
        # @functools.wraps(func)
        def wrapper(*args):

            bound_values = sig.bind(*args)
            nm = func.__name__
            func_obj = func
            # types = func.__type_params__
            dicts = func.__dict__
            frame = inspect.currentframe()
            args, _, _, values = inspect.getargvalues(frame)

            argies = locals().keys()
            argies = locals()
            args = [1, 2]
            if len(arg_types) > len(args):
                raise TypeError
            else:
                for i, arg_type in enumerate(arg_types):
                    if not isinstance(args[i], arg_type):
                        raise TypeError
            return func(*args)
        return wrapper
    return decorate
        # return func(*args, **kwargs)

    # return wrapper


@check_arguments(int, str)
def f(a, b):
    print(a, b)


try:
    f(1, 5)
except Exception as e:
    print('not good')
