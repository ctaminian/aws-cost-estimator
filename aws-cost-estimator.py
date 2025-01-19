import sys
from pricing import PRICING

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
    print("3. Exit Program")

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
    print(f"\nYour instance will run for a total of {total_hours} hours at a rate of ${ec2_price} / hour")
    print(f"Your total cost is estimated to be: ${total_hours * ec2_price:.2f}\n")

def estimate_s3():
    print("You chose S3.")

    storage = get_positive_int("How much data (in GB) will you store in S3 per month? ")
    transfer = get_positive_int("How much data (in GB) will you transfer using S3 per month? ")
    storage_cost = storage * PRICING["S3"]["storage_per_gb"]
    transfer_cost = transfer * PRICING["S3"]["data_transfer_out_per_gb"]
    total_s3_cost = storage_cost + transfer_cost

    print("\nS3 Monthly Cost Breakdown:")
    print(f"- Storage Cost: ${storage_cost:.2f}")
    print(f"- Data Transfer Cost: ${transfer_cost:.2f}")
    print(f"Total Estimated Monthly Cost: ${total_s3_cost:.2f}\n")

if __name__ == "__main__":
    main()