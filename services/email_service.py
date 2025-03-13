import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.message import EmailMessage

from constants import Constants
from utils.datetime_utils import format_timestamp


class EmailService:

    def __init__(self):
        # Email credentials
        self.smtp_server = "smtp.gmail.com"  # Change based on your email provider
        self.smtp_port = 465  # For SSL
        self.sender_email = "praveen.tpw@gmail.com"
        # self.receiver_email = "thanushkawickramarachchi@gmail.com"
        self.password = "fdgxknstjmrchbkv"  # Use an app password for security
        # Send the email using SSL
        self.context = ssl.create_default_context()

    def send(self, receiver_email, subject, body):
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        # Email body
        body = "Here is the body of my message."
        msg.attach(MIMEText(body, "plain"))

        # # Send the email using SSL
        # context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context= self.context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def send_car_booking_email(self, customer, booking, car, additional_services=None):
        """
        Sends a car booking confirmation email, including additional services if booked.
        """

        # Email sender details
        sender_email = self.sender_email
        sender_password = self.password

        # Email Subject
        subject = f"Your Car Booking Details - {booking.booking_id}"

        # Email Body - Main Details
        email_body = f"""
        Dear {customer.user_name},

        Thank you for booking with us! Here are your booking details:

        Booking ID: {booking.booking_id}
        Car Model: {car["brand_model_name"]}
        Car Brand: {car["brand_name"]}
        Pickup Date: {format_timestamp(booking.start_date)}
        Return Date: {format_timestamp(booking.end_date)}
        Total Price: {booking.total_amount}

        """

        # Add Additional Services if Booked
        if additional_services:
            email_body += "Additional Services Booked:\n"
            for service in additional_services:
                email_body += f"\t  - {service.services_description}\n"

        # Footer
        email_body += """

        Please ensure to carry your valid driving license and ID during pickup.

        If you have any questions, feel free to contact our support team.

        Safe travels!
        Best Regards,
        Car Rental Team
        """

        # Creating Email Message
        msg = EmailMessage()
        msg.set_content(email_body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = customer.user_email

        user_email = "thanushkawickramarachchi@gmail.com"

        # Sending the email
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, user_email, msg.as_string())
            print("------------------------------------------------------")
            print("Please check your email regarding the booking details.")
            print("------------------------------------------------------")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def send_car_booking_email_api(self, customer, booking, car, additional_services=None):
        """
        Sends a car booking confirmation email, including additional services if booked.
        """

        # Email sender details
        sender_email = self.sender_email
        sender_password = self.password

        # Email Subject
        subject = f"Your Car Booking Details - {booking.booking_id}"

        # Email Body - Main Details
        email_body = f"""
        Dear {customer.user_name},

        Thank you for booking with us! Here are your booking details:

        Booking ID: {booking.booking_id}
        Car Model: {car.model_name}
        Car Brand: {car.model_name}
        Pickup Date: {format_timestamp(booking.start_date)}
        Return Date: {format_timestamp(booking.end_date)}
        Total Price: {booking.total_amount}

        """

        # Add Additional Services if Booked
        if additional_services:
            email_body += "Additional Services Booked:\n"
            for service in additional_services:
                email_body += f"\t  - {service.services_description}\n"

        # Footer
        email_body += """

        Please ensure to carry your valid driving license and ID during pickup.

        If you have any questions, feel free to contact our support team.

        Safe travels!
        Best Regards,
        Car Rental Team
        """

        # Creating Email Message
        msg = EmailMessage()
        msg.set_content(email_body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = customer.user_email

        user_email = "thanushkawickramarachchi@gmail.com"

        # Sending the email
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, user_email, msg.as_string())
        except Exception as e:
            print(f"Failed to send email: {e}")

    def send_car_invoice_email(self, customer, invoice, booking, additional_services=None):
        """
        Sends a car booking confirmation email, including additional services if booked.
        """

        # Email sender details
        sender_email = self.sender_email
        sender_password = self.password

        # Email Subject
        subject = f"Invoice ID: {invoice["invoice_id"]} - Invoice Details."

        # Email Body - Main Details
        email_body = f"""
        Dear {customer["user_name"]},

        Please find the invoice for your booking details:
        
        ==========================================
                          INVOICE
        ==========================================
        
        Invoice Number: {invoice["invoice_id"]}
        Invoice Date: {format_timestamp(invoice["updated_at"])}
        
        ------------------------------------------
        Itemized Details:
        ------------------------------------------

        Booking ID: {booking.booking_id}
        Pickup Date: {format_timestamp(booking.start_date)}
        Return Date: {format_timestamp(booking.end_date)}
        Total Price: {booking.total_amount}

        """

        # Add Additional Services if Booked
        if additional_services:
            email_body += "Additional Services Booked:\n"
            for service in additional_services:
                email_body += f"\t  - {service["service_description"]}          {service["service_amount"]}\n"

        # Footer
        email_body += f"""
        ------------------------------------------

        Total Amount: {invoice["amount"]}
        Amount Paid:  $0.00
        Balance Due:  {invoice["amount"]}
        
        ------------------------------------------
        Payment Method:
        Visa / Credit Card
        
        Payment URL: {Constants.PAYMENT_URL}{invoice["invoice_id"]}

        If you have any questions, feel free to contact our support team.

        Safe travels!
        Best Regards,
        Car Rental Team
        """

        # Creating Email Message
        msg = EmailMessage()
        msg.set_content(email_body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = customer["user_email"]

        user_email = "thanushkawickramarachchi@gmail.com"

        # Sending the email
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, customer["user_email"], msg.as_string())
            print("Please check your email regarding the booking details.")
        except Exception as e:
            print(f"Failed to send email: {e}")
