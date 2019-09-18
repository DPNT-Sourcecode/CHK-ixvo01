
items_prices={'A':50,'B':30,'C':20,'D':15}
special_offers = {'3A':130, '2B':45}



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    for item in skus:
        if item in items_prices:
            total += items_prices[item]

