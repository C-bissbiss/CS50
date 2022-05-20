# Assumes we are in a long position
import sys
from datetime import datetime, date
from math import log, sqrt, exp
import numpy as np
import pandas as pd
from pandas import DataFrame
import pandas_datareader.data as web
from yahoo_fin import options
from scipy.stats import norm

def main():
    global dividend, ticker, optiontype, K, expiry
    i = 0
    while i < 2:
        dividend = input("Does the security yields cash dividends? ").lower().strip()
        if any(dividend == f for f in ['yes', 'no']):
            break
        else:
            i += 1
            if i < 2:
                print("Please enter YES or NO")
            else:
                print("Too many errors, please restart")
                quit()
    ticker = input('What is the ticker of the security? ').lower().strip()
    while i < 2:
        optiontype = input('Is it a Call or a Put? ').lower().strip()
        if any(optiontype == f for f in ['call', 'put']):
            break
        else:
            i += 1
            if i < 2:
                print("Please enter CALL or PUT")
            else:
                print("Too many errors, please restart")
                quit()
    while i < 2:
        try:
            K = float(input("What is the strike price? $ "))
            break
        except ValueError:
                i += 1
                if i < 2:
                    print("The entered value is not a float")
                else:
                    print("Too many errors, please restart")
                    quit()
    while i < 2:
        try:
            expiry = input('What is the date of expiration(yyyy-mm-dd)? ').strip()
            datetime.strptime(expiry, "%Y-%m-%d")
            break
        except ValueError:
                i += 1
                if i < 2:
                    print("Please enter the format YYYY-MM-DD")
                else:
                    print("Too many errors, please restart")
                    quit()
main()

def mainnd():
    if optiontype == "call":
        datand = {'Obs. Call Price $': [obs],
        'Theo. Call Price $': [round(call(S, K, T, r, sigma),3)],
        '\u0394': [round(norm.cdf(d1(S,K,T,r,sigma)),3)],
        '\u0393': [round(norm.pdf(d1(S,K,T,r,sigma))/(S*sigma*sqrt(T)),3)],
        '\u03bd': [round(0.01*(S*norm.pdf(d1(S,K,T,r,sigma))*sqrt(T)),3)],
        '\u0398': [round(0.01*(-(S*norm.pdf(d1(S,K,T,r,sigma))*sigma)/(2*sqrt(T)) - r*K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))),3)],
        '\u03C1': [round(0.01*(K*T*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))),3)],
        'Implied \u03C3': [vol]}
        df = pd.DataFrame(datand, index=[''])
        print(), print(df), print()

    elif optiontype == "put":
        datand = {'Obs. Call Price $': [obs],
        'Theo. Put Price $': [round(put(S, K, T, r, sigma),3)],
        '\u0394': [round((norm.cdf(d1(S,K,T,r,sigma))-1),3)],
        '\u0393': [round(norm.pdf(d1(S,K,T,r,sigma))/(S*sigma*sqrt(T)),3)],
        '\u03bd': [round(0.01*(S*norm.pdf(d1(S,K,T,r,sigma))*sqrt(T)),3)],
        '\u0398': [round(0.01*(-(S*norm.pdf(d1(S,K,T,r,sigma))*sigma)/(2*sqrt(T)) + r*K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma))),3)],
        '\u03C1': [round(0.01*(-K*T*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma))),3)],
        'Implied \u03C3': [vol]}
        df = pd.DataFrame(datand, index=[''])
        print(), print(df), print()


def mainwd():
    if optiontype == "call":

        datawd = {'Obs. Call Price $': [obs],
        'Theo. Call Price $': [round(call(S, K, T, r, sigma,y),3)],
        '\u0394': [round(norm.cdf(d1(S,K,T,r,sigma,y)),3)],
        '\u0393': [round(exp(-y*T)*(norm.pdf(d1(S,K,T,r,sigma,y))/(S*sigma*sqrt(T))),3)],
        '\u03bd': [round(0.01*(exp(-y*T)*S*norm.pdf(d1(S,K,T,r,sigma,y))*sqrt(T)),3)],
        '\u0398': [round(0.01*(-(exp(-y*T)*S*norm.pdf(d1(S,K,T,r,sigma,y))*sigma)/(2*sqrt(T)) + y*exp(-y*T)*S*norm.cdf(d1(S,K,T,r,sigma,y)) - r*K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma,y))),3)],
        'Int. Rates \u03C1': [round(0.01*(-K*T*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma,y))),3)],
        'Div. \u03C1': [round(0.01*(-S*exp(-y*T)*norm.cdf(-d1(S,K,T,r,sigma,y))),3)],
        'Implied \u03C3': [vol]}
        df = pd.DataFrame(datawd, index=[''])
        print(), print(df), print()
    elif optiontype == "put":
        datawd = {'Obs. Call Price $': [obs],
        'Theo. Put Price $': [round(put(S, K, T, r, sigma,y),3)],
        '\u0394': [round((norm.cdf(-d1(S,K,T,r,sigma,y))-exp(-y*T)),3)],
        '\u0393': [round(exp(-y*T)*norm.pdf(d1(S,K,T,r,sigma,y))/(S*sigma*sqrt(T)),3)],
        '\u03bd': [round(0.01*(exp(-y*T)*S*norm.pdf(d1(S,K,T,r,sigma,y))*sqrt(T)),3)],
        '\u0398': [round(0.01*(-(exp(-y*T)*S*norm.pdf(d1(S,K,T,r,sigma,y))*sigma)/(2*sqrt(T)) - y*exp(-y*T)*S*norm.cdf(d1(S,K,T,r,sigma,y)) + r*K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma,y))),3)],
        'Int. Rates \u03C1': [round(0.01*(-K*T*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma,y))),3)],
        'Div. \u03C1': [round(0.01*(-S*exp(-y*T)*norm.cdf(-d1(S,K,T,r,sigma,y))),3)],
        'Implied \u03C3': [round(vol)]}
        df = pd.DataFrame(datawd, index=[''])
        print(), print(df), print()


