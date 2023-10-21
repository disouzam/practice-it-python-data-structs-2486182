from collections import deque

def main():
    #add code here
    last_five_products_bought = deque(maxlen= 5)
    print ("No item bought yet.")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: DES005")
    last_five_products_bought.appendleft("DES005")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: BEV003")
    last_five_products_bought.appendleft("BEV003")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: DES004")
    last_five_products_bought.appendleft("DES004")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: DES001")
    last_five_products_bought.appendleft("DES001")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: DES002")
    last_five_products_bought.appendleft("DES002")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: DES003")
    last_five_products_bought.appendleft("DES003")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: DES002")
    last_five_products_bought.appendleft("DES002")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: DES002")
    last_five_products_bought.appendleft("DES002")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: STA004")
    last_five_products_bought.appendleft("STA004")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: SAL004")
    last_five_products_bought.appendleft("SAL004")
    print("Last five products bought " + str(last_five_products_bought))

    print("Bought item: ENT005")
    last_five_products_bought.appendleft("ENT005")
    print("Last five products bought " + str(last_five_products_bought))

    return last_five_products_bought

if __name__ == "__main__":
    main()