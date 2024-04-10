'''
7kyu

You love coffee and want to know what beans you can afford to buy it.

The first argument to your search function will be a number which represents your budget.

The second argument will be an array of coffee bean prices.

Your 'search' function should return the stores that sell coffee within your budget.

The search function should return a string of prices for the coffees beans you can afford. The prices in this string are to be sorted in ascending order.


'''

def filter_cofee(budget, prices):

    # instanciate a variable for having a list of acceptable bean prices
    # sort your prices first
    # iterate across the bean_prices and if the bean_prices is <= to your budget 
    # convert to string
    # you append to the empty list 
    # .join / 

    within_budget = []
    sorted_prices = sorted(prices)
    for price in sorted_prices:
        if price <= budget:
            within_budget.append(price)

    return ",".join(within_budget)

    # refactored

    
    #return ",".join([str(price) for price in sorted(prices) if price <= budget])
