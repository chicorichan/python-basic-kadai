class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

 #メソッドの定義
    def check_adult(self):
        if self.age >19:
            print(f"{self.name}は{self.age}歳なので大人です")
        else:
            print(f"{self.name}は{self.age}歳なので大人ではありません")

#インスタンス化
#human = Human("侍太郎", 36)
#human1 = Human("侍花子", 12)
#human2 = Human("侍一郎", 20)      

users = [Human("侍太郎", 36), Human("侍花子", 12), Human("侍一郎", 20)]
 
for user in users:
    user.check_adult()
