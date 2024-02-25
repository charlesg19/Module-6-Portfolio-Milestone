class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0
        
    def updateValues(self):
        self.item_name = input("Enter the item name:\n")
        self.item_description = input("Enter the item description:\n")
        self.item_price = float(input("Enter the item price:\n"))
        self.item_quantity = int(input("Enter the item quantity:\n"))
        
    def print_item_cost(self):
        print(self.item_name, end=" ")
        print(self.item_quantity, end=" ")
        print("@ ${:.2f}".format(self.item_price), end=" ")
        self.total = self.item_price * self.item_quantity
        print("= ${:.2f}".format(self.total))
        
class ShoppingCart:
    def __init__(self, customer_name, current_date):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []

    def add_item(self, item: ItemToPurchase):
        ItemToPurchase.updateValues(item)
        self.cart_items.append(item)
        print(self.cart_items)
        print(item.item_price)

    def remove_item(self, ItemToRemove):
        if (ItemToRemove in self.cart_items) == False:
            print("Item not found in cart. Nothing removed.")
        else:
            self.cart_items.remove(ItemToRemove)
            ##print(self.cart_items)

    def modify_item(self, item: ItemToPurchase):
        if item in self.cart_items:
            if (item.item_name == "none") and (item_description == "none") and (item.item_price == 0) and (item.item_quantity == 0):
                item.updateValues()    
        else:
            print("Item not found in cart. Nothing removed.")

    def get_num_items_in_cart(self):
        print(len(self.cart_items) + 1)

    def get_cost_of_cart(self):
        if (items in self.cart_items) == True:
            for items in self.cart_items:
                total += items.item_price()
            print("$", total)
        else:
            print("SHOPPING CART IS EMPTY")

    def print_total(self):
        print(self.cart_items, "finish later")

    def print_description(self):
        for items in self.cart_items:
            print(item.item_description)

def main():
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    count = 1
    for x in (item1, item2):
        print("  --ITEM #{}--  ".format(count))
        x.updateValues()
        count +=1
    
    print ("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    items_cost_sum = item1.total + item2.total
    print("Total: ${:.2f}".format(items_cost_sum))

    shopping_cart_item = ShoppingCart(input("Enter Name:"), input("Enter Date:"))

    def print_menu(x):
        print("""MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit""")
        selection = input("Choose an option:")
        while selection != "q":
            if selection == "a":
                x.add_item(item1)

            elif selection == "r":
                x.remove_item(item1)

            elif selection == "c":
                x.get_num_items_in_cart()

            elif selection == "i":
                x.print_description()

            elif selection == "o":
                x.print_total()

            else:
                print("eneter a good selectioioion")

            selection = input("Choose an option:")

        
            

    print_menu(shopping_cart_item)
        
        

if __name__ == "__main__":
    main()

            
