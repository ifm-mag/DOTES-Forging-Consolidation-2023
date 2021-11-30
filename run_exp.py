#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 06:41:56 2021

@author: vinodkumar
"""
import time
import numpy as np
from Forging_Consolidation import *

# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 5, 5
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 10, 5
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 10, 10
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 15, 10
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 20, 15
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 25, 20
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 45, 25
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 70, 50
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 100, 70
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 100, 100
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 200, 150
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 200, 200
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 500, 250
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 500, 500
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))

# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 1000, 700
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))

# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 1000, 1000
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))

# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 1500, 1000
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# # display results
# display_result(Z, data)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))


# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 1500, 1500
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))


# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 2000, 1800
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))


# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 2000, 2000
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))


# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 3000, 2500
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))

start = time.time()
np.random.seed(123456789)
random.seed(123456789)
NUM_PARTS, NUM_FORGINGS = 3000, 3000
Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
print('\nProcurement costs with consolidation.\n################################')
print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# display non-consolidation results
display_result(Z, data)
print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))

start = time.time()
np.random.seed(123456789)
random.seed(123456789)
NUM_PARTS, NUM_FORGINGS = 4000, 4000
Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
print('\nProcurement costs with consolidation.\n################################')
print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# display non-consolidation results
display_result(Z, data)
print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
#
# start = time.time()
# np.random.seed(123456789)
# random.seed(123456789)
# NUM_PARTS, NUM_FORGINGS = 10000, 10000
# Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)
# print('\nProcurement costs with consolidation.\n################################')
# print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
# print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
# # display non-consolidation results
# display_result(Z, data)
# print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
