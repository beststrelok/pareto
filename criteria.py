# -*- coding: utf-8 -*-
# python3

# import sys
# os.getcwd() 
# print(sys.version)
# sys.exit()

# gradient-animator.com
# http://thecodeplayer.com/walkthrough/animating-css3-gradients

# /*----------------------------------------------*/
# !!!! IMPORTANT
# import cmd
# import platform

# from pprint import pprint

import pylab
from colorama import init
from colorama import Fore, Back, Style
init() # run init to enable asci console to start coloring

def get_input():
    a = {}
    count = int(input("Type in the number of options: "))
    print('Type F1(x) and F2(x), for example "2,3":')
    for i in range(1, count+1):
        data = input('x'+str(i)+': ')
        a[i] = [int(x) for x in data.split(',')]
        a[i].extend(('+', '+', '+', '+'))
    return a

def pareto(a):
    # F1->max and F2->max
    for i in a:
        for j in a:
            if ((a[i][0] < a[j][0] and a[i][1] < a[j][1]) or (a[i][0] <= a[j][0] and a[i][1] < a[j][1]) or (a[i][0] < a[j][0] and a[i][1] <= a[j][1])):
                a[i][2] = Fore.RED+'-'.center(8)+Fore.RESET

    # F1->min and F2->min
    for i in a:
        for j in a:
            if ((a[i][0] > a[j][0] and a[i][1] > a[j][1]) or (a[i][0] >= a[j][0] and a[i][1] > a[j][1]) or (a[i][0] > a[j][0] and a[i][1] >= a[j][1])):
                a[i][3] = Fore.RED+'-'.center(8)+Fore.RESET

    # F1->max and F2->min
    for i in a:
        for j in a:
            if ((a[i][0] < a[j][0] and a[i][1] > a[j][1]) or (a[i][0] <= a[j][0] and a[i][1] > a[j][1]) or (a[i][0] < a[j][0] and a[i][1] >= a[j][1])):
                a[i][4] = Fore.RED+'-'.center(8)+Fore.RESET

    # F1->min and F2->max
    for i in a:
        for j in a:
            if ((a[i][0] > a[j][0] and a[i][1] < a[j][1]) or (a[i][0] >= a[j][0] and a[i][1] < a[j][1]) or (a[i][0] > a[j][0] and a[i][1] <= a[j][1])):
                a[i][5] = Fore.RED+'-'.center(8)+Fore.RESET
    return a

def render(a):
    print(Style.BRIGHT)
    print(Fore.CYAN)
    print('/--------------------------------------------------------------\\')
    print('|        |  F1(x) |  F2(x) | F1 max | F1 min | F1 max | F1 min |')
    print('|        |        |        | F2 max | F2 min | F2 min | F2 max |')
    print('|--------------------------------------------------------------|')
    for item in a:
        if (item > 1):
            print(Fore.CYAN+'|--------|--------|--------|--------|--------|--------|--------|'+Fore.RESET)
        print(Fore.CYAN+'|'+Fore.CYAN+('x'+str(item)).center(8)\
             +Fore.CYAN+'|'+Fore.YELLOW+str(a[item][0]).center(8)+Fore.RESET\
             +Fore.CYAN+'|'+Fore.YELLOW+str(a[item][1]).center(8)+Fore.RESET\
             +Fore.CYAN+'|'+Fore.GREEN+str(a[item][2]).center(8)+Fore.RESET\
             +Fore.CYAN+'|'+Fore.GREEN+str(a[item][3]).center(8)+Fore.RESET\
             +Fore.CYAN+'|'+Fore.GREEN+str(a[item][4]).center(8)+Fore.RESET\
             +Fore.CYAN+'|'+Fore.GREEN+str(a[item][5]).center(8)+Fore.RESET\
             +Fore.CYAN+'|')
    print('\--------------------------------------------------------------/')

def plot(a):
    # /*------------------------------------------------
    # | exclude non dominant points
    # ------------------------------------------------*/
    for i in range(1, len(a)+1):
        # {1: [2, 3, '+', '\x1b[31m   -    \x1b[39m', '+', '+'], 2: [1, 2, '\x1b[31m   -    \x1b[39m', '+', '+', '+']}
        if (a[i][2] != '+' and a[i][3] != '+' and a[i][4] != '+' and a[i][5] != '+'):
            del a[i];

    # /*------------------------------------------------
    # | RENDER PLOT
    # ------------------------------------------------*/
    b = a.values()
    x = [i[0] for i in b]
    y = [i[1] for i in b]

    pylab.plot(x, y, 'bs-')
    for i in range(0,len(b)):
        pylab.annotate('F(x{0})'.format(i+1), xy=(x[i], y[i]), xytext=(x[i]+.2, y[i]+.2))

    pylab.xticks(range(min(x)-1, max(x)+2))
    pylab.yticks(range(min(y)-1, max(y)+2))
    pylab.show()


# /*------------------------------------------------
# | RUN
# ------------------------------------------------*/
if __name__ == "__main__":
    a = get_input()
    a = pareto(a)
    render(a)
    plot(a)

    input('Press ENTER to exit...')
    print()

# a = {
#     1   : [11, 7, '+', '+', '+', '+'],
#     2   : [8, 5, '+', '+', '+', '+'],
#     3   : [7, 12, '+', '+', '+', '+'],
#     4   : [5, 6, '+', '+', '+', '+'],
#     5   : [3, 18, '+', '+', '+', '+'],
#     6   : [2, 11, '+', '+', '+', '+'],
#     7   : [9, 3, '+', '+', '+', '+'],
#     8   : [19, 4, '+', '+', '+', '+'],
#     9   : [5, 19, '+', '+', '+', '+'],
# }

# a = {
#     1   : [1, 6, '-', '-', '-', '-'],
#     2   : [2, 3, '-', '-', '-', '-'],
#     3   : [1, 3, '-', '+', '-', '-'],
#     4   : [5, 2, '+', '-', '-', '-'],
#     5   : [0, 6, '-', '+', '-', '+'],
#     6   : [5, 1, '-', '+', '+', '-'],
#     7   : [4, 2, '-', '+', '-', '-'],
#     8   : [2, 5, '-', '-', '-', '-'],
#     9   : [2, 6, '+', '-', '-', '-'],
#     10  : [1, 4, '-', '-', '-', '-'],
# }