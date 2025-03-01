from controllers.customer_controller import CustomerController
from database.connection import Database


class BookingService:
    def __init__(self):
        db = Database()
        self.repository = CustomerController(db, None)

    def get_all_cars(self):
        return self.repository.get_all_cars_api()

    def get_all_additional_services(self):
        return self.repository.get_all_additional_services_api()
