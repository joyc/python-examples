price = 24.95
discount_factor = 0.6
shipping_first = 3
shipping_rest = 0.75
num_copies = 60

discounted_price = 24.95 * discount_factor
total_price = discounted_price * num_copies
print "Cost for", num_copies, "books is", total_price

shipping_cost = shipping_first + (num_copies - 1) * shipping_rest
print "Shipping cost is", shipping_cost

total_cost = total_price + shipping_cost
print "Total cost is", total_cost