# NO DIVIDENDS
if dividend == "no":

    def d1(S,K,T,r,sigma):
        return(log(S/K)+(r+sigma**2/2.)*T)/(sigma*sqrt(T))
    def d2(S,K,T,r,sigma):
        return d1(S,K,T,r,sigma)-sigma*sqrt(T)
    def call(S,K,T,r,sigma):
        return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
    def put(S,K,T,r,sigma):
        return K*exp(-r*T)*(1-norm.cdf(d2(S,K,T,r,sigma)))-S*(1-norm.cdf(d1(S,K,T,r,sigma)))
    today = datetime.now()
    one_year_ago = today.replace(year=today.year-1)
    df = web.DataReader(ticker, 'yahoo', one_year_ago, today)
    df = df.sort_values(by="Date")
    df = df.dropna()
    df = df.assign(close_day_before=df.Close.shift(1))
    df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)
    sigma = np.sqrt(252) * df['returns'].std()
    # needs change: doesn't work on weekends
    r = (web.DataReader(
        "^TNX", 'yahoo', today.replace(day=today.day-1), today)['Close'].iloc[-1])/100
    S = df['Close'].iloc[-1]
    T = (datetime.strptime(expiry, "%Y-%m-%d") - datetime.now()).days / 365
    chain = options.get_options_chain(ticker, expiry)
    df = chain[optiontype+"s"]
    vol = df[df["Strike"] == K]["Implied Volatility"]
    try:
        vol = float(vol.str.replace("%", ""))/100
    except TypeError:
        print("The option does not exit, please review your input")
        quit()
    obs = df[df["Strike"] == K]["Last Price"]
    obs = float(obs)
    if __name__ == "__main__":
        mainnd()


# WITH DIVIDENDS
if dividend == "yes":
    def d1(S,K,T,r,sigma,y):
        return(log(S/K)+(r-y+sigma**2/2.)*T)/(sigma*sqrt(T))
    def d2(S,K,T,r,sigma,y):
        return d1(S,K,T,r,sigma,y)-sigma*sqrt(T)
    def call(S,K,T,r,sigma,y):
        return S*exp(-y*T)*norm.cdf(d1(S,K,T,r,sigma,y))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma,y))
    def put(S,K,T,r,sigma,y):
        return K*exp(-r*T)*(1-norm.cdf(d2(S,K,T,r,sigma,y)))-S*exp(-y*T)*(1-norm.cdf(d1(S,K,T,r,sigma,y)))
    today = datetime.now()
    one_year_ago = today.replace(year=today.year-1)
    dividends = web.DataReader(ticker, 'yahoo-dividends', one_year_ago, today)
    dividends.head()
    mean = dividends['value'].mean()
    y = mean
    df = web.DataReader(ticker, 'yahoo', one_year_ago, today)
    df = df.sort_values(by="Date")
    df = df.dropna()
    df = df.assign(close_day_before=df.Close.shift(1))
    df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)
    sigma = np.sqrt(252) * df['returns'].std()
    # needs change: doesn't work on weekends
    r = (web.DataReader(
        "^TNX", 'yahoo', today.replace(day=today.day-1), today)['Close'].iloc[-1])/100
    S = df['Close'].iloc[-1]
    T = (datetime.strptime(expiry, "%Y-%m-%d") - datetime.now()).days / 365
    chain = options.get_options_chain(ticker, expiry)
    df = chain[optiontype+"s"]
    vol = df[df["Strike"] == K]["Implied Volatility"]
    try:
        vol = float(vol.str.replace("%", ""))/100
    except TypeError:
        print("The option does not exit, please review your input")
        quit()
    obs = df[df["Strike"] == K]["Last Price"]
    obs = float(obs)
    if __name__ == "__main__":
        mainwd()

# test for bugs
# make pytest