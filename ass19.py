'''Create a class STORE to keep track of Products(product Code, Name and price)
Display menu of all products to user.
enerate bill as per order.'''

class STORE:
    __product_code = []
    __name = []
    __price =[]

    def input_data(self):
        for i in range(3):
            self.__product_code.append(int(input("Enter the code of product: ")))
            self.__name.append(input("Enter the name of product: "))
            self.__price.append(float(input("Enter the price of product: ")))
    def display_data(self):
        print("Product code\t Name \t Price")
        for i in range(3):
            print(self.__product_code[i],"\t\t",self.__name[i],"\t\t\t",self.__price[i])
    def generate_bill(self,qty):
        total_amount=0
        for i in range(3):
            total_amount= total_amount+self.__price[i]*qty[i]
        print("\t\t###### BILL #######")
        print("Code \t Name\t Price \t Qty \t Subtotal")
        for i in range(3):
            print(self.__product_code[i],"\t",self.__name[i],"\t\t",self.__price[i],"\t",qty[i],"\t",self.__price[i]*qty[i])
        print("----------------------------------------------------")
        print("Total = ",total_amount)
        
s=STORE()
s.input_data()
s.display_data()
qty=[]
for i in range(3):
    print("Enter the quantity for each product")
    qty.append(int(input()))
               
s.generate_bill(qty)
