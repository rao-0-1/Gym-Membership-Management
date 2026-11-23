
from gym import Gym
from member import Member
from membership import Membership
from payment import Payment

# Create the gym
gym = Gym("My Gym")

# Load previously saved members
gym.load_members()

# Main menu
while True:
    print("\n================================")
    print("   GYM MEMBERSHIP MANAGEMENT")
    print("================================")
    print("1. Add a new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Remove a member")
    print("5. Add a membership plan")
    print("6. Display membership plans")
    print("7. Record a payment")
    print("8. Display all payments")
    print("9. Exit")

    choice = input("Choose an option (1-9): ")

    # Option 1: Add a member
    if choice == "1":
        member_id = input("Enter member ID: ")
        name = input("Enter member name: ")

        try:
            age = int(input("Enter member age: "))

            if age <= 0:
                print("Age must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        phone = input("Enter phone number: ")

        new_member = Member(member_id, name, age, phone)
        gym.add_member(new_member)

    # Option 2: Display members
    elif choice == "2":
        gym.display_members()

    # Option 3: Search for a member
    elif choice == "3":
        member_id = input("Enter member ID to search: ")
        gym.search_member(member_id)

    # Option 4: Remove a member
    elif choice == "4":
        member_id = input("Enter member ID to remove: ")
        gym.remove_member(member_id)

    # Option 5: Add a membership plan
    elif choice == "5":
        plan_name = input("Enter membership plan name: ")
        duration = input("Enter membership duration: ")

        try:
            price = float(input("Enter membership price: "))

            if price <= 0:
                print("Price must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid price.")
            continue

        new_membership = Membership(plan_name, duration, price)
        gym.add_membership(new_membership)

    # Option 6: Display membership plans
    elif choice == "6":
        gym.display_memberships()

    # Option 7: Record a payment
    elif choice == "7":
        payment_id = input("Enter payment ID: ")
        member_id = input("Enter member ID: ")

        try:
            amount = float(input("Enter payment amount: "))

            if amount <= 0:
                print("Payment amount must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid amount.")
            continue

        new_payment = Payment(payment_id, member_id, amount)
        gym.add_payment(new_payment)

    # Option 8: Display payments
    elif choice == "8":
        gym.display_payments()

    # Option 9: Save and exit
    elif choice == "9":
        gym.save_members()
        print("Thank you for using My Gym!")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please select a number from 1 to 9.")
