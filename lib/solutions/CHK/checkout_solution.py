
items_prices={'A':50,'B':30,'C':20,'D':15}
special_offers = {'3A':130, '2B':45}



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    for item in skus:
        print(skus)
        same_item_purchased = str(skus.count(item))+'item'
        if same_item_purchased in special_offers:
            total += special_offers[same_item_purchased]
            skus.replace(item, '')
        if item in items_prices:
            total += items_prices[item]
        else:
            return -1
    return total


