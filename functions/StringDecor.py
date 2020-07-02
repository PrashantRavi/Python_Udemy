

def decorfun(fun):
    def inner(n):
        result =fun(n)
        result+=" How are Youo"
        return result
    return inner

@decorfun
def hello(name):
    return "hello "+name

print(hello("Prashant"))