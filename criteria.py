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

def _remove_non_dominant(a):
    for i in range(1, len(a)+1):
        # {1: [2, 3, '+', '\x1b[31m   -    \x1b[39m', '+', '+'], 2: [1, 2, '\x1b[31m   -    \x1b[39m', '+', '+', '+']}
        if (a[i][2] != '+' and a[i][3] != '+' and a[i][4] != '+' and a[i][5] != '+'):
            del a[i];
    return a

def _remove_not_unique(a):
    b = list(a.values())
    unique = []
    [unique.append(item) for item in b if item not in unique]
    return unique

def ___distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**.5

def __draw_quantile(graph):
    to_draw = []

    print('graph---')
    print(graph)
    closest = [999999999, graph[0][0], graph[0][1]]

    for i in range(0, len(graph)):
        if (len(graph) > 1): # 3
            x = [i[0] for i in graph] # [2,3,0]
            y = [i[1] for i in graph] # [3,1,2]
            for i in range(0, len(graph)-1):
                dist = ___distance(closest[1], closest[2], x[i+1], y[i+1]) # 5**.5
                print(dist)
                if (dist < closest[0]):
                    closest[0] = dist # 5**.5
                    closest[1] = x[i+1] # 3
                    closest[2] = y[i+1] # 1
            to_draw.append(closest)
            del graph[0];

    y = [i[2] for i in to_draw] 
    x = [i[1] for i in to_draw]
    print('----====')
    print(to_draw)
    print('====----')
    pylab.plot(x, y, '-')
    print('end quantile')

def _add_points_and_annotate(unique):
    x_all = [i[0] for i in unique]
    y_all = [i[1] for i in unique]
    pylab.plot(x_all, y_all, 'bs')
    for i in range(0,len(unique)):
        pylab.annotate('F(x{0})'.format(i+1), xy=(x_all[i], y_all[i]), xytext=(x_all[i]+.2, y_all[i]+.2))

def _add_lines(unique):
    for j in range(2, 6):
        graph = []
        for i in range(0, len(unique)):
            if (unique[i][j] == '+'):
                graph.append([unique[i][0], unique[i][1]])
        __draw_quantile(graph)

def _add_ticks(unique):
    x_all = [i[0] for i in unique]
    y_all = [i[1] for i in unique]
    pylab.xticks(range(min(x_all)-1, max(x_all)+2))
    pylab.yticks(range(min(y_all)-1, max(y_all)+2))

def plot(a):
    a = _remove_non_dominant(a)
    unique = _remove_not_unique(a)
    _add_points_and_annotate(unique)
    _add_lines(unique)
    _add_ticks(unique)
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