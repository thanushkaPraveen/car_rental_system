from controllers.manage_bookings_controller import ManageBookingController
from database.connection import Database


class AppService:
    def __init__(self):
        db = Database()
        self.admin_repo = ManageBookingController(db)

    def update_booking_status(self, booking_id, status):
        return self.admin_repo.update_booking_status_api(booking_id, status)
