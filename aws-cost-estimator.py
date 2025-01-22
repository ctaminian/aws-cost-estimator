import sys
from pricing import PRICING

session_costs = {
    "EC2": 0.00,
    "S3": 0.00,
    "RDS": 0.00,
}

def main():
    while True:
        load_menu()

def load_menu():
    print("---------------------------------------------------")
    print("---------------AWS Price Estimator-----------------")
    print("---------------------------------------------------")
    print("Which service would you like to estimate costs for?")
    print("1. EC2")
    print("2. S3")
    print("3. RDS")
    print("4. View Cost Summary")
    print("5. Exit Program")

    try:
        choice = int(input("Please enter your choice (e.g., 1 for EC2): "))
    except ValueError:
        print("Invalid input! Please enter a number (e.g., 2 for S3).")
        return

    match choice:
        case 1:
            estimate_ec2()
        case 2:
            estimate_s3()
        case 3:
            estimate_rds()
        case 4:
            view_summary()
        case 5:
            confirm_exit()   
        case _:
            print("Invalid choice! Please select a valid option.")

def confirm_exit():
    confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()

    if confirm == "y":
        print("\nExiting program.")
        print("Thank you for using the AWS price estimator.\n")
        sys.exit()
    else:
        print("\nReturning to the main menu...\n")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def view_summary():
    total_aws_costs = 0
    print("\n----------------------------")
    print(f"AWS Cost Summary:")
    for item in session_costs:
        total_aws_costs += session_costs[item]
        print(f"- {item}: ${session_costs[item]:.2f}")
    print("----------------------------")
    print(f"Total: ${total_aws_costs:.2f}\n")

def estimate_ec2():
    print("You chose EC2.")

    for i, instance in enumerate(PRICING["EC2"], 1):
        print(f"{i}. {instance}")

    try:
        choice = int(input("Please select your EC2 instance from the list above (e.g., 1 for t2.micro): "))
        if choice not in range(1, len(PRICING["EC2"]) + 1):
            print("Invalid choice! Please select a valid option.")
            return
    except ValueError:
        print("Invalid input! Please enter a number (e.g., 2 for t3.micro).")
        return

    instance_name = list(PRICING["EC2"].keys())[choice - 1]
    ec2_price = PRICING["EC2"][instance_name]
    print(f"You selected {instance_name}")

    hours = get_positive_int("How many hours per day will the instance run? ")
    days = get_positive_int("How many days per week? ")
    weeks = get_positive_int("For how many weeks? ")

    total_hours = hours * days * weeks
    total_ec2_cost = total_hours * ec2_price

    session_costs["EC2"] += total_ec2_cost

    print("\n----------------------------")
    print(f"EC2 Cost Breakdown:")
    print(f"- Instance: {instance_name}")
    print(f"- Total Hours: {total_hours}")
    print(f"- Hourly Rate: ${ec2_price}")
    print(f"Total Estimated Cost: ${total_ec2_cost:.2f}")
    print("----------------------------\n")

def estimate_s3():
    print("You chose S3.")

    storage = get_positive_int("How much data (in GB) will you store in S3 per month? ")
    transfer = get_positive_int("How much data (in GB) will you transfer using S3 per month? ")
    storage_cost = storage * PRICING["S3"]["storage_per_gb"]
    transfer_cost = transfer * PRICING["S3"]["data_transfer_out_per_gb"]
    total_s3_cost = storage_cost + transfer_cost

    session_costs["S3"] += total_s3_cost

    print("\n----------------------------")
    print("S3 Cost Breakdown:")
    print(f"- Storage Amount: {storage}GB")    
    print(f"- Storage Cost: ${storage_cost:.2f}")
    print(f"- Transfer Amount: {transfer}GB")   
    print(f"- Data Transfer Cost: ${transfer_cost:.2f}")
    print(f"Total Estimated Cost: ${total_s3_cost:.2f}")
    print("----------------------------\n")

def estimate_rds():
    print("You chose RDS.")
    print("Available database engines:")

    for i, engine in enumerate(PRICING["RDS"].keys(), 1):
        print(f"{i}. {engine}")

    engine_choice = get_positive_int("Select a database engine (e.g. 1 for MySQL): ")
    while engine_choice not in range(1, len(PRICING["RDS"].keys()) + 1):
        print("Invalid choice! Please select a valid option.")
        engine_choice = get_positive_int("Select a database engine (e.g. 1 for MySQL): ")

    selected_engine = list(PRICING["RDS"].keys())[engine_choice - 1]
    print(f"You selected {selected_engine}. Available instance types:")

    for i, instance in enumerate(PRICING["RDS"][selected_engine], 1):
        print(f"{i}. {instance}")

    instance_choice = get_positive_int("Select an instance type (e.g. 1 for db.t3.micro): ")
    while instance_choice not in range(1, len(PRICING["RDS"][selected_engine].keys()) + 1):
        print("Invalid choice! Please select a valid option.")
        instance_choice = get_positive_int("Select an instance type (e.g. 1 for db.t3.micro): ")

    selected_instance = list(PRICING["RDS"][selected_engine].keys())[instance_choice - 1]
    print(f"You selected {selected_instance}")

    db_price = PRICING["RDS"][selected_engine][selected_instance]

    hours = get_positive_int("How many hours per day will the instance run? ")
    days = get_positive_int("How many days per week? ")
    weeks = get_positive_int("For how many weeks? ")

    total_hours = hours * days * weeks
    total_db_cost = total_hours * db_price

    session_costs["RDS"] += total_db_cost

    print("\n----------------------------")
    print(f"RDS Cost Breakdown:")
    print(f"- Engine: {selected_engine}")
    print(f"- Instance: {selected_instance}")
    print(f"- Total Hours: {total_hours}")
    print(f"- Hourly Rate: ${db_price}")
    print(f"Total Estimated Cost: ${total_db_cost:.2f}")
    print("----------------------------\n")

if __name__ == "__main__":
    main()