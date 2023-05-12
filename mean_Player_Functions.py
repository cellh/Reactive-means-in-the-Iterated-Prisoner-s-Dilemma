import math
import random

#The mean probability that I cooperate if you cooperated last round
def mean_pC(pc, pd):
    return pc

#The mean probability that I cooperate if you defected last round
def mean_pD(pc, pd):
    return pd

#The mean probability that I cooperate if you defected last round
def mean_r(pc, pd):
    return pc - pd


#The mean chance you defect against me before I defect, after we've both cooperated
def mean_nice(pc, pd):
        if pc == 0:
            return 0
        elif pc == 1:
            return 1
        else:
            return 1+(1-pc)*math.log(1-pc)/pc

#The mean chance I defect against you before you defect, after we've both cooperated
def mean_niceprm(pc, pd):
        if pc == 0:
            return 1
        elif pc == 1:
            return 0
        else:
            return 1-(1/pc)+((1/pc)-(1/(pc**2)))*math.log(1-pc)

#The mean probability I cooperate in the stationary distribution
def mean_c(pc, pd):
    secern = pc - pd
    rational = secern**2
    positive = (1 + secern)*(-1 + 2*pd + secern)
    negative = (1 - secern)*(-1 + 2*pd + secern)
    denominator = 2*secern**2
    if pc == pd:
        return pc
    elif (pc == 1 and pd == 0) or (pc == 0 and pd == 1):
        return 1/2
    else:
        return (rational + positive*math.log(1 + secern) + negative*math.log(1 - secern))/denominator

#The mean probability you cooperate in the stationary distribution
def mean_cprm(pc, pd):
    secern = pc - pd
    rational = (1 - 2*pd)*secern**2
    positive = (1 + secern)*(-1 + 2*pd + secern)
    negative = (1 - secern)*(-1 + 2*pd + secern)
    denominator = 2*secern**3
    #This is hacky and bad. I should figure out how to handle the diagonal better
    if pc == pd:
        return 1/2
    elif (pc == 1 and pd == 0) or (pc == 0 and pd == 1):
        return 1/2
    else:
        return (rational + positive*math.log(1 + secern) + negative*math.log(1 - secern))/denominator

#The mean probability we both cooperate in the stationary distribution
def mean_piCC(pc, pd):
    secern = pc - pd
    rational = (2 - pd)*secern**2
    positive = -(2 + 2*pd**2*(2 + secern) + pd*(-5 + secern**2))
    negative = (2*pd**2*(-2 + secern) - 2*(-1 + secern)**2 + pd*(5 - 6*secern + secern**2))
    denominator = 2*secern**3
    try:
        if pc == pd:
            return pc/2
        elif pc == 1 and pd == 0:
            return 1 - math.log(2)
        elif pc == 0 and pd == 1:
            return math.log(2) - 1/2
        else:
            return (rational + positive*math.log(1 + secern) + negative*math.log(1 - secern))/denominator
    except:
        return 0

#The mean probability I cooperate and you defect in the stationary distribution
def mean_piCD(pc, pd):
    secern = pc - pd
    rational = -(2 - pd)*secern**2 + secern**3
    positive = (2 - secern + secern**3 + 2*pd**2*(2 + secern) + pd*(-5 + 2*secern + 3*secern**2))
    negative = -(2*pd**2*(-2 + secern) + (-2 + secern)*(-1 + secern)**2 + pd*(5 - 8*secern + 3*secern**2))
    denominator = 2*secern**3
    try:
        if pc == pd:
            return pc/2
        elif pc == 1 and pd == 0:
            return math.log(2) - 1/2
        elif pc == 0 and pd == 1:
            return 1 - math.log(2)
        else:
            return (rational + positive*math.log(1 + secern) + negative*math.log(1 - secern))/denominator
    except:
        return 0

def mean_piCD_alt(pc, pd):
    return mean_c(pc, pd) - mean_piCC(pc, pd)

#The mean probability I defect and you cooperate in the stationary distribution
def mean_piDC(pc, pd):
    secern = pc - pd
    rational = -(1 + pd)*secern**2
    positive = (1 + secern**2 + 2*pd**2*(2 + secern) + pd*(-3 + 2*secern + secern**2))
    negative = (-2*pd**2*(-2 + secern) + (-1 + secern)**2 - pd*(3 - 4*secern + secern**2))
    denominator = 2*secern**3
    try:
        if pc == pd:
            return (1 - pc)/2
        elif pc == 1 and pd == 0:
            return math.log(2) - 1/2
        elif pc == 0 and pd == 1:
            return 1 - math.log(2)
        else:
            return (rational + positive*math.log(1 + secern) + negative*math.log(1 - secern))/denominator
    except:
        return 0

