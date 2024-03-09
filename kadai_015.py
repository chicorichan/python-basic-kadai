class Human:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  #メソッドの定義
  def set_name(self,name):
    self.name = name

  def set_age(self,age):
    self.age = age
  
  def printinfo(self):
    print(f"私は{self.name}です。")
    print(f"{self.age}歳です。")

#インスタンス化
human = Human("侍太郎",36)

human.printinfo()