def div():
    if nr_2==0:
        return('nr_2=0 !!!')
    return nr_1/nr_2

def mult():
    return nr_1*nr_2

def dif():
    return nr_1-nr_2

def sum():
    return nr_1+nr_2

def all():
    d_1={
        "multiply":mult(),
        "sum":sum(),
        "division":div(),
        "diference":dif(),
    }
    return d_1
   
def change():
    global nr_1
    global nr_2
    nr_1=float(input('nr_1: '))
    nr_2=float(input('nr_2: '))
    print(f'The numbs have changed')

nr_1=float(input('nr_1: '))
nr_2=float(input('nr_2: '))
cmd=input("cmd:")

d={
    'multiply':mult,
    'sum':sum,
    'diference':dif,
    'division':div,
    'all':all,
}

while cmd:
    if cmd in d:
        rezultat=d[cmd]
        print(rezultat())
    elif cmd=='change':
        change()
    elif cmd=='quit':
        print('Thank you for using this program!')
        break
    else:
        print('Comand is unknown please enter a valid one')
    cmd=input('cmd: ')