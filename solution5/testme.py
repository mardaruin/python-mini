from specialized import specialize


def sum(x, y):
    return x+y


asdf = specialize(sum, y=1)
vall = asdf(2)

ert = specialize(sum, 1, 1)
val2 = ert()

print(vall, val2)