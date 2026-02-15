"""
This project is developed using the concepts of Object-Oriented Programming (OOP) 
and Inheritance in Python.

The system is designed for a Car Accessories Store to manage stock items.
It allows the user to:

• Add and manage stock quantity
• Sell stock with validation rules
• Update product price
• Calculate price including VAT
• Generate invoice-style output

The project demonstrates the use of:
• Classes and Objects
• Encapsulation (private variables)
• Inheritance
• Method Overriding
• Constructors
• Getter and Setter methods
"""

class StockItem:
    #stock category name
    stock_category="Car accessories"

    def __init__(self,stock_code,quantity,price):
        self.__stock_code=stock_code
        self.__stock_quantity=quantity
        self.__stock_price=price

    #Setter method
    # set price doesn't includes VAT
    def setPrice(self,price):
        self.__stock_price=price

    # here basically we have increased the number of stock as it should be between 1 and 100
    def increaseStock(self,quantity_amount):
        if quantity_amount < 1 :
            print("The error was: Increased amount must be greater than or Equal to one.")
        elif self.__stock_quantity + quantity_amount > 100:
            print("The error was: Stock cannot exceed 100.")
        else:
            self.__stock_quantity += quantity_amount

    # here we are selling the stock as we also have some criterias to check if that doesn't meet error will be generated
    def sellStock(self,quantity_amount):
        if quantity_amount < 1:
            print("The error was: Selling item must be greater than 1")
        elif quantity_amount >self.__stock_quantity:
            print("The error was: Selling amount must be less than the stock amount ")
            return False
        else:
            self.__stock_quantity -= quantity_amount
            return True


    #Getter method
    #here is the stock code
    def getStockCode(self):
        return self.__stock_code


    #here is the stock quantity
    def getStockQuantity(self):
        return self.__stock_quantity

    #here is the stock price without VAT
    def getStockPrice(self):
        return self.__stock_price

    # VAT percentage
    def getVAT(self):
        return 17.5

    #the getter price should include VAT
    def getStockPriceWithVAT(self):
        Final_Price=self.__stock_price + (self.__stock_price * self.getVAT() / 100)
        return Final_Price

    # the stock name as per the question
    def getStockName(self):
        return "Unknown Stock Name"

    # the stock description
    def getStockDescription(self):
        return "Unknown Stock Description"


    #PRINTING THE DETAILS
    def __str__(self):
        return (f"-----------------------------------------------------------------------------------------------------\n"
                f"\tLondon Best Car Accessories Store\n"
                f"\t   123, Baker Street, London\n"
                f"-----------------------------------------------------------------------------------------------------\n"
                f"                   INVOICE              \n"
                f"-----------------------------------------------------------------------------------------------------\n"
                f"\tStock Category: {StockItem.stock_category}\n\n"
                f"\t * Stock Type: {self.getStockName()}\n"
                f"\t * Description: {self.getStockDescription()}\n"
                f"\t * Stock Code: {self.__stock_code}\n"
                f"-----------------------------------------------------------------------------------------------------\n"
                f"\t1. Price Without VAT: {self.getStockPrice():.2f}\n"
                f"\t2. Price With VAT(17.5%): {self.getStockPriceWithVAT():.2f}\n"
                f"\t3. Total unit in stock: {self.__stock_quantity}\n")

# Creating the child class class
class NavSys(StockItem):
    def __init__(self,stock_code,quantity,price,brand):
        super().__init__(stock_code,quantity,price)
        self.__brand=brand

    def getStockName(self):
        return "Navigation System"
    def getStockDescription(self):
        return "GeoVision Sat Nav"

    def __str__(self):
        return super().__str__() + f"\t4. Brand: {self.__brand}\n"

#testing the code
show=input("Which one You want to edit:\n1.Stock Item \n2.Navigation System\n")
if show=='1':
  ask=input("Want to make any changes in the Stock (Y/N)? ")
  ask_new=ask.upper()
# At first StockItem Testing
  print(f"***** StockItem Testing *****\n")
  print("** Creating a Stock with 10 units Unknown item,price 99.99 each, and item code W101\n")
  print("-"*100)
  s1=StockItem("W101",10,99.99)
  print(s1)

  #if-else is being used
  if ask_new=='Y':
    #asking to increase the stock
    increase=int(input("Increase the stock by: "))
    s1.increaseStock(increase)

    #asking to sell the stock
    decrease=int(input("Sell the stock by: "))
    s1.sellStock(decrease)

    #setting the new price
    new=int(input("Enter the new price of the product: "))
    s1.setPrice(new)
    print(s1)
elif show=='2':
  ask2=input("Want to make change in the Navigation System (Y/N): ")
  ask2_new=ask2.lower()


  #another testing
  print(f"\n----- Navigation System Goods With the Brand -----\n\n")
  print("-"*100)
  print("** Creating a stock with 10 units Navigation system, price 99.99, item code NS101, and brand TomTom")
  print("-"*100)
  n1=NavSys("NS101",10,99.99,"TomTom")
  print("** Printing item stock Information\n")
  print(n1)
  if ask2_new=='y':
    #Increasing the Stock By 10
    inc=int(input("Enter the amount of stock you want to increase by: "))
    n1.increaseStock(inc)

    #Selling the stock
    sell=int(input("Enter the amount of stock you want to sell: "))
    n1.sellStock(sell)

    #Setting the new price to 100.99
    pp=int(input("enter the new price you want to keep for the product: "))
    n1.setPrice(pp)
    print(n1)
else:
  print("Sorry no other options left!!! ")