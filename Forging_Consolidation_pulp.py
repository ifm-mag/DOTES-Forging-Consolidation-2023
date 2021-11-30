#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Problem:
    Problem Nature: Pulp
    Library:
Created on August 12, 2021

@author: Dr. Vinod Kumar Chauhan, University of Cambridge

"""

import numpy as np
import time
from pulp import *

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

    # create model
    model = LpProblem(name='Forging_Consolidation', sense=LpMinimize)

    # define variable
    z_k = LpVariable.dicts("z_k", (range(NUM_FORGINGS)), cat="Binary")

    # define auxiliary variables
    # helps to calculate cost of part i
    v_i = LpVariable.dicts("v_i", (range(NUM_PARTS)), cat="Continuous")
    # indicator variable, which helps to find minimum cost forging k for part i
    x_ik = LpVariable.dicts("x_ik", (range(NUM_PARTS), range(NUM_FORGINGS)), cat="Binary")
    # 1 if forging k is purchased at discount level d, otherwise 0
    u_dk = LpVariable.dicts("u_dk", (range(len(Q_d_i)+1), range(NUM_FORGINGS)), cat="Binary")
    # used for linearisation
    Y_ikd = LpVariable.dicts("Y_ikd", (range(NUM_PARTS), range(NUM_FORGINGS), range(len(Q_d_i)+1)), cat="Binary")
    # used for linearisation
    W_ikd = LpVariable.dicts("W_ikd", (range(NUM_PARTS), range(NUM_FORGINGS), range(len(Q_d_i)+1)), cat="Binary")

    # add objective function: minimize the cost
    model += lpSum(CMF_i[i]+(1-D_i[i])*N_i[i]*v_i[i] for i in range(NUM_PARTS)) \
            + lpSum(CFH_k[k]*np.ceil(L_ik[i][k]*P_i[i])*x_ik[i][k] for i in range(NUM_PARTS) for k in range(NUM_FORGINGS))\
            + lpSum(z_k[k]*CFF_k[k]+lpSum((CFU_k[k]+CFT_k[k])*(1-D_k[d])*lpSum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*Y_ikd[i][k][d] for i in range(NUM_PARTS)) for d in range(len(D_k))) for k in range(NUM_FORGINGS))

    # constraints implementation
    # constraint: find min cost forgings for part
    for i in range(NUM_PARTS):
        for k in range(NUM_FORGINGS):
            model += v_i[i] - z_k[k]*(CMU_ik[i][k]+CMT_ik[i][k]) + M*(1-x_ik[i][k]) >= 0
            model += x_ik[i][k] - z_k[k]*(CMU_ik[i][k]+CMT_ik[i][k]) <= 0
    for i in range(NUM_PARTS):
        model += v_i[i] >= E
        model += lpSum(x_ik[i][k] for k in range(NUM_FORGINGS)) == 1

    # constraint: constraints related to economies of scale for forgings, i.e., discounts for forgings
    # only one discount offered
    for k in range(NUM_FORGINGS):
        model += lpSum(u_dk[d][k] for d in range(len(D_k))) == 1
    # For d = 0 and For d = D
    for k in range(NUM_FORGINGS):
        model += lpSum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*W_ikd[i][k][0] for i in range(NUM_PARTS)) <= Q_d_k[0]
        model += u_dk[len(D_k)-1][k]*Q_d_k[len(D_k)-2] - lpSum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*x_ik[i][k] for i in range(NUM_PARTS)) <= 0
    # For d = 1,2,...,D-1
    for k in range(NUM_FORGINGS):
        for d in range(1, len(D_k)-1):
            model += lpSum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*W_ikd[i][k][d] for i in range(NUM_PARTS)) <= Q_d_k[d]
            model += u_dk[d][k]*Q_d_k[d-1] - lpSum(np.ceil(L_ik[i][k]*(N_i[i]+P_i[i]))*x_ik[i][k] for i in range(NUM_PARTS)) <= 0

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
    # tolerance value

    # solve the model
    print('Solving the model...')
    # available solvers:
    # CPLEX_CMD','GUROBI', 'GUROBI_CMD', 'PULP_CBC_CMD', 'PULP_CHOCO_CMD','SCIP_CMD
    # path_to_cplex = "/Applications/CPLEX_Studio_Community129/cplex/bin/x86-64_osx/cplex"
    # solver = CPLEX_CMD(timeLimit=10, path=path_to_cplex)
    # solver = CPLEX_CMD(msg=0, path=path_to_cplex)
    solver = GUROBI(msg=0)
    # solver = CPLEX_CMD(msg=0)
    status = model.solve(solver=solver)

    # final solution
    Z = [z_k[k].varValue for k in range(NUM_FORGINGS)]
    Z = np.array(Z)
    V = np.array([v_i[i].varValue for i in range(NUM_PARTS)])
    U2 = np.array([[u_dk[d][k].varValue for k in range(NUM_FORGINGS)] for d in range(len(D_k))])
    X = np.array([[x_ik[i][k].varValue for k in range(NUM_FORGINGS)] for i in range(NUM_PARTS)])
    Y = np.array([[[Y_ikd[i][k][d].varValue for d in range(len(D_k))] for k in range(NUM_FORGINGS)] for i in range(NUM_PARTS)])
    # print('U:',U2)
    # print('S:', S)
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

    total_cost = value(model.objective)

    if status == LpStatusOptimal:
        print('Optimal cost found:', total_cost)
        # print('Number of solutions: ', model.num_solutions)
    else:
        print('OPTIMAL solution not found.\n\n')
        # print('Number of solutions: ', model.num_solutions)

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
    NUM_PARTS, NUM_FORGINGS = 10, 10
    Z, Cost_forging, Cost_holding, Cost_machining, data, N_f = forging_consolidation(NUM_PARTS, NUM_FORGINGS)

    print('\nProcurement costs with consolidation.\n################################')
    print('Forging cost:{:.0f}, \nMachining cost:{:.0f}, \nHolding cost:{:.0f}'.format(Cost_forging, Cost_machining, Cost_holding))
    print('Total Procurement cost:{:.0f}'.format(Cost_forging+Cost_holding+Cost_machining))
    # display non-consolidation results
    display_result(Z, data)
    print('################################ \nTotal time to solve (minutes):{:.4f}'.format((time.time()-start)/60))
