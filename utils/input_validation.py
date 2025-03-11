import re
from plistlib import InvalidFileException

import bcrypt
from datetime import datetime, timedelta

from attr import dataclass

from models.invalid_input_type_error import InvalidInputTypeError


def get_valid_integer(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt).strip())
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_number_plate():
    while True:
        number_plate = input("Enter Number Plate (e.g., ABC-1234): ").strip()
        if len(number_plate) >= 6:
            return number_plate
        else:
            print("Invalid number plate format. Please try again.")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty. Please try again.")

def get_non_empty_input_api(data):
    value = data.strip()
    if value:
        return value
    else:
        raise InvalidInputTypeError("This field cannot be empty. Please try again.")

def get_valid_float(prompt, min_value):
    while True:
        try:
            value = float(input(prompt).strip())
            if value > min_value:
                return value
            else:
                print(f"Please enter a number greater than {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_year(prompt, min_year, max_year):
    while True:
        try:
            year = int(input(prompt).strip())
            if min_year <= year <= max_year:
                return year
            else:
                print(f"Please enter a year between {min_year} and {max_year}.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

def get_valid_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_max_rental_period(min_rental_period):
    while True:
        max_rental_period = get_valid_positive_integer("Enter Maximum Rental Period (e.g., 30): ")
        if max_rental_period >= min_rental_period:
            return max_rental_period
        else:
            print("Maximum rental period must be greater than or equal to the minimum rental period.")

def get_valid_is_active(input_text = "Is the car active?"):
    while True:
        is_active = input(f"{input_text} (1 for Yes, 0 for No): ").strip()
        if is_active in {"0", "1"}:
            return int(is_active)
        else:
            print("Invalid input. Please enter 1 (Yes) or 0 (No).")

def get_user_confirmation():
    while True:
        confirmation = input("Do you want to proceed? (1 for Yes, 0 for No): ").strip()
        if confirmation in {"0", "1"}:
            return int(confirmation)
        else:
            print("Invalid input. Please enter 1 (Yes) to confirm or 0 (No) to cancel.")

def get_valid_is_status():
    while True:
        is_active = input("Is the car status? (1 for Available, 2 for Unavailable): ").strip()
        if is_active in {"1", "2"}:
            return int(is_active)
        else:
            print("Invalid input. Please enter 1 (Yes) or 0 (No).")

# Check for overlapping date ranges
def check_overlap(start1, end1, start2, end2):
    return max(start1, start2) <= min(end1, end2)

def get_valid_email():
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    while True:
        email = input("Enter your email address: ").strip()
        if re.match(email_pattern, email):
            return email
        else:
            print("Invalid email format. Please enter a valid email address.")

def get_valid_email_api(user_email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    email = user_email.strip()
    if re.match(email_pattern, email):
        return email
    else:
        raise InvalidInputTypeError("Invalid email format. Please enter a valid email address.")


def get_valid_user_type():
    while True:
        is_active = input("Enter User Type ID (e.g., 1 for Admin, 2 for Regular User):").strip()
        if is_active in {"1", "2"}:
            return int(is_active)
        else:
            print("Invalid input. Please enter 1 (Yes) or 2 (No).")

def get_valid_user_type_api(user_type):
    data = user_type.strip()
    if data in {"1", "2"}:
        return int(data)
    else:
        raise InvalidInputTypeError("Invalid input. Please enter 1 (Yes) or 2 (No).")


def hash_password(password: str) -> str:
    """Hashes the password using bcrypt and returns the hashed password."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Store as a string in DB

def verify_password(input_password: str, stored_hashed_password: str) -> bool:
    """Compares the input password with the stored hashed password."""
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))

def get_valid_phone_number():
    """Prompts user to enter a valid phone number and validates it."""
    phone_pattern = r'^\+?[0-9]{7,15}$'  # Allows optional "+" at the start and 7-15 digits

    while True:
        phone_number = input("Enter your phone number: ").strip()
        if re.match(phone_pattern, phone_number):
            return phone_number  # Valid number
        else:
            print("Invalid phone number. Please enter a valid number (7-15 digits, optional +).")

def get_valid_phone_number_api(user_phone_number):
    """Prompts user to enter a valid phone number and validates it."""
    phone_pattern = r'^\+?[0-9]{7,15}$'  # Allows optional "+" at the start and 7-15 digits
    phone_number = user_phone_number.strip()
    if re.match(phone_pattern, phone_number):
        return phone_number  # Valid number
    else:
        raise InvalidInputTypeError("Invalid phone number. Please enter a valid number (7-15 digits, optional +).")



def get_future_date():
    """
    Prompts the user to enter a valid future date in 'YYYY-MM-DD' format.
    Ensures the input is a valid date and is in the future.

    Returns:
        datetime: A valid future date as a datetime object.
    """
    while True:
        try:
            # Get the start date from the user in "YYYY-MM-DD" format
            start_date_str = input("Enter Start Date (YYYY-MM-DD): ").strip()
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

            # Check if the entered date is in the future
            if start_date > datetime.now():
                print(f"Valid future date entered: {start_date.strftime('%Y-%m-%d')}")
                return start_date
            else:
                print("Error: The date must be in the future. Please enter a valid future date.")
        except ValueError:
            print("Invalid format! Please enter the date in 'YYYY-MM-DD' format.")


def get_user_selection():
    """Prompts the user to enter service IDs and returns a list of valid integers."""
    while True:
        user_input = input("\nEnter the IDs of the services you want to select (comma-separated): ")
        try:
            selected_ids = [int(id.strip()) for id in user_input.split(",")]
            return selected_ids
        except ValueError:
            print("Invalid input. Please enter numeric IDs separated by commas.")


def calculate_days_difference(start_date, end_date):
    """
    Calculate the difference in days between two Unix timestamps.

    :param start_date: Unix timestamp for the start date
    :param end_date: Unix timestamp for the end date
    :return: The difference in days
    """
    start_datetime = datetime.utcfromtimestamp(start_date)
    end_datetime = datetime.utcfromtimestamp(end_date)
    return (end_datetime - start_datetime).days

