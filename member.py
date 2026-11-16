class Member: # creates a class called member
    # Represents a gym member.

    def __init__(self, member_id, name, age, phone):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.phone = phone

    def display_member(self):
        # Display the member's information.
        print("\n--- Member Information ---")
        print("ID:", self.member_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)

    def update_phone(self, new_phone):
        # Update the member's phone number.
        self.phone = new_phone
        print("Phone number updated successfully.")

    def get_member_id(self):
        # Return the member's ID.
        return self.member_id

    def get_member_name(self):
        # Return the member's name.
        return self.name
        