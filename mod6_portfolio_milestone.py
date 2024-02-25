class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        
    def updateValues(self):
        self.item_name = input("Enter the item name:\n")
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
        self.cart_items.append(item.item_name)
##    ###    ###### above it is .item_name to see if it was actually printing an object with attrubtes from the ITEMtoPurchase Class
        ##DELETE PRINT
        print(self.cart_items)

    def remove_item(self, ItemToRemove):
        if (ItemToRemove in self.cart_items) == False:
            print("Item not found in cart. Nothing removed.")
        else:
            self.cart_items.remove(ItemToRemove)
            ##DELETE PRINT
            print(self.cart_items)

    def modify_item(self, item: ItemToPurchase):
        print("hi")
        if item in self.cart_items:
            if (ItemToPurchase.item_name == "none") and (ItemToPurchase.item_price == 0) and (ItemToPurchase.item_quantity == 0):
                item.updateValues()    
        else:
            print("Item not found in cart. Nothing removed.")

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


    item1 = ShoppingCart("David", "2024")
    print("add item:")
    item1.add_item(item1)
    item1.modify_item(item1)

if __name__ == "__main__":
    main()

            
