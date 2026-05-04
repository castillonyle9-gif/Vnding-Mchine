import random  # For random suggestions

class Item:
    def __init__(self, name, price, stock, category, code):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.code = code
    
    def is_in_stock(self):
        return self.stock > 0
    
    def reduce_stock(self):
        if self.is_in_stock():
            self.stock -= 1
            return True
        return False

class VendingMachine:
    def __init__(self):
        self.items = [
            Item("Coffee", 2.50, 5, "Hot Drinks", 1),
            Item("Tea", 2.00, 3, "Hot Drinks", 2),
            Item("Cola", 1.50, 4, "Cold Drinks", 3),
            Item("Water", 1.00, 10, "Cold Drinks", 4),
            Item("Chocolate Bar", 1.20, 6, "Sweet Snacks", 5),
            Item("Biscuits", 1.80, 7, "Sweet Snacks", 6),
            Item("Crisps", 1.30, 8, "Savory Snacks", 7),
            Item("Nuts", 2.20, 4, "Savory Snacks", 8),
            Item("Sandwich", 3.00, 2, "Savory Snacks", 9),
            Item("Fruit Juice", 2.00, 5, "Cold Drinks", 10)
        ]
        self.categories = {
            "Hot Drinks": [item for item in self.items if item.category == "Hot Drinks"],
            "Cold Drinks": [item for item in self.items if item.category == "Cold Drinks"],
            "Sweet Snacks": [item for item in self.items if item.category == "Sweet Snacks"],
            "Savory Snacks": [item for item in self.items if item.category == "Savory Snacks"]
        }
    
    def display_menu(self):
        print("\n--- Vending Machine Menu ---")
        for category, items in self.categories.items():
            print(f"\n{category}:")
            for item in items:
                print(f"  {item.code}. {item.name} - £{item.price:.2f} (Stock: {item.stock})")
    
    def get_item_by_code(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None
    
    def select_item(self):
        while True:
            try:
                code = int(input("\nEnter item code: "))
                item = self.get_item_by_code(code)
                if item and item.is_in_stock():
                    return item
                elif item and not item.is_in_stock():
                    print("Sorry, that item is out of stock.")
                else:
                    print("Invalid code. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def insert_money(self, item):
        while True:
            try:
                money = float(input(f"Insert money (item costs £{item.price:.2f}): £"))
                if money >= item.price:
                    return money
                else:
                    print("Insufficient funds. Please insert more money.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
    
    def dispense(self, item):
        if item.reduce_stock():
            print(f"\n{item.name} dispensed! Enjoy your purchase.")
    
    def calculate_change(self, money, price):
        change = money - price
        print(f"Change returned: £{change:.2f}")
        return change
    
    def suggest_item(self, purchased_item):
        # Suggest from same or complementary category
        category = purchased_item.category
        if category == "Hot Drinks":
            suggestions = [item for item in self.items if item.category in ["Sweet Snacks", "Savory Snacks"] and item.is_in_stock()]
        else:
            suggestions = [item for item in self.items if item.category != category and item.is_in_stock()]
        if suggestions:
            suggestion = random.choice(suggestions)
            print(f"Suggestion: Try {suggestion.name} (£{suggestion.price:.2f}) with your {purchased_item.name}?")
    
    def run(self):
        print("Welcome to the Vending Machine!")
        while True:
            self.display_menu()
            item = self.select_item()
            money = self.insert_money(item)
            self.dispense(item)
            self.calculate_change(money, item.price)
            self.suggest_item(item)
            more = input("\nBuy another item? (y/n): ").lower()
            if more != 'y':
                print("Thank you for using the Vending Machine!")
                break

# Main execution
if __name__ == "__main__":
    vm = VendingMachine()
    vm.run()
