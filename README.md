# Gym Membership Management System
This is my simple python program that helps a gym keep track of its **members**, **membership plans** and **payments** from a text menu in the terminal.
My aim was to create files and add the login behind it to create a suitable gym membership program which **runs** perfectly.

## Table of Contents

1. What does this program do?
2. What you need before starting
3. Step-by-step setup
4. How the project is organised
5. How to use the program
6. How these files work together
7. Code walkthrough
   - [member.py](#1-memberpy--who-is-a-member)
   - [membership.py](#2-membershippy--what-plans-exist)
   - [payment.py](#3-paymentpy--who-paid-what)
   - [gym.py](#4-gympy--the-manager)
   - [main.py](#5-mainpy--the-menu-you-interact-with)
   - [members.txt](#6-memberstxt--the-saved-data)
8. Some things which are lacking
9. How I can make it better

## What does my program do?

What if you wanted to run a small gym and keep everything in a notebook? basically this program is designed in a way which replaces that notebook. With it you can:

 **Add** new members (ID, name, age, phone number)
 **See** every member in a go
 **Search** for one member using their ID
 **Remove** a member in the gym
 **Create membership plans** (for example: "Monthly", "1 month", £30)
 **Record payments** made by members
 **Save** your members to a file when you leave, and **load** them back when you return

## What you need before starting
 **Python** Version 3.6 or above that  
 **coding workspaces**  VS Code, PyCharm anything you like 
 **A terminal**  not sure about you but I use Terminal on MacBook

## My Step-by-step setup
### Step 1: Create a project folder
Make a new folder anywhere on your computer, for example `gym_project`.
### Step 2: Create the Python files
Inside that folder, create these **five** files. The names matter, because the files import each other by name.

```
gym_project/
├── main.py
├── gym.py
├── member.py
├── membership.py
├── payment.py
└── members.txt      (optional, the program creates it for you)
```

### Step 3: Paste the code into each file

Copy each piece of code into the file with the matching name.

### Step 4: Check your indentation

During the creation of my files I faced a lot of indentation errors and syntax errors as well so make sure of that.

### Step 5: Check your quote marks

Like I mentioned in the step before that quotation like ' or " matters so take care of that or syntax error will occur.
### Step 6: Run it

Open your terminal, move into the folder, and start the program:

```bash
cd gym_project
python main.py
```
You should see the menu appear.

---

## How the project is organised

Each file has **one job**

| File | Its job | Real-life comparison |
|---|---|---|
| `member.py` | Describes what a *member* is | A membership card |
| `membership.py` | Describes what a *membership plan* is | A price list on the wall |
| `payment.py` | Describes what a *payment* is | A receipt |
| `gym.py` | Holds and manages all of the above | The gym manager / reception desk |
| `main.py` | The menu the user sees and uses | The front desk conversation |
| `members.txt` | Stores saved members between runs | The filing cabinet |

---

## How to use the program

When you run `main.py`, you'll see this menu:

```
================================
 GYM MEMBERSHIP MANAGEMENT
================================
1. Add a new member
2. Display all members
3. Search for a member
4. Remove a member
5. Add a membership plan
6. Display membership plans
7. Record a payment
8. Display all payments
9. Exit
Choose an option (1-9):
```

Type a number and press **Enter**.

### Example session

**Adding a member (option 1):**
```
Choose an option (1-9): 1
Enter member ID: 1234
Enter member name: john
Enter member age: 20
Enter phone number: 9887
Member added successfully!
```

**Searching (option 3):**
```
Choose an option (1-9): 3
Enter member ID to search: 1234

--- Member Information ---
ID: 1234
Name: john
Age: 20
Phone: 9887
```

**Adding a plan (option 5):**
```
Enter membership plan name: Monthly
Enter membership duration: 1 month
Enter membership price: 30
Membership plan added successfully!
```

**Recording a payment (option 7):**
```
Enter payment ID: P001
Enter member ID: 1234
Enter payment amount: 30
Payment recorded successfully!
```

**Exiting (option 9):** saves your members to `members.txt` and closes the program, and make sure to save before you leave the program.
---

## The big picture: how the files work together

```
                    ┌────────────┐
                    │  main.py   │   ← type here
                    └─────┬──────┘
                          │ creates & uses
                    ┌─────▼──────┐
                    │   gym.py   │   ← the manager
                    └─┬────┬───┬─┘
         keeps a list │    │   │ keeps a list
          of members  │    │   │ of payments
           ┌──────────▼┐ ┌─▼───▼─────┐ ┌─────────────┐
           │ member.py │ │membership │ │ payment.py  │
           └───────────┘ │   .py     │ └─────────────┘
                         └───────────┘

                    gym.py  ⇄  members.txt   (save / load)
```

To further explain this so basically `main.py` shows the menu like when you pick an option, it asks the `Gym` object to do the work. The `Gym` keeps three lists members, plans, and payments made up of `Member`, `Membership` and `Payment` objects.

---

## Code walkthrough, file by file

some keywords which were worth it for me to remember:

- **Class**: a blueprint for making things. `Member` is the blueprint; "John, age 20" is one thing made from it.
- **Object**: one actual thing made from a class.
- **`self`**: the object talking about *itself*. Inside `Member`, `self.name` means "*this* member's name".
- **`__init__`**: a special method that runs automatically when a new object is created. It sets the object up.
- **Method**: a function that belongs to a class.
- **List**: a collection of items, like `[member1, member2, member3]`.

---

### 1. `member.py`: Who is a member?

```python
class Member:
    # Represents a gym member.
```
**What this does:** Creates a blueprint called `Member`. Any time the gym signs up a person, we make one `Member` object from this blueprint. Lines starting with `#` are **comments**: notes for humans that Python ignores.

```python
    def __init__(self, member_id, name, age, phone):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.phone = phone
```
**What this does:** This is the **constructor**. When you write `Member("1234", "john", 20, "9887")`, Python runs this method. It takes the four pieces of information and stores each one on the object using `self.`. After this, the member "remembers" their ID, name, age and phone.

```python
    def display_member(self):
        # Display the member's information.
        print("\n--- Member Information ---")
        print("ID:", self.member_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)
```
**What this does:** Prints the member's details neatly on screen. The `\n` at the start of the first line means "start a new line", which adds a blank gap so output isn't squashed together.

```python
    def update_phone(self, new_phone):
        # Update the member's phone number.
        self.phone = new_phone
        print("Phone number updated successfully.")
```
**What this does:** Replaces the old phone number with a new one. (This method exists and works, but there's no menu option for it yet. See [Ideas](#-ideas-for-making-it-better).)

```python
    def get_member_id(self):
        # Return the member's ID.
        return self.member_id

    def get_member_name(self):
        # Return the member's name.
        return self.name
```
**What these do:** These are called **getters**. They simply hand back a stored value. `get_member_id()` is used by `Gym` when searching or removing members, so it can compare IDs.

---

### 2. `membership.py`: What plans exist?

```python
class Membership:
    # Manages gym membership plans.

    def __init__(self, plan_name, duration, price):
        self.plan_name = plan_name
        self.duration = duration
        self.price = price
```
**What this does:** Defines a membership plan with three things: its **name** (e.g. "Gold"), **duration** (e.g. "3 months") and **price** (e.g. `75.0`). Duration is stored as text so you can write whatever suits you.

```python
    def display_plan(self):
        # Display the plan name, duration and price
        print("Plan:", self.plan_name)
        print("Duration:", self.duration)
        print("Price:", self.price)
```
**What this does:** Prints the plan on screen.

```python
    def update_price(self, new_price):
        # Update the membership price
        self.price = new_price

    def get_price(self):
        # Return the membership price
        return self.price

    def get_duration(self):
        # Return the membership duration
        return self.duration
```
**What these do:** `update_price` changes the price (handy for price rises). `get_price` and `get_duration` hand back the stored values for use elsewhere.

---

### 3. `payment.py`: Who paid what?

```python
class Payment:
    # Represents a gym membership payment.

    def __init__(self, payment_id, member_id, amount):
        # Initialise payment information
        self.payment_id = payment_id
        self.member_id = member_id
        self.amount = amount
        self.status = "Unpaid"
```
**What this does:** Creates a payment record with a unique **payment ID**, the **member ID** it belongs to, and the **amount**. Notice that `status` isn't passed in. Every new payment automatically starts as `"Unpaid"`.

```python
    def display_payment(self):
        # Display payment information
        print("Payment ID:", self.payment_id)
        print("Member ID:", self.member_id)
        print("Amount:", self.amount)
        print("Status:", self.status)
```
**What this does:** Prints all four pieces of payment information.

```python
    def mark_as_paid(self):
        # Change payment status to Paid
        self.status = "Paid"
        print("Payment successfully marked as paid. ")
```
**What this does:** Flips the status from `"Unpaid"` to `"Paid"`.

```python
    def get_amount(self):
        # Return payment amount
        return self.amount

    def get_status(self):
        # Return payment status
        return self.status
```
**What these do:** Getters that return the amount and the status.

---

### 4. `gym.py`: The manager

This is the "brain" of the system. It owns the lists and does the real work.

```python
from member import Member
from membership import Membership
from payment import Payment
```
**What this does:** Brings in the three blueprints from their files, so `Gym` can use them. `from member import Member` means "from the file `member.py`, grab the class `Member`".

```python
class Gym:
    """Manages the gym membership system."""
```
**What this does:** Declares the `Gym` class. The text in triple quotes right under it is a **docstring**, a short description of what the class is for.

```python
    def __init__(self, gym_name):
        self.gym_name = gym_name
        self.members = []
        self.memberships = []
        self.payments = []
```
**What this does:** When a gym is created, it gets a name and starts with **three empty lists**: one for members, one for plans, one for payments. `[]` means "an empty list".

#### Member management

```python
    def add_member(self, member):
        """Add a new member to the gym."""
        self.members.append(member)
        print("Member added successfully!")
```
**What this does:** `.append()` adds the member to the end of the members list, then confirms.

```python
    def display_members(self):
        """Display all registered gym members."""
        if not self.members:
            print("No members registered yet.")
        else:
            for member in self.members:
                member.display_member()
```
**What this does:** If the list is empty (`not self.members` is `True` for an empty list), it says so. Otherwise a `for` loop visits each member one by one and asks them to print themselves.

```python
    def search_member(self, member_id):
        """Search for a member using their ID."""
        for member in self.members:
            if member.get_member_id() == member_id:
                member.display_member()
                return member
        print("Member not found.")
        return None
```
**What this does:** Looks through every member. If one has a matching ID, it shows them and **returns** that member (which ends the method immediately). If the loop finishes without a match, it prints "Member not found." and returns `None` (Python's word for "nothing").

```python
    def remove_member(self, member_id):
        """Remove a member using their ID."""
        for member in self.members:
            if member.get_member_id() == member_id:
                self.members.remove(member)
                print("Member removed successfully!")
                return

        print("Member not found.")
```
**What this does:** Same search idea, but when it finds a match it deletes that member from the list with `.remove()`, confirms, and stops with `return`. If nothing matched, it says "Member not found."

#### Saving and loading

```python
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
```
**What this does, piece by piece:**
- `try:` / `except` = "try this, and if something goes wrong, handle it nicely instead of crashing."
- `open("members.txt", "w")` opens the file for **writing** (`"w"`). This wipes the old contents first, then writes fresh ones.
- `with ... as file:` opens the file and automatically closes it when finished, even if something goes wrong.
- For each member, it writes **one line** with their details separated by commas, e.g. `1234,john,20,9887`. The `f"..."` is an **f-string**: anything in `{ }` gets replaced by its value. `\n` ends the line.
- `OSError` catches problems like "no permission to write here" or "disk full".

```python
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
```
**What this does, piece by piece:**
- `open("members.txt", "r")` opens the file for **reading** (`"r"`).
- `self.members = []` clears the current list first so nothing is duplicated.
- `for line in file:` goes through the file one line at a time.
- `line.strip()` removes the invisible newline at the end. `.split(",")` chops the line at each comma into four pieces, and those are assigned to `member_id, name, age, phone` in one go.
- `int(age)` turns the age from text (`"20"`) into a real number (`20`).
- A new `Member` is built and added to the list.
- **Error handling:**
  - `FileNotFoundError`: first ever run, no file yet. Not a problem, just a friendly message.
  - `ValueError`: a line is damaged (wrong number of commas, or the age isn't a number).
  - `OSError`: some other file problem.

#### Membership plans and payments

```python
    def add_membership(self, membership):
        self.memberships.append(membership)
        print("Membership plan added successfully!")
```
**What this does:** Adds a plan to the plans list.

```python
    def display_memberships(self):
        if not self.memberships:
            print("No membership plans available.")
        else:
            print("\n--- Available Membership Plans ---")
            for membership in self.memberships:
                membership.display_plan()
```
**What this does:** Same pattern as showing members: "none yet" message if empty, otherwise a heading followed by every plan.

```python
    def add_payment(self, payment):
        self.payments.append(payment)
        print("Payment recorded successfully!")

    def display_payments(self):
        if not self.payments:
            print("No payments recorded yet.")
        else:
            print("\n--- Payment Records ---")
            for payment in self.payments:
                payment.display_payment()
```
**What these do:** `add_payment` stores a payment; `display_payments` prints all of them, or says there are none.

**Note:** In your original `gym.py`, `add_membership` appears **twice**, and there's also a `record_payment` method that does the same thing as `add_payment`. Python doesn't complain: the *second* `add_membership` simply replaces the first. You can safely delete the duplicates (see [limitations](#-things-to-know-current-limitations)).

---

### 5. `main.py`: The menu you interact with

```python
from gym import Gym
from member import Member
from membership import Membership
from payment import Payment
```
**What this does:** Imports the four classes `main.py` needs.

```python
gym = Gym("My Gym")
```
**What this does:** Creates one gym called "My Gym". Everything you do in the menu happens to this object.

```python
gym.load_members()
```
**What this does:** Reads `members.txt` right at the start so your saved members are back and ready.

```python
while True:
```
**What this does:** Starts an **endless loop**. The menu keeps coming back after every action until we deliberately `break` out of it (option 9).

```python
    print("\n================================")
    print(" GYM MEMBERSHIP MANAGEMENT")
    print("================================")
    print("1. Add a new member")
    ...
    print("9. Exit")

    choice = input("Choose an option (1-9): ")
```
**What this does:** Prints the menu, then `input()` waits for you to type something. Whatever you type is stored in `choice` **as text** (that's why the code compares to `"1"`, not `1`).

#### Option 1: Add a member

```python
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
```
**What this does:**
1. Asks for the ID and name (kept as text).
2. Asks for age and tries `int(...)` to convert it to a whole number. If you type "abc", Python raises a `ValueError`, which is caught and a friendly message shows.
3. If age is 0 or negative, it complains.
4. `continue` means "skip the rest and go back to the top of the menu", so bad input never creates a broken member.
5. Asks for phone (text, since phone numbers can have leading zeros or `+`).
6. Builds a `Member` and hands it to the gym.

#### Options 2, 3, 4: Show, search, remove

```python
    elif choice == "2":
        gym.display_members()

    elif choice == "3":
        member_id = input("Enter member ID to search: ")
        gym.search_member(member_id)

    elif choice == "4":
        member_id = input("Enter member ID to remove: ")
        gym.remove_member(member_id)
```
**What this does:** Short and sweet. The menu just collects the input and passes the job to the gym.

#### Option 5: Add a membership plan

```python
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
```
**What this does:** Same idea as adding a member. `float(...)` converts to a number that can have decimals (like `29.99`). Prices of zero or less are rejected.

#### Option 6: Show plans

```python
    elif choice == "6":
        gym.display_memberships()
```

#### Option 7: Record a payment

```python
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
```
**What this does:** Collects the payment details, checks the amount is a positive number, creates a `Payment` and gives it to the gym.

#### Option 8: Show payments

```python
    elif choice == "8":
        gym.display_payments()
```

#### Option 9: Save and exit

```python
    elif choice == "9":
        gym.save_members()
        print("Thank you for using My Gym!")
        break
```
**What this does:** Saves members to `members.txt`, says goodbye, and `break` jumps out of the `while True` loop. With nothing left to run, the program ends.

#### Anything else

```python
    else:
        print("Invalid choice. Please select a number from 1 to 9.")
```
**What this does:** If you type something that isn't 1 to 9 (like `hello` or `42`), you get a polite nudge and the menu returns.

> In the original code this last line ended with a curly quote `”)`. It must be a normal straight quote `")`, otherwise Python shows a `SyntaxError`.

---

### 6. `members.txt`: The saved data

```
1234,john,20,9887
```

One member per line, with four values separated by commas, always in this order:

```
member_id,name,age,phone
```

You don't have to create this file yourself. Choosing option 9 creates it. If you edit it by hand, keep exactly four values per line and make sure the age is a whole number, otherwise loading will fail for that file. **Don't put commas inside names**, since a comma is what separates the values.

---

## Some things to look out for or lacking

These aren't bugs that stop the program, just things to be aware of:

1. **Only members are saved.** Membership plans and payments live in memory only, so they **disappear** when you close the program.
2. **You must exit with option 9** to save. Closing the window or pressing `Ctrl+C` loses anything added this session.
3. **Duplicate IDs are allowed.** You can add two members with the same ID.
4. **Payments don't check the member exists.** You can record a payment for an ID that isn't registered.
5. **Payments always show "Unpaid".** The `mark_as_paid()` method exists but isn't in the menu yet.
6. **Duplicate code in `gym.py`.** `add_membership` is defined twice and `record_payment` duplicates `add_payment`. Harmless, but tidy it up if you like.
7. **Commas in names or phone numbers** would break the save file format.

---

## Some ideas for making it better

Great next steps if you want to keep learning:

- Add a menu option to **update a member's phone number** (the `update_phone` method is already waiting).
- Add a menu option to **mark a payment as paid** (`mark_as_paid` is ready).
- **Save and load plans and payments** too (copy the pattern from `save_members` / `load_members`, using `memberships.txt` and `payments.txt`).
- **Block duplicate member IDs** before adding.
- **Check the member exists** before recording a payment.
- Show **total money collected** by adding up `get_amount()` for every payment.
- Switch to **JSON** or **CSV** files, which handle commas and more complex data safely.
- Add **join dates** and **expiry dates** using Python's `datetime` module.

---

## Troubleshooting

| Error message | What it usually means | Fix |
|---|---|---|
| `IndentationError` | Spaces at the start of a line are wrong | Make sure code inside classes/functions/ifs is indented consistently (4 spaces) |
| `SyntaxError: invalid character` | Curly quotes `” “` were used | Replace them with straight quotes `"` |
| `ModuleNotFoundError: No module named 'gym'` | File is misnamed or in a different folder | Make sure `gym.py` is lowercase and sits next to `main.py` |
| `No saved members file found.` | First run, no `members.txt` yet | Totally normal! It's created when you exit with option 9 |
| `Error loading members: not enough values to unpack` | A line in `members.txt` is missing a value | Open the file and make sure each line has exactly 4 comma-separated values |
| `python` not recognised | Python isn't installed or not on PATH | Reinstall Python and tick "Add Python to PATH", or try `python3` |

---

Regards,

Rao Muhammad Ibrahim
