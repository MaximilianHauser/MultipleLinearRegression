# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:20:35 2022

@author: Maximilian
"""

# import section ------------------------------------------------------------ #
import numpy as np
import pandas as pd

# variables as lists -------------------------------------------------------- #

# regular explaining variables ---------------------------------------------- #
x_1 = [np.random.normal(loc=0, scale=1) for x in list(range(0,1000))]
x_2 = [np.random.normal(loc=0, scale=1) for x in list(range(0,1000))]

# variables that have no (intended) correlation with y ---------------------- #
decoy_1 = [np.random.normal(loc=0, scale=1) for x in list(range(0,1000))]
decoy_2 = [np.random.normal(loc=0, scale=1) for x in list(range(0,1000))]

# explaining variables, that are correlated with x_1 and x_5 ---------------- #
corr_1 = [x - 2500 for x in x_1]
corr_2 = [x + 2500 for x in x_2]

# explaining variable that is highly heteroscedastic ------------------------ #
inc_v = sorted([np.random.normal(loc=0, scale=1) for x in list(range(0,1000))])

# dict with values so far to convert to DataFrame --------------------------- #
dct = {"X_1":x_1, "X_2":x_2, "D_1":decoy_1, "D_2":decoy_2, "C_1":corr_1, "C_2":corr_2, "I_V":inc_v}

# to pandas DataFrame ------------------------------------------------------- #
df = pd.DataFrame(dct)

# calculating the dependent variable based on the independent variables ----- #
df["Y"] = (df["X_1"] + df["X_2"] + df["C_1"] + df["C_2"] + df["I_V"]) / 5

# adding residuals as random interference weighted by actual value ---------- #
columns_lst = list(df.columns)
     
# save generated table to csv-file ------------------------------------------ #
df.to_csv(path_or_buf="lin.csv", index=False)
