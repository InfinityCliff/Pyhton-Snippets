import inspect

''' You can use the inspect module to get the calling stack. It returns a list of frame records. The third element in 
each record is the caller name. What you want is this: 
'''


def f():
    print(inspect.stack()[1][3])


def g():
    f()

g()
