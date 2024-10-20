def specialize(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)  # line to change
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc