def escape(x):
    return '\x1b[38;5;{}m'.format(x)

def reset():
    return '\x1b[0m'

def color(id, s):
    return escape(id) + s + reset()


#for i in range(0, 256):
#    print(color(i, str(i)))
