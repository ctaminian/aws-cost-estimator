import sys
from pricing import PRICING

def main():
    load_menu()

def load_menu():
    while True:
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
            continue

        match choice:
            case 1:
                estimate_ec2()
                break
            case 2:
                estimate_s3()
                break
            case 3:
                print("Exiting program.")
                print("Thank you for using the AWS price estimator.")
                sys.exit()
            case _:
                print("Invalid choice! Please select a valid option.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
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
    print(f"Your instance will run for a total of {total_hours} hours at a rate of ${ec2_price:.4f} / hour")
    print(f"Your total cost is estimated to be: ${total_hours * ec2_price:.2f}")

def estimate_s3():
    print("You chose S3.")

if __name__ == "__main__":
    main()