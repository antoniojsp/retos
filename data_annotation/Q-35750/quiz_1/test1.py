def foo(i, x=[]):
    x.append(i)
    return x

for i in range(3):

    print(foo(i))

def foo(i, x=None):  # Notice x=None
    if x is None:
        x = []
    x.append(i)
    return x

for i in range(3):
    print(foo(i))