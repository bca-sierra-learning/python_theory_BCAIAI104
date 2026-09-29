# Complete the five functions below. Then complete the main program so it calls them 
# and prints the bill.

# get_price(item) returns the price of the item.
#  It returns 0 if the item is not on the menu.
# item_cost(item, qty) returns the cost of buying qty of an item.
#  It must use get_price().
# calculate_gst(amount, rate=0.05) returns the GST on the amount.
#  The rate is 5% unless another rate is given.
# generate_bill(subtotal, discount_percent=0)
#  returns three values: the discount, the GST 
# (calculated on the amount after the discount), and the final total.
# split_bill(total, people) returns two values: the whole rupees each person pays, 
#  and the rupees left over.


def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa":
        return 50
    elif item == "tea":
        return 10
    elif item == "golibaje":
        return 40
    else:
        return 0


def item_cost(item, qty):
    # TODO: call get_price() and return the cost
    price=get_price(item)
    return price * qty


def calculate_gst(amount, rate=0.05):
    # TODO: return the GST rounded to 2 decimals
    gst=amount * rate
    return round(gst,2)


def generate_bill(subtotal, discount_percent=0):
    discount = subtotal * discount_percent
    amount_after_discount = subtotal - discount
    gst = calculate_gst(amount_after_discount)
    total = amount_after_discount + gst
    return discount,gst,total


def split_bill(total, people):
    each_pays = total / people   
    left_over = total % people
    return each_pays,left_over


# ---------------- Main program ----------------
# A group of 3 friends orders 2 dosa and 3 coffee, with a 10% coupon.

subtotal = item_cost('dosa',2)# TODO: call item_cost() for dosa and coffee and add them
discount, gst, total = # TODO: call generate_bill() using a KEYWORD argument
each, extra = # TODO: call split_bill() with the total (as a whole number) and 3 people

print("Subtotal :", subtotal)
print("Discount :", discount)
print("GST      :", gst)
print("Total    :", total)
print("Each pays:", each, "| Left over:", extra)