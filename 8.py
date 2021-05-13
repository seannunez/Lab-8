import numpy as np

Stocks = np.array([
    [4, 10, 35],
    [2, 15, 45],
    [6, 25, 40]])
Price = np.array([
    [16800],
    [20550],
    [26500]])

Totalprice = np.linalg.inv(Stocks) @ Price
Totalprice2 = np.linalg.solve(Stocks, Price)
print("Month 1 Stock and Price BUNDLE")
print("Stocks: \nUSD/$", Stocks[0],"\nPrice: \nUSD/$", Price[0])
print("-"*42)
print("Month 2 Stock and Price BUNDLE")
print("Stocks: \nUSD/$", Stocks[1],"\nPrice: \nUSD/$", Price[1])
print("-"*42)
print("Month 3 Stock and Price BUNDLE")
print("Stocks: \nUSD/$", Stocks[2],"\nPrice: \nUSD/$", Price[2])
print("-"*42)
print("INVERSE")
print("The price of one set of NOS system is: USD/${:.2f}".format(float(Totalprice[0])))
print("The price of one set of Intake Pipes  is: USD/${:.2f}".format(float(Totalprice[1])))
print("The price of one pack of Injectors is: USD/${:.2f}".format(float(Totalprice[2])))
print("-"*42)
print("SOLVE")
print("The price of one set of NOS system is: USD/${:.2f}".format(float(Totalprice2[0])))
print("The price of one set of Intake Pipes  is: USD/${:.2f}".format(float(Totalprice2[1])))
print("The price of one pack of Injectors is: USD/${:.2f}".format(float(Totalprice2[2])))
