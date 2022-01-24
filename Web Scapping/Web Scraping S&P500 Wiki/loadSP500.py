import pickle
with open('SP500.pickle', 'rb') as f:
    tickers = pickle.load(f)

print(tickers)