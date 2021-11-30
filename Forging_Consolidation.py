#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Problem:
    Problem Nature: MILP
    Library: Python MIP+CBC
Created on August 02, 2021
Last modified: September 24, 2021.

@author: Dr. Vinod Kumar Chauhan, University of Cambridge

"""

import numpy as np
import time
from mip import Model, xsum, minimize, BINARY, INTEGER, CONTINUOUS, OptimizationStatus

from data_gen import *
from auxiliary import *


def forging_consolidation(NUM_PARTS, NUM_FORGINGS):
    """
    Objective :
    -------
    Input :
    -------
    Output:
    -------

    """
    start = time.time()
    E = 1e-10
    M = 1e10
    # load data
    N_i, P_i, L_ik, CMF_i, CMU_ik, CMT_ik, CFH_k, CFF_k, CFU_k, CFT_k, Q_d_i, D_i, Q_d_k, D_k = generate_data(NUM_PARTS, NUM_FORGINGS)
    data = [N_i, P_i, L_ik, CMF_i, CMU_ik, CMT_ik, CFH_k, CFF_k, CFU_k, CFT_k, Q_d_i, D_i, Q_d_k, D_k]

    print('\nTotal number of parts:', NUM_PARTS, ' Total given forgings:', NUM_FORGINGS,'\n')
    print('Generating a model...')

    # Solver selection: solver_name='CBC' or solver_name='GRB'
    opt_solver='GRB'

    # create model
    model = Model(name='Forging_Consolidation', solver_name=opt_solver)

    # define variable
    z_k = [model.add_var(var_type=BINARY) for k in range(NUM_FORGINGS)]

    # define auxiliary variables
    # helps to calculate cost of part i
    v_i = [model.add_var(var_type=CONTINUOUS) for i in range(NUM_PARTS)]
    # indicator variable, which helps to find minimum cost forging k for part i
    x_ik = [[model.add_var(var_type=BINARY) for k in range(NUM_FORGINGS)] for i in range(NUM_PARTS)]
    # 1 if forging k is purchased at discount level d, otherwise 0
    u_dk = [[model.add_var(var_type=BINARY) for k in range(NUM_FORGINGS)] for d in range(len(Q_d_k)+1)]
    # used for linearisation
    Y_ikd = [[[model.add_var(var_type=BINARY) for d in range(len(Q_d_i)+1)] for k in range(NUM_FORGINGS)] for i in range(NUM_PARTS)]
    # used for linearisation
    W_ikd = [[[model.add_var(var_type=BINARY) for d in range(len(Q_d_i)+1)] for k in range(NUM_FORGINGS)] for i in range(NUM_PARTS)]

    # add objective function: minimize the cost
    model.objective = minimize(xsum(CMF_i[i]+v_i[i]*(1-D_i[i])*N_i[i] for i in range(NUM_PARTS)) \
                                + xsum(CFH_k[k]*np.ceil(L_ik[i][k]*P_i[i])*x_ik[i][k] for i in range(NUM_PARTS) for k in range(NUM_FORGINGS))\
                                + xsum(z_k[k]*CFF_k[k]+xsum((CFU_k[k]+CFT_k[k])*(1-D_k[d])*xsum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*Y_ikd[i][k][d] for i in range(NUM_PARTS)) for d in range(len(D_k))) for k in range(NUM_FORGINGS)))

    # constraints implementation
    # constraint: find min cost forgings for part
    for i in range(NUM_PARTS):
        for k in range(NUM_FORGINGS):
            model += v_i[i] - z_k[k]*(CMU_ik[i][k]+CMT_ik[i][k]) + M*(1-x_ik[i][k]) >= 0
            model += x_ik[i][k] - z_k[k]*(CMU_ik[i][k]+CMT_ik[i][k]) <= 0
    for i in range(NUM_PARTS):
        model += v_i[i] >= E
        model += xsum(x_ik[i][k] for k in range(NUM_FORGINGS)) == 1

    # constraint: constraints related to economies of scale for forgings, i.e., discounts for forgings
    # only one discount offered
    for k in range(NUM_FORGINGS):
        model += xsum(u_dk[d][k] for d in range(len(D_k))) == 1
    # For d = 0 and For d = D
    for k in range(NUM_FORGINGS):
        model += xsum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*W_ikd[i][k][0] for i in range(NUM_PARTS)) <= Q_d_k[0]
        model += u_dk[len(D_k)-1][k]*Q_d_k[len(D_k)-2] - xsum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*x_ik[i][k] for i in range(NUM_PARTS)) <= 0
    # For d = 1,2,...,D-1
    for k in range(NUM_FORGINGS):
        for d in range(1, len(D_k)-1):
            model += xsum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*W_ikd[i][k][d] for i in range(NUM_PARTS)) <= Q_d_k[d]
            model += u_dk[d][k]*Q_d_k[d-1] - xsum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*x_ik[i][k] for i in range(NUM_PARTS)) <= 0

    # linearisation constraints
    # Y_ikd
    for i in range(NUM_PARTS):
        for k in range(NUM_FORGINGS):
            for d in range(len(D_k)):
                model += Y_ikd[i][k][d] <= z_k[k]
                model += Y_ikd[i][k][d] <= x_ik[i][k]
                model += Y_ikd[i][k][d] <= u_dk[d][k]
                model += Y_ikd[i][k][d] - z_k[k] - x_ik[i][k] - u_dk[d][k] + 2 >= 0

    # W_ikd
    for i in range(NUM_PARTS):
        for k in range(NUM_FORGINGS):
            for d in range(len(D_k)):
                model += W_ikd[i][k][d] <= x_ik[i][k]
                model += W_ikd[i][k][d] <= u_dk[d][k]
                model += W_ikd[i][k][d] - x_ik[i][k] - u_dk[d][k] + 1 >= 0


    # set parameter values
    # property verbose: 0 to disable solver messages printed on the screen, 1 to enable
    model.verbose = 0
    # optimizing
    # # Performance Tuning parameters
    # # emphasis property. 0. default setting, 1. feasibility, 2. optimality
    # model.emphasis = 2 # focus on optimal solution not fast feasible

    # # Controls the generation of cutting planes, -1 means automatic, 0 disables
    # # completely, 1 (default) generates cutting planes in a moderate way, 2 generates cutting planes aggressively
    # # and 3 generates even more cutting planes
    # model.cuts = 0

    # # provide initial feasible solution for faster processing
    # model.start = [(x_ik[i][j], 1) if (j==0 or j==(num_of_machinist+1)) else (x_ik[i][j], 0) for j in range(num_of_machinist*2) for i in range(num_of_parts)]

    # # select lp_method: AUTO = 0, DUAL = 1, PRIMAL = 2, BARRIER = 3
    # model.lp_method = 3

    # tolerance value
    model.max_mip_gap = 1e-10

    # The NumericFocus parameter controls the degree to which the code attempts to detect and manage numerical issues.
    # Default value:	0 Minimum value:	0 Maximum value:	3
    # model.NumericFocus = 3

    # solve the model
    print('Solving the model...')
    status = model.optimize(max_seconds=float('inf'), max_nodes=float('inf'), max_solutions=float('inf'), relax=False)
    # status = model.optimize(max_seconds=1000)

    # final solution
    Z = np.array([z_k[k].x for k in range(NUM_FORGINGS)])
    V = np.array([v_i[i].x for i in range(NUM_PARTS)])
    U2 = np.array([[u_dk[d][k].x for k in range(NUM_FORGINGS)] for d in range(len(D_k))])
    X = np.array([[x_ik[i][k].x for k in range(NUM_FORGINGS)] for i in range(NUM_PARTS)])
    Y = np.array([[[Y_ikd[i][k][d].x for d in range(len(D_k))] for k in range(NUM_FORGINGS)] for i in range(NUM_PARTS)])
    # print('U:',U2)
    # print('S:', S)
    # print('V:', V)
    # number of forgings
    N_f = np.zeros((NUM_FORGINGS))
    for k in range(NUM_FORGINGS):
        N_f[k] = sum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*X[i][k] for i in range(NUM_PARTS))
    # print('Forging requirements:', N_f)

    # cacluate foring and machining costs.
    Cost_machining = sum(CMF_i[i]+(1-D_i[i])*N_i[i]*V[i] for i in range(NUM_PARTS))
    Cost_holding = sum(CFH_k[k]*np.ceil(L_ik[i][k]*P_i[i])*X[i][k] for i in range(NUM_PARTS) for k in range(NUM_FORGINGS))
    Cost_forging = sum(Z[k]*CFF_k[k]+sum((CFU_k[k]+CFT_k[k])*(1-D_k[d])*sum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*Y[i][k][d] for i in range(NUM_PARTS)) for d in range(len(D_k))) for k in range(NUM_FORGINGS))
    # print(Cost_forging, Cost_holding, Cost_machining,Cost_forging+Cost_holding+Cost_machining)

    total_cost = model.objective_value

    if status == OptimizationStatus.OPTIMAL:
        print('Optimal cost found:', total_cost)
        print('Number of solutions: ', model.num_solutions)
    else:
        print('OPTIMAL solution not found.\n\n')
        print('Number of solutions: ', model.num_solutions)

    # # # save the final model
    # # model.write('RR_FC.lp')

    # # with open('rr_oa_sol', 'wb') as f:
    # #     pickle.dump([XB, XL], f)
    # # vars = len(model.vars)
    print('Time to solve (minutes): ', (time.time()-start)/60)

    return Z, Cost_forging, Cost_holding, Cost_machining, data, N_f


if __name__ == "__main__":
    start = time.time()
    np.random.seed(123456789)
    random.seed(123456789)
    NUM_PARTS, NUM_FORGINGS = 15, 10
    Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)

    print('\nProcurement costs with consolidation.\n################################')
    print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
    print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
    # display non-consolidation results
    display_result(Z, data)
    print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
