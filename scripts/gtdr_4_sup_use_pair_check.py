# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 18:40:21 2023

@author: Horsting

GTDR: Assignment 4 - Supply but no use? And vice versa.

"""
#%% import packages & function file
import pandas as pd
import numpy as np

import gtdr_functions as functions

#%% Import files
table_30 = "OECD_Data_downloads\Table_30.xlsx"  # supply
table_43 = "OECD_Data_downloads\Table_43.xlsx"  # use

# table 43
# import
t_43 = functions.excel_df(table_43, 43, 3)
# drop total columns/rows
t_43_wo_totals = functions.drop_int_totals(t_43, 43, 1)
# slice transactions
t_43_transactions = t_43_wo_totals.iloc[:,0:65]
# t43_total_inputs = t_43_wo_totals.iloc[:,0:65].sum()

# table 30
# import
t_30 = functions.excel_df(table_30, 30, 3)
# drop total columns/rows
t_30_wo_totals = functions.drop_int_totals(t_30, 30, 2)    # fault in code: probably need to change the levels when 
# dropping the intermediate totals

# slice transactions
t_30_transactions = t_30_wo_totals.iloc[:,0:65]
# t43_total_outputs = t_43_wo_totals.iloc[:,0:65].sum()

#%% Check supply-use pairs

t_30_zeros = t_30_transactions[t_30_transactions == 0].notna()  # mask zeros as True, nonzeros False
t_43_zeros = t_43_transactions[t_43_transactions == 0].notna()

# t_30_zeros = t_30_transactions[t_30_transactions == 0]    # masks nonzeros as nans. Nans give difficulty in further comparison
# t_43_zeros = t_43_transactions[t_43_transactions == 0]

# equality_check = t_30_zeros.compare(t_43_zeros)     # does not work because col labels are not the same.
t_43_zeros.columns = t_30_zeros.columns     # making equal columns index, now for 43 does not hold, but only the P2 turned into P1 in the names

t_30_43_comp = t_30_zeros[t_30_zeros == t_43_zeros]  # masking matching Trues 'True', Falses 'False', and non-matches 'nan'
                                                # non-matches are zeros that match a nonzero entry in the other df
t_30_43_discrepancies = t_30_43_comp[t_30_43_comp != np.nan].notna() # non-zero matches are masked as False. True or False masked as True
# t_30_43_2 = t_30_43[t_30_43 == np.nan].notna()  # does not work: everything masked as False

# create dict of the zero-nonzero matches found in t_30_43_1