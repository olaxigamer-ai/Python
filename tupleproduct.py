def product(tup):
    product = 1
    for num in tup:
        product *= num
    return product
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)
result1 = product(tup1)
result2 = product(tup2)
print("Product of tuple 1", result1)
print("Product of tuple 2", result2)