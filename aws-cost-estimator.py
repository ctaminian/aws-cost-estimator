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

def estimate_ec2():
    print("You chose EC2.")

def estimate_s3():
    print("You chose S3.")

if __name__ == "__main__":
    main()