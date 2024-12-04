import functools

def deprecated(since=None, will_be_removed=None):
    def decorator(func):
        func_name = func.__name__

        @functools.wraps(func)
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
            return func(*args, **kwargs)

        return inner

    return decorator

@deprecated()
def foo():
    print("Name 'foo' is just so basic :( Well, i have an idea ;)\n")

@deprecated(since = 'ugabuga')
def bebebe():
    print("Im a rock star\n")

@deprecated()
def vot_bi_bilo_ege_po_smeshnim_nazvaniaym_funkcii(will_be_removed = 'i forgot which'):
    for i in range(10):
        print("<3 " * (i + 1))
    print("Oh my god, there is so many...\n")

@deprecated(since = 2.0, will_be_removed = 1.0)
def ok_lets_be_serious():
    print("Ha-ha, didnt expect that?)\n")

@deprecated()
def bar(x, y):
    return x+y

foo()
bebebe()
vot_bi_bilo_ege_po_smeshnim_nazvaniaym_funkcii()
ok_lets_be_serious()
print(bar(4, y=6))