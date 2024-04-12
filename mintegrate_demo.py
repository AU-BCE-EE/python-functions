# Demo/test of mintegrate function

import numpy as np
import pandas as pd

from mintegrate import mintegrate

#dat = pd.DataFrame({'time': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'rate': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
dat = pd.DataFrame({'time': range(1, 11), 'rate': range(1, 11)})

mintegrate(x = dat['time'], y = dat['rate'], method = 'm')
mintegrate(x = dat['time'], y = dat['rate'], method = 't')
mintegrate(x = dat['time'], y = dat['rate'], method = 'l')
mintegrate(x = dat['time'], y = dat['rate'], method = 'r')

mintegrate(x = dat['time'], y = dat['rate'], method = 'm', lwr = 0)
mintegrate(x = dat['time'], y = dat['rate'], method = 't', lwr = 0)
mintegrate(x = dat['time'], y = dat['rate'], method = 'l', lwr = 0)
mintegrate(x = dat['time'], y = dat['rate'], method = 'r', lwr = 0)

# Nonlinear
x = np.array(range(1, 10))
y = np.exp(-x)

mintegrate(x = x, y = y, method = 'm', value = 'total')
mintegrate(x = x, y = y, method = 't', value = 'total')
mintegrate(x = x, y = y, method = 'l', value = 'total')
mintegrate(x = x, y = y, method = 'r', value = 'total')


