def is_purchase(price, tax):
    total_price=price*(1 + tax)
    print(f"{total_price}円で購入されました。")

is_purchase(100,0.1)