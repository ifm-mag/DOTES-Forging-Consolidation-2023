#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Problem: PCB assembly planning - PCBs allocation to lines and sequencing
    Problem Nature: MILP
    Library: ortools
Created on August 02, 2021

@author: Dr. Vinod Kumar Chauhan, University of Cambridge

"""

import numpy as np
import time
from ortools.linear_solver import pywraplp

from data_gen import *
from print_results import *


def PCBs_allocation_sequencing():
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
    C_pl, B_p, S_pql = generate_data()
    data = [C_pl, B_p, S_pql]
    # total PCBs, lines
    P, L = C_pl.shape

    print('Total PCBs:', P, ' Total assembly lines:', L,'\n')
    print('Generating a model...')

    # create model
    # Create the mip solver with the SCIP backend.
    model = pywraplp.Solver.CreateSolver('SCIP')
    infinity = model.infinity()

    # define variable
    # x: 1 if and only if PCB p is produced after PCB q on line l. (considers dummy PCB as predecessor if a
    # PCB is produced first))
    x = [[[model.BoolVar('x_%i_%i_%i' % (p, q, l)) for l in range(L)] for q in range(P+1)] for p in range(P)]

    # Miller, Tucker, Zemlin method to implement subtour elimination
    z = [[model.NumVar(0, infinity, 'z_%i_%i' % (p,l)) for l in range(L)] for p in range(P)]

    # y: represent the delivery made at customer i by the p-th vehicle of type k origination from depot d.
    tau = model.NumVar(0, infinity, 'tau')

    print('Number of variables =', model.NumVariables())

    # Add objective function: minimize the cost
    model.Minimize(tau)

    # constraints implementation
    # constraint: find bottleneck line to calculate makespan time
    for l in range(L):
        model.Add(tau - sum(x[p][q][l]*(B_p[p]*C_pl[p,l] + S_pql[p,q,l]) for p in range(P) for q in range(P+1)) >= 0)

    # constraint: each PCB should be manufactured at one line only.
    for p in range(P):
        model.Add(sum(x[p][q][l] for l in range(L) for q in range(P+1)) == 1)

    # constraint: if p is manufactured after q on line l then q should also be manufactured on
    # line l (except the dummy PCB).
    for l in range(L):
        for p in range(P):
            for q in range(P):
                model.Add(x[p][q][l] - sum(x[q][q1][l] for q1 in range(P+1)) <= 0)

    # constraint: there is only one predecessor and successor PCB.
    for l in range(L):
        for p in range(P):
            for q in range(P+1):
                model.Add(sum(x[p][q1][l] for q1 in range(P+1)) - x[p][q][l] - (1 - x[p][q][l])*M <= 0)
                model.Add(sum(x[p1][q][l] for p1 in range(P)) - x[p][q][l] - (1 - x[p][q][l])*M <= 0)

    # each line should start at dummy PCB.
    for l in range(L):
        model.Add(sum(x[p][P][l] for p in range(P)) == 1)

    # PCB p can not be produced after itself
    for l in range(L):
        for p in range(P):
            model.Add(x[p][p][l] == 0)

    # # constraint: the sub-tour elimination
    # # MTZ method
    for p1 in range(P):
        for p2 in range(P):
            for l in range(L):
                model.Add(z[p1][l] - z[p2][l] + P - (P+1)*x[p2][p1][l] >= 0)


    # set parameter values
    # property verbose: 0 to disable solver messages printed on the screen, 1 to enable
    # model.verbose = 1
    # optimizing
    # # Performance Tuning parameters
    # # emphasis property. 0. default setting, 1. feasibility, 2. optimality
    # model.emphasis = 2 # focus on optimal solution not fast feasible

    # # Controls the generation of cutting planes, -1 means automatic, 0 disables
    # # completely, 1 (default) generates cutting planes in a moderate way, 2 generates cutting planes aggressively
    # # and 3 generates even more cutting planes
    # model.cuts = 0

    # # provide initial feasible solution for faster processing
    # model.start = [(x[i][j], 1) if (j==0 or j==(num_of_machinist+1)) else (x[i][j], 0) for j in range(num_of_machinist*2) for i in range(num_of_parts)]

    # # select lp_method: AUTO = 0, DUAL = 1, PRIMAL = 2, BARRIER = 3
    # model.lp_method = 3

    # tolerance value
    # model.max_mip_gap = 1e-10

    # The NumericFocus parameter controls the degree to which the code attempts to detect and manage numerical issues.
    # Default value:	0 Minimum value:	0 Maximum value:	3
    # model.NumericFocus = 3

    # solve the model
    print('Solving the model...')
    status = model.Solve()
    # status = model.optimize(max_seconds=1000)

    # final solution
    X = [[[x[p][q][l].solution_value() for l in range(L)] for q in range(P+1)] for p in range(P)]
    X = np.array(X)

    total_cost = model.Objective().Value()

    if status == pywraplp.Solver.OPTIMAL:
        print('Optimal cost found:', total_cost)
        print('Number of solutions: ', model.NumVariables())
    else:
        print('OPTIMAL solution not found.\n\n')
        print('Number of solutions: ', model.NumVariables())

    # # # save the final model
    # # model.write('RR_FC.lp')

    # # with open('rr_oa_sol', 'wb') as f:
    # #     pickle.dump([XB, XL], f)
    # # vars = len(model.vars)
    print('Time to solve (minutes): ', (time.time()-start)/60)

    return X, total_cost, data

if __name__ == "__main__":
    start = time.time()
    np.random.seed(123456789)
    X, total_cost, data = PCBs_allocation_sequencing()
    # display results
    display_result(X, data)
    print('\n\nTotal time of production (minutes):', total_cost)
    print('Total time to solve (minutes): ', (time.time()-start)/60)
