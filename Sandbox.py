from scipy import integrate
import math
import random
from Player_Functions import *
from naive_mean_Player_Functions import *
from mean_Player_Functions import *
from Statistics_Functions import *
from naive_Statistics_Functions import *

function_list = [(mean_niceprm,"n'"),(mean_pC, "pC"),(mean_pD, "pD"),(mean_c, "c"), (mean_cprm,"c'"), (mean_piCC, "piCC"),(mean_piCD, "piCD"), (mean_piDC, "piDC"), (mean_piDD, "piDD"), (mean_rec, "t"), (mean_recprm, "t'"), (mean_nice, "n"), (mean_score_Prisoner, "sPr"), (mean_scoreprm_Prisoner, "sPr'"), (mean_score_Snowdrift, "sSn"), (mean_scoreprm_Snowdrift, "sSn'"), (mean_r,"r")]

N = 5000

for f in function_list:
    for g in function_list:
        print(f[1], g[1])
        print(cor(f[0],g[0]))
        print("Corr:",naiveCor(f[0],g[0], N))
        print("Cov:",naiveCov(f[0],g[0], N))
    print(naive_stddev(f[0]))
    for n in range(2,5):
        print(n, naive_nth_central_moment(f[0], n))

for f in function_list:
    print(f[1])
    print("Naive Mean: ",naiveMean(f[0],N))
    print("Naive StdDev: ",naiveStdDev(f[0],N))

    print("Mean: ",mean(f[0]))
    print("StdDev: ",stddev(f[0]))   



