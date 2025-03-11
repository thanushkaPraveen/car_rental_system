from fastapi import APIRouter

from services.payment_service import PaymentService

router = APIRouter()
controller = PaymentService()


@router.post("/get-all-invoices")
def get_all_invoices(user: dict):
    return controller.get_all_invoices(user["user_id"])
