import functools

def deprecated(func=None, *, since=None, will_be_removed=None):
    def decorator(_func):
        func_name = _func.__name__

        @functools.wraps(_func)
        def inner(*args, **kwargs):
            message = f"Warning: function '{func_name}' is deprecated"
            if since and will_be_removed:
                message += f" since version {since}.\nIt will be removed in version {will_be_removed}."
            elif since:
                message += f" since version {since}.\nIt will be removed in future versions."
            elif will_be_removed:
                message += f".\nIt will be removed in version {will_be_removed}."
            else:
                message += f".\nIt will be removed."

            print(message)
            return _func(*args, **kwargs)

        return inner

    if func is None:
        return decorator
    else:
        return decorator(func)

@deprecated
def foo():
    print("Name 'foo' is just so basic :( Well, i have an idea ;)\n")

@deprecated(since='ugabuga')
def bebebe():
    print("I'm a rock star\n")

@deprecated(will_be_removed='i forgot which')
def vot_bi_bilo_ege_po_smeshnim_nazvaniaym_funkcii():
    for i in range(10):
        print("<3 " * (i + 1))
    print("Oh my god, there is so many...\n")

@deprecated(since='pu', will_be_removed=1.0)
def ok_lets_be_serious():
    print("Ha-ha, didn't expect that?)\n")

@deprecated
def bar(x, y):
    return x + y

bebebe()
vot_bi_bilo_ege_po_smeshnim_nazvaniaym_funkcii()
ok_lets_be_serious()
foo()
print(bar(4, y=6))