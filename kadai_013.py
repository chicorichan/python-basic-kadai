def purchase(price, tax):
    total_price=price*(1 + tax)
    return total_price

check = purchase(100,0.1)
print(f"{check}円で購入されました。")