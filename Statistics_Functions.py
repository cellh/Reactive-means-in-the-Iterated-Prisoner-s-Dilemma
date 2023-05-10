from scipy import integrate
import math

epsilon = 1e-10

#Returns the mean of a function in two variables over the unit square
def mean(f):
    first_half = integrate.nquad(f, [lambda secern : [- secern, 1], [-1, 0]], opts = {'epsabs' : epsilon})
    second_half = integrate.nquad(f, [lambda secern : [0, 1 - secern], [0, 1]], opts = {'epsabs' : epsilon})
    return first_half[0] + second_half[0]

#Returns the nth central moment of a function in two variables over the unit square
def nth_central_moment(f, n = 2):
    mu = mean(f)
    fn = lambda pc, pd : (f(pc, pd) - mu)**n
    return mean(fn)

#Returns the standard deviation of f
def stddev(f):
    return math.sqrt(nth_central_moment(f, 2))

#Returns the covariance of f and g
def cov(f,g):
    muf = mean(f)
    mug = mean(g)
    fg = lambda pc, pd: (f(pc, pd) - muf)*(g(pc, pd) - mug)
    return mean(fg)

#Returns the correlation of f and g
def cor(f, g):
    return cov(f, g)/(stddev(f)*stddev(g))
