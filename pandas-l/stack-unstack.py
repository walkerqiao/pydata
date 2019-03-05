#!/usr/bin/env python
# coding=utf-8

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

data = DataFrame(np.arange(6).reshape((2,3)),
        index=pd.Index(['street1','street2']),
        columns=pd.Index(['one','two','three']))

print("DataFrame:=================")
print(data)

print('stack DataFrame: ----------------')
data2 = data.stack()
print(data2)

print('unstack data -----------')
data3 = data2.unstack()
print(data3)
