import time

def execTime(func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        print("ExecTime ({}): {}".format(func.__name__, time.time() - t1))

    return wrapper

def pprint(list_, size=4):
    if len(list_) < size * 2:
        print(", ".join(str(x) for x in list_))
    else:
        print("List: ", end="")
        print(", ".join(str(x) for x in list_[:size]), end="")
        print(", ..., " if len(list_) > (size * 2) else ", ", end="")
        print(", ".join(str(x) for x in list_[-size:]))
    