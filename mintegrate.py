# Python function for integration of *m*easurements
# S. Hafner

import numpy as np

def mintegrate(x, y, method = 'midpoint', lwr = float('nan'), upr = float('nan'), ylwr = 0, value = 'all'):

    if lwr != lwr:
        lwr = min(x)
    if upr != upr:
        upr = max(x)

    method = method[0]

    if (method == 'l'): 
        aaa = np.cumsum(y * np.diff(np.append(lwr, x)))
    elif (method == 'r'): 
        aaa = np.cumsum(y * np.diff(np.append(x, upr)))
    elif (method == 'm' or method == 't'):
        aaa = np.cumsum(np.append(0, y[:(len(y) - 1)] * np.diff(x)) / 2 + y * np.diff(np.append(lwr, x)) / 2) 
    elif (method == 't'):
        x = np.append(lwr, x)
        y = np.append(ylwr, y)
        aaa = np.cumsum((y[:(len(x) - 1)] + np.diff(y) / 2) * np.diff(x)) 
    else:
        sys.exit('The "method" argument is not recognized.')


    if value == 'all':
        return aaa
    elif value == 'total':
        return list(aaa)[-1]
    else:
        sys.exit('The "value" argument is not recognized. Use "all" to get cumulative results or else "total".')
