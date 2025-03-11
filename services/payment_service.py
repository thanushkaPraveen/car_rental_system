from controllers.invoice_payment_controller import InvoicePaymentController
from database.connection import Database


class PaymentService:
    def __init__(self):
        db = Database()
        self.repository = InvoicePaymentController(db, None)

    def get_all_invoices(self, user_id):
        return self.repository.get_all_invoices_api(user_id)
