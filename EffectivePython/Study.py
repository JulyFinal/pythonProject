
def di(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("error inputs")
di(0,0)

def index(text):
    if text:
        yield 0
    for i,letter in enumerate(text):
        if letter == ' ':
            yield i + 1