#coding:utf-8


from django.dispatch import receiver
from app_a import signals

@receiver(signals.my_signal_a, sender=, weak=True, dispatch_uid="")
def my_signal_a_handler(sender, arg_a, arg_b, arg_c):
    '''
    信号处理函数
    '''
    pass

#用connect方法绑定信号处理函数
signals.my_signal_a.connect(receiver=my_signal_a_handler, sender=, weak=True, dispatch_uid="")

    """
     |      Connect receiver to sender for signal.
     |
     |      Arguments:
     |
     |          receiver
     |              A function or an instance method which is to receive signals.
     |              Receivers must be hashable objects.
     |
     |              If weak is True, then receiver must be weak-referencable (more
     |              precisely saferef.safeRef() must be able to create a reference
     |              to the receiver).
     |
     |              Receivers must be able to accept keyword arguments.
     |
     |              If receivers have a dispatch_uid attribute, the receiver will
     |              not be added if another receiver already exists with that
     |              dispatch_uid.
     |
     |          sender
     |              The sender to which the receiver should respond. Must either be
     |              of type Signal, or None to receive events from any sender.
     |
     |          weak
     |              Whether to use weak references to the receiver. By default, the
     |              module will attempt to use weak references to the receiver
     |              objects. If this parameter is false, then strong references will
     |              be used.
     |
     |          dispatch_uid
     |              An identifier used to uniquely identify a particular instance of
     |              a receiver. This will usually be a string, though it may be
     |              anything hashable.
    """

#信号的发送
from app_a import signals.py

signals.my_signal_a.sender(sender= , arg_a=, arg_b=, arg_c=)

    """
     |      Send signal from sender to all connected receivers.
     |
     |      If any receiver raises an error, the error propagates back through send,
     |      terminating the dispatch loop, so it is quite possible to not have all
     |      receivers called if a raises an error.
     |
     |      Arguments:
     |
     |          sender
     |              The sender of the signal Either a specific object or None.
     |
     |          named
     |              Named arguments which will be passed to receivers.
     |
     |      Returns a list of tuple pairs [(receiver, response), ... ].
    """
