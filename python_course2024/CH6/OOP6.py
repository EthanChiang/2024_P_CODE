class Employee:
    def __init__(self) -> None:
        self.income =0
        # self.__tax = 0

    def earn_money(self,money):
        self.income += money
        # self.__tax += self.income *0.05

    # def get_tax(self):
    #     return self.__tax

    @property    #一個虛擬的PROPERTY 不是方法
    def tax_amount(self):
        return self.income *0.05
    
    @tax_amount.setter
    def tax_amount(self, tax_number):
        self.income = tax_number * 20


wilson = Employee()
wilson.earn_money(300)
# print(wilson.get_tax())
wilson.tax_amount = 200
print(wilson.income) 
print(wilson.tax_amount)       