from models.order_model import create_order, assign_driver
from services.twilio_service import send_sms
from utils.helpers import generate_order_id
from models.order_model import update_status
def process_order(phone, product, quantity):

    order_id = generate_order_id()

    create_order(
        order_id,
        phone,
        product,
        quantity
    )

    send_sms(
        phone,
        f"Order Received. Order ID: {order_id}"
    )

    return order_id
def assign_driver_service(order_id, driver_name):

    assign_driver(
        order_id,
        driver_name
    )

    return True
def update_status_service(order_id, status):

    update_status(
        order_id,
        status
    )

    return True