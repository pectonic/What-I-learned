def hello(end, start = 'Hello'):
    print(start + '' + end)

hello('Can', start='Cakal')
hello('Can')

def f(x,y=2,z=5):
    return x+y+z

print(f(2,y=8))