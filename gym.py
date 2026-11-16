from member import Member
from membership import Membership
from payment import Payment

class Gym:
    """Manages the gym membership system."""

    def __init__(self, gym_name):
        self.gym_name = gym_name
        self.members = []
        self.memberships = []
        self.payments = []

    def add_member(self, member):
        """Add a new member to the gym."""
        self.members.append(member)
        print("Member added successfully!")

    def display_members(self):
        """Display all registered gym members."""
        if not self.members:
            print("No members registered yet.")
        else:
            for member in self.members:
                member.display_member()

    def search_member(self, member_id):
        """Search for a member using their ID."""
        for member in self.members:
            if member.get_member_id() == member_id:
                member.display_member()
                return member
        
        print("Member not found.")
        return None

    def remove_member(self, member_id):
        """Remove a member using their ID."""
        for member in self.members:
            if member.get_member_id() == member_id:
                self.members.remove(member)
                print("Member removed successfully!")
                return

        print("Member not found.")

    def add_membership(self, membership):
        """Add a membership plan to the gym."""
        self.memberships.append(membership)
        print("Membership plan added successfully!")

    def record_payment(self, payment):
        """Record a gym membership payment."""
        self.payments.append(payment)
        print("Payment recorded successfully!")

    def save_members(self):
        """Save all gym members to a text file."""
        try:
            with open("members.txt", "w") as file:
                for member in self.members:
                    file.write(
                        f"{member.member_id},{member.name},"
                        f"{member.age},{member.phone}\n"
                    )

            print("Members saved successfully!")

        except OSError as error:
            print("Error saving members:", error)

    def load_members(self):
        """Load gym members from a text file."""
        try:
            with open("members.txt", "r") as file:
                self.members = []

                for line in file:
                    member_id, name, age, phone = line.strip().split(",")

                    member = Member(
                        member_id, name, int(age), phone
                    )

                    self.members.append(member)

            print("Members loaded successfully!")

        except FileNotFoundError:
            print("No saved members file found.")

        except (ValueError, OSError) as error:
            print("Error loading members:", error)