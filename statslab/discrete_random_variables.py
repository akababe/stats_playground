import math
import scipy.stats as stats

def permutations(n, r):
    """
    Returns nPr = n! / (n-r)!
    """
    return math.perm(n, r)

def combinations(n, r):
    """
    Returns nCr = n! / (r! * (n-r)!)
    """
    return math.comb(n, r)

def binomial_pmf(k, n, p):
    """
    Probability Mass Function for Binomial(n, p).
    P(X=k)
    """
    return stats.binom.pmf(k, n, p)

def binomial_cdf(k, n, p):
    """
    Cumulative Distribution Function for Binomial(n, p).
    P(X <= k)
    """
    return stats.binom.cdf(k, n, p)

def poisson_pmf(k, mu):
    """
    Probability Mass Function for Poisson(mu).
    P(X=k)
    """
    return stats.poisson.pmf(k, mu)

def poisson_cdf(k, mu):
    """
    Cumulative Distribution Function for Poisson(mu).
    P(X <= k)
    """
    return stats.poisson.cdf(k, mu)

def geometric_pmf(k, p):
    """
    Probability Mass Function for Geometric(p).
    P(X=k) (number of trials until the first success)
    """
    return stats.geom.pmf(k, p)

def geometric_cdf(k, p):
    """
    Cumulative Distribution Function for Geometric(p).
    P(X <= k)
    """
    return stats.geom.cdf(k, p)

def bernoulli_pmf(k, p):
    """
    Probability Mass Function for Bernoulli(p).
    """
    return stats.bernoulli.pmf(k, p)
