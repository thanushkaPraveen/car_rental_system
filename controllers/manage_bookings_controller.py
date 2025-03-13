from constants import Constants
from controllers.base_controller import BaseController
from database.sql_statement import SELECT_INVOICES_BY_BOOKING_ID, SELECT_ADDITIONAL_SERVICES_BY_BOOKING_ID
from models.additional_services import AdditionalServices
from models.booking import Booking
from models.invoice import Invoice
from models.response_model import ResponseModel
from models.user import User
from presenter.user_interface import UiTypes
from services.email_service import EmailService


class ManageBookingController(BaseController):

    def __init__(self, db):
        super().__init__(db)

    def _view_all_bookings(self):
        print("Viewing all bookings...")
        Booking.display_all_bookings(self.db)
        self.display_menu()

    def _view_requested_bookings(self):
        print("Viewing all requested bookings...")

        Booking.display_all_requested_bookings(self.db)
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS),
                              Constants.CALLBACK_REQUEST_BOOKING_ID)

    def _view_booking_details(self, booking_id):
        print("Viewing booking details...")

        booking = Booking.retrieve_booking_by_booking_id(self.db, booking_id)

        if not booking:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS_RETRY),
                                  Constants.CALLBACK_REQUEST_BOOKING_ID)
            return

        if Booking.check_overlapped_bookings(self.db, booking):
            self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_BOOKING_VEHICLE_NOT_AVAILABLE))
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_ENTER_CHOICE_REJECT),
                                  Constants.CALLBACK_REQUEST_BOOKING_REJECT, booking_id)
        else:
            self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_BOOKING_DETAILS))
            booking = Booking.display_booking_by_booking_id(self.db, booking_id)
            if not booking:
                self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                      self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_SEE_DETAILS_RETRY),
                                      Constants.CALLBACK_REQUEST_BOOKING_ID)
            else:
                self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_ADDITIONAL_SERVICE_DETAILS))
                AdditionalServices.display_additional_services_by_booking_id(self.db, booking_id)
                self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                      self.string_resource.get(Constants.PRINT_ENTER_CHOICE_CONFIRM_OR_REJECT),
                                      Constants.CALLBACK_REQUEST_BOOKING_CONFIRM_AND_REJECT, booking_id)

    def _send_email(self, booking_id):
        print("Sending invoice details...")
        user = User.get_user_by_booking_id(self.db, booking_id)
        booking = Booking.select(self.db, booking_id)
        services = AdditionalServices.get_additional_services_by_booking_id(self.db, SELECT_ADDITIONAL_SERVICES_BY_BOOKING_ID, booking_id)
        invoice = Invoice.get_invoice_by_booking_id(self.db, SELECT_INVOICES_BY_BOOKING_ID, booking_id)

        send_email = EmailService()
        send_email.send_car_invoice_email(customer=user, invoice=invoice, booking=booking[0], additional_services=services)
        self.ui.press_any_key_to_continue()
        pass

    def on_input_callback(self, callback_type, choice, params=None):
        if callback_type == Constants.CALLBACK_NAVIGATION:
            self._menu_navigation(choice)
        elif callback_type == Constants.CALLBACK_REQUEST_BOOKING_ID:
            self._view_booking_details(choice)
        elif callback_type == Constants.CALLBACK_REQUEST_BOOKING_CONFIRM_AND_REJECT:
            self._booking_confirm_navigation(choice, params)
        elif callback_type == Constants.CALLBACK_REQUEST_BOOKING_REJECT:
            self._booking_reject_navigation(choice, params)
        else:
            self.ui.display(UiTypes.ERROR, "Error this input callback not mapped..")

    def on_back_callback(self, data=None):
        pass

    def _menu_navigation(self, choice):
        if choice == 1:
            self._view_all_bookings()
        elif choice == 2:
            self._view_requested_bookings()
        elif choice == 3:
            self._nav_home()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_INPUT_INVALID_1_3),
                                  Constants.CALLBACK_NAVIGATION)

    def _nav_home(self):
        self.ui.clear_console()
        self.notify_callback()
        self.remove_callback()

    def display_menu(self):
        self.ui.display(UiTypes.MESSAGE,
                        self.string_resource.get(Constants.PRINT_MANAGE_BOOKING_MAIN))
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_ENTER_CHOICE_INPUT_1_3),
                              Constants.CALLBACK_NAVIGATION)

    def _booking_confirm_navigation(self, choice, booking_id):
        if choice == 1 or choice == 2:
            booking = Booking.update_booking_by_booking_id(self.db, booking_id, choice)
            # Create Invoice
            invoice = Invoice(booking_id=booking.booking_id, user_id=booking.user_id,
                              amount=booking.total_amount,
                              is_paid=0, is_active=1)
            Invoice.insert(self.db, invoice)
            if choice == 1:
                self._send_email(booking_id)
            self.display_menu()
        elif choice == 3:
            self.display_menu()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_INPUT_INVALID_1_3),
                                  Constants.CALLBACK_REQUEST_BOOKING_CONFIRM_AND_REJECT, booking_id)

    def _booking_reject_navigation(self, choice, booking_id):
        if choice == 1:
            Booking.update_booking_by_booking_id(self.db, booking_id, choice)
        elif choice == 2:
            self.display_menu()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_INPUT_INVALID_1_2),
                                  Constants.CALLBACK_NAVIGATION)

    def update_booking_status_api(self, booking_id, status):
        try:
            if status == 1 or status == 2:
                booking = Booking.update_booking_by_booking_id(self.db, booking_id, status)
                # Create Invoice
                invoice = Invoice(booking_id=booking.booking_id, user_id=booking.user_id,
                                  amount=booking.total_amount,
                                  is_paid=0, is_active=1)
                new_invoice = Invoice.insert(self.db, invoice)
                if status == 1:
                    self._send_email(booking_id)
                return ResponseModel.create(new_invoice).to_dict()
        except IndexError as e:
            print(e)
            return ResponseModel.create(message="Entered booking id not found.", is_error=True, code=400).to_dict()
        except Exception as e:
            print(e)
            return ResponseModel.create(message="Required fields missing.", is_error=True, code=400).to_dict()
