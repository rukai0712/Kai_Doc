# coding:utf-8


def request_parameter_checker(check_rules, force_ajax=False):
    '''
    用于校验request中的参数是否符合check_rules中的设定
    check_rules - 参数校验规则，为一个list，每条规则如下
    {'p_name':'para_1', 'method':'GET/POST', 'regex':'*', 'must': True, 'desc':u'描述信息'}
    force_ajax - 当参数校验出错时，无论request是否是ajax, 返回数据均按照ajax方式处理
    '''
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            pass
            
        return inner
    return decorator
