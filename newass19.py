
class store:
    product_code=[]
    name =[]
    price=[]
    
    def getdata(self):
        for i in range (2):
            self.product_code.append(int(input("enetr code of product")))
            self.name.append(input("enter name of product"))
            self.price.append(int(input("enter price of product")))

    def final_bill(self,qty):
        total_amount=0
        for i in range(2):
            total_amount=total_amount+(self.price[i]*qty[i])
        print("\t\t###### BILL #######")
        print("Code \t Name\t Price \t Qty \t Subtotal")
        for i in range(2):
            print(self.product_code[i],"\t",self.name[i],"\t\t",self.price[i],"\t",qty[i],"\t",self.price[i]*qty[i])
        print("----------------------------------------------------")
        print("Total = ",total_amount)
    def displaydata(self):
        print("product cost\tproduct name\t product price\t product quontity")
        for i in range(2):
            print(self.product_code[i],"\t",self.name[i],"\t",self.price[i])
s=store()
s.getdata()
s.displaydata()
qty=[]
for i in range(2):
    print("Enter the quantity for each product")
    qty.append(int(input("enter  qountity %d for product")))
    
               
s.final_bill(qty)
            
