import math
import random

#The probability that I cooperate if you cooperated last round
def pC(pc, pd, pcprm, pdprm):
    return pc

#The probability that I cooperate if you defected last round
def pD(pc, pd, pcprm, pdprm):
    return pd

#The degree to which I prioritize cooperating with cooperators over defectors
def secern(pc, pd, pcprm, pdprm):
    return pc - pd

#The degree to which you prioritize cooperating with cooperators over defectors
def secernprm(pc, pd, pcprm, pdprm):
    return pcprm - pdprm

#The probability that you cooperate if I defected last round
def pCprm(pc, pd, pcprm, pdprm):
    return pcprm

#The probability that you cooperate if I defected last round
def pDprm(pc, pd, pcprm, pdprm):
    return pdprm

#The expected number of rounds before I defect against you, after we've both cooperated
def nice(pc, pd, pcprm, pdprm):
    return 1 - (1 - pc)/(1 - pc*pcprm)

#The expected number of rounds before you defect against me, after we've both cooperated
def niceprm(pc, pd, pcprm, pdprm):
    return 1 - (1 - pcprm)/(1 - pc*pcprm)

#The probability I cooperate in the stationary distribution
def c(pc, pd, pcprm, pdprm):
    v = pc - pd
    vprm = pcprm - pdprm
    return (pdprm*v + pd)/(1 - v*vprm)

#The probability you cooperate in the stationary distribution
def cprm(pc, pd, pcprm, pdprm):
    return c(pcprm, pdprm, pc, pd)

#The probability we both cooperate in the stationary distribution
def piCC(pc, pd, pcprm, pdprm):
    return c(pc, pd, pcprm, pdprm)*cprm(pc, pd, pcprm, pdprm)

#The probability I cooperate and you defect in the stationary distribution
def piCD(pc, pd, pcprm, pdprm):
    return c(pc, pd, pcprm, pdprm)*(1 - cprm(pc, pd, pcprm, pdprm))

#The probability I defect and you cooperate in the stationary distribution
def piDC(pc, pd, pcprm, pdprm):
    return (1 - c(pc, pd, pcprm, pdprm))*cprm(pc, pd, pcprm, pdprm)

#The probability we both defect in the stationary distribution
def piDD(pc, pd, pcprm, pdprm):
    return (1 - c(pc, pd, pcprm, pdprm))*(1 - cprm(pc, pd, pcprm, pdprm))

#The probability I reciprocate your last move
def rec(pc, pd, pcprm, pdprm):
    return pc*cprm(pc, pd, pcprm, pdprm) + (1 - pd)*(1 - cprm(pc, pd, pcprm, pdprm))

#The probability you reciprocate my last move
def recprm(pc, pd, pcprm, pdprm):
    return rec(pcprm, pdprm, pc, pd)

#My score against you in the Prisoner's dilemma
def score_Prisoner(pc, pd, pcprm, pdprm):
    rCC = 3
    rCD = 0
    rDC = 5
    rDD = 1
    return rCC*piCC(pc, pd, pcprm, pdprm) + rCD*piCD(pc, pd, pcprm, pdprm) + rDC*piDC(pc, pd, pcprm, pdprm) + rDD*piDD(pc, pd, pcprm, pdprm)

#Your score against me in the Prisoner's dilemma
def scoreprm_Prisoner(pc, pd, pcprm, pdprm):
    rCC = 3
    rCD = 0
    rDC = 5
    rDD = 1
    return rCC*piCC(pc, pd, pcprm, pdprm) + rDC*piCD(pc, pd, pcprm, pdprm) + rCD*piDC(pc, pd, pcprm, pdprm) + rDD*piDD(pc, pd, pcprm, pdprm)

#My score against you in the Snowdrift game
def score_Snowdrift(pc, pd, pcprm, pdprm):
    rCC = 3
    rCD = 1
    rDC = 5
    rDD = 0
    return rCC*piCC(pc, pd, pcprm, pdprm) + rCD*piCD(pc, pd, pcprm, pdprm) + rDC*piDC(pc, pd, pcprm, pdprm) + rDD*piDD(pc, pd, pcprm, pdprm)

#Your score against me in the Snowdrift game
def scoreprm_Snowdrift(pc, pd, pcprm, pdprm):
    rCC = 3
    rCD = 1
    rDC = 5
    rDD = 0
    return rCC*piCC(pc, pd, pcprm, pdprm) + rDC*piCD(pc, pd, pcprm, pdprm) + rCD*piDC(pc, pd, pcprm, pdprm) + rDD*piDD(pc, pd, pcprm, pdprm)
