import time

from tabulate import tabulate

from database.sql_statement import *
from utils.datetime_utils import format_timestamp
from utils.input_validation import check_overlap


class Booking:
    def __init__(self, user_id, car_id, booking_status_id, start_date, end_date, total_amount, note, is_active=1,
                 booking_id=None):
        self.user_id = user_id
        self.car_id = car_id
        self.booking_status_id = booking_status_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_amount = total_amount
        self.note = note
        self.is_active = is_active
        self.booking_id = booking_id

    def __str__(self):
        return (f"Booking ID: {self.booking_id}, User ID: {self.user_id}, Car ID: {self.car_id}, "
                f"Booking Status ID: {self.booking_status_id}, Start Date: {self.start_date}, "
                f"End Date: {self.end_date}, Total Amount: {self.total_amount}, Note: {self.note}, "
                f"Is Active: {self.is_active}")

    @staticmethod
    def insert(db, booking):
        sql = INSERT_BOOKING
        values = (booking.user_id, booking.car_id, booking.booking_status_id, booking.start_date, booking.end_date,
                  booking.total_amount, booking.note, booking.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        booking.booking_id = added_id
        return booking

    @staticmethod
    def update(db, booking):
        sql = UPDATE_BOOKING
        values = (booking.user_id, booking.car_id, booking.booking_status_id, booking.start_date,
                  booking.end_date, booking.total_amount, booking.note, booking.is_active, int(time.time()),
                  booking.booking_id)
        db.update_database(sql, values)
        # print(f"Booking with ID {booking.booking_id} updated.")

    @staticmethod
    def deactivate(db, booking):
        sql = UPDATE_BOOKING
        is_active = 0
        values = (booking.user_id, booking.car_id, booking.booking_status_id, booking.start_date,
                  booking.end_date, booking.total_amount, booking.note, is_active, int(time.time()), booking.booking_id)
        db.update_database(sql, values)
        print(f"Booking with ID {booking.booking_id} deactivated.")

    @staticmethod
    def delete(db, booking):
        sql = DELETE_BOOKING
        values = (booking.booking_id,)
        db.delete_from_database(sql, values)
        print(f"Booking with ID {booking.booking_id} deleted.")

    @staticmethod
    def select(db, booking_id=None):
        sql = SELECT_ALL_BOOKINGS if booking_id is None else SELECT_BOOKING_BY_ID
        values = (booking_id,) if booking_id else None
        rows = db.select_from_database(sql, values)

        '''
        for row in rows:
            print(row)
        '''

        # Create a list to hold Booking objects
        bookings = []
        for row in rows:
            # Assuming `row` is a tuple in the format:
            # (booking_id, user_id, car_id, booking_status_id, start_date, end_date, total_amount, note, is_active, ...)
            booking_obj = Booking(
                user_id=row[1],  # Assuming `user_id` is the second column
                car_id=row[2],  # Assuming `car_id` is the third column
                booking_status_id=row[3],  # Assuming `booking_status_id` is the fourth column
                start_date=row[4],  # Assuming `start_date` is the fifth column
                end_date=row[5],  # Assuming `end_date` is the sixth column
                total_amount=row[6],  # Assuming `total_amount` is the seventh column
                note=row[7],  # Assuming `note` is the eighth column
                is_active=row[8],  # Assuming `is_active` is the ninth column
                booking_id=row[0]  # Assuming `booking_id` is the first column
            )
            bookings.append(booking_obj)

        return bookings

    @staticmethod
    def get_bookings_by_user_id(db, user_id):
        """
        Fetch bookings and related data by user ID.
        """
        sql = SELECT_BOOKINGS_AND_DETAILS_BY_USER_ID
        values = (user_id,)
        rows = db.select_from_database(sql, values)

        bookings = [
            {
                "booking_id": row[0],
                "start_date": row[1],
                "end_date": row[2],
                "total_amount": row[3],
                "note": row[4],
                "number_plate": row[5],
                "model_name": row[6],
                "daily_rate": row[7],
                "year": row[8],
                "status": row[9],
                "user_name": row[10],
                "user_email": row[11],
            }
            for row in rows
        ]

        return bookings

    @staticmethod
    def get_bookings(db, query):
        """
        Fetch all active bookings and order by updated at.
        """
        sql = query
        values = ()
        rows = db.select_from_database(sql, values)

        bookings = [
            {
                "booking_id": row[0],
                "start_date": row[1],
                "end_date": row[2],
                "total_amount": row[3],
                "note": row[4],
                "number_plate": row[5],
                "model_name": row[6],
                "daily_rate": row[7],
                "year": row[8],
                "status": row[9],
                "user_name": row[10],
                "user_email": row[11],
            }
            for row in rows
        ]

        return bookings

    @staticmethod
    def get_booking_by_booking_id(db, query, booking_id):
        """
        Fetch all active bookings and order by updated at.
        """
        sql = query
        values = (booking_id,)
        rows = db.select_from_database(sql, values)

        bookings = [
            {
                "booking_id": row[0],
                "start_date": row[1],
                "end_date": row[2],
                "total_amount": row[3],
                "note": row[4],
                "number_plate": row[5],
                "model_name": row[6],
                "daily_rate": row[7],
                "year": row[8],
                "status": row[9],
                "user_name": row[10],
                "user_email": row[11],
            }
            for row in rows
        ]

        return None if not bookings else bookings[0]

    @staticmethod
    def display_bookings_by_user_id(db, user_id):
        """
        Display bookings and related data for a specific user.
        """
        bookings = Booking.get_bookings_by_user_id(db, user_id)

        if not bookings:
            print("No bookings found for this user.")
            return

        table_data = [
            [
                idx + 1,
                booking["booking_id"],
                booking["start_date"],
                booking["end_date"],
                booking["total_amount"],
                booking["status"],
                booking["number_plate"],
                booking["model_name"],
                booking["daily_rate"],
                booking["year"],
                booking["user_name"],
                booking["user_email"],
                booking["note"],
            ]
            for idx, booking in enumerate(bookings)
        ]

        headers = [
            "Index", "Booking ID", "Start Date", "End Date", "Total Amount", "Status",
            "Number Plate", "Model Name", "Daily Rate", "Year", "User Name", "User Email", "Note"
        ]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        return bookings

    @staticmethod
    def display_all_bookings(db):
        """
        Fetch all bookings and order by updated at.
        """
        bookings = Booking.get_bookings(db, SELECT_ALL_BOOKINGS_ORDER_BY_ASC)
        if not bookings:
            print("No bookings found.")
            return

        table_data = [
            [
                idx + 1,
                booking["booking_id"],
                format_timestamp(booking["start_date"]),
                format_timestamp(booking["end_date"]),
                booking["total_amount"],
                booking["status"],
                booking["number_plate"],
                booking["model_name"],
                booking["daily_rate"],
                booking["year"],
                booking["user_name"],
                booking["user_email"],
                booking["note"],
            ]
            for idx, booking in enumerate(bookings)
        ]

        headers = [
            "Index", "Booking ID", "Start Date", "End Date", "Total Amount", "Status",
            "Number Plate", "Model Name", "Daily Rate", "Year", "User Name", "User Email", "Note"
        ]

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        return bookings

    @staticmethod
    def display_all_requested_bookings(db):
        """
        Fetch all bookings and order by updated at.
        """
        bookings = Booking.get_bookings(db, SELECT_ALL_PENDING_BOOKINGS_ORDER_BY_ASC)
        if not bookings:
            print("No bookings found.")
            return

        table_data = [
            [
                idx + 1,
                booking["booking_id"],
                format_timestamp(booking["start_date"]),
                format_timestamp(booking["end_date"]),
                booking["total_amount"],
                booking["status"],
                booking["number_plate"],
                booking["model_name"],
                booking["daily_rate"],
                booking["year"],
                booking["user_name"],
                booking["user_email"],
                booking["note"],
            ]
            for idx, booking in enumerate(bookings)
        ]

        overlap_rows = set()
        for i in range(len(table_data)):
            for j in range(i + 1, len(table_data)):
                start1 = table_data[i][2]
                end1 = table_data[i][3]
                number_plate1 = table_data[i][6]
                start2 = table_data[j][2]
                end2 = table_data[j][3]
                number_plate2 = table_data[j][6]

                if check_overlap(start1, end1, start2, end2) and number_plate1 == number_plate2:
                    overlap_rows.add(i)
                    overlap_rows.add(j)

        # Highlight overlapping rows in red
        highlighted_table = []
        for idx, row in enumerate(table_data):
            if row[5] == 'Pending':
                if idx in overlap_rows:
                    # Add ANSI escape code for red color
                    highlighted_row = [f"\033[91m{cell}\033[0m" for cell in row]
                    highlighted_table.append(highlighted_row)
                else:
                    highlighted_table.append(row)

        headers = [
            "Index", "Booking ID", "Start Date", "End Date", "Total Amount", "Status",
            "Number Plate", "Model Name", "Daily Rate", "Year", "User Name", "User Email", "Note"
        ]

        print(tabulate(highlighted_table, headers=headers, tablefmt="fancy_grid"))
        return bookings

    @classmethod
    def retrieve_booking_by_booking_id(cls, db, booking_id):
        return Booking.get_booking_by_booking_id(db, SELECT_BOOKING_BY_BOOKING_ID, booking_id)

    @classmethod
    def check_overlapped_bookings(cls, db, booking):
        """
        Fetch booking by booking id and check for overlapping bookings.
        """

        all_bookings = Booking.get_bookings(db, SELECT_ALL_PENDING_BOOKINGS_ORDER_BY_ASC)
        table_data_all_bookings = [
            [
                idx + 1,
                booking["booking_id"],
                booking["start_date"],
                booking["end_date"],
                booking["total_amount"],
                booking["status"],
                booking["number_plate"],
                booking["model_name"],
                booking["daily_rate"],
                booking["year"],
                booking["user_name"],
                booking["user_email"],
                booking["note"],
            ]
            for idx, booking in enumerate(all_bookings)
        ]

        if not booking:
            print("Bookings is required.")
            return False

        for i in range(len(table_data_all_bookings)):
            id1 = table_data_all_bookings[i][1]
            start1 = table_data_all_bookings[i][2]
            end1 = table_data_all_bookings[i][3]
            status1 = table_data_all_bookings[i][5]
            number_plate1 = table_data_all_bookings[i][6]

            id2 = booking["booking_id"]
            start2 = booking["start_date"]
            end2 = booking["end_date"]
            status2 = booking["status"]
            number_plate2 = booking["number_plate"]

            if id1 != id2 and check_overlap(start1, end1, start2, end2) and number_plate1 == number_plate2 and (status1 == "Confirmed" or status2 == "Confirmed"):
                return True

        return False

    @classmethod
    def display_booking_by_booking_id(cls, db, booking_id):
        """
        Fetch booking by booking id.
        """

        booking = Booking.get_booking_by_booking_id(db, SELECT_BOOKING_BY_BOOKING_ID, booking_id)
        if not booking:
            print("No bookings found.")
            return booking

        all_bookings = [booking]
        table_data_all_bookings = [
            [
                idx + 1,
                booking["booking_id"],
                booking["start_date"],
                booking["end_date"],
                booking["total_amount"],
                booking["status"],
                booking["number_plate"],
                booking["model_name"],
                booking["daily_rate"],
                booking["year"],
                booking["user_name"],
                booking["user_email"],
                booking["note"],
            ]
            for idx, booking in enumerate(all_bookings)
        ]

        headers = [
            "Index", "Booking ID", "Start Date", "End Date", "Total Amount", "Status",
            "Number Plate", "Model Name", "Daily Rate", "Year", "User Name", "User Email", "Note"
        ]
        print(tabulate(table_data_all_bookings, headers=headers, tablefmt="fancy_grid"))

        return booking

    @classmethod
    def update_booking_by_booking_id(cls, db, booking_id, choice):
        """
        Update booking by booking id.
        """
        booking = Booking.select(db, booking_id)[0]
        if not booking:
            print("No bookings found.")
            return
        if choice == 1:
            booking.booking_status_id = 1
            booking.update(db, booking)
        else:
            booking.booking_status_id = 3
            booking.update(db, booking)
        return booking
