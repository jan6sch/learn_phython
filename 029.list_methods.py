basket = [1,2,3,4,5]
print(len(basket))

#adding (add one item)
new_list = basket.append(100) # changes basket in it's 'place' (append) not creating a new list
print(basket)
print(new_list) #does not work, look the comment on top

#insert
basket.insert(5, 99)

print(basket)

#extend (add one or multiple items)

basket.extend([101, 102])
print(basket)

#removing

basket.pop() # removes the last value of a list
print(basket)
basket.pop(0) # removes the first value of a list
print(basket)
basket.remove(100) # remove that exact value
print(basket)

what_to_remove = basket.pop(3) # removes the fourth value from the list basket, and saves in what you removed in a new variable
print(what_to_remove)
print(basket)

basket.clear()
print(basket)