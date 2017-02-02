from math import log,sqrt,exp
from scipy.stats import norm


def call_option_pricer(spot,strike,maturity,r,vol):
    d1=(log(spot/strike)+(r+0.5*vol*vol)*maturity)/vol/sqrt(maturity)
    d2=d1-vol*sqrt(maturity)
    price=spot*norm.cdf(d1)-strike*exp(-r*maturity)*norm.cdf(d2)
    return price
# print('OptionPrice:%.4f'%call_option_pricer(spot=2.45,strike=2.5,maturity=0.25,r=0.05,vol=0.25))

from WindPy import *

w.start()
w.menu
i = 0
while i < 50:
    wsddata1 = w.wsd("000001.SZ", "open,high,low,close,volume,amt", "2015-11-22", "2015-12-22", "Fill=Previous")
    print(wsddata1)
    i += 1

