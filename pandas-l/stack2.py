#!/usr/bin/env python
# coding=utf-8

import pandas as pd

df = pd.read_csv("nba.csv")

df_stacked = df.stack()

print(df_stacked.head(26))

df_melt = df.melt(id_vars = ['Name', 'Team'])

print(df_melt.head(20))
