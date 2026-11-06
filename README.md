# Python Authentication System

A simple command-line program written in Python that simulates creating an account and logging in. I built it as part of learning Python and practicing loops, conditionals, and input validation.

## Features

- **Username validation:** letters only, at least 4 characters
- **Age check:**
  - 18 and above: standard account
  - 12 to 17: junior account
  - Under 12: account creation is blocked
- **Password rules:** minimum of 6 characters
- **Login:** asks for username and password, and keeps asking until both are correct

## How to run

1. Make sure Python 3 is installed
2. Download `Authentication.py`
3. Run it in your terminal:

   python Authentication.py

## What I practiced

- `while` loops and `break` / `continue`
- `if / elif / else` conditions
- String methods like `isalpha()` and `isdigit()`
- Taking and validating user input

## Limitations / future improvements

- Account details are only stored while the program is running (no file or database yet)
- Passwords are not hashed or encrypted
- Could be extended to support multiple users

## Author

Your Name | Computer Science student learning Python
