import time

from constants import Constants
from controllers.base_controller import BaseController
from controllers.invoice_payment_controller import InvoicePaymentController
from controllers.my_bookings_controller import MyBookingsController
from models.additional_services import AdditionalServices
from models.booking import Booking
from models.booking_additional_services import BookingAdditionalServices
from models.car import Car
from models.response_model import ResponseModel

from presenter.user_interface import UserInterface, UiTypes
from services.email_service import EmailService
from services.sms import Sms
from utils.input_validation import *


class CustomerController(BaseController):

    def __init__(self, db, customer):
        super().__init__(db)
        self.customer = customer

    def select_car(self):
        selected_services = []
        print("Selecting a car...")

        try:
            cars = Car.select_with_details_and_display(self.db)

            selected_car =  cars[get_valid_integer(f"Enter Selected Car Index (1-{len(cars)}): ", 1, len(cars)) - 1]
            booking_days = get_valid_integer(f"How many days would you like to book? (Choose between {selected_car["min_rental_period"]} and {selected_car["max_rental_period"]} days):", int(selected_car["min_rental_period"]), int(selected_car["max_rental_period"]))
            start_date = get_future_date()
            # Calculate the end date by adding `booking_days` to the start date
            end_date = start_date + timedelta(days=booking_days)
            # Format start and end dates as Unix timestamps
            start_date_timestamp = int(start_date.timestamp())
            end_date_timestamp = int(end_date.timestamp())

            # Get only "yes" or "no" for additional services
            if get_valid_is_active(input_text= "Do you want to add additional services?"):
                # Fetch additional services from the database
                all_services = AdditionalServices.display_additional_services(self.db)
                selected_services =  self.select_services(all_services)

            # Display details
            print(f"\nBooking Details:")
            print(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
            print(f"End Date: {end_date.strftime('%Y-%m-%d')}")
            print(f"Number of Days: {booking_days}")
            print(f"Car Number Plate: {selected_car['number_plate']}")
            print(f"Car Brand: {selected_car['brand_name']}")
            print(f"Car Model: {selected_car['brand_model_name']}")

            total = float(selected_car['daily_rate']) *  booking_days
            print( f"\nDaily rate({selected_car['daily_rate']}) x booking_days({booking_days}) = {total}")

            if selected_services:
                for service in selected_services:
                    total += service.services_amount
                    print(f"{service.services_description} = {service.services_amount:.2f}")  # Format float for display

            print(f"Total = {total:.2f}")

            if get_valid_is_active(input_text="Do you want to confirm your booking?"):
                note = input("Enter a note for the booking (optional, press Enter to skip): ").strip()
                booking_status = 2 # Pending
                new_booking = Booking(user_id=self.customer.user_id ,
                                      car_id= selected_car["car_id"],
                                      booking_status_id=booking_status,
                                      start_date=start_date_timestamp,
                                      end_date=end_date_timestamp,
                                      total_amount=total,
                                      note=note,
                                      is_active=1)
                booking = Booking.insert(self.db, new_booking)

                if selected_services:
                    for service in selected_services:
                        booking_additional_services = BookingAdditionalServices(booking_id=booking.booking_id,
                                                                                additional_services_id=service.additional_services_id,
                                                                                is_active=1)

                        BookingAdditionalServices.insert(self.db, booking_additional_services)

                send_sms = Sms()
                send_sms.send_sms(booking.booking_id)

                self.ui.clear_console()
                send_email = EmailService()
                send_email.send_car_booking_email(customer=self.customer, booking=booking, car=selected_car, additional_services=selected_services)
                self.ui.press_any_key_to_continue()
                self.ui.clear_console()
                self.display_menu()

        except Exception as e:
            # Handle the exception
            print(f"An error occurred: {e}")

    def get_all_cars_api(self):
        try:
            return ResponseModel.create(Car.select_with_details_and_display(self.db)).to_dict()

        except Exception as e:
            ResponseModel.create(f"An error occurred: {e}", is_error=True).to_dict()

    def get_all_additional_services_api(self):
        try:
            return AdditionalServices.display_additional_services(self.db)

        except Exception as e:
            ResponseModel.create(f"An error occurred: {e}", is_error=True).to_dict()

    def select_services(self, all_services):
        """Loops until the user selects valid services."""
        while True:
            selected_ids = get_user_selection()

            selected_services = [service for service in all_services
                                 if service.additional_services_id in selected_ids]

            if not selected_services or len(selected_ids) != len(selected_services):
                print("No valid services selected. Please try again.")
                continue

            # Valid services selected, break the loop
            break

        return selected_services

    def my_bookings(self):
        print("Viewing booked car...")
        my_bookings_controller = MyBookingsController(self.db, self.customer)
        my_bookings_controller.add_callback(self.on_back_callback)
        my_bookings_controller.display_menu()

    def manage_booking(self):
        print("Managing booking...")

    def invoice_payment(self):
        print("Viewing invoice...")
        invoice_payment_controller = InvoicePaymentController(self.db, self.customer)
        invoice_payment_controller.add_callback(self.on_back_callback)
        invoice_payment_controller.display_menu()

    def logout(self):
        print("Logging out...")

    def display_menu(self):
        self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_MANAGE_CUSTOMER_MAIN_1))
        user_details = f"Name: {self.customer.user_name} \nEmail: {self.customer.user_email}"
        self.ui.display(UiTypes.MESSAGE, user_details)
        self.ui.display(UiTypes.MESSAGE, self.string_resource.get(Constants.PRINT_MANAGE_CUSTOMER_MAIN_2))
        self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                              self.string_resource.get(Constants.PRINT_ENTER_CHOICE_INPUT_1_4),
                              Constants.CALLBACK_NAVIGATION)


    def on_input_callback(self, callback_type, choice, params=None):
        if callback_type == Constants.CALLBACK_NAVIGATION:
            self.menu_navigation(choice)
        else:
            self.ui.display(UiTypes.ERROR, "Error this input callback not mapped....")
        pass

    def on_back_callback(self, data=None):
        self.display_menu()
        pass

    def menu_navigation(self, choice):
        if choice == 1:
            self.select_car()
        elif choice == 2:
            self.my_bookings()
        elif choice == 3:
            self.invoice_payment()
        elif choice == 4:
            self.logout()
        else:
            self.ui.display_input(UiTypes.REQUEST_INT_INPUT,
                                  self.string_resource.get(Constants.PRINT_MANAGE_INPUT_INVALID_1_4),
                                  Constants.CALLBACK_NAVIGATION)
