from mean_Player_Functions import *
from naive_mean_Player_Functions import *
import random

N = 10**2
N=1

for i in range(0,N):
    pc = random.random()
    pd = random.random()
    print(mean_c(pc,pd))
    print(naive_mean_c(pc, pd))
    print(" ")
    print(mean_cprm(pc,pd))
    print(naive_mean_cprm(pc, pd))
    print(" ")
    print(mean_piCC(pc,pd))
    print(naive_mean_piCC(pc,pd))
    print(" ")
    print(mean_piCD(pc,pd))
    print(mean_piCD_alt(pc,pd))
    print(naive_mean_piCD(pc, pd))
    print(" ")
    print(mean_piDC(pc,pd))
    print(mean_piDC_alt(pc,pd))
    print(naive_mean_piDC(pc,pd))
    print(" ")
    print(mean_piDD(pc,pd))
    print(mean_piDD_alt(pc,pd))
    print(naive_mean_piDD(pc,pd))
    print(" ")
    print(mean_piCC(pc, pd) + mean_piCD(pc, pd) + mean_piDC(pc, pd) + mean_piDD(pc, pd))
    print(mean_piCC(pc, pd) + mean_piCD_alt(pc, pd) + mean_piDC_alt(pc, pd) + mean_piDD_alt(pc, pd))
    print(naive_mean_piCC(pc, pd) + naive_mean_piCD(pc, pd) + naive_mean_piDC(pc, pd) + naive_mean_piDD(pc, pd))
    print(" ")
    print(mean_rec(pc,pd))
    print(mean_rec_alt(pc,pd))
    print(naive_mean_rec(pc, pd))
    print(" ")
    print(mean_recprm(pc,pd))
    print(naive_mean_recprm(pc,pd))
    print(" ")
input("Done")
