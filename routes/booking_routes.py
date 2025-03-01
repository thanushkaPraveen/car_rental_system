from fastapi import APIRouter

from services.booking_service import BookingService

router = APIRouter()
controller = BookingService()

@router.get("/get-all-cars")
def get_all_cars():
    return controller.get_all_cars()

@router.get("/get-all-additional-services")
def get_all_additional_services():
    return controller.get_all_additional_services()