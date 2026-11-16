from gym import Gym
from member import Member

# Create the gym
gym = Gym("My Gym")

# Load previously saved members
gym.load_members()

# Main menu
while True:
    print("================================")
    print("   GYM MEMBERSHIP MANAGEMENT")
    print("================================")

    print("1. Add a new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Remove a member")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

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

    # Option 5: Save and exit
    elif choice == "5":
        gym.save_members()
        print("Thank you for using My Gym!")
        break

    # Invalid menu choice
    else:
        print("Invalid choice. Please select a number from 1 to 5.")