class Membership:
    # Manages gym membership plans.

    def __init__(self, plan_name, duration, price):
        self.plan_name = plan_name
        self.duration = duration
        self.price = price

    def display_plan(self):
        # Display the plan name, duration and price
        print("Plan:", self.plan_name)
        print("Duration:", self.duration)
        print("Price:", self.price)

    def update_price(self, new_price):
        # Update the membership price
        self.price = new_price

    def get_price(self):
        # Return the membership price
        return self.price

    def get_duration(self):
        # Return the membership duration
        return self.duration