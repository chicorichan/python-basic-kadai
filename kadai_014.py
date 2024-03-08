price1 = 100
price2 = 200

def total():
  tax = 1.1
  check = (price1+ price2)*tax
  return check

print(total())

#戻り値に数式というのはありですか？
price1 = 100
price2 = 200

def total():
  tax = 1.1
  return (price1+ price2)*tax

print(total())