class Payment:
    # Represents a gym membership payment.

    def __init__(self, payment_id, member_id, amount):
        # Initialise payment information
        self.payment_id = payment_id
        self.member_id = member_id
        self.amount = amount
        self.status = "Unpaid"

    def display_payment(self):
        # Display payment information
        print("Payment ID:", self.payment_id)
        print("Member ID:", self.member_id)
        print("Amount:", self.amount)
        print("Status:", self.status)

    def mark_as_paid(self):
        # Change payment status to Paid
        self.status = "Paid"
        print("Payment successfully marked as paid. ")

    def get_amount(self):
        # Return payment amount
        return self.amount

    def get_status(self):
        # Return payment status
        return self.status