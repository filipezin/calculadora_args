def soma(*args):
    return sum(args)

def subtracao(*args):
    if len(args) > 2:
        x = args[0]
        for i in args[1:]:
            x -= i
        return x
    return args[0] - args[1]

def mult(*args):
    x = 1
    for i in args:
        x *= i
    return x

def div(*args):
    if len(args) > 2: 
        x = args[0]
        for i in args[1:]:
            x /= i
        return x
    return args[0] / args[1]

def exp(*args):
    if len(args) > 2:
        x = args[0]
        for i in args[1:]:
            x = x ** i
        return x
    return args[0] ** args[1]

print(soma(1,2,3,4,5))
print(subtracao(100,5,3))
print(mult(1,3,5,7,9))
print(div(1000,10,10))
print(exp(10,2,2))
