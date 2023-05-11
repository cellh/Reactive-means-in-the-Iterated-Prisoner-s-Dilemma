import math
import random

N_default = 2000

#Returns the mean of a function in two variables over the unit square
def naiveMean(f, N = N_default):
    S = 0
    for k1 in range(0,N):
        for k2 in range(0,N):
            S += f(k1/N, k2/N)
            
    return S/N**2

#Returns the mean of a function in two variables over the unit square
def simpsonsMean(f, N = N_default):
    S = f(0, 0) + f(0,1) + f(1,0) + f(1,1)
    if N % 2 != 0:
        N += 1
    for k1 in range(1,N):
        weight1 = 2 + 2*(k1 % 2)
        for k2 in range(1,N):
            weight2 = 2 + 2*(k2 % 2)
            S += weight1*weight2*f(k1/N, k2/N)
    return S/(9*N*N)

#Returns the mean of a function in two variables over the unit square
def randomMean(f, N = N_default):
    S = 0
    for k in range(0,N):
        S += f(random.random(), random.random())
    return S/N

#Returns the nth central moment of a function in two variables over the unit square
def naiveCentralMoment(f, n = 2, N = N_default):
    mu = naiveMean(f, N)
    fn = lambda pc, pd : (f(pc, pd) - mu)**n
    return naiveMean(fn, N)

#Returns the standard deviation of f
def naiveStdDev(f, N = N_default):
    return math.sqrt(naiveCentralMoment(f, 2, N))

#Returns the covariance of f and g
def naiveCov(f,g, N = N_default):
    muf = naiveMean(f, N)
    mug = naiveMean(g, N)
    fg = lambda pc, pd: (f(pc, pd) - muf)*(g(pc, pd) - mug)
    return naiveMean(fg, N)

#Returns the correlation of f and g
def naiveCor(f, g, N = N_default):
    return naiveCov(f, g, N)/(naiveStdDev(f, N)*naiveStdDev(g, N))
