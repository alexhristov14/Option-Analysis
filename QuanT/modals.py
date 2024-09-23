import numpy as np
import scipy.stats as si

# Pricing models

class BlackScholesModel:
    def __init__(self, S, K, T, r, sigma):
        self.S = S        # Underlying asset price
        self.K = K        # Option strike price
        self.T = T        # Time to expiration in years
        self.r = r        # Risk-free interest rate
        self.sigma = sigma  # Volatility of the underlying asset

    def d1(self):
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
    
    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)
    
    def call_option_price(self):
        return (self.S * si.norm.cdf(self.d1(), 0.0, 1.0) - self.K * np.exp(-self.r * self.T) * si.norm.cdf(self.d2(), 0.0, 1.0))
    
    def put_option_price(self):
        return (self.K * np.exp(-self.r * self.T) * si.norm.cdf(-self.d2(), 0.0, 1.0) - self.S * si.norm.cdf(-self.d1(), 0.0, 1.0))


class BinomialOptionsPricing:
    def __init__(self, S, K, T, r, sigma, q, n) -> None:
        self.S = S       # Underlying asset price (current price)
        self.K = K       # Option strike price
        self.T = T       # Time to expiration in years
        self.r = r       # Risk-free interest rate
        self.sigma = sigma # Volatility of the underlying asset
        self.q = q       # Dividend yield
        self.n = n       # Number of time steps / height of the binomial tree
        self.u = 0       # Up factor
        self.d = 0       # Down factor
        self.R = 0       # Risk-free interest rate

    def init_parameters(self):
        self.u = np.exp(self.sigma * np.sqrt(self.T / self.n))
        self.d = 1 / self.u
        # TODO

class MonteCarlo:
    def __init__(self) -> None:
        pass


# Interest rate models

class CIR:
    def __init__(self) -> None:
        pass

class Vasicek:
    def __init__(self) -> None:
        pass

class HullWhite:
    def __init__(self) -> None:
        pass

# Portfolio models