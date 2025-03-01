from models.error_model import ErrorModel
from models.invalid_input_type_error import InvalidInputTypeError
from models.response_model import ResponseModel
from models.user import User
from utils.input_validation import *


class UserController:
    def __init__(self, db):
        self.db = db

    def login_or_register(self):

        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            return self.login()
        elif choice == "2":
            return self.register()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.\n\n")
            return True

    def login(self):
        """Handles user login by validating credentials."""
        user_email = get_valid_email()
        user_password = get_non_empty_input("Enter your password: ")

        # user_email = "admin@admin.com" # TODO
        # user_password = "admin" # TODO

        # Fetch user details from the database
        check_user = User.find_by_email_and_password(self.db, user_email)

        if check_user and len(check_user) == 1:
            stored_hashed_password = check_user[0].user_password
            if verify_password(user_password, stored_hashed_password):
                print("✅ Login successful!")
                return check_user[0]  # Return user object
            else:
                print("❌ Invalid password. Please try again.")
        else:
            print("❌ User not found. Please check your email and try again.")

        return None  # Return None instead of True for failed login

    def login_api(self, email, password):
        """Handles user login by validating credentials."""
        user_email = email
        user_password = password

        # Fetch user details from the database
        check_user = User.find_by_email_and_password(self.db, user_email)

        if check_user and len(check_user) == 1:
            stored_hashed_password = check_user[0].user_password
            if verify_password(user_password, stored_hashed_password):
                return ResponseModel.create(check_user[0]).to_dict()
            else:
                return ResponseModel.create("❌ Invalid password. Please try again.", is_error=True)
        else:
            return ResponseModel.create("❌ Invalid password. Please try again.", is_error=True)

    def register(self):

        # Register
        print("\n-- Register --")
        user_type_id = get_valid_user_type()
        user_name = get_non_empty_input("Enter your name: ")
        user_email = get_valid_email()

        check_user = User.find_by_email_and_password(self.db, user_email)

        if len(check_user) > 0:
            print("Errr: Entered email is already registered")
            return True

        user_phone_number = get_valid_phone_number()
        user_password = get_non_empty_input("Enter your password: ")
        user_password = user_password.strip()
        hashed_password = hash_password(user_password)

        if user_type_id in (1, 2):
            register_user = User(user_type_id=user_type_id, user_name=user_name,
                                 user_email=user_email, user_phone_number=user_phone_number,
                                 user_password=hashed_password, is_active=1)

            return User.insert(self.db, register_user)
        else:
            print("Errr: Entered User Type is Wrong")
            return True

    def register_api(self, user):
        try:
            user_type_id = get_valid_user_type_api(user["user_type_id"])
            user_name = get_non_empty_input_api(user["user_name"])
            user_email = get_valid_email_api(user["user_email"])

            check_user = User.find_by_email_and_password(self.db, user_email)

            if len(check_user) > 0:
                return ResponseModel.create("Errr: Entered email is already registered.", is_error=True).to_dict()

            user_phone_number = get_valid_phone_number_api(user["user_phone_number"])
            user_password = get_non_empty_input_api(user["user_password"])
            user_password = user_password.strip()
            hashed_password = hash_password(user_password)

            if user_type_id in (1, 2):
                register_user = User(user_type_id=user_type_id, user_name=user_name,
                                     user_email=user_email, user_phone_number=user_phone_number,
                                     user_password=hashed_password, is_active=1)

                return ResponseModel.create(User.insert(self.db, register_user)).to_dict()
            else:
                return ResponseModel.create("Errr: Entered User Type is Wrong.", is_error=True)
        except InvalidInputTypeError as e:
            return ResponseModel.create(e.message, is_error=True, code=400).to_dict()
        except Exception as e:
            return ResponseModel.create("Unknown server error.", is_error=True, code=400).to_dict()
