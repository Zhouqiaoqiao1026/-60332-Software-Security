class Item:
    price: float = 9.99

def main():
    i = Item()
    i.price = "cheap"  # type conflict: str to float
    return i.price

main()