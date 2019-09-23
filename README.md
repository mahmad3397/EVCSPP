# EVCSPP
This is a paper implementation of IEEE TRANSACTIONS ON SMART GRID, VOL. 5, NO. 6, NOVEMBER 2014 on Electric Vehicle Charging Station Placement: Formulation, Complexity, and Solutions published by Albert Y.S. Lam, Member, IEEE, Yiu-Wing Leung, Senior Member, IEEE, and Xiaowen Chu, Senior Member, IEEE.

This is done using Cplex Optimizer in Python API as well as using Greedy Algorithm.

Problem Explanation:
Here, n numbers of nodes(N) are given which denote the possible sites for constructing the charging stations. We need to find a subset of N such that:
1. cost of construction should be minimum
2. drivers can easily recharge their vehicle and move throughout the city
So, we need to minimize the total cost i.e.
 minimize C=Σc i . x i,       i=1,........n                                       (1)
 
 subject to:
 
            Σ(fj x j )≥ F i , ∀i,j∈ N i αD                                        (2)
            x i = {0, 1}, ∀i                                                      (3)
            x 0 i + y i 0i = n, ∀i ∈ N̂                                            (4)
            0 ≤ y ijk ≤ nx i x k , ∀(j, k) ∈ Ê ∪ (0 i , i), ∀i ∈ N̂                (5)
            j|(j,k)∈ Ê Σy ijk = x i x k +Σy ikl , l|(k,l)∈ Ê, ∀i, k ∈ N̂           (6)
            j∈ N̂ Σx j =y i 0i , ∀i∈ N̂                                             (7)
            0 ≤ x 0 i , ∀i ∈ N̂                                                    (8)
            x i = 1.                                                              (9)

where,
N-Set of potential charging station construction sites.
E-Set of connections connecting pairs of the construction sites.
n-Size of N .
d(i, j)-Distance of the shortest path from nodes i to j.
f i-Charging capacity of node i.
F i-Demand requirement of node i.
D-Average traversable distance of fully charged electric vehicles.
α-A discount factor.
x i-Boolean variable for construction at node i.
c i-Construction cost at node i.
N i αD  -Set of nodes within distance αD from node i.
N̂ -Set of nodes in induced graph.
Ê-Set of edges in induced graph.
0 i-Source node of flow attached to node i.
x 0 i-Residue of flow remained in 0 i .
y ijk-Amount of flow on edge (j, k) originated from 0 i .
