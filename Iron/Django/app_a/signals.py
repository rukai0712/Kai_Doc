# coding: utf-8

from django.dispatch import Signal

my_signal_a = Signal(providing_args=["arg_a", "arg_b", "arg_c"])

#providing_args 定义receiver调用参数格式，为None也没关系


#Django内置信号
from django.db.models.signals import class_prepared, m2m_changed, post_delete, post_init, post_save, post_syncdb, pre_delete, pre_init, pre_save, pre_syncdb
    """
    django.db.models.signals的信号

    class_prepared = Signal(providing_args=["class"])
    #创建对象执行之前的信号
    pre_init = Signal(providing_args=["instance", "args", "kwargs"])
    #初始化之后的信号
    post_init = Signal(providing_args=["instance"])

    #save()执行之前的信号
    pre_save = Signal(providing_args=["instance", "raw", "using"])
    #save()执行之后的信号
    post_save = Signal(providing_args=["instance", "raw", "created", "using"])
    #delete()执行之前的信号
    pre_delete = Signal(providing_args=["instance", "using"])、
    #delete()执行之后的信号
    post_delete = Signal(providing_args=["instance", "using"])


    #ManyToManyField改变的时候发送此信号
    m2m_changed = Signal(providing_args=["action", "instance", "reverse", "model", "pk_set", "using"])
    #新版本废除，当调用orm同步的时候用
    post_syncdb = Signal(providing_args=["class", "app", "created_models", "verbosity", "interactive"])
    #高版本使用pre_migrate和post_migrate
    """

from django.core.signals import request_started, request_started, request_started
    """
    django.core.signals的信号

    #request请求开始前
    request_started = Signal()
    #request请求结束后
    request_finished = Signal()
    #处理request请求出现异常时
    got_request_exception = Signal(providing_args=["request"])
    """

from django.test.signals import template_rendered, setting_changed
    """
    django.test.signals的信号
    #模板渲染时发送的信号
    template_rendered = Signal(providing_args=["template", "context"])
    #setting改变时发送的信号
    setting_changed = Signal(providing_args=["setting", "value"])
    """

from django.db.backends.signals import connection_created
    """
    django.db.backends.signals的信号
    connection_created = Signal(providing_args=["connection"])
    """
