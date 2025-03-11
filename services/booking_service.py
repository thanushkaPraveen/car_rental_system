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

    def create_a_booking(self, booking):
        return self.repository.create_a_booking_api(booking)

    def get_all_bookings(self, user_id):
        return self.repository.get_all_bookings_api(user_id)