def mean_piDC_alt(pc, pd):
    return mean_cprm(pc, pd) - mean_piCC(pc, pd)

#The mean probability we both defect in the stationary distribution
def mean_piDD(pc, pd):
    secern = pc - pd
    rational = (1 + pd)*secern**2 + secern**3
    positive = -(1 - secern + secern**2 + secern**3 + 2*pd**2*(2 + secern) + pd*(-3 + 4*secern + 3*secern**2))
    negative = (2*pd**2*(-2 + secern) + 3*pd*(-1 + secern)**2 + (-1 + secern)**3)
    denominator = 2*secern**3
    try:
        if pc == pd:
            return (1 - pc)/2
        elif pc == 1 and pd == 0:
            return 1 - math.log(2)
        elif pc == 0 and pd == 1:
            return math.log(2) - 1/2
        else:
            return (rational + positive*math.log(1 + secern) + negative*math.log(1 - secern))/denominator
    except:
        return 0

def mean_piDD_alt(pc, pd):
    return 1 - mean_c(pc, pd) - mean_cprm(pc, pd) + mean_piCC(pc, pd)

#The mean probability I reciprocate your last move
def mean_rec(pc, pd):
    secern = pc - pd
    rational = secern**2*(-1 - 4*pd**2 - 4*pd*(-1 + secern) + 3*secern)
    positive = (1 + secern)*(-1 + 2*pd + secern)**2
    negative = (1 - secern)*(-1 + 2*pd + secern)**2
    denominator = 2*secern**3
    try:
        if pc == pd:
            return 1/2
        elif pc == 1 and pd == 0:
            return 1
        elif pc == 0 and pd == 1:
            return 0
        else:
            return (rational + positive*math.log(1 + secern) + negative*math.log(1 - secern))/denominator
    except:
        return 0

#The mean probability I reciprocate your last move
def mean_rec_alt(pc, pd):
    return pc*mean_cprm(pc, pd) + (1 - pd)*(1 - mean_cprm(pc, pd))

#The mean probability I reciprocate your last move
def mean_recprm(pc, pd):
    secern = pc - pd
    rational = secern**2*(-5 + 3*secern)
    positive = (1 + secern)**3
    negative = (1 - secern)**3
    denominator = 6*secern**3
    try:
        if pc == pd:
            return 1/2
        if pc == 1 and pd == 0:
            return 4*math.log(2)/3-1/3
        if pc == 0 and pd == 1:
            return -4*math.log(2)/3+4/3
        else:
            return (rational + positive*math.log(1 + secern) + negative*math.log(1 - secern))/denominator
    except:
        return 0

#My mean score against you in the Prisoner's dilemma
def mean_score_Prisoner(pc, pd):
    rCC = 3
    rCD = 0
    rDC = 5
    rDD = 1
    return rCC*mean_piCC(pc, pd) + rCD*mean_piCD(pc, pd) + rDC*mean_piDC(pc, pd) + rDD*mean_piDD(pc, pd)

#Your mean score against me in the Prisoner's dilemma
def mean_scoreprm_Prisoner(pc, pd):
    rCC = 3
    rCD = 0
    rDC = 5
    rDD = 1
    return rCC*mean_piCC(pc, pd) + rDC*mean_piCD(pc, pd) + rCD*mean_piDC(pc, pd) + rDD*mean_piDD(pc, pd)

#My mean score against you in the Snowdrift game
def mean_score_Snowdrift(pc, pd):
    rCC = 3
    rCD = 1
    rDC = 5
    rDD = 0
    return rCC*mean_piCC(pc, pd) + rCD*mean_piCD(pc, pd) + rDC*mean_piDC(pc, pd) + rDD*mean_piDD(pc, pd)

#Your mean score against me in the Snowdrift game
def mean_scoreprm_Snowdrift(pc, pd):
    rCC = 3
    rCD = 1
    rDC = 5
    rDD = 0
    return rCC*mean_piCC(pc, pd) + rDC*mean_piCD(pc, pd) + rCD*mean_piDC(pc, pd) + rDD*mean_piDD(pc, pd)
