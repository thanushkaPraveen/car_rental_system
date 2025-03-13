import time

from tabulate import tabulate

from database.sql_statement import *


class User:
    def __init__(self, user_type_id, user_name, user_email, user_phone_number, user_password, is_active=1, user_id=None):
        self.user_type_id = user_type_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_phone_number = user_phone_number
        self.user_password = user_password
        self.is_active = is_active
        self.user_id = user_id  # Will be set after insertion in the database

    @staticmethod
    def insert(db, user):
        sql = INSERT_USER
        values = (user.user_type_id, user.user_name, user.user_email, user.user_phone_number, user.user_password,
                  user.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        user.user_id = added_id
        return user

    @staticmethod
    def update(db, user):
        sql = UPDATE_USER
        values = (user.user_name, user.user_email, user.user_phone_number, user.user_password,
                  user.is_active, int(time.time()), user.user_id)
        db.update_database(sql, values)
        print(f"User with ID {user.user_id} updated.")

    @staticmethod
    def deactivate(db, user):
        sql = UPDATE_USER
        is_active = 0
        values = (user.user_name, user.user_email, user.user_phone_number, user.user_password,
                  is_active, int(time.time()), user.user_id)
        db.update_database(sql, values)
        print(f"User with ID {user.user_id} deactivated.")

    @staticmethod
    def delete(db, user):
        sql = DELETE_USER
        values = (user.user_id,)
        db.delete_from_database(sql, values)
        print(f"User with ID {user.user_id} deleted.")

    @staticmethod
    def select(db, user=None):
        sql = SELECT_ALL_USERS if user is None else SELECT_USER_BY_ID
        values = (user.user_id,) if user else None
        rows = db.select_from_database(sql, values)

        # for row in rows:
        #     print(row)

        users = []
        for row in rows:
            user = User(
                user_id=row[0],  # First column: user_id
                user_type_id=row[1],  # Second column: user_type_id
                user_name=row[2],  # Third column: user_name
                user_email=row[3],  # Fourth column: user_email
                user_phone_number=row[4],  # Fifth column: user_phone_number
                user_password=row[5],  # Sixth column: user_password
                is_active=row[6]  # Seventh column: is_active
            )

            # Add the created User object to the list
            users.append(user)

        return users

    @staticmethod
    def select_user_by_user_id(db, user_id):
        sql = SELECT_ALL_USERS if user_id is None else SELECT_USER_BY_ID
        values = (user_id,)
        rows = db.select_from_database(sql, values)

        # for row in rows:
        #     print(row)

        users = []
        for row in rows:
            user = User(
                user_id=row[0],  # First column: user_id
                user_type_id=row[1],  # Second column: user_type_id
                user_name=row[2],  # Third column: user_name
                user_email=row[3],  # Fourth column: user_email
                user_phone_number=row[4],  # Fifth column: user_phone_number
                user_password=row[5],  # Sixth column: user_password
                is_active=row[6]  # Seventh column: is_active
            )

            # Add the created User object to the list
            users.append(user)

        return users

    @staticmethod
    def find_by_email_and_password(db, user_email, user_password=None):
        sql = ""
        values = ()
        if user_password is None:
            sql = FIND_USER_BY_EMAIL
            values = (user_email,)
        else:
            sql = FIND_USER_BY_EMAIL_AND_PASSWORD
            values = (user_email,user_password)

        rows = db.select_from_database(sql, values)

        users = []
        for row in rows:

            user = User(
                user_id=row[0],  # First column: user_id
                user_type_id=row[1],  # Second column: user_type_id
                user_name=row[2],  # Third column: user_name
                user_email=row[3],  # Fourth column: user_email
                user_phone_number=row[4],  # Fifth column: user_phone_number
                user_password=row[5],  # Sixth column: user_password
                is_active=row[6]  # Seventh column: is_active
            )

            # Add the created User object to the list
            users.append(user)

        return users

    @staticmethod
    def fetch_all_users(db):
        sql = FIND_USER_BY_USER_TYPE
        values = ("User", )
        rows = db.select_from_database(sql, values)

        users = []
        for row in rows:
            user = {
                "user_id": row[0],
                "user_name": row[1],
                "user_email": row[2],
                "user_phone_number": row[3],
            }
            users.append(user)

        return users

    @staticmethod
    def display_all_users(db):
        users = User.fetch_all_users(db)

        if not users:
            print("No users available.")
            return

        headers = [
            "User ID", "User Name", "User Email", "User Phone Number"
        ]

        rows = []
        for user in users:
            rows.append([
                user["user_id"],
                user["user_name"],
                user["user_email"],
                user["user_phone_number"],
            ])

        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        return users

    @staticmethod
    def get_user_by_booking_id(db, booking_id):
        sql = FIND_USER_BY_BOOKING_ID
        values = (booking_id, )
        rows = db.select_from_database(sql, values)

        users = []
        for row in rows:
            user = {
                "user_id": row[0],
                "user_name": row[1],
                "user_email": row[2],
                "user_phone_number": row[3],
            }
            users.append(user)

        return users[0]

