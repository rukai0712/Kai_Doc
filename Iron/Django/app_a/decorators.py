from functools import wraps

def decorator(func):
    '''
    没有参数的装饰器
    '''
    @wraps(func, assigned=available_attrs(func))
    def inner(arg_a, arg_b, arg_c):
        pass
    return inner


def decorator_with_parameter(par_a, par_b, par_c):
    '''
    有参数的装饰器
    '''
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(arg_a, arg_b, arg_c):
            pass
        return inner
    return decorator
