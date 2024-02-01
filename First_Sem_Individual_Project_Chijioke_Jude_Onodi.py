# Creating a function that calculates total sales for the day:
def total_sales_day(morning_sales, evening_sales):
    return morning_sales + evening_sales


# Creating a function that calculates Worker's Salary:
def workers_salary(hourly_rate, hours_worked):
    return hours_worked * hourly_rate


# Creating a function that calculates Profit:
def calculate_profit(sales, costs):
    total_sales = sum(sales)
    total_cost = sum(costs)
    return total_sales - total_cost


# Creating a function that calculates tips for a shift:
def shift_tips(shift_sales):
    return shift_sales * 0.02


# Creating a function that calculates Total tips for a Day:
def total_tips(morning_sales, evening_sales):
    return shift_tips(morning_sales) + shift_tips(evening_sales)



# Main program
# Creating a user-friendly interface with all available operations:
def display_menu():
    print("Welcome to the Sales Management System!")
    print("Please select an operation:")
    print("1. Calculate Total Sales for the Day")
    print("2. Calculate Worker's Salary")
    print("3. Calculate Profit")
    print("4. Calculate Tips for a Shift")
    print("5. Calculate Total Tips for the Day")
    print("6. Exit")
    
display_menu()
    
while True: # To create an infinite loop
    choice = input('Enter a number of your choice (1-6): ')
    if choice == '1':  # Calculating the total sales for the day
        try: # Testing the block of code for errors
            morning_sales = float(input("Enter morning sales: "))
            evening_sales = float(input("Enter evening sales: "))
        except ValueError: # Handles the error
            print("Please, Enter a valid number")
            continue
        total_sales = total_sales_day(morning_sales, evening_sales)
        print(f"Total sales for the day: ${total_sales:.2f}")
    elif choice == '2':
        try:
            hourly_rate = float(input("Enter hourly rate: "))
            hours_worked = float(input("Enter hours worked: "))
        except ValueError:
            print("Please, Enter a valid number")
        salary_worker = workers_salary(hourly_rate, hours_worked)
        print(f"Worker's salary: ${salary_worker:.2f}")
    elif choice == '3':
        sales = []
        costs = []
        try:
            num_items = int(input("Enter the number of items sold: "))
            for i in range(num_items):
                sales.append(float(input(f"Enter the price of item {i+1}: ")))
                costs.append(float(input(f"Enter the cost of item {i+1}: ")))
        except ValueError:
            print("Please, Enter a valid number")
        profit = calculate_profit(sales, costs)
        if profit >= 0:
            print(f"Profit: ${profit:.2f}")
        else:
            print(f"Loss: ${-profit:.2f}")
    elif choice == '4':
        try:
            shift_sales = float(input("Enter shift sales: "))
        except ValueError:
            print("Please, Enter a valid number")
            continue
        tips_shift = shift_tips(shift_sales)
        print(f"Tips for the shift: ${tips_shift:.2f}")
    elif choice == '5':
        try:
            morning_sales = float(input("Enter morning sales: "))
            evening_sales = float(input("Enter evening sales: "))
        except ValueError:
            print("Please, Enter a valid number")
            continue
        tips_total = total_tips(morning_sales, evening_sales)
        print(f"Total tips for the day: ${tips_total:.2f}")
    elif choice == '6':
        print("Thank you for using the Sales Management System!")
        break
    else:
        print("Invalid choice. Please try again.")