def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage
products_list = ['Apple', 'Banana', 'Orange', 'Apple', 'Apple', 'Banana']
target_product = 'Apple'
result = linear_search_product(products_list, target_product)
print(f"Indices of {target_product}: {result}")