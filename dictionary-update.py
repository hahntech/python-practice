#!/usr/bin/python

product = {
    "description": "WCG E-Book",
    "price": 2.75,
    "sold": 1500,
    "stock": 5700
}


def sell(p):
    # this essentially creates an array to contain key/value pairs
    # each value is updated by getting the current and modifing it
    # +/-1
    newValue = {"sold": p.get("sold", 0) + 1, "stock": p.get("stock") - 1}
    # next, we call the update() method on the dictionary passing the
    # the newValue as its argument
    p.update(newValue)


def print_product(p):
    print(", ".join(["{}: {}".format(str(k), str(product[k])) for k in sorted(p.keys())]))

print_product(product)
for i in range(0, 100):
    sell(product)
print_product(product)
