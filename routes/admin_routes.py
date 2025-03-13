from fastapi import APIRouter

from services.app_service import AppService

router = APIRouter()
controller = AppService()


@router.post("/update-booking-status")
def update_booking_status(booking: dict):
    return controller.update_booking_status(booking["booking_id"], booking["status"])
