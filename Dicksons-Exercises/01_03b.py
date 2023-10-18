from collections import Counter

def main():
    # Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    # sell 5 starters, 3 salads, and 3 entrees
    product_sold = Counter(STA001=5, SAL002= 3, ENT004= 3)
    inventory = inventory - product_sold
    # make 9 more starters and 1 more entree
    new_products = Counter(STA001=9, ENT004= 1)
    inventory.update(new_products)
    print(inventory)


if __name__ == "__main__":
    main()
