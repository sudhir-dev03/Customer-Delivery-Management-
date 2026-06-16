from flask import Flask
from flask import render_template
from flask import Flask, render_template, request
from flask import Flask, render_template, request
from flask import request, redirect

from routes.order_routes import order_bp
from routes.sms_routes import sms_bp

from models.order_model import get_all_orders
from models.order_model import (
    get_all_orders,
    get_order_by_id
)

app = Flask(__name__)

app.register_blueprint(order_bp)
app.register_blueprint(sms_bp)

@app.route('/')
def home():

    data = get_all_orders()

    total_orders = len(data)

    pending_orders = len(
        [o for o in data if o["status"] == "Pending"]
    )

    delivered_orders = len(
        [o for o in data if o["status"] == "Delivered"]
    )
    assigned_orders = len(
    [o for o in data if o["status"] == "Assigned"]
)

    return render_template(
        "dashboard.html",
        total_orders=total_orders,
        pending_orders=pending_orders,
        assigned_orders=assigned_orders,
        delivered_orders=delivered_orders

    )
@app.route('/track-order/<order_id>')
def track_order(order_id):

    order = get_order_by_id(order_id)

    return render_template(
        'track_order.html',
        order=order
    )
@app.route('/orders')
def orders():

    data = get_all_orders()

    return render_template(
        'orders.html',
        orders=data
    )
@app.route('/place-order')
def place_order():

    return render_template(
        'place_order.html'
    )

@app.route('/search')
def search():

    order_id = request.args.get('order_id')

    order = None

    if order_id:
        order = get_order_by_id(order_id)

    return render_template(
        'search.html',
        order=order
    )
@app.route('/admin')
def admin():

    data = get_all_orders()

    return render_template(
        'admin.html',
        orders=data
    )
@app.route('/assign/<order_id>')
def assign_page(order_id):

    return render_template(
        'assign_driver.html',
        order_id=order_id
    )

@app.route('/assign-driver-ui',
           methods=['POST'])
def assign_driver_ui():

    order_id = request.form['order_id']
    driver_name = request.form['driver_name']

    from services.order_service import assign_driver_service

    assign_driver_service(
        order_id,
        driver_name
    )
    return redirect('/admin')    

@app.route('/deliver/<order_id>')
def deliver_order(order_id):

    from services.order_service import update_status_service

    update_status_service(
        order_id,
        "Delivered"
    )

    return redirect('/admin')    

    return redirect('/admin')

if __name__ == "__main__":
    app.run(debug=True)