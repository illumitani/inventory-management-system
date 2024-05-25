# Defining inventory as a dictionary with product ID as keys and details as values
inventory = {}

# To add a new product to the inventory
def add_product(product_id, name, quantity, price):
    if not isinstance(quantity, int) or not isinstance(price, float): #isinstance is used to match the object and its type
        print("Please enter correct values. Quantity must be an integer and price must be a float.")
        return
    if product_id not in inventory:
        inventory[product_id] = {'name': name, 'quantity': quantity, 'price': price}
        print("Product added successfully!")
    else:
        print("This product already exists. You can update the existing product by entering 2 from the menu")

# To update the quantity of an existing product
def update_quantity(product_id, new_quantity):
    if product_id in inventory:
        if not isinstance(new_quantity, int):
            print("Please enter correct values. Quantity must be an integer.")
            return
        inventory[product_id]['quantity'] += new_quantity
        print("Quantity updated successfully!")
    else:
        print("Product ID does not exist!")

#To display the current inventory status
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory Status:")
        print(f"| {'Product ID':<10} | {'Name':<20} | {'Quantity':<10} | {'Price':<10} |")
        print("-" * 60)
        for product_id, details in inventory.items():
            print(f"| {product_id:<10} | {details['name']:<20} | {details['quantity']:<10} | ${details['price']:<9.2f} |") #The numbers like 10, 20, and 60  are used to specify the minimum width of each column in characters. 
        print("-" * 60)

# To generate a report showing the total value of the inventory
def generate_report():
    total_value = 0
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory Report:")
        for details in inventory.values():
            total_value += details['quantity'] * details['price']
        print(f"Total Inventory Value: ${total_value}")

# Main function to drive the program
def main():
    while True:
        print("This is the main menu for the inventory management system, Click the number associated to perform the specific task \n1. Add Product\n2. Update Quantity\n3. Display Inventory\n4. Generate Report\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            add_product(product_id, name, quantity, price)
        elif choice == '2':
            product_id = input("Enter Product ID: ")
            new_quantity = int(input("Enter Quantity to add: "))
            update_quantity(product_id, new_quantity)
        elif choice == '3':
            display_inventory()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("You are sucessfully exited from the inventory mangement system")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
