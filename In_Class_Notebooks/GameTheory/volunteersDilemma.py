# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:39:22 2018

@author: shawla
"""

import sys
import matplotlib.pyplot as pyplot


def main(script, *argv):
    cvals = [0.01, 0.3, 0.9]
    avals = [0.95, 0.99, 1.0] #note that this needs to be raised to the Nth pow
    clen = len(cvals)
    alen = len(avals)
    out = []
    r = 0
    for i in range(clen):
        out.append([])
        for j in range(alen):
            out[i].append([])
    for N in range(2, 100):
        for i in range(clen):
            for j in range(alen):
                c = cvals[i]
                a = avals[j] ** N
                gammaN = (c / (a * (1 + r * (N - 1)))) ** (N / (N - 1.0))
                if gammaN <= 1.0: out[i][j].append(gammaN)
                else: out[i][j].append(1.0)

    ns = range(2, 100)
    i = 2
    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    for j in range(clen):
        a = str(avals[j])
        c = str(cvals[i])
        ax.plot(ns, out[i][j], linewidth = 5)
        #pyplot.plot(ns, out[i][j], linewidth = 5)

    title = 'The prob. nobody volunteers for increasing group sizes, with c'
    pyplot.title(title+c)
    pyplot.xlabel('N (group size)')
    pyplot.ylabel('gamma (prob. nobody volunteers)')
    leg = pyplot.legend(('a = 0.95', 'a = 0.99', 'a = 1.0'), 'upper right' )
    #leg = ax.legend(('a = 0.95', 'a = 0.99', 'a = 1.0'), 'upper right' )
    pyplot.ylim(ymax=1.01)
    pyplot.show()
    return

if __name__ == '__main__':
    import sys
    main(*sys.argv)