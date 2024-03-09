class Human:
  def __init__(self,name,age):
    self.name=name
    self.age=age

 #メソッドの定義
  def set_name(self,name):
    self.name = name

  def set_age(self,age):
    self.age = age

#インスタンス化
human = Human("侍太郎",36)
human1 = Human("侍花子",12)
human2 = Human("侍一郎",20)

users = {human.name:human.age, human1.name:human1.age, human2.name:human2.age}

for key, value in users.items():
    #print(f"{key}は{value}です")
    if value > 19:
      print(f"{key}は{value}歳の大人です。")
    else:
      print(f"{key}は{value}歳なので大人ではありません。")