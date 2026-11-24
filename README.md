# Gym Membership Management System

## About the Project

This is a simple Gym Membership Management System made using Python.

I created this project to make it easier for a gym to manage its members, membership plans and payments. Instead of keeping everything in a notebook, users can manage the information through a menu in the terminal.

The main goal of this project was to practise Python, learn how to use classes and objects, and understand how different Python files can work together.

## Table of Contents

1. [Project Features](#project-features)
2. [Requirements](#requirements)
3. [How to Set Up](#how-to-set-up)
4. [Project Structure](#project-structure)
5. [How to Use the Program](#how-to-use-the-program)
6. [How the Files Work Together](#how-the-files-work-together)
7. [Code Overview](#code-overview)
8. [Limitations](#limitations)
9. [Future Improvements](#future-improvements)
10. [Troubleshooting](#troubleshooting)

## Project Features

The program allows users to:

- Add new gym members.
- View all registered members.
- Search for members using their ID.
- Remove members from the system.
- Create membership plans.
- View available membership plans.
- Record member payments.
- View payment records.
- Save member information in a text file.
- Load saved member information when the program starts.

## Requirements

Before running the project, you need:

- **Python:** Version 3.6 or above.
- **Code editor:** PyCharm, VS Code or another Python editor.
- **Terminal:** To run the program.

I developed this project using Python and PyCharm on a MacBook.

## How to Set Up

Follow these steps to run the project on your computer.

### Step 1: Create a project folder

Create a new folder called `gym_project`.

### Step 2: Create the Python files

Inside the folder, create these files:

```text
gym_project/
│
├── main.py
├── gym.py
├── member.py
├── membership.py
├── payment.py
└── members.txt
```

The `members.txt` file can be created automatically when the program saves member information.

### Step 3: Add the code

Copy the correct Python code into each file.

Make sure the file names are correct because the files import information from each other.

### Step 4: Check your code

While working on this project, I sometimes faced indentation and syntax errors.

Make sure:
- Your indentation is correct.
- You use the correct quotation marks.
- Your file names are spelled correctly.
- Your code is saved.

### Step 5: Run the program

Open your terminal and enter:

```bash
cd gym_project
python main.py
```

If your Mac uses `python3`, enter:

```bash
python3 main.py
```

The main menu should appear.

## Project Structure

Each Python file has its own responsibility.

| File | Purpose |
|---|---|
| `main.py` | Displays the menu and handles user input. |
| `gym.py` | Manages members, plans and payments. |
| `member.py` | Stores information about gym members. |
| `membership.py` | Manages membership plans. |
| `payment.py` | Stores payment information. |
| `members.txt` | Saves member information. |

## How to Use the Program

When you run `main.py`, the following menu appears:

```text
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

Enter the number of the option you want and press Enter.

### Example 1: Adding a Member

```text
Choose an option (1-9): 1

Enter member ID: 1234
Enter member name: John
Enter member age: 20
Enter phone number: 9887

Member added successfully!
```

### Example 2: Searching for a Member

```text
Choose an option (1-9): 3

Enter member ID to search: 1234

--- Member Information ---
ID: 1234
Name: John
Age: 20
Phone: 9887
```

### Example 3: Adding a Membership Plan

```text
Enter membership plan name: Monthly
Enter membership duration: 1 month
Enter membership price: 30

Membership plan added successfully!
```

### Example 4: Recording a Payment

```text
Enter payment ID: P001
Enter member ID: 1234
Enter payment amount: 30

Payment recorded successfully!
```

### Exiting the Program

Choose option 9 to save the member information and close the program.

**Important:** Always exit using option 9 so your members are saved.

## How the Files Work Together

The files are connected and each one has a different job.

- `main.py` displays the menu and receives information from the user.
- `gym.py` receives the user's choices and manages the system.
- `member.py` stores member details.
- `membership.py` stores membership plan details.
- `payment.py` stores payment details.
- `members.txt` keeps member information saved between sessions.

For example, when someone adds a new member, `main.py` collects their information and creates a `Member` object. It then sends that object to `gym.py`, which adds it to the members list.

## Code Overview

While building this project, I learned about some important Python concepts.

| Python Concept | What I Learned |
|---|---|
| Classes | How to create blueprints for objects. |
| Objects | How to create individual members, plans and payments. |
| `self` | How an object accesses its own information. |
| `__init__` | How to initialise objects when they are created. |
| Methods | How to create functions inside classes. |
| Lists | How to store multiple members, plans and payments. |
| Loops | How to go through stored information. |
| If statements | How to make decisions in the program. |
| File handling | How to save and load information. |
| Exception handling | How to deal with errors without immediately stopping the program. |
| Imports | How to connect different Python files. |

### 1. member.py

This file contains the `Member` class.

It stores:
- Member ID
- Name
- Age
- Phone number

It also includes methods to display member information, update a phone number and return member details.

### 2. membership.py

This file contains the `Membership` class.

It stores:
- Plan name
- Membership duration
- Price

It also allows the program to display a plan, update its price and return membership information.

### 3. payment.py

This file contains the `Payment` class.

It stores:
- Payment ID
- Member ID
- Payment amount
- Payment status

New payments start with the status `Unpaid`. There is also a method to change the status to `Paid`.

### 4. gym.py

This file contains the `Gym` class.

It is responsible for managing the main parts of the system.

It includes methods to:
- Add members.
- Display members.
- Search for members.
- Remove members.
- Add membership plans.
- Display membership plans.
- Record payments.
- Display payments.
- Save and load member information.

### 5. main.py

This is the main file of the project.

It imports the classes from the other files, creates the gym and displays the menu.

It also receives the user's choices and calls the correct methods from `gym.py`.

### 6. members.txt

This file stores member information so it can be loaded again when the program starts.

For example:

```text
1234,John,20,9887
```

Each member is saved on a separate line.

The program creates this file automatically when member information is saved.

## Limitations

There are still a few things that could be improved in the project:

1. Only member information is saved. Membership plans and payments are not saved after closing the program.
2. Members need to exit using option 9 to save their information.
3. The program currently allows members to have the same ID.
4. Payments can be recorded without checking whether the member exists.
5. Payments start as unpaid, but the menu does not currently include an option to mark them as paid.
6. Names containing commas can cause problems when saving information in the text file.

These are some areas I would like to improve in the future.

## Future Improvements

If I continue developing this project, I would like to add:

- An option to update member information.
- An option to mark payments as paid.
- The ability to save and load membership plans and payments.
- A system to prevent duplicate member IDs.
- A check to make sure a member exists before recording a payment.
- A feature to calculate the total payments received.
- A better way to store information using JSON or a database.
- Membership joining and expiry dates.

## Troubleshooting

| Problem | Possible Solution |
|---|---|
| `IndentationError` | Check that your code uses consistent indentation. |
| `SyntaxError` | Check your brackets, quotation marks and spelling. |
| `ModuleNotFoundError` | Make sure all Python files are in the same folder and correctly named. |
| `No saved members file found` | This is normal when running the program for the first time. |
| `python` not recognised | Try running the program using `python3 main.py`. |

## Final Thoughts

Building this project helped me understand Python better, especially classes, objects, functions, lists and file handling.

I also learned how to split a larger program into smaller files instead of putting everything into one file.

This was a good learning experience and a chance to practise what I have learned in Python.

---

**Created by: Rao Muhammad Ibrahim**
