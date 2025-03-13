import time

from select import select
from tabulate import tabulate

from constants import Constants
from database.sql_statement import *
from res.string_resources import StringResources


class Invoice:
    def __init__(self, booking_id, user_id, amount, payment_method=None, payment_date=None, is_paid=0, is_active=1,
                 invoice_id=None):
        self.booking_id = booking_id
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_date = payment_date
        self.is_paid = is_paid
        self.is_active = is_active
        self.invoice_id = invoice_id  # Will be set after insertion in the database

    @staticmethod
    def insert(db, invoice):
        sql = INSERT_INVOICE
        values = (invoice.booking_id, invoice.user_id, invoice.amount, invoice.payment_method, invoice.payment_date,
                  invoice.is_paid, invoice.is_active, int(time.time()), int(time.time()))
        added_id = db.add_to_database(sql, values)
        invoice.invoice_id = added_id
        return invoice

    @staticmethod
    def update(db, invoice):
        sql = UPDATE_INVOICE
        values = (invoice.booking_id, invoice.user_id, invoice.amount, invoice.payment_method, invoice.payment_date,
                  invoice.is_paid, invoice.is_active, int(time.time()), invoice.invoice_id)
        db.update_database(sql, values)
        print(f"Invoice with ID {invoice.invoice_id} updated.")

    @staticmethod
    def deactivate(db, invoice):
        sql = UPDATE_INVOICE
        is_active = 0
        values = (invoice.booking_id, invoice.user_id, invoice.amount, invoice.payment_method, invoice.payment_date,
                  is_active, invoice.is_active, int(time.time()), invoice.invoice_id)
        db.update_database(sql, values)
        print(f"Invoice with ID {invoice.invoice_id} deactivated.")

    @staticmethod
    def delete(db, invoice):
        sql = DELETE_INVOICE
        values = (invoice.invoice_id,)
        db.delete_from_database(sql, values)
        print(f"Invoice with ID {invoice.invoice_id} deleted.")

    @staticmethod
    def select(db, invoice=None):
        sql = SELECT_ALL_INVOICES if invoice is None else SELECT_INVOICE_BY_ID
        values = (invoice.invoice_id,) if invoice else None
        rows = db.select_from_database(sql, values)

        # for row in rows:
        #     print(row)

        # Create a list to hold Invoice objects
        invoices = []
        for row in rows:
            # Assuming `row` is a tuple in the format:
            # (invoice_id, booking_id, user_id, amount, payment_method, payment_date, is_paid, is_active, ...)
            invoice_obj = Invoice(
                booking_id=row[1],  # Assuming `booking_id` is the second column
                user_id=row[2],  # Assuming `user_id` is the third column
                amount=row[3],  # Assuming `amount` is the fourth column
                payment_method=row[4],  # Assuming `payment_method` is the fifth column
                payment_date=row[5],  # Assuming `payment_date` is the sixth column
                is_paid=row[6],  # Assuming `is_paid` is the seventh column
                is_active=row[7],  # Assuming `is_active` is the eighth column
                invoice_id=row[0]  # Assuming `invoice_id` is the first column
            )
            invoices.append(invoice_obj)

        return invoices

    @staticmethod
    def fetch_all_user_invoices(db):
        sql = SELECT_ALL_USER_INVOICES
        values = None
        rows = db.select_from_database(sql, values)

        invoices = []
        for row in rows:
            invoice_details = {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_id": row[2],
                "amount": row[3],
                "payment_method": row[4],
                "payment_date": row[5],
                "is_paid": bool(row[6]),
                "is_active": bool(row[7]),
                "start_date": row[8],
                "end_date": row[9],
                "car_number_plate": row[10],
                "car_daily_rate": row[11],
                "user_name": row[12],
                "user_email": row[13],
                "user_phone_number": row[14],
            }
            invoices.append(invoice_details)

        return invoices

    @staticmethod
    def display_all_user_invoices(db):
        invoices = Invoice.fetch_all_user_invoices(db)

        if not invoices:
            print("No invoices available.")
            return

        headers = [
            "Invoice ID", "Booking ID", "User ID", "User Name", "User Email",
            "Car Number Plate", "Start Date", "End Date", "Amount",
            "Payment Method", "Payment Date", "Is Paid"
        ]

        rows = []
        for invoice in invoices:
            rows.append([
                invoice["invoice_id"],
                invoice["booking_id"],
                invoice["user_id"],
                invoice["user_name"],
                invoice["user_email"],
                invoice["car_number_plate"],
                time.strftime('%Y-%m-%d', time.localtime(invoice["start_date"]))
                if invoice["start_date"] else "N/A",
                time.strftime('%Y-%m-%d', time.localtime(invoice["end_date"])),
                f"${invoice['amount']:.2f}",
                invoice["payment_method"] if invoice["payment_method"] else "N/A",
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(invoice["payment_date"]))
                if invoice["payment_date"] else "N/A",
                "Yes" if invoice["is_paid"] else "No"
            ])

        print(StringResources.get(Constants.PRINT_INVOICE_DETAILS))
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        return invoices

    @staticmethod
    def fetch_user_invoices(db, user_id):
        sql = SELECT_ALL_INVOICES_FOR_USER
        rows = db.select_from_database(sql, (user_id,))

        invoices = []
        for row in rows:
            invoice_details = {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_id": row[2],
                "amount": row[3],
                "payment_method": row[4],
                "payment_date": row[5],
                "is_paid": bool(row[6]),
                "is_active": bool(row[7]),
                "start_date": row[8],
                "end_date": row[9],
                "car_number_plate": row[10],
                "car_daily_rate": row[11],
                "user_name": row[12],
                "user_email": row[13],
                "user_phone_number": row[14],
            }
            invoices.append(invoice_details)

        return invoices

    @staticmethod
    def fetch_all_invoices_for_admin(db):
        sql = SELECT_ALL_INVOICES_FOR_ALL
        rows = db.select_from_database(sql, ())

        invoices = []
        for row in rows:
            invoice_details = {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_id": row[2],
                "amount": row[3],
                "payment_method": row[4],
                "payment_date": row[5],
                "is_paid": bool(row[6]),
                "is_active": bool(row[7]),
                "start_date": row[8],
                "end_date": row[9],
                "car_number_plate": row[10],
                "car_daily_rate": row[11],
                "user_name": row[12],
                "user_email": row[13],
                "user_phone_number": row[14],
            }
            invoices.append(invoice_details)

        return invoices

    @staticmethod
    def display_user_invoices(db, user_id):
        invoices = Invoice.fetch_user_invoices(db, user_id)

        if not invoices:
            print(f"No invoices found for user ID {user_id}.")
            return

        headers = [
            "Invoice ID", "Booking ID", "Amount", "Payment Method", "Payment Date",
            "Is Paid", "Car Number Plate", "Start Date", "End Date"
        ]

        rows = []
        for invoice in invoices:
            rows.append([
                invoice["invoice_id"],
                invoice["booking_id"],
                f"${invoice['amount']:.2f}",
                invoice["payment_method"] if invoice["payment_method"] else "N/A",
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(invoice["payment_date"]))
                if invoice["payment_date"] else "N/A",
                "Yes" if invoice["is_paid"] else "No",
                invoice["car_number_plate"],
                time.strftime('%Y-%m-%d', time.localtime(invoice["start_date"]))
                if invoice["start_date"] else "N/A",
                time.strftime('%Y-%m-%d', time.localtime(invoice["end_date"]))
                if invoice["end_date"] else "N/A"
            ])

        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        pass

    @classmethod
    def get_invoice_by_invoice_id(cls, db, query, invoice_id):
        """
        Return invoice by invoice Id.
        """
        sql = query
        values = (invoice_id,)
        rows = db.select_from_database(sql, values)

        invoices = [
            {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_id": row[2],
                "amount": row[3],
                "payment_method": row[4],
                "payment_date": row[5],
                "is_paid": row[6],
                "updated_at": row[9],
            }
            for row in rows
        ]

        return None if not invoices else invoices[0]

    @classmethod
    def get_invoice_by_booking_id(cls, db, query, booking_id):
        """
        Return invoice by invoice Id.
        """
        sql = query
        values = (booking_id,)
        rows = db.select_from_database(sql, values)

        invoices = [
            {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_id": row[2],
                "amount": row[3],
                "payment_method": row[4],
                "payment_date": row[5],
                "is_paid": row[6],
                "create_at": row[8],
                "updated_at": row[9]
            }
            for row in rows
        ]

        return None if not invoices else invoices[0]

    @classmethod
    def get_invoiceuser_by_invoice_id(cls, db, query, invoice_id):
        """
        Return invoice by invoice Id.
        """
        sql = query
        values = (invoice_id,)
        rows = db.select_from_database(sql, values)

        invoices = [
            {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_id": row[2],
                "amount": row[3],
                "payment_method": row[4],
                "payment_date": row[5],
                "is_paid": row[6],
                "number_plate": row[10],
                "daily_rate": row[11],
                "user_name": row[12],
                "user_email": row[13],
                "user_phone_number": row[14],
            }
            for row in rows
        ]

        return None if not invoices else invoices[0]

    @classmethod
    def retrieve_invoice_by_invoice_id(cls, db, invoice_id):
        return Invoice.get_invoice_by_invoice_id(db, SELECT_INVOICE_BY_ID, invoice_id)

    @classmethod
    def retrieve_invoice_for_payments(cls, db, invoice_id):
        return Invoice.get_invoiceuser_by_invoice_id(db, SELECT_ALL_INVOICES_FOR_PAYMENT, invoice_id)

    @classmethod
    def display_invoice_by_invoice_id(cls, db, invoice_id):
        """
        Fetch invoice by invoice id and print invoice details.
        """

        invoice = Invoice.get_invoice_by_invoice_id(db, SELECT_INVOICE_BY_ID, invoice_id)
        if not invoice:
            print("No invoices found.")
            return invoice

        all_invoices = [invoice]
        table_data_all_invoices = [
            [
                idx + 1,
                invoice["invoice_id"],
                booking["booking_id"],
                booking["user_id"],
                booking["amount"],
                booking["payment_method"],
                booking["payment_date"],
                booking["is_paid"],
            ]
            for idx, booking in enumerate(all_invoices)
        ]

        headers = [
            "Index", "Invoice ID", "Booking Id", "User Id", "Total Amount", "Payment Method",
            "Payment Method", "Payment Date", "Is Paid"
        ]
        print(tabulate(table_data_all_invoices, headers=headers, tablefmt="fancy_grid"))

        return invoice

    @classmethod
    def update_payment_confirm(cls, db, invoice_id, payment_method, payment_date):
        invoice = Invoice.retrieve_invoice_by_invoice_id(db, invoice_id)

        updated_invoice = Invoice(invoice_id=invoice["invoice_id"],
                                  booking_id=invoice["booking_id"],
                                  user_id=invoice["user_id"],
                                  amount=invoice["amount"],
                                  payment_method=payment_method,
                                  payment_date=payment_date,
                                  is_paid=1, is_active=1)
        Invoice.update(db, updated_invoice)
        return Invoice.retrieve_invoice_by_invoice_id(db, invoice_id)
        pass

    @staticmethod
    def fetch_all_invoices(db):
        sql = SELECT_ALL_INVOICES_WITH_USERS
        values = ()
        rows = db.select_from_database(sql, values)

        list = []
        for row in rows:
            data = {
                "invoice_id": row[0],
                "booking_id": row[1],
                "user_name": row[2],
                "user_email": row[3],
                "amount": row[4],
                "payment_method": row[5],
                "payment_date": row[6],
                "is_paid": row[7],
            }
            list.append(data)

        return list

    @staticmethod
    def display_all_invoices(db):
        data = Invoice.fetch_all_invoices(db)

        if not data:
            print("No invoices available.")
            return

        headers = [
            "Invoice ID","Booking ID", "User Name", "User Email", "Amount", "Payment Method", "Is Paid"
        ]

        rows = []
        for invoice in data:
            rows.append([
                invoice["invoice_id"],
                invoice["booking_id"],
                invoice["user_name"],
                invoice["user_email"],
                invoice["amount"],
                invoice["payment_method"],
                "Paid" if invoice["is_paid"] else "Pending",
            ])

        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        return data