def myf():
    yield "Hello"
    yield "50"
    yield "Bye"

def myf2():
    yield "Hello"
    yield "50"
    return "Bye"

x = myf()
for z in x:
    print(z)

y = myf2()
for z in y:
    print(z)