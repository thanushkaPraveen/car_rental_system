import time

from tabulate import tabulate

from database.sql_statement import *


class AdditionalServices:
    """
    Represents additional services that can be added to bookings.
    """

    def __init__(self, services_description, services_amount, is_active=1, additional_services_id=None):
        """
        Initializes an AdditionalService object.

        :param services_description: Description of the service.
        :param services_amount: Cost of the service.
        :param is_active: Status of the service (1 = Active, 0 = Inactive).
        :param additional_services_id: Unique identifier for the service (optional).
        """
        self.services_description = services_description
        self.services_amount = services_amount
        self.is_active = is_active
        self.additional_services_id = additional_services_id

    @staticmethod
    def insert(db, service):
        """
        Inserts a new additional service into the database.

        :param db: Database connection object.
        :param service: AdditionalServices object to be inserted.
        :return: The inserted AdditionalServices object with an updated ID.
        """
        sql = INSERT_ADDITIONAL_SERVICE
        values = (
            service.services_description, service.services_amount, service.is_active, int(time.time()), int(time.time())
        )
        added_id = db.add_to_database(sql, values)
        service.additional_services_id = added_id
        return service

    @staticmethod
    def update(db, service):
        """
        Updates an existing additional service in the database.

        :param db: Database connection object.
        :param service: AdditionalServices object with updated values.
        """
        sql = UPDATE_ADDITIONAL_SERVICE
        values = (service.services_description, service.services_amount, service.is_active, int(time.time()),
                  service.additional_services_id)
        db.update_database(sql, values)
        print(f"AdditionalService with ID {service.additional_services_id} updated.")

    @staticmethod
    def deactivate(db, service):
        """
        Deactivates an additional service by setting its status to inactive.

        :param db: Database connection object.
        :param service: AdditionalServices object to be deactivated.
        """
        sql = UPDATE_ADDITIONAL_SERVICE
        is_active = 0
        values = (service.services_description, service.services_amount, is_active, int(time.time()),
                  service.additional_services_id)
        db.update_database(sql, values)
        print(f"AdditionalService with ID {service.additional_services_id} deactivated.")

    @staticmethod
    def delete(db, service):
        """
        Deletes an additional service from the database.

        :param db: Database connection object.
        :param service: AdditionalServices object to be deleted.
        """
        sql = DELETE_ADDITIONAL_SERVICE
        values = (service.additional_services_id,)
        db.delete_from_database(sql, values)
        print(f"AdditionalService with ID {service.additional_services_id} deleted.")

    @staticmethod
    def select(db, service=None):
        """
        Retrieves additional services from the database.

        :param db: Database connection object.
        :param service: Optional AdditionalServices object to filter by ID.
        :return: List of AdditionalServices objects.
        """
        sql = SELECT_ALL_ADDITIONAL_SERVICES if service is None else SELECT_ADDITIONAL_SERVICE_BY_ID
        values = (service.additional_services_id,) if service else None
        rows = db.select_from_database(sql, values)

        additional_services = []
        for row in rows:
            service_obj = AdditionalServices(
                services_description=row[1],
                services_amount=row[2],
                is_active=row[3],
                additional_services_id=row[0]
            )
            additional_services.append(service_obj)

        return additional_services

    @staticmethod
    def select_by_service_id(db, service_id):
        """
        Retrieves additional services from the database.

        :param db: Database connection object.
        :param service: Optional AdditionalServices object to filter by ID.
        :return: List of AdditionalServices objects.
        """
        sql = SELECT_ALL_ADDITIONAL_SERVICES if service_id is None else SELECT_ADDITIONAL_SERVICE_BY_ID
        values = (service_id,)
        rows = db.select_from_database(sql, values)

        additional_services = []
        for row in rows:
            service_obj = AdditionalServices(
                services_description=row[1],
                services_amount=row[2],
                is_active=row[3],
                additional_services_id=row[0]
            )
            additional_services.append(service_obj)

        return additional_services

    @staticmethod
    def get_additional_services_by_booking_id(db, query, booking_id):
        """
        Fetches additional services associated with a specific booking ID.

        :param db: Database connection object.
        :param query: SQL query for fetching services.
        :param booking_id: Booking ID to filter services.
        :return: List of additional services associated with the booking.
        """
        sql = query
        values = (booking_id,)
        rows = db.select_from_database(sql, values)

        services = [
            {
                "additional_service_id": row[5],
                "service_description": row[7],
                "service_amount": row[8],
            }
            for row in rows
        ]

        return services

    @classmethod
    def display_additional_services_by_booking_id(cls, db, booking_id):
        """
        Displays additional services for a given booking ID in a tabular format.

        :param db: Database connection object.
        :param booking_id: Booking ID for filtering services.
        """
        services = AdditionalServices.get_additional_services_by_booking_id(db,
                                                                            SELECT_ADDITIONAL_SERVICES_BY_BOOKING_ID,
                                                                            booking_id)
        if not services:
            print("No additional services found.")
            return
        table_data = [
            [
                idx + 1,
                service["additional_service_id"],
                service["service_description"],
                service["service_amount"],
            ]
            for idx, service in enumerate(services)
        ]
        headers = [
            "Index", "Additional Service ID", "Service Description", "Amount"
        ]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        return services

    def display_additional_services(db):
        """
        Displays all available additional services in a structured format.

        :param db: Database connection object.
        """
        all_services = AdditionalServices.select(db)
        if not all_services:
            print("\nNo additional services available.")
            return

        print("\nAvailable Additional Services:")
        print(f"{'ID':<5} {'Description':<30} {'Amount':<10} {'Status':<10}")
        print("-" * 60)

        for service in all_services:
            status = "Active" if service.is_active else "Inactive"
            print(
                f"{service.additional_services_id:<5} {service.services_description:<30} {service.services_amount:<10} {status:<10}"
            )
        return all_services
