import math
import random
from scipy import integrate
from Player_Functions import *

epsilon = 4e-14

#The reactive mean of a function f(pc,pd) over the unit square
def naive_mean_f(pc, pd, f):
    f_specialized = lambda pdprm, secern : f(pc, pd, secern + pdprm, pdprm)
    first_half = integrate.nquad(f_specialized, [lambda secern : [- secern, 1], [-1, 0]], opts = {'epsabs' : epsilon})
    second_half = integrate.nquad(f_specialized, [lambda secern : [0, 1 - secern], [0, 1]], opts = {'epsabs' : epsilon})
    return first_half[0] + second_half[0]

#The mean probability that I cooperate if you cooperated last round
def naive_mean_pC(pc, pd):
    return naive_mean_f(pc, pd, pC)

#The mean probability that I cooperate if you defected last round
def naive_mean_pD(pc, pd):
    return naive_mean_f(pc, pd, pD)

#The mean expected number of rounds before I defect against you, after we've both cooperated
def naive_mean_nice(pc, pd):
    return naive_mean_f(pc, pd, nice)

#The mean probability I cooperate in the stationary distribution
def naive_mean_c(pc, pd):
    return naive_mean_f(pc, pd, c)

#The mean probability you cooperate in the stationary distribution
def naive_mean_cprm(pc, pd):
    return naive_mean_f(pc, pd, cprm)

#The mean probability we both cooperate in the stationary distribution
def naive_mean_piCC(pc, pd):
    return naive_mean_f(pc, pd, piCC)

#The mean probability I cooperate and you defect in the stationary distribution
def naive_mean_piCD(pc, pd):
    return naive_mean_f(pc, pd, piCD)

#The mean probability I defect and you cooperate in the stationary distribution
def naive_mean_piDC(pc, pd):
    return naive_mean_f(pc, pd, piDC)

#The mean probability we both defect in the stationary distribution
def naive_mean_piDD(pc, pd):
    return naive_mean_f(pc, pd, piDD)

#The mean probability I reciprocate your last move
def naive_mean_rec(pc, pd):
    return naive_mean_f(pc, pd, rec)

#The mean probability I reciprocate your last move
def naive_mean_recprm(pc, pd):
    return naive_mean_f(pc, pd, recprm)

#My mean score against you in the Prisoner's dilemma
def naive_mean_score_Prisoner(pc, pd):
    return naive_mean_f(pc, pd, score_Prisoner)

#Your mean score against me in the Prisoner's dilemma
def naive_mean_scoreprm_Prisoner(pc, pd):
    return naive_mean_f(pc, pd, scoreprm_Prisoner)

#My mean score against you in the Snowdrift game
def naive_mean_score_Snowdrift(pc, pd):
    return naive_mean_f(pc, pd, score_Snowdrift)

#Your mean score against me in the Snowdrift game
def naive_mean_scoreprm_Snowdrift(pc, pd):
    return naive_mean_f(pc, pd, scoreprm_Snowdrift)

#Note that mean_piCD, mean_piDC, mean_piDD are all linear combinations of mean_piCC, mean_c, and mean_cprm

#naive_mean_list = [naive_mean_pC, naive_mean_pD, naive_mean_nice, naive_mean_c, naive_mean_cprm, naive_mean_piCC, naive_mean_piCD, naive_mean_piDC, naive_mean_piDD, naive_mean_rec, naive_mean_recprm, naive_mean_score_Prisoner, naive_mean_scoreprm_Prisoner, naive_mean_score_Snowdrift, naive_mean_scoreprm_Snowdrift]
