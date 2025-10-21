# li1 = [1,2,3,4]
# li2 = ['a', 'b', 'c', 'd']
# li3 = [1,2.5,'a', True]

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
# print(amazon_cart[0])
# print(amazon_cart)
# print(amazon_cart[0::2])

# print(amazon_cart)
amazon_cart[0] = 'laptop'
# print(amazon_cart)

new_cart = amazon_cart[:] #new card is = amazon card, and only new card gets a new 0 value ex. newc starts with gum and amac start with laptop
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
new_cart = amazon_cart   #overwrites both lists, ex. newc and amac start with gum
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
