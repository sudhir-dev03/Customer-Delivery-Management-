from flask import Blueprint, request, jsonify

from services.order_service import process_order, assign_driver_service
order_bp = Blueprint(
    'order_bp',
    __name__
)
from services.order_service import (
    process_order,
    assign_driver_service,
    update_status_service
)

@order_bp.route('/create-order',
                methods=['POST'])
def create_order_route():

    data = request.json

    phone = data["phone"]
    product = data["product"]
    quantity = data["quantity"]

    order_id = process_order(
        phone,
        product,
        quantity
    )

    return jsonify({
        "message": "Order Created",
        "order_id": order_id
    })

@order_bp.route('/assign-driver',
                methods=['POST'])
def assign_driver_route():

    data = request.json

    order_id = data["order_id"]
    driver_name = data["driver_name"]

    assign_driver_service(
        order_id,
        driver_name
    )

    return jsonify({
        "message": "Driver Assigned Successfully"
    })
@order_bp.route('/update-status',
                methods=['POST'])
def update_status_route():

    data = request.get_json()

    order_id = data["order_id"]
    status = data["status"]

    update_status_service(
        order_id,
        status
    )

    return jsonify({
        "message": "Status Updated Successfully"
    })
