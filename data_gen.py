#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on

@author: vinodkumar
"""
import numpy as np
import pandas as pd
import pickle
import random

def generate_data(m, n):
    # # Total number of unique parts
    # m = 5
    # # Total number of unique forgings
    # n = 5
    # Number of parts ordered
    N_i = np.random.randint(low=100,high=500, size=(m,))
    # Inventory of parts
    P_i = np.random.randint(low=10,high=50, size=(m,))
    # number of forgings k needed to manufacture one unit part i
    L_ik = 1.0 / np.random.randint(low=1, high=4, size=(m,n))

    # CFHk per unit holding cost for forging k
    CFH_k = np.random.randint(low=15,high=40, size=(n,))
    # # effect of holding cost
    # CFH_k = CFH_k*5
    # Fixed ordering cost associated with forging k
    CFF_k = np.random.randint(low=1000,high=5000, size=(n,))
    # # effect of fixed cost
    # CFF_k = CFF_k*5
    # CFUk per unit cost associated with forging k
    CFU_k = np.random.randint(low=10,high=40, size=(n,))
    # CFTk per unit transportation for forging k
    CFT_k = np.random.randint(low=5,high=25, size=(n,))

    # Fixed ordering cost associated with part i
    CMF_i = np.random.randint(low=1000,high=5000, size=(m,))
    # CMUik per unit machining cost of part i from forging k
    CMU_ik = np.random.randint(low=10, high=40, size=(m,n))
    # CMTik per unit transportation cost of part i manufactured from forging k
    CMT_ik = np.random.randint(low=1, high=5, size=(m,n))

    # make sure all the forgings are used once.
    # create indexes to cover all forgings.
    if n<=m:
        all_forgings = np.random.permutation(n)
        rem = random.sample(range(n), m-n)
        all_forgings = np.concatenate((all_forgings, rem))
    else:
        all_forgings = random.sample(range(n), m)

    # make the data sparse
    # note: if machining cost is 0 then transportation cost has to be 0.
    for i in range(m):
        # up to two options
        indexes = range(n)
        if np.random.rand() >= 0.5:
            indexes = np.delete(indexes, np.random.randint(n))
        # # more than two options
        # num_0 = np.random.randint(low=n-2, high=n)
        # indexes = random.sample(range(n), num_0)
        # # print(num_0, indexes)

        if all_forgings[i] in indexes:
            ind = np.argwhere(indexes==all_forgings[i])
            indexes = np.delete(indexes, ind)
        CMU_ik[i,indexes] = 0
        CMT_ik[i,indexes] = 0
        # print(CMU_ik[i,:])

    # Quantity interval for discount level d of part i
    Q_d_i = [250, 400]
    # Discount levels for parts
    D_d_i = [0, 0.05, 0.10]
    # D_i = [0, 0.15, 0.25]
    # Quantity interval for discount level d of forging k
    Q_d_k = [250, 400]
    # Discount levels for forgings
    D_k = [0, 0.05, 0.10]
    # D_k = [0, 0.0, 0.0]

    # pre-compute discounts for part order
    D_i = np.zeros(m)
    for i in range(m):
        if N_i[i] <= Q_d_i[0]:
            D_i[i] = D_d_i[0]
        elif N_i[i] <= Q_d_i[1]:
            D_i[i] = D_d_i[1]
        else:
            D_i[i] = D_d_i[2]

    return N_i, P_i, L_ik, CMF_i, CMU_ik, CMT_ik, CFH_k, CFF_k, CFU_k, CFT_k, Q_d_i, D_i, Q_d_k, D_k

# _ = generate_data()
