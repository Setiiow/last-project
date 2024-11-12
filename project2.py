products=[]
for i in range (5):
    products.append(input("enter product"))
import datetime
class Store:
    def __init__(self,product):
        self.product=product
    def buy(self):
        products.append(input("enter product"))
        print(products)
    def sell(self):
        del products[int(input("enter index of product you selled"))]
        print(products)
    def changing(self):
        products[int(input("enter index of product you wanna change"))]=input("enter product")
        print(products)
    def show(self):
        print(products)
    def now_time(self):
        from datetime import datetime
        print(datetime.now().time())
    def now_date(self):
        from datetime import date
        print(datetime.datetime.now())
s=Store(products)
while True:
    num=int(input("what do you want to do? (enter number 0 to 6)"))
    if num==0:
        print("closed")
    elif num==1:
        s.buy()
    elif num==2:
        s.sell()
    elif num==3:
        s.changing()
    elif num==4:
        s.show()
    elif num==5:
        s.now_time()
    elif num==6:
        s.now_date()
    else:
        print("unvalid")


#"juice","cake","soda","ice cream","milk"
