#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on

@author:
"""
import numpy as np

from data_gen import *

def display_result(Z, data):
    forgings = [ 'F_'+str(i+1) for i in range(Z.shape[0])]
    forgings = np.array(forgings)
    print('################################')
    # print('\nSelected Forgings:',len(Z.nonzero()[0]),'/',Z.shape[0], ' \n', forgings[Z==1])
    print('\nSelected Forgings:',len(Z.nonzero()[0]),'/',Z.shape[0])
    Cost_forging, Cost_holding, Cost_machining = without_FC(data)
    print('\nProcurement costs without consolidation.\n################################')
    print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
    print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))


def without_FC(data):
    N_i, P_i, L_ik, CMF_i, CMU_ik, CMT_ik, CFH_k, CFF_k, CFU_k, CFT_k, Q_d_i, D_i, Q_d_k, D_k = data
    NUM_PARTS, NUM_FORGINGS = CMU_ik.shape

    # find discounts for parts.
    # consider only main order not Inventory because we need to keep forgings only for the
    # Inventory but not supposed to cost machining.
    d_i = np.zeros(NUM_PARTS)
    for i in range(NUM_PARTS):
        if N_i[i] <= Q_d_i[0]:
            d_i[i] = D_i[0]
        elif N_i[i] <= Q_d_i[1]:
            d_i[i] = D_i[1]
        else:
            d_i[i] = D_i[2]

    # find forgings with minimum cost (>0) for each part
    min_forging_index_i = np.zeros(NUM_PARTS, dtype=int)
    min_forging_cost_i = np.zeros(NUM_PARTS)
    for i in range(NUM_PARTS):
        theta = (CMU_ik[i,:] + CMT_ik[i,:]) * (1.0 - d_i[i]) * N_i[i]
        min_forging_index_i[i] = np.where(theta==np.min(theta[np.nonzero(theta)]))[0][0]
        # print(min_forging_index_i[i])
        min_forging_cost_i[i] = CMU_ik[i,min_forging_index_i[i]] + CMT_ik[i,min_forging_index_i[i]]

    # calcuate number of forgings
    N_f = np.zeros((NUM_FORGINGS))
    for k in range(NUM_FORGINGS):
        N_f[k] = sum([np.ceil(L_ik[i][k]*(N_i[i]+P_i[i])) for i, val in enumerate(min_forging_index_i)  if k==val])

    # print('Forging requirements without consolidation:\n', N_f)
    # calcuate number of forgings for holding
    N_fh = np.zeros((NUM_FORGINGS))
    for k in range(NUM_FORGINGS):
        N_fh[k] = sum([np.ceil(L_ik[i][k]*(P_i[i])) for i, val in enumerate(min_forging_index_i)  if k==val])

    d_k = np.zeros((NUM_FORGINGS,))
    for k in range(NUM_FORGINGS):
        if N_f[k] <= Q_d_k[0]:
            d_k[k] = D_k[0]
        elif N_f[k] <= Q_d_k[1]:
            d_k[k] = D_k[1]
        else:
            d_k[k] = D_k[2]
    # print('d_k:', d_k)
    # cacluate foring and machining costs.
    Cost_machining = sum(CMF_i[i]+(1-d_i[i])*N_i[i]*min_forging_cost_i[i] for i in range(NUM_PARTS))
    Cost_holding = sum(CFH_k[k]*N_fh[k] for k in range(NUM_FORGINGS))
    Cost_forging = sum(CFF_k[k]+(CFU_k[k]+CFT_k[k])*(1-d_k[k])*N_f[k] for k in range(NUM_FORGINGS))

    return Cost_forging, Cost_holding, Cost_machining
